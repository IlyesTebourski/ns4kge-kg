# KGE Models — TypeAugmented.md

**Titre :** A type-augmented knowledge graph embedding framework for knowledge graph completion

| Metrique | Valeur |
|---|---|
| Modeles EVALUES (dans les tableaux) | 12 |
| Modeles MENTIONNES seulement (hors tableaux) | 11 |
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
| ComplEx | ✅ oui | td> </tr> <tr> <td>TaKE+ComplEx</td> <td>O(d + k)</td> |
| DistMult | ✅ oui | td> </tr> <tr> <td>TaKE+Distmult</td> <td>O(d + k)</td> |
| RotatE | ✅ oui | td> </tr> <tr> <td>TaKE+RotatE</td> <td>O(d + k)</td> |
| SimplE | ✅ oui | td> </tr> <tr> <td>TaKE+SimplE</td> <td>O(d + k)</td> |
| TaKE-ComplEx | ✅ oui | 428</td> </tr> <tr> <td>TaKE-ComplEx</td> <td>0.778</td> <td |
| TaKE-DistMult | ✅ oui | 419</td> </tr> <tr> <td>TaKE-DistMult</td> <td>0.757</td> <td |
| TaKE-RotatE | ✅ oui | 533</td> </tr> <tr> <td>TaKE-RotatE</td> <td>0.804</td> <td |
| TaKE-SimplE | ✅ oui | 476</td> </tr> <tr> <td>TaKE-SimplE</td> <td><strong>0.806</strong> |
| TaKE-TransE | ✅ oui | 465</td> </tr> <tr> <td>TaKE-TransE</td> <td>0.490</td> <td |
| TransE | ✅ oui | td> </tr> <tr> <td>TaKE+TransE</td> <td>O(d + k)</td> |
| TypeComplex | ✅ oui | R\|)</td> </tr> <tr> <td>TypeComplex</td> <td>O(d + k)</td> |
| TypeDM | ✅ oui | </thead> <tbody> <tr> <td>TypeDM</td> <td>O(d + k)</td> |

## B. Modeles MENTIONNES seulement — hors tableaux (valides vs prose)

| Modele | Trouve dans la prose ? | Extrait |
|---|:---:|---|
| CAKE | ✅ oui | esides, Niu et al.<sup>33</sup> propose CAKE which automatically extract commonsense |
| HAKE | ✅ oui | g to tail embedding. Soon after RotatE, HAKE<sup>16</sup> and RatE<sup>17</sup> make |
| JOIE | ✅ oui | ons to model the semantic transitivity. JOIE<sup>24</sup> directly represents a KG a |
| RatE | ✅ oui | oon after RotatE, HAKE<sup>16</sup> and RatE<sup>17</sup> make slight improvements t |
| TaKE | ✅ oui | ed Knowledge graph Embedding framework (TaKE) which could utilize type features to e |
| TaRP | ✅ oui | two views. Both TransT<sup>30</sup> and TaRP<sup>32</sup> collect relation types fro |
| TKRL | ✅ oui | xploring the usage of type information. TKRL<sup>22</sup> extends traditional TransE |
| TransC | ✅ oui | nct representations in different types. TransC<sup>23</sup> clearly distinguish concep |
| TransH | ✅ oui | of TransE have been developed. Such as, TransH<sup>13</sup> projects entity embeddings |
| TransR | ✅ oui | stead of relation-specific hyperplanes, TransR<sup>14</sup> directly projects entity e |
| TransT | ✅ oui | d jointly encodes these two views. Both TransT<sup>30</sup> and TaRP<sup>32</sup> coll |

## C1. Recall EVALUES — modeles dans un tableau mais NON extraits

_Aucun._

## C2. Recall MENTIONNES — modeles en prose seulement mais NON extraits

_Aucun._