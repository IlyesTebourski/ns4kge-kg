# NS4KGE Independent Annotation Guide

**Protocol version 1.0**

## 1. What is this task?

NS4KGE automatically extracts information from research papers about negative sampling for knowledge graph embeddings.

Your task is to check whether the extracted information matches what is written in the original PDF.

You do not need to understand RDF, OWL, SHACL, TTL files, or ontology engineering. You only need to be able to read an experimental machine-learning paper and identify elements such as datasets, models, methods, metrics, and reported results.

When a case is unclear, do not guess. Mark it as `AMB` and briefly explain why it is ambiguous.

## 2. What will you do?

For each assigned paper:

1. Open the paper PDF.
2. Open the CSV containing the items extracted by NS4KGE.
3. For each row, find the corresponding information in the PDF.
4. Record the exact wording and its location in the paper.
5. Decide whether the extracted item is correct.
6. Record any eligible item that appears in the paper but is missing from the extraction.

You will work independently. Do not look at another annotator's decisions before completing your own work.

## 3. What knowledge is required?

You should understand the basic structure of an experimental machine-learning paper and recognize:

- a **dataset**, such as FB15k-237;
- a **KGE model**, such as TransE or RotatE;
- a **negative-sampling method**;
- an evaluation **task** and **metric**, such as link prediction and MRR;
- training information, such as optimizer, loss function, hardware, or learning rate;
- a numerical result reported in an experimental table.

You do not need to know the canonical NS4KGE identifiers in advance. They are already provided in the CSV. For example, the paper may write `GHN`, while the CSV contains `method_generative_hard_negative_mining`.

## 4. Files to use

### 4.1 `NS4KGE_entity_annotation_skeleton.csv`

Use this file to check information already extracted by NS4KGE.

For each pre-filled row, add:

- the exact text found in the PDF;
- the page, section, or table;
- your decision;
- a short comment when necessary.

### 4.2 `NS4KGE_missing_entity_candidates.csv`

Use this file only when you find an eligible item in the paper that is missing from the extraction list.

### 4.3 `NS4KGE_configuration_annotation.csv`

Use this file to check extracted numerical results and their experimental configuration.

This file must already be populated before it is sent to annotators. Annotators are not expected to open or interpret TTL files.

## 5. Decision labels

Use the following labels:

| Label | Meaning |
|-------|---------|
| `TP` | The extracted item is confirmed by the paper. |
| `FP` | The extracted item is not confirmed by the paper. |
| `FN` | An eligible item is present in the paper but missing from NS4KGE. |
| `AMB` | The case is unclear and requires later discussion. |

Optional confidence values are `high`, `medium`, and `low`.

## 6. Scope of the annotation

For **Dataset**, **Metric**, and **Task**, use only the main experimental tables selected for extraction. Mentions in the introduction, related work, or discussion do not count.

For **KGEModel (mentions)**, **NSMethod (mentions)**, **NSMethod (proposes)**, **Optimizer**, **LossFunction**, **Hardware**, and **learningRate**, inspect the whole paper.

For **NSMethod (proposes)**, count only a method presented by the authors as a new contribution.

Spelling variants and abbreviations count as the same entity when the reference is clear:

- `FB15K-237`, `FB15K237` → `dataset_fb15k237`
- `GHN`, `Generative Hard Negative Mining` → `method_generative_hard_negative_mining`

Count each unique entity only once per paper.

## 7. How to fill the entity-validation CSV

For each pre-filled row in `NS4KGE_entity_annotation_skeleton.csv`:

1. Find the item, including abbreviations and spelling variants, within the relevant scope.
2. Copy the exact wording into `pdf_text_exact`.
3. Add a short sentence or table context in `pdf_context_short`.
4. Record `page` and `section_or_table`.
5. Use `table_row_or_cell` when relevant.
6. Set `decision` to `TP`, `FP`, or `AMB`.
7. Add a short comment only when needed.

A text search is useful, but always inspect the surrounding context before deciding.

Do not change the pre-filled identifiers, article name, category, scope, or ontology item.

## 8. How to record missing entities

Use `NS4KGE_missing_entity_candidates.csv` only for eligible entities that appear in the PDF but are absent from the extraction list.

One starter row is provided for each paper and category. Duplicate a row when several missing entities are found, and assign each copy a unique row identifier.

Record:

- the exact text from the PDF;
- a short context;
- the page, section, or table;
- a proposed canonical ID or literal value, when possible;
- `FN` or `AMB`;
- a short explanatory comment when useful.

Canonical IDs proposed by annotators may be harmonized later. The evidence copied from the PDF must not be changed during adjudication.

## 9. Numerical configurations

Each extracted configuration is one annotation unit:

```
Dataset + KGEModel + NSMethod + Task + Metric + Value
```

For each configuration:

| Label | Meaning |
|-------|---------|
| `TP` | The full combination and the numerical value match the paper. |
| `FP` | At least one field or the value does not match the paper. |
| `AMB` | The table does not support a clear decision. |

NS4KGE intentionally keeps only a selection of values from some large tables. Therefore, a result that appears in the paper but is absent from NS4KGE is **not** counted as an FN.

Configuration validation therefore measures precision rather than complete table coverage.

## 10. Worked example

Suppose the CSV contains:

> `method_generative_hard_negative_mining`

and the paper states:

> "We propose Generative Hard Negative Mining (GHN)."

A correct annotation would be:

| Field | Value |
|-------|-------|
| `pdf_text_exact` | Generative Hard Negative Mining (GHN) |
| `page` | 2 |
| `section_or_table` | Introduction |
| `decision` | `TP` |
| `confidence` | high |
| `annotator_comment` | Presented as the proposed method. |

## 11. Independent annotation and adjudication

Each annotator must work on a separate copy of the CSV files and add their identifier to the filename.

Example:

> `NS4KGE_entity_annotation_annotator_AP.csv`

Keep all individual annotation files unchanged. Merge copies only after all annotators have finished.

Agreement should be calculated on normalized annotation units and decisions, not on exact text-span equality. Two annotators may select slightly different evidence while identifying the same entity.

Resolve the following cases during adjudication:

- disagreements between TP, FP, and FN;
- all `AMB` cases;
- different canonical IDs proposed for the same missing entity.

Report agreement before adjudication, together with disagreements by category.

## 12. Questions during annotation

When a rule is unclear, do not silently invent a new interpretation. Record the case as `AMB` and raise it with the annotation coordinator.

Changes to the protocol should be documented in the project history and, when needed, reflected in a new protocol version.
