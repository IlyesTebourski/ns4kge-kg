#!/usr/bin/env python3
"""
Validation de l'extraction du KG NS4KGE contre le texte source des articles (.md).

Pour chaque article on valide 4 categories d'entites extraites par le KG :
  - datasets      (Configurations[].Dataset)
  - metrics       (Configurations[].Metric)
  - nsmethods     (proposedNSMethod + mentionedNSMethods + Configurations[].NSMethod)
  - kgemodels     (proposedKGEModel + mentionedKGEModels + Configurations[].KGEModel)

PRECISION : chaque entite extraite est-elle presente dans le texte du .md ?
            (matching "modere" : casse / prefixes / separateurs tolerants,
             mot-entier pour les metriques courtes)

RECALL RELATIF : on construit le vocabulaire global (toutes entites extraites
            sur tous les articles) ; pour chaque article, les entites du vocab
            global NON extraites pour lui mais PRESENTES dans son texte sont
            signalees comme CANDIDATS a revoir (faux negatifs potentiels).
            Le recall affiche est donc INDICATIF (a valider manuellement).

Sorties : validation/reports/<article>.md  (un rapport lisible par article)
          validation/reports/_SUMMARY.md    (recap global + moyennes)
"""

import json
import glob
import os
import re
import html
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))   # parent holding ns4kge-kg/ and the local liste_mds/ corpus
MD_DIR = os.path.join(ROOT, "liste_mds")
KG_DIR = os.path.join(ROOT, "ns4kge-kg", "per_article")
OUT_DIR = os.path.join(HERE, "detailed_reports", "reports")

CATEGORIES = ["datasets", "metrics", "nsmethods", "kgemodels"]
CAT_LABEL = {
    "datasets": "Datasets",
    "metrics": "Metrics",
    "nsmethods": "NS Methods",
    "kgemodels": "KGE Models",
}

# Prefixes que le KG accole parfois aux entites (on les retire pour matcher).
STRIP_PREFIXES = ("dataset_", "model_", "metric_", "method_", "nsmethod_",
                  "kgemodel_", "kge_", "ns_")


# --------------------------------------------------------------------------
# Normalisation & matching
# --------------------------------------------------------------------------

def strip_kg_prefix(s: str) -> str:
    low = s.lower()
    for p in STRIP_PREFIXES:
        if low.startswith(p):
            return s[len(p):]
    return s


# Mots de liaison souvent omis dans le texte (matching "modere").
FILLER = {"negative", "neg", "based", "method", "approach", "technique", "strategy"}
# Tokens trop generiques : on ne relache PAS la contrainte si le nom se reduit a ca.
GENERIC = {"sampling", "sample", "ns", "model", "method", "loss"}
# Separateurs autorises entre tokens (inclut @ pour Hits@10).
SEP = r"[\s\-_/.@]*"


def tokens_of(entity: str):
    """Decoupe une entite en tokens alphanumeriques (@ traite comme separateur)."""
    e = strip_kg_prefix(entity).lower().strip()
    return re.findall(r"[a-z0-9]+", e)


def is_short_acronym(entity: str) -> bool:
    """Metrique/acronyme court -> matching mot-entier pour eviter les faux positifs."""
    toks = tokens_of(entity)
    if "@" in entity:
        return True  # ex: Hits@10
    if len(toks) != 1:
        return False
    t = toks[0]
    return len(t) <= 4 or any(ch.isdigit() for ch in t)


def _render_token(t: str) -> str:
    # hit / hits interchangeables (Hit@10 vs Hits@10)
    if t in ("hit", "hits"):
        return r"hits?"
    # famille sampling / sample / samples
    if t.startswith("sampl"):
        return r"sampl(?:e|es|ing)"
    # pluriel optionnel sur les mots longs (constraint(s), dataset(s)...)
    if len(t) >= 4 and t.isalpha():
        return re.escape(t) + r"s?"
    return re.escape(t)


def build_pattern(entity: str):
    """Construit une regex tolerante (separateurs + mots de liaison optionnels)."""
    toks = tokens_of(entity)
    if not toks:
        return None

    # On retire les mots de liaison des tokens *obligatoires*, sauf si le nom
    # se reduirait a rien / a un seul mot trop generique.
    required = [t for t in toks if t not in FILLER]
    if not required or (len(required) == 1 and required[0] in GENERIC):
        required = toks[:]

    # Entre deux tokens obligatoires : separateurs + 0..n mots de liaison optionnels.
    filler_alt = "|".join(sorted(FILLER, key=len, reverse=True))
    gap = SEP + r"(?:(?:" + filler_alt + r")" + SEP + r")*"

    core = gap.join(_render_token(t) for t in required)
    pat = r"(?<![A-Za-z0-9])" + core + r"(?![A-Za-z0-9])"
    return re.compile(pat, re.IGNORECASE)


