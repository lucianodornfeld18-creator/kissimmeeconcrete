# -*- coding: utf-8 -*-
"""Pricing hub, concrete cost guide, paver cost guide, Cost Index (Dataset)."""
from _data import COST_INDEX, COST_INDEX_RELEASE, BASE_URL, PUBLIC_NAME, TIER1, CITIES
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, faq, cost_rows, cost_range, callout, related, esc

R = COST_INDEX_RELEASE["label"]
D = COST_INDEX_RELEASE["date"]


def pricing_hub():
    body = sec("How pricing works on this site",
        cap(f"Every number here is a planning range from the Kissimmee Concrete Cost Index, release {R} ({D}), for installed work in the Kissimmee and Osceola County market, with the method published and the data downloadable. Ranges are not quotes: your price comes in a written proposal after a site visit that checks access, subgrade, drainage and HOA requirements. The Polk ridge runs slightly lower on labor; the resort corridor slightly higher on scheduling.")
        + cards([
            ("Concrete cost guide", "Driveways, patios, pool decks, slabs and walkways per square foot and per typical project (two-car driveway, 12x12 patio, shed pad), with the factors that move the price.", "/pricing/concrete/", "Concrete costs"),
            ("Paver cost guide", "Paver driveways, patios, pool decks, travertine, walkways, sealing and repair per square foot and per project (600 sq ft pool deck, two-car driveway).", "/pricing/pavers/", "Paver costs"),
            ("Kissimmee Concrete Cost Index", "The full 18-item table, method, limitations, release history, and CSV/JSON downloads under CC BY 4.0 for Realtors, managers and other sites.", "/pricing/kissimmee-concrete-cost-index/", "The index"),
        ]), eyebrow="Pricing")
    body += sec("Ten things that move a concrete or paver price in Osceola County",
        "<ol><li><strong>Removal.</strong> Tearing out an old slab adds $2 to $4 per square foot; thicker slabs and tight access more.</li><li><strong>Size.</strong> Small pours carry the ready-mix short-load fee and a full crew day; under 200 square feet expect the top of every range.</li><li><strong>Thickness and steel.</strong> 6 inches with a rebar grid runs 35 to 45 percent more than 4 inches with fiber.</li><li><strong>Base.</strong> Muck, roots or a saturated subgrade mean fill and extra compaction, priced separately.</li><li><strong>Drainage.</strong> Trench drains, channel drains and swales are line items.</li><li><strong>Finish.</strong> Stamped, colored, exposed aggregate and borders add per square foot.</li><li><strong>Material grade.</strong> Standard concrete pavers versus premium lines versus travertine, marble and porcelain.</li><li><strong>Access.</strong> Gated resort communities, alley lots and rural lots a mixer cannot reach (pump or buggy).</li><li><strong>Permits and HOA.</strong> Fees are passed through; packets are our time.</li><li><strong>Season.</strong> Spring is the busiest window (Google Trends shows paver interest peaking April–May in the Orlando market); rainy-season pours need early starts and sometimes a lost day.</li></ol>", cls="alt")
    body += sec("Get a real number", f"<p>The {tool('concrete-paver-calculator')} turns dimensions into cubic yards, bags, base and a dated range. The {tool('project-brief')} writes up your job so three contractors quote the same thing. The <a href=\"/contact/\">estimate form</a> gets a written proposal.</p>")
    faqs = [
        faq("Are these prices quotes?", "No. They are planning ranges with a published method. A quote comes after a site visit and is in writing."),
        faq("How often is the index updated?", f"Quarterly. The {R} release is dated {D}; the next is scheduled for {COST_INDEX_RELEASE['next']}."),
        faq("Why is a small job so expensive per square foot?", "The truck minimum, the short-load fee and the crew day are the same whether the slab is 100 or 400 square feet."),
        faq("Do you charge for estimates?", "No. Site visits and written proposals are free."),
        faq("Do you offer financing?", "Ask on the estimate; a financing partner will be listed here once one is in place."),
    ]
    return {"route": "/pricing/", "title": "Concrete & Paver Prices in Kissimmee, FL – Cost Guides & Index", "meta_description": f"What concrete and paver work costs around Kissimmee: cost guides per square foot and per project, the ten factors that move a price, and the quarterly Kissimmee Concrete Cost Index ({R}) with downloadable data.", "h1": "Pricing: concrete and paver costs around Kissimmee", "breadcrumbs": [("Home", "/"), ("Pricing", None)], "body_html": body, "faqs": faqs, "kind": "pricing", "nav_active": "/pricing/"}


