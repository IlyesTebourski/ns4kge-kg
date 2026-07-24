# Validation — M2ixKG.md

**Titre extrait :** MixKG: Mixing for harder negative samples in knowledge graph

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 16 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **88.9%** |
| Candidats faux negatifs (dans le texte, non extraits) | 23 |
| **Recall relatif (indicatif, a valider)** | **41.0%** |

## Datasets  —  precision 100% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | nduct experiments on two public KG datasets: FB15k-237 [Toutanova and Chen, 2015] and WN18RR [Dettm |
| WN18RR | ✅ oui | ts: FB15k-237 [Toutanova and Chen, 2015] and WN18RR [Dettmers *et al.*, 2018]. FB15k-237 is a su |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2202.09606v1 [cs.AI] 19 Feb 2022 # MixKG: M |
| FB15k | nduct experiments on two public KG datasets: FB15k-237 [Toutanova and Chen, 2015] and WN18RR [D |
| Wikipedia | k. Yago3: A knowledge base from multilingual wikipedias. In *7th biennial conference on innovative d |
| WN18 | d triplets. Similarly, WN18RR is a subset of WN18 from WordNet KB, which is a large lexical En |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | rediction: mean reciprocal ranking (MRR) and Hits@10. Assuming $\mathcal{N}$ is the size of test |
| MRR | ✅ oui | or link prediction: mean reciprocal ranking (MRR) and Hits@10. Assuming $\mathcal{N}$ is the |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | great advantage of these models is that they map entities and relations in KGs into a low-dim |

## NS Methods  —  precision 80% · recall~ 42%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | : uniform sampling [Bordes et al., 2013] and Bernoulli sampling [Wang et al., 2014]. However, due to the res |
| IGAN | ✅ oui | ative samples from a dynamical distribution. IGAN [Wang et al., 2018] and KBGAN [Cai and Wang, |
| KBGAN | ✅ oui | l distribution. IGAN [Wang et al., 2018] and KBGAN [Cai and Wang, 2018] introduce generative ad |
| MixKG | ✅ oui | arXiv:2202.09606v1 [cs.AI] 19 Feb 2022 # MixKG: Mixing for harder negative samples in knowl |
| MixKG HNM-CES | ❌ NON | _(absent du texte)_ |
| MixKG HNM-SF | ❌ NON | _(absent du texte)_ |
| NSCaching | ✅ oui | select high-quality negative samples, while NSCaching [Zhang et al., 2019] utilizes cached-based m |
| RW-SANS | ✅ oui | e samples from the $l$-hop neighborhood. * **RW-SANS** [Ahrabian *et al.*, 2020] is similar to SA |
| SANS | ✅ oui | high-quality negative samples. Differently, SANS [Ahrabian et al., 2020] absorbs graph struct |
| Uniform Negative Sampling | ✅ oui | plets. Most current KG embedding models use uniform sampling to generate false triplets [Bordes et al., 2 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | : uniform sampling [Bordes et al., 2013] and Bernoulli sampling [Wang et al., 2014]. However, due to the res |
| Dynamic Negative Sampling | two categories: fixed negative sampling and dynamic negative sampling. ### Fixed negative sampling As a classic |
| GAN | g, Shuangyin Li, and Rong Pan. Incorporating gan for negative sampling in knowledge represent |
| Hard Negative Mixing | ert Bulent Sariyildiz, and et al. Pion, Noe. Hard negative mixing for contrastive learning. *arXiv preprint ar |
| MixGCF | chers use mixing for harder negative mining. MixGCF [Huang et al., 2021] uses positive mixing an |
| Negative Sampling | .AI] 19 Feb 2022 # MixKG: Mixing for harder negative samples in knowledge graph Feihu Che, Guohua Yang, |
| Simple Negative Sampling | wever, the present KGE models either rely on simple negative sampling methods, which makes it difficult to obtain |
| Structure-Aware Negative Sampling | n Ahrabian, Aarash Feizi, and et al. Salehi. Structure aware negative sampling in knowledge graphs. *arXiv preprint arXiv:2 |
| Uniform RW-SANS | esults of ComplEx for Uniform, Uniform SANS, Uniform RW-SANS are our reproductions using codes in [Ahrabi |
| Uniform Sampling | plets. Most current KG embedding models use uniform sampling to generate false triplets [Bordes et al., 2 |
| Uniform SANS | 19], and the results of ComplEx for Uniform, Uniform SANS, Uniform RW-SANS are our reproductions using |

## KGE Models  —  precision 100% · recall~ 36%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | ain informative negative triplets; or employ complex adversarial methods, which requires more tra |
| DistMult | ✅ oui | elect ComplEx [Trouillon *et al.*, 2016] and DistMult [Yang *et al.*, 2014] for semantic matching |
| RotatE | ✅ oui | e utilize TransE [Bordes *et al.*, 2013] and RotatE [Sun *et al.*, 2019], then select ComplEx [T |
| TransE | ✅ oui | For translational distance model, we utilize TransE [Bordes *et al.*, 2013] and RotatE [Sun *et |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | utilizes cached-based mechanism to pay more attention to high-quality negative samples. Differentl |
| DAT | nications of the ACM*, 1995. [Nguyen, 2017] Dat Quoc Nguyen. An overview of embedding models |
| GAN | g, Shuangyin Li, and Rong Pan. Incorporating gan for negative sampling in knowledge represent |
| LINE | ve samples. Overall, the monotone decreasing line tells that the criteria for selecting hard n |
| Random Walk | *et al.*, 2020] is similar to SANS, and uses random walks of length $l$ to approximate the $l$-hop nei |
| SimplE | wever, the present KGE models either rely on simple negative sampling methods, which makes it di |
| TaKE | milarity selector. The first criterion is to take the negative triplets with high scores in th |
