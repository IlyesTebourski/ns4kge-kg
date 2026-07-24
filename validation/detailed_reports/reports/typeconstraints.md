# Validation — TypeConstraints.md

**Titre extrait :** Type-Constrained Representation Learning in Knowledge Graphs

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 12 |
| Extraites NON trouvees (FP -> erreur precision) | 2 |
| **Precision** | **85.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 14 |
| **Recall relatif (indicatif, a valider)** | **46.2%** |

## Datasets  —  precision 100% · recall~ 43%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| DBpedia-Music | ✅ oui | r> </thead> <tbody> <tr> <td>DBpedia-Music</td> <td>DBpedia 2014</td> < |
| Freebase-150k | ✅ oui | >981,383</td> </tr> <tr> <td>Freebase-150k</td> <td>Freebase RDF-Dump</td> |
| YAGOc-195k | ✅ oui | ,047,844</td> </tr> <tr> <td>YAGOc-195k</td> <td>YAGO2-Core</td> <td |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:1508.02593v2 [cs.AI] 28 Aug 2015 # Type-Con |
| Cora | </sup> http://alchemy.cs.washington.edu/data/cora/ <sup>12</sup> We tried different amounts of |
| Table 1 Dataset | presentation Learning in Knowledge Graphs 9 Table 1. Datasets used in the experiments. <table> <thead> |
| Wikipedia | Freebase KG includes triples extracted from Wikipedia Infoboxes, MusicBrainz [21], WordNet [15] an |

## Metrics  —  precision 100% · recall~ 67%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| AUPRC | ✅ oui | eport the Area Under Precision Recall Curve (AUPRC) for all models. In addition, we provide the |
| AUROC | ✅ oui | der Receiver Operating Characteristic Curve (AUROC), because it is widely used in this problem |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| MAP | translation function exists that is able to map (or translate) the latent vector representat |

## NS Methods  —  precision 33% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Local Closed-World Assumption | ✅ oui | these cases, it can be beneficial to apply a local closed-world assumption that approximates the semantics of relation- |
| Type-Constrained Negative Sampling | ❌ NON | _(absent du texte)_ |
| Unknown | ❌ NON | _(absent du texte)_ |

_Aucun candidat faux negatif pour cette categorie._

## KGE Models  —  precision 100% · recall~ 40%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| mwNN | ✅ oui | gles Knowledge Vault project [8] (denoted as mwNN) for a number of reasons: * To the best of |
| Neural Tensor Network | ✅ oui | al modeling of KGs. [20] recently proposed a neural tensor network, which we did not consider in our study, sin |
| RESCAL | ✅ oui | n recent work [10,7], it has been shown that RESCAL, a much studied latent variable approach, be |
| TransE | ✅ oui | he art representative latent variable models TransE [5], RESCAL [18] and the multiway neural net |
| TransH | ✅ oui | nsor network proposed in [20]. [23] proposed TransH which improves TransE’s capability to model |
| TransR | ✅ oui | been further extended in [14] by introducing TransR which separates representations of entities |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | ent variable models have increasingly gained attention for the statistical modeling of knowledge gr |
| ComplEx | istic knowledge representation, which allows complex querying over all possible triples and their |
| HypER | $\lambda_A \ge 0$ and $\lambda_R \ge 0$ are hyper-parameters and $\\|\cdot\\|_F$ is the Frobeniu |
| Neural Tensor Networks | C. D. Manning, and A. Y. Ng. Reasoning With Neural Tensor Networks For Knowledge Base Completion. In *NIPS*. 20 |
| Random Walk | eval using a combination of path-constrained random walks. *Mach. Learn.*, 81(1):53–67, 2010. 13. O. |
| RatE | p>8</sup> AUROC considers the false-positive rate which relies on the amount of true-negatives |
| SimplE | sE, the translation function is defined by a simple addition of the latent vector representation |
| SME | es. <sup>9</sup> https://github.com/glorotxa/SME <sup>10</sup> Mainly caused by the ranking f |
| Unstructured | s proposed to support triple extraction from unstructured web documents. The confidence value $\theta_ |
