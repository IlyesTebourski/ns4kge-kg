# Configurations — ccs

**Titre :** Op-Trans: An Optimization Framework for Negative Sampling and Triplet-Mapping Properties in Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Configs verifiees | 150 |
| Valeur existe dans les tables | 150/150 |
| **① Accuracy — valeur existe** | **100.0%** |
| Combinaison (dataset/metric/model/ns) correcte | 144/150 |
| **② Accuracy — combinaison correcte** | **96.0%** |
| **③ 🐤 Canari attrape** | **1/1 — ✅ fiable** |

## Configs fautives (combinaison incorrecte)

| # | Dataset | Metric | KGEModel | NS | Valeur | Valeur existe ? |
|---|---|---|---|---|---|:--:|
| 60 | WN18RR | MR | TransR | NSCaching Sampling | 3639 | ✅ oui (mal associee) |
| 61 | WN18RR | MRR | TransR | NSCaching Sampling | 0.201 | ✅ oui (mal associee) |
| 62 | WN18RR | Hits@10 | TransR | NSCaching Sampling | 0.4822 | ✅ oui (mal associee) |
| 63 | FB15K237 | MR | TransR | NSCaching Sampling | 181 | ✅ oui (mal associee) |
| 64 | FB15K237 | MRR | TransR | NSCaching Sampling | 0.2751 | ✅ oui (mal associee) |
| 65 | FB15K237 | Hits@10 | TransR | NSCaching Sampling | 0.4773 | ✅ oui (mal associee) |
