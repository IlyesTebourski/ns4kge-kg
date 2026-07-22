# NS Methods — LAS.md

**Titre :** Adversarial Knowledge Representation Learning without External Model

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 3 |
| Methodes MENTIONNEES seulement (prose) | 6 |
| Precision evalues | 100% | 
| Precision mentionnes | 83% |
| Recall evalues | 100% |
| Recall mentionnes | 100% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| KBGAN | ✅ | name | h outperforms GAN-based sampling method KBGAN. **INDEX TERMS** Knowledge graph, know |
| Loss Adaptive Sampling | ✅ | name | nowledge representation learning, named loss adaptive sampling (LAS) mechanism, which is effi |
| Uniform Random Negative Sampling | ✅ | name | ses in training FB15k237 by TransE with uniform random negative triplets selection. To allevi |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Bernoulli Negative Sampling | ✅ | name | f $((h, r, t), (h'_s, r, t'_s))$ with a Bernoulli distribution $B(1, p_{up})$. We conside |
| Domain Sampling | ✅ | name | e, corrupted triplets which violate the domain/range restriction of its relation is de |
| GAN-pretrain | ✅ | name | plets. Generative adversarial networks (GANs) inspired approaches are proposed to re |
| Near-miss Sampling | ✅ | name | iminator, and it can be regarded as the near miss sampling in [26]. In this part of exper |
| Nearest-neighbour Sampling | ✅ | name | ], the static negative sampling models, nearest-neighbour sampling and near-miss sampling, are pr |
| Type-constrained Negative Sampling | ❌ |  | _(absent)_ |

## C1. Recall EVALUES — dans un tableau mais non extrait

_Aucun._

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Adaptive Negative Sampling | prose | name | e but strong method, including the loss adaptive negative sampling approach and the push-up mechanism in S |
| Adversarial Negative Sampling | prose | name | this paper, LAS is a simple but strong adversarial negative sampling approach without an external sampling m |
| Random Negative Sampling | prose | name | n, as is illustrated in Figure 1. Thus, random negative sampling would cause very slow convergence and e |
| Static Sampling | prose | name | get competitive results. In [26], the static negative sampling models, nearest-neighbour sampling and |