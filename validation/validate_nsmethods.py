#!/usr/bin/env python3
"""
Validation des NS METHODS extraites par le KG, avec DISTINCTION DE PROVENANCE
(comme KGEModel) et 4 scores : precision evalues / precision mentionnes /
recall evalues / recall mentionnes.

Sources :
- proposedNSMethod + mentionedNSMethods -> prompt1 -> prose (no_tables)
- Configurations[].NSMethod             -> prompt2 -> tables (tables_only)

Difficultes specifiques NS methods (matching iteratif) :
- "Unknown" (placeholder du prompt pour baseline non identifiee) -> EXCLU.
- "Negative Sampling" souvent omis/abrege -> mots de liaison optionnels.
- Fortes ABREVIATIONS : le KG garde le nom complet, le texte utilise l'acronyme
  (Random Negative Sampling -> RNS, Self-Adversarial NS -> SANS) -> on derive et
  matche l'acronyme (sensible a la casse).

Matching hybride : precision insensible casse ; recall sensible casse (bruit).
Sorties : validation/reports_nsmethods/<slug>.md + _SUMMARY.md
"""
import json
import glob
import os
import re

import validate_datasets as VD

MD_DIR = VD.MD_DIR
KG_DIR = VD.KG_DIR
OUT_DIR = os.path.join(VD.HERE, "reports_nsmethods")

SEP = r"[\s\-_/.@()\[\]]*"
# mots de liaison optionnels (souvent omis dans le texte)
FILLER = {"negative", "neg", "sampling", "sample", "based", "method", "approach",
          "technique", "strategy", "with", "w"}
GENERIC = {"sampling", "sample", "ns", "method", "negative"}


def normalize_label(label):
    """Retire les qualificatifs experimentaux pour matcher la methode de BASE :
    (...) [...] %, ratios, regimes d'entrainement (scratch/pretrain), et coupe
    sur les separateurs de compound (+, virgule, 'w/', 'with').
    Ex. 'NoiGAN (hard) (40%)' -> 'NoiGAN' ; 'NSCaching + scratch' -> 'NSCaching' ;
        'closed world constraints, neg_ratio=1' -> 'closed world constraints'."""
    s = re.sub(r"\([^)]*\)", " ", label)
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.split(r"\s*(?:\+|,|\bw/\b|\bwith\b)\s*", s)[0]
    s = re.sub(r"(?i)\b(?:scratch|pretrain)\b", " ", s)
    s = re.sub(r"\d+\s*%?", " ", s)
    s = " ".join(s.split()).strip()
    return s or label.strip()


def tokens_cs(label):
    return re.findall(r"[A-Za-z0-9]+", normalize_label(label))


def content_tokens(label):
    return [t for t in tokens_cs(label) if t.lower() not in FILLER]


def method_key(label):
    """Cle canonique = mots de contenu (sans negative/sampling...). Dedup les
    quasi-doublons : 'Bernoulli Sampling' == 'Bernoulli Negative Sampling'."""
    return "".join(t.lower() for t in content_tokens(label))


# acronymes trop generiques -> ne pas DERIVER de pattern de matching dessus
# (robustesse du matcher : "GAN"/"KG" matcheraient partout ; ce n'est PAS une
# stoplist d'entites qui etouffe le recall, c'est le meme principe que "loss"
# exige pour lossfunction — on ne matche pas sur un acronyme non distinctif).
GENERIC_ACR = {"GAN", "NS", "KG", "LP", "KGE"}

# Verdicts de verification MANUELLE (remplis apres coup ; vides = baseline honnete).
PREC_VERDICTS = {}
RECALL_VERDICTS = {}


def is_unknown(label):
    return VD.norm_key(label).startswith("unknown")


def is_excluded(label):
    # Seuls "Unknown" (placeholder du prompt pour baseline non identifiee) et une
    # cle vide sont exclus. Plus de GENERIC_METHODS (gan/ns...) : un terme trop
    # generique extrait comme NS method est une question de PRECISION (a condamner
    # en verif manuelle), pas a masquer d'office.
    k = method_key(label)
    return is_unknown(label) or k == ""


# Abreviations canoniques de la litterature (Wang et al., TransH) : le texte ecrit
# souvent la forme abregee entre guillemets ("bern"/"unif") plutot que le nom
# complet. On les reconnait comme alias pour ne pas rater la mention/evaluation.
ALIASES = {
    "bernoulli": ["Bernoulli", "bern"],
    "uniform":   ["Uniform", "unif"],
}


def _tok_re(t):
    """Regex d'un token : alias canoniques si connus, + pluriel optionnel ('s?')."""
    alts = ALIASES.get(t.lower(), [t])
    return r"(?:" + "|".join(re.escape(a) for a in alts) + r")s?"


