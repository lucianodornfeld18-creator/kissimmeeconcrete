# -*- coding: utf-8 -*-
"""Page shell for kissimmeeconcrete.com.

Page dict contract (built by content_*.py modules):
{
  "route": "/concrete/driveways/",     # required, trailing slash
  "title": "…",                         # required, full <title> (<= 60-65 chars)
  "meta_description": "…",              # required, 120-160 chars
  "h1": "…",                            # required
  "breadcrumbs": [("Home","/"), ("Concrete","/concrete/"), ("Driveways", None)],
  "body_html": "…",                     # required, main content
  "kind": "service|cityservice|city|county|pillar|guide|compare|tool|pricing|permit|hoa|faq|legal|home|page",
  "service_key": "concrete-driveways",  # optional: appends gallery + Service schema
  "city_key": "st-cloud",               # optional (cityservice / city pages)
  "faqs": [{"q": "…", "a": "<p>…</p>"}],# optional: rendered + FAQPage schema
  "sources": ["fs489117", ("Label","https://…")],  # optional: rendered sources list
  "schema": [ {...} ],                  # optional extra JSON-LD
  "noindex": False, "is_home": False, "nav_active": "/concrete/",
  "changelog": ["2026-09-10 — first published"],
  "og_image": "/static/brand/png/og-default.jpg",
  "no_gallery": False,
}
"""
import base64
import hashlib
import json
import pathlib
import re

from _data import (
    BASE_URL, PUBLIC_NAME, BUSINESS, PHONE_DISPLAY, PHONE_E164, EMAIL, TURNSTILE_SITE_KEY,
    NAV_PRIMARY, FOOTER_LEGAL, SERVICES, CONCRETE_SERVICES, PAVER_SERVICES, COATING_SERVICES,
    CITIES, TIER1, TOOLS, TOOL_ORDER, SOURCES, LAUNCH_DATE,
)
from _photos import gallery_section, photos_for, image_schema
try:
    from content_extra import EXTRA_SECTIONS, EXTRA_FAQS
except ImportError:  # module not written yet
    EXTRA_SECTIONS, EXTRA_FAQS = {}, {}

_STATIC = pathlib.Path(__file__).resolve().parent / "static"


def _minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*\n\s*", "", css)
    return re.sub(r"\s*([{}:;,>])\s*", r"\1", css).replace(";}", "}")


INLINE_CSS = _minify_css((_STATIC / "fonts" / "fonts.css").read_text(encoding="utf-8") + "\n" + (_STATIC / "styles.css").read_text(encoding="utf-8"))
PRELOAD_FONTS = ["/static/fonts/montserrat-var-latin.woff2", "/static/fonts/source-sans-3-var-latin.woff2"]
SITE_JS = "/static/site." + hashlib.md5((_STATIC / "site.js").read_bytes()).hexdigest()[:10] + ".js"
DEFAULT_OG_IMAGE = "/static/brand/png/og-default.jpg"

_HERO_LQIP = "url(data:image/webp;base64," + base64.b64encode((_STATIC / "images" / "hero-lqip.webp").read_bytes()).decode() + ")"
_HERO_GRAD = "linear-gradient(180deg,rgba(20,20,20,.72) 0%,rgba(20,20,20,.55) 50%,rgba(20,20,20,.82) 100%)"
HERO_INLINE_CSS = (
    f".hero{{background-image:{_HERO_GRAD},url(/static/images/hero-paver-driveway-1600.webp),{_HERO_LQIP}}}"
    f"@media (max-width:1200px){{.hero{{background-image:{_HERO_GRAD},url(/static/images/hero-paver-driveway-1200.webp),{_HERO_LQIP}}}}}"
    f"@media (max-width:720px){{.hero{{background-image:{_HERO_GRAD},url(/static/images/hero-paver-driveway-800.webp),{_HERO_LQIP}}}}}"
)

