# -*- coding: utf-8 -*-
"""Tier-1 city hubs: Kissimmee, St. Cloud, Celebration, Poinciana, Buenaventura Lakes, Four Corners,
ChampionsGate, Reunion, Davenport, Haines City, Harmony & Narcoossee."""
from _data import CITIES, SERVICES, COST_INDEX_RELEASE, drive_estimate, city_service_route
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, related, cs, city_services_for, esc


def crumbs(key):
    return [("Home", "/"), ("Areas", "/areas/"), (CITIES[key]["name"], None)]


def page(key, title, desc, h1, body, faqs, sources):
    links = [cs(key, s, SERVICES[s]["name"]) for s in city_services_for(key)]
    if links:
        body += sec(f"Service pages written for {CITIES[key]['name']}", "<p>Each of these covers the soil, permit office, HOA and housing stock of this place for one service, and links back to the master service page.</p>" + related(links), eyebrow="Local service pages")
    return {"route": CITIES[key]["route"], "title": title, "meta_description": desc, "h1": h1, "breadcrumbs": crumbs(key), "body_html": body, "faqs": faqs, "kind": "city", "city_key": key, "nav_active": "/areas/", "sources": sources}


def dist_line(key):
    c = CITIES[key]
    if not c["miles"]:
        return ""
    return f"<p class=\"note\">Straight-line distance from downtown Kissimmee: {c['miles']} miles (Census 2024 Gazetteer internal point). Drive time estimate: about {drive_estimate(c['miles'])} minutes on a weekday morning. County: {esc(c['county'])}. {('Population: ' + esc(c['pop']) + '.') if 'EDR' in c['pop'] else ''}</p>"


