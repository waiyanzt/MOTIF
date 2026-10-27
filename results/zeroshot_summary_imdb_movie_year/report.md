# IMDB movie--year: seed-averaged results

Zero-shot only (std 0). FT rows use the model trained and tested on the same variant.

## Performance

| Method | Variant | MRR | Hits@1 | Hits@3 | Precision | Recall |
|---|---|---:|---:|---:|---:|---:|
| MOTIF (ZS) | v1 | 0.1802 ± 0.0000 | 0.0624 ± 0.0000 | 0.1379 ± 0.0000 | 0.0481 ± 0.0000 | 0.3549 ± 0.0000 |
| MOTIF (ZS) | v2 | 0.1901 ± 0.0000 | 0.0755 ± 0.0000 | 0.1487 ± 0.0000 | 0.0498 ± 0.0000 | 0.8621 ± 0.0000 |
| MOTIF (ZS) | v3 | 0.1553 ± 0.0000 | 0.0396 ± 0.0000 | 0.1055 ± 0.0000 | 0.0497 ± 0.0000 | 0.8717 ± 0.0000 |
| MOTIF (ZS) | v4 | 0.1984 ± 0.0000 | 0.0791 ± 0.0000 | 0.1667 ± 0.0000 | 0.0499 ± 0.0000 | 0.7314 ± 0.0000 |

## Invariance

| Method | Comparison | Kendall-τ |
|---|---|---:|
| MOTIF (ZS) | v1 vs v2 | 0.6166 ± 0.0000 |
| MOTIF (ZS) | v1 vs v3 | 0.6748 ± 0.0000 |
| MOTIF (ZS) | v1 vs v4 | 0.9101 ± 0.0000 |
| MOTIF (ZS) | v2 vs v3 | 0.9114 ± 0.0000 |
| MOTIF (ZS) | v2 vs v4 | 0.6672 ± 0.0000 |
| MOTIF (ZS) | v3 vs v4 | 0.6433 ± 0.0000 |
