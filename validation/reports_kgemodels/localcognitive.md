# KGE Models — Localcognitive.md

**Titre :** RatE: Relation-Adaptive Translating Embedding for Knowledge Graph Completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 9 |
| Modeles MENTIONNES seulement (hors tableaux) | 5 |
| **Precision globale** | **71%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 20% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 50% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | $\circ$ denotes element-wise (Hadamard) complex product, $\otimes$ denotes element-wise |
| ConvE | ✅ oui | 599</td> </tr> <tr> <td>ConvE</td> <td>374</td> <td>. |
| DistMult | ✅ oui | ="3">Semantic matching</td> <td>DistMult</td> <td>$\langle \mathbf{r}, \ |
| HolE | ✅ oui | d>-</td> </tr> <tr> <td>HolE</td> <td>-</td> <td>.93 |
| QuatE | ✅ oui | d>-</td> </tr> <tr> <td>QuatE</td> <td>$\mathbf{h} \otimes \m |
| RatE | ✅ oui | d>✗</td> </tr> <tr> <td>RatE</td> <td>$-\\|\mathbf{h} \odot_{ |
| RotatE | ✅ oui | d>✗</td> </tr> <tr> <td>RotatE</td> <td>$-\\|\mathbf{h} \circ \ |
| TransE | ✅ oui | owspan="3">Trans-based</td> <td>TransE</td> <td>$-\\|\mathbf{h} + \math |
| TuckER | ✅ oui | Table 9: Performance comparison between TuckER and RatE on WN18RR/FB15k-237. “#θ” deno |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| Relation-adaptive translating Embedding | ✅ oui | 10.04863v1 [cs.CL] 10 Oct 2020 # RatE: Relation-Adaptive Translating Embedding for Knowledge Graph Completion **Hao H |
| TorusE | ❌ NON | _(absent de la prose)_ |
| TransD | ❌ NON | _(absent de la prose)_ |
| TransH | ❌ NON | _(absent de la prose)_ |
| TransR | ❌ NON | _(absent de la prose)_ |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose | effectively learn structured knowledge. KBGAN (Cai and Wang, 2018) uses knowledge gra |