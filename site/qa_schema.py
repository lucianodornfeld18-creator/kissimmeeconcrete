# -*- coding: utf-8 -*-
"""Schema, weight and asset verification for dist/.

Checks that every JSON-LD block parses, that the types used are the ones we
intend, that LocalBusiness / PostalAddress / GeoCoordinates / AggregateRating /
Review never appear (no verified entity, address or reviews yet), that the site
name is exactly the public name everywhere, and that page weight and images are
within the limits in the prompt.
"""
import collections
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
DIST = HERE / "dist"
OUT = HERE.parent / "audit" / "schema-report.md"
PUBLIC_NAME = "Kissimmee Concrete"
BANNED_TYPES = {"LocalBusiness", "HomeAndConstructionBusiness", "GeneralContractor",
                "PostalAddress", "GeoCoordinates", "AggregateRating", "Review", "Rating"}
MAX_HTML_KB = 150


def main():
    types = collections.Counter()
    hard, warn = [], []
    weights = []
    img_total = 0
    for f in sorted(DIST.rglob("index.html")):
        rel = os.path.relpath(f.parent, DIST).replace(os.sep, "/")
        route = "/" if rel == "." else "/" + rel + "/"
        html = f.read_text(encoding="utf-8")
        kb = len(html.encode("utf-8")) / 1024
        weights.append((kb, route))
        if kb > MAX_HTML_KB:
            hard.append("%s: HTML %.0f KB over the %d KB limit" % (route, kb, MAX_HTML_KB))
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        if not blocks:
            hard.append("%s: no JSON-LD" % route)
        for b in blocks:
            try:
                data = json.loads(b)
            except Exception as e:
                hard.append("%s: JSON-LD parse error %s" % (route, e))
                continue
            for node in (data if isinstance(data, list) else [data]):
                t = node.get("@type")
                for tt in (t if isinstance(t, list) else [t]):
                    types[tt] += 1
                    if tt in BANNED_TYPES:
                        hard.append("%s: banned schema type %s" % (route, tt))
                blob = json.dumps(node)
                for key in ("aggregateRating", "review", "address", "geo", "priceRange"):
                    if '"%s"' % key in blob:
                        hard.append("%s: schema contains %s" % (route, key))
        # site name consistency
        og = re.search(r'<meta property="og:site_name" content="(.*?)"', html)
        if not og or og.group(1) != PUBLIC_NAME:
            hard.append("%s: og:site_name is %r" % (route, og.group(1) if og else None))
        for bad in (r"Kissimmee Concrete (?:FL|Florida|LLC|Inc|Co\.|Company|Contractors|Services|Pros|Experts|Group|24/7)",
                    r"#1\s", r"Best Concrete", r"Top-Rated"):
            m = re.search(bad, html)
            if m:
                hard.append("%s: forbidden brand variant %r" % (route, m.group(0)))
        imgs = re.findall(r"<img[^>]+>", html)
        img_total += len(imgs)
        for img in imgs:
            if 'loading="lazy"' not in img and 'fetchpriority="high"' not in img:
                warn.append("%s: img without lazy or priority hint" % route)

    static = DIST / "static"
    big = [(p.stat().st_size / 1024, str(p.relative_to(DIST))) for p in static.rglob("*") if p.is_file() and p.stat().st_size > 400 * 1024]
    for kb, name in big:
        warn.append("large asset %.0f KB %s" % (kb, name))

    for required in ["robots.txt", "sitemap.xml", "llms.txt", "llms-full.txt", "feed.xml",
                     "site.webmanifest", "favicon.ico", "api/cost-index.json", "api/cost-index.csv",
                     "_headers", "_redirects", "404.html"]:
        if not (DIST / required).exists():
            hard.append("missing required file: %s" % required)

    weights.sort(reverse=True)
    lines = ["# Schema, weight and asset report", "",
             "Pages: %d · hard: %d · warnings: %d" % (len(weights), len(hard), len(warn)), "",
             "## Schema types used", "", "| Type | Count |", "|---|---|"]
    for t, n in types.most_common():
        lines.append("| %s | %d |" % (t, n))
    lines += ["", "## Heaviest pages", "", "| KB | Route |", "|---|---|"]
    for kb, route in weights[:10]:
        lines.append("| %.0f | %s |" % (kb, route))
    lines += ["", "Images rendered across the site: %d" % img_total, "",
              "## Hard failures", ""] + (["- " + x for x in hard] or ["(none)"]) + ["", "## Warnings", ""] + (["- " + x for x in sorted(set(warn))] or ["(none)"])
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:30]))
    print("\nhard: %d  warnings: %d -> %s" % (len(hard), len(set(warn)), OUT))
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
