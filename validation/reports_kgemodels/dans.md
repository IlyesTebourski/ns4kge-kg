# KGE Models — dans.md

**Titre :** Diversified and Adaptive Negative Sampling on Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 2 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 1 |
| Recall BRUT evalues / mentionnes | 100% / 67% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | RGCN) and decoders (DistMult, RotatE or ComplEx). The best results are in bold, and the |
| DistMult | ✅ oui | the same backbone (RGCN) and decoders (DistMult, RotatE or ComplEx). The best results a |
| RotatE | ✅ oui | backbone (RGCN) and decoders (DistMult, RotatE or ComplEx). The best results are in bo |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| RGCN | ✅ oui | relational graph convolutional network (RGCN) [26] to serve as our base embedding mo |
| TransE | ✅ oui | xt{China} \rangle$ and a classic method TransE [2]. TransE maps each entity and relati |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| MLP | prose | mplemented as a multi-layer perceptron (MLP). Taking $G_E$ as an example, its MLP i |