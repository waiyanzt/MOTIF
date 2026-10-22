# Preliminary MOTIF zero-shot evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
Classification predicts the actual target entity over the full target-type pool; macro averages include every pool class, zero_division=0.
Micro-F1 equals accuracy in this single-label setting. Top-1 ties use the smallest global tail id.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary frozen zero-shot evaluation on the test split; 834 queries. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| compiled/v1 | 0.1804 ± 0.0082 | 0.0635 ± 0.0084 | 0.1355 ± 0.0118 | 0.4688 ± 0.0176 |
| compiled/v2 | 0.1804 ± 0.0082 | 0.0635 ± 0.0084 | 0.1355 ± 0.0118 | 0.4688 ± 0.0176 |
| compiled/v3 | 0.1804 ± 0.0082 | 0.0635 ± 0.0084 | 0.1355 ± 0.0118 | 0.4688 ± 0.0176 |
| compiled/v4 | 0.1804 ± 0.0082 | 0.0635 ± 0.0084 | 0.1355 ± 0.0118 | 0.4688 ± 0.0176 |
| physical/v1 | 0.1802 ± 0.0082 | 0.0624 ± 0.0085 | 0.1379 ± 0.0120 | 0.4580 ± 0.0175 |
| physical/v2 | 0.1901 ± 0.0087 | 0.0755 ± 0.0093 | 0.1487 ± 0.0123 | 0.4652 ± 0.0175 |
| physical/v3 | 0.1553 ± 0.0068 | 0.0396 ± 0.0068 | 0.1055 ± 0.0107 | 0.4436 ± 0.0171 |
| physical/v4 | 0.1984 ± 0.0090 | 0.0791 ± 0.0094 | 0.1667 ± 0.0134 | 0.4748 ± 0.0174 |

### MOTIF / IMDb / Movie-Year (full-type classification: 91 classes)

Preliminary frozen zero-shot evaluation on the test split; 834 queries. Predict the actual calendar year among all 91 target-type entities. Precision and recall are macro-averaged over this fixed class set with zero division set to zero. Micro-F1 equals accuracy for single-label prediction. Top-1 ties use the smallest global entity ID.

| Input | Accuracy | Precision (macro) | Recall (macro) | Micro-F1 | Macro-F1 |
|---|---:|---:|---:|---:|---:|
| compiled/v1 | 0.0396 ± 0.0068 | 0.0102 ± 0.0021 | 0.0113 ± 0.0022 | 0.0396 ± 0.0068 | 0.0101 ± 0.0019 |
| compiled/v2 | 0.0396 ± 0.0068 | 0.0102 ± 0.0021 | 0.0113 ± 0.0022 | 0.0396 ± 0.0068 | 0.0101 ± 0.0019 |
| compiled/v3 | 0.0396 ± 0.0068 | 0.0102 ± 0.0021 | 0.0113 ± 0.0022 | 0.0396 ± 0.0068 | 0.0101 ± 0.0019 |
| compiled/v4 | 0.0396 ± 0.0068 | 0.0102 ± 0.0021 | 0.0113 ± 0.0022 | 0.0396 ± 0.0068 | 0.0101 ± 0.0019 |
| physical/v1 | 0.0360 ± 0.0065 | 0.0118 ± 0.0029 | 0.0142 ± 0.0040 | 0.0360 ± 0.0065 | 0.0120 ± 0.0028 |
| physical/v2 | 0.0456 ± 0.0072 | 0.0005 ± 0.0001 | 0.0110 ± 0.0000 | 0.0456 ± 0.0072 | 0.0010 ± 0.0001 |
| physical/v3 | 0.0180 ± 0.0046 | 0.0013 ± 0.0009 | 0.0043 ± 0.0009 | 0.0180 ± 0.0046 | 0.0011 ± 0.0004 |
| physical/v4 | 0.0480 ± 0.0074 | 0.0141 ± 0.0034 | 0.0137 ± 0.0023 | 0.0480 ± 0.0074 | 0.0127 ± 0.0022 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary frozen zero-shot evaluation on the test split; 834 queries. Both columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v2 | 0.2410 ± 0.0146 | 0.6166 ± 0.0085 |
| v1 vs v3 | 0.3465 ± 0.0160 | 0.6748 ± 0.0075 |
| v1 vs v4 | 0.7806 ± 0.0147 | 0.9101 ± 0.0038 |
| v2 vs v3 | 0.6379 ± 0.0174 | 0.9114 ± 0.0043 |
| v2 vs v4 | 0.2950 ± 0.0153 | 0.6672 ± 0.0082 |
| v3 vs v4 | 0.2518 ± 0.0151 | 0.6433 ± 0.0083 |

### MOTIF / IMDb / Movie-Year (inference noise floor)

Preliminary frozen zero-shot evaluation on the test split; 834 queries. Independent inference processes with identical graph and checkpoint; original 20 candidates per query.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v1 repeat | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 |

Reference repeat bitwise identical: True.
Compiled inputs identical: True; compiled full-type scores bitwise identical: True.
Coverage: complete

