# -*- coding: utf-8 -*-
"""Eleven paver & hardscape service pages, anchored in Kissimmee."""
from _data import SERVICES, CITIES, TIER1, COST_INDEX_RELEASE, src
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, callout, related, cs, cities_for_service, steps, esc


def crumbs(key):
    return [("Home", "/"), ("Pavers", "/pavers/"), (SERVICES[key]["name"], None)]


def city_links(key):
    links = [cs(c, key, CITIES[c]["name"]) for c in cities_for_service(key)]
    if not links:
        return ""
    return sec("City pages for this service", "<p>Kissimmee is the anchor. These pages cover what changes locally: base on ridge sand versus flatwoods sand, which office you deal with, the HOA, and the age and type of the houses.</p>" + related(links), eyebrow="City pages")


def page(key, title, desc, h1, body, faqs, sources):
    return {"route": SERVICES[key]["route"], "title": title, "meta_description": desc, "h1": h1, "breadcrumbs": crumbs(key), "body_html": body + city_links(key), "faqs": faqs, "kind": "service", "service_key": key, "nav_active": "/pavers/", "sources": sources}


# ---------------------------------------------------------------------------
def driveways():
    k = "paver-driveways"
    body = sec("Paver driveway cost, base depth and timeline in Kissimmee",
        cap(f"A paver driveway on standard concrete pavers runs {cost_range('paver-driveway-concrete')} installed in the {COST_INDEX_RELEASE['label']} Cost Index; premium lines such as Belgard Luxury or large-format units run {cost_range('paver-driveway-premium')}. Under the pavers: 6 inches of compacted limerock, 1 inch of bedding sand, 80 mm pavers, edge restraint and polymeric sand. Three to five working days for a two-car driveway, sealing 60 to 90 days later."),
        eyebrow="Quick answer")
    body += sec("What we install",
        f"""<p>New paver driveways over a removed concrete drive, paver driveways for new construction in Harmony, Sunbridge, Weslyn Park and the Bellalago and Tapestry phases still building out, widening an existing paver drive with matching or contrasting units, paver aprons and borders on a concrete drive, and full replacements in the resort communities off US-27 and Osceola Parkway where the builder's original pavers have settled after fifteen years of rental traffic. Layouts: running bond and herringbone for strength under tires, ashlar and random patterns for a stone look, soldier and sailor borders, contrasting bands across a long drive to break it up, and turf or gravel ribbons on modern homes.</p>
<p>Paver types: 60 mm concrete pavers for patios and 80 mm for driveways; clay brick for a traditional look that never fades; permeable interlocking pavers on an open-graded stone base where the lot cannot take more runoff; travertine and porcelain on driveways only in thick formats and only where the HOA allows. Suppliers with plants or design centers serving the Orlando market include Belgard (Oldcastle), Tremron and Oldcastle Coastal; most HOA-approved palettes in Osceola come from those three catalogs.</p>""")
    body += sec("How much base does a paver driveway need on Osceola sand?",
        cap("Six inches of compacted limerock or crushed concrete, placed in two 3-inch lifts and compacted to a refusal reading with a plate compactor, on subgrade that has been proof-rolled and probed. Then 1 inch of screeded concrete sand, the pavers, a concrete or spiked-aluminum edge restraint, and polymeric sand vibrated into the joints with a plate compactor on a pad. Celebration's pattern book calls for the same 6-inch driveway base.")
        + table(["Layer", "Driveway", "Patio / walkway", "Why"], [
            ("Subgrade", "Proof-rolled, probed, muck removed", "Same", "Smyrna/Myakka sand holds water 12 in down in summer; soft pockets settle"),
            ("Geotextile", "Where subgrade is wet or organic", "Optional", "Keeps sand from migrating into the base"),
            ("Base", "6 in limerock, 2 lifts", "4–5 in", "Load spread; the layer that stops settling"),
            ("Bedding sand", "1 in concrete sand, screeded, never compacted before pavers", "1 in", "Levels the units; more than 1½ in and it rolls"),
            ("Pavers", "80 mm (3⅛ in)", "60 mm (2⅜ in)", "Thicker units interlock under tires"),
            ("Edge restraint", "Concrete curb or spiked aluminum on the base", "Same", "Without it the outside course rolls within a year"),
            ("Joint sand", "Polymeric, vibrated in, dry install", "Same", "Locks the field and keeps ants and weeds out"),
        ], caption="Our standard section. Industry guidance from the Concrete Masonry and Hardscapes Association (formerly ICPI) is the reference for depths and materials.")
        + f"<p>Settling at the garage and along the edges is the paver complaint we are called about most, and it traces to base almost every time: sand never compacted, base placed on saturated subgrade in July, a downspout discharging at the edge, or no edge restraint. On the Polk County ridge the problem inverts: Candler sand will not compact dry, so the base gets wetted before the plate goes over it. The two soils get their own guide: {guide('paver-base-flatwoods-vs-ridge')}.</p>", cls="alt")
    body += sec("Permits, aprons and HOA rules for paver driveways",
        cap("Unincorporated Osceola County covers a paver driveway under the same driveway permit as concrete (§22-50.6) and caps width at 24 feet. St. Cloud refers driveway pavers to Public Works rather than issuing a building permit. Kissimmee reviews the driveway through its Engineering application. Polk County regulates pavers within setbacks and, for pavers in the right-of-way, asks the owner to record a Concrete Driveway Paver Release Form accepting maintenance and liability.")
        + f"""<p>Most jurisdictions want the apron in the public right-of-way poured in concrete rather than pavers, so a paver driveway usually ends at a concrete apron with a soldier course at the seam; you can see that detail in our gallery. HOA approval comes before any of it. Poinciana's DCB names concrete, asphalt and brick pavers as the driveway materials and treats 30 days of silence as a denial (Criteria 9.1.1 and 6.1); Solivita requires the original builder's style and material on a replacement and reviews extensions; Solterra caps an expanded drive at three cars wide and can require the installer's insurance certificate. Details: {hoa('poinciana-apv')}, {hoa('solivita')}, {hoa('solterra')}, {hoa('celebration')}, {hoa('bellalago')}; packet: {tool('hoa-packet-checklist')}; jurisdiction: {tool('permit-finder')}.</p>""")
    body += sec("Process and timeline",
        steps([
            "Site visit: measure, check the fall to the street and the garage, probe the subgrade, photograph access, note the HOA's approved palette. Written proposal with the base section, paver line, pattern, borders and price.",
            "HOA packet and permit. Utility locate at 811.",
            "Day 1: saw-cut and remove the old concrete or asphalt, haul off, excavate to depth, proof-roll.",
            "Day 2: base in two lifts, compacted and checked; edge restraint set; bedding sand screeded.",
            "Days 3–4: field laid from the garage down, borders and bands cut on a wet saw, apron seam detailed.",
            "Day 4 or 5: polymeric sand swept and vibrated, surface cleaned, edges dressed with sod or gravel.",
            "Day 60–90: first sealing once efflorescence has come and gone.",
        ]) + f"<p>We lay pavers in the rainy season without much trouble, but polymeric sand has to go in dry and set 24 hours before rain, so that step waits for a clear morning; the {tool('pour-calendar')} helps us pick the day.</p>", cls="alt")
    body += sec(f"Paver driveway costs in Kissimmee ({COST_INDEX_RELEASE['label']})",
        cost_rows(["paver-driveway-concrete", "paver-driveway-premium", "concrete-removal", "paver-sealing", "paver-repair"])
        + "<p>Worked example: a 480-square-foot two-car driveway in a standard 80 mm paver runs roughly $6,700 to $10,600 installed; add $960 to $1,920 to remove the old concrete; add 10 to 15 percent for a contrasting border and two cross bands. A premium large-format line lands at $9,600 to $16,300 before removal. Sealing later costs about $850 to $1,550. The <a href=\"/pricing/pavers/\">paver cost guide</a> has more examples.</p>")
    body += sec("Pavers or concrete?", f"<p>Pavers cost 50 to 70 percent more than a broom-finish slab up front, can be lifted and relaid after a utility cut or settling, come in the palettes most Osceola and Polk HOAs already approved, and let you widen later with matching units. Concrete is cheaper, simpler and easier to keep clean. Side by side: {compare('concrete-vs-pavers')}; decision tool: {tool('concrete-vs-pavers')}.</p>", cls="alt")
    faqs = [
        faq("How much does a paver driveway cost in Kissimmee?", f"About {cost_range('paver-driveway-concrete')} installed for standard 80 mm concrete pavers on a 6-inch base in the {COST_INDEX_RELEASE['label']} Cost Index; a 480-square-foot two-car driveway is roughly $6,700 to $10,600 before removal of the old slab."),
        faq("Do pavers need a permit in Osceola County?", "A paver driveway is a driveway: unincorporated Osceola requires the county driveway permit under §22-50.6, Kissimmee uses its Engineering application, and St. Cloud refers driveway pavers to Public Works. Polk County has a release form for pavers in the right-of-way."),
        faq("Why do paver driveways sink at the garage?", "Base. Either it was too thin, placed on wet sand, or a downspout keeps washing fine sand out from under the edge. Rebuilding the base under the sunken area and relaying the same pavers fixes it; see paver repair."),
        faq("Can you widen my existing paver driveway?", "Yes, to the county's 24-foot limit or the HOA's rule, whichever is tighter. If your line is discontinued we source the closest match or use a contrasting band as the transition."),
        faq("How long does installation take?", "Three to five working days for a two-car driveway including removal of the old surface. Sealing waits 60 to 90 days."),
        faq("Is polymeric sand really necessary?", "On a driveway, yes. Regular sand washes out in the first summer, ants tunnel through it and weeds follow. Polymeric sand installed dry and vibrated in locks the field for years."),
        faq("Which brands do you install?", "Belgard, Tremron and Oldcastle Coastal lines for concrete pavers, plus clay brick and permeable systems. We match your HOA's approved palette first."),
    ]
    return page(k, "Paver Driveways in Kissimmee, FL – Cost, Base Depth, HOA Rules", "Paver driveways in Kissimmee and Osceola County: 6-inch limerock base, 80 mm pavers, polymeric sand, concrete apron at the street, county and HOA rules (APV, Solivita, Solterra), cost per sq ft.", "Paver driveways in Kissimmee, FL", body, faqs, ["icpi", "osceola-22-50-6", "stcloud-permits", "polk-paver-release", "apv", "solivita", "solterra", "belgard", "tremron"])


