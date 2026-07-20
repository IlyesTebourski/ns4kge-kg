# Rapport-preuve — Validation des *metrics* extraits (NS4KGE)

Corpus : **55 articles** — Source : `Configurations[].Metric` (prompt2) — Validation contre `load_md_tables_only()` (tables uniquement).

## 1. Définitions

| Terme | Définition |
|---|---|
| TP | metric extrait par le KG ET présent dans les tableaux de l'article |
| FP | metric extrait par le KG mais absent des tableaux |
| Candidat FN | metric présent dans une cellule `<table>` mais non extrait |
| Précision | TP / (TP + FP) |
| Recall relatif | TP / (TP + candidats FN en table de résultats) |

**Méthodo (matching) :** metrics normalisées par le prompt (ex. `Mean Rank`→`MR`, `Hit@10`→`Hits@10`, `Acc`→`Accuracy`) donc matching par **alias déterministes** ; `Hits@N`/`Hits@k` générique accepté en précision ; recall cherché dans les blocs `<table>` avec N littéral.

## 2. Résultats globaux

| Indicateur | Valeur |
|---|---|
| Metrics extraits (lignes vérifiées) | 199 |
| Validés (TP) | 192 |
| Non validés (FP) | 7 |
| **Précision (micro)** | **96.5%** |
| Candidats FN en table de résultats | 8 |
| Candidats FN en table de stats (ignorés par le prompt) | 0 |
| **Recall relatif (micro)** | **96.0%** |
| Vocabulaire global de metrics | 18 |

## 3. Analyse des erreurs

### 3.1 Faux positifs (extraits mais absents des tableaux)

| Article | Metric extrait |
|---|---|
| ConceptDriven.md | Accuracy |
| GNDN.md | Accuracy |
| LTS.md | Hits@1 |
| NSCaching.md | Accuracy |
| RUGA.md | Accuracy |
| RUGA.md | MR |
| SparseNSG.md | Accuracy |

### 3.2 Candidats faux négatifs — table de résultats

| Article | Metric | Table | Citation |
|---|---|---|---|
| BatchNS.md | F1 | (sans caption) | <th>Metric</th> <th>Micro-F1</th> <th>Macro-F1</th> </tr |
| dans.md | NDCG | (sans caption) | R</th> <th>H@1</th> <th>NDCG@5</th> <th>MRR</th> <th |
| eTruncatedUNS.md | F1 | (sans caption) | </th> <th>Rec.</th> <th>F1-score</th> </tr> </thead> <tbody> |
| MCNS.md | NDCG | (sans caption) | <th>β</th> <th>MovieLens NDCG</th> <th>Amazon NDCG</th> |
| ReasonKGE.md | Hits@3 | Table 6: Link predictions results for *… | th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> < |
| SelfAdv.md | AUPRC | Table 7: TransE with different negative… | ></th> <th colspan="4">Countries (AUC-PR)</th> </tr> <tr> <th></th> |
| SelfAdv.md | AUROC | Table 9: Experimental results on FB15k … | 7</th> <th colspan="3">Countries (AUC-ROC)</th> </tr> <tr> <th></th> |
| TuckerDNCaching.md | Accuracy | Table 4** Example of negative entities … | colspan="4">(c) Many-to-Many Relations Accuracy</th> </tr> <tr> <th>Epo |

### 3.3 Candidats faux négatifs — table de statistiques (priorité basse)

| Article | Metric | Table | Citation |
|---|---|---|---|

## 4. Preuve détaillée — 199 metrics extraits (192 validés / 7 non)