def concrete_guide():
    body = sec("The short version on concrete cost in Kissimmee",
        cap(f"In the {R} Kissimmee Concrete Cost Index, a broom-finish concrete driveway runs {cost_range('concrete-driveway-broom')} installed, a 6-inch driveway with a rebar grid {cost_range('concrete-driveway-6in')}, a patio {cost_range('concrete-patio')}, stamped concrete {cost_range('stamped-concrete')}, a pad {cost_range('concrete-slab-pad')}, a 4-foot walkway {cost_range('concrete-sidewalk')}, removal of an old slab {cost_range('concrete-removal')}, and resurfacing {cost_range('concrete-resurfacing')}. Ready-mix is {cost_range('ready-mix')} delivered."),
        eyebrow=f"Cost guide · {R}")
    body += sec("Per square foot, by item", cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "concrete-patio", "stamped-concrete", "concrete-slab-pad", "concrete-sidewalk", "concrete-removal", "concrete-resurfacing", "ready-mix"]), cls="alt")
    body += sec("What typical jobs cost, project by project",
        table(["Project", "Size", "Spec", "Range (new work)", "Add for removal"], [
            ("Two-car driveway", "20×24 ft = 480 sq ft", "4 in, 3,000–3,500 psi, fiber + edge bars", "$4,080–$6,480", "$960–$1,920"),
            ("Two-car driveway with boat pad", "480 + 240 sq ft", "4 in drive + 6 in pad with #4 grid", "$6,840–$10,560", "$1,440–$2,880"),
            ("Driveway widening", "6×24 ft = 144 sq ft", "4 in, matched joint", "$1,220–$1,940", "n/a"),
            ("Single garage-edge panel replacement", "10×12 ft = 120 sq ft", "4 in, doweled", "$1,020–$1,620", "$240–$480"),
            ("12×12 patio", "144 sq ft", "4 in, broom", "$1,300–$1,900 (minimum-charge floor)", "$290–$580"),
            ("16×20 lanai extension", "320 sq ft", "4 in, doweled, broom", "$2,560–$4,000", "n/a"),
            ("Stamped 12×16 patio", "192 sq ft", "4 in, integral + release color, sealed", "$2,690–$4,220", "n/a"),
            ("Pool deck (new concrete)", "600 sq ft", "4 in, textured", "$4,800–$7,500 + texture coat $1,800–$3,600", "$1,500–$2,800 (hand work at the pool)"),
            ("Pool deck resurfacing", "600 sq ft", "Polymer overlay, knock-down", "$3,000–$5,700", "n/a"),
            ("10×12 shed pad", "120 sq ft", "4 in, fiber", "$1,200–$1,900", "n/a"),
            ("12×40 RV pad", "480 sq ft", "6 in, 4,000 psi, #4 grid", "$5,520–$8,160", "n/a"),
            ("40-ft front walk", "4 ft wide = 160 sq ft", "4 in, broom, joints every 4–5 ft", "$1,360–$2,080", "$320–$640"),
            ("30×40 workshop slab", "1,200 sq ft", "6 in, thickened edge, #4 grid", "$13,800–$20,400", "n/a"),
        ], caption=f"Computed from the {R} index ranges. Fill to raise a slab above the water table, trench drains, root barriers, pump trucks and permit fees are separate line items."))
    body += sec("Why the numbers are what they are",
        f"<p>A 4-inch slab uses one cubic yard of concrete per 81 square feet; at {cost_range('ready-mix')} delivered in the Orlando market this quarter, material for a 480-square-foot driveway is roughly $1,050 to $1,700 before the short-load and fuel surcharges suppliers add. The rest of the price is base (limerock delivered and compacted), forms, fiber and rebar, a crew of three to four for two days, finishing, joints, cure, haul-off, permit fees and the truck's minimum. That is why the same slab is $8.50 per square foot on a straightforward lot and $13.50 on a lot with tight access, a saturated subgrade and a downspout to reroute. Full method on the <a href=\"/pricing/kissimmee-concrete-cost-index/\">Cost Index</a> page and in <a href=\"/data-and-methods/\">Data &amp; methods</a>.</p>", cls="alt")
    body += sec("What changes the concrete price from city to city",
        table(["Place", "Typical adjustment", "Why"], [
            (city("kissimmee"), "Index baseline", "Reference market"),
            (city("buenaventura-lakes"), "Low end", "Straightforward tear-outs, clean sand, no HOA"),
            (city("st-cloud"), "Baseline; +fill on lakefront and east side", "Basinger/EauGallie lots need raising"),
            (city("poinciana"), "Low end; +DCB time", "Routine replacements; DCB approval before work"),
            (city("celebration"), "High end", "Alley access, ARC materials, matching"),
            (city("harmony"), "+fill", "Surface water table on EauGallie/Basinger sand"),
            (city("davenport") + ", " + city("haines-city"), "Slightly below baseline on labor", "Ridge sand: no water table, wetted base"),
            (city("four-corners") + ", " + city("champions-gate") + ", " + city("reunion"), "High end", "Gate access, turnover scheduling, ARC, insurance certificates"),
        ], caption="Adjustments are qualitative; the index ranges already span them."))
    body += sec("Concrete or something else?", f"<p>Pavers run 50 to 70 percent more than broom-finish concrete up front and can be lifted for repairs ({compare('concrete-vs-pavers')}). Stamped concrete sits between the two ({compare('stamped-vs-pavers')}). Resurfacing a sound slab costs about half of a new pour ({compare('resurface-vs-replace')}). The {tool('concrete-vs-pavers')} gives a recommendation in eight questions.</p>", cls="alt")
    faqs = [
        faq("How much does a concrete driveway cost in Kissimmee?", f"About {cost_range('concrete-driveway-broom')} installed for a 4-inch broom finish in the {R} index; a 480-square-foot two-car driveway is $4,080 to $6,480 before removal of an old slab ($960 to $1,920)."),
        faq("How much does a 2-car concrete driveway cost?", "Roughly $4,100 to $6,500 for 480 square feet of new concrete, $5,000 to $8,400 if the old drive has to be removed."),
        faq("How much is a 12x12 concrete patio?", "About $1,300 to $1,900; small pours sit at the top of the per-foot range because of truck minimums."),
        faq("What does it cost to remove an old driveway?", f"{cost_range('concrete-removal')}; a two-car driveway is $960 to $1,920."),
        faq("Is 6-inch concrete worth it?", "For boats, RVs and trucks, yes; it runs 35 to 45 percent more than 4-inch and stops the apron and pad cracks those loads cause. For cars only, 4 inches on a real base is right."),
        faq("What is a normal deposit?", "A deposit that covers materials and permit fees at contract signing, with the balance on completion, is typical for residential flatwork; the contract states the schedule. We do not ask for full payment up front."),
    ]
    return {"route": "/pricing/concrete/", "title": "Concrete Cost in Kissimmee, FL (2026): Per Sq Ft & By Project", "meta_description": f"What concrete costs in Kissimmee in {R} 2026: driveways $8.50–$13.50/sq ft, patios, stamped, pads, walkways and removal, with worked examples for a two-car driveway, 12x12 patio, RV pad and pool deck.", "h1": "Concrete cost in Kissimmee, FL: per square foot and by project", "breadcrumbs": [("Home", "/"), ("Pricing", "/pricing/"), ("Concrete cost guide", None)], "body_html": body, "faqs": faqs, "kind": "pricing", "nav_active": "/pricing/", "changelog": [f"{D} — {R} release; first published"]}


