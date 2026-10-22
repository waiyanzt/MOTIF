# Preliminary MOTIF evaluation

Uncertainty: estimate ± bootstrap SE; 1000 query resamples, seed 0. Percentile 95% CIs are in JSON/CSV.
LP uses each query's original positive + 19 fixed negatives, average ranks for ties.
Classification predicts the actual target entity over the full target-type pool; macro averages include every pool class, zero_division=0.
Micro-F1 equals accuracy in this single-label setting. Top-1 ties use the smallest global tail id.
Invariance uses the original 20 candidates. Identical score vectors have tau=1; undefined nonidentical constant-vector tau is assigned 0 and counted in JSON.

### MOTIF / IMDb / Movie-Year (20-candidate link prediction)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Tail-only ranking over the true year plus 19 fixed frequency-matched negative years per query. Tied scores use average rank.

| Input | MRR | Hits@1 | Hits@3 | Hits@10 |
|---|---:|---:|---:|---:|
| physical/v1 | 0.2028 ± 0.0090 | 0.0839 ± 0.0094 | 0.1787 ± 0.0131 | 0.4772 ± 0.0173 |
| physical/v2 | 0.1875 ± 0.0087 | 0.0683 ± 0.0092 | 0.1583 ± 0.0127 | 0.4580 ± 0.0175 |
| physical/v3 | 0.1724 ± 0.0075 | 0.0528 ± 0.0076 | 0.1403 ± 0.0114 | 0.4460 ± 0.0176 |
| physical/v4 | 0.2225 ± 0.0095 | 0.0971 ± 0.0100 | 0.2062 ± 0.0138 | 0.4976 ± 0.0177 |

### MOTIF / IMDb / Movie-Year (full-type classification: 91 classes)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Predict the actual calendar year among all 91 target-type entities. Precision and recall are macro-averaged over this fixed class set with zero division set to zero. Micro-F1 equals accuracy for single-label prediction. Top-1 ties use the smallest global entity ID.

| Input | Accuracy | Precision (macro) | Recall (macro) | Micro-F1 | Macro-F1 |
|---|---:|---:|---:|---:|---:|
| physical/v1 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v2 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v3 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |
| physical/v4 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 | 0.0110 ± 0.0053 | 0.0012 ± 0.0012 | 0.0000 ± 0.0000 |

### MOTIF / IMDb / Movie-Year (20-candidate invariance)

Preliminary fine-tuned checkpoint evaluation on the test split; 834 queries. Checkpoint fine-tuned on physical/v1, selected by validation MRR. Both columns use the same original 20 candidates per query. Agreement@1 compares predicted entity IDs; Kendall tau-b compares candidate rankings within each query and is then averaged over queries. Representation differences must be interpreted against the reference-repeat noise floor.

| Input | Agreement@1 | Kendall $\tau_b$ |
|---|---:|---:|
| v1 vs v2 | 0.1739 ± 0.0133 | 0.3876 ± 0.0073 |
| v1 vs v3 | 0.3177 ± 0.0159 | 0.4727 ± 0.0067 |
| v1 vs v4 | 0.6499 ± 0.0162 | 0.7616 ± 0.0052 |
| v2 vs v3 | 0.3082 ± 0.0156 | 0.5590 ± 0.0058 |
| v2 vs v4 | 0.2818 ± 0.0153 | 0.4146 ± 0.0076 |
| v3 vs v4 | 0.2866 ± 0.0150 | 0.3731 ± 0.0074 |

Reference repeat bitwise identical: not run.
Compiled inputs identical: None; compiled full-type scores bitwise identical: None.
Coverage: complete

