# Results discussion: MOTIF vs CMPNN across representation variants

Working notes on the tables in `results/overleaf/motif_seed_tables/main.tex` (state as of
2026-10-27). All four tasks with a CMPNN baseline are complete.

---

## 1. What is being compared

**Question.** We evaluate a graph foundation model (MOTIF) on the lab's datasets and
preprocessing. How well does it perform, and how *invariant* is it when the same data is
encoded in a different but equivalent graph representation? We compare it against the
lab's "engine", CMPNN.

**Rows in every table**

| Row | Meaning |
|---|---|
| **CMPNN** | The lab's "original" arm: one model trained per variant and seed, with numbers taken from `SCR/INV-GNN-12D9/docs/results/*_lp.tex`. |
| **MOTIF (ZS)** | The released `motif_3g.pth` checkpoint, frozen, run directly on each variant. It is pretrained on FB15k-237, WN18RR and CoDEx-M and has never seen IMDb or DBLP. |
| **MOTIF (FT)** | The same checkpoint fine-tuned separately on each variant (1,000 steps, untuned pilot recipe). This is the analogue of CMPNN's "original" arm. |

**Metrics** (definitions follow `SCR/.../docs/results/METRICS.md`, so they are comparable with CMPNN)

* **MRR / Hits@1 / Hits@3**: rank of the true answer among the candidates, with ties averaged.
  IMDb and DBLP use 20 candidates per query. WN18RR ranks against all 40,943 entities.
* **Precision / Recall**: every (query, candidate) pair counts as one yes/no prediction,
  "yes" when σ(score) ≥ 0.5, pooled over all pairs. These measure **calibration**
  (where the 0.5 threshold falls), not ranking quality.
* **Kendall-τ (our "invariance" measure)**: for each test query, the same candidates are scored
  on two variants. τ_b measures how often a pair of candidates keeps its order between them,
  averaged over queries (METRICS.md §4.1). τ = 1 means identical rankings; 0 means unrelated
  rankings. It measures **ranking invariance**, not whether the predictions are correct.
* **±**: population std over the lab's three training seeds (1566911444, 20241017,
  20251017). ZS has no training seed, so its ± is 0. This is a property of the setup and
  does not mean ZS is more reliable.

**Reference points I added** (not in the tables)

| Dataset | Chance MRR | Simple structural heuristic | Seed floor for MOTIF (FT) τ |
|---|---|---|---|
| IMDb Movie–Year | 0.193 (from METRICS.md) | – | 0.39–0.55 |
| IMDb Movie–Director | 0.180 (20 distinct candidates) | prior-only 0.280; **co-actor vote 0.350** | 0.82–0.83 |
| DBLP Paper–Conference | 0.180 | prior-only 0.321; **co-author vote 0.559** | 0.83–0.90 |

The **seed floor** is the τ between two MOTIF (FT) models trained on the *same* variant with
different seeds. It is the disagreement caused by training randomness alone. A cross-variant
τ near the floor means that changing the representation causes no more disagreement than
reseeding. A cross-variant τ well below the floor means the representation genuinely changes
what the model learns. (No seed floor is available for CMPNN; see section 7.)

---

## 2. Headline findings

> **Read the τ comparisons with this in mind.** MOTIF (ZS) is *one* frozen model run on two
> graphs, so its τ reflects only sensitivity to the representation. CMPNN's τ compares
> *two separately trained models*, so it also includes training randomness. ZS vs CMPNN is
> therefore not like-for-like. The fair comparison is **MOTIF (FT) vs CMPNN**: both train one
> model per variant.

1. **Frozen MOTIF's rankings change less across representations than CMPNN's, but it
   trails CMPNN on accuracy.** Zero-shot τ is 0.96 vs 0.74 on DBLP, 0.74 vs 0.14 on
   Movie–Year, and only 0.83 vs 0.78 on Movie–Director. Part of this gap is the frozen
   model's missing training variance (see above). Zero-shot MRR is lower than CMPNN on
   every task.