# ---------------------------------------------------------------------------
def kissimmee():
    k = "kissimmee"
    body = sec("What changes from one Kissimmee neighborhood to the next",
        cap("Kissimmee is two jurisdictions with a jagged line between them: the City of Kissimmee (population 87,442 in the 2025 EDR estimate) permits driveways and sidewalks through its Engineering Division, while Buenaventura Lakes, Bellalago, the Pleasant Hill corridor and everything east toward Narcoossee are unincorporated Osceola County under §22-50.6. The houses run from 1920s bungalows downtown to 2025 vacation rentals in Storey Lake, and the ground is Smyrna and Myakka fine sand with a foot of water under it every summer."),
        eyebrow="Kissimmee")
    body += sec("Neighborhoods and what we are usually asked for",
        table(["Area", "Built", "Jurisdiction", "Typical request"], [
            ("Downtown, Lakefront, historic district", "1900s–1960s", "City", "Replacing narrow concrete walks and drives on small lots; brick and paver walks to match the streetscape; live-oak root damage"),
            ("Kissimmee Bay, Remington, Eagle Lake", "1988–2005", "City / county mix", "Driveway replacement and widening, pool-deck pavers, sealing"),
            ("Bermuda Ave / Vine St corridors, Indian Ridge, Lindfields", "1970s–1990s", "City and county", "Cracked 4-in driveways poured on sand; sectional repair vs. replacement"),
            ("Buenaventura Lakes", "1978–1995", "County", "Driveway replacement, resurfacing; see the BVL page"),
            ("Bellalago, Isles of Bellalago", "2005–", "County; FirstService ARC", "Travertine and marble pool decks, paver driveway upgrades, ARC packets"),
            ("Tapestry, Storey Lake, Emerald Island, Windsor Hills", "2004–", "County; resort HOAs", "Pool decks between guests, paver sealing, repairs on rental driveways"),
            ("Osceola Pkwy / The Loop / John Young Pkwy", "1995–", "City", "Small commercial pads, sidewalks, dumpster pads"),
        ], caption="Build dates are approximate development periods for each area, not parcel-level data."))
    body += sec("Permits inside the city versus in the county",
        cap("Inside city limits: the Driveway / Sidewalk Construction application on the City's EnerGov portal, plan review at least two business days, permit issued at least two business days after payment, Engineering Division at 101 Church Street (407-518-2278). In unincorporated Osceola: a county driveway permit for any new or widened residential driveway, 24-foot maximum width, Building Office at 1 Courthouse Square (407-742-0200), residential plan review normally 3 to 5 days, Notice of Commencement at $5,000 or more.")
        + f"<p>Patios, slabs and pool decks follow the flatwork rules on each service page. The {tool('permit-finder')} checks your address against the city boundary; the {juris('city-of-kissimmee')} and {juris('osceola-county')} pages quote the sources. Since July 1, 2026, HB 803 exempts single-family work valued under $7,500 with a written request ({guide('hb-803-permit-exemption')}).</p>", cls="alt")
    body += sec("Ground, water and trees",
        f"<p>Kissimmee sits on the flatwoods: Smyrna fine sand (the single largest map unit in Osceola County at 188,635 acres), Myakka and Immokalee fine sands, all poorly drained with a wet-season water table about 12 inches down (USDA Soil Data Access). Around Lake Tohopekaliga, Shingle Creek and the older lakefront streets the soil grades into Basinger sand and muck where the water table is at the surface in June; slabs there are raised and drained or they sink. Live oaks along Emmett Street, Vine Street and the older subdivisions lift walks and driveways within a decade; {guide('tree-roots-driveways-central-florida')} covers root barriers and rerouting. Well-water irrigation is common outside the city utility area and leaves the orange streaks covered in {guide('rust-stains-irrigation-well-water')}.</p>")
    body += sec("HOA and ARC in Kissimmee communities",
        f"<p>Bellalago reviews every exterior change through an online ARC form on ConnectResident, with the committee meeting twice a month ({hoa('bellalago')}). Storey Lake, Tapestry, Windsor Hills and Emerald Island have management-company ARC processes we work with weekly but whose written criteria we have not published because we have not verified them; ask your manager for the current guidelines and use the {tool('hoa-packet-checklist')} to assemble the submission. Poinciana and Solivita, which carry Kissimmee mailing addresses, are on their own pages.</p>", cls="alt")
    body += sec(f"What work costs in Kissimmee ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "paver-driveway-concrete", "paver-pool-deck", "travertine-pool-deck", "concrete-patio", "paver-sealing", "concrete-removal"]) + "<p>Kissimmee is the reference market for the Cost Index; the Polk ridge runs a little lower on labor and the resort corridor a little higher on scheduling.</p>")
    body += sec("Services in Kissimmee", cards([
        (SERVICES["concrete-driveways"]["name"], "Replacement of 1980s drives, widening to 24 ft, aprons; city or county permit pulled by us.", SERVICES["concrete-driveways"]["route"], "Concrete driveways"),
        (SERVICES["paver-driveways"]["name"], "80 mm pavers on a 6-in base with a concrete apron at the street; HOA palettes matched.", SERVICES["paver-driveways"]["route"], "Paver driveways"),
        (SERVICES["paver-pool-decks"]["name"], "Overlays and rebuilds, travertine and marble, lanai drain channels.", SERVICES["paver-pool-decks"]["route"], "Pool decks"),
        (SERVICES["concrete-repair"]["name"], "Sunken garage panels, apron corners, trip hazards; lift, patch or replace.", SERVICES["concrete-repair"]["route"], "Repair"),
        (SERVICES["paver-sealing"]["name"], "Clean, re-sand, seal; rust and efflorescence handled first.", SERVICES["paver-sealing"]["route"], "Sealing"),
        (SERVICES["concrete-slabs"]["name"], "Shed, AC, generator and hot-tub pads raised above the water table.", SERVICES["concrete-slabs"]["route"], "Slabs and pads"),
    ]) + dist_line(k), cls="alt")
    faqs = [
        faq("Is my Kissimmee address in the city or the county?", "Downtown, the lakefront, the Vine Street and John Young Parkway corridors and most of the Osceola Parkway annexations are city; Buenaventura Lakes, Bellalago, the Pleasant Hill Road corridor, Poinciana and everything east toward Narcoossee are county. The permit finder checks your address against the Census boundary."),
        faq("How wide can my driveway be in Kissimmee?", "In unincorporated Osceola, 24 feet without a conditional use (§22-50.6). Inside the city the Engineering Division reviews width with the application. Bellalago and the resort HOAs may set tighter limits."),
        faq("Do you work in the vacation-rental communities?", "Yes; Storey Lake, Windsor Hills, Emerald Island and Tapestry are regular stops, and we schedule around guest turnovers with your property manager."),
        faq("What is the most common job in Kissimmee?", "Replacing a cracked 1980s or 1990s concrete driveway, either with new concrete or with pavers, followed by paver pool-deck overlays in the newer communities."),
        faq("How soon can you visit?", "Within two business days anywhere in Kissimmee."),
    ]
    return page(k, "Concrete & Pavers in Kissimmee, FL – Local Contractor Guide", "Concrete and paver work in Kissimmee by neighborhood: city vs. county permits, Smyrna and Myakka sand with a 12-inch water table, Bellalago and resort HOA reviews, current costs, live-oak and rust issues.", "Concrete and pavers in Kissimmee, FL: neighborhoods, permits, soil and costs", body, faqs, ["kissimmee-driveway", "osceola-22-50-6", "osceola-faq", "sda", "edr", "bellalago", "hb803"])


# ---------------------------------------------------------------------------
def st_cloud():
    k = "st-cloud"
    body = sec("A 1909 town with 2026 subdivisions",
        cap("St. Cloud (population 76,970, 2025 EDR estimate) permits patios and decks through its own Building Department at 1300 9th Street and sends driveway and sidewalk pavers to Public Works instead of the permit counter. Downtown's brick streets and 1910s–1950s cottages sit on small lots with mature oaks; the Nova Road and Canoe Creek corridors added 1980s–2000s ranches; Narcoossee, Sunbridge and Weslyn Park are adding thousands of new homes with builder-grade paver driveways that will need sealing and repair in five years."),
        eyebrow="St. Cloud")
    body += sec("Areas and what we do in each",
        table(["Area", "Built", "Jurisdiction", "Typical work"], [
            ("Downtown and the East Lake Toho lakefront", "1909–1960", "City", "Narrow drives and walks replaced in concrete or brick-look pavers, root damage, lakefront lots on Basinger sand needing raised slabs"),
            ("Nova Rd, Canoe Creek Rd, Old Hickory Tree Rd", "1980–2005", "City and unincorporated", "Driveway replacement, RV and boat pads on larger lots, septic drainfields to avoid"),
            ("Anthem Park, Hanover Lakes, Twin Lakes (55+), Canoe Creek Estates", "2005–2022", "City / county", "Pool-deck pavers, driveway widening, sealing"),
            ("Narcoossee Rd corridor, Sunbridge, Weslyn Park", "2015–2026", "Unincorporated Osceola (confirm by address)", "Builder paver driveways: sealing, edge restraint, lift-and-relay; new patios"),
            ("Rural lots south and east (Holopaw side)", "any", "Unincorporated", "Long concrete or gravel driveways, workshop slabs, pads for equipment"),
        ], caption="Development periods are approximate. Harmony and the Narcoossee communities have their own page."))
    body += sec("Permits in St. Cloud",
        cap("The city's Permit Information page lists patios, decks, screen enclosures and sheds as permit-required and lists 'pavers for driveways/sidewalks (refer to Public Works)' and 'driveway reseal for single-family/duplex (existing asphalt only)' among items that do not need a building permit. Any work in the right-of-way needs Public Works and Engineering approval. Payments are cashless since January 1, 2025. Building Department: 407-957-7300; portal: stcloudflpermits.selectpaytoday.com.")
        + f"<p>St. Cloud also adopted the HB 803 exemption for single-family work under $7,500 effective July 1, 2026, with a written exemption request and the usual exclusions (structural, electrical, plumbing, mechanical, gas, flood zones). Outside the city line the county rules apply, including the 24-foot driveway width in §22-50.6. Pages: {juris('city-of-st-cloud')}, {juris('osceola-county')}, {tool('permit-finder')}, {guide('hb-803-permit-exemption')}.</p>", cls="alt")
    body += sec("Ground and water",
        f"<p>Most of St. Cloud is Smyrna and Myakka fine sand; the lakefront and the lower ground toward Alligator Lake and the Narcoossee flats include EauGallie and Basinger sands with a water table at or near the surface in summer (USDA Soil Data Access, FL097). Slabs on those units are built up on compacted fill with a swale to carry water away. Rural lots use septic systems; a driveway or pad over a drainfield compacts the soil and crushes the pipe, so we pull the county septic record and stay clear ({guide('septic-drainfield-concrete-driveway')}). Well irrigation is common outside the city utility area and rust-stains light pavers within a season ({guide('rust-stains-irrigation-well-water')}).</p>")
    body += sec(f"Costs in St. Cloud ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "paver-driveway-concrete", "paver-pool-deck", "concrete-slab-pad", "paver-sealing"]) + f"<p>St. Cloud prices track the Kissimmee index. Long rural driveways are quoted by the foot and by truck access; the {tool('concrete-paver-calculator')} gives a first number.</p>", cls="alt")
    body += sec("Services in St. Cloud", cards([
        ("Concrete driveways", "Replacement on the 1980s–2000s streets, long drives and turnarounds on rural lots, aprons per the city or county detail.", city_service_route(k, "concrete-driveways"), "Driveways in St. Cloud"),
        ("Slabs and pads", "RV, boat and workshop slabs on the larger lots; shed and generator pads raised above the water table.", city_service_route(k, "concrete-slabs"), "Slabs in St. Cloud"),
        ("Paver pool decks", "Overlays on 2000s decks, travertine on lakefront homes, lanai drains.", city_service_route(k, "paver-pool-decks"), "Pool decks in St. Cloud"),
        ("Paver sealing", "First seal on builder driveways in Narcoossee and Sunbridge; re-seal on older ones.", city_service_route(k, "paver-sealing"), "Sealing in St. Cloud"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Do driveway pavers need a permit in St. Cloud?", "Not a building permit; the city refers driveway and sidewalk pavers to Public Works, and work in the right-of-way needs Public Works approval. Outside the city line, the county driveway permit applies."),
        faq("Do I need a permit for a patio in St. Cloud?", "Yes; patios and decks are on the city's permit list. HB 803's $7,500 exemption may apply to a small slab with a written request."),
        faq("Is Sunbridge or Weslyn Park in the city?", "The Narcoossee-corridor communities straddle the city line and unincorporated Osceola. The permit finder checks the address; when in doubt we call the Building Department before quoting."),
        faq("Can you pour a driveway over my septic drainfield?", "No. We locate it from the county record and route around it."),
        faq("How far is St. Cloud from your usual base?", "About 8.5 miles from downtown Kissimmee; site visits within two business days."),
    ]
    return page(k, "Concrete & Pavers in St. Cloud, FL – Local Contractor Guide", "Concrete and paver work in St. Cloud: city permit list (patios yes, driveway pavers to Public Works), HB 803, downtown oaks and lakefront Basinger sand, Narcoossee builder driveways, septic lots, costs.", "Concrete and pavers in St. Cloud, FL: permits, ground and what we build", body, faqs, ["stcloud-permits", "osceola-22-50-6", "sda", "edr", "hb803"])


# ---------------------------------------------------------------------------
def celebration():
    k = "celebration"
    body = sec("In Celebration the ARC comes first",
        cap("Celebration is unincorporated Osceola County for permits and the Celebration Residential Owners Association for everything you can see. The Architectural Review Committee meets on the third Monday of each month; the Design Guidelines and applications live on the Front Porch portal for owners and at Town Hall (851 Celebration Avenue, 407-566-1200 ext. 2206). Most homes from the 1996–2010 villages have rear alley garages with short paver aprons and front walks in the streetscape's brick and paver palette."),
        eyebrow="Celebration")
    body += sec("Villages and typical requests",
        table(["Village", "Built", "Typical work"], [
            ("Celebration Village, Lake Evalyn, West Village", "1996–2001", "Replacing settled builder pavers on alley aprons and front walks; sealing; matching the original blends"),
            ("North Village, South Village, East Village", "1999–2006", "Paver driveway rebuilds, pool-deck overlays in travertine, walkway repairs at live oaks"),
            ("Artisan Park", "2004–2008", "Pool decks and lanai extensions on smaller lots"),
            ("Island Village", "2020–2026", "New patios and pool decks to match builder pavers; first sealing"),
        ], caption="Village dates are approximate development periods."))
    body += sec("What the CROA reviews and how to submit",
        cap("Any exterior change visible from a street, alley or neighbor needs an ARC application with the Design Guidelines' required attachments: site plan or survey markup, product name, color, pattern and edge detail, and for pavers a physical sample. Applications are reviewed at the monthly meeting; a complete packet submitted before the agenda deadline is decided that month. Each village has its own accents and approved palettes, and joint-sand color has been a reason for rejection.")
        + f"<p>We prepare the packet with you and attend to questions if the committee has any. The published Design Guidelines we could verify are topic-specific (fans, gutters, street trees, signs); the paver and driveway section is on the owner portal, so ask Town Hall or your CROA login for the current version before choosing material. The {tool('hoa-packet-checklist')} lists what to gather; the {hoa('celebration')} page has the contacts.</p>", cls="alt")
    body += sec("Permits and ground",
        f"<p>Permits are Osceola County's: a county driveway permit for a new or widened driveway (§22-50.6, 24 feet maximum) and the Building Office for anything structural, at 1 Courthouse Square (407-742-0200). Alley aprons touch the community's private streets, which the CDD maintains, so the ARC application doubles as the access approval. The ground is Smyrna and Myakka fine sand drained by the community's engineered lakes and swales; base and drainage rules are the same as elsewhere in the county, and the community's stormwater system is where lanai drains are tied. Pages: {juris('osceola-county')}, {tool('permit-finder')}.</p>")
    body += sec(f"Costs in Celebration ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-driveway-concrete", "paver-driveway-premium", "paver-pool-deck", "travertine-pool-deck", "paver-walkway", "paver-sealing", "paver-repair"]) + "<p>Celebration jobs run toward the top of each range: matching discontinued blends, alley access for trucks, and borders and bands specified by the guidelines.</p>", cls="alt")
    body += sec("Services in Celebration", cards([
        ("Paver driveways", "Alley aprons and front-loaded drives rebuilt on a 6-in base in approved blends.", city_service_route(k, "paver-driveways"), "Driveways in Celebration"),
        ("Paver pool decks", "Travertine and paver overlays on 2000s decks inside screened lanais.", city_service_route(k, "paver-pool-decks"), "Pool decks in Celebration"),
        ("Walkways and steps", "Front walks in the streetscape palette; entry steps rebuilt.", city_service_route(k, "paver-walkways-steps"), "Walkways in Celebration"),
        ("Sealing and repair", "First and repeat sealing, lift-and-relay at oaks and downspouts, concrete repair on garage slabs.", city_service_route(k, "paver-sealing"), "Sealing in Celebration"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Do I need ARC approval to reseal my pavers?", "A like-for-like clear seal is maintenance in most communities, but Celebration reviews finish changes; a wet-look sealer on a matte driveway is a change. Ask Town Hall before switching products."),
        faq("Can I widen my driveway in Celebration?", "Only with ARC approval and, for the county, within the 24-foot limit. Front-loaded lots have little room; alley lots are limited by the garage setback."),
        faq("Who maintains the alleys?", "The community (CDD) maintains the private streets and alleys; the paver apron on your lot is yours. ARC approval covers the connection."),
        faq("How long does approval take?", "The committee meets monthly, on the third Monday; a complete packet before the deadline is heard that month. Allow four to six weeks from submission to work."),
        faq("Do you match the original builder pavers?", "We identify the blend and size and source the current equivalent from the manufacturer; where the line is gone, we borrow units from a hidden area for the visible repair."),
    ]
    return page(k, "Pavers & Concrete in Celebration, FL – ARC, Permits, Costs", "Paver and concrete work in Celebration, FL: CROA Architectural Review Committee (third Monday), village palettes, alley aprons, Osceola County permits, travertine pool decks, costs per sq ft.", "Pavers and concrete in Celebration, FL: ARC first, then the county permit", body, faqs, ["celebration", "osceola-22-50-6", "osceola-faq", "sda"])


# ---------------------------------------------------------------------------
def poinciana():
    k = "poinciana"
    body = sec("Two counties and one Design Control Board",
        cap("Poinciana's 47,000 acres straddle the Osceola–Polk line, so the permit office depends on which village your lot is in, but the Association of Poinciana Villages' Design Control Board applies everywhere: no driveway, patio, paved area or wall may be started without prior written DCB approval, driveways are concrete, asphalt or brick pavers, walks beside the house are capped at 2 feet wide, and an application not acted on within 30 days is deemed disapproved (DCB Criteria 6.1 and 9.1.1). Solivita, the 55+ community on the Polk side, has its own ARC and requires replacement driveways in the builder's original style."),
        eyebrow="Poinciana")
    body += sec("Villages, ages and what fails",
        table(["Area", "Built", "County", "What we see"], [
            ("Villages 1–2 (Marigold Ave, Pleasant Hill side)", "1972–1990", "Osceola", "Original 4-in driveways cracked into panels and stepped at the garage; walks lifted by oaks"),
            ("Villages 3–6", "1985–2005", "Osceola / Polk", "Driveway replacement, widening within DCB limits, patios"),
            ("Villages 7–9 (Cypress Pkwy, Poinciana Pkwy side)", "2000–2020", "Polk / Osceola", "Paver driveway upgrades, pool-deck overlays, sealing"),
            ("Solivita", "2000–2020", "Polk", "Driveway extensions and paver conversions through the Solivita ARC; patios, screen-room slabs"),
            ("Cypress Woods", "1980s", "Osceola", "Sheds are prohibited by covenant; pads and patios only"),
        ], caption="Village boundaries and dates are approximate; APV's office at 401 Walnut Street (863-427-0900) confirms village and county for a lot."))
    body += sec("Which permit office covers your lot?",
        cap("Osceola villages use the County Building Office at 1 Courthouse Square (407-742-0200): county driveway permit for new or widened drives, 24-foot maximum. Polk villages use the Polk County Building Division (863-534-6080, Bartow or the Northeast Government Center in Lake Alfred): permits for slabs supporting structures, within setbacks or in the right-of-way, and a recorded Paver Release Form for pavers in the right-of-way.")
        + f"<p>The {tool('permit-finder')} shows the county for an address; the {juris('osceola-county')} and {juris('polk-county')} pages quote each office. The DCB application goes in first: {hoa('poinciana-apv')}; Solivita residents use the Solivita ARC form ({hoa('solivita')}); the {tool('hoa-packet-checklist')} covers both.</p>", cls="alt")
    body += sec("Ground",
        f"<p>The Osceola side is Smyrna and Myakka fine sand with a wet-season water table around 12 inches; the western villages climb onto the edge of the Polk ridge where Candler and Astatula sands drain fast and need to be wetted to compact. Poinciana's canals and the low ground near Lake Marion and Reedy Creek include Basinger and ponded soils where slabs must be raised. The two soil types are compared in {guide('paver-base-flatwoods-vs-ridge')}. Well irrigation is common and rust-stains driveways ({guide('rust-stains-irrigation-well-water')}).</p>")
    body += sec(f"Costs in Poinciana ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-removal", "concrete-patio", "paver-driveway-concrete", "concrete-repair", "paver-sealing"]) + "<p>Poinciana's older villages are mostly straightforward replacement jobs at the low end of each range; DCB and Solivita submissions add a few weeks but not cost.</p>", cls="alt")
    body += sec("Services in Poinciana", cards([
        ("Concrete driveways", "Replacing 1970s–90s slabs; concrete is the DCB's default material.", city_service_route(k, "concrete-driveways"), "Driveways in Poinciana"),
        ("Concrete patios", "Screen-room and lanai slabs, backyard patios with DCB approval.", city_service_route(k, "concrete-patios"), "Patios in Poinciana"),
        ("Concrete repair", "Garage-edge steps, apron corners, walk trip hazards.", city_service_route(k, "concrete-repair"), "Repair in Poinciana"),
        ("Paver driveways", "Brick or concrete pavers where the DCB approves the change.", city_service_route(k, "paver-driveways"), "Paver driveways in Poinciana"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Do I need APV approval to replace my driveway with the same concrete?", "Yes. The DCB criteria require prior written approval for any driveway or paved area; a like-for-like replacement is usually quick, but it still needs the application."),
        faq("What happens if the DCB doesn't answer?", "Under the criteria, an application not acted on within 30 days of submittal is deemed disapproved; you resubmit or follow up rather than start work."),
        faq("Which county issues my permit?", "Depends on the village. The permit finder checks the address; APV's office can also tell you. Solivita is in Polk County."),
        faq("Can I have a paver driveway in Solivita?", "Only through the Solivita ARC, which requires replacement driveways in the original builder's style and materials and reviews extensions and modifications case by case."),
        faq("Are sheds allowed?", "In most villages, on a concrete pad, no taller than 8 feet, colored to match the house, with DCB approval. Cypress Woods prohibits them by covenant."),
    ]
    return page(k, "Concrete & Pavers in Poinciana, FL – APV DCB, Permits, Costs", "Concrete and paver work in Poinciana: APV Design Control Board rules (9.1.1 driveways, 2-ft walks, 30-day deemed denial), Osceola vs. Polk permits by village, Solivita ARC, 1970s driveway replacement.", "Concrete and pavers in Poinciana, FL: DCB approval, then the right county", body, faqs, ["apv", "solivita", "osceola-22-50-6", "polk-faq", "polk-paver-release", "sda"])


# ---------------------------------------------------------------------------
def bvl():
    k = "buenaventura-lakes"
    body = sec("Forty years on, most BVL driveways are due",
        cap("Buenaventura Lakes was platted and built by Landstar Homes from the late 1970s through the early 1990s on unincorporated Osceola County land between Boggy Creek Road and Simpson Road. The driveways were 4-inch slabs on unprepared sand, and after 35 to 45 wet seasons most have cracked into panels with a step at the garage. Replacement in concrete or pavers goes through the county driveway permit (§22-50.6, 24-foot maximum), and there is no HOA on most streets."),
        eyebrow="Buenaventura Lakes")
    body += sec("What we find under a BVL driveway",
        f"""<p>When the old slab comes out we usually find no base at all: the concrete was poured on graded Smyrna or Myakka fine sand, which holds a water table about 12 inches down in summer. Forty years of that cycle, plus a downspout aimed at the slab edge, is the whole story of the cracked panel at the garage and the settled apron. The good news is that the sand itself is fine to build on once it is proof-rolled and a 4-inch compacted limerock base goes in; we rarely need imported fill in BVL except where a lot backs onto one of the retention lakes. The step-by-step of a BVL replacement, with photos of what comes out, is in {guide('buenaventura-lakes-driveway-replacement')}.</p>
<p>Two other BVL specifics: many lots have live oaks planted in the 1980s that are now lifting walks and the driveway edge, and many homes have been widened or had a second driveway ribbon added without a permit. We check the total width against the county's 24-foot rule before we quote a widening, and we route walks around the oaks or install a root barrier ({guide('tree-roots-driveways-central-florida')}).</p>""")
    body += sec("Permits in BVL",
        cap("Unincorporated Osceola County: a county driveway permit is required for construction or widening of a residential driveway, width is capped at 24 feet without a conditional use, and the Building Office at 1 Courthouse Square (407-742-0200) reviews residential applications in about 3 to 5 days. Jobs of $5,000 or more need a recorded Notice of Commencement. Patios and pads outside setbacks are flatwork; HB 803's $7,500 exemption may apply with a written request.")
        + f"<p>Details: {juris('osceola-county')}; the {tool('permit-finder')} confirms the county for the address (BVL is entirely unincorporated, but the Kissimmee city line runs along its western edge).</p>", cls="alt")
    body += sec("Concrete or pavers for a BVL replacement?",
        f"<p>Most BVL owners replace in concrete: it costs less, matches the street, and there is no HOA pushing pavers. A 4-inch broom-finish drive with fiber and edge rebar on a real base will outlast the original by a wide margin. Pavers make sense when the owner wants the look, plans to widen later, or has a drive that will keep seeing utility work; the trade-offs are in {compare('concrete-vs-pavers')}. Resurfacing is rarely the right answer here because the slabs are moving, not just worn ({compare('resurface-vs-replace')}).</p>")
    body += sec(f"Costs in BVL ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-removal", "paver-driveway-concrete", "concrete-repair", "concrete-resurfacing", "concrete-sidewalk"]) + "<p>A typical BVL two-car driveway is 18 by 22 to 20 by 24 feet (400 to 480 square feet): removal $800 to $1,900, new concrete $3,400 to $6,500, pavers $5,600 to $10,600.</p>", cls="alt")
    body += sec("Services in Buenaventura Lakes", cards([
        ("Concrete driveways", "Tear-out and replacement on a compacted base; widening within 24 ft.", city_service_route(k, "concrete-driveways"), "Driveways in BVL"),
        ("Concrete repair", "Single-panel replacement at the garage when the rest of the drive is sound.", city_service_route(k, "concrete-repair"), "Repair in BVL"),
        ("Resurfacing", "For the minority of slabs that are worn but not moving.", city_service_route(k, "concrete-resurfacing"), "Resurfacing in BVL"),
        ("Paver driveways", "Pavers over a 6-in base where the look is wanted.", city_service_route(k, "paver-driveways"), "Paver driveways in BVL"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Why is every driveway on my street cracked the same way?", "Same builder, same year, same 4-inch slab on sand with no base. The garage-edge step and the apron diagonal are what that construction does after 40 wet seasons."),
        faq("Can I just replace the cracked panel?", "If the rest of the drive is sound, yes, and we price it. In BVL the rest is usually on the same clock, so we also price the full replacement."),
        faq("Is BVL in the city of Kissimmee?", "No; it is unincorporated Osceola County, so the county driveway permit and the 24-foot width rule apply."),
        faq("Is there an HOA?", "Most of BVL has no HOA; a few later sections do. We check before quoting."),
        faq("How long does a BVL driveway replacement take?", "Two to three days on site, then seven days before parking on it."),
    ]
    return page(k, "Concrete Driveways in Buenaventura Lakes, FL – Replacement", "Concrete and paver driveway replacement in Buenaventura Lakes: what is under a 1980s Landstar-era slab, Osceola County driveway permit and 24-ft rule, oak roots, concrete vs. pavers, costs for a two-car drive.", "Concrete and pavers in Buenaventura Lakes: replacing the 1980s driveways", body, faqs, ["osceola-22-50-6", "osceola-faq", "sda", "hb803"])


# ---------------------------------------------------------------------------
def four_corners():
    k = "four-corners"
    body = sec("Vacation homes across four counties on one ridge",
        cap("Four Corners is where Osceola, Polk, Lake and Orange counties meet along US-27 and US-192, and almost every house is a vacation rental in a gated resort community: Windsor Hills, Windsor Palms, Emerald Island and Windsor at Westside on the Osceola side; Solterra, Solara, Bella Vida, Calabay Parc, Tuscan Ridge and Paradise Palms in Polk; Cagan Crossings toward Lake. The work is pool decks, paver sealing and driveway repair, scheduled between guests through a property manager, and the ground is the dry Candler sand of the ridge, not the wet flatwoods sand of Kissimmee."),
        eyebrow="Four Corners")
    body += sec("Which county, which HOA",
        table(["Community", "County", "Built", "ARC / management notes"], [
            ("Windsor Hills, Windsor Palms, Emerald Island, Windsor at Westside", "Osceola (34747)", "2001–2015", "Management-company ARC; written criteria not yet verified by us; county driveway permit for widening"),
            ("Solterra Resort", "Polk (33837)", "2013–", "Verified guidelines: three-car driveway max, no added walking area, no painted concrete, COI may be required; Artemis 407-705-2190"),
            ("Solara, Bella Vida, Paradise Palms, Calabay Parc, Tuscan Ridge", "Polk", "2004–2022", "Management ARC; Polk permit rules; Paver Release Form for pavers in the right-of-way"),
            ("Cagan Crossings, Citrus Ridge", "Lake", "2000s–", "Outside our county coverage for permits; we take pool-deck and sealing calls with the manager's approval"),
        ], caption="Build dates are approximate development periods; the permit finder checks the county for an address."))
    body += sec("How rental communities change the job",
        f"""<p>Three things. Scheduling: pool decks and sealing happen in the gap between check-out and check-in, usually two to four days, so we stage material the day before and finish sealing on a dry morning. Approval: every visible change goes through the community's ARC, and Solterra's guidelines let the board require the installer's insurance certificate naming the association before work starts. Wear: rental pool decks see more foot traffic, more chemicals and more pressure-washing than a family home, so we specify sealers with anti-slip additive and polymeric sand rated for frequent cleaning. The owner's guide is {guide('vacation-rental-owner-hardscape-guide')}; Solterra's rules are on {hoa('solterra')}.</p>""", cls="alt")
    body += sec("Ridge sand turns the base problem around",
        f"<p>Most of Four Corners sits on Candler sand (97,496 acres in Polk County's survey) and Astatula sand: deep, excessively drained, and unable to compact when dry. Base placed on dry ridge sand in an August afternoon reads compacted and settles the first time it gets wet. We wet the subgrade and the limerock, compact in lifts, and probe. On the Osceola side near Reedy Creek the soil goes back to flatwoods sand with a high water table. The two are compared in {guide('paver-base-flatwoods-vs-ridge')}.</p>")
    body += sec(f"Costs in Four Corners ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-pool-deck", "travertine-pool-deck", "paver-sealing", "paver-repair", "paver-driveway-concrete", "concrete-repair"]) + "<p>Resort jobs price toward the top of each range because of gate access, turnover scheduling and ARC requirements; sealing several decks in one community on the same day brings the per-deck price down.</p>", cls="alt")
    body += sec("Services in Four Corners", cards([
        ("Paver pool decks", "Overlays and rebuilds between guests; travertine on premium rentals.", city_service_route(k, "paver-pool-decks"), "Pool decks in Four Corners"),
        ("Paver sealing", "Anti-slip sealers and polymeric re-sanding on rental decks and drives.", city_service_route(k, "paver-sealing"), "Sealing in Four Corners"),
        ("Paver driveways", "Rebuilds of settled builder driveways on ridge sand.", city_service_route(k, "paver-driveways"), "Driveways in Four Corners"),
        ("Concrete repair", "Garage-edge and apron repairs on 2000s slabs.", city_service_route(k, "concrete-repair"), "Repair in Four Corners"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Can you work between guests?", "Yes. Pool-deck overlays take two to four days and sealing one dry day; we coordinate dates with the property manager and stage material the day before."),
        faq("Which county is my rental in?", "Windsor Hills, Windsor Palms, Emerald Island and Windsor at Westside are Osceola; Solterra, Solara, Bella Vida and Calabay Parc are Polk; Cagan Crossings is Lake. The permit finder checks the address."),
        faq("Does the HOA need to approve a pool-deck overlay?", "Every resort community here reviews visible changes. Solterra's written guidelines are on our HOA page; for the others we work from the management company's current form."),
        faq("Why did the builder's driveway settle?", "Ridge sand compacts only when wet; builders working dry in summer left base that settled the first rainy season. Rebuilding the base fixes it."),
        faq("Do you do the whole community's decks?", "We quote group sealing and repair for multiple homes with one manager; it lowers the per-home price."),
    ]
    return page(k, "Pool Decks & Pavers in Four Corners, FL – Rentals, HOAs, Costs", "Paver pool decks, sealing, driveway repair for vacation rentals in Four Corners: Windsor Hills, Solterra, Solara and Emerald Island by county, ARC and insurance rules, ridge sand base, turnover scheduling.", "Pool decks, sealing and driveways in Four Corners, FL: rentals across four counties", body, faqs, ["solterra", "polk-faq", "polk-paver-release", "osceola-22-50-6", "sda"])


# ---------------------------------------------------------------------------
def champions_gate():
    k = "champions-gate"
    body = sec("Resort rules and Osceola permits in ChampionsGate",
        cap("ChampionsGate is an Osceola County resort community off I-4 exit 58 with a Davenport mailing address: vacation-rental neighborhoods (The Retreat and the townhome sections) and primary-home sections (the Country Club, The Vistas) built from 2001 onward around the Omni resort and its golf courses. Permits go through Osceola County (county driveway permit, 24-foot width rule); every visible exterior change goes through the community's architectural review. The ground is ridge sand that needs wetting to compact."),
        eyebrow="ChampionsGate")
    body += sec("What we do in ChampionsGate",
        f"""<p>Pool-deck overlays in travertine and paver on rental homes between guests; sealing and re-sanding of the builder's paver driveways, which are ten to fifteen years old in the earlier sections and settling at the garage; lift-and-relay of sunken areas; repair of concrete garage aprons and sidewalk panels; and, in the Country Club section, patio extensions, seat walls and summer-kitchen structures. The community's approved palettes come from the major manufacturers' catalogs, and matching the original blend matters more here than anywhere because of the uniform streetscape.</p>
<p>Turnover scheduling and manager coordination are covered in {guide('vacation-rental-owner-hardscape-guide')}. We have not published ChampionsGate's written architectural criteria because we have not verified them; the management company issues the current form, and the {tool('hoa-packet-checklist')} lists what to gather.</p>""")
    body += sec("Permits", cap("Osceola County: county driveway permit for a new or widened driveway, 24 feet maximum (§22-50.6), Building Office at 1 Courthouse Square (407-742-0200), 3- to 5-day residential plan review, Notice of Commencement at $5,000 or more. Pool-deck overlays and patios outside setbacks are flatwork; the community's private streets and gates make the ARC approval the practical gate.") + f"<p>{juris('osceola-county')}; {tool('permit-finder')} (ChampionsGate carries a Davenport ZIP but is in Osceola).</p>", cls="alt")
    body += sec("Ground", f"<p>ChampionsGate sits on the northern edge of the Lake Wales Ridge: Candler and Astatula sands that drain fast and compact only when wet. Builder driveways placed dry in summer settle the first wet season, which is the repair we do most here. Toward Reedy Creek the soil returns to flatwoods sand with a high water table. Comparison: {guide('paver-base-flatwoods-vs-ridge')}.</p>")
    body += sec(f"Costs in ChampionsGate ({COST_INDEX_RELEASE['label']})", cost_rows(["paver-pool-deck", "travertine-pool-deck", "paver-sealing", "paver-repair", "paver-driveway-concrete", "concrete-repair"]) + "<p>Gate access and turnover windows put resort jobs toward the top of each range; grouping several homes for sealing brings it down.</p>", cls="alt")
    body += sec("Services in ChampionsGate", cards([
        ("Paver pool decks", "Overlays and travertine decks between guests.", city_service_route(k, "paver-pool-decks"), "Pool decks in ChampionsGate"),
        ("Paver sealing", "Anti-slip sealers, polymeric re-sanding on rental decks and drives.", city_service_route(k, "paver-sealing"), "Sealing in ChampionsGate"),
        ("Paver driveways", "Rebuilds and widening of settled builder driveways.", city_service_route(k, "paver-driveways"), "Driveways in ChampionsGate"),
        ("Concrete repair", "Aprons, garage edges, sidewalk panels.", city_service_route(k, "concrete-repair"), "Repair in ChampionsGate"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Is ChampionsGate in Polk or Osceola County?", "Osceola, despite the Davenport ZIP. Permits go through Osceola County."),
        faq("Can you seal several rental driveways in one visit?", "Yes, and it lowers the per-home price; we coordinate with the manager for gate access and turnover dates."),
        faq("Why are the builder's pavers sinking?", "Ridge sand compacts only when wet; base placed dry settles after the first rainy season. A lift-and-relay on a rebuilt base fixes it."),
        faq("Does the HOA review a pool-deck overlay?", "Yes for anything visible; submit through the management company's ARC form. We prepare the packet."),
    ]
    return page(k, "Pool Decks & Pavers in ChampionsGate, FL – Osceola Permits", "Paver pool decks, sealing and driveway repair in ChampionsGate: Osceola County permits despite the Davenport ZIP, resort ARC review, ridge sand that settles when placed dry, turnover scheduling, costs.", "Pavers, pool decks and repairs in ChampionsGate, FL", body, faqs, ["osceola-22-50-6", "osceola-faq", "sda"])


# ---------------------------------------------------------------------------
def reunion():
    k = "reunion"
    body = sec("Three management companies and one county",
        cap("Reunion Resort is unincorporated Osceola County (Kissimmee 34747) built from 2004 around three golf courses, and its architectural review runs through three management companies: Artemis Lifestyles for single-family homes, Seven Eagles, Eagle Trace, Carriage Pointe, Centre Court Ridge, Heritage Crossing, Spectrum+ and the Grande (407-705-2190); Greystone for Villas North and South (407-645-4945); Southwest Property Management for the Terraces (407-656-1081). Travertine and marble pool decks, paver driveways and sealing are the work; the county driveway permit applies to any widening."),
        eyebrow="Reunion")
    body += sec("What Reunion owners ask for",
        f"""<p>Travertine on the pool deck is the request we hear most, from owners upgrading a 2005-era paver deck on a rental villa and from primary-home owners in the estate sections. Marble and large-format porcelain on the newer contemporary homes; paver driveway rebuilds where the original base settled; sealing and re-sanding on a two- to three-year cycle for rental traffic; seat walls, fire features and summer kitchens on the golf-course lots. Encore Resort at Reunion, the newer vacation-home section, has its own management and the same county rules.</p>
<p>Scheduling around guests is standard here: {guide('vacation-rental-owner-hardscape-guide')}. We have not published Reunion's written ARC criteria because we have not verified them; the management companies issue the forms and the {tool('hoa-packet-checklist')} lists the attachments they typically want.</p>""")
    body += sec("Permits and ground", cap("Osceola County Building Office (1 Courthouse Square, 407-742-0200): county driveway permit for new or widened driveways with the 24-foot limit, 3- to 5-day residential plan review, Notice of Commencement at $5,000 or more. Pool-deck overlays and patios are flatwork. Reunion sits on the ridge's Candler sand, which needs wetting to compact, with flatwoods sand toward the creek side.") + f"<p>{juris('osceola-county')}; {tool('permit-finder')}; {guide('paver-base-flatwoods-vs-ridge')}.</p>", cls="alt")
    body += sec(f"Costs in Reunion ({COST_INDEX_RELEASE['label']})", cost_rows(["travertine-pool-deck", "paver-pool-deck", "paver-driveway-premium", "paver-driveway-concrete", "paver-sealing", "paver-repair"]) + "<p>Reunion work runs at the premium end: travertine and marble material, resort access and finishes matched to the community palette.</p>")
    body += sec("Services in Reunion", cards([
        ("Travertine", "Pool decks and lanais in tumbled travertine with bullnose coping.", city_service_route(k, "paver-travertine"), "Travertine in Reunion"),
        ("Paver pool decks", "Overlays on 2005-era decks, drain channels in the lanai.", city_service_route(k, "paver-pool-decks"), "Pool decks in Reunion"),
        ("Paver sealing", "Rental-cycle sealing with anti-slip additive.", city_service_route(k, "paver-sealing"), "Sealing in Reunion"),
        ("Paver driveways", "Rebuilds in premium lines matched to the streetscape.", city_service_route(k, "paver-driveways"), "Driveways in Reunion"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Who approves a pool-deck change in Reunion?", "The management company for your section: Artemis for single-family and most condo sections, Greystone for the Villas, Southwest for the Terraces. We submit the packet to the right one."),
        faq("Is a permit needed for a travertine overlay?", "An overlay on an existing deck outside setbacks is flatwork in Osceola County; a deck tied to the screen footer or the pool structure is confirmed with the Building Office first."),
        faq("Can you work while the house is rented?", "Between bookings. Overlays take two to four days; we stage material the day before."),
        faq("Travertine or marble?", "Both stay cool; marble is lighter and costs more; travertine has more natural variation. Samples on site decide it."),
    ]
    return page(k, "Travertine Pool Decks & Pavers in Reunion, FL – Osceola", "Travertine and marble pool decks, paver driveways and sealing in Reunion Resort: Artemis, Greystone and Southwest management contacts, Osceola County permits, ridge sand base, rental scheduling, costs.", "Travertine, pavers and pool decks in Reunion, FL", body, faqs, ["osceola-22-50-6", "osceola-faq", "sda"])


# ---------------------------------------------------------------------------
def davenport():
    k = "davenport"
    body = sec("A small city inside a big county, on dry sand",
        cap("The City of Davenport (population 14,031 in the 2025 EDR estimate) is a compact historic town on US-17/92; most of what carries a Davenport address is unincorporated Polk County: Solterra Resort, Providence, Loughman, the US-27 corridor and the resort subdivisions toward Four Corners. Polk County permits slabs that support structures, sit within setbacks or lie in the right-of-way, and records a Paver Release Form for pavers in the right-of-way. The soil is Candler sand, deep and dry, which compacts only when wet."),
        eyebrow="Davenport")
    body += sec("Areas and typical work",
        table(["Area", "Built", "Jurisdiction", "Typical work"], [
            ("Historic Davenport (Bay St, Lake Play area)", "1885–1960", "City of Davenport", "Replacing narrow drives and walks on small lots; root damage; confirm the city's own building rules"),
            ("Providence, Champions Reserve, Astonia, Cascades", "2005–2026", "Polk County", "Paver driveway upgrades, pool-deck pavers, patios; management-company ARC"),
            ("Solterra Resort, Solara, Bella Vida", "2013–", "Polk County", "Rental pool decks and sealing; Solterra's verified guidelines"),
            ("Loughman, Holly Hill Rd, Ronald Reagan Pkwy corridor", "1990s–2020s", "Polk County", "Driveway replacement, RV and boat pads on larger lots"),
        ], caption="Development periods are approximate. The City of Davenport's building department was not verified for this page; confirm with the city for addresses inside the limits."))
    body += sec("Permits in Polk County",
        cap("Polk County's Building Division FAQ: permits are required for 'concrete slabs adjacent to a principal or accessory structure, intended for support of a structure, elevated slabs, sidewalks and portions of driveways in the right of way or within the minimum setbacks'; all slabs must meet setbacks except sidewalks and driveways; pavers within setbacks or adjacent to structures must meet the codes. For pavers in the right-of-way the owner records a notarized Concrete Driveway Paver Release Form (PD BLD 40) accepting maintenance and indemnifying the county. Offices: 330 W. Church Street, Bartow, and the Northeast Government Center, 200 Government Center Blvd, Lake Alfred; (863) 534-6080.")
        + f"<p>A free-standing patio or pad outside the setbacks is not permitted separately in the county; a driveway apron in the right-of-way is. {juris('polk-county')} quotes the sources; the {tool('permit-finder')} separates city and county addresses. Solterra's rules are on {hoa('solterra')}.</p>", cls="alt")
    body += sec("Ridge sand", f"<p>Davenport is on the Lake Wales Ridge: Candler sand (0 to 5 percent slopes) is the dominant map unit around it, with Tavares and Astatula sands nearby (USDA Soil Data Access, FL105). It drains so fast that a base placed dry never densifies; we wet the subgrade and each lift of limerock before compacting and probe the result. It also means fewer drainage problems than Kissimmee and no water table to raise a slab above, except in the low ground around Lake Davenport and Loughman's Reedy Creek side. Details: {guide('paver-base-flatwoods-vs-ridge')}.</p>")
    body += sec(f"Costs in Davenport ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "paver-driveway-concrete", "paver-pool-deck", "concrete-slab-pad", "concrete-repair"]) + "<p>Polk ridge labor runs slightly below the Kissimmee index; resort communities run above it for access and scheduling.</p>", cls="alt")
    body += sec("Services in Davenport", cards([
        ("Concrete driveways", "New and replacement drives; Polk right-of-way rules for the apron.", city_service_route(k, "concrete-driveways"), "Driveways in Davenport"),
        ("Paver driveways", "Rebuilds on wetted, compacted ridge base; Paver Release Form when pavers reach the right-of-way.", city_service_route(k, "paver-driveways"), "Paver driveways in Davenport"),
        ("Paver pool decks", "Overlays and travertine in Providence and the rental communities.", city_service_route(k, "paver-pool-decks"), "Pool decks in Davenport"),
        ("Slabs and pads", "RV, boat and workshop slabs on Loughman-area lots.", city_service_route(k, "concrete-slabs"), "Slabs in Davenport"),
        ("Concrete repair", "Settled builder aprons and garage edges.", city_service_route(k, "concrete-repair"), "Repair in Davenport"),
    ], cols=3) + dist_line(k))
    faqs = [
        faq("Is my Davenport address in the city or the county?", "Most Davenport addresses are unincorporated Polk County; the city limits are the small historic core. The permit finder checks."),
        faq("What is the Paver Release Form?", "A notarized, recorded form Polk County requires when pavers are used in the county right-of-way: the owner accepts maintenance and replacement if the county has to dig, and the obligation runs with the land."),
        faq("Why does ridge sand need wetting?", "Candler sand has no fines to lock together dry; water lets the grains pack under a compactor. Base placed dry settles the first time it rains."),
        faq("Do you cover Providence and Solterra?", "Yes; both are Polk County and both have ARC review. Solterra's written guidelines are on our HOA page."),
        faq("How far is Davenport from Kissimmee?", "About 15 miles straight-line; site visits within three business days."),
    ]
    return page(k, "Concrete & Pavers in Davenport, FL – Polk Permits, Ridge Sand", "Concrete and paver work in Davenport: city vs. unincorporated Polk, Polk's slab and right-of-way permit rules, the Paver Release Form, Candler ridge sand that compacts only wet, Providence and Solterra, costs.", "Concrete and pavers in Davenport, FL: Polk County rules and ridge sand", body, faqs, ["polk-faq", "polk-paver-release", "solterra", "sda", "edr"])


# ---------------------------------------------------------------------------
def haines_city():
    k = "haines-city"
    body = sec("The fastest-growing town on the ridge",
        cap("Haines City (population 44,215 in the 2025 EDR estimate, up sharply since 2015) has a 1920s downtown around Lake Eva, mid-century neighborhoods off US-17/92, and a ring of 2015–2026 subdivisions along US-27 and Ernie Caldwell Boulevard: Hammock Reserve, Magnolia Park, Bradbury Creek, Randa Ridge, Highland Meadows and Southern Dunes. The city has its own building department for addresses inside the limits; unincorporated lots use Polk County. The ground is Candler and Tavares sand on the Lake Wales Ridge."),
        eyebrow="Haines City")
    body += sec("Areas and typical work",
        table(["Area", "Built", "Typical work"], [
            ("Downtown, Lake Eva, historic streets", "1920s–1960s", "Narrow drive and walk replacement, oak roots, small commercial pads"),
            ("US-17/92 and Hinson Ave neighborhoods", "1960s–1990s", "Driveway replacement and widening, patios, pads"),
            ("Southern Dunes, Randa Ridge, Highland Meadows", "2000–2015", "Pool-deck pavers, driveway extensions, sealing"),
            ("Hammock Reserve, Magnolia Park, Bradbury Creek, Tower Lakes", "2016–2026", "Builder concrete driveways cracking early; patios and lanai extensions; first sealing of paver drives"),
        ], caption="Development periods are approximate."))
    body += sec("Permits", cap("Inside the city limits, the City of Haines City's building division reviews permits; we did not verify its published rules for this page, so confirm before assuming a flatwork exemption. Unincorporated addresses follow Polk County's FAQ: permits for slabs adjacent to or supporting a structure, elevated slabs, sidewalks and driveway portions in the right-of-way or within setbacks; a recorded Paver Release Form for pavers in the right-of-way; (863) 534-6080.") + f"<p>{juris('polk-county')}; {tool('permit-finder')} separates city and county addresses. HOAs in the newer subdivisions run management-company ARC processes; the {tool('hoa-packet-checklist')} covers the submission.</p>", cls="alt")
    body += sec("Ground", f"<p>Candler sand dominates the ridge around Haines City with Tavares sand on the lower slopes (USDA Soil Data Access, FL105): well to excessively drained, no water table to fight, but base that will not compact dry. Early cracking on 2016–2026 builder driveways here usually traces to base placed dry and to slabs poured on the same day the forms were set. The lakes (Eva, Hamilton, Marion) have wetter margins where the flatwoods rules return. See {guide('paver-base-flatwoods-vs-ridge')} and {guide('why-concrete-cracks-osceola')}.</p>")
    body += sec(f"Costs in Haines City ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-patio", "paver-driveway-concrete", "concrete-repair", "concrete-removal", "paver-sealing"]) + "<p>Haines City runs at or slightly below the Kissimmee index on labor; travel is about 18 miles straight-line, so we group visits.</p>", cls="alt")
    body += sec("Services in Haines City", cards([
        ("Concrete driveways", "Replacement on the older streets, extensions and turnarounds in the new subdivisions.", city_service_route(k, "concrete-driveways"), "Driveways in Haines City"),
        ("Concrete patios", "Lanai extensions and backyard patios on ridge sand.", city_service_route(k, "concrete-patios"), "Patios in Haines City"),
        ("Concrete repair", "Early cracking on builder drives; apron and garage-edge repairs.", city_service_route(k, "concrete-repair"), "Repair in Haines City"),
        ("Paver driveways", "Upgrades and first sealing in the newer communities.", city_service_route(k, "paver-driveways"), "Paver driveways in Haines City"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Does Haines City have its own building department?", "Yes for addresses inside the city limits. Unincorporated addresses with a Haines City ZIP use Polk County. We did not verify the city's published flatwork rules, so we confirm by phone before quoting."),
        faq("Why is my 2019 driveway already cracking?", "On ridge sand, base placed dry does not compact and settles the first rainy season; a slab poured the same day the forms go in also gets no chance to be checked. The cracking guide shows which cracks matter."),
        faq("Do you cover Southern Dunes and Hammock Reserve?", "Yes; both have HOA review and we prepare the packet."),
        faq("How soon can you visit Haines City?", "Within three business days; we group Polk ridge visits."),
    ]
    return page(k, "Concrete & Pavers in Haines City, FL – Ridge Sand, Polk Permits", "Concrete and paver work in Haines City: city vs. Polk County permits, Candler ridge sand, early cracking on 2016–2026 builder driveways, Southern Dunes and Hammock Reserve HOAs, costs per sq ft.", "Concrete and pavers in Haines City, FL", body, faqs, ["polk-faq", "polk-paver-release", "sda", "edr"])


# ---------------------------------------------------------------------------
def harmony():
    k = "harmony"
    body = sec("New lots on old water in Harmony, Narcoossee and Sunbridge",
        cap("Harmony (2003–, a conservation-minded community on US-192 east of St. Cloud with its own CDD), the Narcoossee Road corridor (Nova Grove, Bridgewalk, Del Webb Sunbridge, Weslyn Park and the rest of Tavistock's Sunbridge, 2015–2026) and the older Narcoossee ranchettes share unincorporated Osceola County permits and some of the wettest ground in our area: EauGallie and Smyrna fine sands cut by Basinger lows where the water table is at the surface in summer. New-construction patios, driveway extensions, RV and boat pads and first sealing of builder pavers are the work."),
        eyebrow="Harmony &amp; Narcoossee")
    body += sec("Communities and typical work",
        table(["Community", "Built", "Notes"], [
            ("Harmony (Harmony CDD, HOA)", "2003–2020", "Front-loaded and alley lots; ARC review through the HOA; paver driveway repairs and sealing on 2005-era drives; patios and lanai extensions"),
            ("Weslyn Park, Del Webb Sunbridge, Nova Grove, Bridgewalk", "2019–2026", "New builder paver driveways and concrete drives; patios, pads, first sealing; confirm city vs. county by address"),
            ("Narcoossee ranchettes (Jones Rd, Absher Rd, Bass Rd)", "1970s–2010s", "Long driveways, RV and boat pads, workshop slabs, septic drainfields to avoid, well irrigation rust"),
            ("Lake Nona south edge (Orange County)", "2010–", "Outside our county coverage for permits; text mention only"),
        ], caption="Development periods are approximate."))
    body += sec("Permits", cap("Unincorporated Osceola County for Harmony and the Narcoossee corridor: county driveway permit for new or widened drives with the 24-foot limit (§22-50.6), Building Office at 1 Courthouse Square (407-742-0200), 3- to 5-day residential plan review, Notice of Commencement at $5,000 or more. Some Sunbridge phases carry St. Cloud addresses and utilities; the permit finder and a call to the Building Department settle which office applies.") + f"<p>{juris('osceola-county')}; {juris('city-of-st-cloud')}; {tool('permit-finder')}. Harmony's HOA and the Sunbridge associations review visible changes; the {tool('hoa-packet-checklist')} lists the attachments.</p>", cls="alt")
    body += sec("Ground and water", f"<p>This is the low, flat east side of the county: EauGallie fine sand (42,853 acres in Osceola), Smyrna, and Basinger fine sand in the sloughs, with a wet-season water table from the surface to about 12 inches (USDA Soil Data Access). Slabs are built on compacted fill above the seasonal high water with positive drainage to a swale; a pad set flush with the lawn sits in water every June. Ranchettes on wells and septic have two extra rules: no concrete over the drainfield ({guide('septic-drainfield-concrete-driveway')}) and expect iron staining from irrigation ({guide('rust-stains-irrigation-well-water')}). Long rural driveways need truck access checked before the pour; a mixer will not cross a wet pasture.</p>")
    body += sec(f"Costs in Harmony and Narcoossee ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "concrete-slab-pad", "paver-driveway-concrete", "paver-pool-deck", "paver-sealing"]) + "<p>Long driveways are quoted by the foot; fill to raise a slab above the water table is priced separately and is common here.</p>", cls="alt")
    body += sec("Services in Harmony and Narcoossee", cards([
        ("Concrete driveways", "Extensions on new lots; long drives and turnarounds on ranchettes.", city_service_route(k, "concrete-driveways"), "Driveways in Harmony"),
        ("Slabs and pads", "RV, boat and workshop slabs raised above the seasonal water.", city_service_route(k, "concrete-slabs"), "Slabs in Harmony"),
        ("Paver driveways", "Rebuilds and widening of 2005-era Harmony pavers; new drives in Sunbridge.", city_service_route(k, "paver-driveways"), "Paver driveways in Harmony"),
        ("Paver pool decks", "New decks and overlays in the new communities.", city_service_route(k, "paver-pool-decks"), "Pool decks in Harmony"),
    ], cols=2) + dist_line(k))
    faqs = [
        faq("Is Sunbridge in St. Cloud or the county?", "Parts carry St. Cloud addresses and utilities while sitting in unincorporated Osceola; the permit finder and a call to the Building Department settle it before we file."),
        faq("Can a mixer truck reach my ranchette?", "We check access, turnaround and ground on the site visit; if a truck cannot reach the pour we price a pump or a buggy."),
        faq("Why does my new driveway sit in water?", "Slabs poured flush with grade on EauGallie or Basinger sand sit in the wet-season water table. Raising the slab on compacted fill with a swale fixes it."),
        faq("Do you build over septic drainfields?", "No. We locate the system from the county record and stay clear."),
        faq("Does Harmony's HOA review pavers?", "Yes for visible changes; submit through the association's ARC form with a sample and site plan."),
    ]
    return page(k, "Concrete & Pavers in Harmony, Narcoossee & Sunbridge, FL", "Concrete and paver work in Harmony, the Narcoossee corridor and Sunbridge: Osceola County permits, EauGallie and Basinger sand with a surface water table, raised slabs, septic and well lots, new-community patios and pads.", "Concrete and pavers in Harmony, Narcoossee and Sunbridge, FL", body, faqs, ["osceola-22-50-6", "osceola-faq", "stcloud-permits", "sda"])


def get_pages():
    return [kissimmee(), st_cloud(), celebration(), poinciana(), bvl(), four_corners(), champions_gate(), reunion(), davenport(), haines_city(), harmony()]
