# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.6092 ± 0.0065 | 0.4122 ± 0.0092 | 0.7671 ± 0.0079 | 0.9599 ± 0.0039 |
| physical/v2 | 0.6069 ± 0.0065 | 0.4085 ± 0.0093 | 0.7659 ± 0.0079 | 0.9584 ± 0.0040 |
| physical/v3 | 0.6087 ± 0.0065 | 0.4104 ± 0.0093 | 0.7674 ± 0.0078 | 0.9606 ± 0.0039 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9494 ± 0.0042 | 0.9516 ± 0.0006 | -0.0023 ± 0.0018 |
| v1 vs v3 | 0.9591 ± 0.0037 | 0.9721 ± 0.0004 | -0.0005 ± 0.0016 |
| v2 vs v3 | 0.9737 ± 0.0030 | 0.9680 ± 0.0004 | 0.0018 ± 0.0013 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

