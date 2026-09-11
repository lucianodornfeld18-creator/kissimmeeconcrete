# kissimmeeconcrete.com

Static site for **Kissimmee Concrete** — concrete, paver and hardscape lead-generation hub for
Kissimmee, Osceola County and the Polk County ridge (40-mile radius).

| | |
|---|---|
| Pages | 154 built, 152 indexable |
| Content | ~201,000 words |
| Stack | Python static generator, no framework, no runtime dependencies |
| Host | Cloudflare Pages + Pages Function + Worker |
| Live preview | https://kissimmeeconcrete.pages.dev |

## Build

```bash
cd site
python build.py          # writes ./dist
```

No third-party Python packages are required: `build.py` uses the standard library only.
The photo and brand pipelines (`images/make_photos.py`, `brand/make_brand_assets.py`) need
Pillow, but their output is committed, so a normal build does not run them.

## Cloudflare Pages settings

The build output is committed, so the simplest configuration is:

| Field | Value |
|---|---|
| Production branch | `main` |
| Framework preset | None |
| Build command | *(leave empty)* |
| Build output directory | `site/dist` |
| Root directory | *(leave empty)* |

If you would rather have Cloudflare build from source, set the build command to
`cd site && python build.py` and keep the same output directory.

### Bindings and secrets

| Name | Type | Where | Status |
|---|---|---|---|
| `CONTACT_EMAIL` | Service binding → `kissimmeeconcrete-contact` | Pages | deployed |
| `RATE_LIMIT_KV` | KV namespace | Pages | created |
| `TURNSTILE_SECRET_KEY` | Secret | Pages | **pending** |
| `CONTACT_DESTINATION` | Secret | Worker | **pending** |
| `RESEND_API_KEY` | Secret (optional auto-reply) | Worker | optional |

## Layout

```
site/            build.py, templates, content modules, static assets, dist/
site/functions/  Pages Function: POST /api/contact
site/workers/    contact-email Worker (service binding)
site/qa_*.py     crawl, style, similarity, schema and word-count audits
research/        keyword, territory, competitor, permit/HOA and question research
architecture/    URL map, intent ownership, titles and metas
brand/           logo pipeline, brand guide, SVG
images/          photo pipeline, masters, photos.json
audit/           generated audit reports
AUDIT-60-POINT.md, OWNER-INPUTS.md
```

## Audits

```bash
cd site
python qa_crawl.py        # links, titles, canonical, JSON-LD, sitemap
python qa_style.py        # forbidden phrases, sibling fingerprints, fact density
python qa_similarity.py   # 8-gram prose overlap, internal and vs sibling sites
python qa_schema.py       # schema types, banned entities, page weight
python qa_words.py        # word counts vs the benchmark floors
```

Current state: crawl 0 hard / 0 warnings · style 0 hard · similarity 0 pairs above 15%
internally and 0 against the five sibling sites · schema 0 hard.

See `AUDIT-60-POINT.md` for the full 60-control audit and `OWNER-INPUTS.md` for what is
still needed before the custom domain goes live.
