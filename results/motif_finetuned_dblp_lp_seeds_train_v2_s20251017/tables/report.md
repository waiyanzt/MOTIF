# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.5999 ± 0.0065 | 0.4002 ± 0.0093 | 0.7629 ± 0.0080 | 0.9576 ± 0.0040 |
| physical/v2 | 0.5974 ± 0.0065 | 0.3991 ± 0.0092 | 0.7528 ± 0.0081 | 0.9580 ± 0.0040 |
| physical/v3 | 0.5913 ± 0.0065 | 0.3908 ± 0.0092 | 0.7491 ± 0.0081 | 0.9584 ± 0.0039 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9434 ± 0.0044 | 0.9571 ± 0.0005 | -0.0024 ± 0.0018 |
| v1 vs v3 | 0.9362 ± 0.0046 | 0.9624 ± 0.0005 | -0.0086 ± 0.0020 |
| v2 vs v3 | 0.9482 ± 0.0043 | 0.9812 ± 0.0003 | -0.0061 ± 0.0017 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

