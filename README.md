# NS4KGE Knowledge Graph

Instantiated knowledge graph built from the NS4KGE ontology and the NS4KGE extraction pipeline.

## Contents
- `kg/NSArticles_populated.ttl` is the assembled RDF/Turtle graph used for validation and querying.
- `per_article/` contains generated per-article JSON and TTL outputs.
- `provenance/manifest.json` records ontology, pipeline, prompt, model, and source-corpus metadata.
- `provenance/sources.csv` records article-level source metadata, source DOIs or URLs where available, and local source-file checksums without publishing source paper text.
- `reports/` contains validation, query, source-audit, and data-quality outputs used by the paper.

## Version
- Current artifact version: `v1.0.0-paper`.
- For the first public GitHub release, create the release/tag as `v1.0.0-paper`.

## Persistent Identifiers
- KG dataset IRI: `https://w3id.org/ns4kge/kg`.
- KG version IRI: `https://w3id.org/ns4kge/kg/1.0.0`.
- KG instance base: `https://w3id.org/ns4kge/id/`.
- Article example: `https://w3id.org/ns4kge/id/article/eans`.
- Method example: `https://w3id.org/ns4kge/id/ns-method/entity-aware-negative-sampling`.
- Configuration example: `https://w3id.org/ns4kge/id/configuration/eans/1`.
- Ontology terms use `https://w3id.org/ns4kge/ontology#`, for example `https://w3id.org/ns4kge/ontology#Article`.

## Resource Availability
- Repository: `https://github.com/IlyesTebourski/ns4kge-kg`.
- Release target: `v1.0.0-paper`.
- Release date: 2026-05-06.
- License: CC BY 4.0.
- Zenodo DOI: `https://doi.org/10.5281/zenodo.20058972`.
- Dereferenceable KG landing IRI: `https://w3id.org/ns4kge/kg`.
- Ontology artifact: `https://doi.org/10.5281/zenodo.20058306` and `https://github.com/IlyesTebourski/ns4kge-ontology`.
- Extraction pipeline artifact: `https://github.com/IlyesTebourski/ns4kge-extraction-pipeline`.

The repository contains only generated structured outputs, assembled RDF, provenance metadata, validation reports, and query reports. It does not redistribute full source article text.

## Boundaries
- This repo is the generated KG artifact only.
- The reusable ontology lives in `../ns4kge-ontology`.
- The Python tooling for assembly, validation, and queries lives in `../ns4kge-extraction-pipeline`.
- Full source article markdown is intentionally excluded and must not be published here.

## Source Text Boundary
- The source articles are not redistributed because they may be copyrighted by their publishers or authors.
- `provenance/sources.csv` records titles, years, source DOIs or URLs where available, local source filenames, and SHA-256 checksums of the local files used for extraction.
- The generated JSON, TTL, and assembled KG contain structured metadata and extracted tabular values rather than substantial prose from the source papers.
- `reports/source_text_audit.txt` records the local audit used to check for substantial source-text leakage before release.

## Data Quality Notes
- The graph represents LLM-assisted extraction outputs and should be treated as a curated research artifact, not as a complete benchmark database.
- Some configurations intentionally lack `ns4kge:hasNSMethod` because the source table row appears to report a baseline or model-only result rather than an attributed negative sampling method.
- `article/randomcorrupt` does not use `ns4kge:proposesNSMethod` because the source is treated as a background/baseline paper rather than a paper proposing a named negative sampling method.
- Numeric results preserve extracted source-table values. In particular, high Mean Rank values can be valid when lower is better; suspicious values are documented in `reports/data_quality_notes.md`.
- Category and subcategory enrichment for `NSMethod` individuals is curated by the extraction pipeline taxonomy and is best-effort.

## Sustainability And Maintenance
- The first intended public release is `v1.0.0-paper`.
- KG dataset and instance IRIs are intended to remain stable under `https://w3id.org/ns4kge/kg` and `https://w3id.org/ns4kge/id/`.
- Future graph releases should use a new release tag, update `provenance/manifest.json`, refresh reports, and publish an archival DOI.
- Rebuilds should be performed with the companion extraction pipeline so that generated per-article TTL, assembled KG, validation report, and query reports stay synchronized.

## Limitations
- The graph covers a small paper artifact corpus about negative sampling for knowledge graph embeddings; it is not a comprehensive survey database.
- Extraction relied on hosted LLMs and legacy generated outputs, so exact per-file model provenance is incomplete for the moved paper artifact.
- SHACL conformance checks graph structure against generated shapes but does not prove that every extracted scientific claim is correct.
- Source article text is excluded for copyright reasons; users must obtain source papers independently if they want to verify extraction details from the original prose.

## Rebuild And Validate
From the pipeline folder:

```bash
uv run nofacts-populate-onto --output-dir ../ns4kge-kg/per_article --ontology ../ns4kge-ontology/ontology/NSArticles_ontology.ttl --out ../ns4kge-kg/kg/NSArticles_populated.ttl
uv run nofacts-validate --data ../ns4kge-kg/kg/NSArticles_populated.ttl --shapes ../ns4kge-ontology/ontology/NSArticles_shapes.ttl
uv run nofacts-query --data ../ns4kge-kg/kg/NSArticles_populated.ttl
```

## License
KG data and provenance files are licensed under CC BY 4.0.