# ---------------------------------------------------------------------------
def patios():
    k = "paver-patios"
    body = sec("What a paver patio costs in Kissimmee and what to decide first",
        cap(f"A paver patio runs {cost_range('paver-patio')} installed in the {COST_INDEX_RELEASE['label']} Cost Index on 60 mm concrete pavers over a 4- to 5-inch compacted base. A 12-by-12 patio lands around $2,000 to $3,000; a 16-by-20 lanai extension around $4,200 to $6,700. Two to three days on site. Travertine, marble and porcelain cost more and are covered on their own pages."),
        eyebrow="Quick answer")
    body += sec("The patios we build most",
        f"""<p>Lanai extensions that continue the screened floor out into the yard, usually 10 to 16 feet deep; fire-pit patios, round or square, with a seat wall on one side; grill and dining patios off the kitchen door; side-yard patios on the narrow lots in Storey Lake and Tapestry where the only outdoor space is beside the house; and pool-side lounge areas that tie into a paver pool deck. Add-ons that turn a patio into an outdoor room: a seat wall, a fire pit, a pergola footing, low-voltage lights in the border, and a turf strip between the patio and the fence ({svc('paver-retaining-walls-outdoor-living')}, {svc('paver-outdoor-lighting')}, {svc('paver-artificial-turf')}).</p>
<p>Patterns and units: 60 mm concrete pavers in running bond, herringbone or a three-piece ashlar; large-format 12-by-24 and 24-by-24 slabs for a modern look; tumbled units for an old-world look; clay brick borders. The square concrete-paver patio with gravel joints in our gallery is a low-cost modern option that drains straight through.</p>""")
    body += sec("Base, slope and drainage for a patio on this ground",
        cap("Four to five inches of compacted limerock on proof-rolled subgrade, 1 inch of bedding sand, 60 mm pavers, edge restraint and polymeric sand, with the surface sloped ⅛ inch per foot away from the house. On the low, flat lots typical of Kissimmee and St. Cloud, a patio that pitches toward the lanai floods it in the first storm; a slot drain at the outer edge or a swale beyond the patio gives the water somewhere to go.")
        + f"<p>Where a patio meets an existing lanai slab we set the first paver course at the slab elevation with a sailor course as the transition, and where it meets sod we finish the edge restraint below grade so the mower rides over it. Fire pits get a non-combustible base and a 3-foot clear ring. On rural St. Cloud and Harmony lots we locate the septic drainfield before laying out: no patio over it ({guide('septic-drainfield-concrete-driveway')}).</p>", cls="alt")
    body += sec("Permits and HOA for patios",
        cap("St. Cloud lists patios among the projects that need a building permit. In Kissimmee and unincorporated Osceola, a detached paver patio outside the setbacks is generally treated as flatwork without a building permit; a patio inside a setback, attached to the house or under a roof should be confirmed with the office. HOAs review patios everywhere: APV Poinciana requires prior written DCB approval for any patio or paved area; Solterra sets a 15-foot rear setback (5 feet to a pool deck or screen patio).")
        + f"<p>We confirm the permit position for your address before quoting and prepare the ARC packet: site plan or survey markup, product and color sample, pattern, drainage note. Pages: {juris('city-of-st-cloud')}, {juris('osceola-county')}, {juris('city-of-kissimmee')}, {hoa('poinciana-apv')}, {hoa('solterra')}, {tool('hoa-packet-checklist')}.</p>")
    body += sec("Process", steps([
        "Layout painted on the lawn; you walk it and we adjust before anything is dug.",
        "Excavate 7 to 8 inches, proof-roll, base in lifts, compact.",
        "Edge restraint, bedding sand screeded to slope.",
        "Field laid, borders and curves cut on a wet saw.",
        "Polymeric sand vibrated in on a dry morning, surface cleaned.",
        "Seal after 60 to 90 days; furniture can go on the day we finish.",
    ]), cls="alt")
    body += sec(f"Paver patio costs ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-patio", "travertine-pool-deck", "concrete-patio", "stamped-concrete", "paver-sealing"]) + "<p>Curves and circles add 10 to 20 percent in cutting and waste; a seat wall adds $75 to $130 per linear foot; a fire pit kit installed $900 to $2,200. Combining the patio with a walkway or a pool-deck overlay in one mobilization lowers the per-foot price.</p>")
    body += sec("Pavers, stamped concrete or plain concrete?", f"<p>Plain concrete is cheapest; stamped concrete gives a stone look for a third more; pavers cost the most, can be lifted for repairs, and are what resort-corridor HOAs usually have on file. Comparisons: {compare('stamped-vs-pavers')} and {compare('concrete-vs-pavers')}.</p>", cls="alt")
    faqs = [
        faq("How much is a 12x12 paver patio?", f"Roughly $2,000 to $3,000 installed in the {COST_INDEX_RELEASE['label']} index on standard 60 mm concrete pavers, at the top of the {cost_range('paver-patio')} range because small jobs carry the same mobilization."),
        faq("Do I need a permit for a paver patio?", "In St. Cloud, yes. In Kissimmee and unincorporated Osceola a detached patio outside setbacks usually does not, but we confirm for your address. HOA approval is required in every planned community."),
        faq("Can the patio drain toward the yard if the yard is flat?", "It has to drain somewhere. We pitch away from the house and, where the yard cannot take it, add a slot drain tied to a downspout line or a dry well."),
        faq("How soon can I use it?", "The day we finish. Sealing waits 60 to 90 days for efflorescence to clear."),
        faq("Can you add a fire pit or seat wall later?", "Yes, on the same base. Planning the footprint now saves cutting pavers later."),
        faq("What about weeds and ants?", "Polymeric sand installed dry and vibrated in, then sealing, keeps joints closed. Regular sand invites both."),
    ]
    return page(k, "Paver Patios in Kissimmee, FL – Cost, Base, Permits", "Paver patios in Kissimmee: lanai extensions, fire-pit and dining patios on a 4–5 in compacted base, slope and drainage on flat lots, permit rules for St. Cloud and Osceola, HOA setbacks, 12x12 cost.", "Paver patios in Kissimmee, FL", body, faqs, ["icpi", "stcloud-permits", "apv", "solterra"])


