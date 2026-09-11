# -*- coding: utf-8 -*-
"""HOA / ARC hub and five verified community pages. Only rules read in the community's own documents are stated."""
from _data import HOAS
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, steps, callout, related, esc


def hub():
    body = sec("HOA and ARC approval for pavers, driveways and patios in Osceola and Polk",
        cap("Every planned community in our territory requires written architectural approval before a driveway, patio, pool deck or paver job starts, and the county permit does not replace it. We have read and quote the criteria for five associations: Poinciana's Association of Poinciana Villages, Solivita, Celebration's CROA, Bellalago, and Solterra Resort. For the others we work through the management company's current form and say plainly that we have not verified their written rules."),
        eyebrow="HOA / ARC")
    body += sec("Verified communities", cards([
        ("Poinciana (APV Design Control Board)", "Driveways in concrete, asphalt or brick pavers; walks beside the house capped at 2 ft; prior written approval for any paved area; 30 days of silence is a denial.", "/hoa/poinciana-apv/", "APV rules"),
        ("Solivita", "Replacement driveways and walks in the original builder's style and material; extensions and modifications reviewed; pavers need a sample.", "/hoa/solivita/", "Solivita rules"),
        ("Celebration (CROA)", "Architectural Review Committee meets the third Monday; Design Guidelines and applications on the Front Porch portal and at Town Hall.", "/hoa/celebration/", "Celebration rules"),
        ("Bellalago & Isles of Bellalago", "Architectural review before any exterior change; online form on ConnectResident; committee twice monthly; FirstService Residential.", "/hoa/bellalago/", "Bellalago rules"),
        ("Solterra Resort", "Expanded driveways no more than three cars wide; no added walking area; no painted or stained concrete; clear matte sealer by request; installer COI may be required.", "/hoa/solterra/", "Solterra rules"),
    ], cols=3))
    body += sec("Communities we work in but have not verified in writing",
        table(["Community", "County", "How we work there"], [
            ("Storey Lake, Tapestry, Windsor Hills, Emerald Island, Windsor Palms, Windsor at Westside", "Osceola", "Management ARC form; typical packet below"),
            ("Reunion (Artemis Lifestyles, Greystone, Southwest Property Management)", "Osceola", "Three management companies by section; contacts on the Reunion page"),
            ("ChampionsGate (Stoneybrook South, The Retreat, Country Club)", "Osceola", "Management ARC form"),
            ("Harmony, Sunbridge associations, Anthem Park, Hanover Lakes", "Osceola", "Management ARC form"),
            ("Providence, Solara, Bella Vida, Paradise Palms, Calabay Parc, Southern Dunes, Hammock Reserve", "Polk", "Management ARC form"),
        ], caption="If your community publishes its guidelines and you send them, we will read them and add a page."), cls="alt")
    body += sec("What every board asks for", f"<p>A site plan or survey with the work marked; the product name, color and pattern with a physical sample for pavers and a chip for stains and sealers; the edge or border detail; a drainage note showing water leaves the lot the way it did before; the installer's insurance certificate, sometimes naming the association as additional insured; and, since HB 803 (July 1, 2026), no building permit as a precondition, because the law now bars HOAs from requiring one before architectural review. The {tool('hoa-packet-checklist')} assembles it.</p>")
    body += sec("Timing", table(["Association", "Meeting or cycle", "Verified?"], [
        ("APV Poinciana", "Application deemed disapproved if not acted on within 30 days", "Yes"),
        ("Celebration CROA", "Third Monday of each month", "Yes"),
        ("Bellalago", "Twice monthly", "Yes"),
        ("Solterra", "Reviewer decides; incomplete applications get 15 days to complete", "Yes"),
        ("Solivita", "Per the ARC's schedule; written appeal to the Board within 30 days of a decision", "Yes (appeal rule)"),
        ("Management-form communities", "Typically two to six weeks", "No"),
    ]), cls="alt")
    faqs = [
        faq("Does my HOA have to approve a driveway replacement in the same material?", "In every verified community here, yes: APV requires prior written approval for any driveway or paved area, Solivita reviews all driveway work, Solterra reviews exterior changes, and Celebration and Bellalago review anything visible. Like-for-like work is approved faster, not skipped."),
        faq("Can the HOA require a building permit before it reviews my project?", "Not since July 1, 2026: HB 803 prohibits associations from requiring a building permit as a precondition for architectural review."),
        faq("Who submits the packet?", "We prepare it; you submit it as the owner, or we submit on your behalf where the association allows."),
        faq("What if the board doesn't answer?", "In Poinciana, silence for 30 days is a denial and you resubmit. Elsewhere, follow up with the manager; do not start work without the letter."),
        faq("Do you carry insurance the association can be named on?", "Yes; when the board requires it, our certificate names the association as additional insured."),
    ]
    return {"route": "/hoa/", "title": "HOA & ARC Approval for Pavers and Driveways – Osceola & Polk", "meta_description": "HOA and architectural review rules for driveways, patios, pool decks and pavers in Osceola and Polk: verified criteria for Poinciana APV, Solivita, Celebration, Bellalago and Solterra, what every board asks for, and HB 803.", "h1": "HOA and ARC approval for concrete and paver work", "breadcrumbs": [("Home", "/"), ("HOA / ARC", None)], "body_html": body, "faqs": faqs, "kind": "hoa", "sources": ["apv", "solivita", "celebration", "bellalago", "solterra", "hb803"]}


