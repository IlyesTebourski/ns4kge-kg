# Draft "Evaluation" section (paper-ready outline)

> Purpose: a structured, factual scaffold an LLM/author only has to rephrase and condense into the paper.
> All numbers are final and reproducible. Keep the *evaluated vs mentioned* framing — it is a selling point.

---

## X. Evaluation of Extraction Quality

### X.1 Setup

We evaluate the automatically populated NS4KGE knowledge graph against the source articles, for the four
entity types it contains: **datasets, metrics, KGE models, and NS methods**, over a corpus of **55 articles**.

Crucially, the evaluation is **faithful to the extraction pipeline**: each entity is checked against the exact
input its generating prompt received. The pipeline splits every article into a *tables-only* view
(`load_md_tables_only`, feeding the results-table prompt) and a *no-tables* view (`load_md_no_tables`, feeding
the metadata prompt). Datasets and metrics originate solely from results tables, so they are validated against
the tables-only view; KGE models and NS methods originate from **both** the tables (configurations = evaluated
entities) and the prose (proposed/mentioned entities), and are validated against the corresponding view. These
views are regenerated with the pipeline's own functions, guaranteeing no train/eval mismatch.

The evaluation procedure is **fully deterministic** (regular-expression matching, no LLM), hence exactly
reproducible.

### X.2 Metrics

For each entity type we report:
- **Precision** = TP / (TP + FP): fraction of extracted entities actually attested in the source.
- **Relative recall** = TP / (TP + FN candidates): fraction of attested entities that were extracted, where
  candidates are drawn from the global vocabulary of entities extracted across the corpus. Recall is *relative*
  (a lower-bound proxy): candidates are text-attested entities that were not extracted.

For KGE models and NS methods we further split every metric by **provenance** — *evaluated* (appearing in a
results table) vs *mentioned only* (cited in prose) — yielding four scores. This mirrors an ontological
distinction the KG is meant to capture: which methods/models are experimentally compared vs merely discussed.

### X.3 Matching

Matching is case-insensitive with tolerant separators and strict word boundaries (a name may not match a
prefix of a longer code, e.g. `FB15k` vs `FB15k-237`). Difficulty grows with the lack of name standardization,
requiring type-specific handling:
- **Datasets:** verbatim; recall restricted to table cells (results vs statistics tables separated by caption).
- **Metrics:** deterministic alias set, since the prompt normalizes surface forms (`Mean Rank`→`MR`, `Hit@10`→`Hits@10`).
- **KGE models:** case-sensitive on the recall side (names are stylized as words, e.g. `SimplE`); generic
  architectures (`GAN`, `MLP`, `BERT`) excluded as non-instances of the class.
- **NS methods:** acronym derivation (`Self-Adversarial Negative Sampling`→`SANS`), qualifier normalization
  (`NoiGAN (hard) (40%)`→`NoiGAN`), near-duplicate canonicalization, and the placeholder `Unknown` excluded.

### X.4 Results

| Entity | Prec. evaluated | Prec. mentioned | Recall evaluated | Recall mentioned |
|---|:---:|:---:|:---:|:---:|
| Datasets | 98.9% | — | 97.3% | — |
| Metrics | 96.5% | — | 96.0% | — |
| KGE Models | 94.5% | 97.9% | 89.5% | 95.5% |
| NS Methods | 89.0% | 87.0% | 80.9% | 71.2% |

Precision is high across all four types (≥ 87%), and the few precision errors are genuine extraction defects
that the evaluation localizes (e.g. a hallucinated `Accuracy` metric, unsplit model+method compounds).

### X.5 Analysis / Discussion

The scores decrease monotonically with the **degree of standardization of entity names**. Dataset and KGE-model
names are frozen community nomenclature (`WN18RR`, `TransE`), matched near-perfectly. Metrics form a small
closed set, only lightly rewritten. NS methods, by contrast, lack a shared naming convention: many are
paraphrased or have no canonical short name, are heavily abbreviated, and are frequently confounded with
inferred, unnamed baselines — which explains, and largely justifies, their lower scores. The lower NS-method
recall on mentions further quantifies a concrete, actionable behavior of the KG: it misses about one third of
the methods cited in related work.

### X.6 Limitations

Recall is *relative* (evaluated against the extracted global vocabulary, not an exhaustive gold standard).
Precision is reported strictly: inferred standard baselines that the article does not name explicitly are
counted as errors even though they may be correct, since they cannot be confirmed by textual search — a
limitation specific to NS methods.
