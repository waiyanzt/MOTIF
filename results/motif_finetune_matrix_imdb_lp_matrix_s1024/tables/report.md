# Preliminary MOTIF fine-tuning matrix

Task: IMDb movie_year; training seed 1024; 1000 optimizer steps per variant.
Each variant starts independently from the same released checkpoint; validation MRR selects its checkpoint.
Diagonal cells are matched-variant adaptation (C-a); off-diagonal cells are cross-representation transfer (C-b).
Values are estimates ± query-bootstrap standard error (1000 resamples), not training-seed variation.
Classification uses the full target-type pool; link prediction uses the original 20 candidates.

## Accuracy

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 |
| v2 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 |
| v3 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 |
| v4 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 | 0.0012 ± 0.0012 |

## Macro-F1

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 |
| v2 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 |
| v3 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 |
| v4 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 | 0.0000 ± 0.0000 |

## MRR (20 candidates)

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.2028 ± 0.0090 | 0.1875 ± 0.0087 | 0.1724 ± 0.0075 | 0.2225 ± 0.0095 |
| v2 | 0.2183 ± 0.0092 | 0.1823 ± 0.0085 | 0.1551 ± 0.0070 | 0.2311 ± 0.0096 |
| v3 | 0.2092 ± 0.0094 | 0.1913 ± 0.0089 | 0.2110 ± 0.0093 | 0.2006 ± 0.0095 |
| v4 | 0.2140 ± 0.0093 | 0.1922 ± 0.0088 | 0.1722 ± 0.0077 | 0.2253 ± 0.0094 |

`performance.csv` contains all train/test cells and all performance metrics.
`classification_diagonal.tex` shows the matched-variant baseline; `classification_all.tex` shows every cell.
`per_variant_comparisons.tex` compares the independently trained diagonal models: training and representation both vary.
`transfer_comparisons.tex` groups Agreement@1 and Kendall tau-b comparisons by fixed training checkpoint.
Both comparison columns use the same 20 candidates per query; classification metrics remain separate.
`comparisons.csv` and `summary.json` retain the comparison statistics and confidence intervals.
Package these saved tables with `script/export_overleaf.py`; no PDF is compiled by this reporter.
