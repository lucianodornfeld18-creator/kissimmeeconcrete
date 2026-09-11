# -*- coding: utf-8 -*-
"""Permit hub and per-jurisdiction pages. Every rule is quoted from the official page checked on 2026-09-10."""
from _data import JURISDICTIONS
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, steps, callout, related, esc


def hub():
    body = sec("Do you need a permit for concrete or pavers in Kissimmee? It depends on the line you live on",
        cap("Five offices cover our territory and they disagree. The City of Kissimmee permits driveways and sidewalks through its Engineering Division. Unincorporated Osceola County requires a driveway permit for any new or widened residential driveway and caps width at 24 feet. St. Cloud permits patios and decks but sends driveway pavers to Public Works. Polk County permits slabs that support structures, sit within setbacks or lie in the right-of-way. Orange County says any concrete pour or paver placement needs a permit."),
        eyebrow="Permits")
    body += sec("Quick answers by project",
        table(["Project", "City of Kissimmee", "Unincorp. Osceola", "City of St. Cloud", "Polk County (unincorp.)", "Orange County (unincorp.)"], [
            ("New or replaced driveway", "Driveway / Sidewalk application (Engineering)", "County driveway permit; 24 ft max", "Building Dept; right-of-way via Public Works", "Permit for portions in right-of-way or within setbacks", "Permit required; 6 in / 3,000 psi apron, no steel"),
            ("Driveway widening", "Same application", "County driveway permit; 24 ft max (§22-50.6)", "Building Dept", "Same as above", "Permit required"),
            ("Paver driveway", "Same application", "Under the driveway permit", "Refer to Public Works (no building permit)", "Pavers in the right-of-way: recorded Paver Release Form", "Zoning permit"),
            ("Backyard patio slab (detached, outside setbacks)", "Generally flatwork; confirm scope", "Generally flatwork; confirm; HB 803 < $7,500", "Permit required (patios on the city list)", "Not permitted separately; drainage rules apply", "Permit required"),
            ("Slab under a screen room / attached to house", "Permit with the enclosure", "Permit with the enclosure", "Permit", "Permit (slab supporting a structure)", "Permit"),
            ("Shed pad", "Shed permitted; pad inspected with it", "Shed permit requirements published; pad with it", "Sheds on the permit list", "Pre-manufactured storage buildings permitted", "All structures need a permit application"),
            ("Pool deck overlay (existing deck)", "Flatwork unless tied to structure", "Flatwork unless tied to structure", "Decks on the permit list; confirm", "Confirm: slab adjacent to a structure", "Permit required"),
            ("Repair in the same footprint", "No permit", "No permit", "No permit (asphalt reseal listed as exempt)", "No permit", "Minor repairs generally exempt"),
            ("Resurfacing / sealing", "No permit", "No permit", "No permit", "No permit", "No permit"),
        ], caption="Summary of official pages checked on 2026-09-10; each jurisdiction page below quotes the source. 'Confirm' means we call the office for your address before quoting."))
    body += sec("Florida's new $7,500 exemption",
        cap("HB 803, signed May 6, 2026 and effective July 1, 2026, exempts owners of single-family dwellings and their contractors from obtaining a building permit for work valued under $7,500, after a written request for exemption, and excludes structural, electrical, plumbing, mechanical and gas work and property in a flood hazard area. It also bars HOAs from requiring a building permit as a precondition for architectural review.")
        + f"<p>What it changes here: a stand-alone pad or patio under $7,500 in a jurisdiction that would otherwise permit it can be exempted with the written request. What it does not change: driveway permits (a driveway in the right-of-way is not a building-permit question), HOA review, or work in a flood zone. {guide('hb-803-permit-exemption')}.</p>", cls="alt")
    body += sec("Who files, who signs", steps([
        "We identify the jurisdiction (the finder below, then a call when an address is near a line).",
        "We prepare and file the application as the contractor; you sign it, and in Osceola County a Notice of Commencement for jobs of $5,000 or more, recorded at the courthouse before the first inspection.",
        "Plan review: Osceola residential 3–5 days; Kissimmee driveway application at least 2 business days, permit at least 2 business days after payment; St. Cloud and Polk vary by scope.",
        "Inspections scheduled by us (Osceola: request before 3 p.m. for next day); permit card on site.",
        "You receive the permit number with the warranty; a buyer's inspector will ask for it.",
    ]))
    body += sec("Jurisdiction pages", cards([
        ("City of Kissimmee", "Driveway / Sidewalk Construction application on EnerGov, Engineering Division contacts, right-of-way approval.", "/permits/city-of-kissimmee/", "Kissimmee"),
        ("Unincorporated Osceola County", "§22-50.6 quoted, driveway permit, 24-ft rule, LDC 4.12.2, Building Office FAQ facts, NOC.", "/permits/osceola-county/", "Osceola County"),
        ("City of St. Cloud", "The city's permit-required and no-permit lists, pavers to Public Works, cashless payments, HB 803 adoption.", "/permits/city-of-st-cloud/", "St. Cloud"),
        ("Polk County", "The county FAQ quoted, the Paver Release Form explained, offices in Bartow and Lake Alfred, cities with their own departments.", "/permits/polk-county/", "Polk County"),
        ("Orange County", "'Anytime you are pouring concrete or placing pavers, a permit is required'; apron spec; Zoning permit for pavers.", "/permits/orange-county/", "Orange County"),
    ]), cls="alt")
    body += sec("Find your jurisdiction", f"<p>The {tool('permit-finder')} geocodes an address in your browser and checks it against the Census city and county boundaries, then shows the rules above for that jurisdiction. Addresses within a few hundred feet of a line get a call to the office before we quote.</p>")
    faqs = [
        faq("Do I need a permit to replace my driveway?", "Yes in every jurisdiction here for a new or replaced driveway that touches the right-of-way; Kissimmee and Osceola permit the whole driveway, St. Cloud sends pavers to Public Works, Polk permits the right-of-way and setback portions, Orange permits all concrete work."),
        faq("Do I need a permit for a patio?", "St. Cloud and Orange County: yes. Kissimmee, Osceola and Polk: a detached slab outside setbacks is generally flatwork, with HB 803's written-request exemption available under $7,500; anything attached, under a roof or within a setback is permitted."),
        faq("Who pulls the permit?", "We do, as the contractor; the owner signs the application and the Notice of Commencement where required."),
        faq("How long does a permit take?", "Osceola residential plan review normally 3 to 5 days; Kissimmee's driveway application at least 2 business days plus 2 to issue; others vary."),
    ]
    return {"route": "/permits/", "title": "Concrete & Paver Permits in Kissimmee, Osceola & Polk (2026)", "meta_description": "Do you need a permit for a driveway, patio, slab, pool deck or pavers? Rules by project for the City of Kissimmee, unincorporated Osceola County, St. Cloud, Polk County and Orange County, with HB 803's $7,500 exemption.", "h1": "Permits for concrete and paver work: Kissimmee, Osceola, St. Cloud, Polk and Orange", "breadcrumbs": [("Home", "/"), ("Permits", None)], "body_html": body, "faqs": faqs, "kind": "permit", "nav_active": "/permits/", "sources": ["kissimmee-driveway", "osceola-22-50-6", "osceola-faq", "stcloud-permits", "polk-faq", "polk-paver-release", "orange-permit", "hb803"]}


