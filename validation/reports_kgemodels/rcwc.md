# KGE Models — RCWC.md

**Titre :** KGBoost: A Classification-Based Knowledge Base Completion Method with Negative Sampling

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 9 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (bruts) | 0 |
| Candidats mentions ratees (bruts) | 0 |
| Recall BRUT evalues / mentionnes | 100% / 100% |
| Vrais oublis (adjuges) evalues / mentionnes | 0 / 0 |
| Recall ADJUGE *evalues* | 100% |
| Recall ADJUGE *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | 946</td> </tr> <tr> <td>ComplEx [Trouillon et al., 2016]</td> < |
| ConvE | ✅ oui | 947</td> </tr> <tr> <td>ConvE [Dettmers et al., 2018]</td> <t |
| DistMult | ✅ oui | 943</td> </tr> <tr> <td>DistMult [Yang et al., 2014]</td> <td>42 |
| InteractE | ✅ oui | .54</td> </tr> <tr> <td>InteractE [Vashishth et al., 2020]</td> < |
| KGBoost-R | ✅ oui | 951</td> </tr> <tr> <td>KGBoost-R (Ours)</td> <td>16</td> |
| KGBoost-T | ✅ oui | ng></td> </tr> <tr> <td>KGBoost-T (Ours)</td> <td><strong>15</str |
| RotatE | ✅ oui | 956</td> </tr> <tr> <td>RotatE [Sun et al., 2019]</td> <td>40< |
| SACN | ✅ oui | ng></td> </tr> <tr> <td>SACN [Shang et al., 2019]</td> <td>- |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE [Bordes et al., 2013]</td> <td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| RESCAL | ✅ oui | trix $M_r$ is used to model a relation. RESCAL [Nickel et al., 2011] suffers from mode |
| TransH | ✅ oui | $r \approx 0$ for symmetric relations. TransH [Lin et al., 2015] and TransR [Lin et a |
| TransR | ✅ oui | elations. TransH [Lin et al., 2015] and TransR [Lin et al., 2015] model symmetric rela |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._