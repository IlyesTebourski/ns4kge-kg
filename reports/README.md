# Reports

Store validation reports and competency-query outputs used in the paper here.

Suggested commands from `../ns4kge-extraction-pipeline`:

```bash
uv run nofacts-validate --data ../ns4kge-kg/kg/ns4kge_populated.ttl --shapes ../ns4kge-ontology/ontology/ns4kge_shapes.ttl > ../ns4kge-kg/reports/validation.txt
uv run nofacts-query --data ../ns4kge-kg/kg/ns4kge_populated.ttl > ../ns4kge-kg/reports/competency_query_results.txt
```

## Files

- `validation.txt` — SHACL validation report
- `competency_query_results.txt` — Competency query results (raw output)
- `use_case_result_tables.md` — Curated result tables per use case (UC1/UC2/UC3) with observations
- `debug_query_results.txt` — Diagnostic query results
- `per_article_validation.txt` — Manual extraction validation on 6 articles (GHN, LAS, IGAN, M2ixKG, RandomCorrupt, EANS) with per-class TP/FP/FN/P/R/F1
- `source_text_audit.txt` — Source text redistribution audit
- `data_quality_notes.md` — Data quality notes
