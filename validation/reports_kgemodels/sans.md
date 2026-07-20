# KGE Models — SANS.md

**Titre :** Structure Aware Negative Sampling in Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 75% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| DistMult | ✅ oui | </tr> <tr> <td rowspan="6">DistMult</td> <td>KBGAN</td> <td |
| RotatE | ✅ oui | </tr> <tr> <td rowspan="4">RotatE</td> <td>Uniform</td> < |
| TransE | ✅ oui | tbody> <tr> <td rowspan="6">TransE</td> <td>KBGAN (Cai and Wang, 2 |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose+table | egative sampling (Bordes et al., 2013), KBGAN (Cai and Wang, 2018), and NSCaching (Zh |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._