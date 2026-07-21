# KGE Models — AdaptativeNS.md

**Titre :** Knowledge Graph Embedding via Adaptive Negative Subsampling

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 6 |
| Modeles MENTIONNES seulement (hors tableaux) | 8 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 89% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | t}$</td> </tr> <tr> <td>ComplEx</td> <td>$Re(\mathbf{h}^T \text |
| ConvE | ✅ oui | })$</td> </tr> <tr> <td>ConvE</td> <td>$f(vec(f([\mathbf{r}, |
| DistMult | ✅ oui | t}$</td> </tr> <tr> <td>DistMult</td> <td>$\mathbf{h}^T \text{di |
| MuRP | ✅ oui | ))$</td> </tr> <tr> <td>MuRp</td> <td>$-d_{\mathbb{B}}(exp_{ |
| RotatE | ✅ oui | 2}$</td> </tr> <tr> <td>RotatE</td> <td>$\|\|\mathbf{h} \odot \m |
| TransE | ✅ oui | d>-</td> </tr> <tr> <td>transE</td> <td>0.226</td> <td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| HAKE | ✅ oui | relationships in knowledge graphs. The HAKE [20] model is designed for graph embedd |
| MEI | ✅ oui | ent intricacies of the knowledge graph. MEI [13] and MEIM [14] partition each embed |
| MEIM | ✅ oui | es of the knowledge graph. MEI [13] and MEIM [14] partition each embedding into mult |
| RESCAL | ✅ oui | ressed in vector space representations. RESCAL [10] introduced a tensor factorization |
| TransD | ✅ oui | between entities and relationships. The TransD [18] model further improves upon TransR |
| TransG | ✅ oui | and relationships more effectively. The TransG [17] model proposes a solution to the c |
| TransH | ✅ oui | many and many-to-one relationships, the TransH [16] model extends it by introducing re |
| TransR | ✅ oui | omes the shortcomings of TransE. In the TransR [7] model, a relation mapping matrix is |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Tucker | prose | ocal interactions are modeled using the Tucker tensor format, while the complete inter |