2. **Fine-tuning closes the accuracy gap and often beats CMPNN.** MOTIF (FT) is within
   0.01 on DBLP, ties or beats it on Movie–Director, is the only model above chance on
   Movie–Year, and **beats CMPNN on all three WN18RR variants** (+.09 to +.14 MRR; MOTIF was
   pretrained on WN18RR).
3. **Fine-tuning makes MOTIF *less* invariant, not more.** Each variant gets its own
   fine-tuned copy, so the copies drift apart:

   | τ (mean over pairs) | ZS / PT | FT | Change | CMPNN | FT seed floor |
   |---|---|---|---|---|---|
   | DBLP | .956 | .841 | −.115 | .742 | .83–.90 |
   | Movie–Director | .834 | .782 | −.052 | .782 | .82–.83 |
   | Movie–Year | .737 | .235 | −.502 | .139 | .39–.55 |
   | WN18RR | .357 | .264 | −.093 | .029 | .48–.67 |

   On DBLP and Movie–Director, the remaining disagreement is at or near the **seed floor**,
   so it comes from training noise, not the representation. On Movie–Year and WN18RR it is
   clearly below the floor, so the representation does change what is learned. In every case
   fine-tuned MOTIF ends at or above CMPNN's τ.
4. **Rank invariance and accuracy invariance are different properties.** On DBLP, MOTIF
   ranks more consistently than CMPNN, yet its MRR varies *more* across variants. On
   Movie–Director the reverse holds: fine-tuned MOTIF's MRR is nearly flat across variants,
   while CMPNN loses 0.07 on v3.
5. **Precision and Recall mostly reflect calibration.** They swing with the model's score
   scale (especially zero-shot) and should not be read as a quality ranking.

---

## 3. DBLP Paper–Conference (v1–v3; the Area attribute is attached to paper / conference / author)

| | MRR v1 / v2 / v3 | Mean | Spread | τ (mean of 3 pairs) |
|---|---|---|---|---|
| CMPNN | .620 / .613 / .615 | .616 | .006 | .742 |
| MOTIF (ZS) | .581 / .570 / .573 | .574 | .011 | **.956** |
| MOTIF (FT) | .606 / .600 / .619 | .608 | .019 | .841 (seed floor .83–.90) |

* **Zero-shot is strong but mostly reproduces an easy heuristic.** It reaches 93% of
  CMPNN's MRR without ever seeing DBLP. However, a co-author majority vote already gets
  0.559, so MOTIF's zero-shot adds only about 0.015 over "papers by the same authors share
  venues". DBLP is a homophily-dominated task, which suits path-based reasoning. A leakage
  audit found no test (paper, conference) edges, and the derived Area edges in v2/v3 come
  from training papers only.
* **Fine-tuning:** v3 ties CMPNN (.619 vs .615), and v1/v2 trail by about 0.013. Hits@1 is
  level with CMPNN. **Hits@3 is consistently lower** (.76–.79 vs .78–.80), so MOTIF's
  second and third choices are weaker.
* **Calibration:** MOTIF (FT) has higher Precision (.28–.30 vs .21–.22) and lower Recall
  (.69–.71 vs .81–.89); it predicts "positive" less often. F1 is higher for MOTIF
  (≈ .40 vs .35 on v1).
* **Invariance:** MOTIF (FT)'s cross-variant τ (.81–.90) sits on its seed floor
  (.83–.90). After fine-tuning, MOTIF disagrees across representations about as much as it
  disagrees with itself across seeds. CMPNN's τ is lower (.69–.83), but without its seed
  floor we cannot say how much of that comes from the representation.
* **The accuracy-invariance paradox:** despite the higher τ, MOTIF's MRR spread across
  variants (.011 for ZS, .019 for FT) is larger than CMPNN's (.006). The consistently
  ranked candidates are not the ones that decide the top rank.

## 4. IMDb Movie–Director (v1, v3; the actor is attached to the movie vs the link node)

