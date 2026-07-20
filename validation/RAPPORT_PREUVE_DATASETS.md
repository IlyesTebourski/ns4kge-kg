# Rapport-preuve — Validation des *datasets* extraits (NS4KGE)

Corpus : **55 articles** — Source : `Configurations[].Dataset` (prompt2) — Validation contre `load_md_tables_only()` (tables uniquement).

## 1. Définitions

| Terme | Définition |
|---|---|
| TP | dataset extrait par le KG ET présent dans les tableaux de l'article |
| FP | dataset extrait par le KG mais absent des tableaux |
| Candidat FN | dataset présent dans une cellule `<table>` mais non extrait |
| Précision | TP / (TP + FP) |
| Recall relatif | TP / (TP + candidats FN en table de résultats) |

**Méthodo (matching) :** insensible à la casse ; séparateurs `-_/.@` tolérés ; frontières strictes (`FB15k` ≠ `FB15k-237`) ; recall cherché uniquement dans les blocs `<table>` ; tableaux classés *stats* vs *résultats* via leur caption.

## 2. Résultats globaux

| Indicateur | Valeur |
|---|---|
| Datasets extraits (lignes vérifiées) | 184 |
| Validés (TP) | 182 |
| Non validés (FP) | 2 |
| **Précision (micro)** | **98.9%** |
| Candidats FN en table de résultats | 5 |
| Candidats FN en table de stats (ignorés par le prompt) | 1 |
| **Recall relatif (micro)** | **97.3%** |
| Vocabulaire global de datasets | 73 |

## 3. Analyse des erreurs

### 3.1 Faux positifs (extraits mais absents des tableaux)

| Article | Dataset extrait |
|---|---|
| CondConstraints.md | Table 1 Dataset |
| GNS.md | FB13 (FB13_reduced) |

### 3.2 Candidats faux négatifs — table de résultats

