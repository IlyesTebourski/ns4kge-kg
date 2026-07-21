# KGE Models — TuckerDNCaching.md

**Titre :** TuckerDNCaching: high-quality negative sampling with tucker decomposition

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 4 |
| Modeles MENTIONNES seulement (hors tableaux) | 4 |
| **Precision globale** | **88%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 75% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | ^n$</td> </tr> <tr> <td>ComplEx</td> <td>$Re(h^\top \cdot diag( |
| DistMult | ✅ oui | tic<br/>matching-based</td> <td>DistMult</td> <td>$h^\top \cdot diag(r) |
| TransD | ✅ oui | ^n$</td> </tr> <tr> <td>TransD</td> <td>$\left\\|h + w_r w_h^\t |
| TransE | ✅ oui | nal<br/>distance-based</td> <td>TransE</td> <td>$\\|h + r - t\\|_{1/2}$< |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| RESCAL | ❌ NON | _(absent de la prose)_ |
| RotatE | ✅ oui | ich has an impact on efficiency. Later, RotatE (Sun et al., 2019) introduced a self-ad |
| TorusE | ✅ oui | lational distance-based models, such as TorusE (Ebisu et al., 2018), by addressing the |
| TuckER | ✅ oui | ng: high-quality negative sampling with tucker decomposition Tiroshan Madushanka<sup> |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._