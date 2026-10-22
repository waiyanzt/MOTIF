# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
Classification predicts the actual target entity over the full target-type pool; macro averages include every pool class, zero_division=0.
Micro-F1 equals accuracy in this single-label setting. Top-1 ties use the smallest global tail id.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2140 ± 0.0093 | 0.0887 ± 0.0098 | 0.2026 ± 0.0134 | 0.4928 ± 0.0173 |
| physical/v2 | 0.1922 ± 0.0088 | 0.0707 ± 0.0090 | 0.1691 ± 0.0133 | 0.4796 ± 0.0173 |
| physical/v3 | 0.1722 ± 0.0077 | 0.0564 ± 0.0079 | 0.1331 ± 0.0119 | 0.4400 ± 0.0170 |
| physical/v4 | 0.2253 ± 0.0094 | 0.1007 ± 0.0100 | 0.2098 ± 0.0138 | 0.5096 ± 0.0175 |

### MOTIF / IMDb / Movie-Year (full-type classification: 91 classes)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. Predict the actual calendar year among all 91 target-type entities. Precision and recall are macro-averaged over this fixed class set with zero division set to zero. Micro-F1 equals accuracy for single-label prediction. Top-1 ties use the smallest global entity ID.

| Input | Accuracy | Precision (macro) | Recall (macro) | Micro-F1 | Macro-F1 |
|---|---:|---:|---:|---:|---:|
| physical/v1 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v2 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v3 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v4 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v4, selected by validation MRR. Both columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v2 | 0.2602 ± 0.0155 | 0.1068 ± 0.0070 |
| v1 vs v3 | 0.4125 ± 0.0169 | 0.2969 ± 0.0073 |
| v1 vs v4 | 0.7206 ± 0.0153 | 0.7498 ± 0.0054 |
| v2 vs v3 | 0.4700 ± 0.0176 | 0.5366 ± 0.0066 |
| v2 vs v4 | 0.2554 ± 0.0149 | 0.1105 ± 0.0076 |
| v3 vs v4 | 0.2878 ± 0.0156 | 0.3154 ± 0.0077 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

