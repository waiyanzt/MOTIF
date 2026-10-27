# Preliminary MOTIF fine-tuning: guide candidate protocol

All metrics rank the positive target against the same 19 fixed negative targets.
Four independently fine-tuned checkpoints; 16 train/test cells.
Error bars are query-bootstrap SE. Training-repeat and multi-seed comparisons remain pending.

## MRR

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.2028 +/- 0.0090 | 0.1875 +/- 0.0087 | 0.1724 +/- 0.0075 | 0.2225 +/- 0.0095 |
| v2 | 0.2183 +/- 0.0092 | 0.1823 +/- 0.0085 | 0.1551 +/- 0.0070 | 0.2311 +/- 0.0096 |
| v3 | 0.2092 +/- 0.0094 | 0.1913 +/- 0.0089 | 0.2110 +/- 0.0093 | 0.2006 +/- 0.0095 |
| v4 | 0.2140 +/- 0.0093 | 0.1922 +/- 0.0088 | 0.1722 +/- 0.0077 | 0.2253 +/- 0.0094 |

## Hits@1

| Train / Test | v1 | v2 | v3 | v4 |
|---|---:|---:|---:|---:|
| v1 | 0.0839 +/- 0.0094 | 0.0683 +/- 0.0092 | 0.0528 +/- 0.0076 | 0.0971 +/- 0.0100 |
| v2 | 0.0983 +/- 0.0097 | 0.0659 +/- 0.0087 | 0.0420 +/- 0.0070 | 0.1067 +/- 0.0103 |
| v3 | 0.0851 +/- 0.0097 | 0.0767 +/- 0.0094 | 0.0923 +/- 0.0100 | 0.0839 +/- 0.0102 |
| v4 | 0.0887 +/- 0.0098 | 0.0707 +/- 0.0090 | 0.0564 +/- 0.0079 | 0.1007 +/- 0.0100 |

Exactly two presentation tables:
- `transfer_performance.tex`: MRR and Hits@1/3/10 for all train/test cells.
- `invariance.tex`: C-a pairs between independently trained diagonal models, followed by C-b test-variant pairs grouped by fixed checkpoint. Regime and Train columns distinguish them.
Original numerical records are retained; extra full-year metrics are not presented.