LOGO_SIZES = "(max-width:420px) 199px, (max-width:960px) 235px, 289px"


def _logo_srcset(kind):  # light|dark, webp|png
    theme, fmt = kind
    return ", ".join(f"/static/brand/{fmt}/logo-horizontal-{theme}-h{h}.{fmt} {int(h*4.515)}w" for h in (64, 96, 160))


def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def turnstile_html():
    if not TURNSTILE_SITE_KEY:
        return ""
    return (f'<div class="cf-turnstile" data-sitekey="{_esc(TURNSTILE_SITE_KEY)}"></div>'
            '<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>')


def header_cta():
    if PHONE_E164:
        return f'<a class="btn btn-primary header-cta" href="tel:{PHONE_E164}">Call {_esc(PHONE_DISPLAY)}</a>'
    return '<a class="btn btn-primary header-cta" href="/contact/">Free estimate</a>'


def mobile_cta():
    call = f'<a class="btn btn-outline" href="tel:{PHONE_E164}">Call</a>' if PHONE_E164 else ''
    return f'<div class="mobile-cta">{call}<a class="btn btn-primary" href="/contact/">Free estimate</a></div>'


def cta_block(title="Get a written estimate for your project", text=None, city=None):
    text = text or "Tell us the size, the surface you have now and where the lot is. We visit, measure, check access and drainage, and send a written proposal. No pressure calls."
    where = f" in {city}" if city else ""
    call = f'<a class="btn btn-outline" href="tel:{PHONE_E164}">Call {_esc(PHONE_DISPLAY)}</a>' if PHONE_E164 else ''
    return f'''
<section class="alt">
  <div class="wrap">
    <h2>{_esc(title)}{_esc(where)}</h2>
    <p class="lede">{_esc(text)}</p>
    <div class="cta-row"><a class="btn btn-primary" href="/contact/">Request a free estimate</a>{call}</div>
  </div>
</section>'''


def _nav_html(active_route):
    return "\n".join(f'<a href="{route}"{" class=\"active\"" if route == active_route else ""}>{_esc(label)}</a>' for label, route in NAV_PRIMARY)


def header_html(active_route=""):
    return f"""
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="/" aria-label="{PUBLIC_NAME} home">
      <picture>
        <source srcset="{_logo_srcset(('dark','webp'))}" sizes="{LOGO_SIZES}" media="(prefers-color-scheme: dark)" type="image/webp">
        <source srcset="{_logo_srcset(('light','webp'))}" sizes="{LOGO_SIZES}" type="image/webp">
        <img class="brand-logo" src="/static/brand/png/logo-horizontal-light-h64.png" srcset="{_logo_srcset(('light','png'))}" sizes="{LOGO_SIZES}" width="289" height="64" alt="{PUBLIC_NAME}" fetchpriority="high" decoding="async">
      </picture>
    </a>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Open menu"><span></span><span></span><span></span></button>
    <nav class="primary-nav" id="primaryNav" aria-label="Primary">
      {_nav_html(active_route)}
    </nav>
    {header_cta()}
  </div>
</header>
""".strip()


