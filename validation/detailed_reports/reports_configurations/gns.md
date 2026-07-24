# Configurations — gns

**Titre :** Good negative sampling for triple classification

| Metrique | Valeur |
|---|---|
| Configs verifiees | 3 |
| Valeur existe dans les tables | 3/3 |
| **① Accuracy — valeur existe** | **100.0%** |
| Combinaison (dataset/metric/model/ns) correcte | 0/3 |
| **② Accuracy — combinaison correcte** | **0.0%** |
| **③ 🐤 Canari attrape** | **1/1 — ✅ fiable** |

## Configs fautives (combinaison incorrecte)

| # | Dataset | Metric | KGEModel | NS | Valeur | Valeur existe ? |
|---|---|---|---|---|---|:--:|
| 0 | FB13 (FB13_reduced) | Accuracy | KG-BERT | Uniform Negative Sampling | 0.5182 | ✅ oui (mal associee) |
| 1 | FB13 (FB13_reduced) | Accuracy | KG-BERT | Pseudo Typed Negative Sampling | 0.8972 | ✅ oui (mal associee) |
| 2 | FB13 (FB13_reduced) | Accuracy | KG-BERT | Good Negative Sampling | 0.9013 | ✅ oui (mal associee) |
