# -*- coding: utf-8 -*-
"""Ten concrete service pages, anchored in Kissimmee. Each page is written from scratch."""
from _data import SERVICES, CITIES, TIER1, COST_INDEX_RELEASE, src
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, callout, related, cs, cities_for_service, esc


def crumbs(key):
    return [("Home", "/"), ("Concrete", "/concrete/"), (SERVICES[key]["name"], None)]


def city_links(key):
    links = [cs(c, key, CITIES[c]["name"]) for c in cities_for_service(key)]
    if not links:
        return ""
    return sec("Where this service changes by city", f"<p>The Kissimmee page above is the master; these pages cover what changes by city: soil unit, permit office, HOA and the age of the houses.</p>" + related(links), eyebrow="City pages")


def page(key, title, desc, h1, body, faqs, sources, toc=None):
    return {"route": SERVICES[key]["route"], "title": title, "meta_description": desc, "h1": h1, "breadcrumbs": crumbs(key), "body_html": body + city_links(key), "faqs": faqs, "kind": "service", "service_key": key, "nav_active": "/concrete/", "sources": sources}


# ---------------------------------------------------------------------------
def driveways():
    k = "concrete-driveways"
    body = sec("What a concrete driveway costs, how thick it is and how long it takes",
        cap(f"A new broom-finish concrete driveway in Kissimmee runs about {cost_range('concrete-driveway-broom')} installed in the {COST_INDEX_RELEASE['label']} Cost Index, or {cost_range('concrete-driveway-6in')} at 6 inches with a rebar grid for boat and RV loads. Removing the old slab adds $2 to $4 per square foot. A two-car driveway is a two- to three-day job plus seven days before you park on it."),
        eyebrow="Quick answer")
    body += sec("What we build and what we rebuild",
        f"""<p>New driveways on new lots, tear-out and replacement of driveways from the 1970s through the 2000s, widening to the county's 24-foot limit, extensions to a side gate or a third bay, aprons where the drive meets the street, turnarounds on lots that back onto a busy road, and parking pads for a boat or camper beside the garage. Most of our replacement work in Kissimmee is on houses built between 1978 and 1995 in Buenaventura Lakes, Kissimmee Bay, the Bermuda Avenue and Vine Street corridors and the older streets off Pleasant Hill Road, where a 4-inch slab poured on unprepared sand has cracked into panels and settled at the garage door.</p>
<p>Finishes: broom (the standard, and the safest in rain), smooth trowel under a lanai roof only, exposed aggregate for a textured look, and integral color where an HOA wants the drive to match a palette. Stamped patterns are on their own page: {svc('concrete-stamped')}.</p>""")
    body += sec("How thick should a driveway be in Kissimmee, and what goes inside it?",
        cap("Four inches of 3,000 to 3,500 psi concrete with fiber reinforcement and #4 rebar along the edges is our standard for cars and SUVs. For boats, RVs, contractor trucks or a driveway that doubles as a turnaround, we pour 6 inches of 4,000 psi with a #4 rebar grid at 18 inches on chairs. Both sit on 4 inches of compacted limerock over proof-rolled sand.")
        + table(["Load", "Slab", "Mix", "Steel", "Base", "Joint spacing"], [
            ("Cars, SUVs, pickups", "4 in", "3,000–3,500 psi, fiber", "#4 bars at edges and re-entrant corners", "4 in limerock", "10 ft max"),
            ("Boat trailer, RV, moving truck", "6 in", "4,000 psi, fiber", "#4 grid @ 18 in on chairs", "4–6 in limerock", "12–15 ft"),
            ("Apron in the right-of-way", "6 in (Orange County detail); match county detail elsewhere", "3,000 psi", "None in the right-of-way", "Per county detail", "Per detail"),
        ], caption="Florida Building Code Residential R506 sets a 3½-inch minimum for slabs on ground; ACI 332 governs joints. We exceed both on driveways.")
        + f"<p>Wire mesh is the reinforcement most homeowners have heard of, and the one we use least on 4-inch work: unless it is chaired at mid-depth it ends up on the bottom of the slab where it does nothing, and a 4-inch slab does not leave room for chairs, mesh and cover. Fiber in the mix plus perimeter rebar controls plastic shrinkage cracking and holds edges; the full argument is in {compare('rebar-vs-fiber-vs-mesh')}. If a quote says \"4 inches with mesh\" ask how the mesh is held up.</p>")
    body += sec("Base and drainage on Osceola's flatwoods sand",
        f"""<p>Kissimmee sits on Smyrna, Myakka and Immokalee fine sands (USDA Soil Data Access, survey area FL097). They are level, they drain poorly, and the water table sits about 12 inches down for weeks between June and September. A slab poured on raw sand floats on saturated ground every summer and settles unevenly where a downspout or the sprinkler keeps one corner wetter than the rest. That is the crack pattern we see on most 1980s driveways in Buenaventura Lakes: a step at the garage, a diagonal at the apron.</p>
<p>So the base is where the money goes. We proof-roll the subgrade, probe for muck and roots, compact 4 inches of limerock in lifts, and set the forms to shed water at a minimum of ⅛ inch per foot away from the house and toward the street or a swale. Where the garage sits lower than the street, which is common on lots regraded after the 1990s stormwater rules, a trench drain at the garage door is part of the job, not an extra. Live oaks get a root barrier or a thickened section; see {guide('tree-roots-driveways-central-florida')}.</p>""", cls="alt")
    body += sec("Which office permits a driveway in Kissimmee?",
        cap("Inside Kissimmee city limits, a new, replaced or widened driveway goes through the Engineering Division's Driveway / Sidewalk Construction application on the EnerGov portal: plan review takes at least two business days and the permit issues at least two business days after the fee is paid. In unincorporated Osceola County, code §22-50.6 requires a county driveway permit for construction or widening and limits residential driveways to 24 feet wide unless a conditional use is approved.")
        + f"""<p>Which one applies depends on which side of the city line you are on, and the line is not obvious in Kissimmee: Buenaventura Lakes, most of the Bellalago and Pleasant Hill corridor, Poinciana and everything east toward Narcoossee are county; downtown, the lakefront, the Vine Street corridor and the newer annexations along John Young Parkway and Osceola Parkway are city. The {tool('permit-finder')} checks your address against the Census city boundary. We file the application as the contractor; you sign it, and on jobs of $5,000 or more in the county you also sign a Notice of Commencement that is recorded at the courthouse before the first inspection. Osceola's residential plan review normally takes 3 to 5 days once the application is complete. Details with sources: {juris('city-of-kissimmee')} and {juris('osceola-county')}.</p>
<p>HOA approval is separate and comes first. In Bellalago, Tapestry, Storey Lake, Remington and Eagle Lake the architectural committee reviews driveway changes; the {tool('hoa-packet-checklist')} lists what they typically ask for.</p>""")
    body += sec("What goes wrong with driveways here, and how we avoid it",
        table(["Symptom", "Usual cause in Kissimmee", "What we do differently"], [
            ("Step or crack at the garage door", "Sand under the slab washed out by roof runoff; no base", "Compacted base, downspouts extended past the slab, expansion joint at the garage"),
            ("Diagonal crack from the apron corner", "Truck loads on a 4-inch slab with no edge steel", "6-inch apron and #4 edge bars; turnarounds specified for the vehicle that uses them"),
            ("Panels rocking, hollow sound", "Saturated subgrade in low spots (Basinger sand)", "Raise the grade, add a swale, or specify 6 inches with a grid"),
            ("Random cracks across the middle", "Joints too far apart or cut too late", "Joints at 10 feet, tooled or cut within 12 hours, ¼ of slab depth"),
            ("Surface scaling or dusting", "Water added to the mix in the heat; finishing before bleed water leaves", "Slump controlled at the truck, early pour, no finishing on bleed water"),
            ("Orange streaks", "Well-water irrigation overspray", "Not a slab defect; see the rust-stain guide"),
        ]), cls="alt")
    body += sec("Process and timeline for a two-car driveway",
        f"""<ol class="steps">
<li>Site visit, soil check, written proposal (day 0).</li>
<li>Permit filed and HOA packet submitted (allow 1–3 weeks depending on the board's meeting schedule).</li>
<li>Utility locate (811), saw-cut at the apron and garage, demolition and haul-off (day 1).</li>
<li>Base compacted, forms set to grade, steel on chairs, inspection if required (day 1–2).</li>
<li>Pour at first light, broom finish, joints, cure compound or cover (day 2 or 3).</li>
<li>Forms pulled, edges dressed, final inspection; foot traffic after 24–48 hours, cars after 7 days, heavy vehicles after 28.</li>
</ol>
<p>June through September we pour early: the Kissimmee 2 NOAA station averages 15.8 to 17.7 rain days a month in those months, almost all in the afternoon. The {tool('pour-calendar')} shows the numbers and {guide('rainy-season-concrete-scheduling')} explains what happens if a storm arrives mid-pour.</p>""")
    body += sec(f"Concrete driveway costs in Kissimmee ({COST_INDEX_RELEASE['label']})",
        cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "concrete-removal", "stamped-concrete", "ready-mix"])
        + f"<p>Worked example: a 20-by-24-foot two-car driveway (480 square feet) at 4 inches uses about 6 cubic yards of concrete. At $8.50 to $13.50 per square foot the new slab is roughly $4,100 to $6,500; if the old drive has to come out, add $960 to $1,920. Widening a 16-foot drive to the 24-foot county maximum adds 8 feet by the length. The <a href=\"/pricing/concrete/\">concrete cost guide</a> has more examples and the <a href=\"/pricing/kissimmee-concrete-cost-index/\">Cost Index</a> explains the method.</p>", cls="alt")
    body += sec("Concrete or pavers for your driveway?",
        f"<p>Concrete wins on first cost and on a clean, uniform look; pavers win on repairability (a sunken area can be lifted and relaid) and on HOA preference in most resort and planned communities. Our side-by-side is {compare('concrete-vs-pavers')} and the eight-question {tool('concrete-vs-pavers')} gives a recommendation for your situation. If the existing drive is sound and only the surface is tired, {svc('concrete-resurfacing')} costs about half of a new pour.</p>")
    faqs = [
        faq("How much does a concrete driveway cost in Kissimmee?", f"About {cost_range('concrete-driveway-broom')} installed for a 4-inch broom-finish driveway in the {COST_INDEX_RELEASE['label']} Cost Index, plus $2 to $4 per square foot if an old slab has to be removed. A 480-square-foot two-car driveway lands between roughly $4,100 and $6,500 for the new concrete alone."),
        faq("Do I need a permit to replace my driveway in Kissimmee?", "Yes in both jurisdictions. Inside the city, the Engineering Division's Driveway / Sidewalk Construction application; in unincorporated Osceola County, a county driveway permit under §22-50.6. We file it. The only exception is resealing or patching an existing drive without changing its footprint."),
        faq("How wide can my driveway be?", "In unincorporated Osceola County, 24 feet unless a conditional use is approved (§22-50.6(a)). Inside Kissimmee and St. Cloud the city engineer reviews width with the application. HOAs often set a tighter limit: Solterra in Davenport, for instance, allows no more than three cars wide."),
        faq("How long before I can drive on new concrete?", "Walk on it after 24 to 48 hours, park a car after 7 days, and keep boats, RVs and moving trucks off for 28 days. Heat speeds the surface set but not the strength curve."),
        faq("Will you use rebar or wire mesh?", "Fiber in the mix and #4 rebar at the edges and corners on a 4-inch slab; a full #4 grid on chairs at 18 inches in a 6-inch slab. We avoid wire mesh in 4-inch slabs because it cannot be held at mid-depth reliably."),
        faq("Can you pour in the rainy season?", "Yes, with a first-light start and the slab finished and covered before the afternoon storms. If the forecast shows more than a 60 percent chance of rain before 2 p.m. we move the pour a day."),
        faq("Can you match my existing driveway when you add a section?", "We match the finish and place a straight joint at the seam so it reads as intentional. Color will be lighter for about a year; a light integral tint can close the gap on an older, warm-gray slab."),
    ]
    return page(k, "Concrete Driveways in Kissimmee, FL – Cost, Thickness, Permits", "Concrete driveways in Kissimmee: 4 in / 3,000 psi for cars, 6 in / 4,000 psi with rebar for RVs, 4 in limerock base for flatwoods sand, city vs. county permits, current cost per sq ft.", "Concrete driveways in Kissimmee, FL", body, faqs, ["fbc-r506", "aci332", "sda", "osceola-22-50-6", "kissimmee-driveway", "osceola-faq", "noaa"])


