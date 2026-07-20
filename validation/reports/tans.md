# Validation — TANS.md

**Titre extrait :** Unified Interpretation of Smoothing Methods for Negative Sampling Loss Functions in Knowledge Graph Embedding

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 27 |
| Extraites NON trouvees (FP -> erreur precision) | 11 |
| **Precision** | **71.1%** |
| Candidats faux negatifs (dans le texte, non extraits) | 13 |
| **Recall relatif (indicatif, a valider)** | **67.5%** |

## Datasets  —  precision 100% · recall~ 75%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k-237 | ✅ oui | istMult, ComplEx, RotatE, HAKE, and HousE on FB15k-237, WN18RR, and YAGO3-10 datasets and their spa |
| FB15k-237-HL | ✅ oui | r> </thead> <tbody> <tr> <td>FB15k-237-HL</td> <td>38.5</td> <td>39.2< |
| WN18RR | ✅ oui | mplEx, RotatE, HAKE, and HousE on FB15k-237, WN18RR, and YAGO3-10 datasets and their sparser sub |
| WN18RR-HL | ✅ oui | <td>43.2</td> </tr> <tr> <td>WN18RR-HL</td> <td>11.0</td> <td>11.5< |
| YAGO3-10 | ✅ oui | E, HAKE, and HousE on FB15k-237, WN18RR, and YAGO3-10 datasets and their sparser subsets show the |
| YAGO3-10-HL | ✅ oui | <td>14.2</td> </tr> <tr> <td>YAGO3-10-HL</td> <td>42.0</td> <td>43.0< |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:2407.04251v1 [cs.CL] 5 Jul 2024 # Unified I |
| FB15k | istMult, ComplEx, RotatE, HAKE, and HousE on FB15k-237, WN18RR, and YAGO3-10 datasets and their |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | oyed conventional metrics in KGC, i.e., MRR, Hits@1 (H@1), Hits@3 (H@3), and Hits@10 (H@10) and |
| Hits@10 | ✅ oui | , i.e., MRR, Hits@1 (H@1), Hits@3 (H@3), and Hits@10 (H@10) and reported the average scores and t |
| Hits@3 | ✅ oui | nal metrics in KGC, i.e., MRR, Hits@1 (H@1), Hits@3 (H@3), and Hits@10 (H@10) and reported the a |
| MRR | ✅ oui | <tr> <th colspan="7">FB15k-237 (MRR)</th> </tr> </thead> <tbody> <tr |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 27% · recall~ 36%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Base subsampling | ❌ NON | _(absent du texte)_ |
| Frequency-based subsampling | ✅ oui | bsampling of Sun et al. (2019) (Base), their frequency-based subsampling (Freq) and unique-based subsampling (Uniq) f |
| Self-Adversarial Negative Sampling | ✅ oui | loss in KGE relies on smoothing methods like Self-Adversarial Negative Sampling (SANS) and subsampling. However, it is uncer |
| Self-Adversarial Negative Sampling w/ Base | ❌ NON | _(absent du texte)_ |
| Self-Adversarial Negative Sampling w/ Freq | ❌ NON | _(absent du texte)_ |
| Self-Adversarial Negative Sampling w/ Uniq | ❌ NON | _(absent du texte)_ |
| Triplet Adaptive Negative Sampling | ✅ oui | he NS loss in KGE and induces a new NS loss, Triplet Adaptive Negative Sampling (TANS), that can cover the characteristics o |
| Triplet Adaptive Negative Sampling w/ Base | ❌ NON | _(absent du texte)_ |
| Triplet Adaptive Negative Sampling w/ Freq | ❌ NON | _(absent du texte)_ |
| Triplet Adaptive Negative Sampling w/ Uniq | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling w/ Base | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling w/ Freq | ❌ NON | _(absent du texte)_ |
| Uniform Negative Sampling w/ Uniq | ❌ NON | _(absent du texte)_ |
| Unique-based subsampling | ✅ oui | their frequency-based subsampling (Freq) and unique-based subsampling (Uniq) for KGE. Kamigaito and Hayashi (2021) |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Adaptive Negative Sampling | ss in KGE and induces a new NS loss, Triplet Adaptive Negative Sampling (TANS), that can cover the characteristics o |
| Adversarial Negative Sampling | in KGE relies on smoothing methods like Self-Adversarial Negative Sampling (SANS) and subsampling. However, it is uncer |
| Negative Sampling | fied Interpretation of Smoothing Methods for Negative Sampling Loss Functions in Knowledge Graph Embedding |
| SANS | ods like Self-Adversarial Negative Sampling (SANS) and subsampling. However, it is uncertain w |
| Self-adversarial Sampling | loss in KGE relies on smoothing methods like Self-Adversarial Negative Sampling (SANS) and subsampling. However, it is uncer |
| Structure-Aware Negative Sampling | am L. Hamilton, and Avishek Joey Bose. 2020. Structure aware negative sampling in knowledge graphs. In *Proceedings of the |
| Subsampling | elf-Adversarial Negative Sampling (SANS) and subsampling. However, it is uncertain what kind of smoot |