def kissimmee():
    j = JURISDICTIONS["city-of-kissimmee"]
    body = sec("Driveway and sidewalk permits inside Kissimmee city limits",
        cap("Residents and property owners requesting updates to existing roads for driveway access or sidewalk construction within City of Kissimmee limits apply online through the City's EnerGov portal, selecting 'Driveway / Sidewalk Construction' as the request type. Plan review takes at least two business days after submission; the permit is issued at least two business days after the fee is paid. Any work within the right-of-way needs Public Works & Engineering approval."),
        eyebrow="City of Kissimmee")
    body += sec("The process, step by step", steps([
        "Confirm the address is inside city limits and not on a county or FDOT right-of-way (the city's own first step). The finder below checks the city boundary.",
        "We open the application on the EnerGov Citizen Self Service portal, select 'Driveway / Sidewalk Construction', enter the address, specify driveway access, sidewalk or both, attach a photo and a site sketch.",
        "City staff follow up with the document list for the scope ('the City requires different documents depending on the work being done'); we supply them.",
        "Plan review: allow at least 2 business days.",
        "Fee communicated by email after approval, paid through the permit lookup tool; permit issued at least 2 business days after payment.",
        "Work, inspections, closeout; you get the permit number.",
    ]) + f"<p>Contacts: Engineering Division, 101 Church Street, 3rd Floor, Kissimmee, FL 34741 · {j['phone']} · engineering@kissimmee.gov. Building Division (patios, slabs, structures): permitting@kissimmee.org · 407-518-2379. Public Works & Engineering (right-of-way): 407-518-2169. Portal: <a href=\"{j['portal']}\" rel=\"noopener\" target=\"_blank\">{j['portal_name']}</a>.</p>", cls="alt")
    body += sec("What we could and could not verify",
        f"<p>Verified on kissimmee.gov: the application type, the review and issuance timelines, the right-of-way rule, the fee process and the contacts. Not verified: a published maximum residential driveway width for the city (the Land Development Code is rendered on Municode and was not readable in our check), and a published flatwork exemption list for detached patio slabs. For those two we call the Engineering or Building Division for your address and put the answer in the proposal. Outside the city line, Osceola County's §22-50.6 applies ({juris('osceola-county')}).</p>")
    body += sec("Where the city line runs", f"<p>City: downtown and the Lake Tohopekaliga lakefront, the Vine Street (US-192) corridor, the John Young Parkway and Osceola Parkway annexations, Kissimmee Bay, Remington, and most of the newer commercial corridors. County: Buenaventura Lakes, Bellalago, the Pleasant Hill Road corridor, Poinciana, Celebration, Harmony, Narcoossee, Reunion, ChampionsGate. The {tool('permit-finder')} checks any address; {city('kissimmee')} has the neighborhood table.</p>", cls="alt")
    body += sec("Related", related([svc("concrete-driveways"), svc("paver-driveways"), svc("concrete-sidewalks-walkways"), guide("driveway-widening-rules-osceola"), guide("hb-803-permit-exemption")]))
    faqs = [
        faq("How long does a Kissimmee driveway permit take?", "At least 2 business days for plan review and at least 2 business days to issue after the fee is paid, per the city's page; allow a week with document requests."),
        faq("Do I need a permit to replace my driveway in Kissimmee?", "Yes, through the Driveway / Sidewalk Construction application, because the driveway connects to the city's right-of-way."),
        faq("What about a patio?", "The Building Division reviews by scope; a detached slab outside setbacks is often flatwork, and HB 803's $7,500 exemption may apply. We confirm for your address."),
        faq("What if my street is a county road?", "Then the application goes to Osceola County, not the city, even inside the city; the city's page tells applicants to confirm the right-of-way is the city's."),
    ]
    return {"route": j["route"], "title": "City of Kissimmee Driveway Permit – How It Works (2026)", "meta_description": "How to permit a driveway or sidewalk inside Kissimmee city limits: the EnerGov Driveway / Sidewalk Construction application, 2-business-day review and issuance timelines, right-of-way rule, Engineering Division contacts.", "h1": "City of Kissimmee: driveway and sidewalk permits", "breadcrumbs": [("Home", "/"), ("Permits", "/permits/"), ("City of Kissimmee", None)], "body_html": body, "faqs": faqs, "kind": "permit", "nav_active": "/permits/", "sources": ["kissimmee-driveway", "hb803"]}


