# -*- coding: utf-8 -*-
"""Tier-2 city hubs on the Polk ridge: Winter Haven, Auburndale, Lake Alfred, Dundee, Lake Wales, Polk City.
Each page covers the four highest-demand services in sections; no city×service URLs until demand is observed."""
from _data import CITIES, SERVICES, COST_INDEX_RELEASE, drive_estimate
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, faq, cost_rows, cost_range, related, esc


def page(key, title, desc, h1, body, faqs, sources):
    c = CITIES[key]
    body += f'<div class="wrap"><p class="note">Straight-line distance from downtown Kissimmee: {c["miles"]} miles (Census 2024 Gazetteer); drive estimate about {drive_estimate(c["miles"])} minutes. Population {esc(c["pop"])}. Polk County.</p></div>'
    return {"route": c["route"], "title": title, "meta_description": desc, "h1": h1, "breadcrumbs": [("Home", "/"), ("Areas", "/areas/"), ("Polk County", "/areas/polk-county/"), (c["name"], None)], "body_html": body, "faqs": faqs, "kind": "city", "city_key": key, "nav_active": "/areas/", "sources": sources}


def four_services(key, drive_note, paver_note, deck_note, repair_note):
    c = CITIES[key]["name"]
    return sec(f"The four jobs we do most in {c}", cards([
        ("Concrete driveways", drive_note, "/concrete/driveways/", "Concrete driveways (Kissimmee master page)"),
        ("Paver driveways", paver_note, "/pavers/driveways/", "Paver driveways"),
        ("Pool decks", deck_note, "/pavers/pool-decks/", "Paver pool decks"),
        ("Concrete repair", repair_note, "/concrete/repair/", "Concrete repair"),
    ], cols=2), eyebrow="Services")


POLK_PERMIT = "Polk County's Building Division FAQ requires permits for 'concrete slabs adjacent to a principal or accessory structure, intended for support of a structure, elevated slabs, sidewalks and portions of driveways in the right of way or within the minimum setbacks'; drainage requirements apply; pavers in the right-of-way need the owner's recorded Concrete Driveway Paver Release Form. Building Division: 330 W. Church Street, Bartow, and 200 Government Center Blvd, Lake Alfred, (863) 534-6080."


