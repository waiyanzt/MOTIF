# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.1997 ± 0.0089 | 0.0827 ± 0.0094 | 0.1631 ± 0.0126 | 0.4784 ± 0.0175 |
| physical/v2 | 0.1927 ± 0.0084 | 0.0719 ± 0.0085 | 0.1523 ± 0.0124 | 0.4712 ± 0.0168 |
| physical/v3 | 0.1602 ± 0.0070 | 0.0396 ± 0.0068 | 0.1175 ± 0.0112 | 0.4388 ± 0.0175 |
| physical/v4 | 0.2152 ± 0.0093 | 0.0959 ± 0.0100 | 0.1835 ± 0.0134 | 0.4928 ± 0.0175 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.3441 ± 0.0160 | 0.5058 ± 0.0070 | -0.0070 ± 0.0093 |
| v1 vs v3 | 0.3657 ± 0.0169 | 0.5793 ± 0.0083 | -0.0396 ± 0.0093 |
| v1 vs v4 | 0.7590 ± 0.0146 | 0.8648 ± 0.0043 | 0.0155 ± 0.0043 |
| v2 vs v3 | 0.4652 ± 0.0168 | 0.5751 ± 0.0058 | -0.0326 ± 0.0071 |
| v2 vs v4 | 0.3393 ± 0.0160 | 0.4692 ± 0.0076 | 0.0225 ± 0.0100 |
| v3 vs v4 | 0.2362 ± 0.0141 | 0.4575 ± 0.0093 | 0.0550 ± 0.0102 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

