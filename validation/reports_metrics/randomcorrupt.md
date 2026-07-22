# Metrics — RandomCorrupt.md

**Titre :** Investigations on Knowledge Base Embedding for Relation Prediction and Extraction

| Metrique | Valeur |
|---|---|
| Metrics extraites trouvees dans les tables (TP) | 2 |
| Extraites NON trouvees (FP) | 0 |
| **Precision** | **100%** |
| Candidats faux negatifs (table resultats) | 0 |
| Candidats en table de stats (priorite basse) | 0 |
| Recall BRUT (avant adjudication) | 100% |
| **Recall relatif (adjuge)** | **100%** |

## Precision — metrics extraites par le KG

| Metric extraite | Dans les tables ? | Table | Extrait |
|---|:---:|---|---|
| Hits@1 | ✅ oui | Table 1. From there we observe that: (1) Generally, KBE models are doing well in the task of relation prediction. It indicates that relation information between entities can be captured by the existing KBE models without any specific modifications to adapt this task; (2) **ComplEx** achieves the best performance on all datasets. In addition, it significantly and consistently outperforms **DistMult** which matches the observations for the task of link prediction; (2) Surprisingly, **TransE** has competitive performance with **ComplEx** on some datasets which disagrees with the observations for the task of link prediction. It indicates that there | an="2">MRR</th> <th colspan="2">Hits@1</th> <th colspan="2">MRR</th> |
| MRR | ✅ oui | Table 1. From there we observe that: (1) Generally, KBE models are doing well in the task of relation prediction. It indicates that relation information between entities can be captured by the existing KBE models without any specific modifications to adapt this task; (2) **ComplEx** achieves the best performance on all datasets. In addition, it significantly and consistently outperforms **DistMult** which matches the observations for the task of link prediction; (2) Surprisingly, **TransE** has competitive performance with **ComplEx** on some datasets which disagrees with the observations for the task of link prediction. It indicates that there | <th> </th> <th colspan="2">MRR</th> <th colspan="2">Hits@1</th |

## Recall — metrics dans les tables mais NON extraites

_Aucun candidat en table de resultats._