# ---------------------------------------------------------------------------
def patios():
    k = "concrete-patios"
    body = sec("Cost, thickness and timeline for a concrete patio in Kissimmee",
        cap(f"A poured concrete patio runs {cost_range('concrete-patio')} installed in the {COST_INDEX_RELEASE['label']} Cost Index; a 12-by-12 patio (144 square feet) usually lands between $1,300 and $1,900 because the truck minimum and the crew day are the same as a bigger pour. We pour 4 inches of 3,000 psi with fiber on a 2- to 4-inch compacted base, sloped ⅛ inch per foot away from the house. One day to form, one to pour."),
        eyebrow="Quick answer")
    body += sec("Patio types we pour",
        f"""<p>Lanai extensions that continue an existing slab out past the screen line; free-standing backyard patios for a grill and a table; fire-pit pads with a stone or paver ring; pads under a pergola or a pre-engineered aluminum roof; and side-yard slabs that connect the driveway to the back gate. Finishes are broom (grippy when wet, the right default around a pool or in a yard that floods), smooth trowel where the slab will be under a roof, exposed aggregate for texture, salt finish, and integral color to warm up the gray. Stamped patterns are covered on {svc('concrete-stamped')}; if you want pavers instead, {svc('paver-patios')}.</p>
<p>Two things that decide the look more than the finish: the slab edge (a clean formed edge with a tooled radius versus a broken edge against sod) and the joint layout (a 12-by-12 patio needs one joint each way, and placing them on the centerlines reads as a design instead of a crack control).</p>""")
    body += sec("What thickness and slope does a patio need on this soil?",
        cap("Four inches of 3,000 psi fiber-reinforced concrete on 2 to 4 inches of compacted limerock, with #4 rebar where the slab meets an existing slab or a pool deck, and a slope of at least ⅛ inch per foot away from the house. The Florida Building Code's residential minimum for a slab on ground is 3½ inches (R506); we do not go below 4 on exterior work because edges chip and fibers need cover.")
        + f"""<p>Drainage is the design question on a Kissimmee lot. Backyards here are flat, the water table is near the surface in summer, and a patio that slopes toward the house sends every afternoon storm into the lanai or against the stem wall. We set the slab to fall away from the structure and, where the yard has nowhere to send the water, add a slot drain along the outer edge tied to a downspout line or a dry well. Existing slabs get an expansion joint at the seam and dowels every 24 inches so the new pour does not settle away from the old one.</p>""", cls="alt")
    body += sec("Do you need a permit for a patio slab in Kissimmee?",
        cap("In the City of St. Cloud, yes: patios are on the city's list of projects that require a permit. In unincorporated Osceola County and inside Kissimmee city limits, a detached slab outside the setbacks and not attached to the house is generally handled without a building permit, but a slab inside a setback, tied to the structure, under a roof, or in a flood zone should be confirmed with the office first. Since July 1, 2026, HB 803 exempts single-family work valued under $7,500 with a written exemption request.")
        + f"<p>We confirm with the right office before we quote and put the answer in the proposal. If a roof, screen enclosure or pergola is going over the patio later, tell us: footings for those change the slab design and always need a permit. Jurisdiction pages: {juris('city-of-kissimmee')}, {juris('osceola-county')}, {juris('city-of-st-cloud')}, {juris('polk-county')}. HOA rules for patios are strict in APV Poinciana (no paved area without prior written DCB approval) and Solterra (rear setback of 15 feet, 5 feet to a pool deck or screen patio); see {hoa('poinciana-apv')} and {hoa('solterra')}.</p>")
    body += sec("From painted outline to first cookout",
        f"""<ol class="steps">
<li>Site visit: we mark the outline with paint, check the fall to the house, look for the septic tank and drainfield on rural St. Cloud and Harmony lots ({guide('septic-drainfield-concrete-driveway', 'never pour over a drainfield')}), and note irrigation lines to cap or move.</li>
<li>Written proposal with slab size, thickness, finish, joint layout and drainage.</li>
<li>Permit or HOA approval where required.</li>
<li>Excavate 6 to 8 inches, compact the subgrade, place and compact base, set forms to slope, tie in steel at existing slabs.</li>
<li>Pour in the morning, finish, joint, cure. Broom finish on the second pass once bleed water is gone.</li>
<li>Forms off next day, sod edges dressed. Furniture after 3 days; a hot tub or heavy planter after 28.</li>
</ol>""", cls="alt")
    body += sec(f"Patio costs in Kissimmee ({COST_INDEX_RELEASE['label']})",
        cost_rows(["concrete-patio", "stamped-concrete", "concrete-slab-pad", "concrete-removal"])
        + "<p>Why small patios cost more per square foot: the ready-mix truck has a minimum load and a short-load fee, the crew is on site for the same half day whether the slab is 144 or 400 square feet, and the base and forming happen either way. Combining a patio with a walkway or a shed pad in the same pour usually costs less than two separate visits.</p>")
    body += sec("Concrete, stamped or pavers for a patio?",
        f"<p>Plain concrete is the least expensive and the easiest to keep clean. Stamped concrete gives a stone or wood look for a third more but needs re-sealing every two to three years in this climate. Pavers cost roughly 50 percent more than plain concrete, can be lifted if a tree root or a pool leak moves the base, and are what most HOAs on the resort corridor already have on file. Comparisons: {compare('stamped-vs-pavers')} and {compare('concrete-vs-pavers')}.</p>", cls="alt")
    faqs = [
        faq("How much is a 12x12 concrete patio in Kissimmee?", f"Roughly $1,300 to $1,900 installed for a plain 4-inch broom-finish slab in the {COST_INDEX_RELEASE['label']} Cost Index, at the top of the {cost_range('concrete-patio')} range because of truck minimums and the crew day. Stamped or colored finishes add $6 to $10 per square foot."),
        faq("Do I need a permit for a backyard patio?", "In St. Cloud, yes. In unincorporated Osceola and in Kissimmee, a detached slab outside setbacks usually does not need a building permit, but we confirm with the office for your address and put the answer in writing. Anything with a roof or footings always needs one."),
        faq("Can you extend my existing lanai slab?", "Yes. We dowel #4 bars into the old slab every 24 inches, place an expansion joint at the seam, match the elevation and finish, and set the new slab to drain away from the house. Color will differ for a year."),
        faq("Broom or smooth finish?", "Broom outdoors. Smooth trowel is slick when wet, and Kissimmee gets 50-plus inches of rain a year. Under a solid roof, smooth or a light sand finish is fine."),
        faq("How soon can I put furniture on it?", "Light furniture after 3 days, a grill after 7, a hot tub or a heavy stone table after 28 days when the concrete reaches design strength."),
        faq("Will a patio crack?", "Hairline shrinkage cracks can appear; control joints at the centerlines are there to make them happen in the joint. Cracks that widen or offset mean the base moved, which on this soil usually means water is getting under the slab; the cracking guide shows the difference."),
    ]
    return page(k, "Concrete Patios in Kissimmee, FL – Cost, Slope, Permits", "Poured concrete patios in Kissimmee: 4 in / 3,000 psi on a compacted base, ⅛ in per ft slope away from the house, permit rules for Kissimmee, St. Cloud and Osceola, 12x12 cost example.", "Concrete patios in Kissimmee, FL", body, faqs, ["fbc-r506", "stcloud-permits", "osceola-faq", "hb803", "apv", "solterra"])


