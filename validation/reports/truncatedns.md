# Validation — TruncatedNS.md

**Titre extrait :** Fusing Attribute Character Embeddings with Truncated Negative Sampling for Entity Alignment

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 29 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **96.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 11 |
| **Recall relatif (indicatif, a valider)** | **72.5%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| D-W15K | ✅ oui | > </tr> <tr> <th rowspan="2">D-W15K</th> <th>DB</th> <th>248</th |
| EN-DE15K | ✅ oui | > </tr> <tr> <th rowspan="2">EN-DE15K</th> <th>EN</th> <th>215</th |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | ts primarily include writers, cities, music, actors, etc. For both datasets, statistical data ar |
| Wikipedia | and temporally enhanced knowledge base from Wikipedia. *Artif. Intell.* **2013**, *194*, 28–61. [C |

## Metrics  —  precision 100% · recall~ 86%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | <tr> <th>Model</th> <th>Hits@1</th> <th>Hits@5</th> <th>Hit |
| Hits@10 | ✅ oui | s@1</th> <th>Hits@5</th> <th>Hits@10</th> <th>Hits@50</th> <th>MR |
| Hits@5 | ✅ oui | del</th> <th>Hits@1</th> <th>Hits@5</th> <th>Hits@10</th> <th>Hi |
| Hits@50 | ✅ oui | @5</th> <th>Hits@10</th> <th>Hits@50</th> <th>MRR</th> <th>MR</th |
| MR | ✅ oui | eriment, hits@k (k = 1, 5, 10, 50), MRR, and MR are used as evaluation metrics to evaluate t |
| MRR | ✅ oui | n the experiment, hits@k (k = 1, 5, 10, 50), MRR, and MR are used as evaluation metrics to ev |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | est baseline model, which indicates that the accuracy of the method in this paper is good in terms |

## NS Methods  —  precision 67% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Random Negative Sampling | ✅ oui | sampling strategy instead of the traditional random negative sampling strategy. This allows the model to learn mor |
| Truncated Negative Sampling | ✅ oui | # Fusing Attribute Character Embeddings with Truncated Negative Sampling for Entity Alignment Hongchan Li, Zhuang Zh |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Negative Sampling | ttribute Character Embeddings with Truncated Negative Sampling for Entity Alignment Hongchan Li, Zhuang Zh |
| Random Sampling | sampling strategy instead of the traditional random negative sampling strategy. This allows the model to learn mor |

## KGE Models  —  precision 100% · recall~ 76%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| BootEA | ✅ oui | of name, relationship, and attribute views. BootEA [24] proposes iterative entity alignment and |
| CrossE | ✅ oui | ity used in the entity triple, respectively. CrossE [13] believes that bidirectional effects bet |
| DAT | ✅ oui | tively updated using newly aligned entities. DAT [21] encodes both entity names and entity re |
| HAKE | ✅ oui | y and modelled entities in hyperbolic space. HAKE [16] believes that polar coordinates are mor |
| IPTransE | ✅ oui | study entity alignment based on embeddings. IPTransE [20] uses an iterative method of joint embed |
| JAPE | ✅ oui | ttribute-preserving embedding is proposed by JAPE [25], and entity embeddings are improved by |
| KD-CoE | ✅ oui | have been abstracted to related data types. KD-CoE [26] jointly learns multi-lingual entity des |
| MTransE | ✅ oui | t between two graphs. To solve this problem, MTransE [10] encodes entities and relationships sepa |
| MultiKE | ✅ oui | site function of the interaction embeddings. MultiKE [23] uses multiple views of entities to embe |
| MuRP | ✅ oui | cribed as rotation changes in complex space. MuRP [15] points out that the relationships betwe |
| RESCAL | ✅ oui | functions to gauge the rationality of facts. RESCAL [11] was the earliest semantic matching mode |
| RotatE | ✅ oui | een entities and relationships. According to RotatE [14], which can model and infer different re |
| SimplE | ✅ oui | ractions between latent factors of entities. SimplE [12] restricts the relationship matrix ($M_r |
| TransD | ✅ oui | ing two different projection matrices by the TransD [17] model, respectively. According to Trans |
| TransE | ✅ oui | dding-based entity alignment models, such as TransE [1]. This model learns entity embeddings by |
| TransEdge | ✅ oui | and performs well in handling tail entities. TransEdge [22] interacts with embeddings between head |
| TransH | ✅ oui | ion in the corresponding relationship space. TransH [19] thinks an entity can have many represen |
| TransR | ✅ oui | ransD [17] model, respectively. According to TransR [18], each entity is made up of several attr |
| Truncated Negative Sampling | ✅ oui | # Fusing Attribute Character Embeddings with Truncated Negative Sampling for Entity Alignment Hongchan Li, Zhuang Zh |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | or knowledge fusion have received widespread attention. In this article, we suggest a method for en |
| ComplEx | onships are described as rotation changes in complex space. MuRP [15] points out that the relatio |
| LINE | has a better generalization capability. In line with expectations, the TransE-based approach |
| RatE | 00, the batch size is 3000, and the learning rate is 0.01. Evaluation metrics: In the experim |
| SE | = \sum_{e \in G1 \cup G2} [1 - \text{sim}(e_{se}, e_{ce})] \eqno(11)$$ Electronics 2023, 12 |
| TaKE | llowing. **Add Function:** The add function takes the embedded vectors of each character of th |
