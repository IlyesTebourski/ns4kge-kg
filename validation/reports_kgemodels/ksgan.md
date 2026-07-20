# KGE Models — KSGAN.md

**Titre :** A Knowledge Selective Adversarial Network for Link Prediction in Knowledge Graph

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 12 |
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
| ComplEx | ✅ oui | ^d$</td> </tr> <tr> <td>ComplEx</td> <td>$Re(\mathbf{h}, \mathb |
| TransD | ✅ oui | d}$</td> </tr> <tr> <td>TransD</td> <td>$-\\|(w_r w_h^\top + I) |
| TransE | ✅ oui | br/>distance<br/>model</td> <td>TransE</td> <td>$-\\|\mathbf{h} + \math |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| DistMult | ✅ oui | ng model (e.g., TransE [6], TransD [7], DistMult [8], ComplEx [9]). However, previous w |
| GTrans | ✅ oui | (or **t** − **r**). As a generic model, GTrans [17] introduces eigenstate and mimesis |
| ManifoldE | ✅ oui | ict magnitude constraints between them. ManifoldE [16] uses a manifold function to constr |
| MLP | ✅ oui | ic matching models such as NTN [21] and MLP [22], focus on neural network architect |
| NTN | ✅ oui | Other semantic matching models such as NTN [21] and MLP [22], focus on neural netw |
| RESCAL | ✅ oui | from the translational distance model, RESCAL [18] is a classic semantic matching mod |
| SimplE | ✅ oui | complex space rather than a real space. SimplE [19] simplifies ComplEx by considering |
| TransF | ✅ oui | ons. Targeting at more flexible models, TransF [15] ensures that **t** (or **h**) has |
| TransH | ✅ oui | t $(h, r, t)$. Various variants such as TransH [12], TransM [13], TransR [14] and Tran |
| TransM | ✅ oui | . Various variants such as TransH [12], TransM [13], TransR [14] and TransD [7] have b |
| TransR | ✅ oui | iants such as TransH [12], TransM [13], TransR [14] and TransD [7] have been developed |
| TuckER | ✅ oui | different similarity scoring function. TuckER [20] is based on Tucker decomposition a |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose+table | ed by an adversarial learning framework KBGAN, this paper proposes a new knowledge se |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._