# ---------------------------------------------------------------------------
def pool_decks():
    k = "concrete-pool-decks"
    body = sec("What a concrete pool deck costs, and when resurfacing beats replacing",
        cap(f"A new textured concrete pool deck costs about the same as a patio, {cost_range('concrete-patio')} installed, plus a textured or cool-deck coating at $3 to $6 per square foot. Resurfacing a sound existing deck with a knock-down or spray texture runs {cost_range('concrete-resurfacing')}. A deck that is heaving, hollow or cracked through needs replacement or a paver overlay, not a coating."),
        eyebrow="Quick answer")
    body += sec("What we do around pools",
        f"""<p>New decks around new pools (coordinated with the pool builder, who owns the shell and the bond beam), replacement of old decks that have lifted or cracked, extensions to make room for a lounge area or an outdoor kitchen, and resurfacing of tired but sound decks with a textured acrylic system. Finishes: knock-down texture (the classic Florida cool-deck look), spray texture, broom, exposed aggregate and stamped. Every pool deck we pour drains away from the pool at ⅛ to ¼ inch per foot and, inside a screen enclosure, toward a channel drain along the screen line so the lanai does not pond after a storm.</p>
<p>If you want stone or pavers on the deck rather than coated concrete, that is {svc('paver-pool-decks')} and {svc('paver-travertine')}; the trade-offs, including how hot each surface gets, are in {compare('cool-deck-vs-pavers')} and {compare('travertine-vs-concrete-pavers')}.</p>""")
    body += sec("Why is my pool deck cracking or lifting, and can it be resurfaced?",
        cap("Three causes account for almost every failed pool deck in Osceola County: the deck was poured on the pool excavation backfill before it settled, the deck has no expansion joint at the coping so it pushes against the bond beam, or water from the deck runs back under the slab. A deck with hairline cracks, no vertical offset and a solid sound when tapped can be resurfaced. Offsets over ¼ inch, hollow spots or wide cracks mean the base failed and a coating will follow it.")
        + f"""<p>We tap-test the deck, check levels at the coping, look at where the water goes during a hose test, and tell you which category you are in. Resurfacing is a polymer-modified overlay or a textured acrylic system over a cleaned, profiled slab, with cracks routed and filled first; it will not hide movement. The decision tree is in {compare('resurface-vs-replace')}.</p>""", cls="alt")
    body += sec("Slip resistance and heat",
        f"<p>Two things matter more on a pool deck than anywhere else: it has to be grippy when wet and cool enough to walk on barefoot in July, when the Kissimmee 2 station's normal high is 91.5 °F. Knock-down textures and broom finishes handle the grip. For heat, color does most of the work: light-colored coatings and light concrete stay markedly cooler than charcoal or dark stamped finishes, and travertine and marble cooler still. Published installer measurements put standard gray concrete pavers at 130 to 145 °F at midday and travertine at 105 to 120 °F under the same sun; we collect those figures and our plan to measure decks here in {guide('surface-temperature-pool-decks')}.</p>")
    body += sec("Permits and HOA for pool decks",
        cap("A pool deck poured with a new pool is part of the pool permit and the pool contractor's scope. A replacement or extension of an existing deck is flatwork: St. Cloud lists patios and decks as permit-required; unincorporated Osceola and Kissimmee treat a detached deck outside setbacks as flatwork but any deck tied to the pool's bond beam, under a screen enclosure or inside a setback should be confirmed with the office. Screen enclosure footings always need a permit.")
        + f"<p>In resort communities (Reunion, ChampionsGate, Windsor Hills, Solterra, Storey Lake) the HOA reviews any visible change to a pool deck, and vacation-rental owners have to schedule around guests; {guide('vacation-rental-owner-hardscape-guide')} covers both. Solterra's guidelines put the pool deck setback at 5 feet to the side and rear; see {hoa('solterra')}.</p>", cls="alt")
    body += sec(f"Pool deck costs ({COST_INDEX_RELEASE['label']})",
        cost_rows(["concrete-patio", "concrete-resurfacing", "paver-pool-deck", "travertine-pool-deck", "concrete-removal"])
        + "<p>A 600-square-foot deck (a common size around a 14-by-28 pool) runs roughly $4,800 to $7,500 for new concrete before the texture coat, $3,000 to $5,700 to resurface, or $9,000 to $14,400 for a paver overlay. Removing an old deck around an existing pool costs more per foot than a driveway because of hand work near the shell and coping.</p>")
    faqs = [
        faq("Can you resurface my pool deck instead of replacing it?", "If it is sound: hairline cracks only, no vertical offsets, no hollow spots when tapped. We hose-test and tap-test first. Heaved or hollow decks need the base fixed, which usually means replacement or a paver overlay on a rebuilt base."),
        faq("What is cool deck?", "A trade name that became the generic term for a textured acrylic coating over concrete that stays cooler and grippier than plain concrete. We install knock-down and spray textures from current manufacturers; the comparison with pavers is on its own page."),
        faq("How long is the pool out of use?", "Two to four days for a resurfacing, five to seven for a replacement including cure before furniture goes back. The pool itself stays full; we protect the water and the coping."),
        faq("Should the deck drain toward the pool?", "No. Away from the pool at ⅛ to ¼ inch per foot, toward a deck drain or the yard, so deck water and chemicals do not run into the pool and the pool overflow does not undermine the slab."),
        faq("Do I need a permit to replace a pool deck?", "In St. Cloud, yes. Elsewhere it depends on whether the deck ties to the pool structure or the screen enclosure; we confirm with the office for your address before quoting."),
    ]
    return page(k, "Concrete Pool Decks in Kissimmee, FL – Resurface or Replace", "Concrete pool decks in Kissimmee: new textured decks, knock-down resurfacing, drainage away from the pool, slip and heat, permits and HOA, costs per sq ft for a 600 sq ft deck.", "Concrete pool decks in Kissimmee, FL", body, faqs, ["stcloud-permits", "solterra", "noaa"])


