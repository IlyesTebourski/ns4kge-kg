# Task — ASA.md

**Titre :** Relation-aware Graph Attention Model With Adaptive Self-adversarial Training

| Metrique | Valeur |
|---|---|
| Task extraits | 1 |
| Trouves automatiquement (TP auto) | 0 |
| **Precision automatique** | **0%** |
| Reclasses valides (verif manuelle) | 0 |
| Condamnes (trouves mais faux) | 0 |
| Vraies erreurs / non verifies | 1 |
| **Precision verifiee** | **0%** |
| Recall — candidats bruts (script) | 1 |
| Recall BRUT (avant adjudication) | 0% |
| Recall — vrais oublis | 1 |
| Recall — faux positifs ecartes | 0 |
| **Recall relatif (adjuge)** | **0%** |

## Precision automatique — Task extrait vs source

| Extrait | Trouve (algo) ? | Extrait de la source |
|---|:---:|---|
| Link Prediction | ❌ non | _(non trouve automatiquement)_ |

## Verification manuelle (adjudication precision)

Chaque ecart avec la source est verifie a la main. Un item non imputable au KG est reclasse **valide** ; une extraction fausse est **condamnee** (compte faux) ; les verdicts citent la source.

| Item | Verdict | Justification |
|---|:---:|---|
| Link Prediction | ⚠️ A VERIFIER | _(non encore verifie)_ |

## Recall — Task du vocab (verifie) present mais NON extrait

| Item | Verdict | Extrait / justification |
|---|:---:|---|
| Relation Prediction | ❌ vrai oubli | Task PRINCIPALE du papier ('end-to-end solution for the relationship prediction task', resultats SOTA dessus) ; configs = Link Prediction. |