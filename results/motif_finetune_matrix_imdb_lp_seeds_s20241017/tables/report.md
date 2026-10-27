# Preliminary MOTIF fine-tuning matrix

Task: IMDB movie_year; training seed 20241017; 1000 optimizer steps per variant.
Each variant starts independently from the same released checkpoint; validation MRR selects its checkpoint.
Diagonal cells are matched-variant adaptation (C-a); off-diagonal cells are cross-representation transfer (C-b).
Values are estimates ± query-bootstrap standard error (1000 resamples), not training-seed variation.
All reported metrics use the original 20 candidates: the positive target plus 19 fixed negatives.
The guide's training-repeat noise floor and multi-seed mean/SD remain pending; this is a single-seed pilot.

## MRR (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.2339 ± 0.0097 | 0.1966 ± 0.0081 | 0.1838 ± 0.0076 | 0.2319 ± 0.0095 |
| v2 | 0.1997 ± 0.0089 | 0.1927 ± 0.0084 | 0.1602 ± 0.0070 | 0.2152 ± 0.0093 |
| v3 | 0.1965 ± 0.0081 | 0.1832 ± 0.0083 | 0.1958 ± 0.0082 | 0.1924 ± 0.0082 |
| v4 | 0.2393 ± 0.0101 | 0.1953 ± 0.0089 | 0.1839 ± 0.0083 | 0.2332 ± 0.0098 |

## Hits@1 (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.1043 ± 0.0104 | 0.0683 ± 0.0084 | 0.0576 ± 0.0076 | 0.1019 ± 0.0100 |
| v2 | 0.0827 ± 0.0094 | 0.0719 ± 0.0085 | 0.0396 ± 0.0068 | 0.0959 ± 0.0100 |
| v3 | 0.0659 ± 0.0083 | 0.0659 ± 0.0084 | 0.0695 ± 0.0085 | 0.0683 ± 0.0083 |
| v4 | 0.1055 ± 0.0109 | 0.0755 ± 0.0089 | 0.0612 ± 0.0087 | 0.1007 ± 0.0103 |

`transfer_performance.tex` contains the MRR/Hits@1/3/10 transfer matrix for all train/test cells.
`performance.csv` contains all train/test cells and all performance metrics.
`invariance.tex` combines C-a comparisons between separately trained models and C-b fixed-checkpoint comparisons, labelled by regime.
All columns use the same 20 candidates per query; Delta MRR is the second test variant minus the first.
`comparisons.csv` and `summary.json` retain the comparison statistics and confidence intervals.
Package these saved tables with `script/export_overleaf.py`; no PDF is compiled by this reporter.
