# KGE Models — ASA.md

**Titre :** Relation-aware Graph Attention Model With Adaptive Self-adversarial Training

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 8 |
| Modeles MENTIONNES seulement (hors tableaux) | 0 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 3 |
| Recall relatif *evalues* | 89% |
| Recall relatif *mentionnes* | 0% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | </thead> <tbody> <tr> <td>ComplEx</td> <td>53.18(10)</td> |
| ConvE | ✅ oui | (8)</td> </tr> <tr> <td>ConvE</td> <td>49.65(11)</td> |
| DistMult | ✅ oui | 10)</td> </tr> <tr> <td>DistMult</td> <td>53.94(9)</td> |
| GATNE | ✅ oui | (9)</td> </tr> <tr> <td>GATNE</td> <td><u>96.25</u>(5)</td> |
| HAN | ✅ oui | 11)</td> </tr> <tr> <td>HAN</td> <td>87.57(7)</td> |
| metapath2vec | ✅ oui | (5)</td> </tr> <tr> <td>metapath2vec</td> <td><u>94.15</u>(6)</td> |
| R-GCN | ✅ oui | (6)</td> </tr> <tr> <td>R-GCN</td> <td>97.16(4)</td> |
| RelGNN | ✅ oui | (3)</td> </tr> <tr> <td>RelGNN - ASA</td> <td>98.84(2)</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

_Aucun modele mentionne hors tableaux._

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| GCN | prose+table | egating the neighbors' information. **R-GCN** (Schlichtkrull et al. 2018) considers |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | iv:2102.07186v1 # Relation-aware Graph Attention Model With Adaptive Self-adversarial Tr |
| GAN | prose | 2019b). Generative adversarial network (GAN) based solutions (Cai and Wang 2018; Wa |
| MLP | prose | 1) consists of a multilayer perceptron (MLP) network to process categorical attribu |