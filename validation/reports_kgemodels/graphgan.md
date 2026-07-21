# KGE Models — GraphGAN.md

**Titre :** GraphGAN: Graph Representation Learning with Generative Adversarial Nets

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 2 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 67% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| DeepWalk | ✅ oui | </thead> <tbody> <tr> <td>DeepWalk</td> <td>0.841</td> <td |
| GraphGAN | ✅ oui | 776</td> </tr> <tr> <td>GraphGAN</td> <td><strong>0.855</strong> |
| LINE | ✅ oui | 812</td> </tr> <tr> <td>LINE</td> <td>0.820</td> <td |
| Node2vec | ✅ oui | 761</td> </tr> <tr> <td>Node2vec</td> <td>0.845</td> <td |
| Struc2vec | ✅ oui | 842</td> </tr> <tr> <td>Struc2vec</td> <td>0.821</td> <td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| PPNE | ✅ oui | nder the supervision of edge existence. PPNE (Li et al. 2017b) directly learns verte |
| SDNE | ✅ oui | aining data in the graph. For instance, SDNE (Wang, \*M. Guo is the corresponding a |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| GAN | prose | ecently, *Generative Adversarial Nets* (GAN) (Goodfellow et al. 2014) have received |