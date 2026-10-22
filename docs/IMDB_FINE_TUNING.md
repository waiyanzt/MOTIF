# IMDb MOTIF fine-tuning on the HPC

Fine-tuning starts from `ckpts/motif_3g.pth` and updates the existing trainable
weights on IMDb training positives. It does not replay the original pretraining
datasets. Static positional encodings remain frozen as defined by MOTIF.
Reuse the existing preprocessed IMDb data and retain the zero-shot results.

Run from MOTIF with the same modules, activated venv and exports as the successful
zero-shot run; see the [HPC runbook](HPC_ZERO_SHOT_RUNBOOK.md). No new dependencies
are required. This new training path has not been executed locally. Its first
runtime validation is the HPC training smoke below.

## Protocol

These commands train one checkpoint on **physical v1 Movie-Year**, then evaluate
the same checkpoint on physical v1-v4. This is guide C-b (cross-representation
transfer), including a v1-to-v1 reference. The trainer also accepts another
`--train-variant`. Independently fine-tuning one model per variant is a separate
experiment, guide C-a; its comparisons involve different trained weights and
require separate reporting. The current reporter deliberately requires the same
selected checkpoint across evaluation variants.

Following section C2 of
`SCR/ULTRA_pilot/ULTRA_pilot/GFM_EVALUATION_GUIDE.md`:

* Train on the 2,925 shared Movie-Year positives and their 19 fixed negative years.
  Context relations are not additional training targets.
* Fix the optimizer-step budget, batch size, keyed data order and candidate sets
  when selecting another training variant.
* Require physical target edges to equal the training positives; reject additional
  Link-to-target copies. Native MOTIF removes each batch's target edges and internal
  inverses, then rebuilds Lift before training. Record the actual number removed.
* Select the checkpoint by MRR on fixed validation candidates using average ranks
  for ties. Full runs use all 418 validation queries. Test labels are not used for
  training or checkpoint selection.
* Update all parameters the released architecture marks trainable. The loss follows
  MOTIF's binary cross-entropy with detached adversarial negative weights.

The pilot defaults are Adam, learning rate `5e-4`, batch size 4, gradient-norm
clipping at 1 and 1,000 optimizer steps. These are starting settings, not established
IMDb hyperparameters or a reproduced paper configuration. Universal and compiled
training arms are outside this initial experiment.

## 1. Two-update training smoke

Sync the new trainer and updated evaluation/reporting scripts to HPC. Inside
the GPU allocation:

```bash
mkdir -p logs
set -o pipefail

python -u script/finetune_imdb_lp.py \
  --task movie_year --train-variant v1 \
  --steps 2 --validate-every 2 --val-limit 16 --run-tag smoke \
  2>&1 | tee logs/imdb_movie_year_finetune_smoke.log
```

This uses the full graph, two optimizer updates and 16 validation queries. It
exercises backward kernels, checks finite gradients and changed parameters, and
records gradient norms for both encoders. Limited validation is for this smoke
only. The successful zero-shot forward did not validate backward kernels.

Outputs:

```text
results/motif_finetune_imdb_lp_smoke/movie_year/train_v1/seed1024/
  best.pth
  training_config.json
  training_summary.json
  history.csv
```

If it fails, preserve the new log before a full run. The Triton path retains the
lazy native-extension import; training does not automatically select the separate
C++/CUDA backend.

## 2. Full pilot training

After the training smoke succeeds, start afresh from the released checkpoint:

```bash
python -u script/finetune_imdb_lp.py \
  --task movie_year --train-variant v1 \
  --steps 1000 --validate-every 100 --run-tag pilot \
  2>&1 | tee logs/imdb_movie_year_finetune_pilot.log
```

The best checkpoint among the evaluated training steps is saved to:

```text
results/motif_finetune_imdb_lp_pilot/movie_year/train_v1/seed1024/best.pth
```

Step-zero validation is recorded separately. Validation ties retain the earlier
checkpoint. Do not initialize the full pilot from the smoke checkpoint. Existing
training output directories are rejected; choose a fresh tag for retries or new
settings. This initial trainer does not resume interrupted optimizer state.

## 3. Evaluate the fine-tuned checkpoint

After training finishes, evaluate all 834 test queries on each physical variant:

```bash
python -u script/eval_lp.py \
  --stage finetuned --dataset imdb --task movie_year \
  --view physical --no-repeat \
  --checkpoint results/motif_finetune_imdb_lp_pilot/movie_year/train_v1/seed1024/best.pth \
  --run-tag v1ft_s1024 \
  2>&1 | tee logs/imdb_movie_year_finetuned_v1ft_s1024.log
```

Every variant uses the same selected weights and the same test queries/candidates.
The evaluator checks training provenance and checkpoint weights, freezes them for
scoring and retains the zero-shot metric definitions. Fine-tuned results require
the same dataset export and model configuration used for training. They are
labelled and stored separately from zero-shot results.

## 4. Tables and Overleaf

After inference succeeds:

```bash
python script/report_lp.py --stage finetuned --dataset imdb --run-tag v1ft_s1024
```

Results go to `results/motif_finetuned_imdb_lp_v1ft_s1024/tables/`, with the same
performance metrics and all six Agreement@1/Kendall tau-b variant comparisons.
Captions identify the v1 fine-tune. To package the saved reports for Overleaf:

```bash
python script/export_overleaf.py \
  --run results/motif_finetuned_imdb_lp_v1ft_s1024 \
  --output results/overleaf/motif_imdb_finetuned_v1_s1024
```

This first pilot uses one training seed. Error bars remain query-bootstrap standard
errors, not training-seed variability. The later multi-seed study should use at
least three training seeds and report mean/standard deviation across seeds
separately, following guide C4/C6. Results remain preliminary pending upstream
scoring/reproduction validation.

Movie-Director can later use `--task movie_director` and its v1/v3 family with a
separately trained checkpoint. These instructions begin with Movie-Year, the
completed zero-shot task.
