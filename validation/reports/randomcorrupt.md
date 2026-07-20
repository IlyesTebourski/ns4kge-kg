# Validation — RandomCorrupt.md

**Titre extrait :** Investigations on Knowledge Base Embedding for Relation Prediction and Extraction

## Score global (article)

| Metrique | Valeur |
|---|---|
| Entites extraites trouvees dans le texte (TP) | 18 |
| Extraites NON trouvees (FP -> erreur precision) | 1 |
| **Precision** | **94.7%** |
| Candidats faux negatifs (dans le texte, non extraits) | 5 |
| **Recall relatif (indicatif, a valider)** | **78.3%** |

## Datasets  —  precision 100% · recall~ 83%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| FB15k | ✅ oui | cally increases the difficulty of reasoning. FB15k (Bordes et al., 2013) is a subset of Freebas |
| FB15k-237 | ✅ oui | es with 1,345 different relations. Likewise, FB15k-237 is a subset of FB15k introduced by (Toutanov |
| FB3M | ✅ oui | ning and testing data. A new dataset, namely FB3M, is introduced which is also a subset of Fre |
| WN18 | ✅ oui | from the literature and introduce a new one. WN18 (Bordes et al., 2013) is a subset of WordNet |
| WN18RR | ✅ oui | onsists of 18 relations and 40,943 entities. WN18RR is a subset of WN18 introduced by (Dettmers |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Arxiv | arXiv:1802.02114v1 [cs.CL] 6 Feb 2018 # Investiga |

## Metrics  —  precision 100% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Hits@1 | ✅ oui | roportion of valid relations ranked in top-1(Hits@1). For each metric, we follow evaluation regi |
| MRR | ✅ oui | e mean reciprocal of correct relation ranks (MRR) and the proportion of valid relations ranke |

_Aucun candidat faux negatif pour cette categorie._

## NS Methods  —  precision 0% · recall~ 100%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| Unknown | ❌ NON | _(absent du texte)_ |

_Aucun candidat faux negatif pour cette categorie._

## KGE Models  —  precision 100% · recall~ 73%

### Precision : entites extraites par le KG

| Entite extraite | Trouvee dans le .md ? | Extrait de texte |
|---|:---:|---|
| ComplEx | ✅ oui | be a new benchmark, which is much larger and complex than previous ones, which we introduce to he |
| ConvE | ✅ oui | n to combine the two entities in a triple. **ConvE** (Dettmers et al., 2017) uses a convolution |
| DistMult | ✅ oui | ffectiveness, and flexibility: **TransE**, **DistMult** and **ComplEx**. We test on four establish |
| HOLE | ✅ oui | tends **DistMult** into the complex space. **HOLE** (Nickel et al., 2016) employs circular cor |
| ManifoldE | ✅ oui | g vectors of entities into various spaces. **ManifoldE** (Xiao et al., 2016) embeds a triple as a m |
| PTransE | ✅ oui | 2014), **TransR** (Lin et al., 2015b) and **PTransE** (Lin et al., 2015a). However, limited effo |
| RESCAL | ✅ oui | triple as a manifold rather than a point. **RESCAL** (Nickel et al., 2011) is one of the earlie |
| TransD | ✅ oui | 2014), **TransR** (Lin et al., 2015b) and **TransD** (Ji et al., 2015), extend **TransE** by pr |
| TransE | ✅ oui | implicity, effectiveness, and flexibility: **TransE**, **DistMult** and **ComplEx**. We test on |
| TransH | ✅ oui | n-based embedding. Later variants, such as **TransH** (Wang et al., 2014), **TransR** (Lin et al |
| TransR | ✅ oui | s, such as **TransH** (Wang et al., 2014), **TransR** (Lin et al., 2015b) and **TransD** (Ji et |

### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)

| Entite (vocab global) | Extrait de texte |
|---|---|
| Attention | 6. Neural relation extraction with selective attention over instances. In *ACL (1)*. Maximilian Ni |
| HAN | ural Language Processing*. pages 1779–1784. Han Xiao, Minlie Huang, and Xiaoyan Zhu. 2016. F |
| HypER | \quad (7) $$ where $\alpha \in (0, 1]$ is a hyper-parameter to tune the balance between the te |
| SimplE | of each other, and were only combined with a simple strategy at inference time. Since they got r |
