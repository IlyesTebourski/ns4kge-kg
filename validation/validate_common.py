#!/usr/bin/env python3
"""
Driver COMMUN pour les validations "source unique" (datasets, metrics, hardware,
optimizer, lossfunction, task). Encode UNE SEULE FOIS la methodologie :

1. PRECISION AUTOMATIQUE — un matcher deterministe et GENERIQUE fourni par
   l'adaptateur. Non taille pour un article : on ne triche pas.

2. VERIFICATION MANUELLE (adjudication) — pour chaque item, un verdict humain
   optionnel dans PREC_VERDICTS[(slug, label)] :
     ("valid", why) : rate par l'algo mais CORRECT (coquille du papier, reformulation,
                      limite du matcher) -> recompte valide.
     ("error", why) : EXTRACTION FAUSSE (hallucination, mauvais type — ex. KBGAN mis
                      en KGEModel au lieu de NSMethod) -> compte faux MEME si la chaine
                      apparait dans le texte.
   Sans verdict : on fait confiance au resultat automatique (un rate non verifie
   reste faux et est signale "a verifier").

3. VOCAB POUR LE RECALL = UNIQUEMENT LES ITEMS VERIFIES CORRECTS.
   >>> Regle centrale : un item FAUX (hallucination / mauvais type) ne doit PAS
   contaminer le vocabulaire et generer de faux candidats de recall ailleurs.
   Le vocab global est donc construit apres la passe de precision, a partir des
   seuls items dont le statut final est "correct" (auto-trouve non condamne, ou
   rate mais reclasse valide). <<<

4. RECALL HONNETE — on cherche chaque item du vocab (non extrait par l'article)
   dans son texte. AUCUNE liste noire de mots pour etouffer le bruit : les
   candidats sur-generes sont adjuges a la main via RECALL_VERDICTS[(slug, label)] :
     ("miss", why) : vrai oubli d'extraction -> compte contre le recall.
     ("fp",   why) : faux positif (la chaine matche un usage non pertinent) -> ignore.
   Sans verdict : candidat "a verifier" (signale, exclu du recall chiffre).

On publie DEUX chiffres de precision (auto + verifiee) et un recall relatif adjuge.

L'adaptateur fournit un objet `Entity` (voir plus bas) ; ce module gere les deux
passes, l'adjudication, le vocab-verifie et le rendu markdown.
"""
import glob
import json
import os

import validate_datasets as VD


# --------------------------------------------------------------------------
# Contrat d'adaptateur
# --------------------------------------------------------------------------
class Entity:
    """A specialiser par entite. Attributs/So methodes attendues :

    name       : libelle humain ("Optimizer", ...).
    out_dir    : dossier de sortie des rapports.
    prec_verdicts   : dict {(slug, label): ("valid"|"error", why)}.
    recall_verdicts : dict {(slug, label): ("miss"|"fp", why)}.

    extract(data)          -> {norm_key: label}   items extraits par le KG.
    source_text(md_path, data) -> str             texte-source a valider contre.
    match(label, text, mode) -> re.Match | None    matcher generique. mode in
                              {"precision","recall"} : permet, comme dans les
                              validateurs KGE/NS, une precision plus LENIENTE (on
                              fait confiance au label extrait, on cherche son coeur
                              distinctif) et un recall plus STRICT (on exige assez de
                              signal pour ne pas crier au faux negatif sur du bruit).
    is_distinctive(label)  -> bool                 (recall) l'item est-il assez
                              specifique pour etre cherche sans generer de bruit ?
                              defaut : True.
    """
    name = "Entity"
    out_dir = None
    prec_verdicts = {}
    recall_verdicts = {}

    def extract(self, data):
        raise NotImplementedError

    def source_text(self, md_path, data):
        raise NotImplementedError

    def match(self, label, text, mode="precision"):
        raise NotImplementedError

    def is_distinctive(self, label):
        return True


