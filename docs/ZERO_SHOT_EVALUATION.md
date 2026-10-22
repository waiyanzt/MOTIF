# MOTIF zero-shot performance and representation sensitivity

The upstream `script/run.py:test` supports zero-shot evaluation and reports MR,
MRR and Hits@k, normally with full-entity head/tail ranking and pessimistic ties.
It does not supply the requested classification metrics, all-pairs invariance,
bootstrap uncertainty or LaTeX reports.

Our `script/eval_lp.py` reads the portable exports, adds inverses once, invokes
MOTIF's released `build_relation_hypergraph`, then calls the native model forward
pass. Checkpoint loading is strict, gradients and dropout are disabled, FP32 is
used with TF32 disabled, and checkpoint state must remain unchanged. Every graph
view and reference repeat runs in its own process. Lift is built once per graph;
the relation encoder remains query-conditioned. No upstream source is edited.

After Lift, its node-count scalar is converted to a Python integer so the relation
encoder's local padding-count increment cannot mutate the graph's stored count.

## Metric definitions

Two settings are explicitly separate:

* **Original link prediction:** positive plus 19 supplied candidates. Report MRR
  and Hits@1/3/10 with `rank = 1 + better + tied/2`. Repeated IMDb negative years
  stay repeated. DBLP uses all 20 conferences.
* **Supplementary full-type classification:** predict the actual year, director,
  or conference over the full pool (91 / 2,081 / 20 classes). Report accuracy,
  macro-precision, macro-recall, micro-F1 and macro-F1. Macro averages include the
  full fixed class set with zero_division=0. Micro-F1 equals accuracy in this
  single-label setting. Score ties choose the smallest global entity ID, never
  the positive-first candidate position.

Full-year classification accuracy is a different protocol from sampled
20-candidate accuracy. Compare trained baselines only under matched candidate
and tie rules. No classification threshold or new year/genre label edges are
introduced. The native model scores the full target-type pool; the benchmark's
20 scores are gathered from those outputs. No full-entity score matrix is saved.
Held-out targets and equivalent copies are excluded from both Lift and entity
message passing; training target links remain permitted context.

The pairwise table has separate **Agreement@1** and **Kendall tau-b** columns, both
on the original 20-candidate setting. Agreement compares the predicted actual
entity IDs. Tau-b compares aligned candidate-score vectors within each query,
then averages over queries; it is not correlation between aggregate MRR values.
Movie-Year has all six v1-v4 pairs, DBLP three, Movie-Director one. JSON/CSV also
contain paired delta MRR, Hit@1/10 flips, full-type prediction agreement, bitwise
equality and maximum absolute score differences.

The guide's convention is preserved: identical score vectors (including
constants) get tau=1; undefined nonidentical constant-vector comparisons get 0
and their count is reported. Interpret those undefined cases separately.

Tables print **estimate ± bootstrap standard error**, from 1,000 query resamples
by default. JSON/CSV additionally store percentile 95% confidence intervals.
Pairwise quantities resample matched queries together. This uncertainty concerns
test queries, not variability across independently trained models. The frozen
reference repeat measures numerical inference noise separately. Judge
representation effects against that measured noise; non-invariance is not
assumed in advance. Tau=1 alone does not establish score-level invariance.

## HPC commands

Place raw data at `rai-datasets/raw/IMDB/movie_metadata.csv` or under
`rai-datasets/raw/DBLP/`, then run the corresponding preparation command.
The adapter reads `rai-datasets/preprocessed/IMDB/` or
`rai-datasets/preprocessed/DBLP/` by default. Intermediate build files are
separate, under `rai-datasets/preprocessed/_build/`.

Use the working compiler/CUDA modules and activated MOTIF venv, with matched
Torch/PyG extension wheels already installed:

```bash
python -m pip install -r requirements-eval.txt
```

The native extension compilation issue still needs resolution before running the
model. First reproduce an upstream benchmark with `script/run.py --epochs 0`.
The new adapter also needs GPU validation against the upstream scoring path;
CPU tests do not substitute for this numerical reproduction.

First reference-only smoke, including a separate repeat:

```bash
python script/eval_lp.py --dataset imdb --task movie_year --view physical --variant v1 --limit 64 --run-tag reference64
python script/report_lp.py --dataset imdb --run-tag reference64
```

All prepared physical/compiled views plus reference repeats (IMDb 14 processes,
DBLP 7, without universal):

```bash
python script/eval_lp.py --dataset imdb --limit 64
python script/report_lp.py --dataset imdb --run-tag smoke64
python script/eval_lp.py --dataset dblp --limit 64
python script/report_lp.py --dataset dblp --run-tag smoke64
```

For full test evaluation, omit `--limit 64` and `--run-tag smoke64`. Use
`--task movie_year` to restrict IMDb to the four-variant task. Other evaluation
options include `--checkpoint`, `--batch-size` (4), `--seed` (1024), `--split`,
`--device`, `--data`, `--output`, and `--no-repeat`. Changed settings require a
fresh `--run-tag`; inference refuses to overwrite existing runs. Reports can be
regenerated with `--bootstrap` and `--bootstrap-seed` without rerunning inference.

## Artifacts

Outputs live under `results/motif_zeroshot_<dataset>_lp_<tag>/`, where the default
tag is `full` or `smoke64` when limited to 64 queries. Each
`<task>/<physical|compiled>/<variant>/` contains `metrics.json` and `scores.npz`.
The physical reference repeat is named `v1__repeat`.

The run root's `tables/` contains:

```text
link_prediction.tex
classification.tex
invariance.tex
controls.tex
performance.csv
invariance.csv
summary.json
report.md
```

Tables identify model, dataset, task and variant/pair. Include them in LaTeX with
`\usepackage{booktabs}` and e.g.
`\input{results/motif_zeroshot_imdb_lp_full/tables/invariance.tex}`.

Every table caption explicitly identifies this as a preliminary frozen zero-shot
evaluation, the split, query count, candidate protocol and bootstrap error-bar
definition. Limited-query runs are labeled as smoke runs. Classification
captions name the prediction target, full class count, averaging and tie rules;
the invariance caption states that both columns use the original 20 candidates.
This is the exploratory evaluation for discussion, with both settings retained.

Reports reject mismatched checkpoints, query/candidate identities,
precision, hardware, model/adapter source hashes and inference settings. They
label partial coverage, save the repeat noise floor, and check compiled graph
and score equality. JSON, CSV, Markdown and TeX reports are eligible for Git;
raw score arrays remain ignored.

Local validation:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

CPU tests check scikit-learn metric parity, tie handling, paired alignment,
bootstrap reproducibility, six-pair LaTeX/report generation, corrupt-input
rejection, and real native Lift construction. Synthetic fixtures are not
experimental results. GPU forward execution, kernel reproducibility and upstream
numerical parity remain to be checked on the HPC.
