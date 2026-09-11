# -*- coding: utf-8 -*-
"""/areas/ index plus county hubs: Osceola, Polk, South Orange."""
from _data import CITIES, TIER1, TIER2, SERVICES, COST_INDEX_RELEASE, drive_estimate
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, related, esc

NOAA_ROWS = [("Jan", "71.8", "48.3", "2.67", "7.6", "4.1"), ("Feb", "74.4", "50.7", "2.37", "6.5", "4.0"), ("Mar", "77.9", "54.4", "3.07", "6.2", "4.2"), ("Apr", "83.0", "59.7", "2.43", "5.7", "3.6"), ("May", "87.4", "65.8", "4.17", "7.8", "5.7"), ("Jun", "90.0", "71.8", "9.18", "15.8", "12.3"), ("Jul", "91.5", "73.5", "7.21", "16.7", "12.2"), ("Aug", "91.4", "74.1", "8.38", "17.7", "13.0"), ("Sep", "89.5", "72.8", "5.88", "14.3", "9.5"), ("Oct", "84.6", "66.2", "3.07", "8.7", "5.7"), ("Nov", "78.6", "57.3", "1.99", "5.8", "3.1"), ("Dec", "73.5", "51.5", "2.15", "6.5", "3.5")]


def areas_index():
    t1 = [(city(k), CITIES[k]["county"], f"{CITIES[k]['miles']} mi" if CITIES[k]["miles"] else "anchor", f"~{drive_estimate(CITIES[k]['miles'])} min" if CITIES[k]["miles"] else "n/a", "City hub + local service pages") for k in TIER1]
    t2 = [(city(k), CITIES[k]["county"], f"{CITIES[k]['miles']} mi", f"~{drive_estimate(CITIES[k]['miles'])} min", "City hub (four services covered on the page)") for k in TIER2]
    mention = [
        ("Orange County (south)", "Hunters Creek 5.0 mi, Southchase 6.1, Meadow Woods 7.2, Williamsburg 7.9, Taft 9.7, Pine Castle 11.5, Dr. Phillips 11.6, Lake Nona, Belle Isle 12.4, Edgewood 13.3, Conway 14.9, Horizon West 16.2, Windermere 16.4, Orlando 12.3, Winter Garden 20.7, Ocoee 21.2, Winter Park 21.4", "Estimates yes; pages live with our Orlando-area colleagues. See South Orange County."),
        ("Lake County", "Four Corners (Lake side) 15, Clermont 25.0, Montverde 26.9, Minneola 29.0, Groveland 33.7, Mascotte 37.2", "Estimates on the Four Corners side; Clermont and beyond are covered by our South Lake colleagues."),
        ("Seminole County", "Altamonte Springs 25.5, Casselberry 26.0, Longwood 28.5, Winter Springs 28.6, Oviedo 28.9, Lake Mary 32.6, Sanford 35.3", "Outside our regular routes; we refer."),
        ("Osceola, no page", "Loughman (Polk) 10.6, Campbell 3.5, Intercession City, Kenansville, Holopaw, Yeehaw Junction", "Covered under the Kissimmee, Davenport and St. Cloud pages and the Osceola County hub."),
        ("Polk, 30–40 mi", "Lakeland 37.1, Bartow 37.7, Frostproof 38.2, Eagle Lake 30.5, Lake Hamilton 21.4, Fort Meade (out)", "Edge of the radius; estimates case by case, no pages."),
    ]
    body = sec("Where Kissimmee Concrete works",
        cap("About 40 miles around downtown Kissimmee: all of Osceola County, the Polk County ridge from Four Corners and Davenport through Haines City to Winter Haven, Auburndale, Lake Alfred, Dundee, Lake Wales and Polk City, and the south Orange County communities next door. Distances below are straight-line from the Census internal point of each place; drive times are rough weekday-morning estimates. Site visits within two business days in Osceola, three on the Polk ridge.")
        + "<h3>Tier 1: city guide plus local service pages</h3>" + table(["Place", "County", "Distance", "Drive (est.)", "Coverage"], t1)
        + "<h3>Tier 2: city guide</h3>" + table(["Place", "County", "Distance", "Drive (est.)", "Coverage"], t2, caption="Tier 2 pages cover the four highest-demand services in sections. Local service pages are added when demand shows in search data.")
        + "<h3>Mentioned, not paged</h3>" + table(["Area", "Places (straight-line miles)", "What we do"], mention, caption="Boundaries follow the county hubs below; Orange, Lake and Seminole communities are served by our sister brands' pages and by us on request."))
    body += sec("County hubs", cards([
        ("Osceola County", "Kissimmee, St. Cloud and unincorporated Osceola: §22-50.6 driveway rule, permit offices, soils, NOAA normals, HOAs and CDDs.", "/areas/osceola-county/", "Osceola County"),
        ("Polk County", "The ridge from Four Corners to Lake Wales: Polk's slab and right-of-way rules, the Paver Release Form, Candler sand, cities with their own building departments.", "/areas/polk-county/", "Polk County"),
        ("South Orange County", "Hunters Creek, Meadow Woods, Southchase, Taft and the Lake Nona edge: Orange County's 'pouring concrete or placing pavers requires a permit' rule and the 6-inch apron spec.", "/areas/orange-county-south/", "South Orange County"),
    ]), cls="alt")
    body += sec("Tools for any address", cards([
        ("Permit & Jurisdiction Finder", "Type an address; see city or county and what that means for a driveway, patio, slab or pavers.", "/tools/permit-finder/", "Check an address"),
        ("Pour Calendar", "Rain days and temperatures by month at the Kissimmee 2 NOAA station.", "/tools/pour-calendar/", "See the calendar"),
        ("HOA / ARC Packet Checklist", "What the boards in our territory ask for before approving pavers or a driveway change.", "/tools/hoa-packet-checklist/", "Build your packet"),
    ]))
    return {"route": "/areas/", "title": "Service Area – Kissimmee, Osceola County & the Polk Ridge", "meta_description": "Where Kissimmee Concrete works: every Osceola County city and community, the Polk County ridge from Four Corners to Lake Wales, and south Orange County, with distances, drive estimates and coverage tiers.", "h1": "Service area: 40 miles around Kissimmee", "breadcrumbs": [("Home", "/"), ("Areas", None)], "body_html": body, "kind": "area", "nav_active": "/areas/", "sources": ["gazetteer", "edr"]}