def apv():
    h = HOAS["poinciana-apv"]
    body = sec("What the Poinciana DCB requires for driveways, walks and patios",
        cap("From the Poinciana Villages Design Control Board Criteria (March 18, 2021): '9.1.1 Driveways and Walks. Concrete, asphalt, or brick pavers will be characteristic of the driveways required. Walks shall be of the same materials unless otherwise approved by the DCB. Any walkway adjacent to the residence dwelling must not exceed two (2) feet in width.' And: 'No building, fence, driveway, patio, drainage, paved area, wall or any other structure shall be commenced, erected, or maintained' without the DCB's prior written approval."),
        eyebrow="Association of Poinciana Villages")
    body += sec("Rules we quote, with sections",
        table(["Topic", "Criteria text (paraphrased where long)", "Section"], [
            ("Driveway materials", "Concrete, asphalt or brick pavers", "9.1.1"),
            ("Walks", "Same materials as the driveway unless the DCB approves otherwise; walks adjacent to the house no wider than 2 feet", "9.1.1"),
            ("Prior approval", "No driveway, patio, drainage, paved area or wall may be commenced without prior written DCB approval; exterior alterations to existing property need approval", "Article 6"),
            ("Deemed denial", "If the DCB fails to approve an application within 30 days of submittal, the application is deemed disapproved", "6.1"),
            ("Application contents", "A complete set of plans and specifications showing the proposed work; APV keeps a copy", "6.2"),
            ("Maintenance", "Owners must keep driveways, walks, patios and paved surfaces clean and in repair (pressure washing etc.)", "9.2.2"),
            ("Duplex driveways", "One driveway per unit, not exceeding the existing driveway width requirements of 9.1.1", "6.5.2.5"),
            ("Sheds", "On a concrete pad, no taller than 8 feet, color complementing the house; prohibited in Cypress Woods by covenant", "Sheds section"),
            ("Detached garages", "Driveways to a detached garage must be compatible with the existing driveway/walkway", "7.4"),
            ("Violations", "Applicant must rectify violations within a reasonable period after notice", "6.6.3"),
        ], caption="Poinciana Villages, Inc. Design Control Board Criteria, 3/18/21, on apvcommunity.com. APV office: 401 Walnut Street, Poinciana, FL 34759 · (863) 427-0900."), cls="alt")
    body += sec("How we handle a Poinciana job", steps([
        "Site visit; we photograph the existing driveway and measure its width, because the Criteria tie new work to the existing width requirement.",
        "DCB application with site plan, material, color and dimensions; you sign as owner. Like-for-like concrete replacements are routine but still required.",
        "Follow-up before day 30; silence is a denial under 6.1.",
        "County permit: Osceola driveway permit (§22-50.6) for Osceola villages, Polk rules for Polk villages; the finder shows which.",
        "Work; DCB copy of the permit number on request.",
    ]) + f"<p>Solivita, inside Poinciana's boundaries but with its own association, uses its own ARC: {hoa('solivita')}. City page: {city('poinciana')}; permits: {juris('osceola-county')}, {juris('polk-county')}.</p>")
    faqs = [
        faq("Can I use pavers on my driveway in Poinciana?", "Brick pavers are an accepted driveway material under 9.1.1, with prior written DCB approval."),
        faq("How wide can my front walk be?", "A walkway adjacent to the house may not exceed 2 feet unless the DCB approves otherwise."),
        faq("What if the DCB doesn't respond?", "After 30 days the application is deemed disapproved; resubmit or follow up."),
        faq("Do I need approval to replace my driveway with the same concrete?", "Yes; the Criteria require prior written approval for any driveway work."),
        faq("Where is the APV office?", "401 Walnut Street, Poinciana, FL 34759, (863) 427-0900."),
    ]
    return {"route": h["route"], "title": "Poinciana APV DCB Rules for Driveways, Walks & Pavers", "meta_description": "Poinciana's Design Control Board criteria quoted: driveways in concrete, asphalt or brick pavers (9.1.1), walks beside the house capped at 2 ft, prior written approval for any paved area, 30-day deemed denial, sheds. How we file.", "h1": "Poinciana (APV) Design Control Board: driveways, walks, patios and pavers", "breadcrumbs": [("Home", "/"), ("HOA / ARC", "/hoa/"), ("Poinciana APV", None)], "body_html": body, "faqs": faqs, "kind": "hoa", "sources": ["apv", "osceola-22-50-6", "polk-faq"]}


