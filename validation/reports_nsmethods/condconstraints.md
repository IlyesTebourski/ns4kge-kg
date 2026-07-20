# NS Methods — CondConstraints.md

**Titre :** Conditional Constraints for Knowledge Graph Embeddings

| Metrique | Valeur |
|---|---|
| Methodes EVALUEES (tableaux) | 3 |
| Methodes MENTIONNEES seulement (prose) | 4 |
| Precision evalues | 100% | 
| Precision mentionnes | 75% |
| Recall evalues | 100% |
| Recall mentionnes | 100% |

## A. Methodes EVALUEES (valides vs `tables_only`)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| closed world constraints, neg_ratio=1 | ✅ | name | N/A</td> </tr> <tr> <td>closed world constraints</td> <td>1</td> <td>801 |
| no constraints, neg_ratio=1 | ✅ | name | </thead> <tbody> <tr> <td>no constraints</td> <td>1</td> <td>667 |
| open world constraints, neg_ratio=1 | ✅ | name | 647</td> </tr> <tr> <td>open world constraints</td> <td>1</td> <td>663 |

## B. Methodes MENTIONNEES seulement (valides vs prose)

| Methode | Trouvee ? | Via | Extrait |
|---|:---:|:---:|---|
| Bernoulli Negative Sampling | ✅ | name | for TransH and is sometimes called the Bernoulli trick [15]. The Bernoulli trick involve |
| Conditional Constraint-Based Negative Sampling | ❌ |  | _(absent)_ |
| Filtered Negative Sampling | ✅ | name | ransE embedding model: using so-called *filtered* negative samples [1]. Filtered negativ |
| Locally Closed World Negative Sampling | ✅ | name | ail with another entity) or to assume a locally closed world in which any valid triple entails a who |

## C1. Recall EVALUES — dans un tableau mais non extrait

_Aucun._

## C2. Recall MENTIONNES — en prose seulement mais non extrait

_Aucun._