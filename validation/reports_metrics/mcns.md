# Metrics — MCNS.md

**Titre :** Understanding Negative Sampling in Graph Representation Learning

| Metrique | Valeur |
|---|---|
| Metrics extraites trouvees dans les tables (TP) | 4 |
| Extraites NON trouvees (FP) | 0 |
| **Precision** | **100%** |
| Candidats faux negatifs (table resultats) | 1 |
| Candidats en table de stats (priorite basse) | 0 |
| Recall BRUT (avant adjudication) | 80% |
| **Recall relatif (adjuge)** | **80%** |

## Precision — metrics extraites par le KG

| Metric extraite | Dans les tables ? | Table | Extrait |
|---|:---:|---|---|
| AUC | ✅ oui | Table 4: Micro-F1 scores for multi-label classification on the BlogCatalog dataset. Similar trends hold for Macro-F1 scores. | tbody> <tr> <td rowspan="9">AUC</td> <td>$Deg^{0.75}$</td> |
| F1 | ✅ oui | (hors table) | </table> Table 4 summarizes the Micro-F1 result on the BlogCatalog dataset. MCNS |
| Hits@30 | ✅ oui | Table 3: The results of link prediction with different negative sampling strategies on the Arxiv dataset. | </tr> <tr> <td rowspan="9">Hits@30</td> <td>$Deg^{0.75}$</td> |
| MRR | ✅ oui | Table 3: The results of link prediction with different negative sampling strategies on the Arxiv dataset. | tbody> <tr> <td rowspan="9">MRR</td> <td>$Deg^{0.75}$</td> |

## Recall — metrics dans les tables mais NON extraites

| Metric | Table | Extrait |
|---|---|---|
| NDCG | (sans caption) | <th>β</th> <th>MovieLens NDCG</th> <th>Amazon NDCG</th> |