def solivita():
    h = HOAS["solivita"]
    body = sec("Solivita's architectural review rules for driveways and pavers",
        cap("From the Solivita Community Association Architectural Review Requirements (November 22, 2013): '6.14 Driveway and Walkways. All replacement driveways and/or walkways must be constructed in the same style and of the same materials utilized by the original builder in the construction of the original driveway and/or walkway. All requests for the extension or modification of a driveway…' are reviewed by the ARC. The application form lists 'Driveway Reseal', 'Walkway', 'Patio/pavers' and 'Screen Enclosure' as items needing review, and pavers require a color sample or picture."),
        eyebrow="Solivita (Poinciana, Polk County)")
    body += sec("What we read in the requirements",
        table(["Topic", "Requirement", "Section"], [
            ("Replacement driveways and walks", "Same style and same materials as the original builder's", "6.14"),
            ("Extensions and modifications", "Reviewed by the ARC on application", "6.14"),
            ("Pavers, patios, driveway reseal, walkways, screen enclosures", "Listed on the application form as items requiring review", "Exhibit A"),
            ("Samples", "Requests for painting, roofing, pavers etc. must include a color sample or picture", "Application instructions"),
            ("Plans", "The ARC may require up to three complete sets of plans; pools and structures need floor-slab and pool-deck elevations and a drainage plan", "5.2, 5.3"),
            ("Walls between back-to-back lots", "4-ft concrete block or solid concrete wall, stucco and painted to match, no closer than 5 ft to the rear line", "Fences and walls"),
            ("Appeal", "Written request to the Board within 30 days of an ARC decision; the Board's determination is dispositive", "Appeals"),
            ("Exculpation", "The Association and ARC are not liable for costs arising from approvals or denials", "16"),
        ], caption="Solivita Community Association, Inc., Architectural Review Requirements, final 11.22.13 (copy hosted by a community realty site; confirm the current version with the association)."), cls="alt")
    body += sec("How a Solivita job goes", f"<p>Because 6.14 ties replacements to the builder's original material, a concrete-to-paver conversion is an 'extension or modification' request with a sample and a plan, decided case by case; a like-for-like concrete replacement is routine. Patios and paver additions behind the house are reviewed with a sample; screen enclosures are reviewed with elevations. Solivita is in Polk County, so the permit rules are Polk's ({juris('polk-county')}), including the Paver Release Form if pavers reach the right-of-way. The {tool('hoa-packet-checklist')} builds the submission; city page: {city('poinciana')}.</p>")
    faqs = [
        faq("Can I replace my Solivita driveway with pavers?", "Only if the ARC approves a departure from the original builder's material under 6.14; submit it as a modification with a sample."),
        faq("Does resealing need approval?", "'Driveway Reseal' is on the application form as a reviewable item, so yes."),
        faq("Which county permits Solivita?", "Polk County."),
        faq("Can I appeal a denial?", "In writing to the Board within 30 days; the Board's decision is final under the requirements."),
    ]
    return {"route": h["route"], "title": "Solivita ARC Rules for Driveways, Pavers & Patios", "meta_description": "Solivita's Architectural Review Requirements quoted: replacement driveways and walks in the original builder's style and material (6.14), extensions reviewed, pavers and patios on the application list with samples, appeals within 30 days.", "h1": "Solivita architectural review: driveways, walkways, pavers and patios", "breadcrumbs": [("Home", "/"), ("HOA / ARC", "/hoa/"), ("Solivita", None)], "body_html": body, "faqs": faqs, "kind": "hoa", "sources": ["solivita", "polk-faq", "polk-paver-release"]}