def find_in_text(entity: str, text: str):
    """Retourne (True, snippet) si l'entite est trouvee dans le texte, sinon (False, '')."""
    pat = build_pattern(entity)
    if pat is None:
        return False, ""
    m = pat.search(text)
    if not m:
        return False, ""
    start = max(0, m.start() - 45)
    end = min(len(text), m.end() + 45)
    snip = text[start:end].replace("\n", " ")
    snip = re.sub(r"\s+", " ", snip).strip()
    return True, snip


# --------------------------------------------------------------------------
# Extraction depuis le KG
# --------------------------------------------------------------------------

def norm_key(entity: str) -> str:
    """Cle canonique pour dedupliquer / comparer les entites entre elles."""
    return "".join(tokens_of(entity))


def extract_entities(data: dict):
    """Renvoie {cat: {norm_key: surface_label}} pour un article."""
    out = {c: {} for c in CATEGORIES}

    def add(cat, val):
        if not val or not str(val).strip():
            return
        val = str(val).strip()
        k = norm_key(val)
        if not k:
            return
        # garde le libelle le plus 'propre' (le premier vu)
        out[cat].setdefault(k, val)

    add("nsmethods", data.get("proposedNSMethod"))
    add("kgemodels", data.get("proposedKGEModel"))
    for v in data.get("mentionedNSMethods", []) or []:
        add("nsmethods", v)
    for v in data.get("mentionedKGEModels", []) or []:
        add("kgemodels", v)

    exp = data.get("Experimentation", {}) or {}
    for c in exp.get("Configurations", []) or []:
        if not isinstance(c, dict):
            continue
        add("datasets", c.get("Dataset"))
        add("metrics", c.get("Metric"))
        add("kgemodels", c.get("KGEModel"))
        add("nsmethods", c.get("NSMethod"))
    return out


# --------------------------------------------------------------------------
# Chargement
# --------------------------------------------------------------------------

def load_articles():
    """Renvoie liste de dicts {slug, md_name, text, entities}."""
    md_files = {}
    for p in glob.glob(os.path.join(MD_DIR, "*.md")):
        slug = os.path.basename(p)[:-3].lower()
        md_files[slug] = p

    articles = []
    for p in sorted(glob.glob(os.path.join(KG_DIR, "*_merged.json"))):
        slug = os.path.basename(p)[: -len("_merged.json")]
        md_path = md_files.get(slug)
        if md_path is None:
            print(f"[WARN] pas de .md pour {slug}")
            continue
        data = json.load(open(p, encoding="utf-8"))
        text = open(md_path, encoding="utf-8").read()
        articles.append({
            "slug": slug,
            "md_name": os.path.basename(md_path),
            "title": (data.get("Article", {}) or {}).get("title", slug),
            "text": text,
            "entities": extract_entities(data),
        })
    return articles


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def build_global_vocab(articles):
    vocab = {c: {} for c in CATEGORIES}
    for a in articles:
        for c in CATEGORIES:
            for k, label in a["entities"][c].items():
                vocab[c].setdefault(k, label)
    return vocab


def validate_article(article, global_vocab):
    text = article["text"]
    res = {c: {"precision_rows": [], "recall_suspects": []} for c in CATEGORIES}
    counts = {c: {"tp": 0, "fp": 0, "suspect": 0} for c in CATEGORIES}

    for c in CATEGORIES:
        extracted = article["entities"][c]  # {key: label}
        # --- PRECISION ---
        for k, label in sorted(extracted.items(), key=lambda kv: kv[1].lower()):
            found, snip = find_in_text(label, text)
            res[c]["precision_rows"].append((label, found, snip))
            counts[c]["tp" if found else "fp"] += 1
        # --- RECALL RELATIF ---
        for k, label in sorted(global_vocab[c].items(), key=lambda kv: kv[1].lower()):
            if k in extracted:
                continue
            found, snip = find_in_text(label, text)
            if found:
                res[c]["recall_suspects"].append((label, snip))
                counts[c]["suspect"] += 1
    return res, counts


# --------------------------------------------------------------------------
# Rendu Markdown
# --------------------------------------------------------------------------

def esc(s: str) -> str:
    return s.replace("|", "\\|")


