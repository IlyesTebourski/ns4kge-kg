# KGE Models — MCNS.md

**Titre :** Understanding Negative Sampling in Graph Representation Learning

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 3 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 3 |
| Recall BRUT evalues / mentionnes | 100% / 50% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| DeepWalk | ✅ oui | <tr> <th> </th> <th>DeepWalk</th> <th>GCN</th> <th>G |
| GCN | ✅ oui | > <th>DeepWalk</th> <th>GCN</th> <th>GraphSAGE</th> |
| GraphSAGE | ✅ oui | k</th> <th>GCN</th> <th>GraphSAGE</th> <th>DeepWalk</th> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| FastGCN | ✅ oui | lleviate the receptive field expansion. FastGCN [5] adopts importance sampling in each |
| LINE | ✅ oui | Embedding methods (e.g. DeepWalk [27], LINE [32]) and Graph Neural Networks (e.g. G |
| node2vec | ✅ oui | s, such as DeepWalk [27], LINE [32] and node2vec [11], actually assign each node two emb |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | basic graph convolution layers [17] to attention-based [34], GAN-based [8], sampled aggr |
| Random Walk | prose | sample positive node pairs, such as by random walk [27], the second-order proximity [32], |
| word2vec | prose | tribution to accelerate the training of word2vec. Mikolov et al. [24] set the negative s |