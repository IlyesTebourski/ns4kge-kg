# Reports

Store validation reports and competency-query outputs used in the paper here.

Suggested commands from `../ns4kge-extraction-pipeline`:

```bash
uv run nofacts-validate --data ../ns4kge-kg/kg/NSArticles_populated.ttl --shapes ../ns4kge-ontology/ontology/NSArticles_shapes.ttl > ../ns4kge-kg/reports/validation.txt
uv run nofacts-query --data ../ns4kge-kg/kg/NSArticles_populated.ttl > ../ns4kge-kg/reports/competency_query_results.txt
```