def celebration():
    h = HOAS["celebration"]
    body = sec("Celebration's Architectural Review Committee",
        cap("The Celebration Residential Owners Association's Architectural Review Committee meets on the third Monday of each month, unless posted otherwise, to review recently submitted applications. Current Design Guidelines and applications are available to owners on the Celebration Front Porch (celebration.fl.us, under the CROA tab with an owner login) and from the Association's offices at Town Hall, 851 Celebration Avenue, Celebration, FL 34747, 407-566-1200 ext. 2206, townhall@ciramail.com."),
        eyebrow="Celebration (CROA)")
    body += sec("What we verified and what we did not",
        f"<p>Verified on celebration.fl.us: the committee's monthly third-Monday schedule, the Town Hall contact, and topic-specific published Design Guidelines (ceiling fans, gutters and downspouts, street trees and easement modifications, common-area signs). Not verified by us: the driveway, paver, patio and pool-deck sections of the Design Guidelines, which sit behind the owner login. Third-party installer pages describe approved patterns, a narrow color palette, village-specific accents and a 6-inch driveway base; we do not repeat those as CROA rules. Ask Town Hall or download the current section from the Front Porch before choosing material, and send it to us; we will build the packet to it.</p>", cls="alt")
    body += sec("How a Celebration job goes", steps([
        "You (or we, with your login) pull the current Design Guidelines section for the work.",
        "We prepare the application: site plan or survey markup, product, color, pattern, edge or border detail, a physical sample, a drainage note.",
        "Submit before the agenda deadline for the third-Monday meeting.",
        "Osceola County permit after approval: driveway permit for a new or widened drive (§22-50.6, 24-ft maximum); flatwork rules for patios and overlays.",
        "Work, then the closeout letter for your file.",
    ]) + f"<p>City page: {city('celebration')}; local service pages: {svc('paver-driveways')} and the Celebration pages linked from it; permits: {juris('osceola-county')}; packet: {tool('hoa-packet-checklist')}.</p>")
    faqs = [
        faq("When does the Celebration ARC meet?", "The third Monday of each month unless posted otherwise."),
        faq("Where are the Design Guidelines?", "On the Celebration Front Porch under the CROA tab (owner login) and at Town Hall, 851 Celebration Avenue."),
        faq("Do you know the approved paver patterns?", "We have not verified that section ourselves; bring the current guideline and we build the packet to it."),
        faq("Does a lanai deck need review?", "Depends on visibility and the material rules; Town Hall answers for your address."),
    ]
    return {"route": h["route"], "title": "Celebration ARC (CROA) – Driveways, Pavers, Pool Decks", "meta_description": "Celebration's Architectural Review Committee: third-Monday meetings, where the Design Guidelines live (Front Porch owner portal and Town Hall), what we verified and what we did not, and how we build the packet for pavers, driveways and pool decks.", "h1": "Celebration (CROA) Architectural Review Committee", "breadcrumbs": [("Home", "/"), ("HOA / ARC", "/hoa/"), ("Celebration", None)], "body_html": body, "faqs": faqs, "kind": "hoa", "sources": ["celebration", "osceola-22-50-6"]}


