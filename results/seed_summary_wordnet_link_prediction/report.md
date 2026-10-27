# WN18RR: seed-averaged results

Mean ± population std over training seeds (20241017, 20251017, 1566911444); MOTIF (PT) is the released checkpoint, which was pretrained on WN18RR (v1's graph), so it is not zero-shot; its spread is over the three seeds' candidate draws (ranking metrics are exact). MOTIF ran on one H200, CMPNN on V100. FT rows use the model trained and tested on the same variant.

## Performance

| Method | Variant | MRR | Hits@1 | Hits@3 | Precision | Recall |
|---|---|---:|---:|---:|---:|---:|
| CMPNN | v1 | 0.4238 ± 0.0095 | 0.3680 ± 0.0105 | 0.4418 ± 0.0107 | 0.1397 ± 0.0022 | 0.9399 ± 0.0026 |
| CMPNN | v2 | 0.3075 ± 0.0559 | 0.2879 ± 0.0697 | 0.3125 ± 0.0538 | 0.9426 ± 0.0647 | 0.3009 ± 0.0749 |
| CMPNN | v3 | 0.2927 ± 0.0306 | 0.2186 ± 0.0281 | 0.3300 ± 0.0319 | 0.4584 ± 0.0437 | 0.6406 ± 0.0259 |
| MOTIF (PT) | v1 | 0.5199 ± 0.0000 | 0.4681 ± 0.0000 | 0.5384 ± 0.0000 | 0.4331 ± 0.0027 | 0.8572 ± 0.0000 |
| MOTIF (PT) | v2 | 0.1450 ± 0.0000 | 0.0769 ± 0.0000 | 0.1362 ± 0.0000 | 0.7286 ± 0.0034 | 0.6153 ± 0.0000 |
| MOTIF (PT) | v3 | 0.3812 ± 0.0000 | 0.3553 ± 0.0000 | 0.3803 ± 0.0000 | 0.8479 ± 0.0085 | 0.4911 ± 0.0000 |
| MOTIF (FT) | v1 | 0.5163 ± 0.0016 | 0.4639 ± 0.0010 | 0.5353 ± 0.0023 | 0.4628 ± 0.0504 | 0.8291 ± 0.0141 |
| MOTIF (FT) | v2 | 0.3964 ± 0.0096 | 0.3601 ± 0.0072 | 0.4012 ± 0.0149 | 0.9914 ± 0.0029 | 0.3479 ± 0.0008 |
| MOTIF (FT) | v3 | 0.4302 ± 0.0031 | 0.3918 ± 0.0022 | 0.4384 ± 0.0032 | 0.9409 ± 0.0146 | 0.5200 ± 0.0282 |

## Invariance

| Method | Comparison | Kendall-τ |
|---|---|---:|
| CMPNN | v1 vs v2 | -0.0706 ± 0.0827 |
| CMPNN | v1 vs v3 | 0.1974 ± 0.0362 |
| CMPNN | v2 vs v3 | -0.0399 ± 0.1129 |
| MOTIF (PT) | v1 vs v2 | 0.5272 ± 0.0012 |
| MOTIF (PT) | v1 vs v3 | 0.2753 ± 0.0011 |
| MOTIF (PT) | v2 vs v3 | 0.2677 ± 0.0010 |
| MOTIF (FT) | v1 vs v2 | 0.4119 ± 0.0119 |
| MOTIF (FT) | v1 vs v3 | 0.1621 ± 0.0485 |
| MOTIF (FT) | v2 vs v3 | 0.2183 ± 0.0759 |
