# Preliminary MOTIF fine-tuning matrix

Task: DBLP paper_conference; training seed 1566911444; 1000 optimizer steps per variant.
Each variant starts independently from the same released checkpoint; validation MRR selects its checkpoint.
Diagonal cells are matched-variant adaptation (C-a); off-diagonal cells are cross-representation transfer (C-b).
Values are estimates ± query-bootstrap standard error (1000 resamples), not training-seed variation.
All reported metrics use the original 20 candidates: the positive target plus 19 fixed negatives.
The guide's training-repeat noise floor and multi-seed mean/SD remain pending; this is a single-seed pilot.

## MRR (20 candidates)

| Train / Test | v1 | v2 | v3 |
|---|---:|---:|---:|
| v1 | 0.6005 ± 0.0065 | 0.6002 ± 0.0065 | 0.6032 ± 0.0065 |
| v2 | 0.5979 ± 0.0066 | 0.5999 ± 0.0065 | 0.5989 ± 0.0065 |
| v3 | 0.5991 ± 0.0066 | 0.5958 ± 0.0066 | 0.6197 ± 0.0065 |

## Hits@1 (20 candidates)

| Train / Test | v1 | v2 | v3 |
|---|---:|---:|---:|
| v1 | 0.4014 ± 0.0093 | 0.3991 ± 0.0092 | 0.4036 ± 0.0092 |
| v2 | 0.3957 ± 0.0092 | 0.3968 ± 0.0092 | 0.3961 ± 0.0091 |
| v3 | 0.3998 ± 0.0093 | 0.3972 ± 0.0093 | 0.4167 ± 0.0093 |

`conference_prediction.tex` reports macro Precision/Recall/F1 for all nine cells; Accuracy and Micro-F1 equal Hits@1.
`link_prediction.tex` reports MRR and Hits for the same nine cells.
`performance.csv` contains all train/test cells and all performance metrics.
`invariance.tex` combines C-a comparisons between separately trained models and C-b fixed-checkpoint comparisons, labelled by regime.
All columns use the same 20 candidates per query; Delta MRR is the second test variant minus the first.
`comparisons.csv` and `summary.json` retain the comparison statistics and confidence intervals.
Package these saved tables with `script/export_overleaf.py`; no PDF is compiled by this reporter.

DBLP exports three tables: `conference_prediction.tex` (macro Precision/Recall/F1),
`link_prediction.tex` (MRR and Hits), and `invariance.tex` (C-a/C-b labelled comparisons).
All three use the same 20-conference pool; no extra classification task or head is trained.
