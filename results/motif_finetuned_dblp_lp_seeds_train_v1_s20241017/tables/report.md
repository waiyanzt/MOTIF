# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.6086 ± 0.0064 | 0.4119 ± 0.0092 | 0.7633 ± 0.0080 | 0.9644 ± 0.0036 |
| physical/v2 | 0.6033 ± 0.0065 | 0.4059 ± 0.0092 | 0.7626 ± 0.0080 | 0.9617 ± 0.0038 |
| physical/v3 | 0.6062 ± 0.0064 | 0.4089 ± 0.0091 | 0.7641 ± 0.0079 | 0.9632 ± 0.0037 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9194 ± 0.0052 | 0.9444 ± 0.0006 | -0.0053 ± 0.0023 |
| v1 vs v3 | 0.9415 ± 0.0044 | 0.9645 ± 0.0005 | -0.0024 ± 0.0018 |
| v2 vs v3 | 0.9557 ± 0.0038 | 0.9679 ± 0.0004 | 0.0028 ± 0.0017 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

