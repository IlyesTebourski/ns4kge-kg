# LossFunction — Localcognitive.md

**Titre :** RatE: Relation-Adaptive Translating Embedding for Knowledge Graph Completion

| Metrique | Valeur |
|---|---|
| LossFunction extraits | 1 |
| Trouves automatiquement (TP auto) | 1 |
| **Precision automatique** | **100%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 0 |
| **Precision verifiee** | **100%** |
| Recall — candidats bruts (script) | 2 |
| Recall BRUT (avant adjudication) | 33% |
| Recall — vrais oublis | 0 |
| Recall — faux positifs ecartes | 2 |
| **Recall relatif (adjuge)** | **100%** |

## Precision automatique — LossFunction extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Self-adversarial negative sampling loss | ✅ oui | {G}^{(tr)}\}. \eqno(6) $$ In contrast, self-adversarial negative sampling (Sun et al., 2019) applies triple scori |

## Recall — LossFunction du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| adversarial loss | ✅ faux positif (ignore) | Abrege de la 'Self-adversarial negative sampling loss' deja extraite. |
| self adversarial loss | ✅ faux positif (ignore) | Meme phrase ; loss deja extraite. |