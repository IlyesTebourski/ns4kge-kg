# Validation — LTS.md

**Titre extrait :** Knowledge Alignment Based on Negative Sampling of Potential Topic Similarities

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 21 |
| Extraites NON trouvees (FP -> erreur precision) | 5 |
| **Precision** | **80.8%** |
| Candidats faux negatifs (dans le texte, non extraits) | 11 |
| **Recall relatif (indicatif, a valider)** | **65.6%** |

## Datasets  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DBP-GEO | ✅ oui | s paper uses the public datasets DBP-LGD and DBP-GEO for evaluation, with the evaluation metric H |
| DBP-LGD | ✅ oui | nsE-LTS, this paper uses the public datasets DBP-LGD and DBP-GEO for evaluation, with the evaluat |
| FB15K | ✅ oui | r> </thead> <tbody> <tr> <td>FB15K</td> <td>14951</td> <td>1345 |
| WN18 | ✅ oui | td>59071</td> </tr> <tr> <td>WN18</td> <td>40943</td> <td>18</ |

_Aucun candidat faux negatif pour cette categorie._

## Metrics  —  precision 33% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ❌ NON | _(absent du texte)_ |
| Hits@10 | ✅ oui | O for evaluation, with the evaluation metric Hits@10. The experimental results are shown in Table |
| MR | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MRR | Hits@k* indicating a more effective method. *MRR* (Mean Reciprocal Rank) [6] represents the a |

## NS Methods  —  precision 67% · recall~ 55%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Custom Pooled Sampling | ✅ oui | Sampling, Dynamic Distribution Sampling and Custom Pooled Sampling respectively. Static distributions can be di |
| Dynamic Distribution Sampling | ✅ oui | let. These are Static Distribution Sampling, Dynamic Distribution Sampling and Custom Pooled Sampling respectively. Sta |
| GAN | ✅ oui | ynamic distribution sampling, represented by GAN[2], is used to provide high quality negative |
| Negative Sampling of Potential Topic Similarities | ✅ oui | L) # Knowledge Alignment Based on Negative Sampling of Potential Topic Similarities *Wei Tian School of Computer, Zhongyuan Uni |
| Random Negative Sampling | ✅ oui | ic, to solve the zero-loss problem caused by random negative sampling. Entity alignment algorithms can be divided |
| Static Distribution Sampling | ✅ oui | e a high quality negative triplet. These are Static Distribution Sampling, Dynamic Distribution Sampling and Custom Po |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN-pretrain | 1</td> </tr> <tr> <td>TransE+GAN-pretrain</td> <td>—</td> <td>240</td> |
| GAN-scratch | 9</td> </tr> <tr> <td>TransE+GAN-scratch</td> <td>—</td> <td>244</td> |
| Gibbs Negative Sampling | chlet distribution. The LDA topic model uses Gibbs sampling to sample the implicit topic of the t word o |
| Negative Sampling | ng (ICICML) # Knowledge Alignment Based on Negative Sampling of Potential Topic Similarities *Wei Tian S |
| Random Sampling | ic, to solve the zero-loss problem caused by random negative sampling. Entity alignment algorithms can be divided |

## KGE Models  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CTransR | ✅ oui | 5.5/68.7</td> </tr> <tr> <td>CTransR(unif/bern)</td> <td>243/231</td> |
| GAN | ✅ oui | ynamic distribution sampling, represented by GAN[2], is used to provide high quality negative |
| SE | ✅ oui | <th>Filt</th> </tr> <tr> <td>SE</td> <td>1011</td> <td>985</ |
| TransD | ✅ oui | 6.3/70.2</td> </tr> <tr> <td>TransD(unif/bern)</td> <td>242/224</td> |
| TransE | ✅ oui | ail entity is replaced in a similar way. The TransE-LTS was obtained by combining a negative sam |
| TransE-LTS | ✅ oui | ail entity is replaced in a similar way. The TransE-LTS was obtained by combining a negative samplin |
| TransE-SNS | ✅ oui | ample from a small number of candidates e.g. TransE-SNS[3]. However, the existing negative sampling |
| TransH | ✅ oui | <td>47.1</td> </tr> <tr> <td>TransH(unif/bern)</td> <td>318/401</td> |
| TranSparse | ✅ oui | 4.2/77.3</td> </tr> <tr> <td>TranSparse(unif/bern)</td> <td>233/223</td> |
| TransR | ✅ oui | 8.5/64.4</td> </tr> <tr> <td>TransR(unif/bern)</td> <td>232/238</td> |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| HAN | C from IEEE Xplore. Restrictions apply. [5] Han X, Zhang C, Sun T, et al. A triple-branch ne |
| LFM | 0.8/41.3</td> </tr> <tr> <td>LFM</td> <td>469</td> <td>456</t |
| RatE | eriod epoch $\in \{50, 100, 150\}$, learning rate $\in \{0.1, 0.01, 0.001, 0.0001\}$, embeddin |
| SME | <td>39.8</td> </tr> <tr> <td>SME</td> <td>542/526</td> <td>53 |
| TaKE | ns and improved Bernoulli distributions that take into account relational substitution. Dynami |
