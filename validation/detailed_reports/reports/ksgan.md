# Validation — KSGAN.md

**Titre extrait :** A Knowledge Selective Adversarial Network for Link Prediction in Knowledge Graph

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 23 |
| Extraites NON trouvees (FP -> erreur precision) | 5 |
| **Precision** | **82.1%** |
| Candidats faux negatifs (dans le texte, non extraits) | 11 |
| **Recall relatif (indicatif, a valider)** | **67.6%** |

## Datasets  —  precision 100% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | hree standard knowledge completion datasets: FB15k-237, WN18 and WN18RR. The results show that KSGA |
| WN18 | ✅ oui | rd knowledge completion datasets: FB15k-237, WN18 and WN18RR. The results show that KSGAN outp |
| WN18RR | ✅ oui | dge completion datasets: FB15k-237, WN18 and WN18RR. The results show that KSGAN outperforms a l |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Actor | ance, a true fact (*Jackie Chan, profession, actor*) may turn into a negative example (*Jackie |
| Arxiv | r learning and inference in knowledge bases. arXiv preprint arXiv:1412.6575 (2014) 9. Trouillo |
| FB15k | hree standard knowledge completion datasets: FB15k-237, WN18 and WN18RR. The results show that |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@10 | ✅ oui | ieves improvement (7.0% for MRR and 1.4% for Hits@10) on average. In summary, the major contribu |
| MRR | ✅ oui | baselines and achieves improvement (7.0% for MRR and 1.4% for Hits@10) on average. In summar |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | uch as TransR, the projection matrix used to map entities from entity space to relation space |

## NS Methods  —  precision 38% · recall~ 50%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ❌ NON | _(absent du texte)_ |
| IGAN | ✅ oui | nk prediction task. In contrast to KBGAN and IGAN [11], KSGAN leverages a knowledge selector a |
| KBGAN | ✅ oui | nspired by an adversarial learning framework KBGAN, this paper proposes a new knowledge selecti |
| Knowledge Selective Adversarial Network | ✅ oui | # A Knowledge Selective Adversarial Network for Link Prediction in Knowledge Graph Kair |
| KSGAN(ComplEx+TransD) | ❌ NON | _(absent du texte)_ |
| KSGAN(ComplEx+TransE) | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | DistMult [8], ComplEx [9]) as a generator in GAN and translational distance models (e.g., Tra |
| KSGAN | edge selective adversarial network, named as KSGAN, using a knowledge selector for high-quality |
| Negative Sampling | h topic. During KG embedding model training, negative sampling is a fundamental method for obtaining negati |

## KGE Models  —  precision 100% · recall~ 79%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | (e.g., TransE [6], TransD [7], DistMult [8], ComplEx [9]). However, previous works such as Trans |
| DistMult | ✅ oui | bedding model (e.g., TransE [6], TransD [7], DistMult [8], ComplEx [9]). However, previous works |
| GTrans | ✅ oui | *r** (or **t** − **r**). As a generic model, GTrans [17] introduces eigenstate and mimesis to re |
| ManifoldE | ✅ oui | g strict magnitude constraints between them. ManifoldE [16] uses a manifold function to constrain * |
| MLP | ✅ oui | emantic matching models such as NTN [21] and MLP [22], focus on neural network architectures |
| NTN | ✅ oui | ckER. Other semantic matching models such as NTN [21] and MLP [22], focus on neural network a |
| RESCAL | ✅ oui | erent from the translational distance model, RESCAL [18] is a classic semantic matching model, w |
| SimplE | ✅ oui | to a complex space rather than a real space. SimplE [19] simplifies ComplEx by considering a dif |
| TransD | ✅ oui | dge graph embedding model (e.g., TransE [6], TransD [7], DistMult [8], ComplEx [9]). However, p |
| TransE | ✅ oui | ing a knowledge graph embedding model (e.g., TransE [6], TransD [7], DistMult [8], ComplEx [9]). |
| TransF | ✅ oui | elations. Targeting at more flexible models, TransF [15] ensures that **t** (or **h**) has the s |
| TransH | ✅ oui | e fact $(h, r, t)$. Various variants such as TransH [12], TransM [13], TransR [14] and TransD [7 |
| TransM | ✅ oui | , t)$. Various variants such as TransH [12], TransM [13], TransR [14] and TransD [7] have been d |
| TransR | ✅ oui | s variants such as TransH [12], TransM [13], TransR [14] and TransD [7] have been developed in r |
| TuckER | ✅ oui | ing a different similarity scoring function. TuckER [20] is based on Tucker decomposition and th |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | DistMult [8], ComplEx [9]) as a generator in GAN and translational distance models (e.g., Tra |
| Neural Tensor Network | n, D., Manning, C.D., Ng, A.: Reasoning with neural tensor networks for knowledge base completion. NIPS. pp. 926 |
| Neural Tensor Networks | n, D., Manning, C.D., Ng, A.: Reasoning with neural tensor networks for knowledge base completion. NIPS. pp. 926 |
| TaKE | es from hidden layer of neural network which takes the vectors of entities and relations as inp |