# ---------------------------------------------------------------------------
def stamped():
    k = "concrete-stamped"
    body = sec("What stamped concrete costs in Kissimmee and what to expect",
        cap(f"Stamped concrete with integral color, a release color and a sealer runs {cost_range('stamped-concrete')} installed in the {COST_INDEX_RELEASE['label']} Cost Index, roughly 60 to 70 percent more than a plain broom finish and 10 to 20 percent less than pavers. Patterns: ashlar slate, random stone, wood plank, cobble, herringbone brick. Re-seal every two to three years in this climate."),
        eyebrow="Quick answer")
    body += sec("Where stamped concrete works, and where it doesn't",
        f"""<p>Patios, pool decks, walkways and driveway borders are where stamped concrete earns its cost: a continuous slab with a stone look and no joints to sand. Full stamped driveways are possible but need 4,000 psi, tight joint spacing and a sealer that tolerates tires; we quote them, and we also tell you that pavers on a driveway are easier to repair after a utility cut. Under a lanai roof, stamped concrete is at its best, because the sealer lasts and the color does not fade.</p>
<p>Decorative options beyond stamping: integral color throughout the mix, broadcast color hardeners for a denser surface, acid or water-based stains on existing concrete, exposed aggregate with a local shell or river rock, and scored patterns cut into a smooth slab. Architectural finishes for modern homes (honed, board-formed) are on {svc('concrete-architectural')}.</p>""")
    body += sec("How is stamped concrete built so the pattern holds up in Florida heat?",
        cap("Stamping is a race against set time. In a Kissimmee summer the surface is ready to stamp 20 to 40 minutes after placement, so we pour small sections, work early, use a set retarder in the mix, and keep a crew on the stamps and one on the release. Color goes in the mix (integral) so a chip shows color, the release powder gives the antiqued highlights, and the slab is cleaned and sealed after 28 days.")
        + f"""<p>The slab underneath is the same 4-inch, 3,000 to 3,500 psi fiber-reinforced concrete on compacted base that we pour for a plain patio, with control joints hidden in grout lines of the pattern where possible. Sealer choice matters more here than anywhere else: a solvent-based acrylic gives the wet look and needs re-coating every two to three years; a water-based or penetrating product lasts longer with less shine. Full breakdown in {compare('sealer-types')}.</p>""", cls="alt")
    body += sec("What goes wrong with stamped concrete, and the fix",
        table(["Problem", "Cause", "Prevention or repair"], [
            ("White haze or peeling sealer", "Sealer applied over moisture, or too thick", "Strip and re-seal with a breathable product; seal only after 28 days on a dry slab"),
            ("Color fading unevenly", "Release color only (no integral color) plus UV", "Integral color under release; re-seal with a UV-stable acrylic"),
            ("Pattern washed out in areas", "Stamped too late in hot weather", "Smaller pours, retarder, early start"),
            ("Slippery when wet", "Glossy sealer with no grit", "Add a slip-resistant additive to the sealer"),
            ("Cracks outside grout lines", "Joints spaced too far or cut late", "Joint layout designed with the pattern; cut within 12 hours"),
        ]))
    body += sec("Permits and HOA",
        f"<p>Stamped concrete follows the same permit rules as the slab type it is (patio, pool deck, driveway): see {svc('concrete-patios')} and {svc('concrete-driveways')}. HOAs care about color and pattern. Solterra prohibits painting or staining concrete surfaces and allows only a clear matte sealer with a request; APV Poinciana requires prior written approval for any paved area; Solivita wants replacement driveways in the original material. We prepare the color and pattern sample the board asks for; see {tool('hoa-packet-checklist')}.</p>", cls="alt")
    body += sec(f"Stamped concrete costs ({COST_INDEX_RELEASE['label']})", cost_rows(["stamped-concrete", "concrete-patio", "paver-patio", "concrete-resurfacing"]) + "<p>Two colors or a border in a contrasting pattern push the price toward the top of the range; a single pattern in one color with a plain broom border sits at the bottom. Stamped overlays over an existing sound slab are possible at roughly the resurfacing price plus $4 to $6 per square foot for the stamp and color.</p>")
    faqs = [
        faq("How much does stamped concrete cost compared with pavers?", f"Stamped runs {cost_range('stamped-concrete')} in the {COST_INDEX_RELEASE['label']} index; concrete pavers on a patio run {cost_range('paver-patio')}. Pavers cost a little more up front and can be lifted for repairs; stamped concrete is one continuous surface and needs periodic re-sealing."),
        faq("How often does stamped concrete need sealing in Florida?", "Every two to three years for a solvent-based acrylic in full sun, three to five for a penetrating sealer or a slab under a lanai roof. Signs it is time: water no longer beads, color looks flat."),
        faq("Will stamped concrete fade?", "Release color alone fades; integral color in the mix does not. We use both, and a UV-stable sealer. Expect the antiqued highlights to soften over five to eight years, which most owners like."),
        faq("Can you stamp over my existing patio?", "If the slab is sound, yes, with a stamped overlay. If it is cracked through or moving, the overlay will crack the same way."),
        faq("Is stamped concrete slippery?", "Glossy sealers can be. We add a grit additive to the sealer on pool decks and walkways."),
    ]
    return page(k, "Stamped & Decorative Concrete in Kissimmee, FL – Cost & Care", "Stamped concrete patios, pool decks and borders in Kissimmee: patterns, integral plus release color, how we stamp in summer heat, sealer choices, HOA color rules, cost per sq ft.", "Stamped and decorative concrete in Kissimmee, FL", body, faqs, ["solterra", "apv", "solivita"])


