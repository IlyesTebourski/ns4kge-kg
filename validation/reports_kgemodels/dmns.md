# KGE Models — DMNS.md

**Titre :** Diffusion-based Negative Sampling on Graphs for Link Prediction

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 8 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 3 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 0% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ARVGA | ✅ oui | 005</td> </tr> <tr> <td>ARVGA</td> <td>.732 ± .011</td> |
| GAT | ✅ oui | </thead> <tbody> <tr> <td>GAT</td> <td>.766 ± .006</td> |
| GCN | ✅ oui | link prediction against baselines using GCN as the base encoder. <table> <thead> |
| GraphGAN | ✅ oui | 004</td> </tr> <tr> <td>GraphGAN</td> <td>.739 ± .003</td> |
| GVAE | ✅ oui | 003</td> </tr> <tr> <td>GVAE</td> <td><u>.783 ± .003</u></td |
| SAGE | ✅ oui | ng></td> </tr> <tr> <td>SAGE</td> <td>.598 ± .014</td> |
| ScaLed | ✅ oui | 001</td> </tr> <tr> <td>ScaLed</td> <td>.676 ± .004</td> |
| SEAL | ✅ oui | 002</td> </tr> <tr> <td>SEAL</td> <td>.751 ± .007</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| GAN | prose | y in visual applications [8, 17]. While GAN-based models are successful in generati |
| GraphSAGE | prose | conduct experiments using GAT [45] and GraphSAGE (SAGE) [14]. For GCN, we employ two lay |
| MLP | prose | $, followed by a multilayer perceptron (MLP). $\tau(\cdot; \theta)$ is a learnable |