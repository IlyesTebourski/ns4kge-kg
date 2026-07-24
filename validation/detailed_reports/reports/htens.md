# Validation — HTENS.md

**Titre extrait :** Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 15 |
| Extraites NON trouvees (FP -> erreur precision) | 3 |
| **Precision** | **83.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **48.4%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | r> </thead> <tbody> <tr> <td>FB15K</td> <td>14,951</td> <td>1,3 |
| FB15K237 | ✅ oui | 0/59,071</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <td>237 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | a person entity sharing the same occupation "actor" as the original entity "Thomas Ian Nicholas |
| Arxiv | Representations*. San Diego, CA, USA. http://arxiv.org/abs/1412.6575 [17] Yongqi Zhang, Quanmi |

## Metrics  —  precision 50% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | on two common metrics: Mean Reciprocal Rank (MRR) and Hits at 10 (H@10). The MRR measures mai |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 80% · recall~ 47%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | ing methods, such as Uniform sampling[2] and Bernoulli sampling[14], assign fixed sampling probabilities to |
| Cache-based Negative Sampling | ✅ oui | generator to construct negative samples. The cache-based sampling method[17] maintains a head cache and a tail |
| Hard Type Constraint | ✅ oui | samples that are more difficult to classify, Hard Type Constraint[9] and Soft Type Constraint[15] are proposed |
| Hierarchical Type Enhanced Negative Sampling | ✅ oui | # Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding **Zhenzhou Li |
| IGAN | ✅ oui | based sampling methods, such as KBGAN[3] and IGAN[13], set the KGE model to be trained as the |
| KBGAN | ✅ oui | ses. The GAN-based sampling methods, such as KBGAN[3] and IGAN[13], set the KGE model to be tra |
| KBGAN(pre) | ❌ NON | _(absent du texte)_ |
| KBGAN(raw) | ❌ NON | _(absent du texte)_ |
| Soft Type Constraint | ✅ oui | ult to classify, Hard Type Constraint[9] and Soft Type Constraint[15] are proposed. However, as the training p |
| Uniform Sampling | ✅ oui | distribution based sampling methods, such as Uniform sampling[2] and Bernoulli sampling[14], assign fixed |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | ing methods, such as Uniform sampling[2] and Bernoulli sampling[14], assign fixed sampling probabilities to |
| Dynamic Distribution Sampling | though substantial progress has been made by dynamic distribution based sampling methods, selecting plausible and prior infor |
| Dynamic Negative Sampling | and 0.0001 for FB15K237. this suggests the dynamic sampling methods may further improve the performance |
| GAN | nal entities as the training progresses. The GAN-based sampling methods, such as KBGAN[3] and |
| GAN-based Negative Sampling | nal entities as the training progresses. The GAN-based sampling methods, such as KBGAN[3] and IGAN[13], set |
| Local Closed-World Assumption | sup>1</sup> collected by [15] and follow the local closed-world assumptions[9]. The statistics of sub-types are shown in |
| Negative Sampling | # Hierarchical Type Enhanced Negative Sampling for Knowledge Graph Embedding **Zhenzhou Li |
| NSCaching | nming Yao, Yingxia Shao, and Lei Chen. 2019. NSCaching: Simple and Efficient Negative Sampling for |
| Uniform Negative Sampling | distribution based sampling methods, such as Uniform sampling[2] and Bernoulli sampling[14], assign fixed |

## KGE Models  —  precision 100% · recall~ 44%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | h as TransE[2], TransD[7], DistMult[16], and ComplEx[12], are proposed to project the entities an |
| DistMult | ✅ oui | (KGE) models, such as TransE[2], TransD[7], DistMult[16], and ComplEx[12], are proposed to projec |
| TransD | ✅ oui | h Embedding (KGE) models, such as TransE[2], TransD[7], DistMult[16], and ComplEx[12], are propo |
| TransE | ✅ oui | wledge Graph Embedding (KGE) models, such as TransE[2], TransD[7], DistMult[16], and ComplEx[12] |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | nal entities as the training progresses. The GAN-based sampling methods, such as KBGAN[3] and |
| HAN | ://doi.org/10.1109/TKDE.2020.3028705 [6] Xu Han, Shulin Cao, Xin Lv, Yankai Lin, Zhiyuan Liu |
| RatE | h default settings, except that the learning rate is set to 0.0005 for FB15K and 0.0001 for FB |
| SimplE | laume Bouchard. 2016. Complex Embeddings for Simple Link Prediction. In *Proceedings of The 33rd |
| TKRL | oter> <sup>1</sup>https://github.com/thunlp/TKRL SIGIR ’23, July 23–27, 2023, Taipei, Taiwan |
