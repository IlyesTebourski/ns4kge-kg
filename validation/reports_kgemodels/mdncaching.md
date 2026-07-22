# KGE Models — MDNCaching.md

**Titre :** MDNCaching: A Strategy to Generate Quality Negatives for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 4 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 1 |
| Candidats mentions ratees (bruts) | 1 |
| Recall BRUT evalues / mentionnes | 80% / 0% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | ^n$</td> </tr> <tr> <td>ComplEx [11]</td> <td>$Re(h \cdot diag( |
| DistMult | ✅ oui | tic<br/>matching-based</td> <td>DistMult [16]</td> <td>$h \cdot diag(r) |
| TransD | ✅ oui | ^n$</td> </tr> <tr> <td>TransD [6]</td> <td>$\left\\|h + w_r w_ |
| TransE | ✅ oui | nal<br/>distance-based</td> <td>TransE [2]</td> <td>$\\|h + r - t\\|_i$< |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Random Walk | prose+table | not include. We consider SANS with the random walk configuration. # 5 Conclusion The |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | ral network approaches have also gained attention in recent research work that utilizes t |