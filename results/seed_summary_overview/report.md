# Overview: averages over all variants

## Link prediction

| Dataset | Method | MRR | Hits@1 | |Δ| MRR | |Δ| Hits@1 | Kendall-τ |
|---|---|---:|---:|---:|---:|---:|
| IMDb Movie–Year | CMPNN | 0.1918 | 0.0680 | 0.0028 | 0.0042 | 0.1392 |
| IMDb Movie–Year | MOTIF (ZS) | 0.1810 ± 0.0000 | 0.0641 ± 0.0000 | 0.0232 | 0.0220 | 0.7372 ± 0.0000 |
| IMDb Movie–Year | MOTIF (FT) | 0.2166 ± 0.0042 | 0.0888 ± 0.0042 | 0.0269 | 0.0219 | 0.2351 ± 0.0840 |
| IMDb Movie–Director | CMPNN | 0.3791 | 0.2156 | 0.0722 | 0.0897 | 0.7819 |
| IMDb Movie–Director | MOTIF (ZS) | 0.2874 ± 0.0000 | 0.1639 ± 0.0000 | 0.0627 | 0.0861 | 0.8343 ± 0.0000 |
| IMDb Movie–Director | MOTIF (FT) | 0.4036 ± 0.0028 | 0.2528 ± 0.0081 | 0.0100 | 0.0008 | 0.7815 ± 0.0151 |
| DBLP Paper–Conference | CMPNN | 0.6159 | 0.4102 | 0.0042 | 0.0043 | 0.7423 |
| DBLP Paper–Conference | MOTIF (ZS) | 0.5744 ± 0.0000 | 0.3838 ± 0.0000 | 0.0076 | 0.0058 | 0.9556 ± 0.0000 |
| DBLP Paper–Conference | MOTIF (FT) | 0.6084 ± 0.0013 | 0.4079 ± 0.0020 | 0.0126 | 0.0103 | 0.8405 ± 0.0284 |
| WN18RR | CMPNN | 0.3413 | 0.2915 | 0.0874 | 0.0996 | 0.0290 |
| WN18RR | MOTIF (PT) | 0.3487 ± 0.0000 | 0.3001 ± 0.0000 | 0.2500 | 0.2608 | 0.3567 ± 0.0009 |
| WN18RR | MOTIF (FT) | 0.4476 ± 0.0031 | 0.4053 ± 0.0020 | 0.0799 | 0.0692 | 0.2641 ± 0.0427 |

## Node classification

| Dataset | Method | Accuracy | |Δ| Accuracy | Kendall-τ |
|---|---|---:|---:|---:|
| IMDb genre | RGCN | 0.6305 | 0.0293 | 0.7844 |
| IMDb genre | SlotGAT | 0.6547 | 0.0084 | 0.7639 |
| IMDb genre | MOTIF (ZS) | 0.5048 ± 0.0000 | 0.1340 | 0.5574 ± 0.0000 |
| IMDb genre | MOTIF (FT) | 0.6022 ± 0.0029 | 0.0088 | 0.8296 ± 0.0221 |

Averages and Kendall-τ for MOTIF are taken within each training seed, then mean ± population std over the three seeds; ZS/PT is a single frozen run. |Δ| is the mean absolute difference between the per-variant means over all variant pairs, computed the same way for every method (no ±). Baseline rows are exact averages of the lab's per-variant means, whose per-seed values are unavailable, so they carry no ±. Kendall-τ is the mean over all variant pairs.
