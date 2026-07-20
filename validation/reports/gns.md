# Validation — GNS.md

**Titre extrait :** Good negative sampling for triple classification

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 15 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **93.8%** |
| Candidats faux negatifs (dans le texte, non extraits) | 17 |
| **Recall relatif (indicatif, a valider)** | **46.9%** |

## Datasets  —  precision 0% · recall~ 0%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB13 (FB13_reduced) | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | al transformers for language understanding. *arXiv preprint arXiv:1810.04805*, 2018. 7. Claudi |
| FB13 | lassification task - on a benchmark dataset -FB13. As result, we demonstrate that Good Negativ |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | for KG-BERT model training would improve the accuracy in the triple classification task. Avoiding |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 100% · recall~ 43%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Bernoulli Negative Sampling | ✅ oui | hods: 1) Uniform Negative Sampling (UNS), 2) Bernoulli Negative Sampling (BNS) and 3) Pseudo Typed Negative Sampling |
| Good Negative Sampling | ✅ oui | # Good negative sampling for triple classification Yoan A. López-Rod |
| Iterative Negative Sampling | ✅ oui | l entity to corrupt. ReasonKGE [9] with its Iterative Negative Sampling (INS) identifies dynamically via symbolic re |
| Pseudo Typed Negative Sampling | ✅ oui | 2) Bernoulli Negative Sampling (BNS) and 3) Pseudo Typed Negative Sampling (PTNS). UNS generates corrupted triples from |
| Typed Negative Sampling | ✅ oui | ion of ontologies in the negative sampling. Typed Negative Sampling (TNS) [10] which is similar to GNS is focuse |
| Uniform Negative Sampling | ✅ oui | ve sampling is composed of three methods: 1) Uniform Negative Sampling (UNS), 2) Bernoulli Negative Sampling (BNS) |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Bernoulli Sampling | hods: 1) Uniform Negative Sampling (UNS), 2) Bernoulli Negative Sampling (BNS) and 3) Pseudo Typed Negative Sampling |
| Corrupting Positive Instances | ed false. It generates negative instances by corrupting positive instances: for every relation r, they collect the sets |
| Local Closed-World Assumption | m> are inconsistent triples. In addition, a Local-Closed World Assumption (LCWA) approach [10] assumes a KG to be only |
| Negative Sampling | # Good negative sampling for triple classification Yoan A. López-Rod |
| ReasonKGE | ity to pick head or tail entity to corrupt. ReasonKGE [9] with its Iterative Negative Sampling (IN |
| Typed Sampling | ion of ontologies in the negative sampling. Typed Negative Sampling (TNS) [10] which is similar to GNS is focuse |
| Uniform Sampling | ve sampling is composed of three methods: 1) Uniform Negative Sampling (UNS), 2) Bernoulli Negative Sampling (BNS) |
| Unknown | re triples that belong to $G\complement$ are unknown, $G\complement$ is composed of three kinds o |

## KGE Models  —  precision 100% · recall~ 53%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| BERT | ✅ oui | on a state-of-the-art embedding method - KG-BERT for triple classification task - on a benchm |
| ComplEx | ✅ oui | ngs in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BERT [21], and al |
| DistMult | ✅ oui | h as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BERT [21], and all these methods |
| KG-BERT | ✅ oui | egy on a state-of-the-art embedding method - KG-BERT for triple classification task - on a benchm |
| ReasonKGE | ✅ oui | ity to pick head or tail entity to corrupt. ReasonKGE [9] with its Iterative Negative Sampling (IN |
| Rescal | ✅ oui | ation embeddings in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20] and KG-BER |
| TransE | ✅ oui | tity and relation embeddings in KGs such as: TransE [5], Rescal [12], ComplEx [16], DistMult [20 |
| TransOWL | ✅ oui | gative sampling for triple classification 5 TransOWL [7] leverages ontology axioms in order to in |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ined BERT-Base model with 12 layers, 12 self-attention heads and hidden state size H =768. KG-BERT |
| LINE | ities randomly. Hence, this work goes on the line of analyzing the impact of negative triple s |
| Neural Tensor Network | her D Manning, and Andrew Ng. Reasoning with neural tensor networks for knowledge base completion. *Advances in |
| Neural Tensor Networks | her D Manning, and Andrew Ng. Reasoning with neural tensor networks for knowledge base completion. *Advances in |
| RatE | ng hyperparameters: batch size: 32, learning rate: $5e^{-5}$ with Adam optimizer implemented i |
| SimplE | cluding triple classification [21]. Making a simple revision of KG-BERT negative sampling, accor |
| TaKE | asing the number of false negatives since it takes into consideration the relation cardinality; |