# ---------------------------------------------------------------------------
def pool_decks():
    k = "paver-pool-decks"
    body = sec("Overlay or rebuild a Kissimmee pool deck, and what each costs",
        cap(f"A paver overlay on a sound existing pool deck, using 1-inch remodel pavers and new bullnose coping, runs {cost_range('paver-pool-deck')} installed in the {COST_INDEX_RELEASE['label']} Cost Index; a full rebuild on a new base runs at patio rates plus coping. A 600-square-foot deck is $9,000 to $14,400 as an overlay. Travertine and marble decks run {cost_range('travertine-pool-deck')}. Four to seven days, pool stays full."),
        eyebrow="Quick answer")
    body += sec("Two ways to get a paver pool deck",
        table(["Approach", "When it fits", "What we do", "Watch out for"], [
            ("Overlay (remodel pavers)", "Existing concrete deck is sound: no heaving, no hollows, cracks hairline only", "Clean and level the slab, set 1-in pavers in a mortar or sand bed, replace coping with bullnose, add drain channel at the screen line", "Adds about 1 in at door thresholds; coping height vs. water line"),
            ("Full rebuild", "Deck heaved by roots or backfill, hollow areas, or you want to change the shape", "Remove the deck, rebuild base to 4–5 in, sand-set 60 mm pavers or thin-set travertine on a new slab, new coping", "More cost; pool contractor coordinates the bond beam if coping is structural"),
            ("New pool", "Pool under construction", "Coordinate with the pool builder after the shell and bond beam are done", "Backfill must be compacted or the deck settles within two summers"),
        ]))
    body += sec("Coping, drainage and the lanai",
        f"""<p>Coping is the piece that makes or breaks a paver deck. We use bullnose or square-edge coping in the same material as the field (paver, travertine or marble), set in mortar on the bond beam with an expansion joint between coping and deck so the deck can move without cracking the pool. Inside a screen enclosure the deck drains to a linear channel along the screen line, not to the pool and not to the screen footer; you can see the drain detail in our marble lanai photos. Outside the cage, the deck falls ⅛ to ¼ inch per foot away from the pool to a drain or the yard.</p>
<p>The screen enclosure itself is a permitted structure with footers; if the cage is being replaced or extended, that contractor's footers go in first and the deck is built around them.</p>""", cls="alt")
    body += sec("Which pool deck surface stays coolest?",
        cap("Published installer and manufacturer measurements put light travertine and marble around 105 to 120 °F at midday in Florida sun, light-colored concrete pavers 10 to 20 degrees warmer, and dark concrete pavers or dark porcelain 130 to 145 °F. Color matters more than material within the concrete paver family. We cite those figures rather than our own because we have not yet measured a deck here; that measurement is planned for July.")
        + f"<p>The comparison with sources, and our measurement plan, is on {guide('surface-temperature-pool-decks')}; the material trade-offs are in {compare('travertine-vs-concrete-pavers')} and {compare('cool-deck-vs-pavers')}. Slip resistance: tumbled surfaces and honed (not polished) stone grip wet feet; sealers on a pool deck get an anti-slip additive.</p>")
    body += sec("Permits and HOA for pool decks",
        cap("A deck built with a new pool is part of the pool permit. Replacing or overlaying an existing deck is flatwork: St. Cloud lists decks as permit-required; Kissimmee and unincorporated Osceola treat a deck outside setbacks as flatwork but a deck tied to the bond beam or the screen footer should be confirmed. Resort-community HOAs (Reunion, ChampionsGate, Windsor Hills, Solterra, Storey Lake) review visible deck changes and vacation-rental owners schedule around guests.")
        + f"<p>Pages: {juris('city-of-st-cloud')}, {juris('osceola-county')}, {hoa('solterra')}, {guide('vacation-rental-owner-hardscape-guide')}. City pages for the resort corridor: {cs('four-corners', 'paver-pool-decks')}, {cs('champions-gate', 'paver-pool-decks')}, {cs('reunion', 'paver-pool-decks')}.</p>", cls="alt")
    body += sec(f"Pool deck costs ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-pool-deck", "travertine-pool-deck", "paver-patio", "concrete-resurfacing", "concrete-removal"]) + "<p>Coping runs $28 to $55 per linear foot installed depending on material; a drain channel $18 to $30 per linear foot; removing an old deck around a pool costs more per foot than a driveway because it is hand work near the shell.</p>")
    faqs = [
        faq("Can pavers go over my existing pool deck?", "If the deck is sound and the extra inch works at the doors and the coping, yes. We tap-test for hollows and check thresholds before quoting."),
        faq("How long is the pool out of use?", "It isn't; the pool stays full. Expect four to seven days of work around it, and keep swimmers out while coping mortar cures (48 hours)."),
        faq("Sand-set or mortar-set?", "Remodel pavers over a concrete deck are usually set in a thin mortar bed or on a sand bed with a mortar perimeter; travertine over a new slab is thin-set. Sand-set on a rebuilt base is standard for full rebuilds. The proposal states which."),
        faq("What is the coolest pool deck material?", "Light travertine and marble in published measurements, then light concrete pavers. Dark pavers and dark porcelain are hottest. We cite sources until we have measured decks here."),
        faq("Will pool chemicals damage pavers?", "Chlorinated splash is fine on sealed concrete pavers and on travertine with a penetrating sealer. Salt pools are harder on unsealed travertine; seal it and rinse the deck monthly."),
        faq("Do I need a permit to replace the deck?", "In St. Cloud, yes. Elsewhere it depends on the tie to the pool structure or screen footer; we confirm for your address."),
    ]
    return page(k, "Paver Pool Decks in Kissimmee, FL – Overlay, Rebuild, Cost", "Paver pool decks in Kissimmee: 1-inch remodel pavers over a sound deck or a full rebuild, bullnose coping, lanai drain channel, which surface stays coolest, permits and resort HOA rules, cost for 600 sq ft.", "Paver pool decks in Kissimmee, FL", body, faqs, ["stcloud-permits", "solterra", "icpi"])