def winter_haven():
    k = "winter-haven"
    body = sec("Between the Chain of Lakes and the ridge",
        cap("Winter Haven (population 60,837, 2025 EDR estimate) is the largest Polk ridge city we serve, 26 miles from Kissimmee: a 1920s–1960s core between the Chain of Lakes, mid-century neighborhoods off Cypress Gardens Boulevard and Havendale Boulevard, and 2015–2026 subdivisions along US-17 and toward Lake Alfred. The city has its own building division; unincorporated addresses follow Polk County. Soil is Candler and Tavares sand on the ridge with wetter margins at the lakes."),
        eyebrow="Winter Haven")
    body += sec("What changes here", f"<p>Lakefront lots on the Chain of Lakes have the flatwoods problem in a ridge town: Basinger and muck margins where a slab has to be raised and drained. Everywhere else the issue is the opposite, Candler sand that will not compact dry, so base is wetted before the plate goes over it ({guide('paver-base-flatwoods-vs-ridge')}). The older neighborhoods have oaks lifting walks and drives ({guide('tree-roots-driveways-central-florida')}); the newer subdivisions (Lake Lucerne, Lakeside Landings, Villamar, Peace Creek Reserve) have builder driveways cracking early on dry-placed base ({guide('why-concrete-cracks-osceola')}). Well irrigation outside the city utility area rust-stains light pavers ({guide('rust-stains-irrigation-well-water')}).</p>")
    body += sec("Permits", cap(POLK_PERMIT + " Inside Winter Haven's city limits the city's building division reviews permits; we confirm its flatwork rules by phone before quoting.") + f"<p>{juris('polk-county')}; {tool('permit-finder')} separates city and county addresses.</p>", cls="alt")
    body += four_services(k, "Replacement on the mid-century streets, extensions in the new subdivisions, apron to the county detail; base wetted and compacted.", "Rebuilds of settled builder drives; concrete apron avoids the Paver Release Form.", "Overlays on 2000s decks, travertine on lakefront homes; Polk's slab rule for decks adjacent to the house confirmed first.", "Early cracks on new drives, oak-lifted walks near the lakes, apron corners.")
    body += sec(f"Costs in Winter Haven ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "paver-driveway-concrete", "paver-pool-deck", "concrete-repair", "paver-sealing"]) + "<p>Polk ridge labor runs slightly below the Kissimmee index; travel is grouped with Auburndale and Lake Alfred visits.</p>", cls="alt")
    faqs = [
        faq("Do you cover Winter Haven from Kissimmee?", "Yes; it is about 26 miles and we group Polk ridge visits, so expect a site visit within three business days."),
        faq("City or county permit?", "City inside the limits, Polk County outside. The permit finder checks the address."),
        faq("Why raise a slab on a lakefront lot?", "Lake margins hold water at the surface in summer; a slab flush with grade settles unevenly."),
        faq("Do you have a Winter Haven-specific page for each service?", "Not yet; the Kissimmee service pages are the masters and this page covers what changes locally. We add local service pages when demand shows it."),
    ]
    return page(k, "Concrete & Pavers in Winter Haven, FL – Ridge and Lakes", "Concrete and paver work in Winter Haven: city vs. Polk County permits, Candler ridge sand vs. Chain of Lakes margins, early cracks on new subdivision driveways, oak-lifted walks, costs from the Cost Index.", "Concrete and pavers in Winter Haven, FL", body, faqs, ["polk-faq", "polk-paver-release", "sda", "edr"])


def auburndale():
    k = "auburndale"
    body = sec("Concrete and pavers in Auburndale",
        cap("Auburndale (population 21,677, 2025 EDR) sits on the ridge between Lake Ariana and Lake Arietta, 27 miles from Kissimmee, with a 1910s downtown, 1950s–1990s neighborhoods off Havendale Boulevard and US-92, and new subdivisions along Berkley Road. City limits use the city's building department; unincorporated addresses use Polk County. Candler sand needs a wetted base; lake margins need raised slabs."),
        eyebrow="Auburndale")
    body += sec("What changes here", f"<p>Auburndale's older streets are oak-lined and the drives are narrow 1950s–1970s slabs; replacement with a root barrier and an expansion joint at the apron is the usual job. The Berkley Road subdivisions (Berkley Ridge, Auburn Cove, Watercrest) are 2018–2026 builds with 16-foot driveways on dry-placed base that show early cracks; extensions and panel replacement over a wetted base are common. Lake Ariana and Lake Arietta lots have wet margins where pads and patios are raised ({guide('paver-base-flatwoods-vs-ridge')}).</p>")
    body += sec("Permits", cap(POLK_PERMIT + " Inside city limits, Auburndale's building department reviews; we confirm its flatwork rules by phone.") + f"<p>{juris('polk-county')}; {tool('permit-finder')}.</p>", cls="alt")
    body += four_services(k, "Narrow 1950s–70s drives replaced; new-subdivision extensions on a wetted base.", "Upgrades of builder drives; concrete apron at the street.", "Overlays and travertine on lake lots; slab rule confirmed with Polk.", "Early cracks, oak lifts, apron corners.")
    body += sec(f"Costs in Auburndale ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "paver-driveway-concrete", "paver-pool-deck", "concrete-repair", "concrete-patio"]), cls="alt")
    faqs = [
        faq("How far is Auburndale from Kissimmee?", "About 27 miles straight-line; visits within three business days, grouped with Winter Haven and Lake Alfred."),
        faq("Which permit office?", "City inside the limits; Polk County outside. The finder checks."),
        faq("Why do the new driveways crack?", "Dry-placed base on ridge sand, compacted by the first rainy season."),
        faq("Do you do lakefront work?", "Yes; lake-margin slabs are raised and drained."),
    ]
    return page(k, "Concrete & Pavers in Auburndale, FL – Ridge Lots, Lake Margins", "Concrete and paver work in Auburndale: oak-lined 1950s streets, Berkley Road subdivisions with early-cracking builder driveways, lake-margin slabs, city vs. Polk County permits, costs.", "Concrete and pavers in Auburndale, FL", body, faqs, ["polk-faq", "sda", "edr"])


def lake_alfred():
    k = "lake-alfred"
    body = sec("Concrete and pavers in Lake Alfred",
        cap("Lake Alfred (population 9,038, 2025 EDR) is the ridge town at US-17/92 and SR-557, 22 miles from Kissimmee, and home to Polk County's Northeast Government Center at 200 Government Center Blvd, the closest county permit office to our whole Polk territory. A small historic core, 1960s–1990s streets around Lake Alfred and Lake Rochelle, and 2019–2026 subdivisions along SR-557 and Buena Vista Drive. Candler sand; wetted base."),
        eyebrow="Lake Alfred")
    body += sec("What changes here", f"<p>Lake Alfred's growth is new: Lake Alfred Estates, Eden Hills, Magnolia Ridge and the SR-557 corridor were platted since 2018, and their builder driveways and patios are the early-cracking, dry-base kind we see across the ridge ({guide('why-concrete-cracks-osceola')}). The older streets have the oak and narrow-drive pattern. Lakefront lots on Lake Alfred and Lake Rochelle get raised slabs. The county's Northeast Government Center in town means permit questions get answered in person the same day.</p>")
    body += sec("Permits", cap(POLK_PERMIT + " Inside city limits, Lake Alfred's building department reviews; confirm by phone.") + f"<p>{juris('polk-county')}; {tool('permit-finder')}.</p>", cls="alt")
    body += four_services(k, "New-subdivision extensions and panel replacement over a wetted base.", "Concrete-to-paver conversions with a concrete apron.", "Overlays on new decks whose backfill settled.", "Early cracks and settled aprons.")
    body += sec(f"Costs in Lake Alfred ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-repair", "paver-driveway-concrete", "paver-pool-deck"]), cls="alt")
    faqs = [
        faq("Where is the closest Polk permit office?", "The Northeast Government Center, 200 Government Center Blvd, in Lake Alfred."),
        faq("Do you serve Lake Alfred?", "Yes; 22 miles from Kissimmee, visits within three business days."),
        faq("Why is my new driveway cracking?", "Dry-placed base on Candler sand; rebuilt wet under the new section it holds."),
        faq("Lakefront slabs?", "Raised and drained on the lake margins."),
    ]
    return page(k, "Concrete & Pavers in Lake Alfred, FL – Near Polk's NE Center", "Concrete and paver work in Lake Alfred: new SR-557 subdivisions with early-cracking builder driveways, lakefront slabs, the Northeast Government Center for Polk permits, costs.", "Concrete and pavers in Lake Alfred, FL", body, faqs, ["polk-faq", "sda", "edr"])


