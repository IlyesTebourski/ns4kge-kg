# KGE Models — GibbsNS.md

**Titre :** Link Prediction Based on Data Augmentation and Metric Learning Knowledge Graph Embedding

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 12 |
| Modeles MENTIONNES seulement (hors tableaux) | 3 |
| **Precision globale** | **93%** |
| Precision (evalues, vs tableaux) | 92% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 1 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 75% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ComplEx | ✅ oui | 533</td> </tr> <tr> <td>ComplEx</td> <td>0.323</td> <td |
| ConvE | ✅ oui | 526</td> </tr> <tr> <td>ConvE</td> <td>0.325</td> <td |
| DistMult | ✅ oui | d>-</td> </tr> <tr> <td>DistMult</td> <td>0.308</td> <td |
| InteractE | ✅ oui | .52</td> </tr> <tr> <td>InteractE</td> <td>0.354</td> <td |
| KGE-EML | ✅ oui | 569</td> </tr> <tr> <td>KGE-EML [11]</td> <td>0.36</td> |
| KGE-EML+GNS | ❌ NON | _(absent des tableaux)_ |
| PairRE | ✅ oui | ng></td> </tr> <tr> <td>PairRE</td> <td>0.351</td> <td |
| PROCRUSTES | ✅ oui | 528</td> </tr> <tr> <td>PROCRUSTES</td> <td>0.345</td> <td |
| RotatE | ✅ oui | 529</td> </tr> <tr> <td>RotatE</td> <td>0.338</td> <td |
| TransD | ✅ oui | </tr> <tr> <td rowspan="5">TransD</td> <td>Uniform</td> < |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE</td> <td>0.33</td> <td> |
| TuckER | ✅ oui | 554</td> </tr> <tr> <td>TuckER</td> <td>0.358</td> <td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| KG-BERT | ✅ oui | ed pre-trained models to tackle issues. KG-BERT [14], for instance, is a BERT-based kno |
| RESCAL | ✅ oui | . An eminent contender in this class is RESCAL proposed by Nickel et al. [24], which c |
| TransH | ✅ oui | gh similarity. To overcome challenges, TransH, introduced by [9], utilizes hyperplane |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| BERT | prose | pre-trained models to tackle issues. KG-BERT [14], for instance, is a BERT-based kno |