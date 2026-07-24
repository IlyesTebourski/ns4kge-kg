# Recap validation DATASETS (base sur les tables_only)

Articles : **55**

| Article | TP | FP | Precision | Cand. resultats | Cand. stats | Recall~ |
|---|---:|---:|:---:|---:|---:|:---:|
| AdaptativeNS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| ADNS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| ASA.md | 3 | 0 | 100% | 0 | 0 | 100% |
| BatchNS.md | 2 | 0 | 100% | 0 | 0 | 100% |
| CAKE.md | 4 | 0 | 100% | 0 | 0 | 100% |
| CANS.md | 6 | 0 | 100% | 1 | 0 | 100% |
| CCS.md | 4 | 0 | 100% | 0 | 0 | 100% |
| ConceptDriven.md | 2 | 0 | 100% | 1 | 0 | 100% |
| CondConstraints.md | 1 | 1 | 50% | 0 | 0 | 100% |
| dans.md | 3 | 0 | 100% | 0 | 0 | 100% |
| DeMix.md | 2 | 0 | 100% | 0 | 0 | 100% |
| DHNS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| DMNS.md | 4 | 0 | 100% | 0 | 0 | 100% |
| DNS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| DomainNS.md | 2 | 0 | 100% | 0 | 0 | 100% |
| EANS.md | 2 | 0 | 100% | 0 | 0 | 100% |
| ERDNS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| eTruncatedUNS.md | 5 | 0 | 100% | 0 | 0 | 100% |
| GHN.md | 3 | 0 | 100% | 0 | 0 | 100% |
| GibbsNS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| GNDN.md | 2 | 0 | 100% | 0 | 0 | 100% |
| GNS.md | 0 | 1 | 0% | 0 | 1 | 100% |
| GraphGAN.md | 4 | 0 | 100% | 0 | 0 | 100% |
| HaSa.md | 2 | 0 | 100% | 0 | 0 | 100% |
| HTENS.md | 2 | 0 | 100% | 0 | 0 | 100% |
| IGAN.md | 4 | 0 | 100% | 0 | 0 | 100% |
| KBGAN.md | 3 | 0 | 100% | 0 | 0 | 100% |
| KSGAN.md | 3 | 0 | 100% | 0 | 0 | 100% |
| LAS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| LEMON.md | 2 | 0 | 100% | 0 | 0 | 100% |
| Localcognitive.md | 4 | 0 | 100% | 0 | 0 | 100% |
| LTS.md | 4 | 0 | 100% | 0 | 0 | 100% |
| M2ixKG.md | 2 | 0 | 100% | 0 | 0 | 100% |
| MCNS.md | 5 | 0 | 100% | 0 | 0 | 100% |
| MDNCaching.md | 2 | 0 | 100% | 0 | 0 | 100% |
| NMiss.md | 2 | 0 | 100% | 0 | 0 | 100% |
| NoiGAN.md | 5 | 0 | 100% | 1 | 0 | 100% |
| NSCaching.md | 4 | 0 | 100% | 0 | 0 | 100% |
| PNS.md | 2 | 0 | 100% | 0 | 0 | 100% |
| RAAKGC.md | 11 | 0 | 100% | 0 | 0 | 100% |
| RandomCorrupt.md | 5 | 0 | 100% | 0 | 0 | 100% |
| RCWC.md | 4 | 0 | 100% | 0 | 0 | 100% |
| ReasonKGE.md | 3 | 0 | 100% | 0 | 0 | 100% |
| RUGA.md | 2 | 0 | 100% | 0 | 0 | 100% |
| SANS.md | 3 | 0 | 100% | 0 | 0 | 100% |
| SelfAdv.md | 8 | 0 | 100% | 0 | 0 | 100% |
| SNS.md | 6 | 0 | 100% | 0 | 0 | 100% |
| SparseNSG.md | 2 | 0 | 100% | 0 | 0 | 100% |
| STC.md | 1 | 0 | 100% | 0 | 0 | 100% |
| TANS.md | 6 | 0 | 100% | 0 | 0 | 100% |
| TruncatedNS.md | 2 | 0 | 100% | 0 | 0 | 100% |
| TuckerDNCaching.md | 4 | 0 | 100% | 0 | 0 | 100% |
| TypeAugmented.md | 4 | 0 | 100% | 0 | 0 | 100% |
| TypeConstraints.md | 3 | 0 | 100% | 0 | 0 | 100% |
| Uniform.md | 2 | 0 | 100% | 1 | 0 | 100% |

## Totaux

| Metrique | Valeur |
|---|---|
| Total TP | 182 |
| Total FP (extraits absents des tables) | 2 |
| Total candidats faux negatifs (tables resultats) | 4 |
| Total candidats en tables stats seulement | 1 |
| **Precision micro** | **98.9%** |
| **Precision macro** | **97.3%** |
| **Recall relatif micro (indicatif)** | **97.8%** |
| **Recall relatif macro (indicatif)** | **100.0%** |

> Recall **indicatif** : les candidats 'table de resultats' sont des datasets presents dans un tableau de resultats mais non extraits — a verifier a la main. Les candidats 'table de stats' sont volontairement ignores par le prompt (tables de statistiques/ablation).