def osceola():
    body = sec("Osceola County for concrete and paver work",
        cap("Osceola County is three permit regimes (City of Kissimmee, City of St. Cloud, unincorporated county), one dominant soil family (Smyrna, Myakka and Immokalee fine sands with a wet-season water table about 12 inches down), one rainy season (June through September, 14 to 18 rain days a month at the Kissimmee 2 station), and dozens of HOAs and community development districts that review anything you can see from the street. This page collects the facts we use on every job in the county, with sources."),
        eyebrow="County hub")
    body += sec("Jurisdictions and what each requires",
        table(["Jurisdiction", "Driveway", "Patio / slab / pad", "Pavers", "Office"], [
            ("City of Kissimmee", "Driveway / Sidewalk Construction application on EnerGov; plan review ≥ 2 business days; permit ≥ 2 business days after payment", "Building Division review by scope; confirm at permitting@kissimmee.org / 407-518-2379", "Same driveway application; right-of-way work needs Public Works & Engineering (407-518-2169)", f"{juris('city-of-kissimmee', 'Engineering, 101 Church St, 3rd Floor · 407-518-2278')}"),
            ("City of St. Cloud", "Building Department; right-of-way needs Public Works approval", "Patios, decks, screen enclosures, sheds on the permit list", "Driveway/sidewalk pavers: refer to Public Works (no building permit)", f"{juris('city-of-st-cloud', '1300 9th St · 407-957-7300')}"),
            ("Unincorporated Osceola", "County driveway permit required for construction or widening; max 24 ft wide without conditional use (§22-50.6); right-of-way under LDC 4.12.2", "Building Office; shed permit requirements published; residential plan review 3–5 days; NOC at $5,000+", "Under the driveway permit", f"{juris('osceola-county', '1 Courthouse Sq, Suite 1400 · 407-742-0200')}"),
        ], caption="Verified on the official pages on 2026-09-10. The county enforces the 8th edition (2023) Florida Building Code, effective 2023-12-31, and does not enforce local amendments to it (Building Office FAQ).")
        + f"<p>Where the lines run: downtown Kissimmee, the lakefront, the Vine Street and John Young Parkway corridors and the Osceola Parkway annexations are city; Buenaventura Lakes, Bellalago, the Pleasant Hill corridor, Poinciana, Celebration, Harmony, Narcoossee, Reunion and ChampionsGate are county; St. Cloud's limits take in the historic core, the Nova Road and Canoe Creek corridors and parts of the Narcoossee communities. The {tool('permit-finder')} checks an address against the Census boundaries. HB 803 (effective July 1, 2026) exempts single-family work valued under $7,500 from a building permit with a written request, with exclusions for structural, electrical, plumbing, mechanical, gas and flood-zone work ({guide('hb-803-permit-exemption')}).</p>", cls="alt")
    body += sec("What is under the county",
        table(["Map unit (USDA, FL097)", "Acres", "Drainage", "Wet-season water table", "What it means for a slab"], [
            ("Smyrna fine sand, 0–2%", "188,635", "Poorly drained", "~12 in", "Compacted base, positive slope, downspouts off the slab"),
            ("Myakka fine sand, 0–2%", "122,954", "Poorly drained", "~12 in", "Same as Smyrna"),
            ("Immokalee fine sand, 0–2%", "70,229", "Poorly drained", "~12 in", "Same; slightly deeper spodic layer"),
            ("Basinger fine sand, depressional", "47,191", "Very poorly drained", "surface", "Raise the slab on fill; swale; expect standing water in June"),
            ("Basinger fine sand, 0–2%", "44,637", "Poorly drained", "~6 in", "Raise and drain"),
            ("EauGallie fine sand, 0–2%", "42,853", "Poorly drained", "~12 in", "Harmony/Narcoossee; compacted base, drainage"),
            ("Placid fine sand, ponded", "38,664", "Very poorly drained", "surface", "Avoid or build up substantially"),
            ("Samsula, Hontoon, Kaliga mucks", "27,882 / 24,676 / 10,205", "Very poorly drained", "surface", "Lake and slough margins; no slab without engineered fill"),
        ], caption="Top map units by acreage from USDA NRCS Soil Data Access, survey area FL097, queried 2026-09-10. Water-table depths are the reported wet-season minimums for the major components.")
        + f"<p>The county's flatwoods sand is fine to build on when it is proof-rolled, compacted and drained; it fails when a slab is poured flush on it with a downspout at the edge. Live oaks in the older neighborhoods lift slabs; well irrigation outside the utility areas leaves iron stains. Guides: {guide('why-concrete-cracks-osceola')}, {guide('tree-roots-driveways-central-florida')}, {guide('rust-stains-irrigation-well-water')}, {guide('paver-base-flatwoods-vs-ridge')}.</p>")
    body += sec("NOAA normals for Kissimmee 2 (1991–2020)",
        table(["Month", "Avg high °F", "Avg low °F", "Rain (in)", "Days ≥ 0.01 in", "Days ≥ 0.10 in"], NOAA_ROWS, caption="NOAA NCEI U.S. Climate Normals 1991–2020, station USC00084625 (Kissimmee 2, FL). Annual total about 52.6 inches; June–September carry roughly 58 percent of it.")
        + f"<p>What we do with these numbers: June through September pours start at first light and are finished and covered before the afternoon storms; polymeric sand and sealers wait for a dry 24 hours; October through April is the season for big pours and stamped work. The {tool('pour-calendar')} turns the table into a month-by-month recommendation, and {guide('rainy-season-concrete-scheduling')} explains the rain-day rule.</p>", cls="alt")
    body += sec("HOAs and CDDs",
        f"<p>Verified criteria with section numbers: {hoa('poinciana-apv')} (APV Design Control Board), {hoa('solivita')}, {hoa('celebration')} (CROA ARC), {hoa('bellalago')}. Communities where we work through the management company's form but have not published written criteria: Tapestry, Storey Lake, Windsor Hills, Emerald Island, Reunion (Artemis, Greystone, Southwest), ChampionsGate, Harmony, the Sunbridge associations. Community development districts (Celebration CDD, Harmony CDD, Reunion East/West CDDs, Stevens Plantation, Tapestry) maintain private streets and stormwater; the ARC approval usually doubles as the access approval for work touching a private street. {tool('hoa-packet-checklist')}.</p>")
    body += sec("Places in Osceola County", related([city(k) for k in TIER1]) + "<p class=\"note\" style=\"margin-top:10px\">Also served without a page: Campbell, Intercession City, Loughman (Polk side), Kenansville, Holopaw, Yeehaw Junction, and the Lake Nona edge (Orange).</p>", cls="alt")
    faqs = [
        faq("How wide can a residential driveway be in Osceola County?", "24 feet in unincorporated Osceola without a conditional use, under Code §22-50.6(a); the same section requires a county driveway permit for construction or widening. Inside Kissimmee and St. Cloud the city engineer reviews width with the application."),
        faq("Which building code does Osceola enforce?", "The 8th edition (2023) Florida Building Code and the 2020 NEC, effective December 31, 2023, with no local amendments to the building code (Building Office FAQ)."),
        faq("How long does a residential permit take?", "Osceola's plan review normally takes 3 to 5 days once the application is complete; Kissimmee's driveway application at least 2 business days for review and 2 more to issue after payment."),
        faq("Do I need a Notice of Commencement?", "In Osceola County, for any project valued at $5,000 or more, recorded at the courthouse before the first inspection."),
        faq("What soil is my lot on?", "Most of the county is Smyrna, Myakka or Immokalee fine sand; lakefront and slough lots are Basinger, Placid or muck. We look up the map unit and probe on site."),
    ]
    return {"route": "/areas/osceola-county/", "title": "Osceola County Concrete & Pavers – Permits, Soils, Climate, HOAs", "meta_description": "Osceola County facts for concrete and paver work: Kissimmee, St. Cloud and county permit rules with the 24-ft driveway limit, USDA soil units and water tables, NOAA Kissimmee 2 rain days, HOA and CDD review.", "h1": "Osceola County: permits, soils, climate and HOAs for concrete and paver work", "breadcrumbs": [("Home", "/"), ("Areas", "/areas/"), ("Osceola County", None)], "body_html": body, "faqs": faqs, "kind": "county", "nav_active": "/areas/", "sources": ["osceola-22-50-6", "osceola-faq", "kissimmee-driveway", "stcloud-permits", "sda", "noaa", "hb803", "apv", "solivita", "celebration", "bellalago"]}


