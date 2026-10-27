# Preliminary MOTIF fine-tuning matrix

Task: IMDB movie_year; training seed 1566911444; 1000 optimizer steps per variant.
Each variant starts independently from the same released checkpoint; validation MRR selects its checkpoint.
Diagonal cells are matched-variant adaptation (C-a); off-diagonal cells are cross-representation transfer (C-b).
Values are estimates ± query-bootstrap standard error (1000 resamples), not training-seed variation.
All reported metrics use the original 20 candidates: the positive target plus 19 fixed negatives.
The guide's training-repeat noise floor and multi-seed mean/SD remain pending; this is a single-seed pilot.

## MRR (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.2450 ± 0.0102 | 0.2021 ± 0.0087 | 0.1936 ± 0.0083 | 0.2365 ± 0.0098 |
| v2 | 0.2222 ± 0.0091 | 0.2069 ± 0.0094 | 0.1804 ± 0.0072 | 0.2319 ± 0.0096 |
| v3 | 0.2205 ± 0.0094 | 0.1976 ± 0.0082 | 0.2027 ± 0.0082 | 0.2036 ± 0.0087 |
| v4 | 0.2149 ± 0.0096 | 0.1887 ± 0.0080 | 0.1525 ± 0.0065 | 0.2355 ± 0.0100 |

## Hits@1 (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.1091 ± 0.0110 | 0.0779 ± 0.0089 | 0.0695 ± 0.0086 | 0.1043 ± 0.0104 |
| v2 | 0.0923 ± 0.0098 | 0.0863 ± 0.0099 | 0.0504 ± 0.0073 | 0.0983 ± 0.0101 |
| v3 | 0.0887 ± 0.0099 | 0.0659 ± 0.0084 | 0.0671 ± 0.0083 | 0.0743 ± 0.0088 |
| v4 | 0.0971 ± 0.0100 | 0.0492 ± 0.0078 | 0.0360 ± 0.0065 | 0.1163 ± 0.0105 |

`transfer_performance.tex` contains the MRR/Hits@1/3/10 transfer matrix for all train/test cells.
`performance.csv` contains all train/test cells and all performance metrics.
`invariance.tex` combines C-a comparisons between separately trained models and C-b fixed-checkpoint comparisons, labelled by regime.
All columns use the same 20 candidates per query; Delta MRR is the second test variant minus the first.
`comparisons.csv` and `summary.json` retain the comparison statistics and confidence intervals.
Package these saved tables with `script/export_overleaf.py`; no PDF is compiled by this reporter.
