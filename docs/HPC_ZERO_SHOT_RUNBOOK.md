# HPC zero-shot runbook

Use this for the preliminary frozen-checkpoint experiments on IMDb and DBLP.
Commands run from the MOTIF repository root in Bash. GPU allocation is handled
separately. The inference commands need a CUDA GPU; preparation and reporting
can run on CPU. No training or optimizer updates occur.

If IMDb preprocessing is already complete and your environment is active,
start at **step 4** after restoring the environment exports in step 1.

## 1. Restore the environment in each GPU job

Use your cluster's actual module names for Python 3.10, GCC and CUDA 12.1.
The GCC 12.2 module below matches the compiler in the reported HPC build log.
With the lazy native-extension import described below, Triton inference does not
require switching to GCC 11. Retain the working module versions from your setup.
If `.venv/` does not exist yet, complete step 2 after loading the modules and
entering the repository, then return to the activation and exports below.

```bash
module load python/3.10
module load gcc/12.2
module load cuda/12.1

cd /nfs/hpc/share/tinw/idealab/MOTIF
source .venv/bin/activate

export CC="$(command -v gcc)"
export CXX="$(command -v g++)"
export TORCH_CUDA_ARCH_LIST="9.0"  # H100
export TORCH_EXTENSIONS_DIR="$PWD/.cache/torch_extensions_cu121_h100"
export TRITON_CACHE_DIR="$PWD/.cache/triton"
export MAX_JOBS=4
export PYTHONHASHSEED=0
export CUBLAS_WORKSPACE_CONFIG=:4096:8
export PYTHONUNBUFFERED=1

mkdir -p logs "$TORCH_EXTENSIONS_DIR" "$TRITON_CACHE_DIR"
```

The architecture setting above is for H100. If using another GPU, use its
appropriate architecture and a separate extension-cache directory.

The local `motif/rspmm/__init__.py` loads the bundled C++/CUDA extension only when
`generalized_rspmm` is called. Importing the Triton modules does not build that
extension. This changes import timing; the model, checkpoint, Lift and Triton
kernels are unchanged. Sync this file to the HPC along with the adapter.
Keep the compiler module available for Triton's own compilation support.
The native backend still needs a compatible GCC/nvcc setup if explicitly used.

## 2. One-time venv setup, if needed

Skip this if dependencies are already installed. After loading the modules and
entering the repository, create the venv if it does not exist:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

python -m pip install numpy==1.26.4
python -m pip install torch==2.1.0 --index-url https://download.pytorch.org/whl/cu121
python -m pip install --only-binary=:all: torch-scatter==2.1.2 torch-sparse==0.6.18 -f https://data.pyg.org/whl/torch-2.1.0+cu121.html
python -m pip install -r requirements-eval.txt
```

Use the CUDA build above for inference. The CPU-only Torch installation in the
preprocessing guide is intended for a separate CPU preprocessing environment.

## 3. Prepare the raw data once

Expected layout:

```text
rai-datasets/
  raw/
    IMDB/movie_metadata.csv
    DBLP/{author_label.txt,paper_author.txt,paper_conf.txt,paper_term.txt}
  preprocessed/
    IMDB/          # adapter-ready export
    DBLP/          # adapter-ready export
    _build/        # intermediate splits and graph.pt bundles
```

Place the raw files yourself, then prepare the desired task:

```bash
mkdir -p rai-datasets/raw/IMDB rai-datasets/raw/DBLP

# IMDb Movie-Year only: v1-v4, with no universal arm.
python script/prepare_imdb_lp.py --tasks movie_year

# Alternatively, prepare both Movie-Year and Movie-Director.
# python script/prepare_imdb_lp.py

