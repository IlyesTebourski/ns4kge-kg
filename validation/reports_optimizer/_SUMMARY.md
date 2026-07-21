# Recap validation OPTIMIZER (source unique, verif manuelle)

Articles avec extraction : **37**

| Article | Extr | TP auto | Prec.auto | Valid | Condamn | Prec.verif | Oublis | FP recall |
|---|---:|---:|:---:|---:|---:|:---:|---:|---:|
| ADNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| BatchNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| CAKE.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| CANS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| CCS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| ConceptDriven.md | 2 | 2 | 100% | 0 | 0 | 100% | 0 | 0 |
| DeMix.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| DHNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| DNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| DomainNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| EANS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| ERDNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| eTruncatedUNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| GHN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| GNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| GraphGAN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| HaSa.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| HTENS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| IGAN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| KBGAN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| KSGAN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| LAS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| Localcognitive.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| M2ixKG.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| MDNCaching.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| NMiss.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| NoiGAN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| NSCaching.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| PNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| SelfAdv.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| SNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| SparseNSG.md | 1 | 0 | 0% | 0 | 0 | 0% | 0 | 0 |
| STC.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| TuckerDNCaching.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| TypeAugmented.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |
| TypeConstraints.md | 2 | 2 | 100% | 0 | 0 | 100% | 0 | 0 |
| Uniform.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 | 0 |

## Totaux

| Metrique | Valeur |
|---|---|
| Optimizer extraits (total) | 39 |
| Trouves automatiquement | 38 |
| **Precision automatique (micro)** | **97.4%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Precision — ratés encore a verifier | 1 |
| **Precision verifiee (micro)** | **97.4%** |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 0 |
| Recall — candidats encore a verifier | 10 |
| **Recall relatif (indicatif, micro)** | **100.0%** |

> Vocab de recall = uniquement les items VERIFIES CORRECTS : une extraction fausse (hallucination / mauvais type) ne contamine pas le vocab et ne genere pas de faux candidats ailleurs. Precision auto = matcher deterministe non taille pour un article ; precision verifiee = apres adjudication manuelle tracable.