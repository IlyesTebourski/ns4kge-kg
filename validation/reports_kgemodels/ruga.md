# KGE Models — RUGA.md

**Titre :** Improving Knowledge Graph Completion Using Soft Rules and Adversarial Learning

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 6 |
| Modeles MENTIONNES seulement (hors tableaux) | 4 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 80% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | 546</td> </tr> <tr> <td>ComplEx</td> <td>0.690</td> <td |
| DistMult | ✅ oui | 468</td> </tr> <tr> <td>DistMult</td> <td>0.634</td> <td |
| HolE | ✅ oui | 570</td> </tr> <tr> <td>HolE</td> <td>0.608</td> <td |
| RUGA | ✅ oui | </tr> <tr> <td><strong>RUGA</strong></td> <td><strong>0.779 |
| RUGE | ✅ oui | 601</td> </tr> <tr> <td>RUGE</td> <td>0.767</td> <td |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>h, t</td> <td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| RESCAL | ✅ oui | coring function. Typical models include RESCAL<sup>[13]</sup>, DistMult<sup>[14]</sup> |
| TransD | ✅ oui | H<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD<sup>[11]</sup> and so on. As shown in F |
| TransH | ✅ oui | ne to expand and apply TranE, including TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, T |
| TransR | ✅ oui | TranE, including TransH<sup>[9]</sup>, TransR<sup>[10]</sup>, TransD<sup>[11]</sup> a |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| word2vec | prose | variance exists in vector space through word2vec. Thus, Bordes et al. proposed a represe |