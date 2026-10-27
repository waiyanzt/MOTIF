# DBLP paper--conference: seed-averaged results

Zero-shot only (std 0). FT rows use the model trained and tested on the same variant.

## Performance

| Method | Variant | MRR | Hits@1 | Hits@3 | Precision | Recall |
|---|---|---:|---:|---:|---:|---:|
| MOTIF (ZS) | v1 | 0.5810 ± 0.0000 | 0.3886 ± 0.0000 | 0.7243 ± 0.0000 | 0.1858 ± 0.0000 | 0.6992 ± 0.0000 |
| MOTIF (ZS) | v2 | 0.5696 ± 0.0000 | 0.3800 ± 0.0000 | 0.7052 ± 0.0000 | 0.1331 ± 0.0000 | 0.8323 ± 0.0000 |
| MOTIF (ZS) | v3 | 0.5727 ± 0.0000 | 0.3830 ± 0.0000 | 0.7089 ± 0.0000 | 0.1179 ± 0.0000 | 0.8740 ± 0.0000 |

## Invariance

| Method | Comparison | Kendall-τ |
|---|---|---:|
| MOTIF (ZS) | v1 vs v2 | 0.9506 ± 0.0000 |
| MOTIF (ZS) | v1 vs v3 | 0.9570 ± 0.0000 |
| MOTIF (ZS) | v2 vs v3 | 0.9591 ± 0.0000 |
