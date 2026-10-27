# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2393 ± 0.0101 | 0.1055 ± 0.0109 | 0.2230 ± 0.0146 | 0.5767 ± 0.0174 |
| physical/v2 | 0.1953 ± 0.0089 | 0.0755 ± 0.0089 | 0.1703 ± 0.0132 | 0.4676 ± 0.0173 |
| physical/v3 | 0.1839 ± 0.0083 | 0.0612 ± 0.0087 | 0.1571 ± 0.0126 | 0.4796 ± 0.0172 |
| physical/v4 | 0.2332 ± 0.0098 | 0.1007 ± 0.0103 | 0.2158 ± 0.0148 | 0.5576 ± 0.0174 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.2458 ± 0.0157 | 0.1241 ± 0.0088 | -0.0439 ± 0.0109 |
| v1 vs v3 | 0.2962 ± 0.0158 | 0.3783 ± 0.0090 | -0.0554 ± 0.0112 |
| v1 vs v4 | 0.5707 ± 0.0166 | 0.6635 ± 0.0061 | -0.0061 ± 0.0090 |
| v2 vs v3 | 0.3477 ± 0.0171 | 0.1711 ± 0.0098 | -0.0114 ± 0.0098 |
| v2 vs v4 | 0.2710 ± 0.0156 | 0.1441 ± 0.0084 | 0.0379 ± 0.0106 |
| v3 vs v4 | 0.3022 ± 0.0160 | 0.4400 ± 0.0085 | 0.0493 ± 0.0100 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