# ---------------------------------------------------------------------------
def travertine():
    k = "paver-travertine"
    body = sec("What travertine costs in Kissimmee and how it is cared for",
        cap(f"A travertine pool deck runs {cost_range('travertine-pool-deck')} installed in the {COST_INDEX_RELEASE['label']} Cost Index, using 1¼-inch tumbled pavers sand-set on a compacted base or thin-set on a new slab, with matching bullnose coping. Travertine is a natural limestone from Turkey, Mexico and Peru; it stays cooler barefoot than concrete pavers and needs a breathable penetrating sealer, never a film-forming one."),
        eyebrow="Quick answer")
    body += sec("Where travertine is the right call",
        f"""<p>Pool decks first: it is the surface most Reunion, Bellalago, Celebration and lakefront St. Cloud owners ask for by name, because it is cooler underfoot in July and reads as stone rather than concrete. Lanai floors, patios and walkways next. Driveways only in the thick 1¼-inch paver format, in a running bond or French pattern, on a full 6-inch base, and only where the HOA allows it; the softer grades will not take tires. The tumbled travertine-look deck under the oaks in our gallery shows the finish most people picture.</p>
<p>Grades and finishes: premium select (few holes, even color), standard (more fill, more variation), tumbled (rounded edges, matte, grippy), honed (smooth, matte), chiseled edge. Colors run ivory, walnut, noce, silver and gold. Sizes: 6-by-12, 12-by-12, 12-by-24, 16-by-24, and the French (Versailles) pattern set. Thickness: 1¼ inch (3 cm) for sand-set pavers, ½ inch tiles for thin-set over concrete.</p>""")
    body += sec("How travertine is installed here",
        cap("Sand-set on a compacted 4- to 5-inch base with 1 inch of bedding sand for patios and pool decks built new; thin-set with a polymer-modified mortar over an existing sound concrete deck or a new slab where the surface must be rigid; mortar-set bullnose coping on the bond beam with an expansion joint to the field. Joints are sanded with a fine polymeric sand or, on thin-set work, grouted. Sealed with a penetrating sealer after 30 days.")
        + f"<p>Two mistakes we fix on other people's travertine: a film-forming acrylic sealer that trapped moisture from the bedding sand and turned white, and travertine sand-set over uncompacted pool backfill that settled in the first summer. The base rules are the same as for pavers ({svc('paver-driveways', 'see the base section')}); the sealer chemistry is in {compare('sealer-types')}.</p>", cls="alt")
    body += sec("Travertine versus concrete pavers, marble and porcelain",
        table(["", "Travertine", "Concrete pavers", "Marble", "Porcelain"], [
            ("Cost installed (pool deck)", cost_range('travertine-pool-deck'), cost_range('paver-pool-deck'), "higher than travertine", "similar to travertine"),
            ("Surface heat (published)", "105–120 °F", "115–145 °F by color", "coolest", "hot in dark colors"),
            ("Wet grip", "tumbled: good; honed: good", "good", "honed: fair", "textured: good"),
            ("Stains", "porous; seal", "porous; seal", "porous; seal", "non-porous"),
            ("Pool chemicals / salt", "seal; rinse", "fine", "seal; rinse", "unaffected"),
            ("Repair", "lift and reset", "lift and reset", "lift and reset", "lift and reset on pedestals; cut units otherwise"),
        ]) + f"<p>Full comparisons: {compare('travertine-vs-concrete-pavers')}; marble and porcelain: {svc('paver-marble-porcelain')}.</p>")
    body += sec("Care", f"<p>Seal with a penetrating, breathable sealer 30 days after installation and every three to four years after; rinse a salt-pool deck monthly; clean with pH-neutral stone cleaner, never acid or a rust remover meant for concrete (it etches the stone). Well-water sprinkler overspray leaves orange iron stains on light travertine within weeks; the fix is head adjustment or an iron filter, not repeated cleaning ({guide('rust-stains-irrigation-well-water')}).</p>", cls="alt")
    body += sec("Permits and HOA", f"<p>Same as any pool deck or patio: St. Cloud requires a permit for decks and patios; Kissimmee and unincorporated Osceola treat detached work outside setbacks as flatwork; HOAs review color and pattern. Reunion has three management companies depending on the neighborhood; the {cs('reunion', 'paver-travertine')} page lists them. Packet: {tool('hoa-packet-checklist')}.</p>")
    faqs = [
        faq("Does travertine get hot in the sun?", "Warm, not scorching. Published measurements put light travertine at 105 to 120 °F on a 95-degree afternoon versus 130 to 145 for dark concrete pavers. We plan to measure decks here in July and will publish the method."),
        faq("Is travertine slippery around a pool?", "Tumbled and honed travertine grip well when wet. Polished travertine does not and is not used outdoors."),
        faq("How much is a 600 sq ft travertine pool deck?", f"About $12,000 to $21,600 installed in the {COST_INDEX_RELEASE['label']} index, plus coping and any drain work."),
        faq("Sand-set or thin-set?", "Sand-set on a new compacted base for patios and rebuilt decks; thin-set over an existing sound slab. Both are in our proposals with the reason."),
        faq("Which sealer for travertine?", "A penetrating, breathable siloxane or fluoropolymer sealer. Film-forming acrylics haze and peel on stone within a year here."),
        faq("Can I use travertine on a driveway?", "Thick 1¼-inch pavers on a full 6-inch base, in a strong pattern, and only if your HOA allows it. It is a premium driveway and it is softer than concrete pavers under tires."),
    ]
    return page(k, "Travertine Pool Decks & Patios in Kissimmee, FL – Cost, Care", "Travertine pool decks, lanais and patios in Kissimmee: grades, sizes, sand-set vs. thin-set, bullnose coping, why film sealers fail, surface heat vs. concrete pavers, cost per sq ft installed.", "Travertine pool decks, patios and driveways in Kissimmee, FL", body, faqs, ["icpi", "stcloud-permits"])


