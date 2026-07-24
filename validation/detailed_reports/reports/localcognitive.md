# Validation — Localcognitive.md

**Titre extrait :** RatE: Relation-Adaptive Translating Embedding for Knowledge Graph Completion

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 25 |
| Extraites NON trouvees (FP -> erreur precision) | 4 |
| **Precision** | **86.2%** |
| Candidats faux negatifs (dans le texte, non extraits) | 12 |
| **Recall relatif (indicatif, a valider)** | **67.6%** |

## Datasets  —  precision 100% · recall~ 80%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k | ✅ oui | k prediction benchmark datasets, i.e., WN18, FB15k, WN18RR and FB15k-237, which shows state-of- |
| FB15k-237 | ✅ oui | mark datasets, i.e., WN18, FB15k, WN18RR and FB15k-237, which shows state-of-the-art results among |
| WN18 | ✅ oui | ur link prediction benchmark datasets, i.e., WN18, FB15k, WN18RR and FB15k-237, which shows st |
| WN18RR | ✅ oui | ction benchmark datasets, i.e., WN18, FB15k, WN18RR and FB15k-237, which shows state-of-the-art |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2010.04863v1 [cs.CL] 10 Oct 2020 # RatE: Re |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | @10</th> <th>Hits@3</th> <th>Hits@1</th> <th>MR</th> <th>MRR</th |
| Hits@10 | ✅ oui | <th>MR</th> <th>MRR</th> <th>Hits@10</th> <th>Hits@3</th> <th>Hit |
| Hits@3 | ✅ oui | RR</th> <th>Hits@10</th> <th>Hits@3</th> <th>Hits@1</th> <th>MR< |
| MR | ✅ oui | cs on link prediction tasks: 1) *mean rank* (MR) to describe the mean rank of the oracle tes |
| MRR | ✅ oui | cle test triples, 2) *mean reciprocal rank* (MRR), and 3) *Hits@N* ($N=1, 3, 10$) to denotes |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 83% · recall~ 45%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| KBGAN | ✅ oui | d to effectively learn structured knowledge. KBGAN (Cai and Wang, 2018) uses knowledge graph em |
| Local-cognitive negative sampling | ✅ oui | relation patterns. We also propose a novel local-cognitive negative sampling method, by integrating type-constraint train |
| Self-adversarial negative sampling | ✅ oui | thcal{G}^{(tr)}\}. \eqno(6) $$ In contrast, self-adversarial negative sampling (Sun et al., 2019) applies triple scoring fu |
| Type-constraint training | ✅ oui | ive negative sampling method, by integrating type-constraint training technique (Krompaß et al., 2015) with self-a |
| Uniform negative sampling | ✅ oui | al{G}^{(tr)}$. To achieve this, we conduct a uniform sampling individually in $\mathcal{E}^{(h,r,t)}$ and |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | {G}^{(tr)}\}. \eqno(6) $$ In contrast, self-adversarial negative sampling (Sun et al., 2019) applies triple scoring fu |
| Local Closed-World Assumption | sents a new link prediction setting based on local closed-world assumptions – the entities to corrupt a triple only come |
| Negative Sampling | o score each graph triple. Moreover, a novel negative sampling method is proposed to utilize both prior kno |
| Self-Adv | ative sampling methods. “Local-cognitive w/o self-adv loss” can be viewed as only using prior know |
| Self-adversarial Sampling | thcal{G}^{(tr)}\}. \eqno(6) $$ In contrast, self-adversarial negative sampling (Sun et al., 2019) applies triple scoring fu |
| Uniform Sampling | al{G}^{(tr)}$. To achieve this, we conduct a uniform sampling individually in $\mathcal{E}^{(h,r,t)}$ and |

## KGE Models  —  precision 79% · recall~ 69%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | nterpretability. Especially when extended to complex vector space, they show the capability in ha |
| ConvE | ✅ oui | l., 2016), ComplEx (Trouillon et al., 2016), ConvE (Dettmers et al., 2017) and QuatE (Zhang et |
| DistMult | ✅ oui | the approaches with semantic matching, e.g., DistMult (Yang et al., 2015) and QuatE (Zhang et al., |
| HolE | ✅ oui | s, we consider DistMult (Yang et al., 2015), HolE (Nickel et al., 2016), ComplEx (Trouillon et |
| QuatE | ✅ oui | hing, e.g., DistMult (Yang et al., 2015) and QuatE (Zhang et al., 2019), use a matching functio |
| RatE | ✅ oui | arXiv:2010.04863v1 [cs.CL] 10 Oct 2020 # RatE: Relation-Adaptive Translating Embedding for |
| Relation-adaptive translating Embedding | ✅ oui | iv:2010.04863v1 [cs.CL] 10 Oct 2020 # RatE: Relation-Adaptive Translating Embedding for Knowledge Graph Completion **Hao Huang, |
| RotatE | ✅ oui | ance, e.g., TransE (Bordes et al., 2013) and RotatE (Sun et al., 2019), first apply a translatio |
| TorusE | ✅ oui | 476. Takuma Ebisu and Ryutaro Ichise. 2018. Toruse: Knowledge graph embedding on a lie group. I |
| TransD | ❌ NON | _(absent du texte)_ |
| TransE | ✅ oui | he approaches with geometric distance, e.g., TransE (Bordes et al., 2013) and RotatE (Sun et al. |
| TransH | ❌ NON | _(absent du texte)_ |
| TransR | ❌ NON | _(absent du texte)_ |
| TuckER | ✅ oui | r> </thead> <tbody> <tr> <td>TuckER (Balazevic et al., 2019)</td> <td>-< |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ion answering over knowledge base with cross-attention combining global knowledge. In Regina Barzil |
| HypER | 37. **Training Setting.** The ranges of the hyper-parameters for grid search are elaborated in |
| LINE | e following two factors. On the one hand, in line with previous trans-based graph embedding ap |
| SimplE | laume Bouchard. 2016. Complex embeddings for simple link prediction. In Maria-Florina Balcan and |
| TaKE | y set during both training and test. We only take this idea in training phase to introduce pri |
