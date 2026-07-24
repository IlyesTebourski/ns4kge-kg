# NS4KGE KG Data Quality Notes

Artifact version: `v1.0.0-paper`.

## Summary
- The assembled graph contains 6,398 triples and conforms to the generated SHACL shapes.
- The graph is an LLM-assisted extraction artifact over a small paper corpus, not a complete benchmark database.
- Numeric results and method labels are preserved from the generated extraction outputs unless normalized by the pipeline URI rules.

## Missing NSMethod Values
- 187 of 734 configurations do not have `ns4kge:hasNSMethod`.
- `article/ghn`: 69 of 105 configurations lack an NS method.
- `article/igan`: 46 of 138 configurations lack an NS method.
- `article/kbgan`: 18 of 54 configurations lack an NS method.
- `article/las`: 20 of 107 configurations lack an NS method.
- `article/pns`: 4 of 16 configurations lack an NS method.
- `article/randomcorrupt`: 30 of 30 configurations lack an NS method.

Interpretation: these rows are retained as extracted because they appear to represent baseline, model-only, or unattributed comparison rows rather than configurations with a named negative sampling method. The release does not impute a method where the extraction did not provide one.

## Article Without Proposed NS Method
- `article/randomcorrupt` has no `ns4kge:proposesNSMethod` relation.

Interpretation: this source is treated as a background or baseline paper in the artifact rather than as a paper proposing a named negative sampling method.

## Outlier Numeric Result
- `article/eans`, `configuration/eans/102`, dataset `WN18RR`, metric `MR`, model `DistMult`, method `KBGAN`, result `11351`.

Interpretation: Mean Rank is an unbounded lower-is-better metric, so high values can be valid. The value is retained and explicitly flagged for manual verification against the source table.

## Taxonomy Enrichment
- All 37 observed `NSMethod` identifiers now have a category and subcategory after adding aliases to the pipeline taxonomy.
- Category and subcategory assignments are curated, best-effort enrichment for this artifact.
- Future corpus expansion should review taxonomy aliases rather than treating current assignments as an exhaustive classification scheme.

## Dataset Variants
- Dataset identifiers preserve distinct benchmark variants such as `dataset/fb15k`, `dataset/fb15k-237`, `dataset/wn18`, and `dataset/wn18rr`.
- The pipeline normalizes common spelling variants such as `FB15K237` to `fb15k-237`, but it does not collapse distinct datasets.

## Validation-Informed Corrections (precision)

The deterministic precision validation (`validation/`) flags entities extracted by
the KG but absent from their source article. A **conservative** subset of these
false positives — only unambiguous artefacts, wrong-type assignments, and
malformed compounds — is suppressed at the JSON→TTL step, via the `BLOCKLIST` in
`ns4kge-extraction-pipeline` (`core/converters.py`). Real entities that merely
failed verbatim matching, and inferred baselines (uniform/bernoulli/random), are
deliberately **kept**.

Current corrections (SHACL-safe — removed from the optional `hasKGEModel` slot and
mention lists, so **no Configuration is dropped**; graph count unchanged):

- Malformed compounds extracted as KGE models: `KGE-EML+GNS` (gibbsns),
  `TransE + A-LSTM` (igan), and the STC compounds `TransE+STC+TCE`, `TransE+TCE`,
  `TransR+STC+TCE`, `TransR+TCE`, `TKRL (RHE+STC)`, `TKRL (RHE+STC+TCE)`,
  `TKRL (WHE+STC)`, `TKRL (WHE+STC+TCE)` (stc).
- Wrong-type entries (NS methods extracted as KGE models): `Knowledge Completion
  GAN` (gndn), `Truncated Negative Sampling` (truncatedns).

Effect: 12 spurious KGE-model entries removed (~66 triples), 0 configurations
dropped, `pyshacl` conformance preserved. Required-slot false positives (e.g. the
hallucinated `Accuracy` metric, the `Table 1 Dataset` artefact) are **not** removed
here, as doing so would drop dozens of configurations; they remain flagged in the
validation reports for manual review.

## Provenance Limitation
- The moved legacy per-article outputs did not record the exact model used for each individual generated file.
- `provenance/manifest.json` documents this limitation.
- Future regenerated outputs should record per-file model, prompt, run date, and pipeline commit provenance.
