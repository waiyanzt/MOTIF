# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.6076 ± 0.0065 | 0.4092 ± 0.0093 | 0.7641 ± 0.0080 | 0.9629 ± 0.0037 |
| physical/v2 | 0.6001 ± 0.0066 | 0.4006 ± 0.0094 | 0.7573 ± 0.0081 | 0.9565 ± 0.0041 |
| physical/v3 | 0.6226 ± 0.0065 | 0.4167 ± 0.0094 | 0.8020 ± 0.0078 | 0.9752 ± 0.0030 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.8991 ± 0.0058 | 0.9139 ± 0.0008 | -0.0075 ± 0.0025 |
| v1 vs v3 | 0.7348 ± 0.0081 | 0.7788 ± 0.0022 | 0.0151 ± 0.0045 |
| v2 vs v3 | 0.7153 ± 0.0082 | 0.7633 ± 0.0023 | 0.0226 ± 0.0046 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

