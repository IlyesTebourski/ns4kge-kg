# KGE Models — STC.md

**Titre :** Representation Learning of Knowledge Graphs with Hierarchical Types

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 17 |
| Modeles MENTIONNES seulement (hors tableaux) | 6 |
| **Precision globale** | **65%** |
| Precision (evalues, vs tableaux) | 53% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 90% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| LFM | ✅ oui | 1.3</td> </tr> <tr> <td>LFM</td> <td>283</td> <td>1 |
| RESCAL | ✅ oui | </thead> <tbody> <tr> <td>RESCAL</td> <td>828</td> <td>6 |
| SE | ✅ oui | 4.1</td> </tr> <tr> <td>SE</td> <td>273</td> <td>1 |
| SME (bilinear) | ✅ oui | 0.8</td> </tr> <tr> <td>SME (bilinear)</td> <td>284</td> <td> |
| SME (linear) | ✅ oui | 9.8</td> </tr> <tr> <td>SME (linear)</td> <td>274</td> <td> |
| TKRL (RHE) | ✅ oui | 7.2</td> </tr> <tr> <td>TKRL (RHE)</td> <td><strong>184</strong>< |
| TKRL (RHE+STC) | ❌ NON | _(absent des tableaux)_ |
| TKRL (RHE+STC+TCE) | ❌ NON | _(absent des tableaux)_ |
| TKRL (WHE) | ✅ oui | 9.4</td> </tr> <tr> <td>TKRL (WHE)</td> <td>186</td> <td> |
| TKRL (WHE+STC) | ❌ NON | _(absent des tableaux)_ |
| TKRL (WHE+STC+TCE) | ❌ NON | _(absent des tableaux)_ |
| TransE | ✅ oui | 3.1</td> </tr> <tr> <td>TransE</td> <td>238</td> <td>1 |
| TransE+STC+TCE | ❌ NON | _(absent des tableaux)_ |
| TransE+TCE | ❌ NON | _(absent des tableaux)_ |
| TransR | ✅ oui | 2.1</td> </tr> <tr> <td>TransR</td> <td>199</td> <td>7 |
| TransR+STC+TCE | ❌ NON | _(absent des tableaux)_ |
| TransR+TCE | ❌ NON | _(absent des tableaux)_ |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| DKRL | ✅ oui | s, entity names or entity descriptions. DKRL [Xie *et al.*, 2016] proposes descripti |
| NTN | ✅ oui | triples, is significant for RL in KGs. NTN [Socher *et al.*, 2013] encodes 3-way t |
| SME | ✅ oui | 2011; 2012], SE [Bordes et al., 2011], SME [Bordes et al., 2012; 2014] and LFM [Je |
| TransD | ✅ oui | judging the distance between entities. TransD [Ji *et al.*, 2015] proposes dynamic ma |
| TransH | ✅ oui | o-1 and N-to-N. To address this issue, TransH [Wang *et al.*, 2014b] interprets relat |
| Type-embodied Knowledge Representation Learning | ✅ oui | paper, we propose a novel method named Type-embodied Knowledge Representation Learning (TKRL) to take advantages of hierarchic |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| TKRL | prose+table | died Knowledge Representation Learning (TKRL) to take advantages of hierarchical ent |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._