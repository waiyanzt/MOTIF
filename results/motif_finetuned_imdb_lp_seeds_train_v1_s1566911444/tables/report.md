# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2450 ± 0.0102 | 0.1091 ± 0.0110 | 0.2314 ± 0.0152 | 0.5971 ± 0.0173 |
| physical/v2 | 0.2021 ± 0.0087 | 0.0779 ± 0.0089 | 0.1751 ± 0.0130 | 0.4856 ± 0.0171 |
| physical/v3 | 0.1936 ± 0.0083 | 0.0695 ± 0.0086 | 0.1655 ± 0.0129 | 0.4724 ± 0.0173 |
| physical/v4 | 0.2365 ± 0.0098 | 0.1043 ± 0.0104 | 0.2206 ± 0.0144 | 0.5743 ± 0.0176 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.2638 ± 0.0152 | 0.1224 ± 0.0105 | -0.0429 ± 0.0105 |
| v1 vs v3 | 0.3273 ± 0.0158 | 0.2611 ± 0.0086 | -0.0514 ± 0.0102 |
| v1 vs v4 | 0.5875 ± 0.0171 | 0.6509 ± 0.0065 | -0.0084 ± 0.0079 |
| v2 vs v3 | 0.5899 ± 0.0167 | 0.5140 ± 0.0083 | -0.0084 ± 0.0060 |
| v2 vs v4 | 0.3333 ± 0.0165 | 0.1919 ± 0.0100 | 0.0345 ± 0.0095 |
| v3 vs v4 | 0.3873 ± 0.0167 | 0.3745 ± 0.0079 | 0.0429 ± 0.0089 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

