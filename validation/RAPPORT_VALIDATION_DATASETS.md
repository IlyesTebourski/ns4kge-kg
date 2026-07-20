# Rapport de validation — Extraction des *datasets* du Knowledge Graph NS4KGE

**Auteur :** Ilyes Tebourski
**Date :** 20 juillet 2026
**Périmètre :** validation de l'extraction des **datasets** sur les 55 articles du corpus
**Livrables :** `validation/validate_datasets.py` (script), `validation/reports_datasets/` (55 rapports par article + `_SUMMARY.md`)

---

## 1. Objectif

Évaluer de façon rigoureuse la qualité de l'extraction automatique des **noms de datasets**
réalisée par le pipeline NS4KGE, sur l'ensemble des 55 articles du corpus. La validation
mesure deux dimensions :

- **Précision** : parmi les datasets extraits par le KG, combien sont réellement présents dans l'article ?
- **Recall (relatif)** : parmi les datasets réellement présents dans les résultats de l'article, combien ont bien été extraits ?

Cette validation est ciblée sur les datasets car ce sont les entités les plus **canoniques**
(noms standardisés : `FB15k-237`, `WN18RR`, `UMLS`, `YAGO3-10`, `Nations`…), donc celles qui
nécessitent le moins de pré-traitement et se prêtent le mieux à une vérification fiable.

---

## 2. Rappel du pipeline d'extraction (point méthodologique clé)

Le pipeline NS4KGE repose sur **deux prompts** appliqués à deux versions pré-traitées de chaque article :

| Prompt | Entrée (pré-traitement) | Ce qui est extrait |
|---|---|---|
| `prompt1_no_results.txt` | `load_md_no_tables()` — l'article **sans les tableaux** | NS methods, KGE models, optimizer, loss, hardware… |
| `prompt2_tab.txt` | `load_md_tables_only()` — **uniquement les tableaux** (`<table>` + leur caption) | `Configurations[]` : **Dataset**, Metric, KGEModel, NSMethod, result |

**Conséquence fondamentale pour la validation :** les datasets ne sont **jamais** extraits de la prose.
Ils proviennent exclusivement des **tableaux de résultats** (`Configurations`), dont l'unique entrée
est le sidecar `tables_only`. Un dataset cité seulement en prose (ex. *« WN18RR is a subset of WN18 »*,
ou une référence bibliographique `arXiv preprint`) **ne doit donc pas** être extrait.

La validation reproduit fidèlement ce découpage : **les datasets sont vérifiés contre le `tables_only`**,
et non contre l'article complet. Point important, le `tables_only` est **régénéré à la volée en
appelant directement la fonction `load_md_tables_only()` du dépôt** (`ns4kge-extraction-pipeline`),
à partir des fichiers sources `liste_mds/*.md`. Il n'y a donc **aucune divergence possible** entre ce
que voit le validateur et ce que voit réellement le prompt, et aucun fichier intermédiaire à maintenir.

```
liste_mds/<Article>.md ──load_md_tables_only()──▶ tables_only (en mémoire)
                                                        │
KG : <article>_merged.json ──Configurations[].Dataset──┤
                                                        ▼
                                          Précision + Recall relatif
                                          → reports_datasets/<article>.md
```

---

## 3. Définitions des métriques

- **TP (vrai positif)** : dataset extrait par le KG **et** retrouvé dans le `tables_only` de l'article.
- **FP (faux positif)** : dataset extrait par le KG mais **absent** du `tables_only` → erreur de précision.
- **Précision** = TP / (TP + FP).
- **Candidat faux négatif** : dataset présent dans une **cellule de tableau** de l'article mais **non extrait** par le KG.
- **Recall relatif** = TP / (TP + candidats en table de résultats).

Le recall est qualifié de **relatif** parce qu'il s'appuie sur un **vocabulaire global** de datasets
(l'union des 73 datasets extraits sur l'ensemble des 55 articles). On teste, pour chaque article,
si l'un de ces 73 datasets apparaît dans ses tableaux sans avoir été extrait. C'est un proxy
robuste, mais qui reste **indicatif** (voir §7).

Pour ne pas confondre datasets de résultats et datasets de statistiques, chaque tableau est
**classé via sa caption** : une caption contenant *statistics / statistical / ablation /
hyper-parameter* désigne un tableau que le prompt demande explicitement d'ignorer. Les candidats
issus de ces tableaux sont donc reportés séparément, en **priorité basse**.

---

## 4. Méthode de *matching* (recherche des noms dans le texte)

Les noms de datasets étant canoniques, un matching **verbatim normalisé** suffit. Décisions retenues :

1. **Insensible à la casse** et tolérant aux **séparateurs** (`espace`, `-`, `_`, `/`, `.`, `@`) :
   `FB15k-237`, `FB15k_237`, `FB15k 237` sont reconnus comme équivalents.
2. **Frontières strictes** : un nom ne peut pas être un simple **préfixe** d'un code plus grand.
   `FB15k` (dataset A) **ne matche pas** l'intérieur de `FB15k-237` (dataset B distinct). Cette
   règle a éliminé la principale source de faux candidats (les tirets étaient initialement traités
   comme des frontières de mots).
3. **Recall restreint aux cellules `<table>`** : un candidat n'est retenu que s'il apparaît dans un
   bloc `<table>…</table>` (une ligne de tableau), et non dans une caption ou une phrase de légende.