# ---------------------------------------------------------------------------
def slabs():
    k = "concrete-slabs"
    body = sec("Shed, AC, generator, hot tub, RV and workshop slabs in Kissimmee",
        cap(f"A concrete pad runs {cost_range('concrete-slab-pad')} installed in the {COST_INDEX_RELEASE['label']} Cost Index; a 10-by-12 shed pad typically lands at $1,200 to $1,900 and a 12-by-40 RV pad at 6 inches with rebar at $6,500 to $9,500. Thickness follows the load: 4 inches for sheds and AC units, 5 under a hot tub, 6 with a #4 grid for RVs, boats and workshop equipment."),
        eyebrow="Quick answer")
    body += sec("Pads we pour, and the spec for each",
        table(["Pad", "Typical size", "Thickness / mix", "Steel", "Notes"], [
            ("Storage shed", "8×10 to 12×20", "4 in, 3,000 psi", "Fiber; #4 at edges", "Osceola has published shed permit requirements; anchoring is the shed installer's scope"),
            ("AC condenser", "3×3 to 4×4", "4 in, 3,000 psi", "Fiber", "Raised 2–4 in above grade so the unit stays out of standing water"),
            ("Standby generator", "4×8 to 5×10", "4 in, 3,000 psi", "#4 grid", "Manufacturer clearances from the house govern location; electrical and gas are licensed trades"),
            ("Hot tub / swim spa", "8×8 to 10×16", "5 in, 3,500 psi", "#4 grid @ 12 in", "A filled 8-person spa weighs about 6,000 lb; level within ¼ in"),
            ("RV / boat pad", "12×40 to 14×50", "6 in, 4,000 psi", "#4 grid @ 18 in on chairs", "Turning radius and hitch swing checked on site; county driveway permit if it connects to the street"),
            ("Workshop / metal building", "24×30 and up", "6 in, 4,000 psi, thickened edge", "#4 grid; edge footing per building supplier", "Anchor bolt layout from the building supplier; permit as an accessory structure"),
            ("Dumpster / equipment pad (commercial)", "10×12 to 12×20", "6–8 in, 4,000 psi", "#4 or #5 grid", "See commercial concrete"),
        ]))
    body += sec("Base, elevation and the water table",
        f"""<p>The one rule for a pad on Osceola's flatwoods sand: keep it above the water. Smyrna and Myakka fine sands hold a wet-season water table about 12 inches down, and a pad set flush with the lawn will have wet feet every June. We build pads 2 to 4 inches above finished grade on 4 inches of compacted limerock, with the top sloped ¼ inch per foot so rain runs off, and we pull the pad away from downspouts. On the Polk County ridge (Davenport, Haines City, Lake Wales) the soil is Candler sand, deep and dry, and the issue is compaction of a base that will not densify unless it is wetted first; see {guide('paver-base-flatwoods-vs-ridge')}.</p>
<p>Rural St. Cloud, Harmony and Kenansville lots often have a septic system. A pad or driveway over a drainfield compacts the soil, blocks evaporation and can crush the pipe; we locate the tank and drainfield from the county record and keep the pad off them: {guide('septic-drainfield-concrete-driveway')}.</p>""", cls="alt")
    body += sec("Do I need a permit for a concrete pad in Osceola or Polk County?",
        cap("It depends on what sits on it. In Polk County, slabs adjacent to or intended to support a structure, elevated slabs, and slabs within the minimum setbacks require a permit; a free-standing pad outside setbacks does not. Osceola publishes shed permit requirements and treats the shed, not the pad, as the permitted structure. Generator and AC pads are usually inspected under the electrical or mechanical permit for the equipment. HB 803's $7,500 exemption (July 1, 2026) can cover a stand-alone pad with a written request.")
        + f"<p>We confirm with the office for your address and put it in the proposal. Sources and office contacts: {juris('osceola-county')}, {juris('polk-county')}, {juris('city-of-kissimmee')}, {juris('city-of-st-cloud')}. HOA rules are stricter than permits for sheds: APV Poinciana requires sheds on a concrete pad, no taller than 8 feet, colored to match the house, and prohibits them entirely in Cypress Woods; see {hoa('poinciana-apv')}.</p>")
    body += sec(f"Pad costs ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-slab-pad", "concrete-driveway-6in", "concrete-patio", "ready-mix"]) + f"<p>Small pads carry a minimum charge because the ready-mix short-load fee and the crew's half day are fixed. Combining a shed pad with a walkway or AC pad in one visit saves 20 to 30 percent versus two trips. Size the pad yourself with the {tool('concrete-paver-calculator')}: it converts length, width and thickness into cubic yards and bags and applies the current index range.</p>", cls="alt")
    faqs = [
        faq("How thick should a shed pad be?", "Four inches of 3,000 psi concrete with fiber for a storage shed, set 2 to 4 inches above grade on a compacted base. Go to 5 inches with a rebar grid if the shed will hold a riding mower, a lift or heavy shelving."),
        faq("How thick should an RV pad be?", "Six inches of 4,000 psi with a #4 rebar grid at 18 inches on chairs. A 12-by-40 pad uses about 9 cubic yards. If it connects to the street it also needs the county or city driveway permit."),
        faq("Do I need a permit for a shed slab in Osceola County?", "The county permits the shed as an accessory structure and publishes the requirements; the slab is inspected with it. A pad with nothing on it outside the setbacks is generally not permitted separately, and HB 803's $7,500 exemption may apply with a written request. We confirm with the office before quoting."),
        faq("Can you pour a pad over my septic drainfield?", "No, and neither should anyone else. We locate the tank and drainfield from the county record and keep the pad clear."),
        faq("How level does a hot tub pad need to be?", "Within ¼ inch across the pad. We pour 5 inches with a grid, then check with a laser before it sets."),
    ]
    return page(k, "Concrete Slabs & Pads in Kissimmee, FL – Shed, RV, AC, Hot Tub", "Concrete pads in Kissimmee and Osceola County: shed, AC, generator, hot tub, RV, boat and workshop slabs with thickness and rebar by load, elevation above the water table, permit rules, costs.", "Concrete slabs and pads in Kissimmee, FL", body, faqs, ["polk-faq", "osceola-faq", "hb803", "apv", "sda"])


