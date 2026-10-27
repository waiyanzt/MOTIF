# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.1965 ± 0.0081 | 0.0659 ± 0.0083 | 0.1775 ± 0.0125 | 0.5036 ± 0.0169 |
| physical/v2 | 0.1832 ± 0.0083 | 0.0659 ± 0.0084 | 0.1379 ± 0.0119 | 0.4724 ± 0.0178 |
| physical/v3 | 0.1958 ± 0.0082 | 0.0695 ± 0.0085 | 0.1691 ± 0.0126 | 0.5048 ± 0.0176 |
| physical/v4 | 0.1924 ± 0.0082 | 0.0683 ± 0.0083 | 0.1643 ± 0.0126 | 0.4748 ± 0.0175 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.3058 ± 0.0159 | 0.1309 ± 0.0091 | -0.0133 ± 0.0103 |
| v1 vs v3 | 0.3453 ± 0.0159 | 0.2426 ± 0.0102 | -0.0007 ± 0.0099 |
| v1 vs v4 | 0.5911 ± 0.0175 | 0.7729 ± 0.0063 | -0.0041 ± 0.0061 |
| v2 vs v3 | 0.5288 ± 0.0175 | 0.7486 ± 0.0073 | 0.0126 ± 0.0063 |
| v2 vs v4 | 0.3741 ± 0.0170 | 0.2643 ± 0.0114 | 0.0092 ± 0.0096 |
| v3 vs v4 | 0.4317 ± 0.0169 | 0.2593 ± 0.0115 | -0.0035 ± 0.0093 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