| | MRR v1 / v3 | Mean | Spread | τ (v1 vs v3) |
|---|---|---|---|---|
| CMPNN | .415 / .343 | .379 | **.072** | .782 |
| MOTIF (ZS) | .319 / .256 | .288 | .063 | .834 |
| MOTIF (FT) | .409 / .399 | **.404** | **.010** | .782 (seed floor .82–.83) |

* **This is the strongest result for MOTIF.** Fine-tuned MOTIF ties CMPNN on v1
  (.409 vs .415) and **beats it clearly on v3 (.399 vs .343)**. Its accuracy is nearly
  invariant to where the actor is attached (spread .010), whereas CMPNN loses 0.07 when the
  actor moves to the link node. Hits@1 tells the same story: .252/.253 vs .260/.171.
* **Zero-shot is weak here:** .319/.256, below the co-actor heuristic (.350), and v3 is
  below even the prior-only baseline (.280). With the actor moved onto the link node,
  frozen MOTIF loses the signal.
* **Zero-shot calibration is odd.** On v1, Precision is .42 and Recall .15; on v3, Recall
  is .002. Frozen MOTIF scores almost every candidate below 0 on these graphs. This is a
  calibration effect and does not affect ranking.
* **Invariance:** fine-tuned τ (.78) is close to its seed floor (.82–.83), so most of the
  cross-variant disagreement is training noise. It equals CMPNN's τ (.78), but MOTIF's
  *accuracy* is the more invariant of the two.

## 5. IMDb Movie–Year (v1–v4; director and actor each attached to the movie or the link node)

| | MRR v1 / v2 / v3 / v4 | Mean | τ (mean of 6 pairs) |
|---|---|---|---|
| chance | .193 | | |
| CMPNN | .189 / .193 / .194 / .192 | .192 | .139 |
| MOTIF (ZS) | .180 / .190 / .155 / .198 | .181 | **.737** |
| MOTIF (FT) | **.240** / .198 / .198 / **.231** | .217 | .235 (seed floor .39–.55) |

* **This task is close to unlearnable from structure.** CMPNN sits exactly at chance on
  every variant. Treat everything here as low-signal. A check on the v1 graph shows why:
  * The true year appears among the years of movies sharing an actor or director for
    **34.3%** of test movies. A *wrong* candidate year appears there **35.3%** of the time,
    so collaborators' exact years carry no information.
  * Voting for collaborators' exact years scores MRR **.153**, below chance. The 19 wrong
    candidates are drawn by year popularity with replacement (14.8 distinct per query), so
    popular-year guesses get punished.
  * Only a coarse **era** signal exists: voting for years within ±3 of collaborators'
    years scores .224. The models see years as unordered nodes (nothing says 1995 is next
    to 1996) and have no per-node embeddings, so they would have to infer era from
    shared-actor structure. Fine-tuned MOTIF's .240 on v1 is about the era heuristic's level.
* **Fine-tuned MOTIF is the only model above chance**, on v1 and v4 (+0.04–0.05 MRR,
  about 10× the seed std). It stays at chance on v2/v3. The variants where it learns are
  the two where the **actor is attached to the movie** (v1 and v4, by the IMDb placement
  table in `SCR/.../models/RGCN/preprocess_IMDB_rgcn_structural.py`). That suggests the
  usable signal for the year comes through actors, and MOTIF finds it only when the actor
  is one hop from the movie.
* **Zero-shot is consistent but uninformative.** Its τ is high (.62–.91), yet its MRR is at
  or below chance (v3 at .155 is clearly *worse* than random). Its rankings form two
  clusters: v1≈v4 (.91) and v2≈v3 (.91), with cross pairs at .62–.67. The same
  actor-placement split appears again: frozen MOTIF responds to where the actor sits,
  though not in a way that helps.
* **Fine-tuning is clearly representation-sensitive here.** Cross-variant τ (.01–.53) is
  well below the seed floor (.39–.55) for most pairs (v1 vs v3 is .008). This is the one
  task where the representation, not seed noise, drives the disagreement.
