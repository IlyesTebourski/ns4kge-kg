# Validation — TypeAugmented.md

**Titre extrait :** A type-augmented knowledge graph embedding framework for knowledge graph completion

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 35 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **94.6%** |
| Candidats faux negatifs (dans le texte, non extraits) | 15 |
| **Recall relatif (indicatif, a valider)** | **70.0%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | limits the versatility of models. Such as in FB15k<sup>12</sup>, 10% of entities with the /musi |
| FB15K-237 | ✅ oui | used for KG completion: FB15K<sup>12</sup>, FB15K-237<sup>41</sup>, WN18<sup>12</sup> and YAGO3-10 |
| WN18 | ✅ oui | FB15K<sup>12</sup>, FB15K-237<sup>41</sup>, WN18<sup>12</sup> and YAGO3-10<sup>42</sup>. FB15 |
| YAGO3-10 | ✅ oui | B15K-237<sup>41</sup>, WN18<sup>12</sup> and YAGO3-10<sup>42</sup>. FB15K and FB15K-237 are two su |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | er hand, although *Andrew Stanton* is not an actor, he is a director that tends to be close to |
| Arxiv | nd knowledge graphs for question answering. *arXiv preprint arXiv:2104.06378* (2021). 6. Sha, X |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | s outperform their base models in *MRR* and *Hits@1/3/10* in most cases on all of the four datas |
| Hits@10 | ✅ oui | ets. Although on the WN18 dataset, RotatE’s *Hits@10* has slightly better performance, but the re |
| Hits@3 | ✅ oui | MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> <th>MR |
| MRR | ✅ oui | k prediction. One is *Mean Reciprocal Rank* (MRR), and the other is *Hits@N*. In order to int |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | ted representation<sup>11</sup>, KGE aims to map the elements (entities and relations) of KG |
| MR | pared to another similar metric *Mean Rank* (MR), which is largely influenced by a single ba |

## NS Methods  —  precision 67% · recall~ 36%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli negative sampling | ❌ NON | _(absent du texte)_ |
| Self-adversarial negative sampling | ✅ oui | Recently, Sun et al.<sup>15</sup> propose a self-adversarial negative sampling strategy and design a self-adversarial negat |
| Soft Type Constraint | ✅ oui | an improved negative sampling strategy named Soft Type Constraint (STC). It selects entities in the same type |
| Type-constrained negative sampling | ✅ oui | to distinct relations. We also design a new type-constrained negative sampling strategy to construct more effective negativ |
| Uniform negative sampling | ✅ oui | ost of the existing KEG models carry out the uniform sampling scheme as in<sup>12</sup>. To generate corru |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adversarial Negative Sampling | ntly, Sun et al.<sup>15</sup> propose a self-adversarial negative sampling strategy and design a self-adversarial negat |
| CAKE | ty. Besides, Niu et al.<sup>33</sup> propose CAKE which automatically extract commonsense from |
| Dynamic Negative Sampling | a candidate set of non-homogeneous entities. Dynamic sampling is performed respectively from them, so as t |
| Local Closed-World Assumption | pe-constrained method<sup>39</sup> applies a local closed-world assumption based on observed triples. For a given posit |
| Negative Sampling | tions. We also design a new type-constrained negative sampling strategy to construct more effective negativ |
| Self-adversarial Sampling | Recently, Sun et al.<sup>15</sup> propose a self-adversarial negative sampling strategy and design a self-adversarial negat |
| Uniform Sampling | ost of the existing KEG models carry out the uniform sampling scheme as in<sup>12</sup>. To generate corru |

## KGE Models  —  precision 100% · recall~ 85%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CAKE | ✅ oui | ty. Besides, Niu et al.<sup>33</sup> propose CAKE which automatically extract commonsense from |
| ComplEx | ✅ oui | $d$, and $\mathbf{z} \in \mathbb{C}^d$ is a complex vector of length $d$. $\\|\cdot\\|_p$ denotes |
| DistMult | ✅ oui | so competitive on many benchmarks, including DistMult<sup>18</sup>, ComplEx<sup>19</sup>, SimplE<s |
| HAKE | ✅ oui | edding to tail embedding. Soon after RotatE, HAKE<sup>16</sup> and RatE<sup>17</sup> make slig |
| JOIE | ✅ oui | ositions to model the semantic transitivity. JOIE<sup>24</sup> directly represents a KG as two |
| RatE | ✅ oui | ng. Soon after RotatE, HAKE<sup>16</sup> and RatE<sup>17</sup> make slight improvements to it. |
| RotatE | ✅ oui | rring these relation patterns, they proposed RotatE which maps triples to complex vector spaces |
| SimplE | ✅ oui | th the recent tensor factorization KGE model SimplE can achieve state-of-the-art performance on |
| TaKE | ✅ oui | gmented Knowledge graph Embedding framework (TaKE) which could utilize type features to enhanc |
| TaKE-ComplEx | ✅ oui | models, such as TaKE-TransE, TaKE-DistMult, TaKE-ComplEx, TaKE-SimplE and TaKE-RotatE. As Fig. 2 show |
| TaKE-DistMult | ✅ oui | TaKE-augmented models, such as TaKE-TransE, TaKE-DistMult, TaKE-ComplEx, TaKE-SimplE and TaKE-RotatE. |
| TaKE-RotatE | ✅ oui | TaKE-DistMult, TaKE-ComplEx, TaKE-SimplE and TaKE-RotatE. As Fig. 2 shows, we first adopt the embeddi |
| TaKE-SimplE | ✅ oui | as TaKE-TransE, TaKE-DistMult, TaKE-ComplEx, TaKE-SimplE and TaKE-RotatE. As Fig. 2 shows, we first a |
| TaKE-TransE | ✅ oui | ive models as TaKE-augmented models, such as TaKE-TransE, TaKE-DistMult, TaKE-ComplEx, TaKE-SimplE an |
| TaRP | ✅ oui | hese two views. Both TransT<sup>30</sup> and TaRP<sup>32</sup> collect relation types from ent |
| TKRL | ✅ oui | els exploring the usage of type information. TKRL<sup>22</sup> extends traditional TransE by e |
| TransC | ✅ oui | distinct representations in different types. TransC<sup>23</sup> clearly distinguish concepts (i |
| TransE | ✅ oui | nspired by tensor factorization techniques. TransE<sup>12</sup> is a typical translation-based |
| TransH | ✅ oui | ants of TransE have been developed. Such as, TransH<sup>13</sup> projects entity embeddings on d |
| TransR | ✅ oui | s. Instead of relation-specific hyperplanes, TransR<sup>14</sup> directly projects entity embedd |
| TransT | ✅ oui | w, and jointly encodes these two views. Both TransT<sup>30</sup> and TaRP<sup>32</sup> collect r |
| TypeComplex | ✅ oui | Jain et al.<sup>31</sup> propose TypeDM and TypeComplex to enhance DistMult and ComplEx respectively |
| TypeDM | ✅ oui | d WordNet), Jain et al.<sup>31</sup> propose TypeDM and TypeComplex to enhance DistMult and Comp |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ate on structured triples, while paying less attention to the type information of entities. In fact |
| HypER | $E_t$ and $\bar{E}_t$ respectively. $k$ is a hyper-parameter indicating that the probability of |
| LINE | k. In the following, we will introduce three lines of them that are closely related to our work |
| Relation-adaptive translating Embedding | Huang, H., Long, G., Shen, T. *et al.* Rate: Relation-adaptive translating embedding for knowledge graph completion. In *Proceedi |