def paver_guide():
    body = sec("The short version on paver cost in Kissimmee",
        cap(f"In the {R} Kissimmee Concrete Cost Index, a paver driveway in standard 80 mm concrete pavers runs {cost_range('paver-driveway-concrete')} installed, premium lines {cost_range('paver-driveway-premium')}, a paver patio {cost_range('paver-patio')}, a paver pool-deck overlay {cost_range('paver-pool-deck')}, a travertine pool deck {cost_range('travertine-pool-deck')}, a paver walkway {cost_range('paver-walkway')}, cleaning-re-sanding-sealing {cost_range('paver-sealing')}, and a lift-and-relay repair {cost_range('paver-repair')}. Removing old concrete first adds {cost_range('concrete-removal')}."),
        eyebrow=f"Cost guide · {R}")
    body += sec("Per square foot, by item", cost_rows(["paver-driveway-concrete", "paver-driveway-premium", "paver-patio", "paver-pool-deck", "travertine-pool-deck", "paver-walkway", "paver-sealing", "paver-repair", "concrete-removal"]), cls="alt")
    body += sec("By project",
        table(["Project", "Size", "Spec", "Range", "Notes"], [
            ("Two-car paver driveway", "480 sq ft", "80 mm pavers, 6 in base, soldier border, concrete apron", "$6,720–$10,560", "+$960–$1,920 removal; +10–15% for bands and a contrasting border"),
            ("Two-car driveway, premium line", "480 sq ft", "Belgard Luxury / large format", "$9,600–$16,320", "Material-driven"),
            ("Lift-and-relay of a sunken driveway", "480 sq ft (full field)", "Rebuilt 6 in base, same pavers", "$4,320–$7,680", "Localized dips are far less; minimum charge applies"),
            ("12×12 paver patio", "144 sq ft", "60 mm pavers, 4–5 in base", "$2,000–$3,000", "Minimum-charge floor"),
            ("16×20 lanai extension in pavers", "320 sq ft", "60 mm, sailor course at the slab", "$4,160–$6,720", "n/a"),
            ("600 sq ft pool deck overlay", "600 sq ft", "1 in remodel pavers, new bullnose coping", "$9,000–$14,400 + coping", "Coping $28–$55 per linear ft; drain channel $18–$30 per ft"),
            ("600 sq ft travertine pool deck", "600 sq ft", "1¼ in tumbled, sand-set or thin-set", "$12,000–$21,600 + coping", "Marble and porcelain higher"),
            ("40-ft front walk", "4 ft = 160 sq ft", "60 mm, border, edge restraint both sides", "$2,240–$3,840", "Steps $250–$450 per riser"),
            ("Seal a driveway", "480 sq ft", "Clean, polymeric re-sand, seal", "$840–$1,560", "+$0.75–$1.50/sq ft to strip a failed sealer"),
            ("Seal a pool deck", "600 sq ft", "Clean, re-sand, anti-slip sealer", "$1,050–$1,950", "Rentals: every 2–3 years"),
            ("Seat wall", "20 linear ft", "Segmental wall units, cap", "$1,500–$2,600", "n/a"),
            ("Fire pit kit installed", "1", "Wall units, steel ring", "$900–$2,200", "Gas features by licensed trades"),
        ], caption=f"Computed from the {R} index ranges. HOA packet preparation is our time; permit and recording fees (Polk Paver Release Form) pass through."))
    body += sec("Where the money goes on a paver job",
        "<p>Material is 35 to 50 percent: standard concrete pavers, premium lines, travertine and porcelain in ascending order. Base is the next largest share and the one that determines whether the job lasts: 6 inches of limerock delivered, placed in lifts and compacted, plus bedding sand, edge restraint and polymeric sand. Labor scales with cuts: borders, bands, curves and circles add cutting time and waste. Removal of an old concrete drive, the concrete apron at the street, and coping and drain work on pool decks are their own line items. Sealing is a separate visit 60 to 90 days later.</p>", cls="alt")
    body += sec("What changes the paver price from community to community",
        table(["Place", "Typical adjustment", "Why"], [
            (city("kissimmee"), "Index baseline", "Reference market"),
            (city("celebration"), "High end", "Village palettes, matching discontinued blends, alley access, ARC"),
            (city("reunion"), "Premium lines", "Streetscape blends, estate lots, resort access"),
            (city("four-corners") + ", " + city("champions-gate"), "High end on scheduling", "Turnover windows, gate access, COI to the association"),
            (city("st-cloud") + ", " + city("harmony"), "Baseline; drainage line items", "Wet ground; swales and downspout work"),
            (city("davenport") + ", " + city("haines-city"), "Slightly below on labor", "Ridge sand; concrete apron avoids the Paver Release Form"),
            (city("poinciana"), "Baseline; DCB time", "Approval before work"),
        ]))
    body += sec("Pavers or concrete?", f"<p>Pavers cost 50 to 70 percent more than broom-finish concrete and can be lifted for repairs; concrete is cheaper and simpler. {compare('concrete-vs-pavers')}; {compare('travertine-vs-concrete-pavers')}; {compare('stamped-vs-pavers')}; {tool('concrete-vs-pavers')}.</p>", cls="alt")
    faqs = [
        faq("How much does a paver driveway cost in Kissimmee?", f"About {cost_range('paver-driveway-concrete')} installed for standard 80 mm pavers on a 6-inch base; a 480-square-foot two-car driveway is $6,720 to $10,560 before removing the old slab."),
        faq("What do pavers cost per square foot installed?", "$14 to $22 for a driveway in standard concrete pavers, $13 to $21 for a patio, $15 to $24 for a pool-deck overlay, $20 to $36 for travertine, in the current index."),
        faq("How much is a 600 sq ft paver pool deck?", "$9,000 to $14,400 as an overlay plus coping; $12,000 to $21,600 in travertine."),
        faq("How much does paver sealing cost?", f"{cost_range('paver-sealing')} including cleaning and polymeric re-sanding; a two-car driveway is about $840 to $1,560."),
        faq("Why are pavers more than concrete?", "Material and the base: a paver driveway needs 6 inches of compacted base, bedding sand, restraint and polymeric sand, plus cutting labor for borders. In exchange it can be lifted and relaid."),
        faq("What about the HOA fees?", "Application fees vary by association and pass through; our packet preparation is included."),
    ]
    return {"route": "/pricing/pavers/", "title": "Paver Cost in Kissimmee, FL (2026): Driveways & Decks", "meta_description": f"What pavers cost in Kissimmee in {R} 2026: driveways $14–$22/sq ft, pool-deck overlays, travertine, patios, walkways, sealing and repair, with worked examples for a two-car driveway and a 600 sq ft pool deck.", "h1": "Paver cost in Kissimmee, FL: per square foot and by project", "breadcrumbs": [("Home", "/"), ("Pricing", "/pricing/"), ("Paver cost guide", None)], "body_html": body, "faqs": faqs, "kind": "pricing", "nav_active": "/pricing/", "changelog": [f"{D} — {R} release; first published"]}