# --------------------------------------------------------------------------
# Chargement
# --------------------------------------------------------------------------
def load_articles(ent):
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(VD.MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(VD.KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            print(f"[WARN] pas de .md pour {slug}")
            continue
        data = json.load(open(p, encoding="utf-8"))
        arts.append({
            "slug": slug,
            "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "text": ent.source_text(md, data),
            "items": ent.extract(data),
        })
    return arts


# --------------------------------------------------------------------------
# Passe 1 : precision + statut final (pour le vocab verifie)
# --------------------------------------------------------------------------
def precision_pass(ent, article):
    """Renvoie (rows, correct_items, spans).
    rows : [(label, found_auto, snippet, status, why)]
      status in {ok, condemned, rescued, wrong} ; ok/rescued = correct.
    correct_items : {norm_key: label} des items au statut final correct.
    spans : positions en texte des items CORRECTS trouves (anti-collision recall)."""
    slug, text = article["slug"], article["text"]
    rows, correct, spans = [], {}, []
    for k, lab in sorted(article["items"].items(), key=lambda kv: kv[1].lower()):
        m = ent.match(lab, text, "precision")
        v = ent.prec_verdicts.get((slug, lab))
        if m:
            snip = VD.snippet_around(text, m)
            if v and v[0] == "error":           # trouve mais FAUX (mauvais type...)
                rows.append((lab, True, snip, "condemned", v[1]))
            else:
                rows.append((lab, True, snip, "ok", ""))
                correct[k] = lab
                spans.append((m.start(), m.end()))
        else:
            if v and v[0] == "valid":           # rate mais correct (coquille...)
                rows.append((lab, False, "", "rescued", v[1]))
                correct[k] = lab
            elif v and v[0] == "error":
                rows.append((lab, False, "", "wrong", v[1]))
            else:
                rows.append((lab, False, "", "wrong", ""))  # non verifie -> faux+signale
    return rows, correct, spans


# --------------------------------------------------------------------------
# Passe 2 : recall (contre le vocab VERIFIE)
# --------------------------------------------------------------------------
def recall_pass(ent, article, vocab, spans):
    """Candidats faux negatifs = items du vocab (verifie) absents des extractions
    de l'article mais presents dans son texte, adjuges. Renvoie
    [(label, snippet, kind, why)] avec kind in {miss, fp, unreviewed}."""
    slug, text = article["slug"], article["text"]
    out = []
    for k, lab in sorted(vocab.items(), key=lambda kv: kv[1].lower()):
        if k in article["items"] or not ent.is_distinctive(lab):
            continue
        m = ent.match(lab, text, "recall")
        if not m:
            continue
        # deja couvert par un item CORRECT plus detaille -> pas un oubli
        if any(not (m.end() <= s or m.start() >= e) for s, e in spans):
            continue
        v = ent.recall_verdicts.get((slug, lab))
        kind = v[0] if v else "unreviewed"
        out.append((lab, VD.snippet_around(text, m), kind, v[1] if v else ""))
    return out


# --------------------------------------------------------------------------
# Rendu
# --------------------------------------------------------------------------
def esc(s):
    return s.replace("|", "\\|")


_STATUS_BADGE = {"ok": "✅ oui", "condemned": "❌ FAUX (trouve mais errone)",
                 "rescued": "✅ valide (verif manuelle)", "wrong": "❌ non"}
_RECALL_BADGE = {"miss": "❌ vrai oubli", "fp": "✅ faux positif (ignore)",
                 "unreviewed": "⚠️ A VERIFIER"}


def render_article(ent, article, rows, recall_rows):
    n = len(rows)
    tp_auto = sum(1 for r in rows if r[1])
    fp_auto = n - tp_auto
    correct = sum(1 for r in rows if r[3] in ("ok", "rescued"))
    wrong = n - correct
    rescued = sum(1 for r in rows if r[3] == "rescued")
    condemned = sum(1 for r in rows if r[3] == "condemned")
    unrev_p = sum(1 for r in rows if r[3] == "wrong" and not r[4])
    pa = tp_auto / n if n else 1.0
    pv = correct / n if n else 1.0
    real_miss = sum(1 for r in recall_rows if r[2] == "miss")
    fp_rec = sum(1 for r in recall_rows if r[2] == "fp")
    todo_rec = sum(1 for r in recall_rows if r[2] == "unreviewed")
    rec = correct / (correct + real_miss) if (correct + real_miss) else 1.0

    L = [f"# {ent.name} — {article['md_name']}", "",
         f"**Titre :** {article['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| {ent.name} extraits | {n} |",
         f"| Trouves automatiquement (TP auto) | {tp_auto} |",
         f"| **Precision automatique** | **{pa:.0%}** |",
         f"| Reclasses valides (verif manuelle) | {rescued} |",
         f"| Condamnes (trouves mais faux) | {condemned} |",
         f"| Vraies erreurs / non verifies | {wrong} |",
         f"| **Precision verifiee** | **{pv:.0%}** |",
         f"| Recall — vrais oublis | {real_miss} |",
         f"| Recall — faux positifs ecartes | {fp_rec} |",
         f"| **Recall relatif (indicatif)** | **{rec:.0%}** |", ""]

    L += [f"## Precision automatique — {ent.name} extrait vs source", "",
          "| Extrait | Trouve (algo) ? | Extrait de la source |", "|---|:---:|---|"]
    if rows:
        for lab, found, snip, status, _ in rows:
            badge = "✅ oui" if found else "❌ non"
            L.append(f"| {esc(lab)} | {badge} | {esc(snip) if found else '_(non trouve automatiquement)_'} |")
    else:
        L.append(f"| _(aucun {ent.name} extrait)_ | — | — |")
    L.append("")

    adj = [r for r in rows if r[3] in ("rescued", "condemned") or (r[3] == "wrong")]
    if adj:
        L += ["## Verification manuelle (adjudication precision)", "",
              "Chaque ecart avec la source est verifie a la main. Un item non imputable "
              "au KG est reclasse **valide** ; une extraction fausse est **condamnee** "
              "(compte faux) ; les verdicts citent la source.", "",
              "| Item | Verdict | Justification |", "|---|:---:|---|"]
        for lab, found, snip, status, why in adj:
            badge = _STATUS_BADGE[status]
            if status == "wrong" and not why:
                badge = "⚠️ A VERIFIER"
            L.append(f"| {esc(lab)} | {badge} | {esc(why) if why else '_(non encore verifie)_'} |")
        L.append("")

    L += [f"## Recall — {ent.name} du vocab (verifie) present mais NON extrait", ""]
    if recall_rows:
        L += ["| Item | Verdict | Extrait / justification |", "|---|:---:|---|"]
        for lab, snip, kind, why in recall_rows:
            info = why if why else snip
            L.append(f"| {esc(lab)} | {_RECALL_BADGE[kind]} | {esc(info)} |")
    else:
        L.append("_Aucun candidat._")

    stats = dict(n=n, tp_auto=tp_auto, correct=correct, wrong=wrong, rescued=rescued,
                 condemned=condemned, unrev_p=unrev_p, real_miss=real_miss,
                 fp_rec=fp_rec, todo_rec=todo_rec, pa=pa, pv=pv, rec=rec)
    return "\n".join(L), stats


def render_summary(ent, rows):
    T = lambda key: sum(r[1][key] for r in rows)
    N, TP, COR, RES, CON = T("n"), T("tp_auto"), T("correct"), T("rescued"), T("condemned")
    UNREVP = T("unrev_p"); MISS, FPR, TODOR = T("real_miss"), T("fp_rec"), T("todo_rec")
    pa = TP / N if N else 1.0
    pv = COR / N if N else 1.0
    rec = COR / (COR + MISS) if (COR + MISS) else 1.0
    L = [f"# Recap validation {ent.name.upper()} (source unique, verif manuelle)", "",
         f"Articles avec extraction : **{sum(1 for r in rows if r[1]['n'])}**", "",
         "| Article | Extr | TP auto | Prec.auto | Valid | Condamn | Prec.verif | Oublis | FP recall |",
         "|---|---:|---:|:---:|---:|---:|:---:|---:|---:|"]
    for name, s in rows:
        if not s["n"]:
            continue
        L.append(f"| {name} | {s['n']} | {s['tp_auto']} | {s['pa']:.0%} | {s['rescued']} "
                 f"| {s['condemned']} | {s['pv']:.0%} | {s['real_miss']} | {s['fp_rec']} |")
    L += ["", "## Totaux", "", "| Metrique | Valeur |", "|---|---|",
          f"| {ent.name} extraits (total) | {N} |",
          f"| Trouves automatiquement | {TP} |",
          f"| **Precision automatique (micro)** | **{pa:.1%}** |",
          f"| Reclasses valides (verif manuelle) | {RES} |",
          f"| Condamnes (trouves mais faux) | {CON} |",
          f"| Precision — ratés encore a verifier | {UNREVP} |",
          f"| **Precision verifiee (micro)** | **{pv:.1%}** |",
          f"| Recall — vrais oublis | {MISS} |",
          f"| Recall — faux positifs ecartes | {FPR} |",
          f"| Recall — candidats encore a verifier | {TODOR} |",
          f"| **Recall relatif (indicatif, micro)** | **{rec:.1%}** |", "",
          "> Vocab de recall = uniquement les items VERIFIES CORRECTS : une extraction "
          "fausse (hallucination / mauvais type) ne contamine pas le vocab et ne genere "
          "pas de faux candidats ailleurs. Precision auto = matcher deterministe non taille "
          "pour un article ; precision verifiee = apres adjudication manuelle tracable."]
    return "\n".join(L)


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------
def run(ent):
    os.makedirs(ent.out_dir, exist_ok=True)
    arts = load_articles(ent)

    # Passe 1 : precision -> statut final -> vocab VERIFIE
    prec = {}         # slug -> (rows, correct, spans)
    vocab = {}        # norm_key -> label, UNIQUEMENT items corrects
    for a in arts:
        rows, correct, spans = precision_pass(ent, a)
        prec[a["slug"]] = (rows, correct, spans)
        for k, lab in correct.items():
            vocab.setdefault(k, lab)
    print(f"Vocab {ent.name} (items verifies corrects) = {len(vocab)}")

    # Passe 2 : recall contre le vocab verifie
    summary_rows = []
    for a in arts:
        rows, correct, spans = prec[a["slug"]]
        recall_rows = recall_pass(ent, a, vocab, spans)
        report, stats = render_article(ent, a, rows, recall_rows)
        open(os.path.join(ent.out_dir, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        summary_rows.append((a["md_name"], stats))

    open(os.path.join(ent.out_dir, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(ent, summary_rows))

    N = sum(s["n"] for _, s in summary_rows)
    TP = sum(s["tp_auto"] for _, s in summary_rows)
    COR = sum(s["correct"] for _, s in summary_rows)
    MISS = sum(s["real_miss"] for _, s in summary_rows)
    TODO = sum(s["unrev_p"] for _, s in summary_rows)
    TODOR = sum(s["todo_rec"] for _, s in summary_rows)
    print(f"{len(arts)} rapports -> {ent.out_dir}/")
    print(f"{ent.name} extraits = {N}")
    print(f"Precision AUTO     = {TP/N if N else 1.0:.1%} (trouves {TP})")
    print(f"Precision VERIFIEE = {COR/N if N else 1.0:.1%} "
          f"(a verifier precision={TODO})")
    print(f"Recall relatif     = {COR/(COR+MISS) if (COR+MISS) else 1.0:.1%} "
          f"(oublis={MISS}, candidats a verifier={TODOR})")
    return summary_rows
