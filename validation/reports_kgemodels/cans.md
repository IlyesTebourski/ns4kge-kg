# KGE Models — CANS.md

**Titre :** Confidence-Aware Negative Sampling Method for Noisy Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 2 |
| Modeles MENTIONNES seulement (hors tableaux) | 6 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 1 |
| Recall BRUT evalues / mentionnes | 100% / 86% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| CKRL | ✅ oui | 9.9</td> </tr> <tr> <td>CKRL(LT)</td> <td>230</td> < |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>249</td> <td>1 |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| GTrans | ✅ oui | iple as a manifold rather than a point. GTrans [20] used dynamic and static weighting |
| ManifoldE | ✅ oui | ctors of entities into various spaces. ManifoldE [19] embedded a triple as a manifold ra |
| puTransE | ✅ oui | d the noise from other relation spaces. puTransE [21] generated multiple embedding space |
| TransD | ✅ oui | ame vector space. Then TransR [17], and TransD [18], extended TransE, by projecting th |
| TransH | ✅ oui | th 1-to-N, N-to-1, or N-to-N relations. TransH [10] proposed to project the entity to |
| TransR | ✅ oui | ons were in the same vector space. Then TransR [17], and TransD [18], extended TransE, |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | , and has therefore quickly gained much attention. However, most conventional embedding m |