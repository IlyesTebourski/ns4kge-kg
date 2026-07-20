# NS Methods — M2ixKG.md

**Titre :** MixKG: Mixing for harder negative samples in knowledge graph

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 7 |
| Methodes MENTIONNEES seulement (prose) | 3 |
| Precision evalues | 71% | 
| Precision mentionnes | 100% |
| Recall evalues | 62% |
| Recall mentionnes | 50% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| KBGAN | ✅ | name | tribution. IGAN [Wang et al., 2018] and KBGAN [Cai and Wang, 2018] introduce generati |
| MixKG HNM-CES | ❌ |  | _(absent)_ |
| MixKG HNM-SF | ❌ |  | _(absent)_ |
| NSCaching | ✅ | name | ct high-quality negative samples, while NSCaching [Zhang et al., 2019] utilizes cached-ba |
| RW-SANS | ✅ | name | ples from the $l$-hop neighborhood. * **RW-SANS** [Ahrabian *et al.*, 2020] is similar |
| SANS | ✅ | name | -quality negative samples. Differently, SANS [Ahrabian et al., 2020] absorbs graph s |
| Uniform Negative Sampling | ✅ | name | . Most current KG embedding models use uniform sampling to generate false triplets [Bo |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Bernoulli Negative Sampling | ✅ | name | form sampling [Bordes et al., 2013] and Bernoulli sampling [Wang et al., 2014]. However, |
| IGAN | ✅ | name | samples from a dynamical distribution. IGAN [Wang et al., 2018] and KBGAN [Cai and |
| MixKG | ✅ | name | Xiv:2202.09606v1 [cs.AI] 19 Feb 2022 # MixKG: Mixing for harder negative samples in |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Random Negative Sampling | table | name | h> <th>Uniform</th> <th>Random Mix</th> <th>HNM-SF</th> |
| Uniform RW-SANS | prose+table | name | s of ComplEx for Uniform, Uniform SANS, Uniform RW-SANS are our reproductions using codes in [A |
| Uniform SANS | prose+table | name | and the results of ComplEx for Uniform, Uniform SANS, Uniform RW-SANS are our reproductions |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Entity Similarity-based Negative Sampling | prose | name | nition of hard negative samples Correct Entity Similarity based Hard Negative Samples (HNS-CES). |
| MixGCF | prose | name | use mixing for harder negative mining. MixGCF [Huang et al., 2021] uses positive mixi |
| Self-adversarial Negative Sampling | prose | acro | -quality negative samples. Differently, SANS [Ahrabian et al., 2020] absorbs graph s |