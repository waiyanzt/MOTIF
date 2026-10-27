# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2149 ± 0.0096 | 0.0971 ± 0.0100 | 0.1859 ± 0.0134 | 0.4772 ± 0.0177 |
| physical/v2 | 0.1887 ± 0.0080 | 0.0492 ± 0.0078 | 0.1739 ± 0.0133 | 0.5180 ± 0.0177 |
| physical/v3 | 0.1525 ± 0.0065 | 0.0360 ± 0.0065 | 0.1067 ± 0.0106 | 0.4376 ± 0.0170 |
| physical/v4 | 0.2355 ± 0.0100 | 0.1163 ± 0.0105 | 0.2110 ± 0.0143 | 0.4976 ± 0.0177 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.1115 ± 0.0105 | 0.3427 ± 0.0080 | -0.0262 ± 0.0110 |
| v1 vs v3 | 0.2566 ± 0.0158 | 0.3433 ± 0.0070 | -0.0623 ± 0.0102 |
| v1 vs v4 | 0.6763 ± 0.0161 | 0.7317 ± 0.0052 | 0.0206 ± 0.0052 |
| v2 vs v3 | 0.3285 ± 0.0159 | 0.2348 ± 0.0077 | -0.0361 ± 0.0089 |
| v2 vs v4 | 0.1667 ± 0.0129 | 0.3667 ± 0.0080 | 0.0468 ± 0.0110 |
| v3 vs v4 | 0.1295 ± 0.0113 | 0.3387 ± 0.0072 | 0.0829 ± 0.0108 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