# ---------------------------------------------------------------------------
def marble_porcelain():
    k = "paver-marble-porcelain"
    body = sec("Marble and large-format porcelain pavers in Kissimmee",
        cap("Marble pavers (1¼ inch, tumbled or honed) give the lightest, coolest pool deck of any material and cost more than travertine. Large-format porcelain pavers (2 cm, 24-by-24 and 24-by-48) are stain-proof, uniform and modern, and must be set on a rigid base, a mortar bed or pedestals rather than sand. Both are quoted per job after a sample; expect pricing above the travertine range."),
        eyebrow="Quick answer")
    body += sec("Marble",
        f"""<p>Marble pool decks and lanai floors are the finish behind the polished white deck and the bullnose coping in our gallery. Tumbled marble in ivory or white stays visibly cooler than travertine in the same sun and has fewer voids to fill. It is softer, so it goes on pool decks, lanais and patios, not driveways, and it needs the same penetrating sealer as travertine and a rinse routine on salt pools. Sizes and patterns match travertine (French pattern, 12-by-24, 16-by-24). We set it sand-set on a compacted base or thin-set over a sound slab, with mortar-set bullnose coping and an expansion joint at the bond beam.</p>""")
    body += sec("Large-format porcelain",
        f"""<p>Two-centimeter porcelain pavers are the modern answer for lanais, entries, steps and rooftop-style terraces: 24-by-24 and 24-by-48 units in stone, concrete and wood looks, non-porous, colorfast, and unaffected by pool chemicals, rust water or oil. The porcelain treads on the entry steps in our gallery are the typical use. The rule that matters: porcelain does not interlock and does not flex, so it cannot be sand-set on a driveway or a large sand-set field. It goes on a mortar bed over a concrete slab (lanais, pool decks over existing concrete, steps), on adjustable pedestals over a slab or a membrane (terraces, decks that need to drain below), or on a stabilized aggregate base with a rigid edge for small patios. Dark porcelain gets hot; light stone-look porcelain is comfortable.</p>""", cls="alt")
    body += sec("Which to choose",
        table(["", "Marble", "Large-format porcelain", "Travertine"], [
            ("Best use", "Pool decks, lanais", "Lanais, entries, steps, modern patios", "Pool decks, patios, walks"),
            ("Heat", "Coolest", "Light colors fine; dark hot", "Cool"),
            ("Stains and chemicals", "Seal; rinse salt", "Immune", "Seal; rinse salt"),
            ("Install", "Sand-set or thin-set", "Mortar bed, pedestals or rigid base only", "Sand-set or thin-set"),
            ("Repair", "Lift and reset", "Replace units", "Lift and reset"),
            ("Cost", "Highest", "Similar to travertine or above", cost_range('travertine-pool-deck')),
        ]) + f"<p>Comparisons: {compare('travertine-vs-concrete-pavers')}; architectural concrete pairs with porcelain on modern homes: {svc('concrete-architectural')}.</p>")
    body += sec("Permits and HOA", f"<p>Same permit logic as a pool deck, patio or walkway; HOAs review color and pattern, and Celebration's ARC in particular reviews materials visible from the street. Pages: {hoa('celebration')}, {juris('city-of-st-cloud')}, {tool('hoa-packet-checklist')}.</p>", cls="alt")
    faqs = [
        faq("Is marble too soft for a pool deck?", "No; tumbled and honed marble pavers are standard on Florida pool decks. It is too soft for driveways."),
        faq("Can porcelain pavers go on a driveway?", "Not in 2 cm sand-set format. Thick driveway-rated porcelain exists but needs a rigid setting bed and is rarely worth it here; concrete pavers or travertine are the driveway options."),
        faq("Does porcelain need sealing?", "No. It is non-porous; grout joints on mortar-set work may be sealed."),
        faq("How is porcelain repaired?", "Damaged units are replaced. Keep a box of spares from the original lot; dye lots vary."),
        faq("What does a marble pool deck cost?", "Above the travertine range; quoted per job after a sample because grade and size drive the material price."),
    ]
    return page(k, "Marble & Large-Format Porcelain Pavers in Kissimmee, FL", "Marble pool decks and 2 cm large-format porcelain pavers in Kissimmee: coolest surfaces, stain-proof options, why porcelain needs a rigid or pedestal base, comparisons with travertine, HOA notes.", "Marble and large-format porcelain pavers in Kissimmee, FL", body, faqs, ["celebration", "stcloud-permits"])


# ---------------------------------------------------------------------------
def walkways():
    k = "paver-walkways-steps"
    body = sec("Paver walkways, entry steps and stoops in Kissimmee",
        cap(f"A paver walkway runs {cost_range('paver-walkway')} installed in the {COST_INDEX_RELEASE['label']} Cost Index; a 4-foot-wide, 40-foot front walk is roughly $2,200 to $3,800. Entry steps are built as concrete or block risers faced and capped with pavers, travertine or porcelain and quoted per step. Base: 4 inches compacted, 1 inch bedding sand, 60 mm pavers, edge restraint on both sides."),
        eyebrow="Quick answer")
    body += sec("What we build",
        f"""<p>Front walks from the driveway to the door, replacing the builder's narrow concrete ribbon with a 4-foot paver walk and a border; side-yard paths to the gate, the pool equipment and the AC pad, often 3 feet wide with a turf or gravel strip; garden paths in tumbled pavers; entry stoops and steps rebuilt in block and capped with bullnose treads; and the steps and landing between a raised lanai and a lower patio. Lighting in the border and the risers is the upgrade most people add ({svc('paver-outdoor-lighting')}); the curved lit steps in our gallery are a concept rendering of that idea and are labelled as such.</p>""")
    body += sec("Base and details that make a walk last",
        f"""<p>Walkways fail at the edges because they are narrow: two edges, one third of the area of a patio. We set edge restraint on both sides on the base, not on the sand, and finish it below grade on the lawn side so the mower rides over it. Base is 4 inches of compacted limerock on proof-rolled subgrade, bedding sand 1 inch, pavers 60 mm, polymeric sand in the joints. The walk is crowned or cross-sloped ⅛ to ¼ inch per foot so rain runs off rather than along it. Steps get a block or poured riser on a footing, a paver or stone tread with a ½- to 1-inch nosing, and a landing at least 3 feet deep at the door; riser height is kept within ¼ inch step to step because that is what people trip on. Around live oaks we curve the walk or install a root barrier ({guide('tree-roots-driveways-central-florida')}).</p>""", cls="alt")
    body += sec("Permits and HOA",
        cap("A private walkway on your lot needs no building permit in Kissimmee or unincorporated Osceola; St. Cloud refers sidewalk pavers to Public Works. Steps with more than three risers or a landing tied to the structure may be reviewed with the entry. In the public right-of-way, paver sidewalk is rarely allowed; concrete follows the jurisdiction's detail. APV Poinciana limits any walkway adjacent to the house to 2 feet wide unless the DCB approves otherwise, and Solterra prohibits additional sidewalks without approval.")
        + f"<p>Pages: {hoa('poinciana-apv')}, {hoa('solterra')}, {juris('city-of-st-cloud')}, {juris('city-of-kissimmee')}, {tool('hoa-packet-checklist')}. Concrete walks: {svc('concrete-sidewalks-walkways')}.</p>")
    body += sec(f"Walkway and step costs ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-walkway", "concrete-sidewalk", "paver-sealing", "paver-repair"]) + "<p>Steps are quoted per riser: a typical block riser faced and capped with pavers runs $250 to $450 per step plus the landing; travertine or porcelain treads add material. Curves add cutting. A walk built with a patio or driveway in the same mobilization is cheaper per foot than a walk alone.</p>", cls="alt")
    faqs = [
        faq("How wide should a paver front walk be?", "Four feet for two people abreast; three feet for a side path. Check the community rule first: APV Poinciana caps walks adjacent to the house at 2 feet without approval."),
        faq("How much is a 40-foot paver walkway?", f"About $2,200 to $3,800 at 4 feet wide in the {COST_INDEX_RELEASE['label']} index; borders and curves push toward the top."),
        faq("Can you rebuild my front steps in pavers?", "Yes: block risers on a footing, paver, travertine or porcelain treads with a nosing, and a landing at the door. Riser heights are equalized, which is usually the reason the old steps felt wrong."),
        faq("Do walkway pavers need a permit?", "Not on your lot in Kissimmee or unincorporated Osceola; St. Cloud refers them to Public Works. In the right-of-way, ask first."),
        faq("Will the walk sink at the edges?", "Not with edge restraint set on the base and a 4-inch compacted base under the whole width. That is the difference between a $14 and a $24 walk."),
    ]
    return page(k, "Paver Walkways & Entry Steps in Kissimmee, FL – Cost & Details", "Paver walkways, side paths, entry steps and stoops in Kissimmee: 4-in base, edge restraint both sides, riser heights within ¼ in, HOA width rules (APV 2 ft), cost per sq ft and per step.", "Paver walkways, paths and entry steps in Kissimmee, FL", body, faqs, ["apv", "solterra", "stcloud-permits"])


