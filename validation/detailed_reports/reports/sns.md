# Validation — SNS.md

**Titre extrait :** Simple negative sampling for link prediction in knowledge graphs

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 19 |
| Extraites NON trouvees (FP -> erreur precision) | 0 |
| **Precision** | **100.0%** |
| Candidats faux negatifs (dans le texte, non extraits) | 15 |
| **Recall relatif (indicatif, a valider)** | **55.9%** |

## Datasets  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15K | ✅ oui | nown knowledge graph datasets, WN18, WN18RR, FB15K, FB15K-237, YAGO3-10. The method is also eva |
| FB15K-237 | ✅ oui | owledge graph datasets, WN18, WN18RR, FB15K, FB15K-237, YAGO3-10. The method is also evaluated on a |
| FIGHT-HF-23R | ✅ oui | so evaluated on a new biological KG dataset (FIGHT-HF-23R). Experimental results show that the SNS imp |
| WN18 | ✅ oui | on five well-known knowledge graph datasets, WN18, WN18RR, FB15K, FB15K-237, YAGO3-10. The met |
| WN18RR | ✅ oui | e well-known knowledge graph datasets, WN18, WN18RR, FB15K, FB15K-237, YAGO3-10. The method is a |
| YAGO3-10 | ✅ oui | ph datasets, WN18, WN18RR, FB15K, FB15K-237, YAGO3-10. The method is also evaluated on a new biolo |

_Aucun candidat faux negatif pour cette categorie._

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | t@10</th> <th>hit@3</th> <th>hit@1</th> <th>MRR</th> <th>hit@10 |
| Hits@10 | ✅ oui | ling methods are used in DistMult model, the hit@10 and hit@3 scores drop in all datasets except |
| Hits@3 | ✅ oui | s are used in DistMult model, the hit@10 and hit@3 scores drop in all datasets except FIGHT-HF- |
| MRR | ✅ oui | ed metrics: Hit@z, and mean reciprocal rank (MRR) [14]. The metrics are defined based on the |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 100% · recall~ 41%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| IGAN | ✅ oui | minator part is trained to learn embeddings. IGAN [8], KBGAN [3], KSGAN [7] are three existing |
| KBGAN | ✅ oui | rt is trained to learn embeddings. IGAN [8], KBGAN [3], KSGAN [7] are three existing GAN-based |
| KSGAN | ✅ oui | ed to learn embeddings. IGAN [8], KBGAN [3], KSGAN [7] are three existing GAN-based sampling me |
| NSCaching | ✅ oui | nerative adversarial network(GAN)-based, and NSCaching, structure aware negative sampling(SANS) are |
| Simple Negative Sampling | ✅ oui | open science logo](page_1_image_1_v2.jpg) # Simple negative sampling for link prediction in knowledge graphs Md |
| Structure Aware Negative Sampling | ✅ oui | versarial network(GAN)-based, and NSCaching, structure aware negative sampling(SANS) are four negative sampling methods in |
| Uniform Random Negative Sampling | ✅ oui | avoiding the 'vanishing-gradient' problem of uniform-random sampling, the complex parameter optimization problem |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | iform-random, generative adversarial network(GAN)-based, and NSCaching, structure aware negat |
| GAN-based Negative Sampling | [8], KBGAN [3], KSGAN [7] are three existing GAN-based sampling methods for KGs. Compared to 'uniform-random |
| Good Negative Sampling | s and the current state-of-art still lacks a good negative sampling method. In this article, we propose a simple |
| Knowledge Selective Adversarial Network | 1-9 (2013). 7. Hu, K., Liu, H., Hao, T.: A knowledge selective adversarial network for link prediction in knowledge graph. In: |
| Negative Sampling | ience logo](page_1_image_1_v2.jpg) # Simple negative sampling for link prediction in knowledge graphs Md |
| NSCaching Sampling | les negatives directly from the caches. With NSCaching sampling, KG embedding models show competitive link p |
| Random Negative Sampling | the 'vanishing-gradient' problem of uniform-random sampling, the complex parameter optimization problem |
| Random Sampling | the 'vanishing-gradient' problem of uniform-random sampling, the complex parameter optimization problem |
| SANS | NSCaching, structure aware negative sampling(SANS) are four negative sampling methods in the l |
| Uniform Random Sampling | avoiding the 'vanishing-gradient' problem of uniform-random sampling, the complex parameter optimization problem |

## KGE Models  —  precision 100% · recall~ 29%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DistMult | ✅ oui | e TransH [11] to represent translational and DistMult [12] to represent semantic matching model as |
| TransH | ✅ oui | sampling for KGs. For evaluation, we choose TransH [11] to represent translational and DistMult |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| ComplEx | graphs. The 10th International Conference on Complex Networks and their Applications, Nov 2021, M |
| GAN | iform-random, generative adversarial network(GAN)-based, and NSCaching, structure aware negat |
| RatE | to 200, embedding dimension to 100, learning rate to 0.0001, margin value to 4.0 for all the e |
| SimplE | open science logo](page_1_image_1_v2.jpg) # Simple negative sampling for link prediction in kno |
| TaKE | increase the number of model parameters and take extra costs on training for parameter optimi |
