# -*- coding: utf-8 -*-
"""Editorial-prose similarity: every dist/ page against every other, and against
the four sibling hubs plus the parent brand site.

What is compared
----------------
Only prose paragraphs inside <main>. Everything below is excluded, because the
prompt excludes legal and structural boilerplate from the editorial comparison
and because these blocks are *meant* to be identical wherever they appear:

  header / nav / footer / breadcrumbs / page head
  the lead form, the call-to-action block and the click-to-call strip
  tables and their captions (the Cost Index is a published dataset; the permit
      summary tables quote official rules verbatim)
  photo captions (the same photo carries the same alt text everywhere)
  the sources list, the "last reviewed" meta line and the update note
  the related-pages pill navigation
  a short list of standing sentences (consent, disclosure, gallery notice)

Threshold: any pair sharing more than 15% of the smaller page's 8-grams of
editorial prose is flagged for rewrite.
"""
import html as htmlmod
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
DIST = HERE / "dist"
OUT = HERE.parent / "audit" / "similarity-report.md"
THRESHOLD = 15.0

SIBLINGS = {
    "ocoeeconcrete.com": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\Projetos\ocoeeconcrete"),
    "windermereconcrete.com": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\Projetos\windermereconcrete"),
    "lakewoodranchconcretefl.com": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\Projetos\lakewoodranchconcretefl"),
    "grovelandconcrete.com": pathlib.Path(r"C:\Users\luana\Documents\Codex\2026-09-07\groveland-concrete\site\dist"),
    "gcmbestservicescorp.com": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\gcm-site"),
}

# Blocks removed before any text is extracted.
_DROP_BLOCKS = [
    r"<script.*?</script>", r"<style.*?</style>",
    r"<header.*?</header>", r"<footer.*?</footer>", r"<nav[^>]*>.*?</nav>",
    r'<form[^>]*>.*?</form>',
    r'<div class="table-wrap">.*?</div>',
    r"<table.*?</table>", r"<caption.*?</caption>",
    r"<figcaption.*?</figcaption>",
    r'<div class="sources">.*?</div>',
    r'<p class="meta-line">.*?</p>',
    r'<p class="changelog">.*?</p>',
    r'<p class="note">.*?</p>',
    r'<ul class="pill-nav">.*?</ul>',
    r'<div class="wrap page-head">.*?</div>',
    r'<div class="data-strip">.*?</div>',
    r'<div class="cta-row">.*?</div>',
    r'<div class="svc-call">.*?</div>',
    r'<p class="cta-phone">.*?</p>',
]
# Standing sentences that legitimately repeat.
BOILER = [
    "by sending this form you agree", "we do not sell your information",
    "kissimmee concrete installs and repairs", "sources checked for this page",
    "what changed in this update", "request a free estimate",
    "job photos from our crews", "images marked", "see the full gallery",
    "tell us the size, the surface you have now", "standard message rates may apply",
    "get a written estimate for your project", "no pressure calls",
    "every lot gets its own base", "use these for finish and pattern ideas",
    "concept rendering", "not a quote",
]


def prose(html):
    """Editorial paragraph text inside <main>, boilerplate removed."""
    m = re.search(r"<main[^>]*>(.*?)</main>", html, flags=re.S)
    body = m.group(1) if m else html
    for pat in _DROP_BLOCKS:
        body = re.sub(pat, " ", body, flags=re.S)
    paras = re.findall(r"<(p|li)\b[^>]*>(.*?)</\1>", body, flags=re.S)
    text = " ".join(p[1] for p in paras)
    text = re.sub(r"<[^>]+>", " ", text)
    text = htmlmod.unescape(re.sub(r"\s+", " ", text)).lower()
    for b in BOILER:
        text = text.replace(b, " ")
    return re.sub(r"[^a-z0-9 ]+", " ", text)


def grams(text, n=8):
    w = text.split()
    return set(" ".join(w[i:i + n]) for i in range(len(w) - n + 1))


def load(root, pattern="*.html"):
    out = {}
    for f in sorted(root.rglob(pattern)):
        try:
            g = grams(prose(f.read_text(encoding="utf-8", errors="ignore")))
        except Exception:
            continue
        if g:
            out[str(f.relative_to(root)).replace("\\", "/")] = g
    return out


def main():
    mine = {k: v for k, v in load(DIST).items() if not k.endswith("404.html")}
    routes = list(mine)
    lines = ["# Editorial similarity report (8-grams of prose, boilerplate excluded)", "",
             "Compared: paragraph and list text inside `<main>` only. Tables, captions, the Cost Index,",
             "quoted ordinance text, forms, the call-to-action, source lists, photo captions, the",
             "\"last reviewed\" line and the update note are excluded as boilerplate or as published data",
             "that is meant to be identical wherever it appears.", "",
             "Threshold: a pair sharing more than %.0f%% of the smaller page's prose 8-grams is flagged." % THRESHOLD, ""]
    flagged = []
    pairs = []
    for i in range(len(routes)):
        a = mine[routes[i]]
        for j in range(i + 1, len(routes)):
            b = mine[routes[j]]
            s = len(a & b)
            if not s:
                continue
            pct = s / max(1, min(len(a), len(b))) * 100
            pairs.append((pct, s, routes[i], routes[j]))
    pairs.sort(reverse=True)
    flagged = [p for p in pairs if p[0] > THRESHOLD]
    lines += ["## Within kissimmeeconcrete.com", "",
              "Pages compared: %d. Pairs sharing any prose: %d. Pairs above threshold: %d." % (len(routes), len(pairs), len(flagged)), "",
              "| Page A | Page B | shared 8-grams | %% of smaller |", "|---|---|---|---|"]
    for pct, s, a, b in pairs[:30]:
        lines.append("| %s | %s | %d | %.1f%% |" % (a, b, s, pct))
    if not pairs:
        lines.append("| (none) | (none) | 0 | 0.0%% |")

    sib_flags = 0
    for name, root in SIBLINGS.items():
        if not root.exists():
            lines += ["", "## vs %s" % name, "", "(folder not found: %s)" % root]
            continue
        theirs = load(root)
        allg = set()
        for g in theirs.values():
            allg |= g
        hits = []
        for r, g in mine.items():
            shared = g & allg
            if shared:
                pct = len(shared) / max(1, len(g)) * 100
                hits.append((len(shared), pct, r, sorted(shared)[:2]))
        hits.sort(reverse=True)
        over = [h for h in hits if h[1] > THRESHOLD]
        sib_flags += len(over)
        lines += ["", "## vs %s (%d pages)" % (name, len(theirs)), "",
                  "Our pages sharing any prose 8-gram: %d. Above threshold: %d." % (len(hits), len(over)), "",
                  "| Our page | shared | %% of our page | sample |", "|---|---|---|---|"]
        if not hits:
            lines.append("| (none) | 0 | 0.0%% | |")
        for n, pct, r, sample in hits[:20]:
            lines.append("| %s | %d | %.2f%% | %s |" % (r, n, pct, " / ".join(sample)))

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:40]))
    print("\nintra-site pairs above %.0f%%: %d | sibling pages above threshold: %d -> %s" % (THRESHOLD, len(flagged), sib_flags, OUT))
    sys.exit(1 if (flagged or sib_flags) else 0)


if __name__ == "__main__":
    main()
