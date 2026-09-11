# -*- coding: utf-8 -*-
"""Static site builder for kissimmeeconcrete.com: python build.py -> dist/"""
import base64
import csv
import datetime
import hashlib
import html as htmlmod
import importlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from templates import render_page, SITE_JS
from _data import BASE_URL, DOMAIN, PUBLIC_NAME, BUSINESS, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, TOOLS, TOOL_ORDER, GUIDES, GUIDE_ORDER, COMPARISONS, COST_INDEX, COST_INDEX_RELEASE, LAUNCH_DATE, EMAIL

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"
CONTENT_MODULES = [
    "content_home", "content_pillars", "content_services_concrete", "content_services_pavers", "content_services_coatings",
    "content_cityservice", "content_cities", "content_cities_tier2", "content_counties", "content_pricing", "content_permits",
    "content_hoa", "content_compare", "content_tools", "content_faq", "content_guides", "content_pages",
]


def _git_date(path, first=False):
    val = LAUNCH_DATE if first else datetime.date.today().isoformat()
    try:
        args = ["git", "log", "--format=%cI", "--follow", "--", str(path)] if first else ["git", "log", "-1", "--format=%cI", "--", str(path)]
        out = subprocess.run(args, capture_output=True, text=True, cwd=ROOT, timeout=10).stdout.strip().splitlines()
        if out:
            val = (out[-1] if first else out[0])[:10]
    except Exception:
        pass
    return val


def load_pages():
    pages, seen = [], {}
    for mod_name in CONTENT_MODULES:
        try:
            mod = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            print(f"[build] SKIP  {mod_name} (not written yet)")
            continue
        importlib.reload(mod)
        mod_pages = mod.get_pages()
        for p in mod_pages:
            if p["route"] in seen:
                raise SystemExit(f"[build] DUPLICATE ROUTE {p['route']} in {seen[p['route']]} and {mod_name}")
            seen[p["route"]] = mod_name
            p["_module"] = mod_name
            p["_lastmod"] = _git_date(ROOT / f"{mod_name}.py")
            p["_published"] = _git_date(ROOT / f"{mod_name}.py", first=True)
            pages.append(p)
        print(f"[build] OK    {mod_name} -> {len(mod_pages)} page(s)")
    return pages


def write_page(page):
    out_dir = DIST if page["route"] == "/" else DIST / page["route"].strip("/")
    out_dir.mkdir(parents=True, exist_ok=True)
    html = render_page(page)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    return html


def write_static():
    dst = DIST / "static"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT / "static", dst)
    shutil.copy(ROOT / "static" / "site.js", DIST / SITE_JS.lstrip("/"))
    shutil.copy(ROOT / "static" / "favicon.ico", DIST / "favicon.ico")


def indexnow_key():
    f = ROOT / "indexnow-key.txt"
    if not f.exists():
        f.write_text(hashlib.sha256((DOMAIN + str(time.time())).encode()).hexdigest()[:32], encoding="utf-8")
    key = f.read_text(encoding="utf-8").strip()
    (DIST / f"{key}.txt").write_text(key, encoding="utf-8")
    return key


def write_robots():
    (DIST / "robots.txt").write_text(f"""# kissimmeeconcrete.com — search and answer-engine crawlers are welcome.
User-agent: *
Allow: /
Disallow: /thank-you/
Disallow: /api/contact

User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Applebot
Allow: /
User-agent: DuckDuckBot
Allow: /
# Training crawlers: allowed by default; owner may flip these to Disallow.
User-agent: GPTBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
""", encoding="utf-8")


def write_sitemap(pages):
    urls = []
    for p in pages:
        if p.get("noindex"):
            continue
        urls.append(f"  <url><loc>{BASE_URL}{p['route']}</loc><lastmod>{p['_lastmod']}</lastmod></url>")
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")


def _visible_text(html):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<footer.*?</footer>|<nav.*?</nav>", " ", html, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmlmod.unescape(re.sub(r"\s+", " ", t)).strip()


