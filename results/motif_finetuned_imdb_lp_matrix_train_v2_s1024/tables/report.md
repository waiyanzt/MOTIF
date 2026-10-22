# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
Classification predicts the actual target entity over the full target-type pool; macro averages include every pool class, zero_division=0.
Micro-F1 equals accuracy in this single-label setting. Top-1 ties use the smallest global tail id.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2183 ± 0.0092 | 0.0983 ± 0.0097 | 0.1954 ± 0.0134 | 0.4988 ± 0.0172 |
| physical/v2 | 0.1823 ± 0.0085 | 0.0659 ± 0.0087 | 0.1427 ± 0.0123 | 0.4592 ± 0.0179 |
| physical/v3 | 0.1551 ± 0.0070 | 0.0420 ± 0.0070 | 0.1091 ± 0.0108 | 0.4365 ± 0.0174 |
| physical/v4 | 0.2311 ± 0.0096 | 0.1067 ± 0.0103 | 0.2146 ± 0.0142 | 0.5180 ± 0.0174 |

### MOTIF / IMDb / Movie-Year (full-type classification: 91 classes)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Predict the actual calendar year among all 91 target-type entities. Precision and recall are macro-averaged over this fixed class set with zero division set to zero. Micro-F1 equals accuracy for single-label prediction. Top-1 ties use the smallest global entity ID.

| Input | Accuracy | Precision (macro) | Recall (macro) | Micro-F1 | Macro-F1 |
|---|---:|---:|---:|---:|---:|
| physical/v1 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v2 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v3 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v4 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v2, selected by validation MRR. Both columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v2 | 0.4341 ± 0.0174 | 0.5165 ± 0.0064 |
| v1 vs v3 | 0.3106 ± 0.0164 | 0.4115 ± 0.0088 |
| v1 vs v4 | 0.7806 ± 0.0146 | 0.8280 ± 0.0048 |
| v2 vs v3 | 0.2818 ± 0.0159 | 0.6368 ± 0.0061 |
| v2 vs v4 | 0.3969 ± 0.0177 | 0.4918 ± 0.0071 |
| v3 vs v4 | 0.1595 ± 0.0127 | 0.3032 ± 0.0094 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