def name_pattern(label, ci):
    """Regex du nom complet, avec mots de liaison optionnels entre tokens."""
    toks = tokens_cs(label)
    if not toks:
        return None
    required = [t for t in toks if t.lower() not in FILLER]
    if not required or (len(required) == 1 and required[0].lower() in GENERIC):
        required = toks[:]
    filler_alt = "|".join(sorted(FILLER, key=len, reverse=True))
    gap = SEP + r"(?:(?:" + filler_alt + r")" + SEP + r")*"
    core = gap.join(_tok_re(t) for t in required)
    return re.compile(r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])", re.I if ci else 0)


# NB : plus de stoplists WEAK_BOTH / WEAK_PROSE. C'etait l'overfit principal —
# on retirait a la main "random"/"uniform"/"bernoulli"/... du recall pour tuer le
# bruit. Desormais, honnete : le recall sur-genere ces candidats, et on les tranche
# a la main (RECALL_VERDICTS : "fp" si la chaine matche un usage non-NS). Le vocab
# n'etant bati que sur les items VERIFIES CORRECTS, un faux item ne contamine rien.


def acronyms_of(label, min_len=3):
    """Acronymes candidats : initiales de TOUS les mots ET des seuls mots de
    contenu. Ex. 'Adaptive Self-Adversarial NS' -> {'ASANS','ASA'} ;
    'Confidence-Aware NS' -> {'CANS'}."""
    toks = tokens_cs(label)
    if len(toks) < 2:
        return set()
    cands = set()
    for seq in (toks, content_tokens(label)):
        acr = "".join(t[0] for t in seq if t and t[0].isalpha()).upper()
        if len(acr) >= min_len and acr not in GENERIC_ACR:
            cands.add(acr)
    return cands


def acr_pattern(label, min_len=3):
    cands = acronyms_of(label, min_len)
    if not cands:
        return None
    alt = "|".join(re.escape(a) for a in sorted(cands, key=len, reverse=True))
    # acronyme = mot entier, SENSIBLE A LA CASSE (evite les faux matchs)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + alt + r")(?![A-Za-z0-9])")


def variant_find(label, text):
    """Match d'une variante '<base> w/ <suffixe>' via l'ACRONYME de la base +
    le suffixe, tel que les tableaux l'ecrivent reellement :
    'Self-Adversarial Negative Sampling w/ Base' -> entete 'SANS w/ Base'.
    Sans ca, le nom complet extrait par le KG ne matche jamais l'acronyme du
    tableau (faux negatif de precision). Acronyme sensible a la casse (bruit)."""
    parts = re.split(r"\s*\bw/\s*|\s+with\s+", label, maxsplit=1)
    if len(parts) != 2:
        return None, None
    base, suffix = parts
    acrs = acronyms_of(base)
    suf_toks = re.findall(r"[A-Za-z0-9]+", suffix)
    if not acrs or not suf_toks:
        return None, None
    alt = "|".join(re.escape(a) for a in sorted(acrs, key=len, reverse=True))
    suf = SEP.join(re.escape(t) for t in suf_toks)
    pat = re.compile(r"(?<![A-Za-z0-9])(?:" + alt + r")" + SEP + r"w/?" + SEP
                     + suf + r"(?![A-Za-z0-9])")
    m = pat.search(text)
    return (m, "variant") if m else (None, None)


def find(label, text, ci, min_acr=3):
    """Retourne (match, via) ou (None, None). via in {name, acro, variant}."""
    p = name_pattern(label, ci)
    if p:
        m = p.search(text)
        if m:
            return m, "name"
    pa = acr_pattern(label, min_acr)
    if pa:
        m = pa.search(text)
        if m:
            return m, "acro"
    return variant_find(label, text)


# --------------------------------------------------------------------------
def load_articles():
    from no_facts_pipeline.core import load_md_tables_only, load_md_no_tables
    md_files = {os.path.basename(p)[:-3].lower(): p
                for p in glob.glob(os.path.join(MD_DIR, "*.md"))}
    arts = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md = md_files.get(slug)
        if not md:
            continue
        data = json.load(open(p, encoding="utf-8"))
        methods = {}

        def add(val, src):
            if not val or not str(val).strip() or is_excluded(val):
                return
            val = str(val).strip()
            k = method_key(val)   # cle canonique (dedup quasi-doublons)
            if k:
                methods.setdefault(k, {"label": val, "src": set()})["src"].add(src)

        add(data.get("proposedNSMethod"), "prose")
        for m in data.get("mentionedNSMethods", []) or []:
            add(m, "prose")
        for c in data.get("Experimentation", {}).get("Configurations", []) or []:
            if isinstance(c, dict):
                add(c.get("NSMethod"), "table")

        arts.append({
            "slug": slug, "md_name": os.path.basename(md),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "prose": load_md_no_tables(md), "tables": load_md_tables_only(md),
            "methods": methods,
        })
    return arts


