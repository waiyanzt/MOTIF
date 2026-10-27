# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2222 ± 0.0091 | 0.0923 ± 0.0098 | 0.2074 ± 0.0141 | 0.5564 ± 0.0171 |
| physical/v2 | 0.2069 ± 0.0094 | 0.0863 ± 0.0099 | 0.1823 ± 0.0132 | 0.4796 ± 0.0175 |
| physical/v3 | 0.1804 ± 0.0072 | 0.0504 ± 0.0073 | 0.1571 ± 0.0123 | 0.4856 ± 0.0167 |
| physical/v4 | 0.2319 ± 0.0096 | 0.0983 ± 0.0101 | 0.2146 ± 0.0146 | 0.5624 ± 0.0175 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.7146 ± 0.0154 | 0.4893 ± 0.0105 | -0.0153 ± 0.0072 |
| v1 vs v3 | 0.5384 ± 0.0186 | 0.5116 ± 0.0084 | -0.0418 ± 0.0069 |
| v1 vs v4 | 0.7650 ± 0.0148 | 0.7950 ± 0.0059 | 0.0097 ± 0.0051 |
| v2 vs v3 | 0.5252 ± 0.0184 | 0.6440 ± 0.0061 | -0.0266 ± 0.0067 |
| v2 vs v4 | 0.6391 ± 0.0167 | 0.4679 ± 0.0093 | 0.0250 ± 0.0075 |
| v3 vs v4 | 0.4269 ± 0.0181 | 0.4876 ± 0.0081 | 0.0515 ± 0.0077 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

