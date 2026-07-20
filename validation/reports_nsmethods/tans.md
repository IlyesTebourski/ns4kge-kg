# NS Methods — TANS.md

**Titre :** Unified Interpretation of Smoothing Methods for Negative Sampling Loss Functions in Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 12 |
| Methodes MENTIONNEES seulement (prose) | 3 |
| Precision evalues | 25% | 
| Precision mentionnes | 67% |
| Recall evalues | 43% |
| Recall mentionnes | 100% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Self-Adversarial Negative Sampling | ✅ | name | in KGE relies on smoothing methods like Self-Adversarial Negative Sampling (SANS) and subsamplin |
| Self-Adversarial Negative Sampling w/ Base | ❌ |  | _(absent)_ |
| Self-Adversarial Negative Sampling w/ Freq | ❌ |  | _(absent)_ |
| Self-Adversarial Negative Sampling w/ Uniq | ❌ |  | _(absent)_ |
| Triplet Adaptive Negative Sampling | ✅ | name | loss in KGE and induces a new NS loss, Triplet Adaptive Negative Sampling (TANS), that can cove |
| Triplet Adaptive Negative Sampling w/ Base | ❌ |  | _(absent)_ |
| Triplet Adaptive Negative Sampling w/ Freq | ❌ |  | _(absent)_ |
| Triplet Adaptive Negative Sampling w/ Uniq | ❌ |  | _(absent)_ |
| Uniform Negative Sampling | ✅ | name | om word embedding to KGE with utilizing uniform distribution as its noise distribution. |
| Uniform Negative Sampling w/ Base | ❌ |  | _(absent)_ |
| Uniform Negative Sampling w/ Freq | ❌ |  | _(absent)_ |
| Uniform Negative Sampling w/ Uniq | ❌ |  | _(absent)_ |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Base subsampling | ❌ |  | _(absent)_ |
| Frequency-based subsampling | ✅ | name | ling of Sun et al. (2019) (Base), their frequency-based subsampling (Freq) and unique-based subsampling (Un |
| Unique-based subsampling | ✅ | name | frequency-based subsampling (Freq) and unique-based subsampling (Uniq) for KGE. Kamigaito and Hayashi ( |

## C1. Recall EVALUES — dans un tableau mais non extrait

| Methode | Ou | Via | Extrait |
|---|---|:---:|---|
| Frequency-based Negative Sampling | table | name | <th>Index</th> <th>Query Frequency</th> <th>Answer Frequency</th> |
| None Sampling | table | name | 2">ComplEx</td> <td rowspan="3">None</td> <td>NS</td> <td>23 |
| SANS | prose+table | name | ike Self-Adversarial Negative Sampling (SANS) and subsampling. However, it is uncert |
| Subsampling | prose+table | name | word2vec (Mikolov et al., 2013) to KGE. Subsampling can smooth the appearance frequency of |

## C2. Recall MENTIONNES — en prose seulement mais non extrait

_Aucun._