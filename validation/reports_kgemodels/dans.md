# KGE Models — dans.md

**Titre :** Diversified and Adaptive Negative Sampling on Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 2 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 2 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 60% |
| Recall relatif *mentionnes* | 100% |

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

| Modele | Ou | Extrait |
|---|---|---|
| CAKE | prose+table | nerate informative negative triplets; **CAKE** [19]: a framework which leverages ext |
| KBGAN | prose+table | ous state-of-the-art approaches such as KBGAN [3], we adopt a generative adversarial |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._