def osceola():
    j = JURISDICTIONS["osceola-county"]
    body = sec("Do you need a permit for a driveway in unincorporated Osceola County?",
        cap("Yes. Osceola County Code of Ordinances §22-50.6 (Ordinance 12-10, §6, effective March 19, 2012) reads: '(a) Residential driveways shall not exceed twenty-four (24) feet in width unless approved by conditional use. (b) Residential driveway construction or widening shall be authorized by the issuance of a driveway permit by Osceola County.' Right-of-way work follows Land Development Code section 4.12.2, which applicants must attest to having read."),
        eyebrow="Unincorporated Osceola County")
    body += sec("Facts from the Building Office, quoted",
        table(["Question", "Answer (Building Office Frequent Questions)"], [
            ("Which code?", "The 8th edition (2023) Florida Building Code and 2020 NEC, effective December 31, 2023; the county does not enforce local amendments to the building code"),
            ("Who can apply?", "'Any owner, licensed contractor or authorized agent may bring in the permit application' but only the applicant (owner or contractor) may sign; signatures not given in person must be notarized"),
            ("Notice of Commencement?", "Required for projects valued at $5,000 or more; notarized, recorded at the County Courthouse (2 Courthouse Square, 2nd floor), copy to the Permitting Office or NOC@Osceola.org before the jobsite inspection"),
            ("Residential plan review time", "'Normally takes 3 to 5 days' if documents meet code; deficiencies bring correction requests"),
            ("Inspections", "Scheduled online, by text or phone; call before 3:00 p.m. for next-day; Saturday inspections requested by 3:00 p.m. Thursday; after-hours minimum $160"),
            ("Owner-builder", "Allowed for 1–2 family homes with a signed Owner-Builder Statement/Affidavit submitted in person"),
            ("Fees", "Per the current adopted County Fee Schedule (Appendix B, Community Development Fees)"),
            ("Contractor registration", "Register with the State (DBPR) first, then with the county's Licensing page (applies to licensed categories; flatwork and pavers are not licensed categories)"),
        ], caption="Building Office: 1 Courthouse Square, Suite 1400, Kissimmee, FL 34741 · 407-742-0200 · permits.osceola.org."), cls="alt")
    body += sec("What falls under which permit",
        f"<p><strong>Driveways.</strong> New, replaced or widened: county driveway permit; 24 feet maximum. Pavers in the driveway are covered by the same permit; the apron in the right-of-way follows the county detail. <strong>Patios, pads, pool-deck overlays.</strong> A detached slab outside the setbacks is generally flatwork without a building permit; a slab within a setback, attached to the house, under a roof, tied to a pool or screen enclosure, or in a flood zone should be confirmed with the Building Office, and HB 803's written-request exemption applies under $7,500 since July 1, 2026. <strong>Sheds.</strong> The county publishes 'Permit Requirements for Storage Sheds'; the shed is the permitted structure and the pad is inspected with it. <strong>Repairs, resurfacing, sealing.</strong> Maintenance, no permit. We confirm the category for your address before we quote and put it in writing.</p>")
    body += sec("Related", related([guide("driveway-widening-rules-osceola"), guide("hb-803-permit-exemption"), svc("concrete-driveways"), svc("concrete-slabs"), city("buenaventura-lakes"), city("poinciana"), city("harmony"), city("celebration")]), cls="alt")
    faqs = [
        faq("How wide can my driveway be?", "24 feet unless a conditional use is approved (§22-50.6(a))."),
        faq("Do I need a permit to widen my driveway?", "Yes; construction or widening requires a county driveway permit (§22-50.6(b))."),
        faq("How long does the permit take?", "Residential plan review normally 3 to 5 days once the application is complete."),
        faq("What is a Notice of Commencement?", "A recorded notice required for jobs of $5,000 or more before the first inspection; we prepare it, you sign before a notary, and it is recorded at the courthouse."),
        faq("Does a backyard patio need a permit?", "A detached slab outside setbacks is generally flatwork; attached, roofed, in-setback or flood-zone slabs are permitted. HB 803's $7,500 exemption needs a written request."),
    ]
    return {"route": j["route"], "title": "Do You Need a Permit for a Driveway in Osceola County? (2026)", "meta_description": "Osceola County's driveway rule quoted: §22-50.6 requires a county driveway permit and caps width at 24 ft. Building Office facts on plan review (3–5 days), Notice of Commencement, inspections, sheds, patios and HB 803.", "h1": "Unincorporated Osceola County: driveway permits, the 24-foot rule and flatwork", "breadcrumbs": [("Home", "/"), ("Permits", "/permits/"), ("Osceola County", None)], "body_html": body, "faqs": faqs, "kind": "permit", "nav_active": "/permits/", "sources": ["osceola-22-50-6", "osceola-faq", "osceola-permits", "hb803"]}