# ---------------------------------------------------------------------------
def sealing():
    k = "paver-sealing"
    body = sec("What sealing costs in Kissimmee and how often it is due",
        cap(f"Cleaning, re-sanding with polymeric sand and sealing runs {cost_range('paver-sealing')} in the {COST_INDEX_RELEASE['label']} Cost Index; a 480-square-foot driveway is about $850 to $1,550, a 600-square-foot pool deck $1,050 to $1,950. Stripping a failed old sealer adds $0.75 to $1.50 per square foot. Seal new concrete pavers 60 to 90 days after installation, then every three to four years on a driveway and every two to three on a pool deck."),
        eyebrow="Quick answer")
    body += sec("Should you seal pavers in Florida?",
        cap("Yes, for concrete pavers: sealing slows fading, makes oil and rust stains removable, locks the joint sand, and keeps mold and algae from taking hold in 50-plus inches of annual rain. Travertine and marble get a penetrating sealer only. Porcelain needs none. Sealing does not stop settling, does not prevent rust from well-water irrigation (it only makes it easier to remove), and does not replace polymeric sand.")
        + f"<p>Two kinds of sealer, two different results. Film-forming acrylics (solvent- or water-based) sit on the surface, give a wet or satin look, and need re-coating every two to three years; applied over damp pavers they haze white, which is the most common sealer failure we are called to fix. Penetrating sealers (silane/siloxane, fluoropolymer) soak in, leave the look natural, breathe, and last three to five years. Joint-stabilizing sealers do both jobs on the sand. The chemistry, with brand types, is in {compare('sealer-types')}.</p>")
    body += sec("Our cleaning and sealing process",
        steps([
            "Inspect: sealer type on the surface (water beads or not), efflorescence, rust, oil, mold, joint depth, any sunken areas to fix first.",
            "Strip if an old film sealer has failed; otherwise skip.",
            "Clean: surface cleaner on a pressure washer at 2,500–3,000 psi with a wide tip to avoid etching, efflorescence cleaner on white haze, rust remover on iron stains, degreaser on oil ({guide('rust-stains-irrigation-well-water', 'stain identification guide')}).",
            "Dry: 24 to 48 hours, longer in the rainy season; sealing over moisture is how pavers turn white.",
            "Re-sand: sweep polymeric sand into the joints to just below the chamfer, vibrate with a plate compactor on a pad, blow off every grain from the surface.",
            "Activate the sand with a fine mist, let it set 24 hours with no rain in the forecast.",
            "Seal: two thin coats, back-rolled, with an anti-slip additive on pool decks and steps. Foot traffic in 4 hours, cars in 48.",
        ]) + f"<p>Timing: sand and sealer both need a dry day and a dry night, so in June through September we book the job for a morning with a clear radar and we watch the {tool('pour-calendar')} the way we do for pours.</p>", cls="alt")
    body += sec("What goes wrong with pavers here, and what sealing does about it",
        table(["Problem", "Cause", "Sealing helps?", "Real fix"], [
            ("White haze on new pavers", "Efflorescence: salts migrating out during the first rainy season", "No; wait it out, then clean", "Efflorescence cleaner before sealing"),
            ("White cloudy sealer", "Film sealer applied over moisture", "No", "Strip and re-seal on a dry deck"),
            ("Orange streaks", "Iron in well-water irrigation", "Makes removal easier", "Adjust heads or add an iron filter"),
            ("Black or green film", "Mold and algae in shade", "Slows it", "Clean; trim shade; seal"),
            ("Weeds and ants in joints", "Loose or missing joint sand", "Only with polymeric sand under it", "Re-sand with polymeric, then seal"),
            ("Fading color", "UV on unsealed concrete pavers", "Yes", "Seal every 3–4 years"),
            ("Sunken areas", "Base washout", "No", "Lift and relay (paver repair)"),
        ]))
    body += sec("Permits and HOA", f"<p>Sealing is maintenance; no permit anywhere. HOAs may regulate the finish: Solterra allows concrete surfaces to be sealed only in a clear matte finish and requires a request, so a wet-look sealer there needs approval first ({hoa('solterra')}). Vacation rentals in Four Corners, ChampionsGate and Reunion schedule sealing between guests: {cs('four-corners', 'paver-sealing')}, {cs('champions-gate', 'paver-sealing')}, {cs('reunion', 'paver-sealing')}.</p>", cls="alt")
    body += sec(f"Sealing costs ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-sealing", "paver-repair", "paver-driveway-concrete"]) + "<p>Price per square foot drops on larger areas; a driveway and pool deck sealed on the same visit cost less than two visits. Stripping is the expensive step, which is why choosing the right sealer the first time matters.</p>")
    faqs = [
        faq("How often should pavers be sealed in Florida?", "Concrete pavers: 60 to 90 days after installation, then every three to four years on a driveway and two to three on a pool deck. Travertine and marble: a penetrating sealer every three to four years. Porcelain: never."),
        faq("How much does paver sealing cost?", f"About {cost_range('paver-sealing')} including cleaning and polymeric re-sanding; a two-car driveway is $850 to $1,550. Stripping an old failed sealer adds $0.75 to $1.50 per square foot."),
        faq("Why did my pavers turn white after sealing?", "Either efflorescence that was sealed in, or a film-forming sealer applied over moisture. Both need the sealer stripped and the deck re-sealed dry."),
        faq("Polymeric sand or regular sand?", "Polymeric. It hardens in the joint, resists washout, ants and weeds, and holds the field. It must go in dry and be activated with a light mist; too much water and it crusts on the surface."),
        faq("Wet look or natural?", "Wet look is a film-forming acrylic: richer color, more maintenance, slippery without additive. Natural is a penetrating sealer: no change in look, longer life. HOAs like Solterra require the matte option."),
        faq("Can you seal in the rainy season?", "Yes, on a morning with a dry forecast for 24 hours. We cancel and reschedule rather than seal ahead of a storm."),
    ]
    return page(k, "Paver Sealing, Cleaning & Re-Sanding in Kissimmee, FL – Cost", "Paver sealing in Kissimmee: clean, re-sand with polymeric sand and seal for $1.75–$3.25/sq ft, film vs. penetrating sealers, why pavers turn white, rust from well water, schedule by surface.", "Paver sealing, cleaning and re-sanding in Kissimmee, FL", body, faqs, ["solterra", "icpi"])