def bellalago():
    h = HOAS["bellalago"]
    body = sec("Bellalago's architectural review process",
        cap("From bellalagohoa.com: 'Prior to any changes to the exterior of your home, an Architectural Review is needed.' Requests are submitted through the online ARC Request Form on the ConnectResident portal (house number and ZIP to start), the review committee convenes twice monthly, and written notification of the decision follows. The Bellalago & Isles of Bellalago Community Association is professionally managed by FirstService Residential; 24-hour resident line (866) 378-1099. The association has announced updated architectural guidelines covering modern materials and technologies."),
        eyebrow="Bellalago &amp; Isles of Bellalago")
    body += sec("What we verified and what we did not", f"<p>Verified: the requirement of review before any exterior change, the online form and portal, the twice-monthly meeting cadence, the management company. Not verified: the specific criteria for driveway width, paver colors, pool-deck materials and fees, which are in the guidelines PDF available to residents. Bring the current document to the site visit and we build the packet to it. Bellalago is unincorporated Osceola County: driveway permit and 24-foot rule for new or widened drives ({juris('osceola-county')}); pool-deck overlays and patios outside setbacks are flatwork.</p>", cls="alt")
    body += sec("Typical Bellalago jobs", f"<p>Travertine and marble pool decks inside screened lanais, paver driveway upgrades in the estate sections, paver and concrete repairs on 2005–2015 builder work, and sealing. The community sits on Smyrna and Myakka fine sand with lakefront lots on Lake Toho's wetter margins; drainage is designed into every deck ({city('kissimmee')}, {svc('paver-pool-decks')}, {svc('paver-travertine')}). Packet: {tool('hoa-packet-checklist')}.</p>")
    faqs = [
        faq("How do I submit an ARC request in Bellalago?", "Through the online ARC Request Form on the ConnectResident portal; the committee meets twice a month."),
        faq("Do I need approval to reseal pavers?", "A like-for-like clear seal is usually maintenance; confirm with FirstService if the finish changes."),
        faq("Which county permits Bellalago?", "Unincorporated Osceola County."),
        faq("Where are the written criteria?", "In the association's guidelines available to residents; we build to the current version you provide."),
    ]
    return {"route": h["route"], "title": "Bellalago HOA Architectural Review – Pavers, Decks, Driveways", "meta_description": "Bellalago's architectural review: approval before any exterior change, the ConnectResident ARC form, twice-monthly committee, FirstService Residential contacts, what we verified, and Osceola County permits for the community.", "h1": "Bellalago and Isles of Bellalago: architectural review", "breadcrumbs": [("Home", "/"), ("HOA / ARC", "/hoa/"), ("Bellalago", None)], "body_html": body, "faqs": faqs, "kind": "hoa", "sources": ["bellalago", "osceola-22-50-6"]}