def footer_html():
    concrete = "\n".join(f'<li><a href="{SERVICES[s]["route"]}">{_esc(SERVICES[s]["name"])}</a></li>' for s in CONCRETE_SERVICES)
    pavers = "\n".join(f'<li><a href="{SERVICES[s]["route"]}">{_esc(SERVICES[s]["name"])}</a></li>' for s in PAVER_SERVICES + COATING_SERVICES)
    areas = "\n".join(f'<li><a href="{CITIES[c]["route"]}">{_esc(CITIES[c]["name"])}</a></li>' for c in TIER1)
    legal = "\n".join(f'<li><a href="{route}">{_esc(label)}</a></li>' for label, route in FOOTER_LEGAL)
    phone = f'<li><a href="tel:{PHONE_E164}">{_esc(PHONE_DISPLAY)}</a></li>' if PHONE_E164 else ''
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <picture>
        <source srcset="/static/brand/webp/logo-stacked-dark-h240.webp" type="image/webp">
        <img src="/static/brand/png/logo-stacked-dark-h240.png" width="342" height="240" alt="{PUBLIC_NAME}" loading="lazy" style="height:120px;width:auto;margin-bottom:12px">
      </picture>
      <p class="footer-blurb">{_esc(BUSINESS["blurb"])}</p>
      <p class="footer-blurb">Hours: {_esc(BUSINESS["hours"])}</p>
    </div>
    <div><h2>Concrete</h2><ul>{concrete}</ul></div>
    <div><h2>Pavers &amp; coatings</h2><ul>{pavers}</ul></div>
    <div>
      <h2>Areas</h2><ul>{areas}<li><a href="/areas/">All areas &amp; counties</a></li></ul>
      <h2 style="margin-top:18px">Contact</h2>
      <ul>{phone}<li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="/contact/">Request an estimate</a></li><li><a href="/pricing/">Pricing &amp; cost index</a></li><li><a href="/permits/">Permits</a></li><li><a href="/tools/">Tools</a></li><li><a href="/faq/">FAQ</a></li></ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>&copy; 2026 {PUBLIC_NAME} &middot; Kissimmee, Osceola County &amp; the Polk County ridge, Florida</span>
    <ul class="legal-links">{legal}</ul>
  </div>
