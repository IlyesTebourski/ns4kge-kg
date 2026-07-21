# KGE Models — GNDN.md

**Titre :** A generative adversarial network for single and multi-hop distributional knowledge base completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 12 |
| Modeles MENTIONNES seulement (hors tableaux) | 6 |
| **Precision globale** | **94%** |
| Precision (evalues, vs tableaux) | 92% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 3 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 67% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| ConvE | ✅ oui | 5.8</td> </tr> <tr> <td>ConvE [19]*</td> <td>0.46</td> |
| ConvKB | ✅ oui | 9.1</td> </tr> <tr> <td>ConvKB [20]</td> <td>0.248</td> |
| Knowledge Completion GAN | ❌ NON | _(absent des tableaux)_ |
| NTN | ✅ oui | 5.2</td> </tr> <tr> <td>NTN [8]*</td> <td>70.6</td> |
| Path-KCGAN [2 hop] | ✅ oui | 4.6</td> </tr> <tr> <td>Path-KCGAN[2 hop]</td> <td>0.58</td> <td |
| Path-KCGAN [3 hop] | ✅ oui | 7.1</td> </tr> <tr> <td>Path-KCGAN[3 hop]</td> <td>0.60</td> <td |
| PathG-RNN [2 hop] | ✅ oui | </thead> <tbody> <tr> <td>PathG-RNN [2 hop]</td> <td>0.41</td> <td |
| PathG-RNN [3 hop] | ✅ oui | 6.3</td> </tr> <tr> <td>PathG-RNN [3 hop]</td> <td>0.43</td> <td |
| PTransE [2 hop] | ✅ oui | 8.5</td> </tr> <tr> <td>PTransE [2 hop]</td> <td>0.49</td> <td |
| PTransE [3 hop] | ✅ oui | 2.2</td> </tr> <tr> <td>PTransE [3 hop]</td> <td>0.54</td> <td |
| TransE | ✅ oui | </thead> <tbody> <tr> <td>TransE [9]*</td> <td>70.9</td> |
| TransG | ✅ oui | 8.9</td> </tr> <tr> <td>TransG [16]*</td> <td>87.4</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| DistMult | ✅ oui | ions over entities and relations, and a DistMult based decoder for factorization. The GC |
| ELECTRA | ✅ oui | ecently developed language model called ELECTRA [37], which is a compute-efficient GAN- |
| HypER | ✅ oui | igm and reports better overall results. HypER [26] uses a 1D-relation-specific convol |
| KCGAN | ✅ oui | iscriminative belief prediction models. KCGAN thus invokes a game between generator-n |
| KG-BERT | ✅ oui | ansformer-based encoding models such as KG-BERT [35] are inspired by transformer-based |
| PTransE | ✅ oui | red as PathG-RNNs. We also compare with PTransE which is a variant of TransE for integr |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| BERT | prose | former-based encoding models such as KG-BERT [35] are inspired by transformer-based |
| GAN | prose | challenges are addressed: 1) Classical GAN architectures’ inability to easily gene |
| GCN | prose | sists of a Convolutional Graph Network (GCN) [39] based encoder for learning repres |