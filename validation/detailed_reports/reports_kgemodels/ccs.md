# KGE Models — CCS.md

**Titre :** Op-Trans: An Optimization Framework for Negative Sampling and Triplet-Mapping Properties in Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 8 |
| Modeles MENTIONNES seulement (hors tableaux) | 13 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 3 |
| Recall BRUT evalues / mentionnes | 100% / 81% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 1 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 93% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| Op-TransD | ✅ oui | 873</td> </tr> <tr> <td>Op-TransD</td> <td>3352</td> <td> |
| Op-TransE | ✅ oui | </thead> <tbody> <tr> <td>Op-TransE</td> <td>4171</td> <td> |
| Op-TransH | ✅ oui | 852</td> </tr> <tr> <td>Op-TransH</td> <td>4404</td> <td> |
| Op-TransR | ✅ oui | 815</td> </tr> <tr> <td>Op-TransR</td> <td>3685</td> <td> |
| TransD | ✅ oui | g functions for TransE, TransH, TransR, TransD. <table> <thead> <tr> <th |
| TransE | ✅ oui | 4. Definition of scoring functions for TransE, TransH, TransR, TransD. <table> <the |
| TransH | ✅ oui | nition of scoring functions for TransE, TransH, TransR, TransD. <table> <thead> |
| TransR | ✅ oui | f scoring functions for TransE, TransH, TransR, TransD. <table> <thead> <tr> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| HAKE | ✅ oui | on translation of the vectors in space. HAKE [31] maps the entities into spatial pol |
| NTN | ✅ oui | SME) [16] model, neural tensor network (NTN) [17] model, and matrix factorization ( |
| OTE | ✅ oui | ntities into spatial polar coordinates. OTE [32] exploits the orthogonality relatio |
| PTransE | ✅ oui | TransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recently, RotatE [30] has ch |
| RESCAL | ✅ oui | ) [17] model, and matrix factorization (RESCAL) [18] model. However, these KGE models |
| RotatE | ✅ oui | nsAt [28], PTransE [29], etc. Recently, RotatE [30] has changed the translation proces |
| SE | ✅ oui | tion, such as the structured embedding (SE) [15] model, semantic matching energy ( |
| SME | ✅ oui | ) [15] model, semantic matching energy (SME) [16] model, neural tensor network (NTN |
| STransE | ✅ oui | nsD [23], TransM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28], PTrans |
| TransA | ✅ oui | sM [24], TranSparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. |
| TransAt | ✅ oui | Sparse [25], STransE [26], TransA [27], TransAt [28], PTransE [29], etc. Recently, Rota |
| TransM | ✅ oui | TransH [21], TransR [22], TransD [23], TransM [24], TranSparse [25], STransE [26], Tr |
| TranSparse | ✅ oui | TransR [22], TransD [23], TransM [24], TranSparse [25], STransE [26], TransA [27], TransA |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | erent from previous models, we pay more attention to the different contributions of each |
| Neural Tensor Network | prose | antic matching energy (SME) [16] model, neural tensor network (NTN) [17] model, and matrix factorizat |
| word2vec | prose | ng vector translation invariance of the word2vec model, Borders et al. proposed the firs |