def st_cloud():
    j = JURISDICTIONS["city-of-st-cloud"]
    body = sec("St. Cloud's permit list for outdoor concrete and pavers",
        cap("The City of St. Cloud's Permit Information page lists patios, decks, screen enclosures, sheds, gazebos, carports, reroofs, windows and solar among projects that require a permit, and lists 'driveway reseal for single-family/duplex (existing asphalt only, no striping)' and 'pavers for driveways/sidewalks (refer to Public Works)' among projects that do not need a building permit. Any work in the right-of-way needs Public Works and Engineering approval. The Building Department stopped accepting cash on January 1, 2025."),
        eyebrow="City of St. Cloud")
    body += sec("What this means by project",
        table(["Project", "St. Cloud position", "What we do"], [
            ("Concrete driveway, new or replaced", "Building Department review; right-of-way portion via Public Works", "File with the Building Department; Public Works approval for the apron"),
            ("Paver driveway or sidewalk", "'Refer to Public Works' (no building permit)", "Public Works approval; concrete apron to the city detail"),
            ("Asphalt reseal (existing)", "No permit", "Not our scope"),
            ("Patio slab, deck", "Permit required (on the list)", "File; HB 803 written-request exemption under $7,500 where the scope qualifies"),
            ("Screen enclosure, shed, gazebo", "Permit required", "The enclosure contractor permits it; our slab is inspected with it"),
            ("Pool deck overlay", "Decks on the list; confirm whether an overlay is treated as maintenance", "Call the Building Department for the address"),
            ("Repair, resurfacing, sealing", "Maintenance", "No permit"),
        ], caption=f"Building Department, 1300 9th Street, St. Cloud, FL 34769 · {j['phone']} · portal: {j['portal_name']}."), cls="alt")
    body += sec("HB 803 in St. Cloud", f"<p>St. Cloud adopted the state's exemption for residential projects valued under $7,500 effective July 1, 2026, with the state's exclusions (structural, electrical, plumbing, mechanical, gas, FEMA special flood hazard areas) and a written exemption request. A detached patio slab under that value can qualify; a driveway in the right-of-way cannot. {guide('hb-803-permit-exemption')}.</p>")
    body += sec("Outside the city line", f"<p>The Narcoossee communities, Harmony and the rural lots east and south straddle the line; some Sunbridge phases carry St. Cloud addresses while sitting in unincorporated Osceola, where §22-50.6 and the county driveway permit apply. The {tool('permit-finder')} checks the boundary; {juris('osceola-county')}; {city('st-cloud')}; {city('harmony')}.</p>", cls="alt")
    body += sec("Related", related([svc("concrete-patios"), svc("paver-driveways"), svc("paver-pool-decks"), guide("septic-drainfield-concrete-driveway")]))
    faqs = [
        faq("Do driveway pavers need a permit in St. Cloud?", "Not a building permit: the city's list refers driveway and sidewalk pavers to Public Works, and the right-of-way portion needs Public Works approval."),
        faq("Do patios need a permit in St. Cloud?", "Yes; patios and decks are on the city's permit-required list. HB 803's $7,500 exemption may apply with a written request."),
        faq("Can I pay the permit fee in cash?", "No; the Building Department has been cashless since January 1, 2025."),
        faq("Is my Narcoossee address in the city?", "The finder checks the boundary; when an address is near the line we call the Building Department before filing."),
    ]
    return {"route": j["route"], "title": "St. Cloud, FL Permits for Patios, Driveways & Pavers (2026)", "meta_description": "City of St. Cloud's permit list quoted: patios and decks need a permit, driveway pavers go to Public Works, asphalt reseal is exempt, cashless since 2025, HB 803 adopted. Building Department contacts and the city line.", "h1": "City of St. Cloud: which outdoor concrete and paver projects need a permit", "breadcrumbs": [("Home", "/"), ("Permits", "/permits/"), ("City of St. Cloud", None)], "body_html": body, "faqs": faqs, "kind": "permit", "nav_active": "/permits/", "sources": ["stcloud-permits", "hb803", "osceola-22-50-6"]}


