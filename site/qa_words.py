# -*- coding: utf-8 -*-
"""Word count per page vs. the floors and targets in the prompt (section 5.3).

python qa_words.py            -> summary by page kind + audit/word-report.md
python qa_words.py --under    -> list every page below its floor, worst first
"""
import collections
import html as htmlmod
import os
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).parent
DIST = HERE / "dist"
OUT = HERE.parent / "audit" / "word-report.md"

# kind -> (floor, target_high). Floors come from the stcloudflconcrete.com benchmark
# measured on 2026-09-10; targets are the prompt's 25-40% above that.
TARGET = {
    "home": (3358, 4500), "pillar": (1470, 3000), "service": (1470, 2600),
    "cityservice": (1200, 1800), "city": (1144, 2400), "county": (2000, 3000),
    "pricing": (2000, 3200), "guide": (1500, 3000), "compare": (1500, 3000),
    "faq": (1000, 3000), "permit": (800, 2000), "hoa": (800, 2000),
    "tool": (600, 2000), "page": (400, 1400),
}


def visible(html):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<footer.*?</footer>|<nav[^>]*>.*?</nav>", " ", html, flags=re.S)
    # click-to-call chrome repeats on every page; it is not editorial word count
    t = re.sub(r'<div class="topbar">.*?</div></div>|<div class="svc-call">.*?</div>|<div class="mobile-cta">.*?</div>|<p class="cta-phone">.*?</p>', " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmlmod.unescape(re.sub(r"\s+", " ", t)).strip()


def kind_of(route):
    if route == "/":
        return "home"
    if route.startswith(("/concrete/", "/pavers/", "/coatings/", "/exterior/")):
        n = route.strip("/").count("/")
        return "cityservice" if n == 2 else ("pillar" if n == 0 else "service")
    if route.startswith("/areas/"):
        return "county" if "county" in route else ("page" if route == "/areas/" else "city")
    for prefix, k in [("/pricing/", "pricing"), ("/permits/", "permit"), ("/hoa/", "hoa"),
                      ("/compare/", "compare"), ("/tools/", "tool"), ("/guides/", "guide"), ("/faq", "faq")]:
        if route.startswith(prefix):
            return k
    return "page"


def rows():
    out = []
    for f in DIST.rglob("index.html"):
        rel = os.path.relpath(f.parent, DIST).replace(os.sep, "/")
        route = "/" if rel == "." else "/" + rel + "/"
        out.append((route, len(visible(f.read_text(encoding="utf-8")).split())))
    return sorted(out)


def main():
    data = rows()
    groups = collections.defaultdict(list)
    for route, w in data:
        groups[kind_of(route)].append((route, w))
    lines = ["# Word-count report", "", "Floors are the stcloudflconcrete.com benchmark per page type; targets are the prompt's range.", "",
             "| Kind | Pages | Median | Min | Max | Floor | Target | Below floor |", "|---|---|---|---|---|---|---|---|"]
    total = 0
    for k in ["home", "pillar", "service", "cityservice", "city", "county", "pricing", "permit", "hoa", "compare", "tool", "guide", "faq", "page"]:
        v = [w for _, w in groups.get(k, [])]
        if not v:
            continue
        total += sum(v)
        lo, hi = TARGET[k]
        lines.append("| %s | %d | %d | %d | %d | %d | %d-%d | %d |" % (k, len(v), statistics.median(v), min(v), max(v), lo, lo, hi, sum(1 for x in v if x < lo)))
    lines += ["", "Total indexable pages: %d · total words: %d" % (len(data), total), "", "## Pages below their floor", "", "| Route | Kind | Words | Floor | Gap |", "|---|---|---|---|---|"]
    under = []
    for route, w in data:
        k = kind_of(route)
        lo = TARGET[k][0]
        if w < lo and route not in ("/404/", "/thank-you/"):
            under.append((lo - w, route, k, w, lo))
    for gap, route, k, w, lo in sorted(under, reverse=True):
        lines.append("| %s | %s | %d | %d | %d |" % (route, k, w, lo, gap))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:24]))
    print("\n%d pages below floor -> %s" % (len(under), OUT))
    if "--under" in sys.argv:
        for gap, route, k, w, lo in sorted(under, reverse=True):
            print("%-52s %-12s %5d  floor %5d  gap %5d" % (route, k, w, lo, gap))


if __name__ == "__main__":
    main()
