# KGE Models — NoiGAN.md

**Titre :** NoiGAN: Noise Aware Knowledge Graph Embedding with GAN

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 5 |
| Modeles MENTIONNES seulement (hors tableaux) | 5 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 0 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 100% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| Attention | ✅ oui | 507</td> </tr> <tr> <td>Attention</td> <td><strong>436</strong></ |
| DistMult | ✅ oui | <td rowspan="10">0%</td> <td>DistMult</td> <td>.218</td> <td> |
| KBGAN | ✅ oui | 507</td> </tr> <tr> <td>KBGAN</td> <td>.266</td> <td> |
| RotatE | ✅ oui | 503</td> </tr> <tr> <td>RotatE</td> <td>.326</td> <td> |
| TransE | ✅ oui | > </tr> <tr> <td>NoiGAN-TransE (soft)</td> <td><strong>.949</s |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| CKRL | ✅ oui | 19)), (3) noise aware KGE models (e.g., CKRL (Xie et al., 2018)) and (4) KGE models |
| ComplEx | ✅ oui | 2011), DistMult (Yang et al., 2014) and ComplEx (Trouillon et al., 2016). To optimize t |
| RESCAL | ✅ oui | esentations. The typical models include RESCAL (Nickel et al., 2011), DistMult (Yang e |
| TransH | ✅ oui | relation. TransE (Bordes et al., 2013), TransH (Wang et al., 2014) and TransR (Lin et |
| TransR | ✅ oui | , 2013), TransH (Wang et al., 2014) and TransR (Lin et al., 2015) are the representati |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._