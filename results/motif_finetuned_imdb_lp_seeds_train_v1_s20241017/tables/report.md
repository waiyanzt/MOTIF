# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2339 ± 0.0097 | 0.1043 ± 0.0104 | 0.2134 ± 0.0144 | 0.5516 ± 0.0174 |
| physical/v2 | 0.1966 ± 0.0081 | 0.0683 ± 0.0084 | 0.1799 ± 0.0129 | 0.4796 ± 0.0173 |
| physical/v3 | 0.1838 ± 0.0076 | 0.0576 ± 0.0076 | 0.1547 ± 0.0123 | 0.4748 ± 0.0171 |
| physical/v4 | 0.2319 ± 0.0095 | 0.1019 ± 0.0100 | 0.2062 ± 0.0140 | 0.5444 ± 0.0177 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.3273 ± 0.0165 | 0.2704 ± 0.0092 | -0.0374 ± 0.0092 |
| v1 vs v3 | 0.4472 ± 0.0167 | 0.4340 ± 0.0073 | -0.0502 ± 0.0083 |
| v1 vs v4 | 0.6583 ± 0.0163 | 0.6848 ± 0.0062 | -0.0021 ± 0.0065 |
| v2 vs v3 | 0.5516 ± 0.0178 | 0.2755 ± 0.0122 | -0.0128 ± 0.0063 |
| v2 vs v4 | 0.3801 ± 0.0170 | 0.2616 ± 0.0106 | 0.0353 ± 0.0087 |
| v3 vs v4 | 0.4185 ± 0.0164 | 0.5042 ± 0.0067 | 0.0481 ± 0.0079 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