def render_article_report(article, res, counts):
    L = []
    L.append(f"# Validation — {article['md_name']}")
    L.append("")
    L.append(f"**Titre extrait :** {article['title']}")
    L.append("")

    tot_tp = sum(counts[c]["tp"] for c in CATEGORIES)
    tot_fp = sum(counts[c]["fp"] for c in CATEGORIES)
    tot_sus = sum(counts[c]["suspect"] for c in CATEGORIES)
    prec = tot_tp / (tot_tp + tot_fp) if (tot_tp + tot_fp) else 1.0
    rec = tot_tp / (tot_tp + tot_sus) if (tot_tp + tot_sus) else 1.0

    L.append("## Score global (article)")
    L.append("")
    L.append("| Metrique | Valeur |")
    L.append("|---|---|")
    L.append(f"| Entites extraites trouvees dans le texte (TP) | {tot_tp} |")
    L.append(f"| Extraites NON trouvees (FP -> erreur precision) | {tot_fp} |")
    L.append(f"| **Precision** | **{prec:.1%}** |")
    L.append(f"| Candidats faux negatifs (dans le texte, non extraits) | {tot_sus} |")
    L.append(f"| **Recall relatif (indicatif, a valider)** | **{rec:.1%}** |")
    L.append("")

    for c in CATEGORIES:
        rows = res[c]["precision_rows"]
        if not rows and not res[c]["recall_suspects"]:
            continue
        cc = counts[c]
        p = cc["tp"] / (cc["tp"] + cc["fp"]) if (cc["tp"] + cc["fp"]) else 1.0
        r = cc["tp"] / (cc["tp"] + cc["suspect"]) if (cc["tp"] + cc["suspect"]) else 1.0
        L.append(f"## {CAT_LABEL[c]}  —  precision {p:.0%} · recall~ {r:.0%}")
        L.append("")
        L.append("### Precision : entites extraites par le KG")
        L.append("")
        L.append("| Entite extraite | Trouvee dans le .md ? | Extrait de texte |")
        L.append("|---|:---:|---|")
        for label, found, snip in rows:
            mark = "✅ oui" if found else "❌ NON"
            snip_disp = esc(snip) if found else "_(absent du texte)_"
            L.append(f"| {esc(label)} | {mark} | {snip_disp} |")
        L.append("")
        sus = res[c]["recall_suspects"]
        if sus:
            L.append("### ⚠️ Candidats faux negatifs (present dans le texte, PAS extrait)")
            L.append("")
            L.append("| Entite (vocab global) | Extrait de texte |")
            L.append("|---|---|")
            for label, snip in sus:
                L.append(f"| {esc(label)} | {esc(snip)} |")
            L.append("")
        else:
            L.append("_Aucun candidat faux negatif pour cette categorie._")
            L.append("")

    return "\n".join(L), (tot_tp, tot_fp, tot_sus, prec, rec)


def render_summary(summary_rows, totals):
    L = []
    L.append("# Recap global de validation KG vs articles")
    L.append("")
    L.append(f"Articles valides : **{len(summary_rows)}**")
    L.append("")
    L.append("## Par article")
    L.append("")
    L.append("| Article | TP | FP | Precision | Candidats FN | Recall~ |")
    L.append("|---|---:|---:|:---:|---:|:---:|")
    for name, tp, fp, sus, prec, rec in summary_rows:
        L.append(f"| {name} | {tp} | {fp} | {prec:.0%} | {sus} | {rec:.0%} |")
    L.append("")

    TP, FP, SUS = totals
    micro_p = TP / (TP + FP) if (TP + FP) else 1.0
    micro_r = TP / (TP + SUS) if (TP + SUS) else 1.0
    macro_p = sum(r[4] for r in summary_rows) / len(summary_rows)
    macro_r = sum(r[5] for r in summary_rows) / len(summary_rows)

    L.append("## Totaux")
    L.append("")
    L.append("| Metrique | Valeur |")
    L.append("|---|---|")
    L.append(f"| Total TP (extraites & trouvees) | {TP} |")
    L.append(f"| Total FP (extraites & absentes) | {FP} |")
    L.append(f"| Total candidats faux negatifs | {SUS} |")
    L.append(f"| **Precision micro** (toutes entites confondues) | **{micro_p:.1%}** |")
    L.append(f"| **Precision macro** (moyenne des articles) | **{macro_p:.1%}** |")
    L.append(f"| **Recall relatif micro** (indicatif) | **{micro_r:.1%}** |")
    L.append(f"| **Recall relatif macro** (indicatif) | **{macro_r:.1%}** |")
    L.append("")
    L.append("> Le recall est **indicatif** : les 'candidats faux negatifs' sont des "
             "entites du vocabulaire global presentes dans le texte mais non extraites "
             "pour cet article. Certaines sont de vrais oublis, d'autres de simples "
             "mentions (related work, etc.) — a valider a la main.")
    return "\n".join(L)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    articles = load_articles()
    global_vocab = build_global_vocab(articles)

    print(f"Vocab global : " + ", ".join(
        f"{CAT_LABEL[c]}={len(global_vocab[c])}" for c in CATEGORIES))

    summary_rows = []
    TP = FP = SUS = 0
    for a in articles:
        res, counts = validate_article(a, global_vocab)
        report, (tp, fp, sus, prec, rec) = render_article_report(a, res, counts)
        out_path = os.path.join(OUT_DIR, f"{a['slug']}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report)
        summary_rows.append((a["md_name"], tp, fp, sus, prec, rec))
        TP += tp; FP += fp; SUS += sus

    summary = render_summary(summary_rows, (TP, FP, SUS))
    with open(os.path.join(OUT_DIR, "_SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"\n{len(articles)} rapports ecrits dans {OUT_DIR}/")
    print(f"Precision micro = {TP/(TP+FP):.1%}   "
          f"Recall relatif micro = {TP/(TP+SUS):.1%}   (voir _SUMMARY.md)")


if __name__ == "__main__":
    main()