# DBLP, when its raw files are available.
# python script/prepare_dblp_lp.py
```

Do not rerun preparation for every inference experiment. Reuse the resulting
export at `rai-datasets/preprocessed/IMDB/` or `DBLP/`. Existing build and export
directories are rejected. See [data preparation](DATA_PREPARATION.md) for
`--bundle-root`, `--work-dir`, `--output` and old-layout migration options.

## 4. Run IMDb Movie-Year smoke evaluation

Run inside the GPU allocation after step 1. This evaluates the same fixed subset
of 64 queries on four physical variants, four compiled views, and a separate
physical v1 repeat: **nine inference processes**, run sequentially on one GPU.
Both the 20-candidate link-prediction metrics and full 91-year classification
metrics are calculated from this run.

```bash
set -o pipefail

python -u script/eval_lp.py --dataset imdb --task movie_year --limit 64 --run-tag smoke64 2>&1 | tee logs/imdb_movie_year_smoke64.log
```

The first model forward can take longer while Triton kernels compile.
A user-reported single-view GPU smoke run completed for physical v1 on 64
Movie-Year queries, saving `motif_zeroshot_imdb_lp_debug64/movie_year/physical/v1`
with MRR 0.1681 and full-type accuracy 0.0312. This confirms that the Triton
forward path ran in that HPC session. The saved artifacts have not yet been
reviewed, and the other variants, compiled views, reference repeat and upstream
numerical reproduction remain pending. Fine-tuning backward kernels were not
exercised by this inference run.

If it fails, keep the log and send the error. Stop before starting the full run.

## 5. Generate smoke reports and LaTeX

After inference finishes successfully:

```bash
python script/report_lp.py --dataset imdb --run-tag smoke64
```

Outputs:

```text
results/motif_zeroshot_imdb_lp_smoke64/
  movie_year/
    physical/v1/{metrics.json,scores.npz}
    physical/v1__repeat/{metrics.json,scores.npz}
    ...
    compiled/v1/{metrics.json,scores.npz}
    ...
  tables/
    report.md
    summary.json
    performance.csv
    invariance.csv
    link_prediction.tex
    classification.tex
    invariance.tex
    controls.tex
```

Start with `tables/report.md`. It shows performance, all six physical v1-v4
comparisons, the reference repeat and agreement among compiled views. Smoke
outputs are explicitly labeled as limited-query preliminary results.

## 6. Run the full Movie-Year test set

After a successful smoke run, evaluate every view and repeat on the full test set:

```bash
python -u script/eval_lp.py --dataset imdb --task movie_year --run-tag full 2>&1 | tee logs/imdb_movie_year_full.log
python script/report_lp.py --dataset imdb --run-tag full
```

This uses all 834 held-out Movie-Year test queries. Outputs go to
`results/motif_zeroshot_imdb_lp_full/`. The suite runs four physical variants,
four compiled views and one physical v1 repeat, as nine sequential inference
processes. Reporting calculates all six physical variant pairs, including
Agreement@1 and Kendall tau-b, plus performance metrics and the repeat control.
Run reporting after inference finishes successfully. Use a fresh run tag for
both commands if this output directory already contains runs.

For scientific reporting, also reproduce the checkpoint's upstream benchmark and
validate numerical agreement with its scoring path. The experiments remain
preliminary until that validation is complete.

## 7. Optional additional tasks

Use distinct tags so existing Movie-Year output directories do not conflict.
Restore the module/venv exports in step 1 in each new GPU job. The same frozen
checkpoint, inference adapter and reporting code handle these tasks.

### IMDb Movie-Director

The Movie-Year commands above do not evaluate Movie-Director. The default IMDb
preprocessor prepares both tasks, but `--tasks movie_year` prepares only Year.
Inspect `rai-datasets/preprocessed/IMDB/manifest.json` or list that directory to
see which tasks were exported on the HPC.

The canonical Movie-Director family has **v1 and v3**, with Actor context on the
Movie or Link respectively. Director is the supervised target and stays on the
Movie; Year is fixed Movie context. There are 836 test queries, with the true
director plus 19 fixed negatives for LP. Supplementary classification ranks all
2,081 directors. All views and the reference repeat total five inference
processes, and reporting compares physical v1 vs v3.

If `movie_director/manifest.json` exists in the default IMDb export:

```bash
python script/eval_lp.py --dataset imdb --task movie_director --limit 64 --run-tag director_smoke64
python script/report_lp.py --dataset imdb --run-tag director_smoke64