| Article | Dataset | Table | Citation |
|---|---|---|---|
| CANS.md | FB15k | (sans caption) | </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td |
| CANS.md | WN18 | (sans caption) | </thead> <tbody> <tr> <td>WN18</td> <td>18</td> <td>40 |
| ConceptDriven.md | WN | (sans caption) | table> <thead> <tr> <th>Method</th> <th>WN.↑</th> <th>FB.↑</th> <th>AVG.↑</th> <th |
| NoiGAN.md | Actor | (sans caption) | <td>Positive</td> <td>(voice actor (filmmaking occupation),<br/>/people/pr |
| Uniform.md | Actor | (sans caption) | <br/>Screen Actors Guild Award for Best Actor - Motion Picture</td> </tr> <tr |

### 3.3 Candidats faux négatifs — table de statistiques (priorité basse)

| Article | Dataset | Table | Citation |
|---|---|---|---|
| GNS.md | FB13 | Table 1: The statistics for base line d… | </thead> <tbody> <tr> <td>FB13 (FB13_reduced)</td> <td>13</td> |

## 4. Preuve détaillée — 184 datasets extraits (182 validés / 2 non)

| # | Article | Dataset extrait | Validé | Table | Citation dans le texte |
|---:|---|---|:---:|---|---|
| 1 | AdaptativeNS.md | FB15k-237 | ✅ | (sans caption) | 134</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 2 | AdaptativeNS.md | WN18RR | ✅ | (sans caption) | </thead> <tbody> <tr> <td>WN18RR</td> <td>40,493</td> <t |
| 3 | AdaptativeNS.md | YAGO3-10 | ✅ | (sans caption) | 466</td> </tr> <tr> <td>YAGO3-10</td> <td>123,182</td> < |
| 4 | ADNS.md | Kinship | ✅ | Table 1. Statistical information of the… | 652</td> </tr> <tr> <td>Kinship</td> <td>104</td> <td>2 |
| 5 | ADNS.md | Nations | ✅ | Table 1. Statistical information of the… | 068</td> </tr> <tr> <td>Nations</td> <td>14</td> <td>55 |
| 6 | ADNS.md | UMLS | ✅ | Table 1. Statistical information of the… | </thead> <tbody> <tr> <td>UMLS</td> <td>135</td> <td>4 |
| 7 | ASA.md | Amazon | ✅ | Table 1: Statistics of the datasets. | </thead> <tbody> <tr> <td>Amazon (Cen et al. 2019)</td> <td>10,1 |
| 8 | ASA.md | Company | ✅ | Table 1: Statistics of the datasets. | /10</td> </tr> <tr> <td>Company</td> <td>11,585</td> <t |
| 9 | ASA.md | Youtube | ✅ | Table 1: Statistics of the datasets. | /10</td> </tr> <tr> <td>Youtube (Cen et al. 2019)</td> <td>2,00 |
| 10 | BatchNS.md | FB15k | ✅ | (hors table) | PBG with other embedding methods on the FB15k dataset. PBG embeddings are trained wit |
| 11 | BatchNS.md | LiveJournal | ✅ | (hors table) | mance of PBG, DeepWalk, and MILE on the LiveJournal dataset and the YouTube dataset. **Left |
| 12 | CAKE.md | DBpedia-242 | ✅ | Table 1: Statistics of the experimental… | 838</td> </tr> <tr> <td>DBpedia-242</td> <td>298</td> <td>9 |
| 13 | CAKE.md | FB15K | ✅ | Table 1: Statistics of the experimental… | </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td |
| 14 | CAKE.md | FB15K237 | ✅ | Table 1: Statistics of the experimental… | 071</td> </tr> <tr> <td>FB15K237</td> <td>237</td> <td>1 |
| 15 | CAKE.md | NELL-995 | ✅ | Table 1: Statistics of the experimental… | 466</td> </tr> <tr> <td>NELL-995</td> <td>200</td> <td>7 |
| 16 | CANS.md | FB15K-N1 | ✅ | (sans caption) | r> <th>Dataset</th> <th>FB15K-N1</th> <th>FB15K-N2</th> |
| 17 | CANS.md | FB15K-N2 | ✅ | (sans caption) | > <th>FB15K-N1</th> <th>FB15K-N2</th> <th>FB15K-N3</th> </tr |
| 18 | CANS.md | FB15K-N3 | ✅ | (sans caption) | > <th>FB15K-N2</th> <th>FB15K-N3</th> </tr> </thead> <tbody> |
| 19 | CANS.md | WN18-N1 | ✅ | (sans caption) | r> <th>Dataset</th> <th>WN18-N1</th> <th>WN18-N2</th> < |
| 20 | CANS.md | WN18-N2 | ✅ | (sans caption) | h> <th>WN18-N1</th> <th>WN18-N2</th> <th>WN18-N3</th> </tr> |
| 21 | CANS.md | WN18-N3 | ✅ | (sans caption) | h> <th>WN18-N2</th> <th>WN18-N3</th> </tr> </thead> <tbody> |
| 22 | CCS.md | FB15K | ✅ | Table 3. Optimal configurations of each… | 000</td> </tr> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 23 | CCS.md | FB15K237 | ✅ | Table 3. Optimal configurations of each… | 134</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <t |
| 24 | CCS.md | WN18 | ✅ | Table 3. Optimal configurations of each… | 466</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 25 | CCS.md | WN18RR | ✅ | Table 3. Optimal configurations of each… | </thead> <tbody> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 26 | ConceptDriven.md | FB15k-237 | ✅ | (sans caption) | ,034</td> <td>3,134</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <td>237</td> <td>2 |
| 27 | ConceptDriven.md | WN18RR | ✅ | (sans caption) | st</th> </tr> </thead> <tbody> <tr> <td>WN18RR</td> <td>40,943</td> <td>11</td> <td>86 |
| 28 | CondConstraints.md | MUTAG | ✅ | (hors table) | Table 1, while those for MUTAG can be found in Table 2. Note that for |
| 29 | CondConstraints.md | Table 1 Dataset | ❌ | — | — |
| 30 | dans.md | NELL-995 | ✅ | Table 1: Statistics of datasets. | 003</td> </tr> <tr> <td>NELL-995</td> <td>63,916</td> <t |
| 31 | dans.md | UMLS | ✅ | Table 1: Statistics of datasets. | 465</td> </tr> <tr> <td>UMLS</td> <td>135</td> <td>4 |
| 32 | dans.md | WN18RR | ✅ | Table 1: Statistics of datasets. | </thead> <tbody> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 33 | DeMix.md | FB15K237 | ✅ | (sans caption) | 134</td> </tr> <tr> <td>FB15K237</td> <td>237</td> <td>1 |
| 34 | DeMix.md | WN18RR | ✅ | (sans caption) | </thead> <tbody> <tr> <td>WN18RR</td> <td>11</td> <td>40 |
| 35 | DHNS.md | DB15K | ✅ | Table 1. Statistics of three MMKGC benc… | </thead> <tbody> <tr> <td>DB15K</td> <td>12842</td> <td |
| 36 | DHNS.md | MKG-W | ✅ | Table 1. Statistics of three MMKGC benc… | 904</td> </tr> <tr> <td>MKG-W</td> <td>15000</td> <td |
| 37 | DHNS.md | MKG-Y | ✅ | Table 1. Statistics of three MMKGC benc… | 274</td> </tr> <tr> <td>MKG-Y</td> <td>15000</td> <td |
| 38 | DMNS.md | Actor | ✅ | Table 1: Summary of datasets. | ous</td> </tr> <tr> <td>Actor</td> <td>7600</td> <td> |
| 39 | DMNS.md | Citeseer | ✅ | Table 1: Summary of datasets. | ous</td> </tr> <tr> <td>Citeseer</td> <td>3327</td> <td> |
| 40 | DMNS.md | Coauthor-CS | ✅ | Table 1: Summary of datasets. | ous</td> </tr> <tr> <td>Coauthor-CS</td> <td>18333</td> <td |
| 41 | DMNS.md | Cora | ✅ | Table 1: Summary of datasets. | </thead> <tbody> <tr> <td>Cora</td> <td>2708</td> <td> |
| 42 | DNS.md | FB15k | ✅ | Table 1: Knowledge Base completion data… | r> <th>Dataset</th> <th>FB15K</th> <th>Fb15k-237</th> |
| 43 | DNS.md | Fb15k-237 | ✅ | Table 1: Knowledge Base completion data… | /th> <th>FB15K</th> <th>Fb15k-237</th> <th>WN18RR</th> </tr> |
| 44 | DNS.md | WN18RR | ✅ | Table 1: Knowledge Base completion data… | <th>Fb15k-237</th> <th>WN18RR</th> </tr> </thead> <tbody> |
| 45 | DomainNS.md | FB15k | ✅ | Table 1. | 000</td> </tr> <tr> <td>FB15k</td> <td>14,951</td> <t |
| 46 | DomainNS.md | WN18 | ✅ | Table 1. | </thead> <tbody> <tr> <td>WN18</td> <td>40,943</td> <t |
| 47 | EANS.md | FB15K237 | ✅ | Table 1: Statistics of FB15K-237 and WN… | </thead> <tbody> <tr> <td>FB15K237</td> <td>14,541</td> <t |
| 48 | EANS.md | WN18RR | ✅ | (hors table) | Table 1: Statistics of FB15K-237 and WN18RR datasets. <table> <thead> <tr> |
| 49 | ERDNS.md | FB15K237 | ✅ | Table 1.** Comparison of the proposed m… | </thead> <tbody> <tr> <td>FB15K237</td> <td>0</td> <td>100 |
| 50 | ERDNS.md | WN18RR | ✅ | Table 1.** Comparison of the proposed m… | d>1</td> </tr> <tr> <td>WN18RR</td> <td>0</td> <td>100 |
| 51 | ERDNS.md | YAGO3-10 | ✅ | Table 1.** Comparison of the proposed m… | d>1</td> </tr> <tr> <td>YAGO3-10</td> <td>0</td> <td>100 |
| 52 | eTruncatedUNS.md | DBP-WD | ✅ | Table 1: Statistical data of DWY100K | tbody> <tr> <td rowspan="2">DBP-WD</td> <td>DBpedia</td> < |
| 53 | eTruncatedUNS.md | DBP-YG | ✅ | Table 1: Statistical data of DWY100K | </tr> <tr> <td rowspan="2">DBP-YG</td> <td>DBpedia</td> < |
| 54 | eTruncatedUNS.md | DBP_FR-EN | ✅ | (sans caption) | /td> </tr> <tr> <td>(C) DBP_FR-EN</td> <td>S1</td> <td>0. |
| 55 | eTruncatedUNS.md | DBP_JA-EN | ✅ | (sans caption) | /td> </tr> <tr> <td>(B) DBP_JA-EN</td> <td>S1</td> <td>0. |
| 56 | eTruncatedUNS.md | DBP_ZH-EN | ✅ | (sans caption) | ead> <tbody> <tr> <td>(A) DBP_ZH-EN</td> <td>S1</td> <td>0. |
| 57 | GHN.md | FB15k-237 | ✅ | Table 1: Statistics of the datasets use… | 134</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 58 | GHN.md | Wikidata5M | ✅ | Table 1: Statistics of the datasets use… | 466</td> </tr> <tr> <td>Wikidata5M</td> <td>4,594,485</td> |
| 59 | GHN.md | WN18RR | ✅ | Table 1: Statistics of the datasets use… | </thead> <tbody> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 60 | GibbsNS.md | FB15k | ✅ | (hors table) | Table 1. Statistics of public datasets: FB15k, FB12k-237, and WN11RR. <table> <thea |
| 61 | GibbsNS.md | FB15k-237 | ✅ | Table 1. Statistics of public datasets:… | 134</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 62 | GibbsNS.md | WN18RR | ✅ | (hors table) | ink prediction results on FB15k-237 and WN18RR. <table> <thead> <tr> <th |
| 63 | GNDN.md | FB15K | ✅ | Table 2 | 000</td> </tr> <tr> <td>FB15K</td> <td>1345</td> <td> |
| 64 | GNDN.md | WN18 | ✅ | Table 2 | </thead> <tbody> <tr> <td>WN18</td> <td>18</td> <td>40 |
| 65 | GNS.md | FB13 (FB13_reduced) | ❌ | — | — |
| 66 | GraphGAN.md | arXiv-AstroPh | ✅ | (hors table) | ble> Table 1: Accuracy and Macro-F1 on arXiv-AstroPh and arXiv-GrQc in link prediction. <tab |
| 67 | GraphGAN.md | arXiv-GrQc | ✅ | (hors table) | uracy and Macro-F1 on arXiv-AstroPh and arXiv-GrQc in link prediction. <table> <thead> |
| 68 | GraphGAN.md | BlogCatalog | ✅ | (hors table) | ble> Table 2: Accuracy and Macro-F1 on BlogCatalog and Wikipedia in node classification. < |
| 69 | GraphGAN.md | Wikipedia | ✅ | (hors table) | ccuracy and Macro-F1 on BlogCatalog and Wikipedia in node classification. <table> <thea |
| 70 | HaSa.md | FB15k-237 | ✅ | Table 1: Dataset | lspan="3"># of false negative triple in FB15K-237</td> </tr> <tr> <td>512 |
| 71 | HaSa.md | WN18RR | ✅ | Table 1: Dataset | lspan="3"># of false negative triple in WN18RR</td> </tr> <tr> <td>512 |
| 72 | HTENS.md | FB15K | ✅ | (sans caption) | </thead> <tbody> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 73 | HTENS.md | FB15K237 | ✅ | (sans caption) | 071</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <t |
| 74 | IGAN.md | FB13 | ✅ | Table 1: Data sets used in the experime… | 071</td> </tr> <tr> <td>FB13</td> <td>13</td> <td>75 |
| 75 | IGAN.md | FB15K | ✅ | Table 1: Data sets used in the experime… | </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td |
| 76 | IGAN.md | WN11 | ✅ | Table 1: Data sets used in the experime… | 733</td> </tr> <tr> <td>WN11</td> <td>11</td> <td>38 |
| 77 | IGAN.md | WN18 | ✅ | Table 1: Data sets used in the experime… | 544</td> </tr> <tr> <td>WN18</td> <td>18</td> <td>40 |
| 78 | KBGAN.md | FB15k-237 | ✅ | (hors table) | and COMPLEX, $\lambda = 1$ is used for FB15k-237 and $\lambda = 0.1$ is used for WN18 an |
| 79 | KBGAN.md | WN18 | ✅ | (hors table) | 15k-237 and $\lambda = 0.1$ is used for WN18 and WN18RR. All other hyperparameters a |
| 80 | KBGAN.md | WN18RR | ✅ | (hors table) | nd $\lambda = 0.1$ is used for WN18 and WN18RR. All other hyperparameters are shared a |
| 81 | KSGAN.md | FB15k-237 | ✅ | (sans caption) | </thead> <tbody> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 82 | KSGAN.md | WN18 | ✅ | (sans caption) | 466</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 83 | KSGAN.md | WN18RR | ✅ | (sans caption) | 000</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 84 | LAS.md | FB15k237 | ✅ | (sans caption) | </thead> <tbody> <tr> <td>FB15k237</td> <td>14,541</td> <t |
| 85 | LAS.md | WN18 | ✅ | (sans caption) | 466</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 86 | LAS.md | WN18RR | ✅ | (sans caption) | 000</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 87 | LEMON.md | WN18 | ✅ | Table 1: Dataset statistics. This table… | </thead> <tbody> <tr> <td>WN18</td> <td>40,943</td> <t |
| 88 | LEMON.md | WN18RR | ✅ | Table 1: Dataset statistics. This table… | 000</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 89 | Localcognitive.md | FB15k | ✅ | Table 3 and Table 4. It is observed tha… | 000</td> </tr> <tr> <td>FB15k</td> <td>14,951</td> <t |
| 90 | Localcognitive.md | FB15k-237 | ✅ | Table 3 and Table 4. It is observed tha… | 134</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 91 | Localcognitive.md | WN18 | ✅ | Table 3 and Table 4. It is observed tha… | </thead> <tbody> <tr> <td>WN18</td> <td>40,943</td> <t |
| 92 | Localcognitive.md | WN18RR | ✅ | Table 3 and Table 4. It is observed tha… | 071</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 93 | LTS.md | DBP-GEO | ✅ | (sans caption) | h> <th>DBP-LGD</th> <th>DBP-GEO</th> </tr> </thead> <tbody> |
| 94 | LTS.md | DBP-LGD | ✅ | (sans caption) | <tr> <th>model</th> <th>DBP-LGD</th> <th>DBP-GEO</th> </tr> |
| 95 | LTS.md | FB15K | ✅ | (sans caption) | </thead> <tbody> <tr> <td>FB15K</td> <td>14951</td> <td |
| 96 | LTS.md | WN18 | ✅ | (sans caption) | 071</td> </tr> <tr> <td>WN18</td> <td>40943</td> <td |
| 97 | M2ixKG.md | FB15k-237 | ✅ | Table 1: Statistics of datasets | th> <th>WN18RR</th> <th>FB15k-237</th> </tr> </thead> <tbody> |
| 98 | M2ixKG.md | WN18RR | ✅ | Table 1: Statistics of datasets | r> <th>Dataset</th> <th>WN18RR</th> <th>FB15k-237</th> </t |
| 99 | MCNS.md | Alibaba | ✅ | Table 1: Statistics of the tasks and da… | d>/</td> </tr> <tr> <td>Alibaba</td> <td>159,633</td> < |
| 100 | MCNS.md | Amazon | ✅ | Table 1: Statistics of the tasks and da… | d>/</td> </tr> <tr> <td>Amazon</td> <td>255,404</td> < |
| 101 | MCNS.md | Arxiv | ✅ | Table 1: Statistics of the tasks and da… | <td>Link Prediction</td> <td>Arxiv</td> <td>5,242</td> <td |
| 102 | MCNS.md | BlogCatalog | ✅ | Table 1: Statistics of the tasks and da… | td>Node Classification</td> <td>BlogCatalog</td> <td>10,312</td> <t |
| 103 | MCNS.md | MovieLens | ✅ | Table 1: Statistics of the tasks and da… | pan="3">Recommendation</td> <td>MovieLens</td> <td>2,625</td> <td |
| 104 | MDNCaching.md | FB15K237 | ✅ | Table 3. Comparison of state-of-the-art… | 134</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <t |
| 105 | MDNCaching.md | WN18RR | ✅ | Table 3. Comparison of state-of-the-art… | </thead> <tbody> <tr> <td>WN18RR</td> <td>93,003</td> <t |
| 106 | NMiss.md | FB15k | ✅ | (sans caption) | </thead> <tbody> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 107 | NMiss.md | WN18 | ✅ | (sans caption) | 071</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 108 | NoiGAN.md | FB15K | ✅ | Table 1: Data Statistics | </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td |
| 109 | NoiGAN.md | FB15K-237 | ✅ | Table 1: Data Statistics | 000</td> </tr> <tr> <td>FB15K-237</td> <td>237</td> <td>1 |
| 110 | NoiGAN.md | WN18 | ✅ | Table 1: Data Statistics | 071</td> </tr> <tr> <td>WN18</td> <td>18</td> <td>40 |
| 111 | NoiGAN.md | WN18RR | ✅ | Table 1: Data Statistics | 466</td> </tr> <tr> <td>WN18RR</td> <td>11</td> <td>40 |
| 112 | NoiGAN.md | YAGO3-10 | ✅ | Table 1: Data Statistics | 134</td> </tr> <tr> <td>YAGO3-10</td> <td>37</td> <td>12 |
| 113 | NSCaching.md | FB15K | ✅ | (sans caption) | 134</td> </tr> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 114 | NSCaching.md | FB15K237 | ✅ | (sans caption) | 071</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <t |
| 115 | NSCaching.md | WN18 | ✅ | (sans caption) | </thead> <tbody> <tr> <td>WN18</td> <td>40,943</td> <t |
| 116 | NSCaching.md | WN18RR | ✅ | (sans caption) | 000</td> </tr> <tr> <td>WN18RR</td> <td>93,003</td> <t |
| 117 | PNS.md | FB15K | ✅ | (sans caption) | n="2">WN18</th> <th colspan="2">FB15K</th> </tr> <tr> <th>Mea |
| 118 | PNS.md | WN18 | ✅ | (sans caption) | ">Approach</th> <th colspan="2">WN18</th> <th colspan="2">FB15K</th> |
| 119 | RAAKGC.md | FB15k-237 | ✅ | Table 1: Statistics of the datasets use… | 134</td> </tr> <tr> <td>FB15k-237</td> <td>272,115</td> < |
| 120 | RAAKGC.md | FB15k-237_v1 | ✅ | (hors table) | 6: The Hit@10 and MRR of WN18RR_v1 and FB15k-237_v1 under inductive scenario. The optimal v |
| 121 | RAAKGC.md | FB15k-237_v2 | ✅ | (hors table) | ody> </table> Table 18: The results of FB15k-237_v2 dataset. The **boldface** values indica |
| 122 | RAAKGC.md | FB15k-237_v3 | ✅ | (hors table) | ody> </table> Table 19: The results of FB15k-237_v3 dataset. The **boldface** values indica |
| 123 | RAAKGC.md | FB15k-237_v4 | ✅ | (hors table) | ody> </table> Table 20: The results of FB15k-237_v4 dataset. The **boldface** values indica |
| 124 | RAAKGC.md | Wikidata5M-Trans | ✅ | Table 1: Statistics of the datasets use… | 466</td> </tr> <tr> <td>Wikidata5M-Trans</td> <td>20,614,279</td> |
| 125 | RAAKGC.md | WN18RR | ✅ | Table 1: Statistics of the datasets use… | </thead> <tbody> <tr> <td>WN18RR</td> <td>86,835</td> <t |
| 126 | RAAKGC.md | WN18RR_v1 | ✅ | (hors table) | models w./w.o. our RAA framework on the WN18RR_v1 dataset (Teru, Denis, and Hamilton 2020 |
| 127 | RAAKGC.md | WN18RR_v2 | ✅ | (hors table) | ody> </table> Table 14: The results of WN18RR_v2 dataset. The **boldface** values indica |
| 128 | RAAKGC.md | WN18RR_v3 | ✅ | (hors table) | ody> </table> Table 15: The results of WN18RR_v3 dataset. The **boldface** values indica |
| 129 | RAAKGC.md | WN18RR_v4 | ✅ | (hors table) | ody> </table> Table 16: The results of WN18RR_v4 dataset. The **boldface** values indica |
| 130 | RandomCorrupt.md | FB15k | ✅ | Table 1. From there we observe that: (1… | ng></td> </tr> <tr> <td>FB15k</td> <td>0.883</td> <td |
| 131 | RandomCorrupt.md | FB15k-237 | ✅ | Table 1. From there we observe that: (1… | ng></td> </tr> <tr> <td>FB15k-237</td> <td><strong>0.955</strong> |
| 132 | RandomCorrupt.md | FB3M | ✅ | Table 1. From there we observe that: (1… | ng></td> </tr> <tr> <td>FB3M</td> <td>0.475</td> <td |
| 133 | RandomCorrupt.md | WN18 | ✅ | Table 1. From there we observe that: (1… | </thead> <tbody> <tr> <td>WN18</td> <td><strong>0.971</strong> |
| 134 | RandomCorrupt.md | WN18RR | ✅ | Table 1. From there we observe that: (1… | ng></td> </tr> <tr> <td>WN18RR</td> <td>0.843</td> <td |
| 135 | RCWC.md | FB15K | ✅ | Table 1: Statistics of link prediction … | 134</td> </tr> <tr> <td>FB15K</td> <td>14,691</td> <t |
| 136 | RCWC.md | FB15k-237 | ✅ | Table 1: Statistics of link prediction … | 071</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 137 | RCWC.md | WN18 | ✅ | Table 1: Statistics of link prediction … | </thead> <tbody> <tr> <td>WN18</td> <td>40,943</td> <t |
| 138 | RCWC.md | WN18RR | ✅ | Table 1: Statistics of link prediction … | 000</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 139 | ReasonKGE.md | DBPedia15K | ✅ | Table 3: Link prediction results | > <th>Yago3-10</th> <th>DBPedia15K</th> </tr> </thead> <tbody> |
| 140 | ReasonKGE.md | LUBM3U | ✅ | Table 3: Link prediction results | <tr> <th> </th> <th>LUBM3U</th> <th>Yago3-10</th> |
| 141 | ReasonKGE.md | Yago3-10 | ✅ | Table 3: Link prediction results | th> <th>LUBM3U</th> <th>Yago3-10</th> <th>DBPedia15K</th> </ |
| 142 | RUGA.md | FB15K | ✅ | Table 4. Experimental results of variou… | </thead> <tbody> <tr> <td>FB15K</td> <td>14951</td> <td |
| 143 | RUGA.md | YAGO37 | ✅ | Table 4. Experimental results of variou… | 071</td> </tr> <tr> <td>YAGO37</td> <td>123189</td> <t |
| 144 | SANS.md | FB15K-237 | ✅ | Table 1: Comparison of different negati… | <th> </th> <th colspan="2">FB15K-237</th> <th colspan="2">WN18</th> |
| 145 | SANS.md | WN18 | ✅ | Table 1: Comparison of different negati… | >FB15K-237</th> <th colspan="2">WN18</th> <th colspan="2">WN18RR</th |
| 146 | SANS.md | WN18RR | ✅ | Table 1: Comparison of different negati… | n="2">WN18</th> <th colspan="2">WN18RR</th> </tr> <tr> <th>Sco |
| 147 | SelfAdv.md | Countries S1 | ✅ | Table 13: Results of ablation study on … | d>6</td> </tr> <tr> <td>Countries S1</td> <td>500</td> <td>5 |
| 148 | SelfAdv.md | Countries S2 | ✅ | Table 13: Results of ablation study on … | 0.1</td> </tr> <tr> <td>Countries S2</td> <td>500</td> <td>5 |
| 149 | SelfAdv.md | Countries S3 | ✅ | Table 13: Results of ablation study on … | 0.1</td> </tr> <tr> <td>Countries S3</td> <td>500</td> <td>5 |
| 150 | SelfAdv.md | FB15k | ✅ | Table 4: Results of several models eval… | est</th> </tr> <tr> <td>FB15k</td> <td>14,951</td> <t |
| 151 | SelfAdv.md | FB15k-237 | ✅ | Table 4: Results of several models eval… | 000</td> </tr> <tr> <td>FB15k-237</td> <td>14,541</td> <t |
| 152 | SelfAdv.md | WN18 | ✅ | Table 4: Results of several models eval… | 071</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 153 | SelfAdv.md | WN18RR | ✅ | Table 4: Results of several models eval… | 466</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 154 | SelfAdv.md | YAGO3-10 | ✅ | Table 12: The best hyperparameter setti… | <tr> <th></th> <th>YAGO3-10</th> <th></th> <th></th |
| 155 | SNS.md | FB15K | ✅ | Table 3: Link prediction(LP) results: M… | 466</td> </tr> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 156 | SNS.md | FB15K-237 | ✅ | Table 3: Link prediction(LP) results: M… | 000</td> </tr> <tr> <td>FB15K-237</td> <td>14,541</td> <t |
| 157 | SNS.md | FIGHT-HF-23R | ✅ | Table 3: Link prediction(LP) results: M… | 071</td> </tr> <tr> <td>FIGHT-HF-23R</td> <td>90,430</td> <t |
| 158 | SNS.md | WN18 | ✅ | Table 3: Link prediction(LP) results: M… | 134</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 159 | SNS.md | WN18RR | ✅ | Table 3: Link prediction(LP) results: M… | </thead> <tbody> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 160 | SNS.md | YAGO3-10 | ✅ | Table 3: Link prediction(LP) results: M… | 414</td> </tr> <tr> <td>YAGO3-10</td> <td>113,273</td> < |
| 161 | SparseNSG.md | FB15K | ✅ | Table 1 Datasets used in the experiment | </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td |
| 162 | SparseNSG.md | WN18 | ✅ | Table 1 Datasets used in the experiment | 071</td> </tr> <tr> <td>WN18</td> <td>18</td> <td>40 |
| 163 | STC.md | FB15K | ✅ | Table 1: Statistics of datasets | </thead> <tbody> <tr> <td>FB15K</td> <td>1,345</td> <td |
| 164 | TANS.md | FB15k-237 | ✅ | (sans caption) | </tr> <tr> <th colspan="4">FB15k-237 (x10^3)</th> </tr> </thead> <tb |
| 165 | TANS.md | FB15k-237-HL | ✅ | (sans caption) | </thead> <tbody> <tr> <td>FB15k-237-HL</td> <td>38.5</td> <td> |
| 166 | TANS.md | WN18RR | ✅ | (sans caption) | </tr> <tr> <th colspan="4">WN18RR (x10^2)</th> </tr> <tr> |
| 167 | TANS.md | WN18RR-HL | ✅ | (sans caption) | 3.2</td> </tr> <tr> <td>WN18RR-HL</td> <td>11.0</td> <td> |
| 168 | TANS.md | YAGO3-10 | ✅ | (sans caption) | </tr> <tr> <th colspan="4">YAGO3-10 (x10^4)</th> </tr> <tr> |
| 169 | TANS.md | YAGO3-10-HL | ✅ | (sans caption) | 4.2</td> </tr> <tr> <td>YAGO3-10-HL</td> <td>42.0</td> <td> |
| 170 | TruncatedNS.md | D-W15K | ✅ | Table 1. Data statistics of the monolin… | </tr> <tr> <th rowspan="2">D-W15K</th> <th>DB</th> <th>24 |
| 171 | TruncatedNS.md | EN-DE15K | ✅ | Table 3. D-W15K entity alignment result… | </tr> <tr> <th rowspan="2">EN-DE15K</th> <th>EN</th> <th>21 |
| 172 | TuckerDNCaching.md | FB15K | ✅ | (sans caption) | 134</td> </tr> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 173 | TuckerDNCaching.md | FB15K237 | ✅ | (sans caption) | 071</td> </tr> <tr> <td>FB15K237</td> <td>14,541</td> <t |
| 174 | TuckerDNCaching.md | WN18 | ✅ | (sans caption) | </thead> <tbody> <tr> <td>WN18</td> <td>40,943</td> <t |
| 175 | TuckerDNCaching.md | WN18RR | ✅ | (sans caption) | 000</td> </tr> <tr> <td>WN18RR</td> <td>40,943</td> <t |
| 176 | TypeAugmented.md | FB15K | ✅ | Table 3. Link prediction results on FB1… | </thead> <tbody> <tr> <td>FB15K</td> <td>14,951</td> <t |
| 177 | TypeAugmented.md | FB15K-237 | ✅ | Table 3. Link prediction results on FB1… | 071</td> </tr> <tr> <td>FB15K-237</td> <td>14,541</td> <t |
| 178 | TypeAugmented.md | WN18 | ✅ | Table 3. Link prediction results on FB1… | 466</td> </tr> <tr> <td>WN18</td> <td>40,943</td> <t |
| 179 | TypeAugmented.md | YAGO3-10 | ✅ | Table 3. Link prediction results on FB1… | 000</td> </tr> <tr> <td>YAGO3-10</td> <td>123,182</td> < |
| 180 | TypeConstraints.md | DBpedia-Music | ✅ | Table 1. Datasets used in the experimen… | </thead> <tbody> <tr> <td>DBpedia-Music</td> <td>DBpedia 2014</td> |
| 181 | TypeConstraints.md | Freebase-150k | ✅ | Table 1. Datasets used in the experimen… | 383</td> </tr> <tr> <td>Freebase-150k</td> <td>Freebase RDF-Dump</td> |
| 182 | TypeConstraints.md | YAGOc-195k | ✅ | Table 1. Datasets used in the experimen… | 844</td> </tr> <tr> <td>YAGOc-195k</td> <td>YAGO2-Core</td> |
| 183 | Uniform.md | FB15K | ✅ | Table 2: **Statistics of the data sets*… | h>NB. OF PARAMETERS</th> <th>ON FB15K</th> </tr> </thead> <tbody> |
| 184 | Uniform.md | WN | ✅ | Table 3: **Link prediction results.** T… | > <th>DATA SET</th> <th>WN</th> <th>FB15K</th> <th |
