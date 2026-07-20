# NS Methods — dans.md

**Titre :** Diversified and Adaptive Negative Sampling on Knowledge Graphs

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 10 |
| Methodes MENTIONNEES seulement (prose) | 3 |
| Precision evalues | 90% | 
| Precision mentionnes | 100% |
| Recall evalues | 90% |
| Recall mentionnes | 75% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| CAKE | ✅ | name | nerate informative negative triplets; **CAKE** [19]: a framework which leverages ext |
| Diversified and Adaptive Negative Sampling | ✅ | name | Xiv:2410.07592v2 [cs.AI] 26 Oct 2025 # Diversified and Adaptive Negative Sampling on Knowledge Graphs |
| KBGAN | ✅ | name | ous state-of-the-art approaches such as KBGAN [3], we adopt a generative adversarial |
| Markov Chain Monte Carlo Negative Sampling | ❌ |  | _(absent)_ |
| NSCaching | ✅ | name | nodes via random walks on the graph; **NSCaching** [39]: a model that employs importance |
| Popularity-weighted Negative Sampling | ✅ | name | edge graph sampled in a uniform [33] or popularity-weighted manner [17]. Although random sampling i |
| Random Negative Sampling | ✅ | name | ive triplets are often obtained through random sampling. More recent works [34, 3] exp |
| Self-adversarial Negative Sampling | ✅ | name | weighted sampling; **Self-adv** [28]: a self-adversarial negative sampling methodology; **MCNS** |
| SMiLE | ✅ | name | triplets to sample negative triplets; **SMiLE** [22]: a framework which employs speci |
| Structure-Aware Negative Sampling | ✅ | name | rent heuristics or learning strategies. Structure-aware models [1, 37] exploit the graph struct |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| GNDN | ✅ | name | as KBGAN [3], IGAN [30], HeGAN [11] and GNDN [38], which learn the underlying sample |
| HeGAN | ✅ | name | GAN) [10] such as KBGAN [3], IGAN [30], HeGAN [11] and GNDN [38], which learn the und |
| IGAN | ✅ | name | rial nets (GAN) [10] such as KBGAN [3], IGAN [30], HeGAN [11] and GNDN [38], which l |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| SANS | prose+table | name | hood of positive examples. For example, SANS [1] hypothesizes that entities that are |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Self-Adv | prose | name | d other negative samplers (Random, Pop, Self-Adv and MCNS) employ RGCN [26] as the backb |