| # | Article | Metric extrait | Validé | Table | Citation dans le texte |
|---:|---|---|:---:|---|---|
| 1 | AdaptativeNS.md | Hits@1 | ✅ | (sans caption) | </th> <th>MRR</th> <th>H@1</th> <th>H@3</th> <th>H |
| 2 | AdaptativeNS.md | Hits@10 | ✅ | (sans caption) | 1</th> <th>H@3</th> <th>H@10</th> <th>MRR</th> <th>H |
| 3 | AdaptativeNS.md | Hits@3 | ✅ | (sans caption) | R</th> <th>H@1</th> <th>H@3</th> <th>H@10</th> <th> |
| 4 | AdaptativeNS.md | MRR | ✅ | (sans caption) | <tr> <th> </th> <th>MRR</th> <th>H@1</th> <th>H |
| 5 | ADNS.md | Hits@1 | ✅ | Table 3. Evaluation of Negative Samplin… | 42%</td> </tr> <tr> <td>Hit@1: 0%</td> <td>Hit@1: 13.68%</td> |
| 6 | ADNS.md | Hits@10 | ✅ | Table 3. Evaluation of Negative Samplin… | 88%</td> </tr> <tr> <td>Hit@10: 93.53%</td> <td>Hit@10: 94.53% |
| 7 | ADNS.md | Hits@3 | ✅ | Table 3. Evaluation of Negative Samplin… | 15%</td> </tr> <tr> <td>Hit@3: 40.05%</td> <td>Hit@3: 37.31%< |
| 8 | ADNS.md | Hits@5 | ✅ | Table 3. Evaluation of Negative Samplin… | 98%</td> </tr> <tr> <td>Hit@5: 60.95%</td> <td>Hit@5: 59.95%< |
| 9 | ADNS.md | MR | ✅ | Table 3. Evaluation of Negative Samplin… | td rowspan="6">Nations</td> <td>MR: 5</td> <td>MR: 5</td> |
| 10 | ADNS.md | MRR | ✅ | Table 3. Evaluation of Negative Samplin… | : 4</td> </tr> <tr> <td>MRR: 26.96%</td> <td>MRR: 33.79%</t |
| 11 | ASA.md | AP | ✅ | Table 3: Test results on Company. **Hit… | </th> <th>AUC↑</th> <th>AP↑</th> <th>F1↑(0.5)</th> |
| 12 | ASA.md | AUC | ✅ | Table 3: Test results on Company. **Hit… | r> <th>Methods</th> <th>AUC↑</th> <th>AP↑</th> <th> |
| 13 | ASA.md | F1 | ✅ | Table 3: Test results on Company. **Hit… | ↑</th> <th>AP↑</th> <th>F1↑(0.5)</th> <th>AUC↑</th> |
| 14 | ASA.md | Hits@1 | ✅ | (hors table) | e> Table 3: Test results on Company. **Hit@k** is reported as a percentage. <table> |
| 15 | ASA.md | Hits@10 | ✅ | (hors table) | e> Table 3: Test results on Company. **Hit@k** is reported as a percentage. <table> |
| 16 | ASA.md | Hits@30 | ✅ | (hors table) | e> Table 3: Test results on Company. **Hit@k** is reported as a percentage. <table> |
| 17 | ASA.md | MRR | ✅ | (sans caption) | r> <th>Methods</th> <th>MRR↑</th> <th>Hit@1↑</th> < |
| 18 | BatchNS.md | Hits@10 | ✅ | Table 1. Performance of PBG, DeepWalk, … | RR</th> <th>MR</th> <th>Hits@10</th> <th>Memory</th> </tr> |
| 19 | BatchNS.md | MR | ✅ | Table 1. Performance of PBG, DeepWalk, … | c</th> <th>MRR</th> <th>MR</th> <th>Hits@10</th> < |
| 20 | BatchNS.md | MRR | ✅ | Table 1. Performance of PBG, DeepWalk, … | tr> <th>Metric</th> <th>MRR</th> <th>MR</th> <th>Hi |
| 21 | CAKE.md | Hits@1 | ✅ | Table 3, our CANS module significantly … | th> <th>Hits@3</th> <th>Hits@1</th> <th>MR</th> <th>MR |
| 22 | CAKE.md | Hits@10 | ✅ | Table 3, our CANS module significantly … | R</th> <th>MRR</th> <th>Hits@10</th> <th>Hits@3</th> <t |
| 23 | CAKE.md | Hits@3 | ✅ | Table 3, our CANS module significantly … | h> <th>Hits@10</th> <th>Hits@3</th> <th>Hits@1</th> <t |
| 24 | CAKE.md | MR | ✅ | Table 3, our CANS module significantly … | <tr> <th> </th> <th>MR</th> <th>MRR</th> <th>H |
| 25 | CAKE.md | MRR | ✅ | Table 3, our CANS module significantly … | > </th> <th>MR</th> <th>MRR</th> <th>Hits@10</th> < |
| 26 | CANS.md | Hits@10 | ✅ | (sans caption) | an="2">MRR</th> <th colspan="2">Hits@10 (%)</th> </tr> <tr> <th |
| 27 | CANS.md | MR | ✅ | (sans caption) | ">FB15K-N1</th> <th colspan="2">Mean Rank</th> <th colspan="2">MRR</th> |
| 28 | CANS.md | MRR | ✅ | (sans caption) | >Mean Rank</th> <th colspan="2">MRR</th> <th colspan="2">Hits@10 (% |
| 29 | CCS.md | Hits@1 | ✅ | Table 8. Experimental results on the FB… | R</th> <th>MRR</th> <th>Hits@1</th> <th>Hits@3</th> <t |
| 30 | CCS.md | Hits@10 | ✅ | Table 6. Results of the performance of … | R</th> <th>MRR</th> <th>Hits@10</th> <th>MR</th> <th>MR |
| 31 | CCS.md | Hits@3 | ✅ | Table 8. Experimental results on the FB… | th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> </tr> |
| 32 | CCS.md | MR | ✅ | Table 6. Results of the performance of … | 237</th> </tr> <tr> <th>MR</th> <th>MRR</th> <th>H |
| 33 | CCS.md | MRR | ✅ | Table 6. Results of the performance of … | <tr> <th>MR</th> <th>MRR</th> <th>Hits@10</th> < |
| 34 | ConceptDriven.md | Accuracy | ❌ | — | — |
| 35 | ConceptDriven.md | Hits@1 | ✅ | (sans caption) | d</th> <th>MRR↑</th> <th>MRR+%</th> <th>H@1↑</th> <th>H@3↑</th> <th>H@10↑</th> <th> |
| 36 | ConceptDriven.md | Hits@10 | ✅ | (sans caption) | +%</th> <th>H@1↑</th> <th>H@3↑</th> <th>H@10↑</th> <th>MRR↑</th> <th>MRR+%</th> <th> |
| 37 | ConceptDriven.md | Hits@3 | ✅ | (sans caption) | ↑</th> <th>MRR+%</th> <th>H@1↑</th> <th>H@3↑</th> <th>H@10↑</th> <th>MRR↑</th> <th> |
| 38 | ConceptDriven.md | MRR | ✅ | (sans caption) | 237</th> </tr> <tr> <th>Method</th> <th>MRR↑</th> <th>MRR+%</th> <th>H@1↑</th> <th> |
| 39 | CondConstraints.md | Hits@10 | ✅ | Table 1, while those for MUTAG can be f… | R</th> <th>MRR</th> <th>Hits@10</th> <th>FN</th> </tr> </ |
| 40 | CondConstraints.md | MR | ✅ | Table 1, while those for MUTAG can be f… | <th>neg ratio</th> <th>MR</th> <th>MRR</th> <th>H |
| 41 | CondConstraints.md | MRR | ✅ | Table 1, while those for MUTAG can be f… | io</th> <th>MR</th> <th>MRR</th> <th>Hits@10</th> < |
| 42 | dans.md | Hits@1 | ✅ | (sans caption) | d</th> <th>MRR</th> <th>H@1</th> <th>NDCG@5</th> <t |
| 43 | dans.md | MRR | ✅ | (sans caption) | tr> <th>method</th> <th>MRR</th> <th>H@1</th> <th>N |
| 44 | dans.md | NDCG@5 | ✅ | (sans caption) | R</th> <th>H@1</th> <th>NDCG@5</th> <th>MRR</th> <th>H |
| 45 | DeMix.md | Hits@1 | ✅ | (sans caption) | th> <th>Hits@3</th> <th>Hits@1</th> <th>MRR</th> <th>H |
| 46 | DeMix.md | Hits@10 | ✅ | Table 2.** Link prediction results for … | </th> <th>MRR</th> <th>Hits@10</th> <th>MRR</th> <th>H |
| 47 | DeMix.md | Hits@3 | ✅ | (sans caption) | h> <th>Hits@10</th> <th>Hits@3</th> <th>Hits@1</th> <t |
| 48 | DeMix.md | MRR | ✅ | Table 2.** Link prediction results for … | <tr> <th> </th> <th>MRR</th> <th>Hits@10</th> < |
| 49 | DHNS.md | Hits@1 | ✅ | Table 3. Evaluation results (%) of <mar… | <tr> <th>MRR</th> <th>H1</th> <th>H3</th> <th>H1 |
| 50 | DHNS.md | Hits@10 | ✅ | Table 3. Evaluation results (%) of <mar… | H1</th> <th>H3</th> <th>H10</th> <th>MRR</th> <th>H |
| 51 | DHNS.md | Hits@3 | ✅ | Table 3. Evaluation results (%) of <mar… | RR</th> <th>H1</th> <th>H3</th> <th>H10</th> <th>M |
| 52 | DHNS.md | MRR | ✅ | Table 3. Evaluation results (%) of <mar… | G-W</th> </tr> <tr> <th>MRR</th> <th>H1</th> <th>H3 |
| 53 | DMNS.md | MAP | ✅ | Table 3: Evaluation of link prediction … | <tr> <th> </th> <th>MAP</th> <th>NDCG</th> <th> |
| 54 | DMNS.md | NDCG | ✅ | Table 3: Evaluation of link prediction … | </th> <th>MAP</th> <th>NDCG</th> <th>MAP</th> <th>N |
| 55 | DNS.md | Hits@1 | ✅ | (hors table) | Base completion performance comparison. H@n denotes Hits@n. We report *filtered* Me |
| 56 | DNS.md | Hits@10 | ✅ | (hors table) | Base completion performance comparison. H@n denotes Hits@n. We report *filtered* Me |
| 57 | DNS.md | MRR | ✅ | (hors table) | @n denotes Hits@n. We report *filtered* Mean Reciprocal Rank (MRR), *filtered* Hits@10 and *filtered |
| 58 | DomainNS.md | Hits@10 | ✅ | (hors table) | diction results on two datasets. Higher Hits@10 or lower Mean Rank indicates better per |
| 59 | DomainNS.md | MR | ✅ | (hors table) | n two datasets. Higher Hits@10 or lower Mean Rank indicates better performance. Following |
| 60 | EANS.md | Hits@10 | ✅ | (sans caption) | R</th> <th>MRR</th> <th>Hit@10</th> <th>MR</th> <th>MR |
| 61 | EANS.md | MR | ✅ | (sans caption) | 8RR</th> </tr> <tr> <th>MR</th> <th>MRR</th> <th>H |
| 62 | EANS.md | MRR | ✅ | (sans caption) | <tr> <th>MR</th> <th>MRR</th> <th>Hit@10</th> <t |
| 63 | ERDNS.md | Hits@1 | ✅ | (sans caption) | <tr> <th>MRR</th> <th>Hits@1</th> <th>Hits@3</th> <t |
| 64 | ERDNS.md | Hits@10 | ✅ | (sans caption) | th> <th>Hits@3</th> <th>Hits@10</th> <th>MRR</th> <th>H |
| 65 | ERDNS.md | Hits@3 | ✅ | (sans caption) | th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> < |
| 66 | ERDNS.md | MRR | ✅ | (sans caption) | lEx</th> </tr> <tr> <th>MRR</th> <th>Hits@1</th> <t |
| 67 | eTruncatedUNS.md | Hits@1 | ✅ | Table 2: Result comparison on entity al… | -YG</th> </tr> <tr> <th>Hits@1</th> <th>Hits@10</th> < |
| 68 | eTruncatedUNS.md | Hits@10 | ✅ | Table 2: Result comparison on entity al… | tr> <th>Hits@1</th> <th>Hits@10</th> <th>MRR</th> <th>H |
| 69 | eTruncatedUNS.md | MRR | ✅ | Table 2: Result comparison on entity al… | h> <th>Hits@10</th> <th>MRR</th> <th>Hits@1</th> <t |
| 70 | GHN.md | Hits@1 | ✅ | (hors table) | Following previous work, **MRR** and **Hits@k** are reported under the filtered setti |
| 71 | GHN.md | Hits@10 | ✅ | (hors table) | Following previous work, **MRR** and **Hits@k** are reported under the filtered setti |
| 72 | GHN.md | Hits@3 | ✅ | (hors table) | Following previous work, **MRR** and **Hits@k** are reported under the filtered setti |
| 73 | GHN.md | MRR | ✅ | (hors table) | ed training. Following previous work, **MRR** and **Hits@k** are reported under the |
| 74 | GibbsNS.md | Hits@1 | ✅ | Table 3. Capacity for handling complex … | </th> <th>MRR</th> <th>H@1</th> <th>H@3</th> <th>H |
| 75 | GibbsNS.md | Hits@10 | ✅ | Table 3. Capacity for handling complex … | 1</th> <th>H@3</th> <th>H@10</th> <th>MRR</th> <th>H |
| 76 | GibbsNS.md | Hits@3 | ✅ | Table 3. Capacity for handling complex … | R</th> <th>H@1</th> <th>H@3</th> <th>H@10</th> <th> |
| 77 | GibbsNS.md | MR | ✅ | (sans caption) | h> </th> <th> </th> <th>MR</th> <th>MRR</th> <th>H |
| 78 | GibbsNS.md | MRR | ✅ | Table 3. Capacity for handling complex … | <tr> <th> </th> <th>MRR</th> <th>H@1</th> <th>H |
| 79 | GNDN.md | Accuracy | ❌ | — | — |
| 80 | GNDN.md | Hits@10 | ✅ | (sans caption) | <tr> <th>MRR</th> <th>HIT@10</th> <th>MRR</th> <th>H |
| 81 | GNDN.md | MRR | ✅ | (sans caption) | 15k</th> </tr> <tr> <th>MRR</th> <th>HIT@10</th> <t |
| 82 | GNS.md | Accuracy | ✅ | (hors table) | able 2: Triple classification outcomes (accuracy, standard deviation) <table> <thead> |
| 83 | GraphGAN.md | Accuracy | ✅ | (hors table) | </tr> </tbody> </table> Table 1: Accuracy and Macro-F1 on arXiv-AstroPh and arXiv |
| 84 | GraphGAN.md | F1 | ✅ | (hors table) | > </table> Table 1: Accuracy and Macro-F1 on arXiv-AstroPh and arXiv-GrQc in link |
| 85 | HaSa.md | Hits@1 | ✅ | (sans caption) | </th> <th>MRR↑</th> <th>Hit@1↑</th> <th>Hit@3↑</th> < |
| 86 | HaSa.md | Hits@10 | ✅ | (sans caption) | th> <th>Hit@3↑</th> <th>Hit@10↑</th> <th>MR↓</th> <th> |
| 87 | HaSa.md | Hits@3 | ✅ | (sans caption) | th> <th>Hit@1↑</th> <th>Hit@3↑</th> <th>Hit@10↑</th> |
| 88 | HaSa.md | MR | ✅ | (sans caption) | 237</th> </tr> <tr> <th>MR↓</th> <th>MRR↑</th> <th |
| 89 | HaSa.md | MRR | ✅ | (sans caption) | <tr> <th>MR↓</th> <th>MRR↑</th> <th>Hit@1↑</th> < |
| 90 | HTENS.md | Hits@10 | ✅ | (sans caption) | </th> <th>MRR</th> <th>H@10</th> <th>MRR</th> <th>H |
| 91 | HTENS.md | MRR | ✅ | (sans caption) | h> </th> <th> </th> <th>MRR</th> <th>H@10</th> <th> |
| 92 | IGAN.md | Accuracy | ✅ | (hors table) | Evaluation results about classification accuracy on triplets classification(%). <table> |
| 93 | IGAN.md | Hits@10 | ✅ | (sans caption) | <th>Mean Rank</th> <th>Hits@10 (%)</th> <th>Mean Rank</th> |
| 94 | IGAN.md | MR | ✅ | (sans caption) | <tr> <th> </th> <th>Mean Rank</th> <th>Hits@10 (%)</th> |
| 95 | KBGAN.md | Hits@10 | ✅ | (sans caption) | <tr> <th>MRR</th> <th>H@10</th> <th>MRR</th> <th>H |
| 96 | KBGAN.md | MRR | ✅ | (sans caption) | 8RR</th> </tr> <tr> <th>MRR</th> <th>H@10</th> <th> |
| 97 | KSGAN.md | Hits@10 | ✅ | (sans caption) | <td colspan="5">FB15k237 validation Hits@10</td> </tr> <tr> <th>Siz |
| 98 | KSGAN.md | MRR | ✅ | (sans caption) | <td colspan="5">FB15k237 validation MRR</td> </tr> <tr> <th>Siz |
| 99 | LAS.md | Hits@10 | ✅ | (sans caption) | RR</th> <th>MR</th> <th>H@10</th> <th>MRR</th> <th>M |
| 100 | LAS.md | MR | ✅ | (sans caption) | <tr> <th>MRR</th> <th>MR</th> <th>H@10</th> <th> |
| 101 | LAS.md | MRR | ✅ | (sans caption) | 8RR</th> </tr> <tr> <th>MRR</th> <th>MR</th> <th>H@ |
| 102 | LEMON.md | Hits@10 | ✅ | Table 3: Results of KGE models without … | </th> <th>MRR</th> <th>H@10</th> <th>MRR</th> <th>H |
| 103 | LEMON.md | MRR | ✅ | Table 3: Results of KGE models without … | <tr> <th> </th> <th>MRR</th> <th>H@10</th> <th> |
| 104 | Localcognitive.md | Hits@1 | ✅ | Table 4: Link prediction results on WN1… | th> <th>Hits@3</th> <th>Hits@1</th> <th>MR</th> <th>MR |
| 105 | Localcognitive.md | Hits@10 | ✅ | Table 4: Link prediction results on WN1… | R</th> <th>MRR</th> <th>Hits@10</th> <th>Hits@3</th> <t |
| 106 | Localcognitive.md | Hits@3 | ✅ | Table 4: Link prediction results on WN1… | h> <th>Hits@10</th> <th>Hits@3</th> <th>Hits@1</th> <t |
| 107 | Localcognitive.md | MR | ✅ | Table 4: Link prediction results on WN1… | 15k</th> </tr> <tr> <th>MR</th> <th>MRR</th> <th>H |
| 108 | Localcognitive.md | MRR | ✅ | Table 4: Link prediction results on WN1… | <tr> <th>MR</th> <th>MRR</th> <th>Hits@10</th> < |
| 109 | LTS.md | Hits@1 | ❌ | — | — |
| 110 | LTS.md | Hits@10 | ✅ | (sans caption) | 256</td> </tr> <tr> <td>Hits@10/%</td> <td>100</td> <td |
| 111 | LTS.md | MR | ✅ | (sans caption) | <td rowspan="2">FB15K</td> <td>Mean Rank</td> <td>100</td> <td>0 |
| 112 | M2ixKG.md | Hits@10 | ✅ | (sans caption) | s</th> <th>MRR</th> <th>Hits@10(%)</th> <th>MRR</th> <t |
| 113 | M2ixKG.md | MRR | ✅ | (sans caption) | r> <th>Metrics</th> <th>MRR</th> <th>Hits@10(%)</th> |
| 114 | MCNS.md | AUC | ✅ | Table 4: Micro-F1 scores for multi-labe… | tbody> <tr> <td rowspan="9">AUC</td> <td>$Deg^{0.75}$</td> |
| 115 | MCNS.md | F1 | ✅ | (hors table) | </table> Table 4 summarizes the Micro-F1 result on the BlogCatalog dataset. MCNS |
| 116 | MCNS.md | Hits@30 | ✅ | Table 3: The results of link prediction… | </tr> <tr> <td rowspan="9">Hits@30</td> <td>$Deg^{0.75}$</td> |
| 117 | MCNS.md | MRR | ✅ | Table 3: The results of link prediction… | tbody> <tr> <td rowspan="9">MRR</td> <td>$Deg^{0.75}$</td> |
| 118 | MDNCaching.md | Hits@10 | ✅ | (sans caption) | RR</th> <th>MR</th> <th>Hits@10</th> <th>MRR</th> <th>M |
| 119 | MDNCaching.md | MR | ✅ | (hors table) | FB15K237 datasets. Note that results of MR and results for TransD and ComplEx embe |
| 120 | MDNCaching.md | MRR | ✅ | (sans caption) | 237</th> </tr> <tr> <th>MRR</th> <th>MR</th> <th>Hi |
| 121 | NMiss.md | Hits@10 | ✅ | (sans caption) | </th> <th>MRR</th> <th>HITS@10</th> <th>neg. sampling</th> |
| 122 | NMiss.md | MRR | ✅ | (sans caption) | <tr> <th> </th> <th>MRR</th> <th>HITS@10</th> < |
| 123 | NoiGAN.md | AUC | ✅ | Table 3: Evaluation Results on Knowledg… | <th colspan="2">Metric</th> <th>AUC</th> <th>Spe</th> <th>A |
| 124 | NoiGAN.md | Hits@1 | ✅ | Table 4: Examples of Noisy Triples and … | </th> <th>MRR</th> <th>H@1</th> <th>H@3</th> <th>H |
| 125 | NoiGAN.md | Hits@10 | ✅ | Table 4: Examples of Noisy Triples and … | 1</th> <th>H@3</th> <th>H@10</th> <th>MRR</th> <th>H |
| 126 | NoiGAN.md | Hits@3 | ✅ | Table 4: Examples of Noisy Triples and … | R</th> <th>H@1</th> <th>H@3</th> <th>H@10</th> <th> |
| 127 | NoiGAN.md | MRR | ✅ | Table 4: Examples of Noisy Triples and … | <tr> <th> </th> <th>MRR</th> <th>H@1</th> <th>H |
| 128 | NoiGAN.md | Spe | ✅ | Table 3: Evaluation Results on Knowledg… | c</th> <th>AUC</th> <th>Spe</th> <th>AUC</th> <th>S |
| 129 | NSCaching.md | Accuracy | ❌ | — | — |
| 130 | NSCaching.md | Hits@10 | ✅ | (sans caption) | RR</th> <th>MR</th> <th>Hit@10</th> <th>MRR</th> <th>M |
| 131 | NSCaching.md | MR | ✅ | (sans caption) | </th> <th>MRR</th> <th>MR</th> <th>Hit@10</th> <t |
| 132 | NSCaching.md | MRR | ✅ | (sans caption) | h> </th> <th> </th> <th>MRR</th> <th>MR</th> <th>Hi |
| 133 | PNS.md | Hits@10 | ✅ | (sans caption) | <th>Mean Rank</th> <th>Hits@10</th> <th>Mean Rank</th> |
| 134 | PNS.md | MR | ✅ | (sans caption) | 15K</th> </tr> <tr> <th>Mean Rank</th> <th>Hits@10</th> < |
| 135 | RAAKGC.md | Hits@1 | ✅ | Table 4. | /thead> <tbody> <tr> <td>(h1, r1)</td> <td>(-5, -5)</td> |
| 136 | RAAKGC.md | Hits@10 | ✅ | Table 3: Results of adding different ta… | /th> <th>Hit@3</th> <th>Hit@10</th> <th>MRR</th> <th>H |
| 137 | RAAKGC.md | Hits@3 | ✅ | Table 4. | 0)</td> </tr> <tr> <td>(h3, r1)</td> <td>(10, 15)</td> |
| 138 | RAAKGC.md | MRR | ✅ | Table 3: Results of adding different ta… | ans</th> </tr> <tr> <th>MRR</th> <th>Hit@1</th> <th |
| 139 | RandomCorrupt.md | Hits@1 | ✅ | Table 1. From there we observe that: (1… | an="2">MRR</th> <th colspan="2">Hits@1</th> <th colspan="2">MRR</th> |
| 140 | RandomCorrupt.md | MRR | ✅ | Table 1. From there we observe that: (1… | <th> </th> <th colspan="2">MRR</th> <th colspan="2">Hits@1</th |
| 141 | RCWC.md | Hits@1 | ✅ | (sans caption) | R</th> <th>MRR</th> <th>H@1</th> <th>H@3</th> <th>H |
| 142 | RCWC.md | Hits@10 | ✅ | (sans caption) | 1</th> <th>H@3</th> <th>H@10</th> <th>MR</th> <th>MR |
| 143 | RCWC.md | Hits@3 | ✅ | (sans caption) | R</th> <th>H@1</th> <th>H@3</th> <th>H@10</th> <th> |
| 144 | RCWC.md | MR | ✅ | (sans caption) | <tr> <th> </th> <th>MR</th> <th>MRR</th> <th>H |
| 145 | RCWC.md | MRR | ✅ | (sans caption) | > </th> <th>MR</th> <th>MRR</th> <th>H@1</th> <th>H |
| 146 | ReasonKGE.md | Hits@1 | ✅ | (sans caption) | </th> <th>MRR</th> <th>Hits@1</th> <th>Hits@10</th> < |
| 147 | ReasonKGE.md | Hits@10 | ✅ | (sans caption) | th> <th>Hits@1</th> <th>Hits@10</th> <th>MRR</th> <th>H |
| 148 | ReasonKGE.md | MRR | ✅ | (sans caption) | h> </th> <th> </th> <th>MRR</th> <th>Hits@1</th> <t |
| 149 | RUGA.md | Accuracy | ❌ | — | — |
| 150 | RUGA.md | Hits@1 | ✅ | (sans caption) | an="2">MED</th> <th colspan="4">HITS@N</th> <th rowspan="2">MRR</th> |
| 151 | RUGA.md | Hits@10 | ✅ | (sans caption) | an="2">MED</th> <th colspan="4">HITS@N</th> <th rowspan="2">MRR</th> |
| 152 | RUGA.md | Hits@3 | ✅ | (sans caption) | an="2">MED</th> <th colspan="4">HITS@N</th> <th rowspan="2">MRR</th> |
| 153 | RUGA.md | Hits@5 | ✅ | (sans caption) | an="2">MED</th> <th colspan="4">HITS@N</th> <th rowspan="2">MRR</th> |
| 154 | RUGA.md | MR | ❌ | — | — |
| 155 | RUGA.md | MRR | ✅ | (sans caption) | </tr> <tr> <th rowspan="2">MRR</th> <th rowspan="2">MED</th> |
| 156 | SANS.md | Hits@10 | ✅ | Table 1: Comparison of different negati… | <th>Algorithm</th> <th>Hit@10 (%)</th> <th>MRR</th> < |
| 157 | SANS.md | MRR | ✅ | Table 1: Comparison of different negati… | <th>Hit@10 (%)</th> <th>MRR</th> <th>Hit@10 (%)</th> |
| 158 | SelfAdv.md | AUC | ✅ | Table 7: TransE with different negative… | ></th> <th colspan="4">Countries (AUC-PR)</th> </tr> <tr> <th></th> |
| 159 | SelfAdv.md | Hits@1 | ✅ | Table 5: Results of several models eval… | th>MR</th> <th>MRR</th> <th>H@1</th> <th>H@3</th> <th>H@10< |
| 160 | SelfAdv.md | Hits@10 | ✅ | Table 5: Results of several models eval… | h>H@1</th> <th>H@3</th> <th>H@10</th> <th>MR</th> <th>MRR</t |
| 161 | SelfAdv.md | Hits@3 | ✅ | Table 5: Results of several models eval… | h>MRR</th> <th>H@1</th> <th>H@3</th> <th>H@10</th> <th>MR</ |
| 162 | SelfAdv.md | MR | ✅ | Table 5: Results of several models eval… | </tr> <tr> <th></th> <th>MR</th> <th>MRR</th> <th>H@1</ |
| 163 | SelfAdv.md | MRR | ✅ | Table 5: Results of several models eval… | <th></th> <th>MR</th> <th>MRR</th> <th>H@1</th> <th>H@3</ |
| 164 | SNS.md | Hits@1 | ✅ | (sans caption) | /th> <th>hit@3</th> <th>hit@1</th> <th>MRR</th> <th>h |
| 165 | SNS.md | Hits@10 | ✅ | (sans caption) | <tr> <th>MRR</th> <th>hit@10</th> <th>hit@3</th> <th |
| 166 | SNS.md | Hits@3 | ✅ | (sans caption) | th> <th>hit@10</th> <th>hit@3</th> <th>hit@1</th> <th |
| 167 | SNS.md | MRR | ✅ | (hors table) | Table 3: Link prediction(LP) results: MRR, and Hit@z of different negative sampli |
| 168 | SparseNSG.md | Accuracy | ❌ | — | — |
| 169 | SparseNSG.md | Hits@10 | ✅ | Table 4** Comparison of relationship pr… | ">MeanRank</th> <th colspan="2">Hit@10(%)</th> <th colspan="2">MRR</th |
| 170 | SparseNSG.md | Hits@3 | ✅ | Table 5** Comparison of the results of … | ">MeanRank</th> <th colspan="2">Hit@3(%)</th> <th colspan="2">MeanRan |
| 171 | SparseNSG.md | MR | ✅ | Table 4** Comparison of relationship pr… | an="2">MRR</th> <th colspan="2">MeanRank</th> <th colspan="2">Hit@10(%)< |
| 172 | SparseNSG.md | MRR | ✅ | Table 4** Comparison of relationship pr… | <th> </th> <th colspan="2">MRR</th> <th colspan="2">MeanRank</ |
| 173 | STC.md | Accuracy | ✅ | (sans caption) | r> <th>Methods</th> <th>Accuracy(%)</th> </tr> </thead> <tbody> |
| 174 | STC.md | Hits@1 | ✅ | Table 4: Evaluation results on long-tai… | >Mean Rank</th> <th colspan="2">Hits@1(%)</th> </tr> <tr> <th> |
| 175 | STC.md | Hits@10 | ✅ | Table 3: Evaluation results on relation… | >Mean Rank</th> <th colspan="2">Hits@10(%)</th> </tr> <tr> <th> |
| 176 | STC.md | MR | ✅ | Table 3: Evaluation results on relation… | "2">Metric</th> <th colspan="2">Mean Rank</th> <th colspan="2">Hits@10(%) |
| 177 | TANS.md | Hits@1 | ✅ | Table 6: Results on WN18RR. | an="2">MRR</th> <th colspan="2">H@1</th> <th colspan="2">H@3</th> |
| 178 | TANS.md | Hits@10 | ✅ | Table 6: Results on WN18RR. | an="2">H@3</th> <th colspan="2">H@10</th> <th rowspan="2">γ</th> |
| 179 | TANS.md | Hits@3 | ✅ | Table 6: Results on WN18RR. | an="2">H@1</th> <th colspan="2">H@3</th> <th colspan="2">H@10</th> |
| 180 | TANS.md | MRR | ✅ | Table 1: The characteristics of each sm… | <tr> <th colspan="7">FB15k-237 (MRR)</th> </tr> </thead> <tbody> |
| 181 | TruncatedNS.md | Hits@1 | ✅ | Table 4. EN-DE15K entity alignment resu… | <tr> <th>Model</th> <th>Hits@1</th> <th>Hits@5</th> <t |
| 182 | TruncatedNS.md | Hits@10 | ✅ | Table 4. EN-DE15K entity alignment resu… | th> <th>Hits@5</th> <th>Hits@10</th> <th>Hits@50</th> < |
| 183 | TruncatedNS.md | Hits@5 | ✅ | Table 4. EN-DE15K entity alignment resu… | th> <th>Hits@1</th> <th>Hits@5</th> <th>Hits@10</th> < |
| 184 | TruncatedNS.md | Hits@50 | ✅ | Table 4. EN-DE15K entity alignment resu… | h> <th>Hits@10</th> <th>Hits@50</th> <th>MRR</th> <th>M |
| 185 | TruncatedNS.md | MR | ✅ | Table 4. EN-DE15K entity alignment resu… | 0</th> <th>MRR</th> <th>MR</th> </tr> </thead> <tbody> |
| 186 | TruncatedNS.md | MRR | ✅ | Table 4. EN-DE15K entity alignment resu… | h> <th>Hits@50</th> <th>MRR</th> <th>MR</th> </tr> </ |
| 187 | TuckerDNCaching.md | Hits@1 | ✅ | (hors table) | </table> Table 5** Comparison of MRR, Hits@1, Hits@3, Hits@10 on WN18RR and FB15K237 |
| 188 | TuckerDNCaching.md | Hits@10 | ✅ | Table 4** Example of negative entities … | ations</th> <th colspan="2">(b) Hits@10 for Many-to-Many Relations</th> |
| 189 | TuckerDNCaching.md | Hits@3 | ✅ | (hors table) | > Table 5** Comparison of MRR, Hits@1, Hits@3, Hits@10 on WN18RR and FB15K237 dataset |
| 190 | TuckerDNCaching.md | MR | ✅ | Table 6 continued | </th> <th>MRR</th> <th>MR</th> <th>Hits@10</th> < |
| 191 | TuckerDNCaching.md | MRR | ✅ | Table 4** Example of negative entities … | d> <tr> <th colspan="2">(a) MRR for Many-to-Many Relations</th> |
| 192 | TypeAugmented.md | Hits@1 | ✅ | Table 4. Link prediction results on WN1… | <tr> <th>MRR</th> <th>Hits@1</th> <th>Hits@3</th> <t |
| 193 | TypeAugmented.md | Hits@10 | ✅ | Table 4. Link prediction results on WN1… | th> <th>Hits@3</th> <th>Hits@10</th> <th>MRR</th> <th>H |
| 194 | TypeAugmented.md | Hits@3 | ✅ | Table 4. Link prediction results on WN1… | th> <th>Hits@1</th> <th>Hits@3</th> <th>Hits@10</th> < |
| 195 | TypeAugmented.md | MRR | ✅ | Table 4. Link prediction results on WN1… | 237</th> </tr> <tr> <th>MRR</th> <th>Hits@1</th> <t |
| 196 | TypeConstraints.md | AUPRC | ✅ | (hors table) | ody> </table> Table 2.** Comparison of AUPRC and AUROC result for RESCAL with and wi |
| 197 | TypeConstraints.md | AUROC | ✅ | (hors table) | le> Table 2.** Comparison of AUPRC and AUROC result for RESCAL with and without expl |
| 198 | Uniform.md | Hits@10 | ✅ | Table 4: **Detailed results by category… | >MEAN RANK</th> <th colspan="2">HITS@10 (%)</th> <th colspan="2">MEAN R |
| 199 | Uniform.md | MR | ✅ | Table 4: **Detailed results by category… | </tr> <tr> <th colspan="2">MEAN RANK</th> <th colspan="2">HITS@10 (% |