## KGE Models  —  precision 100% · recall~ 76%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| BERT | ✅ oui | ddings, Clark et al. (2020a) indicate that a BERT (Devlin et al., 2019)-like model ELECTRA (Cl |
| ComplEx | ✅ oui | s. Experimental results of TransE, DistMult, ComplEx, RotatE, HAKE, and HousE on FB15k-237, WN18R |
| DistMult | ✅ oui | ing methods. Experimental results of TransE, DistMult, ComplEx, RotatE, HAKE, and HousE on FB15k-2 |
| ELECTRA | ✅ oui | that a BERT (Devlin et al., 2019)-like model ELECTRA (Clark et al., 2020b) uses the NS loss to pe |
| GenKGC | ✅ oui | methods like KGT5 (Saxena et al., 2022) and GenKGC (Xie et al., 2022) are unique in directly ge |
| HAKE | ✅ oui | esults of TransE, DistMult, ComplEx, RotatE, HAKE, and HousE on FB15k-237, WN18RR, and YAGO3-1 |
| HousE | ✅ oui | TransE, DistMult, ComplEx, RotatE, HAKE, and HousE on FB15k-237, WN18RR, and YAGO3-10 datasets |
| KEPLER | ✅ oui | d language model (PLM)-based approaches like KEPLER (Wang et al., 2021) and SimKGC (Wang et al., |
| KGT5 | ✅ oui | -training. Generation-based KGC methods like KGT5 (Saxena et al., 2022) and GenKGC (Xie et al. |
| RotatE | ✅ oui | mental results of TransE, DistMult, ComplEx, RotatE, HAKE, and HousE on FB15k-237, WN18RR, and Y |
| SimKGC | ✅ oui | proaches like KEPLER (Wang et al., 2021) and SimKGC (Wang et al., 2022) also have an important r |
| TransE | ✅ oui | l smoothing methods. Experimental results of TransE, DistMult, ComplEx, RotatE, HAKE, and HousE |
| word2vec | ✅ oui | E. Sun et al. (2019) import subsampling from word2vec (Mikolov et al., 2013) to KGE. Subsampling c |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | G: Explainable conversational reasoning with attention-based walks over knowledge graphs. In *Proce |
| SimplE | $p_d(y\|x)$ and $p_d(x)$. First, we assume a simple replacement from $p_\theta(y\|x)$ to $p_\thet |
| Structured Embedding | Collobert, and Yoshua Bengio. 2011. Learning structured embeddings of knowledge bases. In *Proceedings of the A |
| Structured Embeddings | Collobert, and Yoshua Bengio. 2011. Learning structured embeddings of knowledge bases. In *Proceedings of the A |
