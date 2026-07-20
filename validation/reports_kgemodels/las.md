# KGE Models — LAS.md

**Titre :** Adversarial Knowledge Representation Learning without External Model

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 6 |
| Modeles MENTIONNES seulement (hors tableaux) | 21 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 2 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 75% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | 462</td> </tr> <tr> <td>ComplEx (pretrained)</td> <td>0.264</td |
| ConvE | ✅ oui | d>-</td> </tr> <tr> <td>ConvE [23]</td> <td><strong>31.6</str |
| DistMult | ✅ oui | </thead> <tbody> <tr> <td>DistMult [18]</td> <td>24.1</td> |
| R-GCN | ✅ oui | 1.0</td> </tr> <tr> <td>R-GCN [28]</td> <td>24.8</td> |
| TransD* | ✅ oui | 431</td> </tr> <tr> <td>TransD (pretrained)</td> <td>0.244</td |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE (pretrained)</td> <td>0.243</td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ANALOGY | ✅ oui | bability-based models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good |
| DKRL | ✅ oui | ] exploit relation paths, TEKE [33] and DKRL [34] embed knowledge graph with textual |
| HolE | ✅ oui | dels (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx [20], and ConvE [23] etc) |
| ITransF | ✅ oui | [13], STransE [14], puTransE [15], and ITransF [16]) define an energy function accordi |
| KALE | ✅ oui | owledge graph with textual information, KALE [35] and RUGE [36] utilize logical rule |
| KG2E | ✅ oui | 6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], Tra |
| ProjE | ✅ oui | ny other probability-based models, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also |
| PTransE | ✅ oui | and TKRL [30] consider the entity type, PTransE [31] and RTransE [32] exploit relation |
| puTransE | ✅ oui | Sparse [12], TransG [13], STransE [14], puTransE [15], and ITransF [16]) define an energ |
| RESCAL | ✅ oui | models Probability-based models (e.g., RESCAL [17], DistMult [18], HolE [19], ComplEx |
| RTransE | ✅ oui | sider the entity type, PTransE [31] and RTransE [32] exploit relation paths, TEKE [33] |
| RUGE | ✅ oui | with textual information, KALE [35] and RUGE [36] utilize logical rules. In this pa |
| SSE | ✅ oui | further improve the task. For example, SSE [29] and TKRL [30] consider the entity |
| STransE | ✅ oui | nsA [11], TranSparse [12], TransG [13], STransE [14], puTransE [15], and ITransF [16]) |
| TEKE | ✅ oui | nd RTransE [32] exploit relation paths, TEKE [33] and DKRL [34] embed knowledge grap |
| TKRL | ✅ oui | ove the task. For example, SSE [29] and TKRL [30] consider the entity type, PTransE |
| TransA | ✅ oui | [7], TransR [8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STr |
| TransG | ✅ oui | G2E [10], TransA [11], TranSparse [12], TransG [13], STransE [14], puTransE [15], and |
| TransH | ✅ oui | slation-based models (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], |
| TranSparse | ✅ oui | 8], TransD [9], KG2E [10], TransA [11], TranSparse [12], TransG [13], STransE [14], puTran |
| TransR | ✅ oui | d models (e.g., TransE [6], TransH [7], TransR [8], TransD [9], KG2E [10], TransA [11] |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| GCN | prose+table | ls, e.g. ProjE [21], ANALOGY [22] and R-GCN [28], also achieve good results for lin |
| KBGAN | prose+table | h outperforms GAN-based sampling method KBGAN. **INDEX TERMS** Knowledge graph, know |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._