# ---------------------------------------------------------------------------
def repair():
    k = "paver-repair"
    body = sec("Sunken areas, failed edges, open joints and replacement pieces",
        cap(f"Lifting and relaying a sunken area of pavers runs {cost_range('paver-repair')} in the {COST_INDEX_RELEASE['label']} Cost Index with a minimum visit charge; a 60-square-foot dip at the garage is typically $600 to $1,000. The pavers come up, the base is rebuilt and compacted, the same pavers go back, and the joints get polymeric sand. Edge restraint replacement is priced per linear foot; matching pieces for discontinued lines are sourced before we quote."),
        eyebrow="Quick answer")
    body += sec("The five paver problems we fix",
        table(["Problem", "Cause here", "Repair"], [
            ("Dip or sunken area at the garage, along the edge or under a downspout", "Fine sand washed out from under a thin base; downspout or sprinkler saturating one spot", "Fix the water first; lift the field, rebuild and compact base, relay, re-sand"),
            ("Outside course rolling or spreading", "No edge restraint, or restraint set on the sand instead of the base", "Install spiked aluminum or concrete edge restraint on the base; reset the course"),
            ("Ant mounds, weeds, sand loss", "Regular sand or thin polymeric", "Clean out, re-sand with polymeric, seal"),
            ("Cracked, chipped or stained units", "Vehicle damage, rust, oil, a dropped grill", "Replace units from spares or a sourced match; treat the stain chemistry"),
            ("Utility cut or new plumbing line through the drive", "Trench backfilled loose", "Rebuild base in lifts over the trench; relay; no visible patch"),
        ]))
    body += sec("How a lift-and-relay works",
        steps([
            "Mark the dip with a string line; find and fix the cause (extend the downspout, cap or move the sprinkler, repair the leak).",
            "Pull the pavers with a paver extractor, stacking them in order; the pattern goes back the way it came.",
            "Remove bedding sand, excavate soft base, place new limerock in lifts, compact, screed new sand.",
            "Relay, cut any broken units from spares, set edge restraint if missing.",
            "Sweep polymeric sand, compact, activate, seal the area or the whole field if the rest is due.",
        ]) + f"<p>Because pavers are units, the repair disappears in a week as the joint sand weathers; that repairability is the main reason pavers beat concrete on the resurface-or-replace question ({compare('resurface-vs-replace')}). Full base failures across most of a driveway are a rebuild, not a repair, and we say so.</p>", cls="alt")
    body += sec("Matching discontinued pavers", f"<p>Builders in Storey Lake, Tapestry, Bellalago, Solterra and the Reunion phases used lines that Belgard, Tremron and Oldcastle have since renamed or dropped. We identify the unit by size, chamfer and blend, check the manufacturers' current equivalents, and if nothing matches we borrow units from a hidden area (behind the AC, under the trash-can pad) and put the odd units there. Keeping a pallet of spares from any new installation is the cheap insurance.</p>")
    body += sec("Permits and HOA", f"<p>Repairs in the same footprint need no permit. HOAs usually want a note if the repair area will look different for a few weeks; resort communities also want work scheduled around guests. {guide('vacation-rental-owner-hardscape-guide')} covers scheduling; {tool('hoa-packet-checklist')} covers what to send. Repair on the ridge (Davenport, Haines City) often involves base that was never wetted before compaction: {guide('paver-base-flatwoods-vs-ridge')}.</p>", cls="alt")
    body += sec(f"Repair costs ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-repair", "paver-sealing", "paver-driveway-concrete"]) + "<p>Edge restraint runs $9 to $16 per linear foot installed; replacement units $6 to $15 each for common lines; a utility-trench relay across a two-car driveway $700 to $1,400. Small repairs carry a minimum charge; combining them with sealing lowers the total.</p>")
    faqs = [
        faq("Why are my pavers sinking near the garage?", "Water from the roof or a sprinkler is washing the fine sand out from under a thin base. Fix the water, then lift, rebuild the base and relay."),
        faq("Can sunken pavers be reused?", "Yes, almost always. They come up, the base is rebuilt, and the same units go back in the same pattern."),
        faq("How much does a paver repair cost?", f"{cost_range('paver-repair')} for a lift-and-relay with a minimum visit charge; a typical 60-square-foot dip is $600 to $1,000."),
        faq("What if my pavers are discontinued?", "We match by size and blend from current lines, or borrow units from a hidden area and put the substitutes there."),
        faq("Do ants damage pavers?", "They tunnel through loose joint sand and undermine the bedding. Polymeric sand and sealing stop them; a colony under the field means re-sanding after treatment."),
        faq("Is it worth repairing or should I redo the driveway?", "Repair if the base under the rest is sound and the dip is local. Rebuild if more than a third of the field has moved or the base was never built."),
    ]
    return page(k, "Paver Repair in Kissimmee, FL – Sunken Areas, Edges, Ants", "Paver repair in Kissimmee: lift-and-relay of sunken areas after fixing the water source, edge restraint replacement, polymeric re-sanding for ants and weeds, matching discontinued pavers, costs.", "Paver repair in Kissimmee, FL", body, faqs, ["icpi"])


# ---------------------------------------------------------------------------
def walls_outdoor_living():
    k = "paver-retaining-walls-outdoor-living"
    body = sec("Retaining walls, seat walls, fire pits and summer kitchens in Kissimmee",
        cap("Decorative segmental retaining walls up to 4 feet, seat walls, raised planters, fire pits and the paver and block structure of summer kitchens, all in Belgard, Tremron or Oldcastle wall units or stone veneer. Walls that retain more than 4 feet, support a structure or carry a surcharge need an engineer and a licensed contractor, and we refer those. Seat walls run about $75 to $130 per linear foot installed; the rest is quoted per design."),
        eyebrow="Quick answer")
    body += sec("What we build",
        f"""<p>Raised terraces on sloped lakefront lots in St. Cloud and Kissimmee, like the curved stone-faced terrace with the cedar pergola in our gallery; low retaining walls that turn a sloped side yard into a level pad; seat walls around a fire pit or along the edge of a patio (18 to 20 inches high is sitting height); raised planters against the lanai; fire pits in a kit or built from wall units with a steel ring; and the block-and-paver structure of an outdoor kitchen, with counters in concrete or stone and the gas, electrical and appliances handled by licensed trades we coordinate with. Lighting built into wall caps and pillars is the usual finishing touch ({svc('paver-outdoor-lighting')}).</p>""")
    body += sec("How a segmental wall is built on this soil",
        cap("A 6-inch compacted limerock leveling pad below grade, the first course buried, units stacked with a setback, drainage stone and a perforated drain pipe behind the wall, geogrid every second or third course on walls over 3 feet, and a cap adhered with a construction adhesive rated for exterior use. On flatwoods sand the drain matters more than the height: water trapped behind a wall in a wet June is what pushes it over.")
        + f"<p>Walls over 4 feet measured from the bottom of the footing, walls with a fence, pool or driveway above them, and terraced walls closer than twice their height to each other need engineering and a licensed contractor under Florida's building code; Polk County's FAQ lists retaining walls required for structural support among permit items and directs decorative-wall questions to a plans examiner. We build the decorative and low-wall scope and tell you when a job crosses the line.</p>", cls="alt")
    body += sec("Permits and HOA",
        f"<p>Low decorative walls and seat walls outside setbacks are generally not permitted separately in Kissimmee and unincorporated Osceola; St. Cloud reviews case by case; Polk County wants a plans examiner's opinion on decorative walls ({juris('polk-county')}). Fire features, gas lines and outdoor kitchens involve licensed trades and permits. HOAs review anything visible: Solterra's guidelines cover walls and fences (4-foot masonry walls between back-to-back lots with a 5-foot rear setback) and grills and fire pits; APV Poinciana requires DCB approval for walls ({hoa('solterra')}, {hoa('poinciana-apv')}).</p>")
    body += sec("Pricing", "<p>Seat walls $75 to $130 per linear foot; low retaining walls $60 to $110 per square foot of face including base, drain and cap; fire pit kits installed $900 to $2,200; outdoor kitchen structures from $4,500 for a straight 8-foot run before appliances and utilities; stone veneer on a block wall $28 to $45 per square foot. Quoted per design after a site visit.</p>", cls="alt")
    faqs = [
        faq("Do you build structural retaining walls?", "Walls up to 4 feet that hold back a yard, yes. Walls over 4 feet, walls supporting a driveway, pool or building, and terraced walls need an engineer and a licensed contractor; we refer those."),
        faq("How high is a seat wall?", "18 to 20 inches to the top of the cap, 12 to 14 inches deep."),
        faq("Does a fire pit need a permit?", "A wood fire pit in a kit usually does not; a gas fire feature needs a licensed gas contractor and a permit. HOAs have their own rules on both."),
        faq("Why do walls lean here?", "Water. No drain stone or pipe behind the wall, so a wet June pushes it over. Every wall we build drains."),
        faq("Can you do the whole outdoor kitchen?", "The block, paver, stone and concrete structure and counters. Gas, electrical and appliances are licensed trades we coordinate."),
    ]
    return page(k, "Retaining Walls, Seat Walls & Outdoor Living in Kissimmee, FL", "Decorative segmental retaining walls to 4 ft, seat walls, raised terraces, fire pits and summer-kitchen structures in Kissimmee: drainage behind the wall, when engineering is required, HOA rules, prices.", "Retaining walls, seat walls and outdoor living in Kissimmee, FL", body, faqs, ["polk-faq", "solterra", "apv"])


