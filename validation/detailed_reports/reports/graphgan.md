# Validation — GraphGAN.md

**Titre extrait :** GraphGAN: Graph Representation Learning with Generative Adversarial Nets

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 14 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **93.3%** |
| Candidats faux negatifs (dans le texte, non extraits) | 16 |
| **Recall relatif (indicatif, a valider)** | **46.7%** |

## Datasets  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| arXiv-AstroPh | ✅ oui | owing five datasets in our experiments: * **arXiv-AstroPh**<sup>2</sup> is from the e-print arXiv and |
| arXiv-GrQc | ✅ oui | has 18,772 vertices and 198,110 edges. * **arXiv-GrQc**<sup>3</sup> is also from arXiv and covers |
| BlogCatalog | ✅ oui | ph has 5,242 vertices and 14,496 edges. * **BlogCatalog**<sup>4</sup> is a network of social relatio |
| Wikipedia | ✅ oui | 333,982 edges, and 39 different labels. * **Wikipedia**<sup>5</sup> is a co-occurrence network of |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | 2017 Nov 22 [cs.LG] arXiv:1711.08267v1 # GraphGAN: Graph Representati |
| MovieLens | 184,812 edges, and 40 different labels. * **MovieLens-1M**<sup>6</sup> is a bipartite graph consis |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Accuracy | ✅ oui | 95% to 21.71% in node classification both on Accuracy. Additionally, GraphGAN improves Precision@2 |
| F1 | ✅ oui | en vertex pair. Table 1: Accuracy and Macro-F1 on arXiv-AstroPh and arXiv-GrQc in link pred |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 50% · recall~ 20%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Negative Sampling | ✅ oui | ositive samples (connected vertex pairs) and negative samples (disconnected vertex pairs), also preserving |
| Unknown | ❌ NON | _(absent du texte)_ |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| GAN | E). Recently, *Generative Adversarial Nets* (GAN) (Goodfellow et al. 2014) have received a gr |
| IRGAN | ce. The result suggests that, different with IRGAN (Wang et al. 2017a), the design of graph sof |
| Random Negative Sampling | $ for all vertices $v \neq v_c$, and perform random sampling proportionally to their approximated connect |
| Random Sampling | $ for all vertices $v \neq v_c$, and perform random sampling proportionally to their approximated connect |

## KGE Models  —  precision 100% · recall~ 41%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DeepWalk | ✅ oui | kelihood of edges in the graph. For example, DeepWalk (Perozzi, Al-Rfou, and Skiena 2014) uses ran |
| GraphGAN | ✅ oui | 2017 Nov 22 [cs.LG] arXiv:1711.08267v1 # GraphGAN: Graph Representation Learning with Generati |
| LINE | ✅ oui | the same coin (Wang et al. 2017a). In fact, LINE (Tang et al. 2015) has done a preliminary tr |
| Node2vec | ✅ oui | rving context vertices for the given vertex. Node2vec (Grover and Leskovec 2016) further extends t |
| PPNE | ✅ oui | ces under the supervision of edge existence. PPNE (Li et al. 2017b) directly learns vertex emb |
| SDNE | ✅ oui | he training data in the graph. For instance, SDNE (Wang, \*M. Guo is the corresponding author |
| Struc2vec | ✅ oui | td>0.842</td> </tr> <tr> <td>Struc2vec</td> <td>0.821</td> <td>0.81 |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | w et al. 2014) have received a great deal of attention. By designing a game-theoretical *minimax* g |
| GAN | E). Recently, *Generative Adversarial Nets* (GAN) (Goodfellow et al. 2014) have received a gr |
| HAN | ; Sturt, B.; Khandelwal, U.; Norick, B.; and Han, J. 2014. Personalized entity recommendation |
| HypER | $k$ for all methods is set as 20. The above hyper-parameters are chosen by cross validation. T |
| MEI | et al. 2014), text embedding (Tang, Qu, and Mei 2015), and social network analysis (Liu et a |
| metapath2vec | Dong, Y.; Chawla, N. V.; and Swami, A. 2017. metapath2vec: Scalable representation learning for hetero |
| Random Walk | alk (Perozzi, Al-Rfou, and Skiena 2014) uses random walk to sample "context" vertices for each vertex |
| RatE | update parameters in GraphGAN with learning rate 0.001. In each iteration, we set $s$ as 20 a |
| StAR | ens-1M in recommendation. first treat all 4-star and 5-star ratings as edges to obtain a bipa |
| TaKE | raph-structure-aware.** The generator should take advantage of the structural information of a |
