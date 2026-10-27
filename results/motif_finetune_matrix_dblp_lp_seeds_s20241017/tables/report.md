# Preliminary MOTIF fine-tuning matrix

Task: DBLP paper_conference; training seed 20241017; 1000 optimizer steps per variant.
Each variant starts independently from the same released checkpoint; validation MRR selects its checkpoint.
Diagonal cells are matched-variant adaptation (C-a); off-diagonal cells are cross-representation transfer (C-b).
Values are estimates ± query-bootstrap standard error (1000 resamples), not training-seed variation.
All reported metrics use the original 20 candidates: the positive target plus 19 fixed negatives.
The guide's training-repeat noise floor and multi-seed mean/SD remain pending; this is a single-seed pilot.

## MRR (20 candidates)

| Train / Test | v1 | v2 | v3 |
|---|---:|---:|---:|
| v1 | 0.6086 ± 0.0064 | 0.6033 ± 0.0065 | 0.6062 ± 0.0064 |
| v2 | 0.6010 ± 0.0067 | 0.6029 ± 0.0066 | 0.6033 ± 0.0065 |
| v3 | 0.5968 ± 0.0065 | 0.5967 ± 0.0065 | 0.6145 ± 0.0065 |

## Hits@1 (20 candidates)

| Train / Test | v1 | v2 | v3 |
|---|---:|---:|---:|
| v1 | 0.4119 ± 0.0092 | 0.4059 ± 0.0092 | 0.4089 ± 0.0091 |
| v2 | 0.4047 ± 0.0095 | 0.4036 ± 0.0094 | 0.4055 ± 0.0093 |
| v3 | 0.3995 ± 0.0092 | 0.3998 ± 0.0091 | 0.4122 ± 0.0093 |

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
