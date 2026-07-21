# KGE Models — DHNS.md

**Titre :** Diffusion-based Hierarchical Negative Sampling for Multimodal Knowledge Graph Completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 15 |
| Modeles MENTIONNES seulement (hors tableaux) | 6 |
| **Precision globale** | **100%** |
| Precision (evalues, vs tableaux) | 100% |
| Precision (mentionnes, vs prose) | 100% |
| Candidats evaluations ratees (en tableau, non extrait) | 1 |
| Candidats mentions ratees (en prose, non extrait) | 0 |
| Recall relatif *evalues* | 94% |
| Recall relatif *mentionnes* | 100% |

## A. Modeles EVALUES — extraits des tableaux (valides vs `tables_only`)

| Modele | Trouve dans les tableaux ? | Extrait |
|---|:---:|---|
| AdaMF | ✅ oui | .88</td> </tr> <tr> <td>AdaMF</td> <td><u>32.51</u></td> |
| ComplEx | ✅ oui | .80</td> </tr> <tr> <td>ComplEx</td> <td>27.48</td> <td |
| DistMult | ✅ oui | .68</td> </tr> <tr> <td>DistMult</td> <td>23.03</td> <td |
| GC-OTE | ✅ oui | .71</td> </tr> <tr> <td>GC-OTE</td> <td>31.85</td> <td |
| IKRL | ✅ oui | wspan="8">MMKGC Models</td> <td>IKRL</td> <td>26.82</td> <td |
| MMKRL | ✅ oui | .72</td> </tr> <tr> <td>MMKRL</td> <td>26.81</td> <td |
| OTKGE | ✅ oui | .62</td> </tr> <tr> <td>OTKGE</td> <td>23.86</td> <td |
| PairRE | ✅ oui | .73</td> </tr> <tr> <td>PairRE</td> <td>31.13</td> <td |
| RotatE | ✅ oui | r framework DHNS</mark> integrated with RotatE model and some state-of-the-art baselin |
| RSME | ✅ oui | .44</td> </tr> <tr> <td>RSME</td> <td>29.76</td> <td |
| TBKGC | ✅ oui | .07</td> </tr> <tr> <td>TBKGC</td> <td>28.08</td> <td |
| TransAE | ✅ oui | .58</td> </tr> <tr> <td>TransAE</td> <td>28.09</td> <td |
| TransD | ✅ oui | .23</td> </tr> <tr> <td>TransD</td> <td>21.52</td> <td |
| TransE | ✅ oui | 7">Unimodal KGC Models</td> <td>TransE</td> <td>24.86</td> <td |
| VBKGC | ✅ oui | .83</td> </tr> <tr> <td>VBKGC</td> <td>30.61</td> <td |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| KGDM | ✅ oui | idering the query node's context, while KGDM [16] applies DDPM to estimate the proba |
| LAFA | ✅ oui | y in an adversarial training framework. LAFA [24] considers the relationships betwee |
| QuatE | ✅ oui | ntisymmetric relations. RotatE [25] and QuatE [36] introduce rotational and quaternio |
| RESCAL | ✅ oui | ar interaction-based KGE models such as RESCAL [22] and DistMult [35], formulated as: |
| TransH | ✅ oui | based KGE models such as TransE [3] and TransH [31], formulated as: $$C(\mathbf{x}_e, |
| VISTA | ✅ oui | aggregation of multi-modal information. VISTA [11] designs three transformer-based en |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

| Modele | Ou | Extrait |
|---|---|---|
| OTE | prose+table | x [27], RotatE [25], PairRE [7], and GC-OTE [26]. (2) **Multimodal KGC models:** w |

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._