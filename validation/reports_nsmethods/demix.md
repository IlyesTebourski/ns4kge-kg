# NS Methods — DeMix.md

**Titre :** Negative Sampling with Adaptive Denoising Mixup for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 8 |
| Methodes MENTIONNEES seulement (prose) | 3 |
| Precision evalues | 100% | 
| Precision mentionnes | 100% |
| Recall evalues | 73% |
| Recall mentionnes | 60% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Adaptive Denoising Mixup | ✅ | name | ] 15 Oct 2023 # Negative Sampling with Adaptive Denoising Mixup for Knowledge Graph Embedding Xiangnan |
| Bernoulli Sampling | ✅ | name | riples from a uniform distribution. - *Bernoulli Sampling* [24]. which sample negative t |
| CANS | ✅ | name | d by utilizing the graph structure. - *CANS* [16]. The CANS is a component of CAKE |
| ESNS | ✅ | name | ainly compare CANS instead of CAKE. - *ESNS* [29]. It takes semantic similarities a |
| NSCaching | ✅ | name | negative triples with high scores, and NSCaching[31] introduces a caching mechanism to s |
| RW-SANS | ✅ | name | ing to the current embedding model. - *RW-SANS* [1]. It samples negative triples from |
| Self-adversarial Sampling | ✅ | name | .s. Epoch based on RotatE. Normal means self-adversarial negative sampling. Leakage means ensuri |
| Uniform Sampling | ✅ | name | hbf{e}_j, y_j) \sim \begin{cases} \text{Uniform } (\mathcal{T}_{cap}) & \text{if } (\ma |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| IGAN | ✅ | name | high scores. For example, KBGAN[6] and IGAN[23] introduce a generative adversarial |
| KBGAN | ✅ | name | triples with high scores. For example, KBGAN[6] and IGAN[23] introduce a generative |
| MixKG | ✅ | name | harder negative triples for KGE such as MixKG [8]. Different from existing methods, D |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| SANS | prose+table | name | to the current embedding model. - *RW-SANS* [1]. It samples negative triples from |
| Self-Adv | table | name | > </tr> <tr> <td>TransE+Self-Adv</td> <td>0.215<sup>Δ</sup></td> |
| Commonsense-Aware Negative Sampling | prose+table | acro | d by utilizing the graph structure. - *CANS* [16]. The CANS is a component of CAKE |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| CAKE | prose | name | *CANS* [16]. The CANS is a component of CAKE [16] responsible for solving the invali |
| MixGCF | prose | name | eneralization and robustness of models. MixGCF [13] integrates multiple negative sampl |