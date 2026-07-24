# Validation — dans.md

**Titre extrait :** Diversified and Adaptive Negative Sampling on Knowledge Graphs

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 22 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **91.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 33 |
| **Recall relatif (indicatif, a valider)** | **40.0%** |

## Datasets  —  precision 100% · recall~ 43%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| NELL-995 | ✅ oui | ons to minimize leakage from training. (2) **NELL-995** [8] is a subset of the web-based facts col |
| UMLS | ✅ oui | ly the top 200 relations are retained. (3) **UMLS** [7] is a specialized knowledge base contai |
| WN18RR | ✅ oui | ge graphs are used for our experiment. (1) **WN18RR** [2], a harder variant of WN18 [7], which i |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2410.07592v2 [cs.AI] 26 Oct 2025 # Diversif |
| FB15k | ncluded the experimental results for dataset FB15k-237 which show favorable performance on Comp |
| FB15k-237 | ncluded the experimental results for dataset FB15k-237 which show favorable performance on ComplEx |
| WN18 | ent. (1) **WN18RR** [2], a harder variant of WN18 [7], which is derived from WordNet consistin |

## Metrics  —  precision 67% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ❌ NON | _(absent du texte)_ |
| MRR | ✅ oui | g metrics including Mean Reciprocal Ranking (MRR), Hit ratio at 1 (H@1) and Normalized discou |
| NDCG@5 | ✅ oui | Normalized discounted cumulative gain at 5 (NDCG@5) [28]. Details of these ranking metrics can |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| NDCG | Normalized discounted cumulative gain at 5 (NDCG@5) [28]. Details of these ranking metrics ca |

## NS Methods  —  precision 92% · recall~ 41%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| CAKE | ✅ oui | to generate informative negative triplets; **CAKE** [19]: a framework which leverages extra in |
| Diversified and Adaptive Negative Sampling | ✅ oui | arXiv:2410.07592v2 [cs.AI] 26 Oct 2025 # Diversified and Adaptive Negative Sampling on Knowledge Graphs Ran Liu¹, Zhongzhou Liu |
| GNDN | ✅ oui | such as KBGAN [3], IGAN [30], HeGAN [11] and GNDN [38], which learn the underlying sample dist |
| HeGAN | ✅ oui | ets (GAN) [10] such as KBGAN [3], IGAN [30], HeGAN [11] and GNDN [38], which learn the underlyi |
| IGAN | ✅ oui | versarial nets (GAN) [10] such as KBGAN [3], IGAN [30], HeGAN [11] and GNDN [38], which learn |
| KBGAN | ✅ oui | previous state-of-the-art approaches such as KBGAN [3], we adopt a generative adversarial netwo |
| Markov Chain Monte Carlo Negative Sampling | ❌ NON | _(absent du texte)_ |
| NSCaching | ✅ oui | itive nodes via random walks on the graph; **NSCaching** [39]: a model that employs importance samp |
| Popularity-weighted Negative Sampling | ✅ oui | entity [2]. Unfortunately, in uniform [2] or popularity-weighted sampling [17], the sampled entity could be completely |
| Random Negative Sampling | ✅ oui | negative triplets are often obtained through random sampling. More recent works [34, 3] explore advanced |
| Self-adversarial Negative Sampling | ✅ oui | rity-weighted sampling; **Self-adv** [28]: a self-adversarial negative sampling methodology; **MCNS** [36]: a model which de |
| SMiLE | ✅ oui | tual triplets to sample negative triplets; **SMiLE** [22]: a framework which employs specific c |
| Structure-Aware Negative Sampling | ✅ oui | A., Salehi, Y., Hamilton, W.L., Bose, A.J.: Structure aware negative sampling in knowledge graphs. arXiv preprint arXiv:20 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adaptive Negative Sampling | 592v2 [cs.AI] 26 Oct 2025 # Diversified and Adaptive Negative Sampling on Knowledge Graphs Ran Liu¹, Zhongzhou Liu |
| Adversarial Negative Sampling | weighted sampling; **Self-adv** [28]: a self-adversarial negative sampling methodology; **MCNS** [36]: a model which de |
| Bayesian Personalized Ranking | r, C., Gantner, Z., Schmidt-Thieme, L.: Bpr: Bayesian personalized ranking from implicit feedback. arXiv preprint arXiv |
| GAN | , we adopt a generative adversarial network (GAN) [30] for the generation of negative samples |
| GAN-based Negative Sampling | re two significant differences from previous GAN-based negative sampling on the knowledge graph. First, we design a t |
| Importance Sampling | [3, 30], reinforcement learn- ing [31], and importance sampling [39]. These methods provide a more explicit |
| Negative Sampling | .AI] 26 Oct 2025 # Diversified and Adaptive Negative Sampling on Knowledge Graphs Ran Liu¹, Zhongzhou Liu |
| PinSAGE | for negative sampling. In a similar spirit, PinSage [14] generates localized graphs via random w |
| Random Sampling | negative triplets are often obtained through random sampling. More recent works [34, 3] explore advanced |
| Reinforced Negative Sampling | , Y., He, X., Cao, Y., Wang, M., Chua, T.S.: Reinforced negative sampling over knowledge graph for recommendation. In: |
| SANS | ghborhood of positive examples. For example, SANS [1] hypothesizes that entities that are in c |
| Self-Adv | ampling with popularity-weighted sampling; **Self-adv** [28]: a self-adversarial negative sampling |
| Self-adversarial Sampling | rity-weighted sampling; **Self-adv** [28]: a self-adversarial negative sampling methodology; **MCNS** [36]: a model which de |
| Uniform Negative Sampling | p** [17]: a variant of Rand that substitutes uniform sampling with popularity-weighted sampling; **Self-ad |
| Uniform Random Negative Sampling | ining ten negative triplets are obtained via uniform random sampling to further increase the diversity. In all ca |
| Uniform Random Sampling | ining ten negative triplets are obtained via uniform random sampling to further increase the diversity. In all ca |
| Uniform Sampling | p** [17]: a variant of Rand that substitutes uniform sampling with popularity-weighted sampling; **Self-ad |

