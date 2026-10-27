# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2205 ± 0.0094 | 0.0887 ± 0.0099 | 0.2110 ± 0.0145 | 0.5228 ± 0.0173 |
| physical/v2 | 0.1976 ± 0.0082 | 0.0659 ± 0.0084 | 0.1691 ± 0.0128 | 0.5348 ± 0.0175 |
| physical/v3 | 0.2027 ± 0.0082 | 0.0671 ± 0.0083 | 0.1775 ± 0.0131 | 0.5264 ± 0.0176 |
| physical/v4 | 0.2036 ± 0.0087 | 0.0743 ± 0.0088 | 0.1930 ± 0.0138 | 0.4928 ± 0.0176 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.3333 ± 0.0164 | -0.3411 ± 0.0094 | -0.0229 ± 0.0123 |
| v1 vs v3 | 0.3981 ± 0.0169 | 0.2955 ± 0.0075 | -0.0178 ± 0.0096 |
| v1 vs v4 | 0.8393 ± 0.0129 | 0.8105 ± 0.0040 | -0.0169 ± 0.0044 |
| v2 vs v3 | 0.6583 ± 0.0161 | -0.2565 ± 0.0073 | 0.0051 ± 0.0091 |
| v2 vs v4 | 0.3669 ± 0.0169 | -0.3232 ± 0.0093 | 0.0060 ± 0.0113 |
| v3 vs v4 | 0.4101 ± 0.0170 | 0.2250 ± 0.0072 | 0.0009 ± 0.0094 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

