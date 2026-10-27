# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.5979 ± 0.0066 | 0.3957 ± 0.0092 | 0.7599 ± 0.0080 | 0.9614 ± 0.0039 |
| physical/v2 | 0.5999 ± 0.0065 | 0.3968 ± 0.0092 | 0.7629 ± 0.0079 | 0.9614 ± 0.0038 |
| physical/v3 | 0.5989 ± 0.0065 | 0.3961 ± 0.0091 | 0.7599 ± 0.0081 | 0.9621 ± 0.0038 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9704 ± 0.0033 | 0.9579 ± 0.0005 | 0.0020 ± 0.0013 |
| v1 vs v3 | 0.9685 ± 0.0034 | 0.9696 ± 0.0004 | 0.0010 ± 0.0013 |
| v2 vs v3 | 0.9797 ± 0.0028 | 0.9697 ± 0.0004 | -0.0010 ± 0.0011 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