def polk():
    body = sec("Polk County's ridge for concrete and paver work",
        cap("The part of Polk County we serve is the Lake Wales Ridge and the I-4/US-27 corridor: Four Corners, Davenport, Loughman, Haines City, Lake Alfred, Auburndale, Winter Haven, Dundee, Lake Wales and Polk City. Permits come from Polk County for unincorporated addresses and from each city's own building department inside its limits. The ground is Candler, Astatula and Tavares sand: deep, dry, and unable to compact until it is wetted, which is the opposite problem from Osceola's."),
        eyebrow="County hub")
    body += sec("Where the rules live, and who applies them",
        cap("Two authorities matter on the ridge. Polk County's Building Division covers unincorporated addresses, which is most of what carries a Davenport or Haines City mailing address, and each city covers what is inside its own limits. Polk decides by location rather than by activity, so a slab's position relative to the structure, the setbacks and the easements is what determines whether it is permitted work.")
        + f"<p>We keep the county's own wording, its office addresses and the Concrete Driveway Paver Release Form on a single page rather than restating them here, so there is one version to keep current when the county changes something. That page is {juris('polk-county')}. What belongs on this page is the rest of the ridge: which cities run their own departments, what the sand does, how the rainy season lands here, and which associations we have read.</p>", cls="alt")
    body += sec("Cities with their own building departments",
        table(["City", "Population (2025 EDR)", "Our page", "Note"], [
            ("Davenport", "14,031", city("davenport"), "Historic core only; Solterra, Providence, Loughman are county"),
            ("Haines City", "44,215", city("haines-city"), "Fast-growing; US-27 subdivisions"),
            ("Winter Haven", "60,837", city("winter-haven"), "Chain of Lakes margins"),
            ("Auburndale", "21,677", city("auburndale"), "Berkley Road growth"),
            ("Lake Alfred", "9,038", city("lake-alfred"), "Home of the county's Northeast Government Center"),
            ("Dundee", "5,847", city("dundee"), "US-27 subdivisions"),
            ("Lake Wales", "17,748", city("lake-wales"), "Top of the ridge; sloped lots"),
            ("Polk City", "3,007", city("polk-city"), "Rural lots toward the Green Swamp"),
            ("Lake Hamilton, Eagle Lake, Bartow, Lakeland, Frostproof", "3,139 / 6,209 / 22,958 / 124,733 / 2,996", "n/a", "Edge of the radius; no page"),
        ], caption="We did not verify each city's published flatwork rules for this page; for a city address we confirm by phone before quoting."))
    body += sec("Ridge sand turns the base problem around",
        table(["Map unit (USDA, FL105)", "Acres", "Drainage", "What it means"], [
            ("Smyrna and Myakka fine sands", "144,718", "Poorly drained", "The Polk flatwoods (Poinciana's Polk side, Green Swamp edge): same rules as Osceola"),
            ("Candler sand, 0–5%", "97,496", "Excessively drained", "The ridge: no water table; base must be wetted to compact"),
            ("Pomona fine sand", "91,570", "Poorly drained", "Flatwoods pockets"),
            ("Tavares fine sand, 0–5%", "53,679", "Moderately well drained", "Lower ridge slopes; wet the base"),
            ("Astatula sand, 0–5%", "34,785", "Excessively drained", "Top of the ridge (Lake Wales); wet the base"),
            ("Basinger, Placid, Samsula, Hontoon", "22,607 / 18,486 / 53,893 / 50,474", "Very poorly drained", "Lake margins and swamps; raise and drain or avoid"),
        ], caption="USDA NRCS Soil Data Access, survey area FL105, queried 2026-09-10.")
        + f"<p>Dry-placed base on Candler sand reads compacted on the plate and settles the first rainy season; that single fact explains the early-cracking builder driveways in every 2015–2026 subdivision from Davenport to Lake Wales. We wet the subgrade and each lift of limerock, compact, and probe. {guide('paver-base-flatwoods-vs-ridge')}; {guide('why-concrete-cracks-osceola')}.</p>", cls="alt")
    body += sec("Climate", f"<p>The ridge shares Kissimmee's rainy season: at the Kissimmee 2 station, June averages 15.8 days with measurable rain, July 16.7, August 17.7, September 14.3; October through April run 6 to 9. Normal highs peak at 91.5 °F in July. We use the same first-light pour rule across the county ({tool('pour-calendar')}).</p>")
    body += sec("HOAs", f"<p>Verified: {hoa('solterra')} (three-car driveway limit, no painted concrete, COI on request) and, on the Polk side of Poinciana, {hoa('poinciana-apv')} and {hoa('solivita')}. Management-form communities: Providence, Champions Reserve, Astonia, Cascades, Solara, Bella Vida, Paradise Palms, Calabay Parc, Tuscan Ridge, Southern Dunes, Hammock Reserve, Magnolia Park, Bradbury Creek, Lake Lucerne, Berkley Ridge. {tool('hoa-packet-checklist')}.</p>", cls="alt")
    body += sec("Places on the Polk ridge", related([city(k) for k in ["four-corners", "davenport", "haines-city", "poinciana"] + TIER2]))
    faqs = [
        faq("Does Polk County require a permit for a driveway?", "For the portion in the right-of-way or within the minimum setbacks, yes; a replacement in the same footprint on your lot outside setbacks is flatwork, with drainage requirements still applying. Inside a city, the city's building department decides."),
        faq("What is the Paver Release Form?", "A notarized, recorded form for pavers in the county right-of-way: the owner accepts maintenance and replacement if the county digs, indemnifies the county, and the obligation runs with the land. A concrete apron avoids it."),
        faq("Do patios need a permit in Polk?", "A detached patio slab outside the setbacks and not supporting a structure is not permitted separately; a slab supporting a screen room, within a setback, or elevated is."),
        faq("Why do new driveways on the ridge crack early?", "Base placed dry on Candler sand does not compact until the first rainy season does it, and the slab follows it down."),
        faq("Which Polk office is closest to Kissimmee?", "The Northeast Government Center at 200 Government Center Blvd, Lake Alfred."),
    ]
    return {"route": "/areas/polk-county/", "title": "Polk County Ridge Concrete & Pavers – Rules, Release Form, Sand", "meta_description": "Polk County facts for concrete and paver work on the ridge: the county's slab, driveway and paver rules quoted, the Paver Release Form, cities with their own departments, Candler sand that compacts only wet, HOAs.", "h1": "Polk County ridge: permits, the Paver Release Form, ridge sand and HOAs", "breadcrumbs": [("Home", "/"), ("Areas", "/areas/"), ("Polk County", None)], "body_html": body, "faqs": faqs, "kind": "county", "nav_active": "/areas/", "sources": ["polk-faq", "polk-paver-release", "sda", "edr", "noaa", "solterra"]}


