# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.1907 ± 0.0083 | 0.0624 ± 0.0082 | 0.1619 ± 0.0130 | 0.4976 ± 0.0173 |
| physical/v2 | 0.1946 ± 0.0087 | 0.0731 ± 0.0088 | 0.1727 ± 0.0134 | 0.4688 ± 0.0171 |
| physical/v3 | 0.1940 ± 0.0084 | 0.0707 ± 0.0085 | 0.1727 ± 0.0131 | 0.4796 ± 0.0174 |
| physical/v4 | 0.1910 ± 0.0081 | 0.0624 ± 0.0082 | 0.1691 ± 0.0130 | 0.4976 ± 0.0169 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v3, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.5959 ± 0.0170 | 0.4960 ± 0.0060 | 0.0039 ± 0.0074 |
| v1 vs v3 | 0.6667 ± 0.0161 | 0.6621 ± 0.0046 | 0.0033 ± 0.0069 |
| v1 vs v4 | 0.8597 ± 0.0122 | 0.8421 ± 0.0028 | 0.0003 ± 0.0035 |
| v2 vs v3 | 0.6882 ± 0.0159 | 0.7309 ± 0.0050 | -0.0006 ± 0.0061 |
| v2 vs v4 | 0.5959 ± 0.0173 | 0.4725 ± 0.0062 | -0.0036 ± 0.0075 |
| v3 vs v4 | 0.6511 ± 0.0165 | 0.6386 ± 0.0046 | -0.0029 ± 0.0069 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