# ---------------------------------------------------------------------------
def turf():
    k = "paver-artificial-turf"
    body = sec("Artificial turf tied into pavers and concrete in Kissimmee",
        cap("Turf strips between driveway ribbons, side yards where St. Augustine will not grow in the shade, dog runs, putting greens and the green band around a paver patio. Installed on 3 to 4 inches of compacted base with a weed barrier, nailed to a treated-lumber or paver edge, infilled with silica sand or a cooling infill. Priced per square foot with the base; quoted per job."),
        eyebrow="Quick answer")
    body += sec("Where turf makes sense here",
        f"""<p>The lots in Storey Lake, Tapestry, Solterra and the newer Harmony phases leave a 4- to 6-foot side yard that never gets sun, and sod dies there every year. Turf between the driveway and the fence, or between paver ribbons on a modern drive, solves it once. Dog owners in the resort communities use it for the same reason. Putting greens go behind the pool cage on larger lots. What turf does not fix: drainage. Turf on flatwoods sand needs a base that drains, and a low spot stays a low spot under turf.</p>""")
    body += sec("Installation", steps([
        "Remove sod and 4 inches of soil; cap or relocate sprinkler heads (turf needs no water; the rest of the yard still does).",
        "Base: 3 to 4 inches of compacted limerock or decomposed granite, graded to drain, with a weed barrier.",
        "Edge: paver soldier course, concrete curb or treated lumber, so the turf has a clean nailing edge against the hardscape.",
        "Turf laid with the grain in one direction, seamed, stretched and nailed every 6 inches at the edges.",
        "Infill brushed in: silica sand for stability, a cooling infill where the area gets full sun and bare feet.",
    ]) + f"<p>Heat is real: turf in full Kissimmee sun gets hotter than pavers. Lighter turf, cooling infill and shade help; for a pool-side lounge we still recommend travertine or marble ({svc('paver-travertine')}).</p>", cls="alt")
    body += sec("HOA", f"<p>Many HOAs treat turf as a landscape change that needs approval, and some prohibit it in front yards. APV Poinciana's landscape criteria and Solterra's approved landscape palette both apply; check before ordering ({hoa('poinciana-apv')}, {hoa('solterra')}).</p>")
    faqs = [
        faq("Does turf get hot?", "Yes, hotter than pavers in full sun. Lighter fibers, cooling infill and shade help; it is not a pool-deck material."),
        faq("Will my HOA allow it?", "Many allow it in side and back yards with approval and prohibit it in front. We check the community's rule first."),
        faq("How long does it last?", "Twelve to fifteen years for a quality product with UV protection; the base outlasts the turf."),
        faq("Does it drain?", "Through the backing and the base, if the base was built to drain. Turf over a low spot still puddles."),
    ]
    return page(k, "Artificial Turf With Pavers in Kissimmee, FL – Side Yards, Strips", "Artificial turf in Kissimmee tied into paver and concrete edges: side yards that won't grow sod, driveway ribbons, dog runs and putting greens, base and drainage, heat, HOA approval.", "Artificial turf tied into hardscape in Kissimmee, FL", body, faqs, ["apv", "solterra"])


# ---------------------------------------------------------------------------
def lighting():
    k = "paver-outdoor-lighting"
    body = sec("Outdoor lighting built into pavers, steps and pillars in Kissimmee",
        cap("Low-voltage LED lighting installed as part of the hardscape: paver lights in a driveway border, riser lights in entry steps, cap lights on seat walls and pillars, path lights along a walk, and downlights under a pergola. Wire is run in conduit under the pavers before the field is laid, so the fixtures look built in. A 12-volt transformer on a photocell or timer runs it all; a licensed electrician installs the outlet if one is needed."),
        eyebrow="Quick answer")
    body += sec("Fixtures and where they go",
        table(["Fixture", "Where", "Notes"], [
            ("Paver lights (brick-sized LED)", "Driveway and walkway borders", "Sized to match a soldier course; drive-over rated"),
            ("Riser lights", "Entry steps, terrace steps", "Recessed into the riser under the tread nosing; the safest light on a step"),
            ("Cap lights", "Seat walls, pillars, columns", "Wash the wall face; the pillar light in our gallery is a surface-mount version"),
            ("Path lights", "Walks, planting beds", "Stake-mounted; easiest to add later"),
            ("Well and up lights", "Palms, oaks, house facade", "Landscape lighting; coordinated with the hardscape wiring"),
            ("Pergola and kitchen lighting", "Outdoor living", "Downlights and task lights on the same transformer"),
        ]))
    body += sec("How it is installed with the hardscape",
        f"<p>Conduit and pull strings go into the base before the bedding sand, junctions land in accessible boxes at the edge, and fixtures are set as the field is laid so nothing is cut afterward. The transformer mounts near an exterior GFCI outlet; if there is no outlet where it is needed, a licensed electrician adds one under an electrical permit. Everything downstream of the transformer is 12-volt and does not need a permit. Retrofitting lights into an existing paver drive means lifting a border course and running wire in the bedding; it is a half-day job with the {svc('paver-repair', 'lift-and-relay')} technique.</p>", cls="alt")
    body += sec("HOA", f"<p>Fixtures visible from the street are reviewed in most communities; Solterra's guidelines have a lighting section and Celebration's ARC reviews exterior fixtures. Warm white (2700–3000 K), aimed down, is what boards approve ({hoa('solterra')}, {hoa('celebration')}).</p>")
    faqs = [
        faq("Do outdoor lights need a permit?", "The 12-volt side does not. A new 120-volt outlet for the transformer does, through a licensed electrician."),
        faq("Can lights be added to my existing paver driveway?", "Yes, by lifting the border course, running wire in the bedding sand and setting paver lights in place of border units."),
        faq("What does hardscape lighting cost?", "Fixtures $45 to $140 each installed plus a transformer ($250 to $500) and wiring; a typical driveway border with 12 paver lights runs $1,400 to $2,600 when done with the paver job."),
        faq("What color temperature?", "Warm white, 2700 to 3000 K, aimed down. HOAs approve it and it does not glare into neighbors' windows."),
    ]
    return page(k, "Outdoor Lighting in Pavers, Steps & Pillars – Kissimmee, FL", "Low-voltage lighting built into paver borders, entry steps, seat walls and pillars in Kissimmee: fixtures, conduit under the pavers, transformer and outlet rules, retrofits, HOA color temperature.", "Outdoor lighting built into pavers, steps and pillars in Kissimmee, FL", body, faqs, ["solterra", "celebration"])


def get_pages():
    return [driveways(), patios(), pool_decks(), travertine(), marble_porcelain(), walkways(), sealing(), repair(), walls_outdoor_living(), turf(), lighting()]