def build_global_vocab(arts):
    vocab = {}
    for a in arts:
        for k, e in a["methods"].items():
            vocab.setdefault(k, e["label"])
    return vocab


def precision_pass(article):
    """Precision (insensible casse) + collecte des items VERIFIES CORRECTS (vocab)."""
    slug, prose, tables = article["slug"], article["prose"], article["tables"]
    evaluated, mentioned = [], []
    verified = {}          # method_key -> label
    te = fe = tm = fm = 0
    for k, e in sorted(article["methods"].items(), key=lambda kv: kv[1]["label"].lower()):
        label, src = e["label"], e["src"]
        # espace de recherche = union des entrees vues par le(s) prompt(s) source(s)
        text = "\n".join(([prose] if "prose" in src else []) +
                         ([tables] if "table" in src else []))
        m, via = find(label, text, ci=True)
        v = PREC_VERDICTS.get((slug, label))
        ok = bool(m) if not v else (v[0] == "valid" or (bool(m) and v[0] != "error"))
        row = (label, bool(m), (via or ""), VD.snippet_around(text, m) if m else "")
        if "table" in src:
            evaluated.append(row); te += bool(m); fe += (not m)
        else:
            mentioned.append(row); tm += bool(m); fm += (not m)
        if ok:
            verified[k] = label
    return evaluated, mentioned, verified, (te, fe, tm, fm)


def recall_pass(article, vocab):
    """RECALL (sensible casse) : methode du vocab VERIFIE presente dans l'article mais
    non extraite. Plus de stoplists WEAK_* : on sur-genere honnetement, dedup par
    position (une occurrence = un seul candidat), puis on tranche a la main."""
    prose, tables = article["prose"], article["tables"]
    raw = []   # (label, src, via, start, end, snippet)
    for k, label in sorted(vocab.items(), key=lambda kv: kv[1].lower()):
        if k in article["methods"]:
            continue
        for src, txt in (("prose", prose), ("table", tables)):
            m, via = find(label, txt, ci=False, min_acr=4)
            if m:
                raw.append((label, src, via, m.start(), m.end(), VD.snippet_around(txt, m)))
    raw.sort(key=lambda x: 0 if x[2] == "name" else 1)   # noms d'abord
    claimed = {"prose": [], "table": []}
    survivors = {}
    for label, src, via, s, e, snip in raw:
        if any(not (e <= cs or s >= ce) for cs, ce in claimed[src]):
            continue   # span deja pris par un autre candidat -> collision, on saute
        claimed[src].append((s, e))
        d = survivors.setdefault(label, {"where": set(), "via": via, "snip": snip})
        d["where"].add(src)
    return [(label, "+".join(sorted(d["where"])), d["via"], d["snip"])
            for label, d in survivors.items()]


def split_suspects(suspects):
    me = [s for s in suspects if "table" in s[1]]
    mm = [s for s in suspects if "table" not in s[1]]
    return me, mm


# --------------------------------------------------------------------------
def esc(s):
    return s.replace("|", "\\|")


def render_article(a, evaluated, mentioned, suspects, counts):
    te, fe, tm, fm = counts
    tp, fp = te + tm, fe + fm
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    pe = te / (te + fe) if (te + fe) else 1.0
    pm = tm / (tm + fm) if (tm + fm) else 1.0
    miss_e, miss_m = split_suspects(suspects)
    re_e = te / (te + len(miss_e)) if (te + len(miss_e)) else 1.0
    re_m = tm / (tm + len(miss_m)) if (tm + len(miss_m)) else 1.0

    L = [f"# NS Methods — {a['md_name']}", "", f"**Titre :** {a['title']}", "",
         "| Metrique | Valeur |", "|---|---|",
         f"| Methodes EVALUEES (tableaux) | {te + fe} |",
         f"| Methodes MENTIONNEES seulement (prose) | {tm + fm} |",
         f"| Precision evalues | {pe:.0%} | ",
         f"| Precision mentionnes | {pm:.0%} |",
         f"| Recall evalues | {re_e:.0%} |",
         f"| Recall mentionnes | {re_m:.0%} |", "",
         "## A. Methodes EVALUEES (valides vs `tables_only`)", "",
         "| Methode | Trouvee ? | Via | Extrait |", "|---|:---:|:---:|---|"]
    for label, ok, via, snip in evaluated:
        L.append(f"| {esc(label)} | {'✅' if ok else '❌'} | {via} | {esc(snip) if ok else '_(absent)_'} |")
    L += ["", "## B. Methodes MENTIONNEES seulement (valides vs prose)", ""]
    if mentioned:
        L += ["| Methode | Trouvee ? | Via | Extrait |", "|---|:---:|:---:|---|"]
        for label, ok, via, snip in mentioned:
            L.append(f"| {esc(label)} | {'✅' if ok else '❌'} | {via} | {esc(snip) if ok else '_(absent)_'} |")
    else:
        L.append("_Aucune._")
    L += ["", "## C1. Recall EVALUES — dans un tableau mais non extrait", ""]
    if miss_e:
        L += ["| Methode | Ou | Via | Extrait |", "|---|---|:---:|---|"]
        L += [f"| {esc(l)} | {w} | {v} | {esc(s)} |" for l, w, v, s in miss_e]
    else:
        L.append("_Aucun._")
    L += ["", "## C2. Recall MENTIONNES — en prose seulement mais non extrait", ""]
    if miss_m:
        L += ["| Methode | Ou | Via | Extrait |", "|---|---|:---:|---|"]
        L += [f"| {esc(l)} | {w} | {v} | {esc(s)} |" for l, w, v, s in miss_m]
    else:
        L.append("_Aucun._")
    return "\n".join(L), (te, fe, tm, fm, len(miss_e), len(miss_m))