def dundee():
    k = "dundee"
    body = sec("Concrete and pavers in Dundee",
        cap("Dundee (population 5,847, 2025 EDR) is a citrus-era ridge town on US-27 between Lake Hamilton and Lake Wales, 22 miles from Kissimmee, with a small 1920s core, 1970s–1990s streets around Lake Marie and Lake Annie, and 2020–2026 subdivisions along US-27 and Dundee Road. Town limits use the town's building process; unincorporated addresses use Polk County. Candler sand on the ridge; wetted base."),
        eyebrow="Dundee")
    body += sec("What changes here", f"<p>Dundee's work is split between replacing 1970s–1990s drives on the lake streets and fixing early cracks on the new subdivisions' builder driveways (Dundee Groves, Ridge at Lake Marie, Sable Palms). Larger unincorporated lots off Dundee Road and toward Lake Hamilton keep boats and campers, so 6-inch pads with a rebar grid are common ({svc('concrete-slabs')}). The ridge's Candler sand compacts only wet ({guide('paver-base-flatwoods-vs-ridge')}).</p>")
    body += sec("Permits", cap(POLK_PERMIT + " Inside town limits, Dundee's building process applies; confirm by phone.") + f"<p>{juris('polk-county')}; {tool('permit-finder')}.</p>", cls="alt")
    body += four_services(k, "1970s–90s lake-street replacements; new-subdivision panel repairs.", "Upgrades with a concrete apron.", "Overlays on new decks.", "Early cracks, settled aprons, boat-pad edges.")
    body += sec(f"Costs in Dundee ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "concrete-slab-pad", "concrete-repair"]), cls="alt")
    faqs = [
        faq("Do you serve Dundee?", "Yes; 22 miles from Kissimmee, grouped with Lake Wales and Haines City visits."),
        faq("Town or county permit?", "Town inside the limits; Polk County outside."),
        faq("Boat pad spec?", "Six inches of 4,000 psi with a #4 grid on a wetted, compacted base."),
        faq("Why raise a slab by the lake?", "Lake margins hold water in summer; the slab is set above it with a swale."),
    ]
    return page(k, "Concrete & Pavers in Dundee, FL – Ridge Town, Lake Streets", "Concrete and paver work in Dundee: lake-street driveway replacements, early cracks on new US-27 subdivisions, boat and RV pads on unincorporated lots, town vs. Polk County permits, costs.", "Concrete and pavers in Dundee, FL", body, faqs, ["polk-faq", "sda", "edr"])


def lake_wales():
    k = "lake-wales"
    body = sec("At the top of the Lake Wales Ridge",
        cap("Lake Wales (population 17,748, 2025 EDR) sits at the high point of the Lake Wales Ridge, 28 miles from Kissimmee: a 1910s–1920s downtown, mid-century neighborhoods around Lake Wailes and Crooked Lake, and new subdivisions along US-27 and SR-60. The city has its own building division; unincorporated addresses use Polk County. The soil is Candler and Astatula sand, the driest ground we work on, and the lots slope more than anywhere else in our territory."),
        eyebrow="Lake Wales")
    body += sec("What changes here", f"<p>Slope. Lake Wales lots fall enough that driveways are pitched to the street with a trench drain at the garage and patios are stepped or built up on the low side; the base under both is wetted before compaction because Candler and Astatula sands will not densify dry ({guide('paver-base-flatwoods-vs-ridge')}). The historic streets have oaks and narrow drives; the newer subdivisions (Lake Wales Highlands, Leoma's Landing, Whispering Ridge) have builder driveways on dry-placed base. No water table to fight except at the lake margins.</p>")
    body += sec("Permits", cap(POLK_PERMIT + " Inside city limits, Lake Wales' building division reviews; confirm by phone.") + f"<p>{juris('polk-county')}; {tool('permit-finder')}.</p>", cls="alt")
    body += four_services(k, "Sloped drives with a garage trench drain; historic-street replacements.", "Rebuilds on wetted base with a concrete apron.", "Overlays and travertine on sloped lots; deck drainage to the low side.", "Early cracks and oak lifts.")
    body += sec(f"Costs in Lake Wales ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-patio", "paver-driveway-concrete", "concrete-repair"]) + "<p>Lake Wales is at the edge of our radius; visits are grouped with Dundee and Haines City and priced with travel in mind.</p>", cls="alt")
    faqs = [
        faq("Is Lake Wales in your service area?", "Yes, at the edge: 28 miles straight-line, visits within three business days, grouped with Dundee and Haines City."),
        faq("How do you handle a sloped driveway?", "Pitch to the street where possible; a trench drain at the garage where the drive falls toward it."),
        faq("Why wet the base?", "Candler and Astatula sands compact only wet; dry base settles the first rainy season."),
        faq("City or county permit?", "City inside the limits; Polk County outside."),
    ]
    return page(k, "Concrete & Pavers in Lake Wales, FL – Sloped Ridge Lots", "Concrete and paver work in Lake Wales: sloped lots on Candler and Astatula sand, trench drains at the garage, stepped patios, historic-street oaks, new US-27 subdivisions, city vs. Polk permits, costs.", "Concrete and pavers in Lake Wales, FL", body, faqs, ["polk-faq", "sda", "edr"])


