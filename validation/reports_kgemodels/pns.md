# KGE Models — PNS.md

**Titre :** Enhancing Knowledge Graph Embedding with Probabilistic Negative Sampling

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 1 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>263</td> <td>0 |
| TransH | ✅ oui | 349</td> </tr> <tr> <td>TransH(bern)</td> <td>401</td> |
| TransR | ✅ oui | <th>Epoch</th> <th>Modified TransR</th> <th>Original TransR</th> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| TransG | ✅ oui | o the current state-of-the-art approach TransG[4] to further improve its performance. |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._