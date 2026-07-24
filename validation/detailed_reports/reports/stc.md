# Validation — STC.md

**Titre extrait :** Representation Learning of Knowledge Graphs with Hierarchical Types

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 16 |
| Extraites NON trouvees (FP -> erreur precision) | 16 |
| **Precision** | **50.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 14 |
| **Recall relatif (indicatif, a valider)** | **53.3%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | aper, we first use a typical knowledge graph FB15K [Bordes et al., 2013] to evaluate our models |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Wikipedia | nuous vector space by alignment models using Wikipedia anchors, entity names or entity descriptions |

## Metrics  —  precision 75% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | <tr> <th>Methods</th> <th>Accuracy(%)</th> </tr> </thead> <tbody> < |
| Hits@1 | ✅ oui | n="2">Mean Rank</th> <th colspan="2">Hits@1(%)</th> </tr> <tr> <th>Raw</ |
| Hits@10 | ✅ oui | ly outperform all baselines in mean rank and Hits@10. It indicates that the hierarchical type inf |
| MR | ❌ NON | _(absent du texte)_ |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 25% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| Soft Type Constraint | ✅ oui | propose a method for negative sampling named Soft Type Constraint (STC). STC improves the probability of selec |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Local Closed-World Assumption | pleteness located in KGs, we also follow the local closed-world assumptions (LCWA) proposed in [Krompaß et al., 2015] as |
| Negative Sampling | formalize a margin-based score function with negative sampling as objective for training: $$ L = \sum_{(h, |

## KGE Models  —  precision 48% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DKRL | ✅ oui | nchors, entity names or entity descriptions. DKRL [Xie *et al.*, 2016] proposes description-ba |
| LFM | ✅ oui | , 2011], SME [Bordes et al., 2012; 2014] and LFM [Jenatton et al., 2012], we directly use the |
| NTN | ✅ oui | ed in triples, is significant for RL in KGs. NTN [Socher *et al.*, 2013] encodes 3-way tensor |
| RESCAL | ✅ oui | their papers. For other baselines including RESCAL [Nickel et al., 2011; 2012], SE [Bordes et a |
| SE | ✅ oui | ncluding RESCAL [Nickel et al., 2011; 2012], SE [Bordes et al., 2011], SME [Bordes et al., 2 |
| SME | ✅ oui | al., 2011; 2012], SE [Bordes et al., 2011], SME [Bordes et al., 2012; 2014] and LFM [Jenatto |
| SME (bilinear) | ❌ NON | _(absent du texte)_ |
| SME (linear) | ❌ NON | _(absent du texte)_ |
| TKRL (RHE) | ❌ NON | _(absent du texte)_ |
| TKRL (RHE+STC) | ❌ NON | _(absent du texte)_ |
| TKRL (RHE+STC+TCE) | ❌ NON | _(absent du texte)_ |
| TKRL (WHE) | ❌ NON | _(absent du texte)_ |
| TKRL (WHE+STC) | ❌ NON | _(absent du texte)_ |
| TKRL (WHE+STC+TCE) | ❌ NON | _(absent du texte)_ |
| TransD | ✅ oui | when judging the distance between entities. TransD [Ji *et al.*, 2015] proposes dynamic mapping |
| TransE | ✅ oui | (TKRL). In TKRL, we follow the assumption in TransE [Bordes et al., 2013], considering relations |
| TransE+STC+TCE | ❌ NON | _(absent du texte)_ |
| TransE+TCE | ❌ NON | _(absent du texte)_ |
| TransH | ✅ oui | , N-to-1 and N-to-N. To address this issue, TransH [Wang *et al.*, 2014b] interprets relations |
| TransR | ✅ oui | different distances in different relations. TransR [Lin *et al.*, 2015b] directly models entiti |
| TransR+STC+TCE | ❌ NON | _(absent du texte)_ |
| TransR+TCE | ❌ NON | _(absent du texte)_ |
| Type-embodied Knowledge Representation Learning | ✅ oui | this paper, we propose a novel method named Type-embodied Knowledge Representation Learning (TKRL) to take advantages of hierarchical en |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ructured information in triples, paying less attention to the rich information located in hierarchi |
| HypER | s that of negative triple. $\gamma > 0$ is a hyper-parameter of margin. $T'$ stands for the neg |
| LINE | es sampled from Freebase, in which the solid lines indicate the most significant roles that hea |
| Neural Tensor Network | her D Manning, and Andrew Ng. Reasoning with neural tensor networks for knowledge base completion. In *Proceedin |
| Neural Tensor Networks | her D Manning, and Andrew Ng. Reasoning with neural tensor networks for knowledge base completion. In *Proceedin |
| RatE | ces are set to be $n \times n$. For learning rate $\lambda$, we could select a fixed rate foll |
| SimplE | among which the translation-based models are simple and effective with the state-of-the-art perf |
| Structured Embedding | Ronan Collobert, and Yoshua Bengio. Learning structured embeddings of knowledge bases. In *Proceedings of AAAI* |
| Structured Embeddings | Ronan Collobert, and Yoshua Bengio. Learning structured embeddings of knowledge bases. In *Proceedings of AAAI* |
| TaKE | Knowledge Representation Learning (TKRL) to take advantages of hierarchical entity types. We |
| TKRL | -embodied Knowledge Representation Learning (TKRL) to take advantages of hierarchical entity t |
