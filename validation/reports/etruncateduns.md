# Validation — eTruncatedUNS.md

**Titre extrait :** Bootstrapping Entity Alignment with Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **90.5%** |
| Candidats faux negatifs (dans le texte, non extraits) | 14 |
| **Recall relatif (indicatif, a valider)** | **57.6%** |

## Datasets  —  precision 100% · recall~ 83%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DBP-WD | ✅ oui | > <tbody> <tr> <td rowspan="2">DBP-WD</td> <td>DBpedia</td> <td>10 |
| DBP-YG | ✅ oui | > </tr> <tr> <td rowspan="2">DBP-YG</td> <td>DBpedia</td> <td>10 |
| DBP_FR-EN | ✅ oui | 0.72</td> </tr> <tr> <td>(C) DBP_FR-EN</td> <td>S1</td> <td>0.58</t |
| DBP_JA-EN | ✅ oui | 0.75</td> </tr> <tr> <td>(B) DBP_JA-EN</td> <td>S1</td> <td>0.46</t |
| DBP_ZH-EN | ✅ oui | </thead> <tbody> <tr> <td>(A) DBP_ZH-EN</td> <td>S1</td> <td>0.48</t |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Wikipedia | e of external lexicons, machine translation, Wikipedia links [Suchanek et al., 2012; Wang et al., 2 |

## Metrics  —  precision 100% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | ">DBP-YG</th> </tr> <tr> <th>Hits@1</th> <th>Hits@10</th> <th>MR |
| Hits@10 | ✅ oui | <tr> <th>Hits@1</th> <th>Hits@10</th> <th>MRR</th> <th>Hits@1 |
| MRR | ✅ oui | @1</th> <th>Hits@10</th> <th>MRR</th> <th>Hits@1</th> <th>Hit |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | ed on a global optimal goal to guarantee the accuracy, and employs an alignment editing method to |
| F1 | Prec.</th> <th>Rec.</th> <th>F1-score</th> </tr> </thead> <tbody> |

## NS Methods  —  precision 33% · recall~ 33%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Epsilon-Truncated Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling | ✅ oui | triples, we propose an $\epsilon$-truncated uniform negative sampling method. We also swap aligned entities betwee |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | , we propose an $\epsilon$-truncated uniform negative sampling method. We also swap aligned entities betwee |
| Uniform Sampling | triples, we propose an $\epsilon$-truncated uniform negative sampling method. We also swap aligned entities betwee |

## KGE Models  —  precision 100% · recall~ 53%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AlignE | ✅ oui | td>0.320</td> </tr> <tr> <td>AlignE</td> <td>47.18</td> <td>79.1 |
| BootEA | ✅ oui | d Tensorflow to develop our approach, called BootEA. Our experiments were conducted on a persona |
| IPTransE | ✅ oui | ransforming monolingual KG embedding spaces. IPTransE [Zhu et al., 2017] represents different KGs |
| JAPE | ✅ oui | ing parameter sharing on existing alignment. JAPE [Sun et al., 2017] refines KG embeddings for |
| KR-EAR | ✅ oui | rporates reverse triples and relation paths. KR-EAR [Lin et al., 2016] introduces categorical at |
| MTransE | ✅ oui | ding different KGs towards entity alignment. MTransE [Chen et al., 2017] performs cross-lingual e |
| PTransE | ✅ oui | al., 2014], TransR [Lin et al., 2015b] and PTransE [Lin et al., 2015a]. Most existing KG embed |
| TransE | ✅ oui | the inherent KG semantics. As an early work, TransE [Bordes et al., 2013] interprets a relation |
| TransH | ✅ oui | t is further improved by many works, such as TransH [Wang et al., 2014], TransR [Lin et al., 20 |
| TransR | ✅ oui | works, such as TransH [Wang et al., 2014], TransR [Lin et al., 2015b] and PTransE [Lin et al., |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | y, knowledge graphs (KGs) attract increasing attentions and are being widely used in AI-related appl |
| ComplEx | e recurrent neural networks for modeling the complex semantics of KGs. # Acknowledgments This w |
| HypER | \cdot, 0)$. $\gamma_1, \gamma_2 > 0$ are two hyper-parameters and $\mu_1 > 0$ is a balance hype |
| LINE | in confirmed the effectiveness of BootEA. In line with our expectations, the F1-score of all t |
| Neural Tensor Network | D. Manning, and Andrew Y. Ng. Reasoning with neural tensor networks for knowledge base completion. In *Proceedin |
| Neural Tensor Networks | D. Manning, and Andrew Y. Ng. Reasoning with neural tensor networks for knowledge base completion. In *Proceedin |
| RatE | mpled for each positive triple. The learning rate was set to 0.01 and the training spent 500 e |
| SimplE | ed in the subsequent iterations. We employ a simple but effective editing technique to achieve t |
| TaKE | $-nearest neighbors for one entity averagely takes linear time using the quick select algorithm |
