# Validation — GHN.md

**Titre extrait :** Improving Knowledge Graph Completion with Generative Hard Negative Mining

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 28 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **93.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 11 |
| **Recall relatif (indicatif, a valider)** | **71.8%** |

## Datasets  —  precision 100% · recall~ 60%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | GC datasets (WN18RR (Dettmers et al., 2017), FB15K237 (Toutanova and Chen, 2015a), and Wikidata (W |
| Wikidata5M | ✅ oui | d>20,466</td> </tr> <tr> <td>Wikidata5M</td> <td>4,594,485</td> <td> |
| WN18RR | ✅ oui | te our method on three popular KGC datasets (WN18RR (Dettmers et al., 2017), FB15K237 (Toutanova |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | ctorization for knowledge graph completion. *arXiv preprint arXiv:1901.09590*. Kurt Bollacker, |
| FB15k | td>3,134</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <td |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | r> <tr> <th>MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hit |
| Hits@10 | ✅ oui | s@1</th> <th>Hits@3</th> <th>Hits@10</th> <th>MRR</th> <th>Hits@1 |
| Hits@3 | ✅ oui | MRR</th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> <th>MR |
| MRR | ✅ oui | B15k-237</th> </tr> <tr> <th>MRR</th> <th>Hits@1</th> <th>Hit |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Accuracy | {L}_{gen}$ as the objective until validation accuracy did not significantly increase for 5k steps. |
| MAP | nce the generated sequences are difficult to map to unseen entities. Therefore, we will explo |

## NS Methods  —  precision 82% · recall~ 82%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Adversarial Contrast | ✅ oui | ao Wang, Wei Hu, and Guo-Jun Qi. 2020. Adco: Adversarial contrast for efficient learning of unsupervised repre |
| Approximate Nearest Neighbor Negative Sampling | ✅ oui | pact of generated negatives, we construct an approximate nearest neighbor negative sampling strategy (ANN) inspired by Xiong et al. (202 |
| Generative Hard Negative Mining | ✅ oui | # Improving Knowledge Graph Completion with Generative Hard Negative Mining **Zile Qiao¹, Wei Ye² , Dingyao Yu², Tong M |
| GHN-SL | ✅ oui | <td>51.1</td> </tr> <tr> <td>GHN-SL</td> <td>67.3</td> <td>59.3< |
| Hard Negative Mixing | ✅ oui | hilippe Weinzaepfel, and Diane Larlus. 2020. Hard negative mixing for contrastive learning. *ArXiv, abs/2010.0 |
| In-batch Negative Sampling | ✅ oui | lf-information, respectively. IB denotes the in-batch sampling strategy. ANN denotes the nearest neighbor n |
| NSCaching | ✅ oui | nming Yao, Yingxia Shao, and Lei Chen. 2018. Nscaching: Simple and efficient negative sampling for |
| Pre-batch Negative Sampling | ❌ NON | _(absent du texte)_ |
| Reinforced Negative Sampling | ✅ oui | xin Cao, Meng Wang, and Tat-Seng Chua. 2020. Reinforced negative sampling over knowledge graph for recommendation. *Pr |
| Self Negative Sampling | ✅ oui | iant of SimKGC with in-batch, pre-batch, and self-negative sampling strategy, respectively (Wang et al., 2022).) |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Nearest Neighbor Sampling | rated negatives, we construct an approximate nearest neighbor negative sampling strategy (ANN) inspired by Xiong et al. (202 |
| Negative Sampling | inguistics are two essential properties for negative sample selection: * **Vicinity** (Robinson et al |

## KGE Models  —  precision 100% · recall~ 71%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | s et al., 2013), TransH (Wang et al., 2014), Complex (Trouillon et al., 2016), and RotatE (Sun et |
| DistMult | ✅ oui | ion of the binary representation of triples. DistMult (Yang et al., 2014) models the three-way int |
| DKRL | ✅ oui | els a relation as rotation in complex space. DKRL (Xie et al., 2016) leverages a CNN network t |
| KEPLER | ✅ oui | CNN network to obtain text representations. KEPLER (Wang et al., 2019) uses a Transformer-based |
| KG-BERT | ✅ oui | The textual mentions we used are provided by KG-BERT (Yao et al., 2019). Then we formally describ |
| MTL-KGC | ✅ oui | and the masked language modeling objective. MTL-KGC (Kim et al., 2020) proposes a multi-task lea |
| RotatE | ✅ oui | 2014), Complex (Trouillon et al., 2016), and RotatE (Sun et al., 2019b), etc. **Text-based metho |
| SimKGC | ✅ oui | 2022). The recent robust text-based method, SimKGC (Wang et al., 2022), tackles the sub-optimal |
| StAR | ✅ oui | properties. KG-BERT (Yao et al., 2019) and StAR (Wang et al., 2021) both leverage pre-traine |
| TransE | ✅ oui | on of graphs. Representative efforts include TransE (Bordes et al., 2013), TransH (Wang et al., |
| TransH | ✅ oui | fforts include TransE (Bordes et al., 2013), TransH (Wang et al., 2014), Complex (Trouillon et a |
| Tucker | ✅ oui | (2016) introduces complex number embeddings. Tucker (Balažević et al., 2019) facilitate KGC base |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | , Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. *Advances in neural informa |
| BERT | textual mentions we used are provided by KG-BERT (Yao et al., 2019). Then we formally describ |
| RatE | We use AdamW optimizer with linear learning rate decay, the learning rate is initialized to $ |
| SimplE | tor** Saxena et al. (2022) has proved that a simple encoder-decoder Transformer (Vaswani et al., |
| TaKE | ecture. The first encoder $\text{BERT}_{hr}$ takes the text query $t_{hr}$ as input and produce |