def render_summary(rows, TE, FE, TM, FM, SE, SM):
    TP, FP = TE + TM, FE + FM
    mp = TP / (TP + FP) if (TP + FP) else 1.0
    pe = TE / (TE + FE) if (TE + FE) else 1.0
    pm = TM / (TM + FM) if (TM + FM) else 1.0
    re_e = TE / (TE + SE) if (TE + SE) else 1.0
    re_m = TM / (TM + SM) if (TM + SM) else 1.0
    L = ["# Recap validation NS METHODS (provenance explicite)", "",
         f"Articles : **{len(rows)}**", "",
         "| Article | Eval | Ment | Prec.eval | Prec.ment | Manq.eval | Manq.ment |",
         "|---|---:|---:|:---:|:---:|---:|---:|"]
    for name, te, fe, tm, fm, se, sm in rows:
        pe_ = te / (te + fe) if (te + fe) else 1.0
        pm_ = tm / (tm + fm) if (tm + fm) else 1.0
        L.append(f"| {name} | {te+fe} | {tm+fm} | {pe_:.0%} | {pm_:.0%} | {se} | {sm} |")
    L += ["", "## Totaux (4 scores)", "", "| Metrique | Valeur |", "|---|---|",
          f"| Methodes EVALUEES | {TE + FE} |",
          f"| Methodes MENTIONNEES seulement | {TM + FM} |",
          f"| **Precision evalues** | **{pe:.1%}** |",
          f"| **Precision mentionnes** | **{pm:.1%}** |",
          f"| **Recall evalues (indicatif)** | **{re_e:.1%}** |",
          f"| **Recall mentionnes (indicatif)** | **{re_m:.1%}** |",
          f"| Precision globale (micro) | {mp:.1%} |",
          f"| Candidats manques (eval / ment) | {SE} / {SM} |"]
    return "\n".join(L)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    arts = load_articles()

    # Phase 1 : precision -> vocab bati UNIQUEMENT sur les items verifies corrects
    prec = {}
    vocab = {}
    for a in arts:
        ev, me, verified, counts = precision_pass(a)
        prec[a["slug"]] = (ev, me, counts)
        for k, lab in verified.items():
            vocab.setdefault(k, lab)
    print(f"Vocab global NS methods (items verifies corrects) = {len(vocab)}")

    # Phase 2 : recall contre le vocab verifie
    rows = []
    TE = FE = TM = FM = SE = SM = 0
    for a in arts:
        ev, me, counts = prec[a["slug"]]
        sus = recall_pass(a, vocab)
        report, (te, fe, tm, fm, se, sm) = render_article(a, ev, me, sus, counts)
        open(os.path.join(OUT_DIR, f"{a['slug']}.md"), "w", encoding="utf-8").write(report)
        rows.append((a["md_name"], te, fe, tm, fm, se, sm))
        TE += te; FE += fe; TM += tm; FM += fm; SE += se; SM += sm
    open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8").write(
        render_summary(rows, TE, FE, TM, FM, SE, SM))
    TP, FP = TE + TM, FE + FM
    print(f"{len(arts)} rapports -> {OUT_DIR}/")
    print(f"Evalues={TE+FE} Mentionnes={TM+FM}")
    print(f"Precision  evalues={TE/(TE+FE):.1%}  mentionnes={TM/(TM+FM):.1%}")
    print(f"Recall     evalues={TE/(TE+SE):.1%} (manq {SE})  mentionnes={TM/(TM+SM):.1%} (manq {SM})")


if __name__ == "__main__":
    main()
