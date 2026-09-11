# -*- coding: utf-8 -*-
from _data import SERVICES, CONCRETE_SERVICES, PAVER_SERVICES, COATING_SERVICES, CITIES, TIER1, src, COST_INDEX_RELEASE
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, faq, cost_rows, callout, related, cs, esc


def concrete():
    intro = f'''
<section class="tight"><div class="wrap">
<p class="lede">Poured concrete is the workhorse surface in Osceola County: driveways, patios, pool decks, pads for sheds and generators, sidewalks and small commercial slabs. Done right on this soil it lasts 30 years or more. Done cheaply it cracks in the first wet season. This page covers what we pour, how we build the base for flatwoods sand and a 12-inch water table, what the county and the two cities require, and what each job costs in the {COST_INDEX_RELEASE['label']} Cost Index.</p>
<nav class="toc" aria-label="On this page"><ol>
<li><a href="#services">Concrete services</a></li><li><a href="#specs">Thickness, PSI and reinforcement</a></li><li><a href="#base">Base and drainage on Osceola sand</a></li><li><a href="#permits">Permits by jurisdiction</a></li><li><a href="#cost">Costs</a></li><li><a href="#process">How a pour day runs</a></li><li><a href="#areas">Where we pour</a></li></ol></nav>
</div></section>'''

    services_html = sec("Concrete services in Kissimmee and Osceola County", cards([
        (SERVICES[k]["name"], SERVICES[k]["short"] + ".", SERVICES[k]["route"], "Details, specs and prices") for k in CONCRETE_SERVICES
    ], cols=3), hid="services", eyebrow="Services")

    specs = sec("How thick, how strong, and what goes inside the slab",
        cap("For a car driveway or patio we pour 4 inches of 3,000 psi concrete with fiber reinforcement and #4 rebar along the edges and at re-entrant corners; for RV, boat or truck loads we go to 6 inches of 4,000 psi with a #4 rebar grid at 18 inches. The Florida Building Code's residential minimum for a slab on ground is 3½ inches (R506), and ACI 332 governs joint spacing.")
        + table(["Use", "Thickness", "Mix", "Reinforcement", "Joints"], [
            ("Walkway, small patio", "4 in", "3,000 psi", "Fiber; #4 bar at corners", "Every 8–10 ft"),
            ("Car driveway, patio, pool deck", "4 in", "3,000–3,500 psi", "Fiber + #4 perimeter bars; wire mesh only if held at mid-depth", "Every 10 ft, depth ¼ of slab"),
            ("Driveway with boat/RV, workshop slab", "6 in", "4,000 psi", "#4 rebar grid at 18 in on chairs", "Every 12–15 ft"),
            ("Shed, AC, generator, hot-tub pad", "4 in (5 in under a hot tub)", "3,000 psi", "Fiber; #3 or #4 grid under point loads", "None under 100 sq ft"),
            ("Apron in the right-of-way (Orange County spec)", "6 in", "3,000 psi", "No steel in the right-of-way", "Match county detail"),
        ], caption="Our standard specs. The written proposal lists the spec for your job; the county detail governs anything in the right-of-way.")
        + f"<p>Two things we do that many local quotes leave out. First, we hold reinforcement at mid-depth on chairs. Wire mesh that gets walked to the bottom of a 4-inch slab does nothing, which is why we prefer fiber plus perimeter rebar on 4-inch work; the trade-offs are in {compare('rebar-vs-fiber-vs-mesh')}. Second, we saw-cut or tool control joints to a quarter of the slab depth within 12 hours, so the shrinkage cracks that all concrete develops happen in the joint and not across the middle of the drive. {guide('why-concrete-cracks-osceola', 'Why concrete cracks here')} explains what is normal and what is not.</p>",
        hid="specs", cls="alt", eyebrow="Specifications")

    base = sec("Base and drainage on flatwoods sand",
        cap("Smyrna, Myakka and Immokalee fine sands cover most of the county. They are level, poorly drained and hold a water table around 12 inches deep from June through September (USDA Soil Data Access). A slab poured on that ground needs a compacted base, positive slope of at least ⅛ inch per foot away from the house, and somewhere for the water to go.")
        + f"""<p>Our base is 4 inches of compacted limerock or crushed concrete on driveways (2 to 4 inches on patios), placed on subgrade that has been proof-rolled and probed. Where we find muck, roots or a soft pocket, we dig it out and replace it with fill compacted in 4-inch lifts; on Basinger or Placid sand in a depression we tell you up front that the drive should be raised, because no thickness of concrete bridges saturated ground for long. Drainage is designed, not assumed: a lanai deck gets a channel drain, a driveway that slopes to the garage gets a trench drain at the door, and downspouts get extended past the slab edge. On the Polk County ridge the soil is Candler sand, deep and dry, and the base problem is the reverse; we cover that on the {city('davenport')} and {city('haines-city')} pages and in {guide('paver-base-flatwoods-vs-ridge')}.</p>
<p>Live oaks are the other base problem in older Kissimmee neighborhoods. Roots lift a 4-inch slab in five to ten years if the slab crosses a root zone; we route, bridge with thicker sections, or install a root barrier, and we explain the options in {guide('tree-roots-driveways-central-florida')}.</p>""",
        hid="base", eyebrow="Ground conditions")

    permits = sec("Which office permits concrete work",
        cap("Kissimmee city limits: the Engineering Division reviews driveway and sidewalk applications on EnerGov, plan review at least two business days. Unincorporated Osceola: a county driveway permit is required for construction or widening and residential driveways may not exceed 24 feet wide (§22-50.6). St. Cloud: patios and decks need a building permit. Polk: slabs supporting structures, within setbacks or in the right-of-way need a permit.")
        + f"<p>We pull the permit as the contractor of record, schedule the inspections, and give you the permit number for your records. You will sign the application and, on jobs of $5,000 or more in Osceola, a Notice of Commencement that gets recorded at the courthouse before the first inspection. The {tool('permit-finder')} tells you which jurisdiction your address is in; the {juris('city-of-kissimmee')}, {juris('osceola-county')}, {juris('city-of-st-cloud')} and {juris('polk-county')} pages quote the rules with sources.</p>",
        hid="permits", cls="alt", eyebrow="Permits")

    cost = sec(f"What poured concrete costs around Kissimmee ({COST_INDEX_RELEASE['label']})",
        cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "concrete-patio", "stamped-concrete", "concrete-slab-pad", "concrete-sidewalk", "concrete-removal", "concrete-resurfacing", "ready-mix"])
        + f"<p>Why the ranges are where they are: ready-mix runs $175 to $280 a cubic yard delivered in the Orlando market this quarter, a 4-inch slab uses one yard per 81 square feet, and the rest of the price is forming, base, steel, finishing labor and the truck's minimum load. Small pours (under 200 square feet) sit at the top of every range because the truck minimum and the crew day are the same. The full method is on the <a href=\"/pricing/kissimmee-concrete-cost-index/\">Cost Index</a> page and the by-project breakdown is in the <a href=\"/pricing/concrete/\">concrete cost guide</a>.</p>",
        hid="cost", eyebrow="Pricing")

    process = sec("How a driveway pour actually runs",
        f"""<ol class="steps">
<li><strong>Site visit and written proposal.</strong> We measure, probe the subgrade, check the soil map unit and the slope to the street, photograph access for the truck, and note HOA and permit requirements. The proposal lists thickness, PSI, reinforcement, base depth, joint layout and drainage.</li>
<li><strong>Permit and HOA.</strong> We file with the right office (city or county), you sign the application and, if required, the ARC form. Utility locates are called in at 811.</li>
<li><strong>Demolition and haul-off.</strong> The old slab is saw-cut at the apron and garage, broken, and hauled the same day. Old base is tested; if it is sound we reuse it, if not it goes too.</li>
<li><strong>Base, forms and steel.</strong> Limerock placed and compacted in lifts, forms set to the slope on the proposal, rebar on chairs, fiber in the mix, expansion joint at the garage and apron.</li>
<li><strong>Pour day.</strong> First truck at daylight in summer. Place, screed, bull-float, wait for bleed water to leave, edge, joint, broom, cure. In the rainy season the slab is covered before 2 p.m.</li>
<li><strong>Cure and joints.</strong> Control joints tooled or saw-cut within 12 hours. Foot traffic after 24 to 48 hours, cars after 7 days, heavy loads after 28. Curing details by month are in {guide('concrete-curing-florida-heat')}.</li>
<li><strong>Inspection, cleanup, warranty.</strong> Final inspection scheduled, forms pulled, sod edges dressed, and the written workmanship warranty handed over with the permit number.</li>
</ol>""",
        hid="process", cls="alt", eyebrow="Process")

    areas = sec("Where we pour concrete",
        f"<p>Service pages are written for Kissimmee, and each has city pages where the soil, permit office or housing stock changes the job: {cs('st-cloud', 'concrete-driveways')}, {cs('buenaventura-lakes', 'concrete-driveways')}, {cs('poinciana', 'concrete-driveways')}, {cs('davenport', 'concrete-driveways')}, {cs('haines-city', 'concrete-driveways')} and {cs('harmony', 'concrete-driveways')}. County-level detail lives on the <a href=\"/areas/osceola-county/\">Osceola County</a> and <a href=\"/areas/polk-county/\">Polk County</a> pages.</p>"
        + related([city(k) for k in TIER1]),
        hid="areas", eyebrow="Areas")

    faqs = [
        faq("Do you pour 4,000 psi on every driveway?", "No. 3,000 to 3,500 psi is right for a car driveway on a properly compacted base; the extra cement in a 4,000 psi mix helps under boat trailers, RVs and delivery trucks, which is where we specify it along with a 6-inch slab. Strength above what the load needs does not stop cracking; base and joints do."),
        faq("Can you match the color of my existing driveway when you add a section?", "New concrete is lighter for the first year and rarely matches perfectly. We match the finish (broom direction and texture), place a straight expansion joint at the seam so the line looks intentional, and can add a light integral color if the existing slab has aged to a warm gray."),
        faq("How long before I can park on it?", "Walk on it after 24 to 48 hours, park a car after 7 days, and keep boats, RVs and moving trucks off for 28 days. In July heat the surface sets faster but strength gain follows the same curve, so the calendar does not shorten."),
        faq("Will my concrete driveway crack?", "Every slab develops hairline shrinkage cracks; the job of the joints is to make them happen where you planned. Cracks that widen past about 1/8 inch, offset vertically, or run at a corner toward the garage point to base movement, and those are the ones we investigate. See the cracking guide for photos of each."),
        faq("Do I need a permit for a backyard patio slab?", "In St. Cloud, yes: patios are on the city's permit list. In unincorporated Osceola and inside Kissimmee, a detached patio slab outside setbacks is usually handled without a building permit, but anything within setbacks, attached to the house or in a flood zone should be confirmed with the office first, and HB 803's $7,500 exemption needs a written request. We confirm before we quote."),
        faq("Do you do stamped concrete and colored concrete?", "Yes. Slate, ashlar and wood-plank patterns with integral color and a release color, sealed with a solvent- or water-based sealer depending on the sun exposure. Stamped work runs $14 to $22 per square foot in the current index and needs re-sealing every two to three years here."),
    ]
    body = intro + services_html + specs + base + permits + cost + process + areas
    return {
        "route": "/concrete/",
        "title": "Concrete Contractor in Kissimmee, FL – Driveways, Patios, Slabs",
        "meta_description": "Poured concrete driveways, patios, pool decks, slabs and walkways in Kissimmee and Osceola County: 4 in / 3,000 psi specs, base for flatwoods sand, permits by office, current costs.",
        "h1": "Concrete driveways, patios, pool decks and slabs in Kissimmee, FL",
        "breadcrumbs": [("Home", "/"), ("Concrete", None)],
        "body_html": body,
        "faqs": faqs,
        "kind": "pillar",
        "nav_active": "/concrete/",
        "sources": ["fbc-r506", "aci332", "sda", "osceola-22-50-6", "kissimmee-driveway", "stcloud-permits", "polk-faq", "noaa"],
    }


