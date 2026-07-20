# KGE Models — BatchNS.md

**Titre :** PyTorch-BigGraph: A Large-scale Graph Embedding System

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 13 |
| Modeles MENTIONNES seulement (hors tableaux) | 2 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 93% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | gt;</td> </tr> <tr> <td>ComplEx</td> <td>x ⊙ θᵣ</td> <t |
| DeepWalk | ✅ oui | </thead> <tbody> <tr> <td>DeepWalk*</td> <td>0.691</td> <t |
| HolE | ✅ oui | 749</td> </tr> <tr> <td>HolE (Nickel et al., 2016b)</td> <td |
| MILE (1 level) | ✅ oui | GB</td> </tr> <tr> <td>MILE (1 level)*</td> <td>0.629</td> < |
| MILE (5 levels) | ✅ oui | GB</td> </tr> <tr> <td>MILE (5 levels)*</td> <td>0.505</td> < |
| PBG | ✅ oui | GB</td> </tr> <tr> <td>PBG (1 partition)</td> <td>0.749</t |
| PBG (ComplEx) | ✅ oui | 785</td> </tr> <tr> <td>PBG (ComplEx)</td> <td>0.242</td> <t |
| PBG (TransE) | ✅ oui | 910</td> </tr> <tr> <td>PBG (TransE)</td> <td>0.265</td> <t |
| R-GCN+ | ✅ oui | 840</td> </tr> <tr> <td>R-GCN+ (Schlichtkrull et al., 2018)</td> |
| Reciprocal ComplEx-N3 | ✅ oui | 838</td> </tr> <tr> <td>Reciprocal ComplEx-N3 (Lacroix et al., 2018)</td> <td |
| RESCAL | ✅ oui | </thead> <tbody> <tr> <td>RESCAL</td> <td>Aᵣx</td> <td>& |
| StarSpace | ✅ oui | 842</td> </tr> <tr> <td>StarSpace (Wu et al., 2018)</td> <td>-</t |
| TransE | ✅ oui | gt;</td> </tr> <tr> <td>TransE</td> <td>x + θᵣ</td> <t |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| DistMult | ✅ oui | n operators allows PBG to train RESCAL, DistMult, TransE, and ComplEx models (Nickel et |
| word2vec | ✅ oui | this literature are algorithms such as word2vec which allowed word embedding methods to |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| GCN | prose+table | al., 2018). The problem studied by the GCN is different than the one solved by PBG |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._