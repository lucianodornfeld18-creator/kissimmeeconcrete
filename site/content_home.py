# -*- coding: utf-8 -*-
from _data import CITIES, TIER1, TIER2, SERVICES, CONCRETE_SERVICES, PAVER_SERVICES, TOOLS, GUIDES, COST_INDEX_RELEASE, src, drive_estimate
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, lead_form, faq, cost_rows, callout, related, esc
from _photos import home_strip


def get_pages():
    hero = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow" style="color:#D3A64A">Kissimmee · Osceola County · Polk ridge</span>
      <h1>Concrete and paver contractor for Kissimmee, St. Cloud and the 40 miles around them</h1>
      <p class="lede">Driveways, patios, pool decks, slabs and walkways in poured concrete. Paver driveways, travertine and marble pool decks, walkways, sealing and repair. Built on Osceola's wet flatwoods sand and Polk's dry ridge sand by a crew that knows which one your lot sits on, which office issues your permit, and what your HOA will ask for.</p>
      <div class="cta-row"><a class="btn btn-primary" href="/contact/">Request a free estimate</a><a class="btn btn-outline" href="/pricing/">See current price ranges</a></div>
      <p class="small" style="color:#D8D5CC;margin-top:14px">Insured. Free on-site estimates with a written proposal. Workmanship warranty in writing. Every quote states thickness, mix, reinforcement, base depth and drainage, so you can compare it line by line with anyone else's.</p>
    </div>
    <div>{lead_form(heading="Free estimate in two business days", compact=True)}</div>
  </div>
</section>
<div class="wrap"><div class="data-strip">
  <div><b>16–18</b><span>rain days a month, June–August, at the Kissimmee 2 NOAA station (1991–2020). We pour before noon in the rainy season.</span></div>
  <div><b>12 in</b><span>typical wet-season water table under Smyrna and Myakka fine sand, the two most common soils in Osceola County (USDA).</span></div>
  <div><b>24 ft</b><span>maximum residential driveway width in unincorporated Osceola County without a conditional use (Code §22-50.6).</span></div>
  <div><b>{COST_INDEX_RELEASE['label']}</b><span>Cost Index release. Installed ranges per square foot for 18 items, refreshed quarterly, downloadable as CSV/JSON.</span></div>