def polk():
    j = JURISDICTIONS["polk-county"]
    body = sec("Polk County's slab, driveway and paver rules, quoted",
        cap("From the Polk County Building Division FAQ: permits are required for 'concrete slabs adjacent to a principal or accessory structure, intended for support of a structure, elevated slabs, sidewalks and portions of driveways in the right of way or within the minimum setbacks.' 'All slabs shall meet minimum setbacks from property lines and easements, except sidewalk and driveways. Building Code and Land Development Code drainage requirements shall be met.' 'Pavers installed within the required setbacks or adjacent to structures' must meet Building Code and LDC requirements. Structural and decorative retaining walls go to a plans examiner."),
        eyebrow="Polk County (unincorporated)")
    body += sec("The Concrete Driveway Paver Release Form",
        cap("Form PD BLD 40 (revised May 16, 2019): when concrete pavers are used for a residential driveway or sidewalk in the county right-of-way, the property owner signs a notarized statement accepting 'full responsibility for any required maintenance or repair' and 'paver replacement or reconstruction in the event the County must remove any portion of my driveway/sidewalk for any work to be performed in the right-of-way', indemnifies the county, and records the instrument with the Clerk of Courts; a certified copy is submitted before driveway approval, and the agreement runs with the land to future owners.")
        + f"<p>Most owners avoid the form by ending the pavers at a soldier course on the lot and pouring the apron in concrete to the county detail, which is also what most HOAs prefer. When pavers do go in the right-of-way we prepare the form, you sign before a notary, and we record it. {svc('paver-driveways')}.</p>", cls="alt")
    body += sec("By project",
        table(["Project", "Polk County position", "What we do"], [
            ("Driveway, new or replaced", "Portions in the right-of-way or within setbacks need a permit; drainage rules apply", "File for the right-of-way portion; drainage on the proposal"),
            ("Paver driveway", "Same, plus Paver Release Form if pavers reach the right-of-way", "Concrete apron or the form"),
            ("Detached patio or pad outside setbacks", "Not permitted separately", "Flatwork; HB 803 written request where relevant"),
            ("Slab supporting a structure (screen room, shed, workshop)", "Permit", "Permitted with the structure; pre-manufactured storage buildings are permitted structures"),
            ("Pool deck adjacent to the house / screen footer", "Confirm: slab adjacent to a structure", "Call the Building Division for the address"),
            ("Retaining wall", "Structural: permit; decorative: ask a plans examiner", "We build decorative walls to 4 ft; structural walls are referred"),
            ("Repair, resurfacing, sealing", "Maintenance", "No permit"),
        ], caption=f"Offices: 330 W. Church Street, Bartow, FL 33830; Northeast Government Center, 200 Government Center Blvd, Lake Alfred, FL 33850 · {j['phone']} · virtual inspections via VuSpex GO."))
    body += sec("Cities with their own building departments", f"<p>Davenport, Haines City, Winter Haven, Auburndale, Lake Alfred, Dundee, Lake Wales, Polk City, Lake Hamilton, Eagle Lake, Bartow and Lakeland review permits inside their limits; Poinciana's Polk villages, Solterra, Providence, Loughman, Four Corners' Polk side and most 'Davenport' addresses are unincorporated county. We did not verify each city's published flatwork rules; for a city address we call before quoting. {tool('permit-finder')}; county hub: <a href=\"/areas/polk-county/\">Polk County</a>.</p>", cls="alt")
    body += sec("Related", related([city("davenport"), city("haines-city"), city("four-corners"), city("poinciana"), hoa("solterra"), guide("paver-base-flatwoods-vs-ridge")]))
    faqs = [
        faq("Do I need a permit for a driveway in Polk County?", "For the portion in the right-of-way or within the setbacks, yes; drainage requirements apply to the whole driveway. Inside a city, the city's department decides."),
        faq("What is the Paver Release Form?", "A notarized, recorded agreement for pavers in the county right-of-way: you accept maintenance and replacement if the county digs, and the obligation runs with the land. A concrete apron avoids it."),
        faq("Do I need a permit for a patio in Polk County?", "A detached slab outside the setbacks that does not support a structure is not permitted separately; a slab supporting a screen room, within a setback, or elevated is."),
        faq("Which office is closest to Kissimmee?", "The Northeast Government Center, 200 Government Center Blvd, Lake Alfred."),
        faq("Do you build retaining walls in Polk?", "Decorative walls to 4 feet; walls for structural support need a permit and a licensed contractor, and we refer them."),
    ]
    return {"route": j["route"], "title": "Polk County Permits for Slabs, Driveways & Pavers (2026)", "meta_description": "Polk County's building rules for concrete and pavers quoted: which slabs and driveway portions need a permit, the Concrete Driveway Paver Release Form for pavers in the right-of-way, offices in Bartow and Lake Alfred, cities with their own departments.", "h1": "Polk County: slab and driveway permits and the Paver Release Form", "breadcrumbs": [("Home", "/"), ("Permits", "/permits/"), ("Polk County", None)], "body_html": body, "faqs": faqs, "kind": "permit", "nav_active": "/permits/", "sources": ["polk-faq", "polk-paver-release", "hb803"]}


