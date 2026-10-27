# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.6010 ± 0.0067 | 0.4047 ± 0.0095 | 0.7607 ± 0.0081 | 0.9625 ± 0.0037 |
| physical/v2 | 0.6029 ± 0.0066 | 0.4036 ± 0.0094 | 0.7659 ± 0.0079 | 0.9621 ± 0.0037 |
| physical/v3 | 0.6033 ± 0.0065 | 0.4055 ± 0.0093 | 0.7626 ± 0.0080 | 0.9617 ± 0.0038 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9629 ± 0.0037 | 0.9622 ± 0.0005 | 0.0020 ± 0.0014 |
| v1 vs v3 | 0.9599 ± 0.0038 | 0.9638 ± 0.0005 | 0.0024 ± 0.0015 |
| v2 vs v3 | 0.9809 ± 0.0026 | 0.9877 ± 0.0002 | 0.0004 ± 0.0010 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