> Choix assumé : matching **modéré**, ni trop strict (on tolère les variantes d'écriture), ni trop
> permissif (pas de sous-chaîne, pas de distance d'édition), afin de minimiser à la fois les faux
> positifs et les faux négatifs.

---

## 5. Résultats globaux

| Indicateur | Valeur |
|---|---|
| Articles validés | **55 / 55** |
| Datasets distincts extraits (occurrences par article) | 184 |
| Vocabulaire global de datasets | 73 |
| **Vrais positifs (TP)** | **182** |
| **Faux positifs (FP)** | **2** |
| **Précision (micro)** | **98,9 %** |
| Candidats faux négatifs (tableaux de résultats) | 5 |
| Candidats en tableau de statistiques (priorité basse) | 1 |
| **Recall relatif (micro)** | **97,3 %** |
| Articles à précision 100 % | **53 / 55** |

> *Micro* = agrégation sur toutes les entités du corpus. La précision *macro* (moyenne des
> précisions par article) est du même ordre (≈ 99 %).

---

## 6. Analyse des faux positifs (précision)

Les **2 seuls** faux positifs ne sont pas des erreurs de matching mais de **vraies erreurs
d'extraction en amont** (le KG a produit un libellé qui n'est pas un dataset réel) :

| Article | Libellé extrait | Diagnostic |
|---|---|---|
| `CondConstraints.md` | `Table 1 Dataset` | En-tête de tableau capturé par erreur comme nom de dataset. |
| `GNS.md` | `FB13 (FB13_reduced)` | Libellé composite avec parenthèse ; la forme canonique du dataset dans l'article est `FB13`. |

**Conclusion précision :** 98,9 %, et les 2 écarts sont des artefacts d'extraction identifiés,
non des faux positifs du validateur.

---

## 7. Analyse des candidats faux négatifs (recall)

La restriction aux tableaux fait passer le nombre de candidats de **108 (bruités, sur l'article
complet)** à **6** au total. Chaque candidat restant a été **revu manuellement** :

| Article | Candidat | Où | Verdict |
|---|---|---|---|
| `CANS.md` | `FB15k` | tableau de stats (sans caption) | Faux positif du recall : ce sont les datasets **de base** ; les résultats utilisent `FB15K-N1/N2/N3` (bien extraits). |
| `CANS.md` | `WN18` | tableau de stats (sans caption) | Idem : résultats sur `WN18-N1/N2/N3`, correctement extraits. |
| `ConceptDriven.md` | `WN` | en-tête abrégé `WN.↑` | Abréviation de colonne ; le dataset réel `WN18RR` est extrait. |
| `NoiGAN.md` | `Actor` | cellule `actor (filmmaking occupation)` | Le mot « actor » est une **valeur d'entité**, pas le dataset *Actor*. |
| `Uniform.md` | `Actor` | cellule `Best Actor - Motion Picture` | Idem, valeur de données, pas le dataset. |
| `GNS.md` | `FB13` | *Table 1 (statistics)* | Tableau de statistiques → volontairement ignoré par le prompt. |

**Conclusion recall :** après revue, **aucun des candidats n'est un véritable oubli d'extraction**.
Le recall réel sur les datasets de résultats est donc, sur ce corpus, effectivement proche de 100 %,
les 6 candidats étant des fausses alertes de deux natures bien identifiées :
(a) datasets de base présents dans un tableau de **statistiques**, et
(b) **mots courants ambigus** (`Actor`) apparaissant comme valeurs de données.

---

## 8. Limites connues

- **Recall « relatif »** : il ne peut détecter que les oublis portant sur des datasets déjà connus
  du vocabulaire global (73 datasets). Un dataset totalement absent de tout le corpus ne serait pas
  détecté. En pratique, les benchmarks KGE étant très standardisés, cette limite est faible.
- **Captions manquantes** : quelques tableaux n'ont pas de caption (`(sans caption)`), ce qui empêche
  de les classer automatiquement en *stats* vs *résultats* (cas `CANS`). Cela génère de rares fausses
  alertes de recall, sans impact sur la précision.
- **Mots ambigus** : les datasets dont le nom est un mot courant (`Actor`, `Amazon`, `Company`…)
  peuvent apparaître comme valeurs de cellule ; ils sont signalés comme candidats à revoir, jamais
  comptés automatiquement comme erreurs.

---

## 9. Conclusion

Sur les 55 articles du corpus, l'extraction des datasets présente une **précision de 98,9 %** et un
**recall relatif de 97,3 %**. Après revue manuelle :

- les **2 faux positifs** sont des artefacts d'extraction bien caractérisés (en-tête de tableau,
  libellé composite), et non des défauts de la méthode de validation ;
- **aucun** des candidats faux négatifs ne correspond à un vrai oubli d'extraction.

La qualité de l'extraction des datasets est donc **élevée et vérifiée**. Le point fort
méthodologique de cette validation est qu'elle est **fidèle au pipeline** : la vérification est
réalisée exactement sur l'entrée que reçoit le prompt d'extraction (`tables_only`), en réutilisant
le code du dépôt, ce qui écarte tout écart entre l'évaluation et le système évalué.

---

## 10. Reproductibilité

```bash
# depuis /home/ilyes/POSTER
python3 validation/validate_datasets.py
```

Le script lit `liste_mds/*.md` et `ns4kge-kg/per_article/*_merged.json`, régénère les `tables_only`
via `load_md_tables_only()` du dépôt `ns4kge-extraction-pipeline`, puis écrit :

- `validation/reports_datasets/<article>.md` — le détail par article (tableau précision + candidats recall) ;
- `validation/reports_datasets/_SUMMARY.md` — le tableau récapitulatif des 55 articles et les totaux.