def pavers():
    intro = f'''
<section class="tight"><div class="wrap">
<p class="lede">Pavers are the surface most of Osceola's newer communities were built with, and the one most HOAs on the resort corridor prefer for a remodel. We install concrete pavers, clay brick, permeable systems, travertine, marble and large-format porcelain on driveways, pool decks, patios, walkways and steps, and we clean, re-sand, seal and repair what is already there. Below: the base that stops settling on this sand, the HOA rules we have verified, current costs and where each job differs by city.</p>
<nav class="toc" aria-label="On this page"><ol>
<li><a href="#services">Paver and hardscape services</a></li><li><a href="#base">Base, bedding and edge restraint</a></li><li><a href="#materials">Materials and suppliers</a></li><li><a href="#hoa">HOA and permits</a></li><li><a href="#cost">Costs</a></li><li><a href="#maintain">Sealing and maintenance</a></li><li><a href="#areas">Where we install</a></li></ol></nav>
</div></section>'''

    services_html = sec("Paver, hardscape and coating services", cards([
        (SERVICES[k]["name"], SERVICES[k]["short"] + ".", SERVICES[k]["route"], "Details, specs and prices") for k in PAVER_SERVICES + COATING_SERVICES
    ], cols=3), hid="services", eyebrow="Services")

    base = sec("What goes under pavers on Osceola sand",
        cap("A paver driveway here gets 6 inches of compacted limerock (or crushed concrete) in two lifts, 1 inch of screeded bedding sand, 60 or 80 mm pavers, a concrete or spiked-aluminum edge restraint, and polymeric sand vibrated into the joints. Patios and pool decks get 4 to 5 inches of base. Celebration's pattern book specifies the 6-inch driveway base; industry guidance from the Concrete Masonry and Hardscapes Association (formerly ICPI) is the same order of magnitude for this soil.")
        + f"""<p>Settling is the complaint we are called out for most, and almost all of it traces to base. Fine sand that was never compacted, base placed on wet subgrade, a downspout discharging at the edge of the field, or edge restraint that was skipped so the outside course rolled. On flatwoods sand we compact the subgrade before the base goes down and we check moisture; on the Polk ridge's Candler sand we wet the base to get compaction at all. Where a driveway meets the street, most jurisdictions want a poured concrete apron rather than pavers in the right-of-way, and Polk County asks the owner to record a Paver Release Form if pavers do go there. The details by county are in {guide('paver-base-flatwoods-vs-ridge')} and on the {juris('polk-county')} page.</p>
<p>Lifting and relaying is the advantage pavers have over concrete. A sunken area by the garage can be pulled, the base rebuilt, and the same pavers reset in a day; the {svc('paver-repair')} page shows what that costs and when it is worth it.</p>""",
        hid="base", cls="alt", eyebrow="Installation")

    materials = sec("Materials we install and where they come from",
        table(["Material", "Typical use", "Thickness", "Notes"], [
            ("Concrete pavers (Belgard, Tremron, Oldcastle Coastal lines)", "Driveways, patios, walks", "60 mm patios, 80 mm driveways", "Widest color and pattern range; most HOA-approved lines are here"),
            ("Clay brick pavers", "Walks, borders, traditional driveways", "2¼ in", "Color does not fade; smaller units mean more joints"),
            ("Permeable pavers", "Driveways where runoff matters", "80 mm", "Open-graded stone base instead of limerock; fewer HOAs have an approved detail"),
            ("Travertine (tumbled or honed)", "Pool decks, lanais, patios", "1¼ in (3 cm) pavers, ½ in tiles for thin-set", "Cooler barefoot than concrete pavers; needs a breathable sealer"),
            ("Marble", "Pool decks, lanais", "1¼ in", "Lightest color, coolest surface; higher cost"),
            ("Large-format porcelain", "Modern lanais, steps, entries", "2 cm (¾ in)", "Stain-proof and uniform; must be set on a rigid base or pedestals"),
            ("Thin pavers / remodel pavers", "Overlays on sound existing pool decks", "1 in (25–30 mm)", "Adds height at doors and coping; we check thresholds first"),
        ], caption="Supplier plants and design centers for the Orlando market are listed on the manufacturer sites (Belgard dealer locator; Tremron locations; Oldcastle Coastal).")
        + f"<p>Belgard's Luxury collection and Tremron's Orlando-area production give us short lead times on most lines; special-order travertine and porcelain add two to four weeks. If your community's approved palette is a discontinued line, we source matching pieces for repairs before we recommend a full replacement. Comparisons homeowners ask for most: {compare('travertine-vs-concrete-pavers')}, {compare('concrete-vs-pavers')} and {compare('stamped-vs-pavers')}.</p>",
        hid="materials", eyebrow="Materials")

    hoa_html = sec("HOA approval and permits for paver work",
        cap("Every planned community in our area requires written architectural approval before pavers go down. Poinciana's DCB names concrete, asphalt and brick pavers as the driveway materials and deems an unanswered application denied after 30 days. Solterra caps a widened driveway at three cars and may require the installer's insurance certificate. Solivita wants replacement driveways in the original style and material. Permits are lighter: St. Cloud sends driveway pavers to Public Works, Osceola covers them under the driveway permit, Polk regulates pavers within setbacks and in the right-of-way.")
        + f"<p>Verified criteria, with section numbers, are on the community pages for <a href=\"/hoa/poinciana-apv/\">Poinciana (APV)</a>, <a href=\"/hoa/solivita/\">Solivita</a>, <a href=\"/hoa/celebration/\">Celebration</a>, <a href=\"/hoa/bellalago/\">Bellalago</a> and <a href=\"/hoa/solterra/\">Solterra</a>. The {tool('hoa-packet-checklist')} assembles the submission, and the {tool('permit-finder')} sorts out city versus county for your address.</p>",
        hid="hoa", cls="alt", eyebrow="HOA &amp; permits")

    cost = sec(f"What pavers cost around Kissimmee ({COST_INDEX_RELEASE['label']})",
        cost_rows(["paver-driveway-concrete", "paver-driveway-premium", "paver-patio", "paver-pool-deck", "travertine-pool-deck", "paver-walkway", "paver-sealing", "paver-repair", "concrete-removal"])
        + f"<p>Material is 35 to 50 percent of a paver job; the rest is base, labor and cuts. Borders and bands add pattern and cutting time, curves add waste, and a driveway that needs the old concrete removed adds $2 to $4 per square foot before the first paver is set. Per-project examples (two-car driveway, 12-by-12 patio, 600-square-foot pool deck) are in the <a href=\"/pricing/pavers/\">paver cost guide</a>.</p>",
        hid="cost", eyebrow="Pricing")

    maintain = sec("Sealing, re-sanding and keeping pavers looking new",
        cap("Seal concrete pavers 60 to 90 days after installation, then every three to four years on a driveway and every two to three on a pool deck that sees pool chemicals and afternoon storms. Re-sand joints with polymeric sand whenever they drop below the chamfer. Travertine and marble take a penetrating, breathable sealer, never a film-forming one, or moisture from the bedding sand will haze under the coating.")
        + f"<p>Well-water irrigation is the local villain: iron in the water oxidizes on the surface and leaves orange streaks wherever a head overshoots the lawn. Sealer makes rust easier to remove but does not prevent it; the fix is head adjustment or an iron filter, covered in {guide('rust-stains-irrigation-well-water')}. Efflorescence, the white haze that shows up after the first rainy season, is normal on new concrete pavers and washes off with an efflorescence cleaner before sealing. The full maintenance schedule is on the {svc('paver-sealing')} page and the sealer chemistry is in {compare('sealer-types')}.</p>",
        hid="maintain", cls="alt", eyebrow="Maintenance")

    areas = sec("Where we install pavers",
        f"<p>Service pages are anchored in Kissimmee; the city pages cover what changes locally: {cs('celebration', 'paver-driveways')}, {cs('st-cloud', 'paver-pool-decks')}, {cs('reunion', 'paver-travertine')}, {cs('four-corners', 'paver-pool-decks')}, {cs('champions-gate', 'paver-sealing')}, {cs('davenport', 'paver-driveways')} and {cs('harmony', 'paver-pool-decks')}.</p>" + related([city(k) for k in TIER1]),
        hid="areas", eyebrow="Areas")

    faqs = [
        faq("Can pavers go over my existing concrete pool deck?", "Usually, if the deck is sound and the added inch does not create a step at sliding doors or bury the pool coping. We check thresholds, drainage and the condition of the slab first; if the deck is heaving or hollow, a thin overlay hides the problem for a year and then follows it."),
        faq("How long does a paver driveway take?", "Three to five working days for a typical two-car driveway with removal of the old concrete: one day to demo and haul, one to build and compact the base, one or two to set the field and cut borders, and a half day to sand, compact and clean. Sealing waits 60 to 90 days."),
        faq("Do pavers need a permit?", "In unincorporated Osceola the driveway permit covers a paver driveway and the county caps width at 24 feet. St. Cloud refers driveway and sidewalk pavers to Public Works rather than issuing a building permit. Polk County regulates pavers within setbacks or next to structures and has a release form for pavers in the right-of-way. Patios and pool decks in the back yard are mostly an HOA matter, but we confirm with the office for your address."),
        faq("Why are there ants and weeds in my joints?", "Because the joint sand is regular sand or the polymeric sand was installed wet or too thin. Ants tunnel through loose sand and carry it up as mounds; weed seeds germinate in the same loose joints. Cleaning, re-sanding with a polymeric product and sealing closes the joints for years."),
        faq("Which pavers stay coolest for a pool deck?", "Light travertine and marble measure the coolest in published comparisons, standard concrete pavers in a light color next, dark concrete pavers and dark porcelain the hottest. Our comparison page collects the published numbers and explains how we plan to measure decks here in July with an infrared thermometer."),
        faq("Do you sell pavers without installation?", "No. We are installers; the manufacturers' dealer locators list retail yards in the Orlando market for do-it-yourself buyers."),
    ]
    body = intro + services_html + base + materials + hoa_html + cost + maintain + areas
    return {
        "route": "/pavers/",
        "title": "Paver Installation in Kissimmee, FL – Driveways, Pool Decks",
        "meta_description": "Paver driveways, travertine and marble pool decks, patios, walkways, sealing and repair in Kissimmee and Osceola County. 6-inch base, HOA rules verified, current costs per square foot.",
        "h1": "Paver driveways, pool decks, patios and hardscape in Kissimmee, FL",
        "breadcrumbs": [("Home", "/"), ("Pavers", None)],
        "body_html": body,
        "faqs": faqs,
        "kind": "pillar",
        "nav_active": "/pavers/",
        "sources": ["icpi", "apv", "solivita", "solterra", "celebration", "stcloud-permits", "polk-paver-release", "osceola-22-50-6", "belgard", "tremron", "oldcastle"],
    }


def get_pages():
    return [concrete(), pavers()]