def cost_index():
    rows = []
    for k, name, unit, lo, hi, note in COST_INDEX:
        f = (lambda v: f"${v:,.2f}") if lo < 100 else (lambda v: f"${v:,.0f}")
        rows.append((k, name, unit, f(lo), f(hi), note or "&nbsp;"))
    body = sec("What the Kissimmee Concrete Cost Index is",
        cap(f"A quarterly table of installed price ranges for 18 residential concrete, paver and coating items in the Kissimmee and Osceola County market, published as a page, a table, and machine-readable CSV and JSON under a CC BY 4.0 license. Release {R} ({D}, version {COST_INDEX_RELEASE['version']}) is a market composite built from supplier price lists, published regional ranges and our own takeoffs for standard job sizes; as anonymized executed quotes accumulate they will be added and each item will show its sample size."),
        eyebrow="Dataset")
    body += sec(f"The {R} release table", table(["Key", "Item", "Unit", "Low", "High", "Notes"], rows, caption=f"Installed planning ranges, Kissimmee/Osceola market, release {R} ({D}). Not quotes. License CC BY 4.0 with attribution to Kissimmee Concrete and a link to this page.")
        + f"<p><a class=\"btn btn-primary\" href=\"/api/cost-index.json\">Download JSON</a> <a class=\"btn btn-outline\" href=\"/api/cost-index.csv\">Download CSV</a></p>", cls="alt")
    body += sec("Method",
        f"""<ol><li><strong>Inputs.</strong> Ready-mix concrete at $175–$280 per cubic yard delivered (Orlando-market supplier price lists, September 2026); limerock, bedding sand, polymeric sand, pavers, travertine and sealers at current dealer pricing; labor at prevailing crew rates for the Osceola market; permit and disposal fees at published schedules; published regional ranges from national cost references as a cross-check.</li>
<li><strong>Assumptions for the low end.</strong> Straightforward access, sound subgrade, standard finish, no removal, job size at or above the truck's full-load threshold.</li>
<li><strong>Assumptions for the high end.</strong> Removal of an old surface, tight or gated access, borders and bands, premium material within the item, small job size.</li>
<li><strong>Excluded.</strong> Structural fill to raise a slab, tree-root work, drainage systems, engineered walls, pump trucks, sales tax where applicable, financing, HOA fees. These are line items on a proposal.</li>
<li><strong>Sample.</strong> Release {R}: market composite, no executed-quote sample yet. From the next release, anonymized quotes (service, city, square footage, price, date) will be added; items with fewer than five quotes stay labelled composite.</li>
<li><strong>Update cadence.</strong> Quarterly; next release {COST_INDEX_RELEASE['next']}. Each release keeps the previous table available and notes what moved.</li></ol>
<p>Full detail and the other datasets we publish (NOAA normals, USDA soils, boundaries) are on <a href="/data-and-methods/">Data &amp; methods</a>.</p>""")
    body += sec("Limitations", "<ul><li>It prices the Kissimmee/Osceola market; the Polk ridge runs slightly lower on labor and the resort corridor slightly higher on scheduling.</li><li>It does not price your job. Subgrade, access and drainage are only known after a site visit.</li><li>It does not capture spring peak demand, when crew availability tightens.</li><li>Material prices move; the release date is the reference.</li></ul>", cls="alt")
    body += sec("How to cite", f"<p>\"Kissimmee Concrete Cost Index, release {R} ({D}), {BASE_URL}/pricing/kissimmee-concrete-cost-index/, CC BY 4.0.\" Realtors, property managers and other sites may reproduce the table with that attribution; we ask that ranges be quoted with their release label because they change quarterly.</p>")
    body += sec("Release history", table(["Release", "Date", "Version", "Change"], [(R, D, COST_INDEX_RELEASE["version"], "First release; market composite")]))
    schema = [{
        "@context": "https://schema.org", "@type": "Dataset",
        "name": "Kissimmee Concrete Cost Index",
        "description": f"Quarterly installed price ranges for 18 residential concrete, paver and coating items in the Kissimmee and Osceola County, Florida market. Release {R}, {D}. Planning ranges, not quotes.",
        "url": BASE_URL + "/pricing/kissimmee-concrete-cost-index/",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "creator": {"@type": "Organization", "name": PUBLIC_NAME, "url": BASE_URL + "/"},
        "publisher": {"@type": "Organization", "name": PUBLIC_NAME, "url": BASE_URL + "/"},
        "datePublished": D, "dateModified": D, "version": COST_INDEX_RELEASE["version"],
        "keywords": ["concrete driveway cost", "paver driveway cost", "pool deck cost", "Kissimmee", "Osceola County", "Florida", "cost index"],
        "spatialCoverage": {"@type": "Place", "name": "Kissimmee and Osceola County, Florida, USA"},
        "temporalCoverage": "2026-07/2026-09",
        "isAccessibleForFree": True,
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE_URL + "/api/cost-index.json"},
            {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": BASE_URL + "/api/cost-index.csv"},
        ],
        "variableMeasured": [{"@type": "PropertyValue", "name": name, "unitText": unit, "minValue": lo, "maxValue": hi, "unitCode": "USD"} for k, name, unit, lo, hi, note in COST_INDEX],
    }]
    faqs = [
        faq("Is the index based on real jobs?", f"Release {R} is a market composite from supplier price lists, published regional ranges and our own takeoffs. Executed-quote samples are added from the next release and each item will show its count."),
        faq("Can I reuse the data?", "Yes, under CC BY 4.0 with attribution to Kissimmee Concrete and a link to this page."),
        faq("Why publish prices at all?", "Because the question homeowners ask first is what it costs, and a range with a method beats a number with none."),
        faq("Does the index apply to Davenport or Winter Haven?", "As a reference, yes; the Polk ridge runs slightly lower on labor. The city pages note local adjustments."),
    ]
    return {"route": "/pricing/kissimmee-concrete-cost-index/", "title": f"Kissimmee Concrete Cost Index ({R}) – 18 Items, CSV/JSON", "meta_description": f"The Kissimmee Concrete Cost Index, release {R}: installed price ranges for 18 concrete, paver and coating items in the Kissimmee/Osceola market, with method, limitations and CC BY 4.0 downloads in CSV and JSON.", "h1": f"Kissimmee Concrete Cost Index, release {R}", "breadcrumbs": [("Home", "/"), ("Pricing", "/pricing/"), ("Cost Index", None)], "body_html": body, "faqs": faqs, "schema": schema, "kind": "pricing", "nav_active": "/pricing/", "changelog": [f"{D} — release {R} v{COST_INDEX_RELEASE['version']}, first publication"]}


def get_pages():
    return [pricing_hub(), concrete_guide(), paver_guide(), cost_index()]