def orange():
    j = JURISDICTIONS["orange-county"]
    body = sec("Orange County permits any concrete or paver work",
        cap("Unincorporated Orange County's 'Do I Need a Permit' guide states: 'Anytime you are pouring concrete or placing pavers, a permit is required.' Pavers are permitted through Zoning; concrete driveways and walkways through Building. Sheds: 'All structures require a permit'; structures of 120 square feet or less may be exempt from the building code but still need an application. Driveways in the right-of-way: minimum 6 inches of 3,000 psi concrete, no steel in the right-of-way, at least 3 feet from the property line."),
        eyebrow="Orange County (unincorporated)")
    body += sec("Why this page exists", f"<p>Hunters Creek, Southchase, Meadow Woods, Williamsburg, Taft and the south edge of Lake Nona are minutes from Kissimmee and in unincorporated Orange County (parts of Lake Nona and Southchase are City of Orlando). We take those jobs at Kissimmee prices; the rules are Orange County's, and they are stricter than Osceola's on patios and slabs. Full Orlando-area coverage belongs to our sister brands; the <a href=\"/areas/orange-county-south/\">South Orange County</a> hub explains the boundary. Contact: Division of Building Safety, {j['phone']} · EResQuestions@ocfl.net.</p>", cls="alt")
    body += sec("By project",
        table(["Project", "Orange County position"], [
            ("Concrete driveway, patio, slab, walkway", "Building permit required"),
            ("Pavers (driveway, patio, walk)", "Zoning permit required"),
            ("Driveway apron in the right-of-way", "6 in, 3,000 psi, no steel, 3 ft from property line; right-of-way utilization rules"),
            ("Shed", "Permit application for all structures; ≤ 120 sq ft may be exempt from the building code"),
            ("Fence", "Zoning permit ≤ 6 ft; building permit over 6 ft or masonry"),
            ("Minor repair", "Generally exempt; the county's guide is 'not complete or exhaustive', so confirm"),
        ]))
    body += sec("Related", related([svc("concrete-driveways"), svc("paver-driveways"), svc("concrete-patios"), tool("permit-finder")]), cls="alt")
    faqs = [
        faq("Do I need a permit for a patio in Hunters Creek?", "Yes, in unincorporated Orange County any concrete pour or paver placement requires a permit."),
        faq("What is the driveway apron spec?", "Six inches of 3,000 psi concrete with no steel in the right-of-way, at least 3 feet from the property line."),
        faq("Is Lake Nona city or county?", "Parts are City of Orlando, parts unincorporated Orange; the finder checks the address."),
        faq("Do you serve Orange County?", "The communities next to Kissimmee, yes; full Orlando-area pages are on our sister sites."),
    ]
    return {"route": j["route"], "title": "Orange County Permits for Concrete & Pavers – South Orange (2026)", "meta_description": "Unincorporated Orange County's rule quoted: any concrete pour or paver placement needs a permit (pavers via Zoning), 6-inch no-steel apron spec, shed rules. For Hunters Creek, Meadow Woods, Southchase and Taft next to Kissimmee.", "h1": "Orange County: permits for concrete and pavers in the communities next to Kissimmee", "breadcrumbs": [("Home", "/"), ("Permits", "/permits/"), ("Orange County", None)], "body_html": body, "faqs": faqs, "kind": "permit", "nav_active": "/permits/", "sources": ["orange-permit"]}


def get_pages():
    return [hub(), kissimmee(), osceola(), st_cloud(), polk(), orange()]
