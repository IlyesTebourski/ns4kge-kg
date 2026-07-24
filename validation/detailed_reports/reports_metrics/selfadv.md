# Metrics — SelfAdv.md

**Titre :** RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space

| Metrique | Valeur |
|---|---|
| Metrics extraites trouvees dans les tables (TP) | 6 |
| Extraites NON trouvees (FP) | 0 |
| **Precision** | **100%** |
| Candidats faux negatifs (table resultats) | 2 |
| Candidats en table de stats (priorite basse) | 0 |
| Recall BRUT (avant adjudication) | 75% |
| **Recall relatif (adjuge)** | **86%** |

## Precision — metrics extraites par le KG

| Metric extraite | Dans les tables ? | Table | Extrait |
|---|:---:|---|---|
| AUC | ✅ oui | Table 7: TransE with different negative sampling techniques. The results in first 2 rows are taken from (Cai  (Cai & Wang, 2017), where KBGAN uses a ComplEx negative sample generator. | ></th> <th colspan="4">Countries (AUC-PR)</th> </tr> <tr> <th></th> |
| Hits@1 | ✅ oui | Table 5: Results of several models evaluated on the FB15k-237 and WN18RR datasets. Results of [♥] are taken from (Nguyen et al., 2017). Other results are taken from (Dettmers et al., 2017). | th>MR</th> <th>MRR</th> <th>H@1</th> <th>H@3</th> <th>H@10< |
| Hits@10 | ✅ oui | Table 5: Results of several models evaluated on the FB15k-237 and WN18RR datasets. Results of [♥] are taken from (Nguyen et al., 2017). Other results are taken from (Dettmers et al., 2017). | h>H@1</th> <th>H@3</th> <th>H@10</th> <th>MR</th> <th>MRR</t |
| Hits@3 | ✅ oui | Table 5: Results of several models evaluated on the FB15k-237 and WN18RR datasets. Results of [♥] are taken from (Nguyen et al., 2017). Other results are taken from (Dettmers et al., 2017). | h>MRR</th> <th>H@1</th> <th>H@3</th> <th>H@10</th> <th>MR</ |
| MR | ✅ oui | Table 5: Results of several models evaluated on the FB15k-237 and WN18RR datasets. Results of [♥] are taken from (Nguyen et al., 2017). Other results are taken from (Dettmers et al., 2017). | </tr> <tr> <th></th> <th>MR</th> <th>MRR</th> <th>H@1</ |
| MRR | ✅ oui | Table 5: Results of several models evaluated on the FB15k-237 and WN18RR datasets. Results of [♥] are taken from (Nguyen et al., 2017). Other results are taken from (Dettmers et al., 2017). | <th></th> <th>MR</th> <th>MRR</th> <th>H@1</th> <th>H@3</ |

## Recall — metrics dans les tables mais NON extraites

| Metric | Table | Extrait |
|---|---|---|
| AUPRC | Table 7: TransE with different negative sampling techniques. The results in first 2 rows are taken from (Cai  (Cai & Wang, 2017), where KBGAN uses a ComplEx negative sample generator. | ></th> <th colspan="4">Countries (AUC-PR)</th> </tr> <tr> <th></th> |
| AUROC | Table 9: Experimental results on FB15k by relation category. The first three rows are taken from (He et al., 2015). The rest of the results are from RotatE trained with the self-adversarial negative sampling technique. | 7</th> <th colspan="3">Countries (AUC-ROC)</th> </tr> <tr> <th></th> |