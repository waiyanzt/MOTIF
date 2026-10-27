# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.5991 ± 0.0066 | 0.3998 ± 0.0093 | 0.7603 ± 0.0082 | 0.9614 ± 0.0037 |
| physical/v2 | 0.5958 ± 0.0066 | 0.3972 ± 0.0093 | 0.7566 ± 0.0082 | 0.9557 ± 0.0041 |
| physical/v3 | 0.6197 ± 0.0065 | 0.4167 ± 0.0093 | 0.7967 ± 0.0077 | 0.9707 ± 0.0033 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 2666 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.9385 ± 0.0047 | 0.9631 ± 0.0005 | -0.0032 ± 0.0020 |
| v1 vs v3 | 0.7397 ± 0.0083 | 0.8870 ± 0.0013 | 0.0206 ± 0.0043 |
| v2 vs v3 | 0.7254 ± 0.0084 | 0.8748 ± 0.0014 | 0.0238 ± 0.0046 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