def orange_south():
    body = sec("Next door to Kissimmee, under different rules",
        cap("Hunters Creek (5 miles from downtown Kissimmee), Southchase (6.1), Meadow Woods (7.2), Williamsburg (7.9), Taft (9.7) and the south edge of Lake Nona are closer to us than St. Cloud, and we take those calls. Their pages live with our Orlando-area colleagues, so this hub covers only what a homeowner there needs from us: Orange County's permit position, its apron spec, and how the ground compares. Unincorporated Orange County says plainly that 'anytime you are pouring concrete or placing pavers, a permit is required.'"),
        eyebrow="County hub")
    body += sec("Orange County's rules",
        table(["Item", "Orange County (unincorporated)", "Source"], [
            ("Concrete work", "'Anytime you are pouring concrete or placing pavers, a permit is required'", "Do I Need a Permit guide"),
            ("Pavers", "Zoning permit", "Do I Need a Permit guide"),
            ("Driveway in the right-of-way", "Minimum 6 in of 3,000 psi concrete, no steel in the right-of-way, minimum 3 ft from the property line", "Right-of-Way Utilization Regulations / driveway detail"),
            ("Sheds", "All structures require a permit; 120 sq ft or less may be exempt from the building code but still need to apply", "Do I Need a Permit guide"),
            ("Contact", "407-836-5550 · EResQuestions@ocfl.net", "Orange County Permits & Licenses"),
        ], caption="The county's own guide notes it is not complete or exhaustive; confirm scope with the Division of Building Safety.")
        + f"<p>Compared with Osceola, the difference is that a backyard patio slab in unincorporated Orange County is permitted where in Osceola it is usually flatwork, and the apron spec is 6 inches with no steel. City of Orlando addresses (parts of Lake Nona and Southchase) follow the city's permitting. {juris('orange-county')}; {tool('permit-finder')}.</p>", cls="alt")
    body += sec("Ground and water", f"<p>South Orange is the same flatwoods as north Osceola: Smyrna, Myakka and Immokalee fine sands with a wet-season water table around 12 inches, wetter toward Shingle Creek and the Boggy Creek chain. Base, slope and downspout rules from the Osceola hub apply unchanged ({city('kissimmee', 'see the Kissimmee page')}, {guide('why-concrete-cracks-osceola')}). Hunters Creek, Southchase and Meadow Woods are 1985–2005 communities with the same cracked-4-inch-slab pattern as Buenaventura Lakes and the same HOA reviews.</p>")
    body += sec("What we do here", f"<p>Driveway replacement, paver driveways, pool-deck overlays, sealing and repair, the same as across the county line, at the Kissimmee index. Because these communities are minutes from us, site visits are within two business days. For full local pages on Orlando, Dr. Phillips, Windermere, Winter Garden and Ocoee, our sister brands cover those markets; we do not duplicate them here.</p>" + related([svc("concrete-driveways"), svc("paver-driveways"), svc("paver-pool-decks"), svc("concrete-repair"), svc("paver-sealing")]), cls="alt")
    faqs = [
        faq("Do I need a permit for a patio in Hunters Creek or Meadow Woods?", "In unincorporated Orange County, yes: the county's guide says pouring concrete or placing pavers requires a permit (pavers through Zoning). We file it."),
        faq("Do you serve Lake Nona?", "The south edge, yes, on request; the pages for Lake Nona live with our Orlando-area colleagues."),
        faq("What is the driveway apron spec?", "Six inches of 3,000 psi with no steel in the right-of-way, at least 3 feet from the property line, per Orange County."),
        faq("Same prices as Kissimmee?", "Yes; these communities are inside the Kissimmee index market."),
    ]
    return {"route": "/areas/orange-county-south/", "title": "South Orange County Concrete & Pavers – Hunters Creek", "meta_description": "Concrete and paver work in south Orange County next to Kissimmee: Hunters Creek, Southchase, Meadow Woods, Taft and the Lake Nona edge, with Orange County's 'permit required' rule and 6-inch apron spec.", "h1": "South Orange County: Hunters Creek, Meadow Woods, Southchase and the Lake Nona edge", "breadcrumbs": [("Home", "/"), ("Areas", "/areas/"), ("South Orange County", None)], "body_html": body, "faqs": faqs, "kind": "county", "nav_active": "/areas/", "sources": ["orange-permit", "sda"]}


def get_pages():
    return [areas_index(), osceola(), polk(), orange_south()]