</div></div>'''

    concrete_cards = cards([
        ("Concrete driveways", "New pours, tear-out and replacement, widening to the 24-foot county limit, aprons and turnarounds. 4 inches at 3,000 psi for cars, 6 inches with #4 rebar for boats and RVs.", "/concrete/driveways/", "Driveway details and prices"),
        ("Patios and pool decks", "Broom, smooth and exposed-aggregate patios; textured and knock-down pool decks that drain away from the pool and stay walkable in July.", "/concrete/patios/", "Patios"),
        ("Slabs and pads", "Shed pads, AC and generator pads, hot-tub and workshop slabs sized to the equipment and to the Florida Building Code's 3½-inch minimum.", "/concrete/slabs/", "Slabs and pads"),
        ("Stamped and decorative", "Integral color, release colors, slate and ashlar patterns, sealed and re-sealed on a schedule that suits a wet climate.", "/concrete/stamped/", "Stamped concrete"),
        ("Repair and resurfacing", "Cracks, spalling, sunken sections near the garage and the street, trip hazards, and honest advice on when lifting or an overlay beats a new pour.", "/concrete/repair/", "Repair"),
        ("Sidewalks, commercial, architectural", "Walkways and right-of-way sidewalk sections, small parking areas and dumpster pads, and honed or board-formed finishes for modern homes.", "/concrete/", "All concrete services"),
    ])
    paver_cards = cards([
        ("Paver driveways", "60 and 80 mm concrete pavers, clay brick and permeable systems over a 6-inch compacted limerock base, with borders, bands and a concrete apron where the county requires one.", "/pavers/driveways/", "Paver driveways"),
        ("Paver and travertine pool decks", "Thin-paver remodels over existing decks, full rebuilds, bullnose coping, drain channels in the lanai, travertine and marble that stay cooler barefoot.", "/pavers/pool-decks/", "Pool decks"),
        ("Patios, walkways and steps", "Lanai extensions, fire-pit patios, front walks and entry steps with riser lighting. Porcelain and large-format options for contemporary homes.", "/pavers/patios/", "Patios"),
        ("Sealing, cleaning and re-sanding", "Clean, re-sand with polymeric sand, seal with a breathable or wet-look product, and a schedule for re-sealing that matches how much rain the deck sees.", "/pavers/sealing/", "Sealing"),
        ("Paver repair", "Sunken areas by the garage or the downspout, failed edge restraint, ant hills and weeds in the joints, matching replacement pieces for discontinued lines.", "/pavers/repair/", "Repair"),
        ("Walls, turf, lighting", "Decorative segmental walls and seat walls, fire pits and summer kitchens, turf strips, and low-voltage lighting built into the hardscape.", "/pavers/retaining-walls-outdoor-living/", "Outdoor living"),
    ])

    soils = sec(
        "Why the ground under Kissimmee changes how we build",
        cap("Most of Osceola County sits on Smyrna, Myakka and Immokalee fine sands: flat, poorly drained, with a wet-season water table about 12 inches down (USDA Soil Data Access, county FL097). The Polk County ridge around Davenport, Haines City and Lake Wales is Candler sand, deep and excessively drained. The two need different base prep, so we look up your soil unit before we price the job.")
        + f"""<p>On flatwoods sand the base has to be compacted in lifts and the slab has to shed water, because the ground under it will be saturated for weeks every summer. A driveway that sits in a low spot on Basinger sand (water table at the surface in June) needs a raised section and a swale, not just more concrete. On the ridge the problem flips: Candler sand is so free-draining that a base placed dry will not compact, so we wet it, compact it, and check it with a probe before any rock goes down. We explain the difference in {guide('paver-base-flatwoods-vs-ridge', 'our flatwoods-versus-ridge guide')}, and the {tool('permit-finder')} tells you which county and which soil group your address falls in.</p>
<p>Rain is the other constraint. The Kissimmee 2 NOAA station averages 15.8 days with measurable rain in June, 16.7 in July and 17.7 in August, with 12 or 13 of those days over a tenth of an inch. From October to April the count drops to 6 or 7. That is why our summer pours start at first light and are usually finished and covered before the sea-breeze storms build after 2 p.m. The {tool('pour-calendar')} shows the month-by-month numbers and the pour window we recommend.</p>""",
        eyebrow="Local conditions")

    permits = sec(
        "Who issues your permit depends on which side of a line you live on",
        cap("Inside Kissimmee city limits, driveway and sidewalk work goes through the City's Engineering Division on the EnerGov portal. In unincorporated Osceola County, §22-50.6 requires a county driveway permit for any new or widened residential driveway and caps width at 24 feet. In St. Cloud, pavers on a driveway are referred to Public Works rather than the Building Department. Polk County has its own rules and a paver release form.")
        + table(
            ["Jurisdiction", "Driveway / apron", "Patio, slab, pad", "Pavers", "Office"],
            [
                ("City of Kissimmee", "Driveway / Sidewalk Construction application; plan review at least 2 business days; permit at least 2 business days after payment", "Building Division review; confirm scope with permitting@kissimmee.org", "Same driveway application when in the right-of-way", f"{juris('city-of-kissimmee', 'Engineering, 101 Church St · 407-518-2278')}"),
                ("Unincorporated Osceola", "County driveway permit required for construction or widening; 24 ft maximum width (§22-50.6)", "Building Office; residential plan review normally 3–5 days; NOC at $5,000+", "Driveway permit covers pavers in the drive; right-of-way work under LDC 4.12.2", f"{juris('osceola-county', '1 Courthouse Sq · 407-742-0200')}"),
                ("City of St. Cloud", "Building Department; work in the right-of-way needs Public Works approval", "Patios and decks need a permit (city list)", "Driveway and sidewalk pavers: refer to Public Works (no building permit)", f"{juris('city-of-st-cloud', '1300 9th St · 407-957-7300')}"),
                ("Polk County (unincorporated)", "Portions of driveways in the right-of-way or within setbacks need a permit", "Slabs adjacent to or supporting a structure, elevated slabs, slabs within setbacks", "Pavers within setbacks or adjacent to structures must meet the codes; Paver Release Form for pavers in the right-of-way", f"{juris('polk-county', 'Bartow / Lake Alfred · 863-534-6080')}"),
            ],
            caption="Summary of rules verified on official pages on 2026-09-10. Each linked permit page quotes the source and tells you what we file and what you file.",
        )
        + f"<p>Florida's new HB 803 exempts single-family work valued under $7,500 from a building permit from July 1, 2026, with exceptions for structural, electrical, plumbing, mechanical, gas and flood-zone work, and only after a written exemption request. A small pad may qualify; a driveway in the right-of-way still needs its driveway permit. Details and the caveats are in {guide('hb-803-permit-exemption', 'our HB 803 guide')}.</p>",
        cls="alt", eyebrow="Permits")

    pricing = sec(
        f"What concrete and pavers cost around Kissimmee right now ({COST_INDEX_RELEASE['label']})",
        cap(f"A plain broom-finish concrete driveway runs about $8.50 to $13.50 per square foot installed in the Kissimmee market in the {COST_INDEX_RELEASE['label']} release of our Cost Index; a paver driveway on a 6-inch limerock base runs $14 to $22; a travertine pool deck $20 to $36. Tearing out an old slab adds $2 to $4 per square foot. These are planning ranges with a published method, not quotes.")
        + cost_rows(["concrete-driveway-broom", "paver-driveway-concrete", "paver-pool-deck", "travertine-pool-deck", "concrete-patio", "paver-sealing", "epoxy-garage", "concrete-removal"])
        + f"<p>The full index has 18 items, a per-project view (two-car driveway, 12-by-12 patio, 600-square-foot pool deck) and the reasoning behind each range. It is published as a page, a table and as <a href=\"/api/cost-index.json\">JSON</a> and <a href=\"/api/cost-index.csv\">CSV</a> under a CC BY 4.0 license so Realtors, property managers and other sites can cite it. Read the <a href=\"/pricing/kissimmee-concrete-cost-index/\">Kissimmee Concrete Cost Index</a>, the <a href=\"/pricing/concrete/\">concrete cost guide</a> or the <a href=\"/pricing/pavers/\">paver cost guide</a>.</p>",
        eyebrow="Pricing")

    area_rows = []
    for k in TIER1:
        c = CITIES[k]
        area_rows.append((city(k), c["county"], f"{c['miles']} mi" if c["miles"] else "anchor", f"about {drive_estimate(c['miles'])} min" if c["miles"] else "n/a", c["pop"]))
    areas = sec(
        "Where we work across Osceola County and the Polk ridge",
        f"""<p>We estimate within roughly 40 miles of downtown Kissimmee. Osceola County is home turf, and the resort corridor and the Polk ridge along US-27 and I-4 are where most of the rest of the work is. The table gives each place's straight-line distance and a rough weekday drive estimate, so you can see where you sit relative to us before you call.</p>"""
        + table(["Place", "County", "Distance", "Drive (est.)", "Population"], area_rows, caption="Population: Florida EDR 2025 estimates for incorporated cities; CDPs and communities have no municipal figure.")
        + f"<p>Polk ridge towns with their own pages: {', '.join(city(k) for k in TIER2)}. South Orange County communities such as Hunters Creek, Meadow Woods, Southchase and Lake Nona are close to us, and we take those calls, but their pages live with our Orlando-area colleagues; see <a href=\"/areas/orange-county-south/\">South Orange County</a> and the full <a href=\"/areas/\">service-area map</a>.</p>",
        cls="alt", eyebrow="Service area")

    tools_html = sec(
        "Tools we built for homeowners here",
        cards([
            (TOOLS["permit-finder"]["name"], "Two municipal lines run through our territory and neither is obvious from the street. Enter an address and see which office has your job.", TOOLS["permit-finder"]["route"], "Check an address"),
            (TOOLS["concrete-paver-calculator"]["name"], "Volume, bags, rock depth, unit counts and joint sand, with the waste factor set by the pattern you pick.", TOOLS["concrete-paver-calculator"]["route"], "Run the numbers"),
            (TOOLS["pour-calendar"]["name"], "Thirty years of station normals turned into the months that pour easily and the months that need a daylight start.", TOOLS["pour-calendar"]["route"], "See the calendar"),
            (TOOLS["concrete-vs-pavers"]["name"], "Eight questions, one recommendation, and the reasoning shown so you can disagree with it.", TOOLS["concrete-vs-pavers"]["route"], "Get a recommendation"),
            (TOOLS["hoa-packet-checklist"]["name"], "Every document five local boards have asked us for, gathered on one printable page.", TOOLS["hoa-packet-checklist"]["route"], "Build your packet"),
            (TOOLS["project-brief"]["name"], "Fix the specification so three bidders price the same job instead of three different ones.", TOOLS["project-brief"]["route"], "Write a brief"),
        ]),
        eyebrow="Tools")

    hoa_sec = sec(
        "HOA and ARC rules we have read so you don't have to",
        cap("Poinciana's Design Control Board (APV) calls for concrete, asphalt or brick pavers on driveways and treats a silent 30 days as a denial. Solivita requires replacement driveways in the original builder's style and materials. Solterra caps expanded driveways at three cars wide and bans painted or stained concrete. Celebration's ARC meets on the third Monday. Bellalago reviews twice a month through ConnectResident.")
        + f"<p>We quote the actual criteria, with section numbers, on each community page: {hoa('poinciana-apv')}, {hoa('solivita')}, {hoa('celebration')}, {hoa('bellalago')} and {hoa('solterra')}. For Storey Lake, Tapestry, Reunion, ChampionsGate, Windsor Hills and Providence we have management contacts but not verified written criteria yet, so we say so rather than guess. The {tool('hoa-packet-checklist')} assembles what those boards typically ask for: site plan or survey, product sample, color, pattern, drainage note and the installer's insurance certificate.</p>",
        cls="alt", eyebrow="HOA / ARC")

    guides_html = sec(
        "Guides written for this county, not for the whole country",
        cards([
            (GUIDES["why-concrete-cracks-osceola"]["name"], "Shrinkage cracks versus base failure, what a 12-inch water table does to a slab, and the joints that keep cracks where you want them.", GUIDES["why-concrete-cracks-osceola"]["route"], "Read the guide"),
            (GUIDES["rust-stains-irrigation-well-water"]["name"], "Iron in well water oxidizes on concrete and pavers. How to tell rust from tannin, oil and efflorescence, what removes each, and how to stop the sprinkler from re-staining.", GUIDES["rust-stains-irrigation-well-water"]["route"], "Read the guide"),
            (GUIDES["vacation-rental-owner-hardscape-guide"]["name"], "Scheduling around guest turnovers, HOA approvals in resort communities, and the surfaces that hold up to rental traffic.", GUIDES["vacation-rental-owner-hardscape-guide"]["route"], "Read the guide"),
        ]),
        eyebrow="Guides")

    faqs = [
        faq("Do you serve both Kissimmee and St. Cloud?", "Yes. Kissimmee and St. Cloud are the two cities we estimate in most, and they have different permit offices: Kissimmee's Engineering Division handles driveway and sidewalk applications on EnerGov, while St. Cloud's Building Department covers patios and decks and sends driveway pavers to Public Works. Between them, unincorporated Osceola County follows §22-50.6 for driveways."),
        faq("What should I check before hiring anyone for this work?", "Insurance, in the form of a certificate sent by the agent rather than a photo. The exact business name, checked on Sunbiz. Two or three addresses of jobs finished more than two years ago that you can drive past. And a written contract that states thickness, mix, reinforcement, base depth, joint layout and drainage. Our guide walks through all four."),
        faq("How soon can you come out?", "We schedule site visits within two business days in Kissimmee, St. Cloud, Celebration, Poinciana and Buenaventura Lakes, and within three for the Polk ridge and the Four Corners resort communities. Spring is our busiest season: Google Trends for the Orlando market shows paver interest peaking in April and May every year, so book early if you want a pool deck done before summer."),
        faq("Do you pour in the rainy season?", "Yes, with an early start. June through September average 14 to 18 rain days a month at the Kissimmee 2 station, almost all of it afternoon storms. Forms and base are prepared the day before, trucks arrive at first light, and the slab is finished and covered before the storms build. If the morning forecast shows more than a 60 percent chance of rain before 2 p.m., we move the pour."),
        faq("Concrete or pavers for a driveway?", "Concrete costs less up front ($8.50 to $13.50 per square foot for a broom finish in our current index) and gives a clean, uniform look. Pavers cost more ($14 to $22 for standard concrete pavers) but can be lifted and relaid after settling or a utility repair, and many HOAs on the Osceola and Polk resort corridor prefer them. Our decision tool walks through use, budget, HOA, heat and resale in eight questions."),
        faq("Do you work with HOAs and property managers?", "Every week. We prepare the packet the architectural review committee asks for (survey or site plan, product and color sample, pattern, drainage note, our insurance certificate) and we schedule around guest turnovers for vacation rentals in Four Corners, ChampionsGate, Reunion and Windsor Hills."),
        faq("What is the Kissimmee Concrete Cost Index?", f"A quarterly table of installed price ranges for 18 concrete, paver and coating items in the Kissimmee and Osceola County market, with the method published and the data downloadable as CSV and JSON under a CC BY 4.0 license. The {COST_INDEX_RELEASE['label']} release is a market composite from supplier price lists and published regional ranges; as anonymized job quotes accumulate they will be added to the sample and the release notes will say so."),
        faq("Who does the work and who owns this site?", "Kissimmee Concrete is the Osceola County and Polk ridge service brand of a Central Florida concrete and paver contractor; the crews that install your job are the same crews behind our sister brands in West Orange and South Lake counties. The legal entity, insurance and warranty terms are listed on the About page and in every written proposal."),
    ]

    body = hero + sec("Concrete work, priced and built for Osceola County", concrete_cards + f"<p style=\"margin-top:18px\"><a class=\"card-link\" href=\"/concrete/\">Everything we do in poured concrete &rarr;</a></p>", eyebrow="Concrete") \
        + sec("Pavers, travertine and outdoor living", paver_cards + f"<p style=\"margin-top:18px\"><a class=\"card-link\" href=\"/pavers/\">Everything we do in pavers and hardscape &rarr;</a></p>", cls="alt", eyebrow="Pavers &amp; hardscape") \
        + soils + permits + pricing + areas + home_strip() + tools_html + hoa_sec + guides_html \
        + sec("Ready for a number you can plan around?", "<p class=\"lede\">Send the form, or email hello@kissimmeeconcrete.com with a photo and rough dimensions. We visit, measure, check the soil and the access, and send a written proposal that lists thickness, PSI, reinforcement, base depth and drainage so you can compare it line by line with anyone else's.</p><div class=\"cta-row\"><a class=\"btn btn-primary\" href=\"/contact/\">Request a free estimate</a><a class=\"btn btn-outline\" href=\"/tools/project-brief/\">Build a project brief first</a></div>", cls="alt")

    return [{
        "route": "/",
        "title": "Kissimmee Concrete | Concrete & Paver Contractor, Kissimmee FL",
        "meta_description": "Concrete driveways, patios, pool decks and slabs plus paver driveways, travertine decks, sealing and repair across Kissimmee, St. Cloud, Osceola County and the Polk ridge. Free estimates.",
        "h1": "Concrete and paver contractor for Kissimmee, St. Cloud and the 40 miles around them",
        "body_html": body,
        "faqs": faqs,
        "kind": "home",
        "is_home": True,
        "nav_active": "/",
        "sources": ["osceola-22-50-6", "kissimmee-driveway", "stcloud-permits", "polk-faq", "noaa", "sda", "edr", "hb803"],
    }]
