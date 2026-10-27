# Seed-averaged tables (lab format)

`script/report_seeds.py` produces the two tables in `assets/table format.png`:

* **Performance:** one row per method and variant, with MRR, Hits@1, Hits@3, Precision and Recall.
* **Invariance:** one Kendall-τ row per variant pair.

Metric definitions and aggregation follow `SCR/INV-GNN-12D9/docs/results/METRICS.md`,
so the MOTIF rows can be compared directly with the lab's CMPNN results:

* MRR and Hits@k use the 20 fixed candidates per query, and ties get the averaged rank.
* Precision and Recall are binary metrics, pooled over all (query, candidate) pairs. A pair
  counts as predicted positive when σ(score) ≥ 0.5, i.e. MOTIF's logit ≥ 0. With 1 positive
  in 20 candidates, a model that predicts every pair positive shows Precision ≈ 0.05 and
  Recall = 1.
* Kendall-τ is the per-query τ_b between two variants' candidate scores, averaged over
  queries. It is computed within one seed.
* Each cell is mean ± population std (ddof = 0) over the training seeds
  1566911444, 20241017 and 20251017.
* **MOTIF (FT)** rows use the model trained and tested on the same variant, which is the
  lab's "original" arm. FT τ compares the independently trained v_i and v_j models.
* **MOTIF (ZS)** has no training seed. Its single deterministic run is shown with std 0.

## 1. Fine-tune with the three lab seeds

From the repository root on the submit node:

```bash
sbatch slurm/finetune_seeds.sbatch                              # IMDb movie_year
sbatch --export=ALL,DATASET=dblp slurm/finetune_seeds.sbatch    # DBLP paper_conference
```

This submits one array task per seed. Each task runs the full train/test matrix
(`script/run_finetune_matrix.py`) under the run tag `seeds`. The output goes to
`results/motif_finetune_matrix_<dataset>_lp_seeds_s<seed>/`, and Slurm logs go to
`logs/motif-ft-seeds-<job>_<task>.out`. You can resubmit after a failure: `--resume`
reuses completed cells.

## 2. Build the tables

```bash
python script/report_seeds.py --dataset imdb \
  --zeroshot results/motif_zeroshot_imdb_lp_full \
  --finetune results/motif_finetune_matrix_imdb_lp_seeds_s* \
  --baseline-tex ../SCR/INV-GNN-12D9/docs/results/IMDB_lp.tex
```

This step runs on CPU in a few seconds. It writes `results/seed_summary_<dataset>_<task>/`:
`performance.tex`, `invariance.tex`, `report.md`, `performance.csv`, `invariance.csv` and
`summary.json`.

* `--baseline-tex` adds the CMPNN "original" rows from the lab's results file.
  `--baseline` selects a different model block, e.g. `RGCN`.
* Drop `--zeroshot` or `--finetune` to report only one of them.
* All matrices passed together must share code and settings, apart from the seed.