# ---------------------------------------------------------------------------
def sidewalks():
    k = "concrete-sidewalks-walkways"
    body = sec("What a walkway costs in Kissimmee and which rules apply",
        cap(f"A 4-foot-wide concrete walkway runs {cost_range('concrete-sidewalk')} installed in the {COST_INDEX_RELEASE['label']} Cost Index, about $8.50 to $13 per square foot. A 40-foot front walk costs roughly $1,400 to $2,100. Sidewalk sections in the public right-of-way follow the city or county detail and need the same driveway/sidewalk application as a driveway inside Kissimmee."),
        eyebrow="Quick answer")
    body += sec("What we pour",
        f"""<p>Front walks from the driveway to the door, side-yard paths to the gate and the AC pad, garden paths, walkways connecting a patio to a pool, and replacement of public sidewalk panels that a tree root or a utility cut has lifted in front of your house. Widths: 3 feet for a side path, 4 feet for a front walk (two people abreast), 5 feet where the right-of-way detail calls for it. Finishes: broom, with a tooled edge and joints every 4 to 5 feet so the panels read as a walk and not a slab. If you want pavers or steps, see {svc('paver-walkways-steps')}.</p>""")
    body += sec("Spec for a walkway on this soil",
        cap("Four inches of 3,000 psi fiber-reinforced concrete on 2 inches of compacted base, joints every 4 to 5 feet, a cross-slope of ⅛ to ¼ inch per foot so water runs off the walk and not along it, and a ½-inch expansion joint where the walk meets the driveway, the stoop or a public sidewalk. Right-of-way sidewalk sections follow the jurisdiction's detail, which in Orange County means 6 inches of 3,000 psi with no steel.")
        + f"<p>Walkways fail at the edges and at trees. Edges chip when the form is pulled before the concrete has set, or when sod is laid so the walk edge is unsupported; we tool a radius and leave the form on overnight. Live oaks lift walk panels within a few years if the walk crosses the root plate; we curve the walk around the tree, bridge with a thicker panel, or install a root barrier, as explained in {guide('tree-roots-driveways-central-florida')}.</p>", cls="alt")
    body += sec("Permits for walkways and public sidewalk",
        cap("A private walkway on your lot outside the setbacks is flatwork that generally needs no building permit in Kissimmee or unincorporated Osceola County; St. Cloud sends sidewalk pavers to Public Works and reviews poured work case by case. Any sidewalk in the public right-of-way is different: inside Kissimmee it is the Engineering Division's Driveway / Sidewalk Construction application; in Osceola County it falls under LDC 4.12.2 right-of-way rules; in Polk County sidewalks in the right-of-way need a permit.")
        + f"<p>APV Poinciana caps any walkway adjacent to the house at 2 feet wide unless the DCB approves otherwise (Criteria 9.1.1), and Solterra prohibits additional sidewalks without approval; see {hoa('poinciana-apv')} and {hoa('solterra')}. Jurisdiction detail: {juris('city-of-kissimmee')}, {juris('osceola-county')}, {juris('polk-county')}.</p>")
    body += sec(f"Walkway costs ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-sidewalk", "paver-walkway", "concrete-removal", "concrete-repair"]) + "<p>Narrow walks cost more per square foot than patios because forming is the same on both sides for a third of the area. Replacing a single lifted public sidewalk panel is a minimum-charge job; two or three panels together cost far less each.</p>", cls="alt")
    faqs = [
        faq("How wide should a front walkway be?", "Four feet lets two people walk side by side; three feet is fine for a side path. APV Poinciana limits walks adjacent to the house to 2 feet without DCB approval, so check the community rule first."),
        faq("Who fixes the public sidewalk in front of my house?", "It varies by jurisdiction and by who damaged it. Inside Kissimmee, sidewalk work in the right-of-way goes through the Engineering Division's application; we can do the work under that permit."),
        faq("How much is a 40-foot walkway?", f"About $1,400 to $2,100 at 4 feet wide in the {COST_INDEX_RELEASE['label']} index, more if an old walk has to be removed or the route crosses tree roots."),
        faq("Can a walkway be poured in one day?", "Forming and base one day, pour the next morning, walk on it the day after. Small jobs are often combined with a pad or patio pour."),
        faq("Will tree roots lift it?", "Eventually, if it crosses a live oak's root plate. Curving around the tree or installing a root barrier at pour time is far cheaper than replacing panels later."),
    ]
    return page(k, "Concrete Sidewalks & Walkways in Kissimmee, FL – Cost & Rules", "Concrete walkways and sidewalk sections in Kissimmee: 4 in / 3,000 psi, 4-ft width, joints every 4–5 ft, right-of-way rules for Kissimmee, Osceola and Polk, HOA width limits, cost per linear foot.", "Concrete sidewalks and walkways in Kissimmee, FL", body, faqs, ["kissimmee-driveway", "polk-faq", "apv", "solterra", "orange-permit"])


# ---------------------------------------------------------------------------
def repair():
    k = "concrete-repair"
    body = sec("Cracks, sinking, spalling and trip hazards in Kissimmee",
        cap(f"Repairing a sunken or cracked section of driveway costs less than replacing it only when the base under the rest of the slab is sound. Sectional replacement of a failed panel runs {cost_range('concrete-driveway-broom')} for the new concrete plus $2 to $4 for removal; routing and sealing cracks or grinding a trip hazard is a minimum-charge visit of a few hundred dollars. We inspect first and tell you which repair is worth doing."),
        eyebrow="Quick answer")
    body += sec("Which cracks are normal and which mean trouble?",
        cap("Hairline cracks under 1/16 inch with no vertical offset are shrinkage cracks; every slab has them and they are cosmetic. Cracks that widen past 1/8 inch, show a step from one side to the other, run diagonally from a corner, or come with a hollow sound when you tap the slab mean the base has moved, and on Osceola's saturated flatwoods sand that almost always means water is getting under the slab.")
        + table(["What you see", "What it usually means here", "Repair"], [
            ("Hairline map cracks, no offset", "Plastic shrinkage; too much water in the mix or finished in the heat", "Cosmetic; seal if you want to keep water out"),
            ("Straight crack near a joint or where one should be", "Joints spaced too far or cut late", "Route and fill with a flexible sealant; add a joint"),
            ("Step at the garage door", "Roof runoff washed the sand from under the slab edge", "Fix the downspout, then lift (polyurethane) or replace the panel"),
            ("Corner broken off at the apron", "Truck loads on a thin, unreinforced edge", "Replace the apron section at 6 in with edge steel"),
            ("Panel sunk 1–2 in, hollow sound", "Void from washout or a leaking irrigation line", "Repair the leak; lift or replace"),
            ("Surface flaking (spalling)", "Finishing on bleed water, or sealer trapping moisture", "Resurface with a polymer overlay if the slab is sound"),
            ("Slab lifted at a tree", "Live oak roots", "Root barrier and panel replacement, or reroute"),
        ]))
    body += sec("Lift, patch or replace?",
        f"""<p>Polyurethane lifting (foam injected under the slab to raise it) works when the slab is intact and the void is small and dry; it is fast and leaves the surface as it was, and several national companies sell it aggressively in Kissimmee. It does not fix the reason the slab sank. If a downspout or a broken sprinkler line is still saturating the sand, the foam and the slab go back down within a few seasons. We recommend lifting when the slab is under ten years old, the cause has been corrected, and the panel is otherwise sound. We recommend sectional replacement when the panel is cracked through, when it is the apron or garage-edge panel that carries the load, or when the driveway is 1980s vintage and the rest of it is on borrowed time; at that point {svc('concrete-driveways', 'replacing the whole drive')} is often the better dollar. The decision tree with numbers is in {compare('resurface-vs-replace')}.</p>
<p>Patching with bagged mortar over a moving crack is the repair we are most often asked to redo. It fails at the bond line within a year. Cracks get routed to a clean V and filled with a flexible polyurethane sealant that moves with the slab; spalled surfaces get a polymer-modified overlay ({svc('concrete-resurfacing')}); trip hazards over ¼ inch on a walk get ground flush or the panel replaced.</p>""", cls="alt")
    body += sec("Repairs in Buenaventura Lakes and other 1980s neighborhoods",
        f"<p>Buenaventura Lakes, Kissimmee Bay and the older Poinciana villages were built from the late 1970s into the 1990s on 4-inch slabs with little or no base. Forty years of wet seasons later, most of those driveways are cracked into three or four panels with a step at the garage. Repairing one panel buys time; the neighbors' panels show what the rest of the drive will do. We price both the repair and the replacement so you can decide with the numbers in front of you. City pages: {cs('buenaventura-lakes', 'concrete-repair')}, {cs('poinciana', 'concrete-repair')}, {cs('st-cloud', 'concrete-repair')}, {cs('davenport', 'concrete-repair')}.</p>")
    body += sec("Permits for repairs",
        f"<p>Patching, crack sealing, grinding and lifting are maintenance and need no permit. Replacing a panel in the same footprint is generally treated as repair; replacing the apron or any section in the right-of-way needs the driveway/sidewalk application in Kissimmee and the driveway permit in unincorporated Osceola. HOAs usually want notice for a visible panel replacement because the new concrete will be lighter. Offices: {juris('city-of-kissimmee')}, {juris('osceola-county')}, {juris('city-of-st-cloud')}, {juris('polk-county')}.</p>", cls="alt")
    body += sec(f"Repair costs ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-repair", "concrete-resurfacing", "concrete-removal", "concrete-driveway-broom"]) + "<p>Crack routing and sealing is priced by the linear foot with a minimum visit charge; panel replacement by the square foot at new-pour rates plus removal; grinding a trip hazard by the hour. Lifting is quoted per job by the injection contractor; we refer it when it is the right answer.</p>")
    faqs = [
        faq("Why is my driveway sinking at the garage?", "Roof water. The downspout or the roof edge dumps water at the slab edge, the fine sand under it washes out, and the panel drops. Fix the water first (extend the downspout, add a splash block or a drain), then lift or replace the panel."),
        faq("Is polyurethane lifting worth it?", "For an intact, relatively new slab with a small, dry void after the water problem is fixed, yes. For a cracked 1980s panel that carries traffic at the apron or garage, replacement is the better spend."),
        faq("Can you repair a crack so it doesn't show?", "Not invisibly. A routed and sealed crack shows as a clean line; a replaced panel shows as a lighter panel for about a year. Resurfacing the whole slab hides both."),
        faq("Does homeowners insurance cover a cracked driveway?", "Usually not for settling, roots or wear. Sudden damage from a covered event (a vehicle, a fallen tree) sometimes is. Check your policy; we provide photos and a written assessment for a claim."),
        faq("How fast can you fix a trip hazard on my walk?", "Grinding a lip under ¾ inch is a same-week visit. Replacing a panel is a two-day job once scheduled."),
    ]
    return page(k, "Concrete Repair in Kissimmee, FL – Cracks, Sinking, Spalling", "Concrete repair in Kissimmee and Osceola County: which cracks matter, why slabs sink at the garage on flatwoods sand, lift vs. patch vs. replace with costs, 1980s Buenaventura Lakes driveways.", "Concrete repair in Kissimmee, FL", body, faqs, ["sda", "kissimmee-driveway", "osceola-22-50-6"])