def solterra():
    h = HOAS["solterra"]
    body = sec("Solterra Resort's architectural guidelines for driveways, concrete and pavers",
        cap("From the Solterra Resort Homeowners Association Architectural Guidelines, Standards & Criteria (August 18, 2020): expanded driveways may be no more than three cars wide; 'No additional walking area may be added to expanded driveways'; 'Painting or staining of concrete paved surfaces is prohibited. Concrete surfaces may be sealed in a clear matte finish and a request must be submitted to the Reviewer'; 'Additional sidewalks in any location require' approval; parking is limited to the garage and driveway. Requests for pavers or tile require a lot survey with a sketch of the area and a sample of the material."),
        eyebrow="Solterra Resort (Davenport, Polk County)")
    body += sec("Rules we quote",
        table(["Topic", "Guideline", "Section"], [
            ("Driveway and sidewalk extensions", "Expanded driveways no more than three cars wide; no added walking area; additional sidewalks need approval", "VIII.J"),
            ("Concrete finish", "No painting or staining of concrete; clear matte sealer allowed with a request", "VIII.J"),
            ("Pavers and tile", "Lot survey with a sketch of the area and a sample of the material required with the request", "II.B"),
            ("Setbacks", "Front 20 ft to a front-facing garage, 15 ft to the structure; side 5 ft; rear 15 ft (5 ft to a pool deck or screen patio)", "VIII.A"),
            ("Pools and decks", "Reviewed; 5-ft side setback and county rear setback; drainage from additions no closer than 5 ft to a neighbor", "VIII.LL, VIII.A"),
            ("Contractor insurance", "The Board may require the contractor to provide a certificate naming the Association as insured, with minimum General Liability and Workers' Compensation limits", "III.C"),
            ("Incomplete applications", "Applicant has 15 days to supply missing information or a new application is needed", "III.A"),
            ("Canopies", "Bolted into patio concrete or anchored in concrete; max 10×10×10 ft; solid neutral color", "VIII.E"),
            ("Walls between back-to-back lots", "4-ft masonry wall, stucco, painted to match, 5 ft from the rear line", "VIII.N"),
        ], caption="Solterra Resort HOA, Architectural Guidelines, Standards & Criteria, 8/18/2020, on solterraresorthoa.com/documents. Management: Artemis Lifestyles, (407) 705-2190."), cls="alt")
    body += sec("How a Solterra job goes", f"<p>Survey markup, product sample, pattern and color, drainage note, and our insurance certificate naming the association when the Reviewer asks; submission through Artemis; 15 days to complete anything missing. Rental owners schedule between guests ({guide('vacation-rental-owner-hardscape-guide')}). Solterra is unincorporated Polk County: right-of-way and setback portions of a driveway are permitted, a concrete apron avoids the Paver Release Form, and slabs adjacent to structures are confirmed ({juris('polk-county')}). Service pages: {svc('paver-driveways')}, {svc('paver-pool-decks')}, {svc('paver-sealing')}; area: {city('four-corners')}, {city('davenport')}.</p>")
    faqs = [
        faq("How wide can I make my Solterra driveway?", "No more than three cars wide, with approval, and no added walking area."),
        faq("Can I stain my concrete driveway?", "No; painting or staining concrete surfaces is prohibited. A clear matte sealer is allowed with a request."),
        faq("Will the HOA want my contractor's insurance?", "The Board may require a certificate naming the Association as insured, with minimum liability and workers' compensation limits."),
        faq("What goes in a paver request?", "A lot survey with a sketch of the area and a sample of the paver."),
        faq("Who manages Solterra?", "Artemis Lifestyles, (407) 705-2190."),
    ]
    return {"route": h["route"], "title": "Solterra Resort HOA Rules – Driveways, Concrete, Pavers, COI", "meta_description": "Solterra Resort's architectural guidelines quoted: driveways no wider than three cars, no added walkway, no painted or stained concrete, clear matte sealer by request, survey and sample for pavers, contractor insurance naming the association.", "h1": "Solterra Resort: architectural rules for driveways, concrete and pavers", "breadcrumbs": [("Home", "/"), ("HOA / ARC", "/hoa/"), ("Solterra", None)], "body_html": body, "faqs": faqs, "kind": "hoa", "sources": ["solterra", "polk-faq", "polk-paver-release"]}


def get_pages():
    return [hub(), apv(), solivita(), celebration(), bellalago(), solterra()]
