# Synthèse validation RECALL — les 10 objets (adjudication terminée 2026-07-22)

Méthodo : le script génère les candidats FN automatiquement (matcher déterministe,
règle de casse homogène + mot-catégorie requis en recall) ; chaque candidat est
adjugé à la main (verdict `miss` = vrai oubli / `fp` = faux flag, justifié, tracé
dans `recall_checks/<entité>_recall_check.csv` et injecté dans les
`RECALL_VERDICTS` du validateur — chiffres régénérables en relançant les scripts).

- **Recall BRUT** = script seul, tous candidats comptés comme oublis (toujours
  réaffiché à chaque run, jamais perdu).
- **Recall FINAL (adjugé)** = trouvés / (trouvés + vrais FN).

| # | Objet | Précision | Recall BRUT | Candidats | Vrais FN | FP écartés | **Recall FINAL** |
|--:|---|:---:|:---:|---:|---:|---:|:---:|
| 1 | Datasets | 98.9% | 97.8% | 4 | 0 | 4 | **100%** |
| 2 | Metrics | 96.5% | 96.0% | 8 | 6 | 2 | **97.0%** |
| 3 | KGE models — évalués | 94.4% | 93.6% | 22 | 11 | 11 | **96.7%** |
| 4 | KGE models — mentionnés | 97.9% | 82.1% | 50 | 4 | 46 | **98.3%** |
| 5 | NS methods — évalués | 93.1% | 85.2% | 33 | 1 | 32 | **99.5%** |
| 6 | NS methods — mentionnés | 92.0% | 64.1% | 71 | 15 | 56 | **89.4%** |
| 7 | Hardware | 94.1% (vérifiée) | 100% | 0 | 0 | 0 | **100%** |
| 8 | Optimizer | 97.4% | 79.2% | 10 | 2 | 8 | **95.0%** |
| 9 | LossFunction | 84.3% | 67.3% | 34 | 7 | 27 | **90.9%** |
| 10 | Task | 95.5% | 76.2% | 20 | 4 | 16 | **94.1%** |

**Total : 253 candidats adjugés → 50 vrais FN, 203 faux flags.**

## Vrais FN par objet (résumé)

- **Metrics (6)** : F1 (batchns, etruncateduns), NDCG (mcns), Hits@3 (reasonkge),
  AUC-ROC (selfadv), Accuracy (tuckerdncaching) — métriques rapportées dans des
  tables de résultats, non extraites.
- **KGE évalués (11)** : lignes de baselines dans des tables de résultats non
  extraites — domainns (KG2E, NTN, SE, Unstructured), igan (SE, SME, Unstructured),
  lts (LFM, SME), selfadv (SE), stc (TKRL).
- **KGE mentionnés (4)** : NTN (ccs, gndn), GraphSAGE (dmns), TKRL (htens).
- **NS évalués (1)** : CKRL — baseline évaluée de cans.
- **NS mentionnés (15)** : IGAN (ccs, gibbsns), IRGAN (graphgan, kbgan),
  MixGCF (demix, m2ixkg), CAKE (conceptdriven, demix), SANS (dmns),
  NCE (asa, dmns, mcns), LCWA-NS (gns, stc), Entity-Similarity-NS (gibbsns).
- **Optimizer (2)** : SGD (typeaugmented), AdaGrad (typeconstraints) — optimizers
  réellement utilisés dans le protocole, non extraits.
- **LossFunction (7)** : policy gradient (graphgan, igan, kbgan, ksgan, noigan,
  ruga — entraînement des générateurs GAN), Triplet loss (dans — loss standardisée
  des expériences).
- **Task (4)** : Relation Prediction (asa — task principale !, nscaching,
  tuckerdncaching), Triple Classification (lts).

## Familles de faux flags (203)

Mot anglais banal (attention, line, simple, good, random…) ; matchs partiels
(R-GCN→GCN, KG-BERT→BERT, GC-OTE→OTE, Self-Adversarial→Adversarial) ; acronyme vs
nom complet de la même méthode extraite (SANS/EANS/CANS/DMNS/MDNCaching…) ;
termes de catégorie (dynamic/static/simple/GAN-based sampling) ; related work où
la méthode propre est extraite ; tables de stats/complexité ; auteurs ("Adam
Lerer") ; hypothétiques/future work ; composants d'architecture (MLP, word2vec).
