# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
All presentation metrics use the benchmark candidate sets specified in guide B2.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.1953 ± 0.0088 | 0.0767 ± 0.0092 | 0.1607 ± 0.0126 | 0.4820 ± 0.0176 |
| physical/v2 | 0.1939 ± 0.0087 | 0.0767 ± 0.0091 | 0.1607 ± 0.0128 | 0.4640 ± 0.0177 |
| physical/v3 | 0.1673 ± 0.0074 | 0.0528 ± 0.0077 | 0.1187 ± 0.0111 | 0.4472 ± 0.0171 |
| physical/v4 | 0.2090 ± 0.0090 | 0.0875 ± 0.0095 | 0.1835 ± 0.0132 | 0.4928 ± 0.0173 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. All columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Delta MRR is the second variant minus the first. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ | $\Delta$MRR |
|---|---:|---:|---:|
| v1 vs v2 | 0.4125 ± 0.0170 | 0.5426 ± 0.0093 | -0.0014 ± 0.0091 |
| v1 vs v3 | 0.4904 ± 0.0167 | 0.6497 ± 0.0081 | -0.0280 ± 0.0074 |
| v1 vs v4 | 0.8165 ± 0.0135 | 0.8777 ± 0.0039 | 0.0137 ± 0.0042 |
| v2 vs v3 | 0.7122 ± 0.0165 | 0.8334 ± 0.0055 | -0.0266 ± 0.0052 |
| v2 vs v4 | 0.4712 ± 0.0174 | 0.5668 ± 0.0087 | 0.0151 ± 0.0090 |
| v3 vs v4 | 0.4640 ± 0.0170 | 0.5918 ± 0.0090 | 0.0418 ± 0.0082 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