* **Ignore Precision and Recall for this task.** Precision is about 0.05 (the base rate)
  for everyone, and Recall std reaches ±0.47.
* **Compared with Movie–Director:** both are IMDb link-prediction tasks with the same
  candidate protocol, but Movie–Director is learnable (directors repeatedly work with the same
  actors: co-actor heuristic .350, both models well above the .180 chance level), while
  Movie–Year is not. Movie–Director is therefore the more informative IMDb task for the
  MOTIF vs CMPNN comparison, and Movie–Year's τ values carry little meaning.

## 6. WN18RR (v1 = no_changes, v2 = all_inverse_edges, v3 = transitive_edges)

All MOTIF WN18RR runs use one H200; CMPNN ran on V100. The frozen rows are labelled
**MOTIF (PT)**, not ZS, because `motif_3g.pth` was **pretrained on WN18RR**, on exactly v1's
training graph. They are in-domain, not zero-shot. (No test answers were seen: the pretraining
used the official train split only.)

| MRR | v1 | v2 | v3 | Mean | Spread |
|---|---|---|---|---|---|
| CMPNN | .424 ± .010 | .308 ± .056 | .293 ± .031 | .341 | .131 |
| MOTIF (PT) | .520 | **.145** | .381 | .349 | .375 |
| MOTIF (FT) | **.516 ± .002** | **.396 ± .010** | **.430 ± .003** | **.448** | .120 |

| Kendall-τ | v1 vs v2 | v1 vs v3 | v2 vs v3 |
|---|---|---|---|
| CMPNN | −.071 | .197 | −.040 |
| MOTIF (PT) | .527 | .275 | .268 |
| MOTIF (FT) | .412 | .162 | .218 |
| FT seed floor (same variant, different seeds) | v1 .67 · v2 .58 · v3 .48 | | |

* **Fine-tuned MOTIF beats CMPNN on every variant**, by +.09 (v1), +.09 (v2) and +.14 (v3) MRR,
  with much smaller seed std. This is the largest and most consistent MOTIF advantage in the
  study. It is not surprising for v1 (pretrained on this graph), but it holds on the
  transformed variants too.
* **Pretrained MOTIF is strongly representation-sensitive here.** It drops from .520 (v1) to
  .145 when every edge gets an explicit inverse (v2), and to .381 when 3-hop shortcut
  relations are added (v3). Both variants only add *redundant* information derived from
  training facts. The likely cause is MOTIF's relation encoder: v2 duplicates every relation
  in reverse on top of MOTIF's own internal inverses, and v3 adds 526 new relation types.
  The relation-motif graph grows from 18.7k hyperedges (v1) to 144.7k (v2) and 50.5M (v3).
  Fine-tuning recovers most of the loss.
* **Invariance is low for every model on WN18RR**, and the numbers need care:
  * The τ candidates are 100 *random* entities per query, as in CMPNN's protocol. Most of
    them are irrelevant, so τ is dominated by how a model orders junk candidates. That is
    why even same-variant reseeding gives only τ .48–.67.
  * MOTIF (FT) cross-variant τ (.16–.41) is **below** its seed floor (.48–.67), so the
    representation genuinely changes what is learned.
  * MOTIF (FT) is still clearly more invariant than CMPNN, whose τ is ≈ 0 or negative on two
    pairs.
* **Accuracy spread:** fine-tuned MOTIF varies .12 across variants, about the same as CMPNN
  (.13), at a much higher level.
* **GPU check:** the H200 reruns of v1 and v2 match the earlier V100 runs exactly for the
  frozen model (MRR .5199 on both). Fine-tuned seeds differ by up to .01, because training
  on these kernels is not bitwise deterministic, but the 3-seed means agree within .002
  (v1 .5148 vs .5163; v2 .3967 vs .3964).

## 6b. IMDb node classification (genre: Action / Comedy / Drama; v1–v4 as in Movie–Year)

