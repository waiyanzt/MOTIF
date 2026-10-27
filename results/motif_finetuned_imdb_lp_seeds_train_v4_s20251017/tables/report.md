# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2229 ± 0.0094 | 0.0875 ± 0.0098 | 0.2038 ± 0.0143 | 0.5707 ± 0.0173 |
| physical/v2 | 0.1862 ± 0.0086 | 0.0707 ± 0.0089 | 0.1427 ± 0.0121 | 0.4592 ± 0.0176 |
| physical/v3 | 0.1547 ± 0.0066 | 0.0360 ± 0.0064 | 0.1115 ± 0.0108 | 0.4544 ± 0.0173 |
| physical/v4 | 0.2241 ± 0.0095 | 0.0923 ± 0.0101 | 0.2014 ± 0.0138 | 0.5719 ± 0.0171 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.4089 ± 0.0168 | 0.4830 ± 0.0077 | -0.0367 ± 0.0097 |
| v1 vs v3 | 0.2230 ± 0.0148 | 0.3495 ± 0.0104 | -0.0682 ± 0.0110 |
| v1 vs v4 | 0.6115 ± 0.0170 | 0.7150 ± 0.0065 | 0.0012 ± 0.0076 |
| v2 vs v3 | 0.2854 ± 0.0149 | 0.6256 ± 0.0075 | -0.0314 ± 0.0085 |
| v2 vs v4 | 0.4269 ± 0.0179 | 0.5346 ± 0.0079 | 0.0379 ± 0.0095 |
| v3 vs v4 | 0.1403 ± 0.0121 | 0.3568 ± 0.0109 | 0.0694 ± 0.0113 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