# ---------------------------------------------------------------------------
def resurfacing():
    k = "concrete-resurfacing"
    body = sec("What resurfacing fixes in Kissimmee, and what it costs",
        cap(f"A polymer-modified overlay over a sound slab runs {cost_range('concrete-resurfacing')} installed in the {COST_INDEX_RELEASE['label']} Cost Index, about half the cost of a new pour. It fixes spalling, surface scaling, stains and a tired finish; it does not fix a moving base. Textures: knock-down, spray, broom, stamped overlay. Two to three days including cure."),
        eyebrow="Quick answer")
    body += sec("What resurfacing can and cannot do",
        f"""<p>An overlay is a thin layer (⅛ to ½ inch) of cement, polymer and fine aggregate bonded to a cleaned and profiled slab. It renews the surface of a driveway, patio, pool deck or walkway that is structurally fine but ugly: spalled from years of pressure washing and sealer, pitted, stained by rust or oil, or scarred by an old coating. It can also change the look, from plain gray to a knock-down texture or a stamped stone pattern, for a third of the price of tearing out and re-pouring.</p>
<p>It cannot hold a slab together. Panels that rock, cracks with an offset, hollow spots, and slabs that heave against the pool coping will telegraph through any overlay within a season. That is why we hose-test and tap-test before we quote and send you to {svc('concrete-repair')} or a new pour when that is the honest answer; the decision tree is {compare('resurface-vs-replace')}.</p>""")
    body += sec("How we resurface",
        f"""<ol class="steps">
<li>Inspection: tap test for hollows, string line for offsets, hose test for drainage, moisture check.</li>
<li>Repair: cracks routed and filled with a flexible sealant, spalled areas ground, pop-outs patched.</li>
<li>Profile: pressure wash at 3,500 psi and acid-etch or grind so the overlay bonds; rust and oil stains treated with the right chemistry (a rust remover for iron, a degreaser for oil; {guide('rust-stains-irrigation-well-water')}).</li>
<li>Bond coat and overlay in one or two passes, textured while wet (knock-down, spray, broom or stamped).</li>
<li>Cure 24 hours, then seal with a breathable sealer chosen for sun exposure and slip resistance ({compare('sealer-types')}).</li>
<li>Foot traffic after 24 hours, vehicles after 72 hours in warm weather.</li>
</ol>
<p>Timing matters in the rainy season: overlays are thin and a downpour 30 minutes after placement ruins them, so we work mornings and watch the radar the same way we do for pours ({tool('pour-calendar')}).</p>""", cls="alt")
    body += sec("Permits and HOA", f"<p>Resurfacing is maintenance and does not need a permit in any of our jurisdictions. HOAs care about color and finish: Solterra allows only a clear matte sealer on concrete and prohibits paint or stain, so a colored overlay there needs approval first; see {hoa('solterra')} and the {tool('hoa-packet-checklist')}.</p>")
    body += sec(f"Resurfacing costs ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-resurfacing", "stamped-concrete", "concrete-driveway-broom", "concrete-removal"]) + "<p>A 480-square-foot two-car driveway resurfaces for about $2,400 to $4,600, versus $5,000 to $8,400 to remove and re-pour. The gap is why we push back when a homeowner is about to overlay a slab that is moving: spending half now and the full amount in three years is the expensive path.</p>", cls="alt")
    faqs = [
        faq("How long does a resurfaced driveway last?", "Ten to fifteen years on a sound slab with a re-seal every three to five years. The overlay is only as stable as the concrete under it."),
        faq("Can you resurface a pool deck?", "Yes; knock-down and spray textures over a sound deck are the most common resurfacing job we do. Heaved or hollow decks need the base fixed first."),
        faq("Will the overlay crack where the old slab is cracked?", "Existing cracks are routed and filled, and joints are honored through the overlay. Static shrinkage cracks stay hidden; moving cracks reappear, which is why we test the slab first."),
        faq("Can you change the color or add a pattern?", "Yes. Integral color in the overlay, a stamped overlay for a stone look, or a two-tone knock-down. HOA approval may be needed for a visible color change."),
        faq("How soon can I drive on it?", "About 72 hours in warm weather; foot traffic after 24 hours. Sealing adds a day."),
    ]
    return page(k, "Concrete Resurfacing & Overlays in Kissimmee, FL – Cost", "Concrete resurfacing in Kissimmee: polymer overlays and knock-down textures over sound driveways, patios and pool decks, what an overlay cannot fix, process, sealing and cost vs. a new pour.", "Concrete resurfacing and overlays in Kissimmee, FL", body, faqs, ["solterra"])


