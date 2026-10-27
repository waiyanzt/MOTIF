# IMDb Movie--Director: seed-averaged results

Mean ± population std over training seeds (20241017, 20251017, 1566911444); zero-shot has no training seed (std 0). FT rows use the model trained and tested on the same variant.

## Performance

| Method | Variant | MRR | Hits@1 | Hits@3 | Precision | Recall |
|---|---|---:|---:|---:|---:|---:|
| CMPNN | v1 | 0.4152 ± 0.0109 | 0.2604 ± 0.0071 | 0.4394 ± 0.0264 | 0.0979 ± 0.0050 | 0.7835 ± 0.0269 |
| CMPNN | v3 | 0.3430 ± 0.0072 | 0.1707 ± 0.0057 | 0.3724 ± 0.0139 | 0.0893 ± 0.0028 | 0.7951 ± 0.0182 |
| MOTIF (ZS) | v1 | 0.3188 ± 0.0000 | 0.2069 ± 0.0000 | 0.3110 ± 0.0000 | 0.4247 ± 0.0000 | 0.1519 ± 0.0000 |
| MOTIF (ZS) | v3 | 0.2561 ± 0.0000 | 0.1208 ± 0.0000 | 0.2596 ± 0.0000 | 0.0870 ± 0.0000 | 0.0024 ± 0.0000 |
| MOTIF (FT) | v1 | 0.4086 ± 0.0022 | 0.2524 ± 0.0113 | 0.4075 ± 0.0148 | 0.0963 ± 0.0037 | 0.8118 ± 0.0218 |
| MOTIF (FT) | v3 | 0.3986 ± 0.0035 | 0.2532 ± 0.0056 | 0.3796 ± 0.0011 | 0.0920 ± 0.0023 | 0.8349 ± 0.0195 |

## Invariance

| Method | Comparison | Kendall-τ |
|---|---|---:|
| CMPNN | v1 vs v3 | 0.7819 ± 0.0238 |
| MOTIF (ZS) | v1 vs v3 | 0.8343 ± 0.0000 |
| MOTIF (FT) | v1 vs v3 | 0.7815 ± 0.0151 |
