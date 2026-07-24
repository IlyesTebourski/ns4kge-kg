# Use-case result tables

Representative SPARQL result tables for the three analytical use cases of NS4KGE,
with the observations they support. These tables illustrate what the competency
queries return over the populated knowledge graph; the raw, full outputs are in
[`competency_query_results.txt`](competency_query_results.txt), and the SPARQL
queries themselves live in the extraction-pipeline repository
(`nofacts-query` / `src/no_facts_pipeline/cli/query.py`).

Naming follows the canonical use cases:

| Use case | Focus | Related CQs |
|---|---|---|
| UC1 — Literature navigation | Structured exploration of the literature | CQ1–CQ4 |
| UC2 — Evaluation coverage | Untested / under-reported parts of the experimental space | CQ5–CQ7 |
| UC3 — Configuration exploration | Retrieving configurations to inform future experiments | CQ8–CQ11 |

---

## UC1 — Literature navigation

**Query.** Which combinations of NS method, KGE model, and dataset have been
evaluated together in the literature? (CQ4)

**Table 1. Most frequent combinations, ranked by number of articles.**

| NS Method | KGE Model | Dataset | #Articles |
|---|---|---|---|
| KBGAN | TransE | WN18RR | 12 |
| KBGAN | TransE | FB15k-237 | 12 |
| Uniform NS | TransE | FB15k-237 | 11 |
| NSCaching | TransE | FB15k-237 | 11 |
| Uniform NS | TransE | WN18RR | 11 |
| Self-Adversarial NS | RotatE | FB15k-237 | 10 |
| NSCaching | TransE | WN18RR | 10 |
| NSCaching | DistMult | WN18RR | 10 |
| NSCaching | DistMult | FB15k-237 | 10 |
| Self-Adversarial NS | RotatE | WN18RR | 9 |

**Observation.** The literature concentrates around a small set of recurring
method–model–dataset combinations. These recurrent configurations act as de
facto evaluation baselines, despite the absence of a standardized experimental
protocol. At the same time, their coverage remains limited relative to the
overall configuration space, indicating that experimental practices are still
fragmented: the populated graph reveals many unexplored method–model–dataset
combinations, suggesting substantial gaps in current evaluation coverage.

---

## UC2 — Evaluation coverage

**Query.** Which NS methods proposed in the corpus were evaluated exclusively on
datasets with known train–test leakage (FB15k, WN18), and never on their
corrected counterparts (FB15k-237, WN18RR)? (CQ6)

**Table 2. NS methods evaluated exclusively on datasets with known leakage.**

| NS Method | Dataset(s) | Proposed in | Year |
|---|---|---|---|
| Soft Type Constraint | FB15k | STC | 2016 |
| Probabilistic NS | FB15k, WN18 | PNS | 2017 |
| Batched NS | FB15k | BatchNS | 2019 |
| Knowledge Completion GAN | FB15k, WN18 | KCGAN | 2021 |
| NS by Relational Freq. | FB15k, WN18 | SparsENSG | 2021 |
| Soft Rules & Graph Adv. | FB15k | RUGA | 2021 |
| NS by Topic Similarity | FB15k, WN18 | LTS | 2022 |

**Observation.** Seven NS methods in the corpus were evaluated only on datasets
affected by train–test leakage, without evaluation on corrected benchmarks such
as FB15k-237 or WN18RR. Some were proposed recently (2021–2022), indicating that
the transition toward corrected evaluation datasets is still incomplete in parts
of the literature. The populated graph further shows that none of these methods
was later reevaluated on corrected datasets within the corpus — a corpus-level
analysis that would be difficult to perform systematically from unstructured
articles alone.

---

## UC3 — Configuration exploration

**Query.** Which similar experimental configurations yield strongly diverging
results across articles, and can these divergences be attributed to differences
in reported training settings? (CQ10–CQ11)

**Table 3. Illustrative examples of result divergences under similar experimental settings.**

Setup 1 — KBGAN / WN18RR / TransE / MR: a divergence unexplained by the reported
configuration. Setup 2 — KBGAN / WN18RR / DistMult / MRR: a divergence plausibly
linked to a difference in loss function.

| Setup | Article | Result | Learning Rate | NS Ratio | Loss Function |
|---|---|---|---|---|---|
| 1 | LAS | 3,978 | – | – | Margin-based |
| 1 | CCS | 5,356 | – | – | Margin-based |
| 2 | EANS | 0.204 | – | – | LogSigmoid |
| 2 | ERDNS | 0.385 | – | – | NS Loss |

**Observation.** The queried configurations reveal substantial result divergences
despite sharing the same NS method, KGE model, dataset, and evaluation metric. In
Setup 1, the difference in reported MR (3,978 vs. 5,356) cannot be explained from
the reported training configuration: both articles use the same loss function and
neither reports the learning rate or NS ratio. In Setup 2, the divergence in MRR
(0.204 vs. 0.385) coincides with a difference in loss function (LogSigmoid vs. NS
Loss), although other unreported parameters may also contribute. These examples
illustrate two recurrent situations: divergences left unexplained by incomplete
reporting, and divergences for which plausible factors can be identified but not
isolated conclusively. The ontology makes such comparability issues directly
queryable across articles.
