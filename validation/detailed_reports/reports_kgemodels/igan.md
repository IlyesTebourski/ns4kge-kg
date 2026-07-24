# KGE Models — IGAN.md

**Titre :** Incorporating GAN for Negative Sampling in Knowledge Representation Learning

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 9 |
| Modeles MENTIONNES seulement (hors tableaux) | 1 |
| **Precision globale** | **60%** |
| Precision (evalues, vs tableaux) | 56% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 3 |
| Candidats mentions ratees (bruts) | 0 |
| Recall BRUT evalues / mentionnes | 62% / 100% |
| Vrais oublis (adjuges) evalues / mentionnes | 3 / 0 |
| Recall ADJUGE *evalues* | 62% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| Single Layer Model | ❌ NON | _(absent des tableaux)_ |
| SME(Bilinear) | ✅ oui | ng></td> </tr> <tr> <td>SME(Bilinear) (Bordes et al. 2012)</td> <td> |
| Structured Embedding | ❌ NON | _(absent des tableaux)_ |
| TransD | ✅ oui | ng></td> </tr> <tr> <td>TransD (Ji et al. 2015)</td> <td>91</t |
| TransE | ✅ oui | 5.7</td> </tr> <tr> <td>TransE (Bordes et al. 2013)</td> <td>< |
| TransE + A-LSTM | ❌ NON | _(absent des tableaux)_ |
| TransH | ✅ oui | ng></td> </tr> <tr> <td>TransH (Wang et al. 2014)</td> <td>87< |
| TransR | ✅ oui | ng></td> </tr> <tr> <td>TransR (Lin et al. 2015)</td> <td><str |
| Unstructured Model | ❌ NON | _(absent des tableaux)_ |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| Neural Tensor Network | ✅ oui | ag{8}$$ where g() is tanh function. **Neural Tensor Network** (Socher et al. 2013) extends Single L |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| SE | prose+table | results show that 1. Models including SE, SME(bilinear), TransE and TransH are f |
| SME | prose+table | ults show that 1. Models including SE, SME(bilinear), TransE and TransH are furthe |
| Unstructured | prose+table | ages (Xie et al. 2016a) of entities. **Unstructured Model** (Bordes et al. 2012; Bordes et |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._