def write_llms(pages, rendered):
    def block(title, items):
        return [f"## {title}", ""] + [f"- [{n}]({BASE_URL}{r})" + (f": {s}" if s else "") for n, r, s in items] + [""]
    lines = [f"# {PUBLIC_NAME}", "", f"> {BUSINESS['blurb']}", "", f"Website: {BASE_URL}", f"Email: {EMAIL}", f"Service area: {BUSINESS['service_area_short']}.",
             "Facts we publish with sources: Osceola County driveway width rule (§22-50.6, 24 ft max, permit required), City of Kissimmee driveway/sidewalk permit process, St. Cloud paver rule (refer to Public Works), Polk County slab/driveway permit rules and the Concrete Driveway Paver Release Form, Florida s. 489.117(4)(a) (no state or local license for driveway, paver or stucco work), NOAA 1991-2020 normals for Kissimmee 2 (June-September average 15-18 rain days a month), USDA soils (Smyrna, Myakka, Immokalee, Basinger fine sands in Osceola; Candler sand on the Polk ridge).",
             f"Cost Index: {COST_INDEX_RELEASE['label']} release, planning ranges only, machine-readable at {BASE_URL}/api/cost-index.json (CC BY 4.0).", ""]
    lines += block("Services", [(SERVICES[k]["name"], SERVICES[k]["route"], SERVICES[k]["short"]) for k in SERVICE_ORDER])
    lines += block("Service areas", [(CITIES[k]["name"], CITIES[k]["route"], f"{CITIES[k]['county']} County") for k in CITY_ORDER])
    lines += block("Tools", [(TOOLS[k]["name"], TOOLS[k]["route"], TOOLS[k]["short"]) for k in TOOL_ORDER])
    lines += block("Guides", [(GUIDES[k]["name"], GUIDES[k]["route"], "") for k in GUIDE_ORDER])
    lines += block("Comparisons", [(v["name"], v["route"], "") for v in COMPARISONS.values()])
    lines += block("Other", [("Pricing hub", "/pricing/", ""), ("Permits hub", "/permits/", ""), ("HOA / ARC guides", "/hoa/", ""), ("FAQ", "/faq/", ""), ("About", "/about/", ""), ("Editorial standards", "/editorial-standards/", ""), ("Data & methods", "/data-and-methods/", ""), ("Contact", "/contact/", "")])
    (DIST / "llms.txt").write_text("\n".join(lines), encoding="utf-8")
    # llms-full: title, URL and the visible text of every indexable page (main content only)
    full = [f"# {PUBLIC_NAME} — full text", ""]
    for p in pages:
        if p.get("noindex"):
            continue
        txt = _visible_text(rendered[p["route"]])
        full += [f"## {p['title']}", f"URL: {BASE_URL}{p['route']}", f"Updated: {p['_lastmod']}", "", txt, ""]
    (DIST / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")


def write_cost_index_api():
    (DIST / "api").mkdir(exist_ok=True)
    data = {
        "name": "Kissimmee Concrete Cost Index", "release": COST_INDEX_RELEASE, "license": "CC BY 4.0", "publisher": PUBLIC_NAME, "url": BASE_URL + "/pricing/kissimmee-concrete-cost-index/",
        "scope": "Installed planning ranges for residential concrete, paver and coating work in Kissimmee, Osceola County and the Polk County ridge, Florida. Not quotes.",
        "method": BASE_URL + "/data-and-methods/",
        "items": [{"key": k, "item": n, "unit": u, "low_usd": lo, "high_usd": hi, "notes": note} for k, n, u, lo, hi, note in COST_INDEX],
    }
    (DIST / "api" / "cost-index.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
    with open(DIST / "api" / "cost-index.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["key", "item", "unit", "low_usd", "high_usd", "notes", "release", "release_date", "license"])
        for k, n, u, lo, hi, note in COST_INDEX:
            w.writerow([k, n, u, lo, hi, note, COST_INDEX_RELEASE["label"], COST_INDEX_RELEASE["date"], "CC BY 4.0"])


def write_feed():
    try:
        from content_tools import ASK_ENTRIES
    except Exception:
        ASK_ENTRIES = []
    items = "".join(
        f"<item><title>{htmlmod.escape(e['q'])}</title><link>{BASE_URL}/tools/ask-the-estimator/#{e['id']}</link><guid>{BASE_URL}/tools/ask-the-estimator/#{e['id']}</guid><pubDate>{e['rfc822']}</pubDate><description>{htmlmod.escape(e['a_text'])}</description></item>"
        for e in ASK_ENTRIES)
    (DIST / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Ask the Estimator — {PUBLIC_NAME}</title><link>{BASE_URL}/tools/ask-the-estimator/</link><description>Short answers to real questions homeowners in Kissimmee, Osceola County and the Polk ridge ask about concrete and pavers.</description><language>en-us</language>{items}</channel></rss>', encoding="utf-8")


def write_manifest():
    (DIST / "site.webmanifest").write_text(json.dumps({"name": PUBLIC_NAME, "short_name": PUBLIC_NAME, "start_url": "/", "display": "browser", "background_color": "#F2F2EF", "theme_color": "#B07828",
                                                       "icons": [{"src": "/static/brand/png/favicon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/static/brand/png/favicon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2), encoding="utf-8")


def _inline_script_hashes():
    hashes = set()
    for f in DIST.rglob("*.html"):
        for m in re.finditer(r"<script(?P<attrs>[^>]*)>(?P<body>.*?)</script>", f.read_text(encoding="utf-8"), flags=re.S):
            if "src=" in m.group("attrs") or "application/ld+json" in m.group("attrs"):
                continue
            if m.group("body").strip():
                hashes.add("'sha256-" + base64.b64encode(hashlib.sha256(m.group("body").encode("utf-8")).digest()).decode() + "'")
    return sorted(hashes)


def write_headers_and_redirects():
    csp = "; ".join([
        "default-src 'self'",
        "script-src 'self' " + " ".join(_inline_script_hashes()) + " https://challenges.cloudflare.com https://static.cloudflareinsights.com",
        "style-src 'self' 'unsafe-inline'",
        "img-src 'self' data:",
        "font-src 'self'",
        "connect-src 'self' https://cloudflareinsights.com https://challenges.cloudflare.com https://geocoding.geo.census.gov",
        "frame-src https://challenges.cloudflare.com",
        "form-action 'self'",
        "base-uri 'self'",
        "object-src 'none'",
        "frame-ancestors 'self'",
        "upgrade-insecure-requests",
    ])
    (DIST / "_headers").write_text(f"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  Cross-Origin-Opener-Policy: same-origin
  Content-Security-Policy: {csp}

https://:project.pages.dev/*
  X-Robots-Tag: noindex, nofollow

https://:branch.:project.pages.dev/*
  X-Robots-Tag: noindex, nofollow

/static/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/static/images/*
  Cache-Control: public, max-age=31536000, immutable
/static/brand/*
  Cache-Control: public, max-age=31536000, immutable
/static/site.*.js
  Cache-Control: public, max-age=31536000, immutable
/static/data/*
  Cache-Control: public, max-age=604800
/api/cost-index.json
  Cache-Control: public, max-age=86400
  Access-Control-Allow-Origin: *
/api/cost-index.csv
  Cache-Control: public, max-age=86400
  Access-Control-Allow-Origin: *
/sitemap.xml
  Cache-Control: public, max-age=3600
/llms.txt
  Cache-Control: public, max-age=3600
/llms-full.txt
  Cache-Control: public, max-age=3600
""", encoding="utf-8")
    (DIST / "_redirects").write_text("/index.html / 301\n/concrete/index.html /concrete/ 301\n/pavers/index.html /pavers/ 301\n", encoding="utf-8")


def write_404():
    src = DIST / "404" / "index.html"
    if src.exists():
        shutil.copy(src, DIST / "404.html")


def write_title_meta_csv(pages):
    out = ROOT.parent / "architecture" / "02-titles-metas.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["route", "kind", "title", "title_len", "h1", "meta_description", "desc_len", "noindex"])
        for p in pages:
            w.writerow([p["route"], p.get("kind", ""), p["title"], len(p["title"]), p["h1"], p["meta_description"], len(p["meta_description"]), p.get("noindex", False)])


def write_hashes(rendered):
    (DIST / "CONTENT-HASHES.json").write_text(json.dumps({r: hashlib.sha256(_visible_text(h).encode()).hexdigest()[:16] for r, h in rendered.items()}, indent=1), encoding="utf-8")


def main():
    if DIST.exists():
        for i in range(5):
            try:
                shutil.rmtree(DIST); break
            except PermissionError:
                time.sleep(0.5)
    DIST.mkdir(parents=True)
    pages = load_pages()
    rendered = {p["route"]: write_page(p) for p in pages}
    write_static()
    write_robots()
    write_sitemap(pages)
    write_llms(pages, rendered)
    write_cost_index_api()
    write_feed()
    write_manifest()
    write_404()
    write_headers_and_redirects()
    write_title_meta_csv(pages)
    write_hashes(rendered)
    key = indexnow_key()
    print(f"\n[build] {len(pages)} page(s) written to {DIST}; IndexNow key {key}")


if __name__ == "__main__":
    main()
