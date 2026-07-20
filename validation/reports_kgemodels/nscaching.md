# KGE Models — NSCaching.md

**Titre :** NSCaching: Simple and Efficient Negative Sampling for Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 7 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 83% |
| Recall relatif *mentionnes* | 88% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | op$</td> </tr> <tr> <td>ComplEx [38]</td> <td>$\text{Re}(\mathb |
| DistMult | ✅ oui | ="2">semantic matching</td> <td>DistMult [46]</td> <td>$\mathbf{h} \cdot |
| TransD | ✅ oui | _1$</td> </tr> <tr> <td>TransD [20]</td> <td>$\\|\mathbf{h} + \ |
| TransE | ✅ oui | translational distance</td> <td>TransE [7]</td> <td>$\\|\mathbf{h} + \m |
| TransH | ✅ oui | _1$</td> </tr> <tr> <td>TransH [42]</td> <td>$\\|\mathbf{h} - \ |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| ANALOGY | ✅ oui | DistMult [46], HolE [31], ComplEx [38], ANALOGY [27], etc. All these methods are summar |
| HolE | ✅ oui | e variants of RESCAL are DistMult [46], HolE [31] and ComplEx [38]. DistMult simplif |
| ManifoldE | ✅ oui | nsD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and semantic matching model |
| RESCAL | ✅ oui | e plausibility of triplets $(h, r, t)$. RESCAL [32] is the most original model. The en |
| TransM | ✅ oui | nsR [26], TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc., and semanti |
| TranSparse | ✅ oui | TransH [42], TransR [26], TransD [20], TranSparse [21], TransM [11], ManifoldE [45], etc. |
| TransR | ✅ oui | his problem, variants like TransH [42], TransR [26], TransD [20] are introduced to pro |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| KBGAN | prose+table | wo pioneered works, i.e., IGAN [39] and KBGAN [9], attempting to address these challe |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| LINE | prose | EGATIVE ENTITIES IN CACHE ON FB13. EACH LINE DISPLAYS 5 RANDOM SAMPLED NEGATIVE ENTI |