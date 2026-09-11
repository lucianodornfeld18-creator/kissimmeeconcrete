# -*- coding: utf-8 -*-
"""Photo library for kissimmeeconcrete.com (source of truth: ../images/photos.json).

The site serves /static/images/<slug>-{1600,960,480}.webp. Photos are provider
job photos from Central Florida (never asserted to be in a specific city) or
AI concept renderings, which are labelled on the page and in the alt text.
"""
import json
import pathlib

_JSON = pathlib.Path(__file__).resolve().parent.parent / "images" / "photos.json"
PHOTOS = json.loads(_JSON.read_text(encoding="utf-8")) if _JSON.exists() else []


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def photos_for(service_key, include_secondary=True, real_first=True):
    out = [p for p in PHOTOS if (p["services"][0] == service_key or (include_secondary and service_key in p["services"]))]
    if real_first:
        out.sort(key=lambda p: (p["kind"] != "real", p["services"][0] != service_key))
    return out


FEATURED_SLUGS = [
    "wide-gray-paver-driveway-charcoal-grid-street-view",
    "marble-paver-lanai-pool-deck-drain-channel",
    "curved-raised-terrace-stone-wall-cedar-pergola",
    "front-entry-steps-porcelain-treads-new-build",
    "tumbled-travertine-look-pool-deck-drain-oaks",
    "paver-driveway-install-in-progress-staged-stacks",
]


def featured(limit=6):
    by_slug = {p["slug"]: p for p in PHOTOS}
    picked = [by_slug[s] for s in FEATURED_SLUGS if s in by_slug]
    for p in PHOTOS:
        if len(picked) >= limit:
            break
        if p["kind"] == "real" and p not in picked:
            picked.append(p)
    return picked[:limit]


def figure_html(p, sizes="(max-width:560px) 100vw, (max-width:1120px) 50vw, 360px", eager=False):
    slug = p["slug"]
    srcset = ", ".join(f"/static/images/{slug}-{w}.webp {w}w" for w in (480, 960, 1600))
    badge = '<span class="photo-badge">Concept rendering</span>' if p["kind"] == "rendering" else ""
    return (
        f'<figure class="photo">'
        f'<a href="/static/images/{slug}-1600.webp" target="_blank" rel="noopener">'
        f'<img src="/static/images/{slug}-960.webp" srcset="{srcset}" sizes="{sizes}" '
        f'width="{p["w"]}" height="{p["h"]}" alt="{_esc(p["alt"])}" '
        f'{"" if eager else "loading=\"lazy\" "}decoding="async"></a>{badge}'
        f'<figcaption>{_esc(p["alt"])}</figcaption></figure>'
    )


def gallery_section(service_key, service_name, limit=6, heading=None, intro=None):
    items = photos_for(service_key)[:limit]
    if not items:
        return ""
    has_render = any(p["kind"] == "rendering" for p in items)
    note = ' Images marked "concept rendering" show a finish or layout, not a job we photographed.' if has_render else ""
    figs = "\n".join(figure_html(p) for p in items)
    heading = heading or f"Finished {_esc(service_name.lower())} from our crews"
    intro = intro or "Job photos from our crews around Central Florida. Every lot gets its own base, slope and drainage plan, so use these for finish and pattern ideas rather than as a template."
    return f'''
<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Photos</span>
    <h2>{heading}</h2>
    <p class="lede">{intro}{note}</p>
    <div class="gallery">
{figs}
    </div>
    <p style="margin-top:18px"><a class="card-link" href="/gallery/">See the full gallery, with real photos and renderings labelled &rarr;</a></p>
  </div>
</section>
'''


def home_strip(limit=6):
    figs = "\n".join(figure_html(p) for p in featured(limit))
    return f'''
<section>
  <div class="wrap">
    <span class="eyebrow">Recent work</span>
    <h2>Driveways, pool decks and terraces our crews have built</h2>
    <p class="lede">Real job photos, not stock. Gray paver driveways with charcoal banding, marble and travertine-look pool decks inside screened lanais, a raised terrace with a cedar pergola, porcelain-capped entry steps. Renderings in the gallery are labelled so you always know what you're looking at.</p>
    <div class="gallery" style="margin-top:26px">
{figs}
    </div>
    <div class="cta-row" style="margin-top:22px">
      <a class="btn btn-outline" href="/gallery/">Browse the gallery</a>
    </div>
  </div>
</section>
'''


def image_schema(items, base_url):
    return [{
        "@context": "https://schema.org",
        "@type": "ImageObject",
        "contentUrl": f"{base_url}/static/images/{p['slug']}-1600.webp",
        "name": p["alt"],
        "description": p["alt"] + (" (concept rendering)" if p["kind"] == "rendering" else " (job photo, Central Florida)"),
        "width": p["w"], "height": p["h"],
    } for p in items]
