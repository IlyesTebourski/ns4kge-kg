# KGE Models — Uniform.md

**Titre :** Translating Embeddings for Modeling Multi-relational Data

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 7 |
| Modeles MENTIONNES seulement (hors tableaux) | 1 |
| **Precision globale** | **88%** |
| Precision (evalues, vs tableaux) | 86% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 2 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 75% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| LFM | ✅ oui | .06</td> </tr> <tr> <td>LFM [6]</td> <td>$O(n_e k + n_r k + |
| RESCAL | ✅ oui | .75</td> </tr> <tr> <td>RESCAL [11]</td> <td>$O(n_e k + n_r k^ |
| SME(bilinear) | ✅ oui | .82</td> </tr> <tr> <td>SME(BILINEAR) [2]</td> <td>$O(n_e k + n_r k |
| SME(linear) | ✅ oui | .47</td> </tr> <tr> <td>SME(LINEAR) [2]</td> <td>$O(n_e k + n_r k |
| Structured Embeddings | ❌ NON | _(absent des tableaux)_ |
| TransE | ✅ oui | .84</td> </tr> <tr> <td>TransE</td> <td>$O(n_e k + n_r k)$</td |
| Unstructured | ✅ oui | </thead> <tbody> <tr> <td>Unstructured [2]</td> <td>$O(n_e k)$</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| Neural Tensor Model | ✅ oui | point. Another related approach is the Neural Tensor Model [14]. A special case of this model corr |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| SE | prose+table | those of [3] (Structured Embeddings or SE) and [14]. 3 Table 1: **Numbers of pa |
| SME | prose+table | 2], and the energy-based models SE [3], SME(linear)/SME(bilinear) [2] and LFM [6]. |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._