There is **no CMPNN baseline** for node classification; the rows compare against the lab's
RGCN and SlotGAT ("original" arm, `IMDB_nc.tex`). MOTIF classifies by link prediction to one
node per genre. Only **training** movies are linked to their genre, so MOTIF sees training
labels as graph edges and uses no node features. The baselines use plot-keyword features
and never see neighbours' labels, so this comparison is **not like-for-like**.

| Accuracy | v1 | v2 | v3 | v4 | Spread | τ (mean of 6) |
|---|---|---|---|---|---|---|
| prior (most common genre) | .354 | | | | | |
| co-director/co-actor genre vote | .584 (v1 graph) | | | | | |
| RGCN | .652 | .603 | .649 | .618 | .048 | .784 |
| SlotGAT | .654 | .663 | .656 | .647 | .016 | .764 |
| MOTIF (ZS) | .610 | **.357** | .505 | .548 | .253 | .557 |
| MOTIF (FT) | .609 | .592 | .605 | .603 | **.017** | **.830** (seed floor .85–.92) |

* **Fine-tuned MOTIF reaches 0.59–0.61 without any node features**, about 0.05 below the
  feature-based baselines and slightly above the genre-vote heuristic. Most of its signal is
  "the genres of this movie's collaborators' other films".
* **Fine-tuned MOTIF is the most invariant model here.** Its accuracy spread (.017) matches
  SlotGAT's, and its τ (.83) is above both baselines and close to its own seed floor.
* **Here fine-tuning *increases* invariance**, the opposite of link prediction. Zero-shot is
  good only when director and actor are attached to the movie (v1 .610). When both sit on the
  link node (v2) it collapses to the prior (.357). Fine-tuning teaches each copy to reach
  through the link node.
* With 3 classes, per-movie τ takes only four values, so it is a coarse statistic.

---

## 7. Caveats and threats to validity

1. **The fine-tuning budgets are unequal.** MOTIF uses an untuned pilot recipe (1,000
   steps, lr 5e-4, small batch; on WN18RR that is about 0.1 epoch). CMPNN trains to early
   stopping. MOTIF (FT) is likely a lower bound.
2. **There is no CMPNN seed floor.** We cannot split CMPNN's lower τ into representation
   effects and seed noise. If CMPNN's per-seed score files exist, this is cheap to compute
   and would make the τ comparison much stronger.
3. **ZS ± 0 is not comparable to seed std.** A frozen model has no training variance. This
   is a genuine advantage of the setup, but it should be stated explicitly.
4. **Candidate sets** match CMPNN's protocol on every task. On WN18RR, Precision/Recall/τ
   use 100 seed-dependent sampled candidates, as CMPNN did, so those columns carry some
   sampling noise.
5. **Hardware:** CMPNN ran on V100. MOTIF ran on IMDb/DBLP on V100 and on WN18RR on H200
   (v3 needs about 45 GB). Everything runs in fp32 with TF32 off, so differences should be
   at rounding level. The archived V100 v1/v2 runs can confirm this.
6. **Leakage audits** (DBLP; IMDb Movie–Director; WN18RR) found no test or validation
   targets in any evaluation graph. Movie–Year was audited by the original exporter. The
   WN18RR caveat is pretraining, not leakage.

## 8. What I would look at next

* **CMPNN seed floor:** the most useful single addition for interpreting τ.
* **Report heuristics** (co-author .559, co-actor .350, chance levels) in the paper, so a
  reader can see how much of each task is trivially solvable.
* **The WN18RR v2 collapse:** check whether removing the explicit inverse relations at
  inference (letting MOTIF's internal inverses do the work) restores pretrained
  performance. That would pin the cause on duplicated inverse relations in the
  relation-motif graph.
* **A short fine-tuning sweep** (steps × lr) on DBLP and Movie–Director, to see whether
  MOTIF (FT) pulls ahead of CMPNN once it gets a comparable budget.
* **Movie–Year actor-placement effect:** if it holds up, it is a concrete mechanistic story
  ("the model only finds the year signal when the actor is one hop from the movie").
