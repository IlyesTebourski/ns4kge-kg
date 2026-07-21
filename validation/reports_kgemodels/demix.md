# KGE Models — DeMix.md

**Titre :** Negative Sampling with Adaptive Denoising Mixup for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
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
| ComplEx | ✅ oui | ng></td> </tr> <tr> <td>ComplEx+Uniform</td> <td>0.429</td> |
| DistMult | ✅ oui | </thead> <tbody> <tr> <td>DistMult+Uniform</td> <td>0.412</td> |
| HAKE | ✅ oui | ng></td> </tr> <tr> <td>HAKE+Uniform<sup>Δ</sup></td> <td>0. |
| RotatE | ✅ oui | </thead> <tbody> <tr> <td>RotatE+Uniform<sup>Δ</sup></td> <td>0. |
| TransE | ✅ oui | les</td> </tr> <tr> <td>TransE+Uniform</td> <td>0.175*</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| TransH | ✅ oui | amely 1-N, N-1, 1-1, and N-N defined in TransH [24], we record the num of positive tri |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._