# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.5968 ± 0.0065 | 0.3995 ± 0.0092 | 0.7506 ± 0.0080 | 0.9572 ± 0.0040 |
| physical/v2 | 0.5967 ± 0.0065 | 0.3998 ± 0.0091 | 0.7539 ± 0.0080 | 0.9546 ± 0.0042 |
| physical/v3 | 0.6145 ± 0.0065 | 0.4122 ± 0.0093 | 0.7779 ± 0.0079 | 0.9670 ± 0.0035 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.8455 ± 0.0069 | 0.9048 ± 0.0010 | -0.0001 ± 0.0029 |
| v1 vs v3 | 0.7629 ± 0.0081 | 0.8448 ± 0.0013 | 0.0177 ± 0.0040 |
| v2 vs v3 | 0.7404 ± 0.0083 | 0.8509 ± 0.0014 | 0.0178 ± 0.0042 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

