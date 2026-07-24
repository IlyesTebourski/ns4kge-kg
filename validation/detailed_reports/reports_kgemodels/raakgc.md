# KGE Models — RAAKGC.md

**Titre :** Knowledge Graph Completion with Relation-Aware Anchor Enhancement

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 14 |
| Modeles MENTIONNES seulement (hors tableaux) | 9 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 1 |
| Candidats mentions ratees (bruts) | 2 |
| Recall BRUT evalues / mentionnes | 93% / 82% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | 9.2</td> </tr> <tr> <td>ComplEx</td> <td>46.8</td> <td> |
| ConvE | ✅ oui | 5.9</td> </tr> <tr> <td>ConvE</td> <td>45.6</td> <td> |
| DistMult | ✅ oui | 9.7</td> </tr> <tr> <td>DistMult</td> <td>44.4</td> <td> |
| HaSa | ✅ oui | 4.9</td> </tr> <tr> <td>HaSa</td> <td>53.8</td> <td> |
| InsKGC | ✅ oui | s for the text-based methods, we choose InsKGC (Jiang, Drummond, and Cohn 2023) and Si |
| KG-BERT | ✅ oui | ods</td> </tr> <tr> <td>KG-BERT</td> <td>21.6</td> <td> |
| MTL-KGC | ✅ oui | d>-</td> </tr> <tr> <td>MTL-KGC</td> <td>33.1</td> <td> |
| QuatE | ✅ oui | 9.0</td> </tr> <tr> <td>QuatE</td> <td>48.1</td> <td> |
| RAA-KGC | ✅ oui | d>-</td> </tr> <tr> <td>RAA-KGC</td> <td><strong><u>59.74</u></ |
| RGCN | ✅ oui | d>-</td> </tr> <tr> <td>RGCN</td> <td>42.7</td> <td> |
| RotatE | ✅ oui | d>-</td> </tr> <tr> <td>RotatE</td> <td>47.6</td> <td> |
| SimKGC | ✅ oui | d>-</td> </tr> <tr> <td>SimKGC</td> <td>55.31</td> <td |
| StAR | ✅ oui | d>-</td> </tr> <tr> <td>StAR</td> <td>40.1</td> <td> |
| TransE | ✅ oui | ods</td> </tr> <tr> <td>TransE</td> <td>24.3</td> <td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| BERTRL | ✅ oui | lation-aware neighborhood of the query. BERTRL (Zha, Chen, and Yan 2022) collects poss |
| ConKGC | ✅ oui | he query as extra context to the model. ConKGC (Shang et al. 2023) introduces a sampli |
| DKRL | ✅ oui | . 2024). The pioneer text-based method, DKRL (Xie et al. 2016), initially integrates |
| GenKGC | ✅ oui | sion. Besides the mentioned algorithms, GenKGC (Xie et al. 2022) and KICGPT (Wei et al |
| KEPLER | ✅ oui | ng KG-BERT (Yao, Mao, and Luo 2019) and KEPLER (Wang et al. 2021b), utilize a Pre-trai |
| KG-S2S | ✅ oui | KGT5-context (Kochsiek et al. 2023) and KG-S2S (Chen et al. 2022a) model the link pred |
| KGT5-context | ✅ oui | r encoding text descriptions. Moreover, KGT5-context (Kochsiek et al. 2023) and KG-S2S (Chen |
| KICGPT | ✅ oui | lgorithms, GenKGC (Xie et al. 2022) and KICGPT (Wei et al. 2023) go beyond the neighbo |
| LMKE | ✅ oui | s by the decoder directly. Furthermore, LMKE (Wang et al. 2022b) introduces a contra |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| BERT | prose+table | twork. Subsequent studies, including KG-BERT (Yao, Mao, and Luo 2019) and KEPLER (Wa |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | ng promising performance and increasing attention for the rapid development of large lang |
| KGT5 | prose | r encoding text descriptions. Moreover, KGT5-context (Kochsiek et al. 2023) and KG-S |