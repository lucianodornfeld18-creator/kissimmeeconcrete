# -*- coding: utf-8 -*-
"""Technical crawl of dist/: links, orphans, titles/H1/meta uniqueness and length,
canonical, JSON-LD validity, HTML size, images with width/height, sitemap match.
Writes audit/crawl-report.md; exit 1 on hard failures.
"""
import html as htmlmod
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).parent
DIST = HERE / "dist"
OUT = HERE.parent / "audit" / "crawl-report.md"


def route_of(f):
    r = "/" + f.relative_to(DIST).parent.as_posix()
    return "/" if r in ("/", "/.") else r.rstrip("/") + "/"


def main():
    pages = {}
    for f in DIST.rglob("index.html"):
        pages[route_of(f)] = f.read_text(encoding="utf-8")
    hard, warn = [], []
    titles, h1s, descs, firsts = Counter(), Counter(), Counter(), Counter()
    inbound = defaultdict(set)
    all_links = set()
    sitemap = set(re.findall(r"<loc>https://kissimmeeconcrete\.com(/[^<]*)</loc>", (DIST / "sitemap.xml").read_text(encoding="utf-8")))
    static_files = {"/" + p.relative_to(DIST).as_posix() for p in DIST.rglob("*") if p.is_file()}
    for route, html in pages.items():
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        title = htmlmod.unescape(t.group(1).strip()) if t else ""
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S)
        d = re.search(r'<meta name="description" content="(.*?)"', html)
        desc = htmlmod.unescape(d.group(1)) if d else ""
        can = re.search(r'<link rel="canonical" href="(.*?)"', html)
        noindex = "noindex" in (re.search(r'<meta name="robots" content="(.*?)"', html) or [None, ""])[1] if re.search(r'<meta name="robots" content="(.*?)"', html) else False
        titles[title] += 1; descs[desc] += 1
        if len(h1) != 1:
            hard.append(f"{route}: {len(h1)} H1")
        else:
            h1s[htmlmod.unescape(re.sub('<[^>]+>', '', h1[0])).strip()] += 1
        if not title:
            hard.append(f"{route}: missing title")
        elif len(title) > 65:
            warn.append(f"{route}: title {len(title)} chars")
        if not desc:
            hard.append(f"{route}: missing description")
        elif not (110 <= len(desc) <= 165):
            warn.append(f"{route}: description {len(desc)} chars")
        if not can or can.group(1) != "https://kissimmeeconcrete.com" + route:
            hard.append(f"{route}: canonical mismatch ({can.group(1) if can else 'none'})")
        if (route in sitemap) == noindex:
            hard.append(f"{route}: sitemap/noindex mismatch")
        size = len(html.encode("utf-8"))
        if size > 150 * 1024:
            warn.append(f"{route}: HTML {size // 1024} KB > 150 KB")
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                hard.append(f"{route}: JSON-LD parse error {e}")
        for img in re.findall(r"<img[^>]+>", html):
            if 'width="' not in img or 'height="' not in img:
                warn.append(f"{route}: img without width/height: {img[:60]}")
            if 'alt="' not in img:
                hard.append(f"{route}: img without alt")
        main_html = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
        mtxt = htmlmod.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", main_html.group(1) if main_html else ""))).strip()
        firsts[" ".join(mtxt.split()[:12])] += 1
        html_nojs = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
        for href in re.findall(r'href="([^"]+)"', html_nojs):
            if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("sms:") or href.startswith("#"):
                continue
            h = href.split("#")[0].split("?")[0]
            if not h:
                continue
            all_links.add(h)
            if h.endswith("/"):
                inbound[h].add(route)
                if h not in pages:
                    hard.append(f"{route}: broken link {h}")
            else:
                if h not in static_files:
                    hard.append(f"{route}: broken asset {h}")
    for k, c in titles.items():
        if c > 1:
            hard.append(f"duplicate title x{c}: {k}")
    for k, c in h1s.items():
        if c > 1:
            hard.append(f"duplicate H1 x{c}: {k}")
    for k, c in descs.items():
        if c > 1:
            hard.append(f"duplicate description x{c}: {k[:60]}")
    for k, c in firsts.items():
        if c > 1 and k:
            warn.append(f"same first 12 words x{c}: {k}")
    noindex_routes = {r for r, h in pages.items() if 'content="noindex' in h}
    for route in pages:
        if route == "/" or route == "/404/" or route in noindex_routes:
            continue
        if not inbound.get(route):
            hard.append(f"orphan: {route}")
    for s in sitemap:
        if s not in pages:
            hard.append(f"sitemap URL without page: {s}")
    lines = [f"# Crawl report", "", f"Pages: {len(pages)} · sitemap URLs: {len(sitemap)} · hard: {len(hard)} · warnings: {len(warn)}", "", "## Hard failures", ""] + [f"- {x}" for x in hard] + ["", "## Warnings", ""] + [f"- {x}" for x in warn]
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:120]))
    print(f"... -> {OUT}")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