def polk_city():
    k = "polk-city"
    body = sec("Concrete and pavers in Polk City",
        cap("Polk City (population 3,007, 2025 EDR) is the small town at SR-33 and I-4 on the north end of the ridge, 27 miles from Kissimmee, surrounded by unincorporated Polk lots of an acre and up toward the Green Swamp. The work is rural: long driveways, RV and boat pads, workshop slabs, and pads that have to stay above water on the swamp-edge ground. Town limits use the town's process; most addresses are county."),
        eyebrow="Polk City")
    body += sec("What changes here", f"<p>Polk City sits where the dry Candler ridge meets the wet flatwoods and the Green Swamp: a lot on SR-33 may be Candler sand that needs a wetted base, and a lot two miles east on Fussels Corner Road may be Smyrna or Basinger sand with a summer water table at the surface where every pad is raised ({guide('paver-base-flatwoods-vs-ridge')}). Most lots are on wells and septic, so drives are routed clear of drainfields ({guide('septic-drainfield-concrete-driveway')}) and iron-stained by irrigation ({guide('rust-stains-irrigation-well-water')}). Mixer access across pasture and culverts is checked before we quote.</p>")
    body += sec("Permits", cap(POLK_PERMIT + " Inside town limits, Polk City's process applies; confirm by phone. Pre-manufactured storage buildings are permitted structures.") + f"<p>{juris('polk-county')}; {tool('permit-finder')}.</p>", cls="alt")
    body += four_services(k, "Long rural drives quoted by the foot; turnarounds and boat pads.", "Less common here; concrete apron rules apply.", "Rare; overlays on the few subdivision decks.", "Settled pads and aprons; drainfield-adjacent repairs.")
    body += sec(f"Costs in Polk City ({COST_INDEX_RELEASE['label']})", cost_rows(["concrete-driveway-broom", "concrete-driveway-6in", "concrete-slab-pad", "concrete-repair"]) + "<p>Long drives and workshop slabs dominate; the calculator gives a first number by the foot.</p>", cls="alt")
    faqs = [
        faq("Do you pour long rural driveways in Polk City?", "Yes, quoted by the foot after a truck-access and septic check."),
        faq("Which soil is my lot?", "Ridge sand or flatwoods sand depending on which side of SR-33; the finder shows the county and we probe on site."),
        faq("Workshop slab?", "Six inches with a thickened edge and the building supplier's anchor layout; the building is permitted as an accessory structure."),
        faq("How far from Kissimmee?", "About 27 miles; visits within three business days."),
    ]
    return page(k, "Concrete & Pavers in Polk City, FL – Rural Lots, Pads, Drives", "Concrete and paver work in Polk City: long rural driveways, RV and workshop slabs, ridge sand vs. Green Swamp flatwoods, septic and well lots, Polk County permit rules, costs.", "Concrete and pavers in Polk City, FL", body, faqs, ["polk-faq", "sda", "edr"])


def get_pages():
    return [winter_haven(), auburndale(), lake_alfred(), dundee(), lake_wales(), polk_city()]
