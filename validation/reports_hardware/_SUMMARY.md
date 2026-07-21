# Recap validation HARDWARE (prose `no_tables`, avec verif manuelle)

Articles : **55**

| Article | Extrait | TP auto | Prec.auto | Valides(manuel) | Erreurs | Prec.verif | Cand.recall |
|---|---:|---:|:---:|---:|---:|:---:|---:|
| ADNS.md | 2 | 1 | 50% | 1 | 0 | 100% | 0 |
| BatchNS.md | 1 | 0 | 0% | 0 | 1 | 0% | 0 |
| CAKE.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| CCS.md | 1 | 0 | 0% | 1 | 0 | 100% | 0 |
| DHNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| EANS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| eTruncatedUNS.md | 2 | 2 | 100% | 0 | 0 | 100% | 0 |
| GHN.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| HaSa.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| Localcognitive.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| NSCaching.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| SNS.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |
| TruncatedNS.md | 2 | 2 | 100% | 0 | 0 | 100% | 0 |
| TuckerDNCaching.md | 1 | 1 | 100% | 0 | 0 | 100% | 0 |

## Totaux

| Metrique | Valeur |
|---|---|
| Hardware extrait (total) | 17 |
| Trouves automatiquement (TP auto) | 14 |
| Non trouves par l'algo | 3 |
| **Precision automatique (micro)** | **82.4%** |
| Ratés reclasses VALIDES (verif manuelle) | 2 |
| Vraies erreurs d'extraction | 1 |
| Ratés encore a verifier | 0 |
| **Precision verifiee (micro)** | **94.1%** |
| Candidats faux negatifs recall | 0 |
| **Recall relatif (indicatif, micro)** | **100.0%** |

> Methodo : la **precision automatique** vient d'un matcher deterministe non taille pour un article (aucune triche). La **precision verifiee** integre l'adjudication manuelle STRICTE : seules les coquilles averees du PAPIER (Teals->Tesla, RTX 260->2060) sont reclassees valides ; une reformulation par le KG ou un identifiant absent de la source reste comptee comme erreur. Chaque verdict cite la prose (section 'Verification manuelle' de chaque rapport d'article). Source unique : hardware = prompt1 (prose) ; aucun tableau n'en extrait.