# After the smoke run succeeds, run all 836 test queries.
python script/eval_lp.py --dataset imdb --task movie_director --run-tag director_full
python script/report_lp.py --dataset imdb --run-tag director_full
```

If the existing IMDb export contains only Movie-Year, prepare Director in fresh
directories, then point evaluation at that export:

```bash
python script/prepare_imdb_lp.py --tasks movie_director \
  --work-dir rai-datasets/preprocessed/_build/IMDB_director \
  --output rai-datasets/preprocessed/IMDB_director

python script/eval_lp.py --dataset imdb --task movie_director \
  --data rai-datasets/preprocessed/IMDB_director \
  --limit 64 --run-tag director_smoke64
python script/report_lp.py --dataset imdb --run-tag director_smoke64

# After the smoke run succeeds; keep the same --data path.
python script/eval_lp.py --dataset imdb --task movie_director \
  --data rai-datasets/preprocessed/IMDB_director --run-tag director_full
python script/report_lp.py --dataset imdb --run-tag director_full
```

If both tasks were prepared in the default IMDb export, a single evaluation
command without `--task` runs both, e.g. `--dataset imdb --run-tag both_full`.
This repeats the Year experiment, so separate Director commands are sufficient
when Year has already been run.

### DBLP Paper-Conference

The query is `(paper, paper_to_conference, ?)` over all **20 conferences**.
The physical variants differ in where the training-support Area context sits:

| Variant | Area placement |
| --- | --- |
| v1 | Paper-to-Area |
| v2 | Conference-to-Area |
| v3 | Author-to-Area |

Universal is omitted. Each variant also has a compiled view. The suite runs
three physical variants, three compiled views and a physical v1 repeat: seven
sequential inference processes. Shared queries/candidates support the three
comparisons v1-v2, v1-v3 and v2-v3, with Agreement@1 and Kendall tau-b.

Place these raw files yourself:

```text
rai-datasets/raw/DBLP/
  author_label.txt
  paper_author.txt
  paper_conf.txt
  paper_term.txt
```

Prepare once on CPU (skip if the adapter-ready DBLP export already exists):

```bash
python script/prepare_dblp_lp.py
```

Expected post-filter train/validation/test positives: **9,448 / 1,348 / 2,666**,
with 26,076 nodes. The command verifies canonical raw files/splits, uses
training-only mapping support and target edges, and exports to
`rai-datasets/preprocessed/DBLP/`.

Inside the GPU allocation, run the smoke suite:

```bash
mkdir -p logs
set -o pipefail

python -u script/eval_lp.py --dataset dblp --task paper_conference \
  --limit 64 --run-tag smoke64 2>&1 | tee logs/dblp_paper_conference_smoke64.log

# After successful inference:
python script/report_lp.py --dataset dblp --run-tag smoke64
```

Then run the full 2,666-query suite and generate reports after it succeeds:

```bash
python -u script/eval_lp.py --dataset dblp --task paper_conference \
  --run-tag full 2>&1 | tee logs/dblp_paper_conference_full.log
python script/report_lp.py --dataset dblp --run-tag full
```

Reports go to `results/motif_zeroshot_dblp_lp_<tag>/tables/`, including LP and
classification performance, the three variant pairs, repeat/compiled controls,
query-bootstrap uncertainty and LaTeX. DBLP LP and classification both use the
same 20-conference universe; IMDb's full-type classification is a supplementary
larger pool. Generate reports on the HPC while the ignored score arrays are
available, before sharing text summaries through Git.

## 8. Preserve and share the results

Keep `metrics.json`, `scores.npz`, the tables and the terminal log. Raw per-query
scores let us recompute metrics and investigate differences later. For example:

```bash
tar -czf results/imdb_movie_year_smoke64_results.tar.gz results/motif_zeroshot_imdb_lp_smoke64 logs/imdb_movie_year_smoke64.log
```

The full results directory is preferable to only the LaTeX table when reviewing
numerical behavior. NumPy `.npz` and `.npy` arrays are ignored throughout the
repository, and all `rai-datasets/` contents remain ignored. Under `results/`,
JSON, Markdown, LaTeX, CSV and `.log` files are eligible for version control;
binary arrays and archives remain ignored.

To share small reports through Git, first sync the updated `.gitignore` to the
HPC. After full inference finishes, generate reports there while `scores.npz`
is available, optionally copy the terminal log into the result directory, then
stage and inspect the files:

```bash
python script/report_lp.py --dataset imdb --run-tag full
cp logs/imdb_movie_year_full.log results/motif_zeroshot_imdb_lp_full/run.log

