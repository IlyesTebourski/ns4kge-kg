# KGE Models — SparseNSG.md

**Titre :** A Novel Negative Sampling Based on Frequency of Relational Association Entities for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 9 |
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
| ANALOGY | ✅ oui | 0.1</td> </tr> <tr> <td>ANALOGY</td> <td>d = 200, α = 0.1</td> |
| ComplEx | ✅ oui | 0.1</td> </tr> <tr> <td>COMPLEX</td> <td>d = 200, α = 0.1</td> |
| DistMult | ✅ oui | 001</td> </tr> <tr> <td>DISTMULT</td> <td>d = 200, α = 0.1</td> |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>d=100, γ = 1, α = 0.00 |
| TransH | ✅ oui | 001</td> </tr> <tr> <td>TransH</td> <td>d = 100, γ = 1, α = 0. |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| NTN | ✅ oui | other kinds of models, such as SE, SME, NTN. However, a practical knowledge graph i |
| SE | ✅ oui | 15], and other kinds of models, such as SE, SME, NTN. However, a practical knowled |
| SME | ✅ oui | ter contains, Semantic Matching Energy (SME) [10], Semantically Smooth Embedding (S |
| SSE | ✅ oui | E) [10], Semantically Smooth Embedding (SSE) [11], and translation-based methods [1 |
| TransA | ✅ oui | sing, some presentation models, such as TransA [16], TransG [19], replace the relation |
| TransD | ✅ oui | ls, such as TransE, TransH, TransR, and TransD [15], and other kinds of models, such a |
| TransG | ✅ oui | esentation models, such as TransA [16], TransG [19], replace the relation of a triplet |
| TranSparse | ✅ oui | ment, widely used in TransR, TransD and TranSparse [18], can effectively reduce the probab |
| TransR | ✅ oui | s, such as TransE [12], TransH [13] and TransR [14], are the most used knowledge graph |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._