</footer>
""".strip()


def breadcrumbs_html(crumbs):
    parts = []
    for label, route in crumbs:
        parts.append(f'<a href="{route}">{_esc(label)}</a>' if route else f'<span aria-current="page">{_esc(label)}</span>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{" <span class=\"sep\">/</span> ".join(parts)}</nav>'


def breadcrumb_schema(crumbs):
    items = []
    for i, (label, route) in enumerate(crumbs, start=1):
        e = {"@type": "ListItem", "position": i, "name": label}
        if route:
            e["item"] = BASE_URL + route
        items.append(e)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


ORG_ID = BASE_URL + "/#organization"
WEBSITE_ID = BASE_URL + "/#website"

WIKI = {
    "kissimmee": "https://en.wikipedia.org/wiki/Kissimmee,_Florida",
    "st-cloud": "https://en.wikipedia.org/wiki/St._Cloud,_Florida",
    "celebration": "https://en.wikipedia.org/wiki/Celebration,_Florida",
    "poinciana": "https://en.wikipedia.org/wiki/Poinciana,_Florida",
    "buenaventura-lakes": "https://en.wikipedia.org/wiki/Buenaventura_Lakes,_Florida",
    "four-corners": "https://en.wikipedia.org/wiki/Four_Corners,_Florida",
    "champions-gate": "https://en.wikipedia.org/wiki/ChampionsGate,_Florida",
    "reunion": "https://en.wikipedia.org/wiki/Reunion,_Florida",
    "davenport": "https://en.wikipedia.org/wiki/Davenport,_Florida",
    "haines-city": "https://en.wikipedia.org/wiki/Haines_City,_Florida",
    "harmony": "https://en.wikipedia.org/wiki/Harmony,_Florida",
    "winter-haven": "https://en.wikipedia.org/wiki/Winter_Haven,_Florida",
    "auburndale": "https://en.wikipedia.org/wiki/Auburndale,_Florida",
    "lake-alfred": "https://en.wikipedia.org/wiki/Lake_Alfred,_Florida",
    "dundee": "https://en.wikipedia.org/wiki/Dundee,_Florida",
    "lake-wales": "https://en.wikipedia.org/wiki/Lake_Wales,_Florida",
    "polk-city": "https://en.wikipedia.org/wiki/Polk_City,_Florida",
}


def city_entity(key):
    c = CITIES[key]
    e = {"@type": "City", "name": c["name"].replace(" & Narcoossee", "")}
    if key in WIKI:
        e["sameAs"] = WIKI[key]
    return e


def organization_schema():
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": ORG_ID,
        "name": PUBLIC_NAME,
        "url": BASE_URL + "/",
        "logo": {"@type": "ImageObject", "url": BASE_URL + "/static/brand/png/logo-stacked-light-h400.png", "width": 570, "height": 400},
        "email": EMAIL,
        "description": BUSINESS["blurb"],
        "areaServed": [city_entity(k) for k in CITIES],
        "knowsAbout": ["Concrete driveways", "Concrete patios", "Concrete slabs", "Stamped concrete", "Concrete repair", "Paver driveways", "Paver pool decks", "Travertine", "Paver sealing", "Garage floor coatings", "Osceola County building permits", "HOA architectural review"],
    }
    if PHONE_E164:
        org["telephone"] = PHONE_E164
    return org


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": WEBSITE_ID, "name": PUBLIC_NAME, "url": BASE_URL + "/", "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"}


def service_schema(page):
    svc = SERVICES[page["service_key"]]
    area = [city_entity(page["city_key"])] if page.get("city_key") else [city_entity(k) for k in TIER1]
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": page.get("service_name", svc["name"]),
        "serviceType": svc["name"],
        "description": page["meta_description"],
        "provider": {"@id": ORG_ID},
        "areaServed": area,
        "url": BASE_URL + page["route"],
    }


def faq_html(faqs, heading="Questions we get about this"):
    if not faqs:
        return ""
    items = "\n".join(f'<div class="qa"><h3>{_esc(f["q"])}</h3>{f["a"]}</div>' for f in faqs)
    return f'<section class="faq"><div class="wrap"><h2>{_esc(heading)}</h2>{items}</div></section>'


def faq_schema(faqs):
    def strip(html):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": strip(f["a"])}} for f in faqs]}


def sources_html(keys):
    if not keys:
        return ""
    lis = []
    for k in keys:
        if isinstance(k, tuple):
            label, url = k
        else:
            label, url = SOURCES[k]
        lis.append(f'<li><a href="{url}" rel="noopener" target="_blank">{_esc(label)}</a></li>')
    return f'<div class="wrap"><div class="sources"><strong>Sources checked for this page</strong><ol>{"".join(lis)}</ol></div></div>'


def meta_line(page):
    pub = page.get("_published", LAUNCH_DATE)
    mod = page.get("_lastmod", pub)
    txt = f'Published {pub}' + (f' &middot; Last reviewed {mod}' if mod != pub else '')
    return f'<p class="meta-line">{txt} &middot; By the {PUBLIC_NAME} team</p>'


def changelog_html(page):
    items = page.get("changelog") or [f'{page.get("_published", LAUNCH_DATE)} — first published']
    return '<div class="wrap"><p class="changelog"><strong>What changed in this update:</strong> ' + " &middot; ".join(_esc(i) for i in items) + '</p></div>'


def clip_desc(s, n=158):
    """Trim a meta description to <= n chars at a clause boundary (', ' / '; ' / '. ') or a word boundary."""
    s = " ".join(str(s).split())
    if len(s) <= n:
        return s
    cut = s[:n]
    for sep in (". ", "; ", ", "):
        i = cut.rfind(sep)
        if i >= 110:
            return cut[:i].rstrip(",;") + "."
    i = cut.rfind(" ")
    return cut[:i].rstrip(",;:") + "."


def render_page(page):
    route = page["route"]
    is_home = page.get("is_home", False)
    title = page["title"]
    desc = clip_desc(page["meta_description"])
    canonical = BASE_URL + route
    og_image = BASE_URL + page.get("og_image", DEFAULT_OG_IMAGE)
    h1 = page["h1"]
    crumbs = page.get("breadcrumbs", [])
    robots = "noindex,nofollow" if page.get("noindex") else "index,follow,max-image-preview:large,max-snippet:-1"
    kind = page.get("kind", "page")

    schema = []
    if is_home:
        schema += [website_schema(), organization_schema()]
    if crumbs:
        schema.append(breadcrumb_schema(crumbs))
    wp = {"@context": "https://schema.org", "@type": "WebPage", "@id": canonical + "#webpage", "url": canonical, "name": title, "description": desc, "isPartOf": {"@id": WEBSITE_ID}, "inLanguage": "en-US",
          "datePublished": page.get("_published", LAUNCH_DATE), "dateModified": page.get("_lastmod", page.get("_published", LAUNCH_DATE))}
    schema.append(wp)
    if page.get("service_key"):
        schema.append(service_schema(page))
    if page.get("faqs"):
        schema.append(faq_schema(page["faqs"]))
    if kind in ("guide", "compare"):
        schema.append({
            "@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc, "url": canonical,
            "mainEntityOfPage": canonical, "datePublished": page.get("_published", LAUNCH_DATE), "dateModified": page.get("_lastmod", page.get("_published", LAUNCH_DATE)),
            "author": {"@type": "Organization", "@id": ORG_ID, "name": PUBLIC_NAME}, "publisher": {"@id": ORG_ID}, "image": og_image, "inLanguage": "en-US",
        })
    schema.extend(page.get("schema", []))

    body = page["body_html"] + EXTRA_SECTIONS.get(route, "")
    if EXTRA_FAQS.get(route):
        page["faqs"] = (page.get("faqs") or []) + EXTRA_FAQS[route]
        schema = [x for x in schema if x.get("@type") != "FAQPage"] + [faq_schema(page["faqs"])]
    if page.get("service_key") and not page.get("no_gallery"):
        svc = SERVICES[page["service_key"]]
        body += gallery_section(page["service_key"], svc["name"], limit=3 if page.get("city_key") else 6)
        schema.extend(image_schema(photos_for(page["service_key"])[:3 if page.get("city_key") else 6], BASE_URL))
    body += faq_html(page.get("faqs"))
    if not is_home and kind not in ("legal", "home") and not page.get("no_cta"):
        body += cta_block(city=CITIES[page["city_key"]]["name"] if page.get("city_key") else None)
    body += sources_html(page.get("sources"))
    if kind not in ("legal", "home") and not page.get("noindex"):
        body += changelog_html(page)

    head_block = "" if is_home else f'<div class="wrap page-head">{breadcrumbs_html(crumbs) if crumbs else ""}<h1>{_esc(h1)}</h1>{meta_line(page) if kind not in ("legal",) else ""}</div>'
    preload = "".join(f'<link rel="preload" as="font" type="font/woff2" href="{f}" crossorigin>' for f in PRELOAD_FONTS)
    hero_preload = '<link rel="preload" as="image" href="/static/images/hero-paver-driveway-1200.webp" type="image/webp" media="(min-width: 721px)" fetchpriority="high">' if is_home else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{_esc(title)}</title>
<meta name="description" content="{_esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{'website' if is_home else 'article'}">
<meta property="og:title" content="{_esc(title)}">
<meta property="og:description" content="{_esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{PUBLIC_NAME} logo">
<meta property="og:site_name" content="{PUBLIC_NAME}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/static/brand/png/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/static/brand/png/favicon-192.png">
<link rel="apple-touch-icon" href="/static/brand/png/favicon-180.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="Ask the Estimator — {PUBLIC_NAME}" href="/feed.xml">
<meta name="theme-color" content="#F2F2EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#161616" media="(prefers-color-scheme: dark)">
{preload}{hero_preload}
<style>{INLINE_CSS}</style>
{f'<style>{HERO_INLINE_CSS}</style>' if is_home else ''}
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header_html(page.get("nav_active", ""))}
<main id="main">
{head_block}
{body}
</main>
{footer_html()}
{mobile_cta()}
<script src="{SITE_JS}" defer></script>
</body>
</html>
"""
