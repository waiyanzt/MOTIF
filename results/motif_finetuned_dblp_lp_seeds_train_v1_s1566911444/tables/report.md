# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.6005 ± 0.0065 | 0.4014 ± 0.0093 | 0.7603 ± 0.0080 | 0.9580 ± 0.0040 |
| physical/v2 | 0.6002 ± 0.0065 | 0.3991 ± 0.0092 | 0.7614 ± 0.0081 | 0.9584 ± 0.0040 |
| physical/v3 | 0.6032 ± 0.0065 | 0.4036 ± 0.0092 | 0.7641 ± 0.0081 | 0.9610 ± 0.0038 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9340 ± 0.0049 | 0.9509 ± 0.0006 | -0.0003 ± 0.0019 |
| v1 vs v3 | 0.9449 ± 0.0044 | 0.9689 ± 0.0004 | 0.0027 ± 0.0017 |
| v2 vs v3 | 0.9295 ± 0.0051 | 0.9515 ± 0.0006 | 0.0030 ± 0.0021 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