## KGE Models  —  precision 100% · recall~ 31%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | ree popular decoders, namely, DistMult [35], ComplEx [29] and RotatE [27]. We provide the DistMul |
| DistMult | ✅ oui | al{F}$ using three popular decoders, namely, DistMult [35], ComplEx [29] and RotatE [27]. We provi |
| RGCN | ✅ oui | ayer relational graph convolutional network (RGCN) [26] to serve as our base embedding model i |
| RotatE | ✅ oui | ers, namely, DistMult [35], ComplEx [29] and RotatE [27]. We provide the DistMult function below |
| TransE | ✅ oui | = \text{China} \rangle$ and a classic method TransE [2]. TransE maps each entity and relation in |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | C.C.: Replacing paths with connection-biased attention for knowledge graph completion. In: Proceedi |
| GAN | , we adopt a generative adversarial network (GAN) [30] for the generation of negative samples |
| HypER | t to the generator $\epsilon$, $\sigma$ is a hyper-parameter controlling the covariance of the |
| MLP | is implemented as a multi-layer perceptron (MLP). Taking $G_E$ as an example, its MLP is par |
| Random Walk | PinSage [14] generates localized graphs via random walks to extract informative negative samples. How |
| RatE | the model for 5000 epochs, using a learning rate of 0.001 and a mini-batch size of 1000 for U |
| SimplE | triplet by a randomly sampled entity. Beyond simple random sampling, generative adversarial nets |
| StAR | usionopolis Way, Singapore 138632 xlli@i2r.a-star.edu.sg ³ Beijing Normal University, 19 Xinwa |
| Structured Embedding | 38. Zeng, J., Liu, L., Zheng, X.: Learning structured embeddings of knowledge graphs with adversarial learnin |
| Structured Embeddings | 38. Zeng, J., Liu, L., Zheng, X.: Learning structured embeddings of knowledge graphs with adversarial learnin |
| TaKE | tive samples to produce negative samples, we take one step further to consider the diversity a |
