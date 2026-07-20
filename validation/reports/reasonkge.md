# Validation — ReasonKGE.md

**Titre extrait :** Improving Knowledge Graph Embeddings with Ontological Reasoning

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 17 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **94.4%** |
| Candidats faux negatifs (dans le texte, non extraits) | 24 |
| **Recall relatif (indicatif, a valider)** | **41.5%** |

## Datasets  —  precision 100% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DBPedia15K | ✅ oui | U</th> <th>Yago3-10</th> <th>DBPedia15K</th> </tr> </thead> <tbody> <tr> |
| LUBM3U | ✅ oui | ead> <tr> <th> </th> <th>LUBM3U</th> <th>Yago3-10</th> <th>D |
| Yago3-10 | ✅ oui | h> </th> <th>LUBM3U</th> <th>Yago3-10</th> <th>DBPedia15K</th> </tr> |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | aphs. CoRR **abs/1708.06816** (2017), http://arxiv.org/abs/1708.06816 22. Krompaß, D., Baier, |
| Company | locatedIn --> germany bosch -- type --> company john -. locatedIn .-> bosch subgrap |

## Metrics  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | <th> </th> <th>MRR</th> <th>Hits@1</th> <th>Hits@10</th> <th>MR |
| Hits@10 | ✅ oui | MRR</th> <th>Hits@1</th> <th>Hits@10</th> <th>MRR</th> <th>Hits@1 |
| MRR | ✅ oui | ls in terms of the traditional metrics i.e **MRR** and **Hits@k** in the filtered setting [9] |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | address this issue we propose to improve the accuracy of embeddings using ontological reasoning. M |
| Hits@3 | MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> <th>MR |
| MAP | hat are typically disjoint. (ii) The linear map assumption, *e.g.*, ComplEx [33] embeds enti |

## NS Methods  —  precision 89% · recall~ 44%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Distributional Negative Sampling | ✅ oui | world assumption [27]. Alternatives include Distributional Negative Sampling (DNS) [12] and its variation [2], where duri |
| Near Miss Sampling | ✅ oui | tion approach [30]. *Nearest Neighbor* and *Near Miss sampling* [21] resp. exploit a pre-trained embedding |
| Nearest Neighbor Sampling | ❌ NON | _(absent du texte)_ |
| NSCaching | ✅ oui | tive samples from a node’s neighborhood. The NSCaching sampling method [40] suggests to sample nega |
| Random Negative Sampling | ✅ oui | tive samples are generated using the default random sampling strategy<sup>4</sup>. In the subsequent iter |
| ReasonKGE | ✅ oui | ally, we present a novel iterative approach *ReasonKGE* that identifies dynamically via symbolic re |
| Static Sampling | ✅ oui | dding models. We refer to such technique as *static sampling* because in contrast to our proposed dynamic |
| Structure-Aware Negative Sampling | ✅ oui | for negative sampling. The work [1] presents structure-aware negative sampling (SANS), which utilizes the graph structure b |
| Type-Constrained Negative Sampling | ✅ oui | ]. Another related method is concerned with type-constrained negative sampling [22]. Given a triple from the KG, the negati |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Affinity Dependent Negative Sampling | en, H., Ali, M., Mohiuddin, K., Lehmann, J.: Affinity dependent negative sampling for knowledge graph embeddings. In: (DL4KG20 |
| Dynamic Negative Sampling | refer to this negative sampling strategy as *dynamic sampling*. On the one hand, this intuitively allows u |
| GAN | 35. Wang, P., Li, S., Pan, R.: Incorporating GAN for negative sampling in knowledge represent |
| Iterative Negative Sampling | in a nutshell # 3 Ontological Reasoning for Iterative Negative Sampling While a variety of embedding models exist i |
| KBGAN | p. 2787–2795 (2013) 10. Cai, L., Wang, W.Y.: KBGAN: adversarial learning for knowledge graph em |
| Negative Sampling | by a given embedding model and feeds them as negative samples for retraining this model. In order to addre |
| NSCaching Sampling | tive samples from a node’s neighborhood. The NSCaching sampling method [40] suggests to sample negatives fro |
| Random Sampling | tive samples are generated using the default random sampling strategy<sup>4</sup>. In the subsequent iter |
| SANS | presents structure-aware negative sampling (SANS), which utilizes the graph structure by sele |
| Unknown | ohn, worksAt, bosch \rangle$ holds or not is unknown. Given a triple $\alpha$, we denote by $Ent( |

## KGE Models  —  precision 100% · recall~ 25%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | athcal{I}}$. This assignment is extended to (complex) classes and roles as shown in Table 1. An |
| Embed2Reason | ✅ oui | ve sampling. For example, a related method *Embed2Reason (E2R)* has been proposed by Garg *et al.* [1 |
| TransE | ✅ oui | i) The translation-based assumption, *e.g.*, TransE [9] embeds entities and relations as vectors |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | 35. Wang, P., Li, S., Pan, R.: Incorporating GAN for negative sampling in knowledge represent |
| KBGAN | p. 2787–2795 (2013) 10. Cai, L., Wang, W.Y.: KBGAN: adversarial learning for knowledge graph em |
| LINE | ledge into KG Embeddings.** Another relevant line of work concerns the integration of ontologi |
| Neural Tensor Network | D., Manning, C.D., Ng, A.Y.: Reasoning with neural tensor networks for knowledge base completion. In: NIPS. pp. |
| Neural Tensor Networks | D., Manning, C.D., Ng, A.Y.: Reasoning with neural tensor networks for knowledge base completion. In: NIPS. pp. |
| ReasonKGE | ally, we present a novel iterative approach *ReasonKGE* that identifies dynamically via symbolic re |
| SimplE | er, É., Bouchard, G.: Complex embeddings for simple link prediction. In: ICML. pp. 2071–2080 (20 |
| StAR | thcal{G}) \cup \mathcal{O}$ is consistent ($\star$). From the assumption that $\text{Relv}(\al |
| TaKE | dicted triple is ignored). Therefore, we can take $\langle bosch, locatedIn, bob \rangle$ as a |
