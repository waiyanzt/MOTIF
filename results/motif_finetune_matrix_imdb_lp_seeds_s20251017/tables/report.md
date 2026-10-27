# Preliminary MOTIF fine-tuning matrix

Task: IMDB movie_year; training seed 20251017; 1000 optimizer steps per variant.
Each variant starts independently from the same released checkpoint; validation MRR selects its checkpoint.
Diagonal cells are matched-variant adaptation (C-a); off-diagonal cells are cross-representation transfer (C-b).
Values are estimates ± query-bootstrap standard error (1000 resamples), not training-seed variation.
All reported metrics use the original 20 candidates: the positive target plus 19 fixed negatives.
The guide's training-repeat noise floor and multi-seed mean/SD remain pending; this is a single-seed pilot.

## MRR (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.2419 ± 0.0098 | 0.1969 ± 0.0087 | 0.2034 ± 0.0091 | 0.2270 ± 0.0097 |
| v2 | 0.1953 ± 0.0088 | 0.1939 ± 0.0087 | 0.1673 ± 0.0074 | 0.2090 ± 0.0090 |
| v3 | 0.1907 ± 0.0083 | 0.1946 ± 0.0087 | 0.1940 ± 0.0084 | 0.1910 ± 0.0081 |
| v4 | 0.2229 ± 0.0094 | 0.1862 ± 0.0086 | 0.1547 ± 0.0066 | 0.2241 ± 0.0095 |

## Hits@1 (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.1007 ± 0.0106 | 0.0767 ± 0.0093 | 0.0863 ± 0.0099 | 0.0935 ± 0.0103 |
| v2 | 0.0767 ± 0.0092 | 0.0767 ± 0.0091 | 0.0528 ± 0.0077 | 0.0875 ± 0.0095 |
| v3 | 0.0624 ± 0.0082 | 0.0731 ± 0.0088 | 0.0707 ± 0.0085 | 0.0624 ± 0.0082 |
| v4 | 0.0875 ± 0.0098 | 0.0707 ± 0.0089 | 0.0360 ± 0.0064 | 0.0923 ± 0.0101 |

`transfer_performance.tex` contains the MRR/Hits@1/3/10 transfer matrix for all train/test cells.
`performance.csv` contains all train/test cells and all performance metrics.
`invariance.tex` combines C-a comparisons between separately trained models and C-b fixed-checkpoint comparisons, labelled by regime.
All columns use the same 20 candidates per query; Delta MRR is the second test variant minus the first.
`comparisons.csv` and `summary.json` retain the comparison statistics and confidence intervals.
Package these saved tables with `script/export_overleaf.py`; no PDF is compiled by this reporter.
