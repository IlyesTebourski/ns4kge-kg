# KGE Models — LTS.md

**Titre :** Knowledge Alignment Based on Negative Sampling of Potential Topic Similarities

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 9 |
| Modeles MENTIONNES seulement (hors tableaux) | 1 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 2 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 82% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| CTransR | ✅ oui | 8.7</td> </tr> <tr> <td>CTransR(unif/bern)</td> <td>243/231</td |
| SE | ✅ oui | ilt</th> </tr> <tr> <td>SE</td> <td>1011</td> <td> |
| TransD | ✅ oui | 0.2</td> </tr> <tr> <td>TransD(unif/bern)</td> <td>242/224</td |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>7.01</td> <td> |
| TransE-LTS | ✅ oui | .71</td> </tr> <tr> <td>TransE-LTS</td> <td>13.89</td> <td |
| TransE-SNS | ✅ oui | >74</td> </tr> <tr> <td>TransE-SNS(unif/bern)</td> <td>220/207</td |
| TransH | ✅ oui | 7.1</td> </tr> <tr> <td>TransH(unif/bern)</td> <td>318/401</td |
| TranSparse | ✅ oui | 7.3</td> </tr> <tr> <td>TranSparse(unif/bern)</td> <td>233/223</td |
| TransR | ✅ oui | 4.4</td> </tr> <tr> <td>TransR(unif/bern)</td> <td>232/238</td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| GAN | ✅ oui | c distribution sampling, represented by GAN[2], is used to provide high quality neg |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| LFM | table | 1.3</td> </tr> <tr> <td>LFM</td> <td>469</td> <td>4 |
| SME | table | 9.8</td> </tr> <tr> <td>SME</td> <td>542/526</td> < |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._