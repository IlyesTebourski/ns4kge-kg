# Datasets — CANS.md

**Titre :** Confidence-Aware Negative Sampling Method for Noisy Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Datasets extraits trouves dans les tables (TP) | 6 |
| Extraits NON trouves (FP -> erreur precision) | 0 |
| **Precision** | **100%** |
| Candidats faux negatifs (table de resultats) | 1 |
| Candidats en table de stats seulement (priorite basse) | 0 |
| Recall BRUT (avant adjudication) | 86% |
| **Recall relatif (adjuge)** | **100%** |

## Precision — datasets extraits par le KG

| Dataset extrait | Dans les tables ? | Table | Extrait |
|---|:---:|---|---|
| FB15K-N1 | ✅ oui | (sans caption) | r> <th>Dataset</th> <th>FB15K-N1</th> <th>FB15K-N2</th> |
| FB15K-N2 | ✅ oui | (sans caption) | > <th>FB15K-N1</th> <th>FB15K-N2</th> <th>FB15K-N3</th> </tr |
| FB15K-N3 | ✅ oui | (sans caption) | > <th>FB15K-N2</th> <th>FB15K-N3</th> </tr> </thead> <tbody> |
| WN18-N1 | ✅ oui | (sans caption) | r> <th>Dataset</th> <th>WN18-N1</th> <th>WN18-N2</th> < |
| WN18-N2 | ✅ oui | (sans caption) | h> <th>WN18-N1</th> <th>WN18-N2</th> <th>WN18-N3</th> </tr> |
| WN18-N3 | ✅ oui | (sans caption) | h> <th>WN18-N2</th> <th>WN18-N3</th> </tr> </thead> <tbody> |

## Recall — datasets dans les tables mais NON extraits

### ⚠️ Candidats en table de resultats (a revoir en priorite)

| Dataset | Table | Extrait |
|---|---|---|
| WN18 | (sans caption) | </thead> <tbody> <tr> <td>WN18</td> <td>18</td> <td>40 |
