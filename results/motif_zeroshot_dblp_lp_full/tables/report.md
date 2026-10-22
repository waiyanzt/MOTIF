# Preliminary MOTIF zero-shot evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
Classification predicts the actual target entity over the full target-type pool; macro averages include every pool class, zero_division=0.
Micro-F1 equals accuracy in this single-label setting. Top-1 ties use the smallest global tail id.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / DBLP / Paper-Conference (20-candidate link prediction)

Preliminary frozen zero-shot evaluation on the test split; 2666 queries. Tail-only ranking over all 20 conferences. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| compiled/v1 | 0.5761 ± 0.0066 | 0.3796 ± 0.0092 | 0.7198 ± 0.0082 | 0.9392 ± 0.0048 |
| compiled/v2 | 0.5761 ± 0.0066 | 0.3796 ± 0.0092 | 0.7198 ± 0.0082 | 0.9392 ± 0.0048 |
| compiled/v3 | 0.5761 ± 0.0066 | 0.3796 ± 0.0092 | 0.7198 ± 0.0082 | 0.9392 ± 0.0048 |
| physical/v1 | 0.5810 ± 0.0067 | 0.3886 ± 0.0093 | 0.7243 ± 0.0082 | 0.9370 ± 0.0050 |
| physical/v2 | 0.5696 ± 0.0069 | 0.3800 ± 0.0094 | 0.7052 ± 0.0084 | 0.9280 ± 0.0052 |
| physical/v3 | 0.5727 ± 0.0068 | 0.3830 ± 0.0092 | 0.7089 ± 0.0083 | 0.9351 ± 0.0050 |

### MOTIF / DBLP / Paper-Conference (full-type classification: 20 classes)

Preliminary frozen zero-shot evaluation on the test split; 2666 queries. Predict the actual conference among all 20 target-type entities. Precision and recall are macro-averaged over this fixed class set with zero division set to zero. Micro-F1 equals accuracy for single-label prediction. Top-1 ties use the smallest global entity ID.

| Input | Accuracy | Precision (macro) | Recall (macro) | Micro-F1 | Macro-F1 |
|---|---:|---:|---:|---:|---:|
| compiled/v1 | 0.3796 ± 0.0092 | 0.3061 ± 0.0128 | 0.3129 ± 0.0091 | 0.3796 ± 0.0092 | 0.2957 ± 0.0093 |
| compiled/v2 | 0.3796 ± 0.0092 | 0.3061 ± 0.0128 | 0.3129 ± 0.0091 | 0.3796 ± 0.0092 | 0.2957 ± 0.0093 |
| compiled/v3 | 0.3796 ± 0.0092 | 0.3061 ± 0.0128 | 0.3129 ± 0.0091 | 0.3796 ± 0.0092 | 0.2957 ± 0.0093 |
| physical/v1 | 0.3886 ± 0.0093 | 0.3203 ± 0.0140 | 0.3077 ± 0.0090 | 0.3886 ± 0.0093 | 0.2955 ± 0.0094 |
| physical/v2 | 0.3800 ± 0.0094 | 0.3339 ± 0.0161 | 0.2907 ± 0.0084 | 0.3800 ± 0.0094 | 0.2831 ± 0.0096 |
| physical/v3 | 0.3830 ± 0.0092 | 0.3231 ± 0.0152 | 0.2938 ± 0.0084 | 0.3830 ± 0.0092 | 0.2847 ± 0.0093 |

### MOTIF / DBLP / Paper-Conference (20-candidate invariance)

Preliminary frozen zero-shot evaluation on the test split; 2666 queries. Both columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v2 | 0.8953 ± 0.0057 | 0.9506 ± 0.0005 |
| v1 vs v3 | 0.9070 ± 0.0058 | 0.9570 ± 0.0005 |
| v2 vs v3 | 0.9156 ± 0.0055 | 0.9591 ± 0.0004 |

### MOTIF / DBLP / Paper-Conference (inference noise floor)

Preliminary frozen zero-shot evaluation on the test split; 2666 queries. Independent inference processes with identical graph and checkpoint; original 20 candidates per query.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v1 repeat | 1.0000 ± 0.0000 | 1.0000 ± 0.0000 |

Reference repeat bitwise identical: True.
Compiled inputs identical: True; compiled full-type scores bitwise identical: True.
Coverage: complete

