# -*- coding: utf-8 -*-
"""Style + network-fingerprint checker for dist/ (prompt sections 2.2 and 9.2).

python qa_style.py            -> report to stdout + audit/style-report.md
Exit code 1 if any hard failure (forbidden phrase, sibling fingerprint, placeholder).

Single-word entries in FORBIDDEN are matched on word boundaries, so a quoted
official phrase such as Polk County's "elevated slabs" or Solivita's "utilized
by the original builder" is not a false positive for "elevate" / "utilize".
"""
import html as htmlmod
import pathlib
import re
import statistics
import sys

DIST = pathlib.Path(__file__).parent / "dist"
OUT = pathlib.Path(__file__).parent.parent / "audit" / "style-report.md"

FORBIDDEN = [
    "in today's fast-paced world", "whether you're", "whether you are looking", "look no further", "it's important to note", "it is important to note",
    "it's worth noting", "in conclusion", "ultimately,", "at the end of the day", "when it comes to", "elevate", "seamless", "unlock", "delve",
    "robust", "leverage", "game-changer", "transform your outdoor space", "dream outdoor space", "backyard oasis", "backyard paradise",
    "we understand that", "our team of experts", "top-notch", "state-of-the-art", "cutting-edge", "meticulous", "comprehensive", "hassle-free",
    "peace of mind", "stand the test of time", "a testament to", "nestled", "vibrant", "boasts", "tapestry of", "not only", "from start to finish",
    "one-stop shop", "we've got you covered", "enhance", "utilize", "in order to", "let's dive in", "here's the thing", "why choose us",
]
ONCE_PER_PAGE = ["ensure"]
FINGERPRINTS = [
    "38-point", "42-point", "48-point", "-point installation", "-point install", "our four promises", "straight answers before you spend",
    "in plain english", "built local since", "poured right", "built to last", "craft code", "estate standard", "outlasts the mortgage",
    "every service we bring to", "homeowners ask us", "concrete specialists serving", "concrete services we offer in", "paver specialists serving",
    "paver services we offer in", "neighborhoods & zip codes we serve", "neighborhoods and zip codes we serve", "township grid",
]
PLACEHOLDERS = [r"\{\{[A-Z_]+\}\}", r"lorem ipsum", r"\bTODO\b", r"XXX-XXXX", r"\(555\)"]


def visible(html):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<footer.*?</footer>|<nav[^>]*>.*?</nav>", " ", html, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmlmod.unescape(re.sub(r"\s+", " ", t)).strip()


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) > 2]


FACT_RE = re.compile(r"(\$\d|\d+(\.\d+)?\s?(%|in\b|inch|inches|ft\b|feet|sq ft|psi|mm|°F|days?|hours?|weeks?|years?|miles?|mph|yd)|§|\b(19|20)\d\d\b|\b[A-Z][a-z]+ (County|Code|Statute|Building|Village|Resort|Lakes)\b)")


def check_page(path, html):
    text = visible(html)
    low = text.lower()
    issues, warnings = [], []
    for ph in FORBIDDEN:
        if " " in ph or not ph.isalpha():
            hit = ph in low
        else:
            hit = re.search(r"\b" + re.escape(ph) + r"\b", low) is not None
        if hit:
            issues.append("forbidden phrase: '%s'" % ph)
    for fp in FINGERPRINTS:
        if fp in low:
            issues.append("sibling fingerprint: '%s'" % fp)
    for pat in PLACEHOLDERS:
        if re.search(pat, html):
            issues.append("placeholder: /%s/" % pat)
    for w in ONCE_PER_PAGE:
        n = len(re.findall(r"\b" + w + r"\b", low))
        if n > 1:
            warnings.append("'%s' used %dx" % (w, n))
    sents = sentences(text)
    words = text.split()
    if len(words) > 250 and sents:
        lens = [len(s.split()) for s in sents]
        sd = statistics.pstdev(lens)
        if sd < 6:
            warnings.append("low sentence-length variety (sd=%.1f)" % sd)
        facts = len(FACT_RE.findall(text))
        per150 = facts / (len(words) / 150)
        if per150 < 1.0:
            warnings.append("fact density %.2f per 150 words (target >= 1)" % per150)
    colon_h2 = re.findall(r"<h2[^>]*>([^<]*: [^<]*)</h2>", html)
    if colon_h2:
        warnings.append("H2 in 'X: Y' format: " + colon_h2[0][:60])
    if text.count("—") > 6:
        warnings.append("%d em dashes" % text.count("—"))
    return len(words), issues, warnings


def main():
    rows, hard = [], 0
    for f in sorted(DIST.rglob("index.html")):
        route = "/" + f.relative_to(DIST).parent.as_posix().strip(".") + "/"
        route = route.replace("//", "/")
        words, issues, warnings = check_page(f, f.read_text(encoding="utf-8"))
        hard += len(issues)
        rows.append((route, words, issues, warnings))
    lines = ["# Style & fingerprint report", "", "Pages: %d · hard failures: %d" % (len(rows), hard), "", "| Route | Words | Failures | Warnings |", "|---|---|---|---|"]
    for route, words, issues, warnings in rows:
        lines.append("| %s | %d | %s | %s |" % (route, words, "; ".join(issues) or "none", "; ".join(warnings) or "none"))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    for route, words, issues, warnings in rows:
        if issues or warnings:
            print(route, words, "FAIL" if issues else "warn", issues, warnings)
    print("\n%d pages, %d hard failures -> %s" % (len(rows), hard, OUT))
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
