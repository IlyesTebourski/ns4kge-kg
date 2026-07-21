# KGE Models — EANS.md

**Titre :** Entity Aware Negative Sampling with Auxiliary Loss of False Negative Prediction for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
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
| ComplEx | ✅ oui | </tr> <tr> <td rowspan="6">ComplEx<br/>(Trouillon et al., 2016)</td> |
| DistMult | ✅ oui | </tr> <tr> <td rowspan="7">DistMult<br/>(Yang et al., 2014)</td> <t |
| RotatE | ✅ oui | </tr> <tr> <td rowspan="5">RotatE<br/>(Sun et al., 2019)</td> <td |
| TransD | ✅ oui | </tr> <tr> <td rowspan="6">TransD<br/>(Ji et al., 2015)</td> <td> |
| TransE | ✅ oui | tbody> <tr> <td rowspan="7">TransE<br/>(Bordes et al., 2013)</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| RESCAL | ✅ oui | relation vectors into various spaces. RESCAL (Nickel et al., 2011), DistMult (Yang e |
| TransH | ✅ oui | . Various extensions of TransE, such as TransH (Wang et al., 2014), TransR (Lin et al. |
| TransR | ✅ oui | sE, such as TransH (Wang et al., 2014), TransR (Lin et al., 2015) and TransD (Ji et al |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._