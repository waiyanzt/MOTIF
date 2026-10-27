# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2419 ± 0.0098 | 0.1007 ± 0.0106 | 0.2338 ± 0.0150 | 0.5791 ± 0.0174 |
| physical/v2 | 0.1969 ± 0.0087 | 0.0767 ± 0.0093 | 0.1679 ± 0.0127 | 0.4556 ± 0.0168 |
| physical/v3 | 0.2034 ± 0.0091 | 0.0863 ± 0.0099 | 0.1691 ± 0.0126 | 0.4832 ± 0.0172 |
| physical/v4 | 0.2270 ± 0.0097 | 0.0935 ± 0.0103 | 0.2098 ± 0.0142 | 0.5444 ± 0.0179 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.0827 ± 0.0097 | 0.0986 ± 0.0088 | -0.0450 ± 0.0130 |
| v1 vs v3 | 0.0899 ± 0.0102 | 0.1657 ± 0.0109 | -0.0385 ± 0.0135 |
| v1 vs v4 | 0.4856 ± 0.0171 | 0.6474 ± 0.0069 | -0.0149 ± 0.0089 |
| v2 vs v3 | 0.5659 ± 0.0176 | 0.6225 ± 0.0071 | 0.0065 ± 0.0068 |
| v2 vs v4 | 0.1355 ± 0.0119 | 0.2060 ± 0.0086 | 0.0301 ± 0.0123 |
| v3 vs v4 | 0.1415 ± 0.0127 | 0.2598 ± 0.0108 | 0.0236 ± 0.0126 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