git add -- .gitignore results/
git diff --cached --stat
git commit -m "Add preliminary MOTIF IMDb Movie-Year zero-shot results"
git push
```

After pulling locally, the report CSV/JSON files can be analyzed and the LaTeX
tables edited directly. Re-running `report_lp.py`, changing bootstrap settings,
or investigating per-query scores locally also requires the ignored
`scores.npz` files. Transfer the full archive separately when needed; keep the
original score files on the HPC. Ignore rules do not untrack files already in
Git; an already-tracked array requires `git rm --cached -- path/to/scores.npz`
to remove it from the Git index while retaining the local file.

## Table definitions

* `link_prediction.tex`: true tail plus 19 supplied negatives, tail-only MRR and
  Hits@1/3/10, with average ranks for ties.
* `classification.tex`: actual year prediction over all 91 years for Movie-Year;
  accuracy, macro-precision, macro-recall, Micro-F1 and Macro-F1. Micro-F1 equals
  accuracy for this single-label setting.
* `invariance.tex`: all six physical Movie-Year pairs, with separate Agreement@1
  and Kendall tau-b columns over the original 20 candidates.
* `controls.tex`: the independent reference repeat, used as the inference-noise
  floor. Compiled-input/output agreement is also recorded in Markdown/JSON.

Every caption identifies the model, dataset, task, split, query count, candidate
protocol and preliminary status. Error bars are **bootstrap standard errors over
queries**, not standard deviations over training seeds; JSON/CSV also contain
95% confidence intervals. See [evaluation definitions](ZERO_SHOT_EVALUATION.md).

## Common issues

* **pybind11 `cast.h:45` compilation error:** the reported log uses GCC 12.2 and
  CUDA 12.1 to build the native `rspmm` extension. For the Triton inference path,
  sync the updated `motif/rspmm/__init__.py`; it must define a lazy wrapper rather
  than eagerly importing `.rspmm` at module scope. Retry with a fresh run tag.
  If the native backend is intentionally used, a GCC 11.x module (not necessarily
  11.3), refreshed `CC`/`CXX` and a separate build cache are a known workaround
  for this compiler issue. Preserve the failing compiler command if it continues.
* **The same build error after the lazy-import edit:** inspect the exact HPC file
  named in the traceback, using `sed -n '1,20p' motif/rspmm/__init__.py` from the
  repository root. A traceback executing `from .rspmm import generalized_rspmm`
  at line 1 shows the old initializer was used for that run. Editing the Windows
  checkout does not update the HPC copy automatically. Sync the file, start a new
  Python process and save a fresh log with a fresh run tag; old logs do not change.
* **No CUDA GPU visible:** run inference inside the GPU allocation with the CUDA
  Torch wheel and activated venv.
* **Output already exists:** select a fresh `--run-tag`, e.g. `smoke64_r2`, and use
  the same tag for reporting. Inference does not silently resume partial suites.
* **Out of memory:** use `--batch-size 1` for the whole suite with a fresh tag,
  e.g. `--run-tag smoke64_bs1`. Keep that batch size fixed across views/repeats.
* **Missing export:** preparation must finish before inference. `--data` can
  select a nondefault adapter-ready export directory.
* **Partial or incompatible reports:** inspect missing runs and keep checkpoint,
  code, GPU type, batch size, seed and query settings fixed across the suite.
  After changing them, start a new tag rather than combining old and new runs.