# ---------------------------------------------------------------------------
def architectural():
    k = "concrete-architectural"
    body = sec("Honed, board-formed and custom finishes in Kissimmee",
        cap("Architectural concrete treats the slab or wall as a design element: honed and polished flatwork, board-formed seat walls and planters that show the wood grain, large-format saw-cut panels with open joints, integral colors chosen to a paint chip, and exposed local aggregate. Pricing starts around stamped-concrete rates and rises with the finish; every job is quoted after a sample panel is approved."),
        eyebrow="Quick answer")
    body += sec("Where it fits",
        f"""<p>New construction in Bellalago's estate sections, the lakefront streets of Kissimmee and St. Cloud, Harmony's newer phases and the modern farmhouse and coastal-contemporary homes going up around Narcoossee and Lake Nona's southern edge. Typical scopes: a front entry with a floating concrete stoop and porcelain treads, a lanai floor honed to a low sheen and saw-cut into 4-by-4-foot panels, a board-formed seat wall around a fire feature, a monolithic outdoor kitchen counter, and driveway ribbons separated by turf or gravel strips. The porcelain-capped steps and the stone-faced curved terrace in our gallery are this kind of work.</p>
<p>It pairs with {svc('paver-marble-porcelain')} for large-format pavers, {svc('paver-retaining-walls-outdoor-living')} for walls and kitchens, and {svc('paver-outdoor-lighting')} for the lighting that architectural finishes are usually designed around.</p>""")
    body += sec("How architectural finishes are built",
        table(["Finish", "How", "Where it works", "Watch out for"], [
            ("Honed / polished", "Grind the cured slab with progressively finer diamonds, densify, seal", "Lanais, covered patios, entries", "Slippery when wet unless left at a low grit; not for open pool decks"),
            ("Board-formed", "Cast against rough-sawn boards so the grain and joints show", "Seat walls, planters, retaining walls, kitchen bases", "Needs a mix that flows into the texture; form release and vibration matter"),
            ("Saw-cut panels", "Pour, then cut a grid of clean joints ⅛ in wide", "Modern flatwork", "Joint spacing has to follow ACI 332 or the panels crack elsewhere"),
            ("Integral color to a chip", "Pigment dosed by the yard; sample panel first", "Anywhere", "Color varies between trucks; we pour one area from one load"),
            ("Exposed aggregate", "Seed local shell or river rock, wash the surface", "Patios, walks", "Sealer choice controls slip and gloss"),
            ("Concrete countertops and bench tops", "Cast in place or precast, ground and sealed", "Outdoor kitchens", "Food-safe sealer; heat from grills"),
        ], caption="Every architectural job starts with a 2-by-2-foot sample panel you approve before we form the real thing."))
    body += sec("Permits and HOA", f"<p>Flatwork follows the same permit logic as patios and driveways ({juris('city-of-kissimmee')}, {juris('osceola-county')}, {juris('city-of-st-cloud')}). Walls over 4 feet, anything retaining a load or supporting a roof, and kitchen gas and electrical need licensed trades and permits; we build the decorative and flatwork scope and coordinate the rest. Architectural review committees want drawings and a color sample for anything visible from the street; the {tool('hoa-packet-checklist')} lists it.</p>", cls="alt")
    faqs = [
        faq("Is architectural concrete slippery?", "Honed floors can be if polished to a high grit and used in the open. We stop at a lower grit on exterior floors and use a penetrating sealer with an anti-slip additive; broom and exposed aggregate finishes are grippy by nature."),
        faq("How much does it cost?", "Quoted per job after the sample panel. Expect stamped-concrete rates as a floor and two to three times plain concrete for honed floors and board-formed walls."),
        faq("Can you match a paint chip?", "Closely. Integral pigment is dosed to a target and we pour a sample; concrete color varies by a shade between loads, so one area is poured from one truck."),
        faq("Do you do the outdoor kitchen too?", "The concrete and paver structure, counters and the hardscape around it. Gas, electrical and appliances are licensed trades we coordinate with."),
    ]
    return page(k, "Architectural Concrete in Kissimmee, FL – Honed, Board-Formed", "Architectural concrete in Kissimmee: honed and polished lanai floors, board-formed seat walls, saw-cut panels, integral color to a chip, exposed aggregate. Sample panels first; permits and ARC notes.", "Architectural concrete in Kissimmee, FL", body, faqs, ["aci332"])


# ---------------------------------------------------------------------------
def commercial():
    k = "concrete-commercial"
    body = sec("Commercial flatwork in Kissimmee and Osceola County",
        cap("Small commercial concrete: dumpster pads, sidewalks and ADA ramps, equipment pads, small parking areas and drive lanes, loading aprons, and repairs at strip centers, churches, HOA amenity centers and vacation-rental communities. We pour 6 to 8 inches of 4,000 psi with a rebar grid on an engineered base for vehicle areas and 4 to 6 inches for pedestrian work. Commercial permits in Osceola run 2 to 4 weeks of plan review."),
        eyebrow="Quick answer")
    body += sec("Scope we take on",
        f"""<p>We are a flatwork crew, not a site contractor. The commercial jobs that fit: a dumpster enclosure pad for a restaurant on US-192, a replacement sidewalk and ramp at a church in St. Cloud, a pad for a generator or a chiller behind a medical office, a 20-space parking area for an HOA clubhouse in Poinciana, drive-lane panel replacement at a shopping center, and the pool deck and walkways at a vacation-rental community's amenity center in Four Corners or ChampionsGate. Large parking lots, structural slabs, foundations and anything requiring a general contractor of record are outside our scope and we say so up front.</p>""")
    body += sec("Specs for commercial pads and drive lanes",
        table(["Element", "Thickness / mix", "Steel", "Base", "Notes"], [
            ("Dumpster pad and approach", "8 in, 4,000 psi", "#4 grid @ 12 in", "6 in compacted limerock", "Sized for the truck's front wheels; slope to a drain"),
            ("Drive lane panels", "6–8 in, 4,000 psi", "#4 grid @ 18 in", "6 in", "Match existing joint layout; dowel to adjacent panels"),
            ("Parking stalls (light vehicles)", "6 in, 4,000 psi", "#4 grid or fiber + edge steel", "6 in", "Joints at 12–15 ft"),
            ("Sidewalk and ADA ramp", "4 in (6 in at curb ramps), 3,000–4,000 psi", "Fiber; #4 at ramps", "4 in", "Detectable warning surfaces and slopes per the ADA standards"),
            ("Equipment pad", "6 in, 4,000 psi", "#4 grid", "4–6 in", "Anchor bolt layout from the equipment supplier"),
        ], caption="Where a site plan or an engineer specifies otherwise, the engineered detail governs."))
    body += sec("Permits", f"<p>Commercial work needs a building permit in every jurisdiction here and usually a site-plan or engineering review for anything touching drainage or parking counts. Osceola County's commercial plan review normally takes 2 to 4 weeks (Building Office FAQ). Kissimmee and St. Cloud review through their own building divisions; Polk through the Building Division in Bartow. We handle the flatwork permit; the property owner's engineer handles drainage and site approvals. Contacts: {juris('osceola-county')}, {juris('city-of-kissimmee')}, {juris('city-of-st-cloud')}, {juris('polk-county')}.</p>", cls="alt")
    body += sec("Pricing", "<p>Commercial flatwork is quoted per job from plans or a site visit; thickness, steel, base, traffic control, night or weekend work and haul-off drive the price. As a reference, 6-inch 4,000 psi work with a grid runs in the $11.50 to $17 per square foot range in our residential index before commercial requirements are added.</p>")
    faqs = [
        faq("Do you do parking lots?", "Small ones: an HOA clubhouse lot, a church lot expansion, drive-lane panel replacement at a center. Full-size commercial lots with site drainage design are outside our scope."),
        faq("How thick is a dumpster pad?", "Eight inches of 4,000 psi with a #4 grid at 12 inches, sized so the truck's front wheels sit on the pad when it lifts the container."),
        faq("Can you work at night or on weekends?", "Yes for occupied centers and amenity areas; it is priced into the quote."),
        faq("Who pulls the permit?", "We pull the flatwork permit as the contractor. Site-plan, drainage and engineering approvals are the owner's engineer's scope."),
    ]
    return page(k, "Commercial Concrete & Parking Lots in Kissimmee, FL – Flatwork", "Commercial flatwork in Kissimmee and Osceola County: dumpster pads, sidewalks and ADA ramps, equipment pads, small parking areas and drive-lane repairs. Specs, permit timelines, scope limits.", "Commercial concrete and small parking lots in Kissimmee, FL", body, faqs, ["osceola-faq"])


def get_pages():
    return [driveways(), patios(), pool_decks(), stamped(), slabs(), sidewalks(), repair(), resurfacing(), architectural(), commercial()]
