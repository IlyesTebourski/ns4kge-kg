# KGE Models — TruncatedNS.md

**Titre :** Fusing Attribute Character Embeddings with Truncated Negative Sampling for Entity Alignment

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 14 |
| **Precision globale** | **95%** |
| Precision (evalues, vs tableaux) | 80% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 1 |
| Recall BRUT evalues / mentionnes | 100% / 93% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| IPTransE | ✅ oui | 258</td> </tr> <tr> <td>IPTransE</td> <td>32.73</td> <td |
| JAPE | ✅ oui | 412</td> </tr> <tr> <td>JAPE</td> <td>14.45</td> <td |
| MTransE | ✅ oui | 007</td> </tr> <tr> <td>MtransE</td> <td>16.51</td> <td |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>8.35</td> <td> |
| Truncated Negative Sampling | ❌ NON | _(absent des tableaux)_ |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| BootEA | ✅ oui | ame, relationship, and attribute views. BootEA [24] proposes iterative entity alignmen |
| CrossE | ✅ oui | sed in the entity triple, respectively. CrossE [13] believes that bidirectional effect |
| DAT | ✅ oui | y updated using newly aligned entities. DAT [21] encodes both entity names and enti |
| HAKE | ✅ oui | modelled entities in hyperbolic space. HAKE [16] believes that polar coordinates ar |
| KD-CoE | ✅ oui | been abstracted to related data types. KD-CoE [26] jointly learns multi-lingual entit |
| MultiKE | ✅ oui | function of the interaction embeddings. MultiKE [23] uses multiple views of entities to |
| MuRP | ✅ oui | d as rotation changes in complex space. MuRP [15] points out that the relationships |
| RESCAL | ✅ oui | ions to gauge the rationality of facts. RESCAL [11] was the earliest semantic matching |
| RotatE | ✅ oui | ntities and relationships. According to RotatE [14], which can model and infer differe |
| SimplE | ✅ oui | ons between latent factors of entities. SimplE [12] restricts the relationship matrix |
| TransD | ✅ oui | wo different projection matrices by the TransD [17] model, respectively. According to |
| TransEdge | ✅ oui | erforms well in handling tail entities. TransEdge [22] interacts with embeddings between |
| TransH | ✅ oui | n the corresponding relationship space. TransH [19] thinks an entity can have many rep |
| TransR | ✅ oui | [17] model, respectively. According to TransR [18], each entity is made up of several |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| Attention | prose | owledge fusion have received widespread attention. In this article, we suggest a method f |