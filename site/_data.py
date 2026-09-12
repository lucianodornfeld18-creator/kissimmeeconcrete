# -*- coding: utf-8 -*-
"""Shared structural data for kissimmeeconcrete.com.

Positioning (owner-approved model, same as the sibling hubs built for this
provider): Kissimmee Concrete presents as a concrete, paver and hardscape
contractor serving Kissimmee, Osceola County and the Polk County ridge. Trust
claims are limited to what the owner has approved for the network: insured,
free estimates, written workmanship warranty. Never "licensed" without a
number, never a street address, never reviews/ratings/years/project counts
that are not documented. See OWNER-INPUTS.md for every pending fact.
"""
import datetime

DOMAIN = "kissimmeeconcrete.com"
BASE_URL = f"https://{DOMAIN}"
PUBLIC_NAME = "Kissimmee Concrete"
BUILD_DATE = datetime.date.today().isoformat()
LAUNCH_DATE = "2026-09-10"   # first build; git commit dates take over once the repo has history

# ---------------------------------------------------------------------------
# Business facts. The number is the site's own tracked Twilio line, which
# screens robocalls, whispers "press any key to accept" on the owner's leg and
# falls through to a transcribed voicemail. See twilio/README.md. Setting
# PHONE_DISPLAY to None removes every call-to-action rather than showing a
# placeholder.
# ---------------------------------------------------------------------------
PHONE_DISPLAY = "(689) 263-6255"
PHONE_E164 = "+16892636255"
EMAIL = "hello@kissimmeeconcrete.com"
TURNSTILE_SITE_KEY = None     # public Turnstile key for this domain (OWNER-INPUTS.md)

BUSINESS = {
    "public_name": PUBLIC_NAME,
    "domain": DOMAIN,
    "email": EMAIL,
    "trust_points": ["Concrete, Paver & Hardscape Contractor", "Insured", "Free On-Site Estimates", "Written Workmanship Warranty"],
    "blurb": (
        "Kissimmee Concrete installs and repairs concrete driveways, patios, pool decks, slabs and "
        "walkways, and builds paver driveways, pool decks, patios and outdoor living spaces across "
        "Kissimmee, St. Cloud, Celebration, Poinciana, Harmony, the Four Corners resort corridor and "
        "the Polk County ridge from Davenport to Lake Wales. Insured, free on-site estimates, written "
        "workmanship warranty."
    ),
    "service_area_short": "Kissimmee, St. Cloud, Celebration, Poinciana, Buenaventura Lakes, Harmony, Four Corners, ChampionsGate, Reunion, Davenport, Haines City and the Polk County ridge (about 40 miles around Kissimmee)",
    "hours": "Mon–Fri 7:30 a.m.–6 p.m., Sat 8 a.m.–1 p.m.",
}

# ---------------------------------------------------------------------------
# Services. pillar: concrete | pavers | coatings. enabled False = written but not built.
# ---------------------------------------------------------------------------
SERVICES = {
    "concrete-driveways": {"name": "Concrete Driveways", "short": "New, replacement, widening, extensions, aprons and turnarounds", "route": "/concrete/driveways/", "pillar": "concrete", "enabled": True},
    "concrete-patios": {"name": "Concrete Patios", "short": "Broom, smooth, exposed-aggregate and colored patio slabs", "route": "/concrete/patios/", "pillar": "concrete", "enabled": True},
    "concrete-pool-decks": {"name": "Concrete Pool Decks", "short": "Textured and cool-deck finishes, deck resurfacing", "route": "/concrete/pool-decks/", "pillar": "concrete", "enabled": True},
    "concrete-stamped": {"name": "Stamped & Decorative Concrete", "short": "Patterns, integral color, release colors and sealers", "route": "/concrete/stamped/", "pillar": "concrete", "enabled": True},
    "concrete-slabs": {"name": "Concrete Slabs & Pads", "short": "Shed, AC, generator, RV, boat, hot-tub, workshop and dumpster pads", "route": "/concrete/slabs/", "pillar": "concrete", "enabled": True},
    "concrete-sidewalks-walkways": {"name": "Sidewalks & Walkways", "short": "Front walks, side yards, right-of-way sidewalk sections", "route": "/concrete/sidewalks-walkways/", "pillar": "concrete", "enabled": True},
    "concrete-repair": {"name": "Concrete Repair", "short": "Cracks, spalling, sunken sections, trip hazards, lifting decisions", "route": "/concrete/repair/", "pillar": "concrete", "enabled": True},
    "concrete-resurfacing": {"name": "Concrete Resurfacing & Overlays", "short": "Polymer-modified overlays, textured and knock-down finishes", "route": "/concrete/resurfacing/", "pillar": "concrete", "enabled": True},
    "concrete-architectural": {"name": "Architectural Concrete", "short": "Honed, board-formed and custom finishes", "route": "/concrete/architectural/", "pillar": "concrete", "enabled": True},
    "concrete-commercial": {"name": "Commercial Concrete & Parking Lots", "short": "Flatwork, dumpster pads, sidewalks, small parking areas", "route": "/concrete/commercial/", "pillar": "concrete", "enabled": True},
    "paver-driveways": {"name": "Paver Driveways", "short": "Concrete pavers, clay brick and permeable systems", "route": "/pavers/driveways/", "pillar": "pavers", "enabled": True},
    "paver-patios": {"name": "Paver Patios", "short": "Lanai extensions, backyard patios, fire-pit areas", "route": "/pavers/patios/", "pillar": "pavers", "enabled": True},
    "paver-pool-decks": {"name": "Paver Pool Decks", "short": "Paver decks and remodels over existing concrete", "route": "/pavers/pool-decks/", "pillar": "pavers", "enabled": True},
    "paver-travertine": {"name": "Travertine", "short": "Travertine pool decks, patios and driveways", "route": "/pavers/travertine/", "pillar": "pavers", "enabled": True},
    "paver-marble-porcelain": {"name": "Marble & Large-Format Porcelain", "short": "Marble decks and 24x24 and larger porcelain pavers", "route": "/pavers/marble-porcelain/", "pillar": "pavers", "enabled": True},
    "paver-walkways-steps": {"name": "Paver Walkways & Steps", "short": "Front walks, side paths, entry steps and stoops", "route": "/pavers/walkways-steps/", "pillar": "pavers", "enabled": True},
    "paver-sealing": {"name": "Paver Sealing & Cleaning", "short": "Clean, re-sand with polymeric sand, seal or re-seal", "route": "/pavers/sealing/", "pillar": "pavers", "enabled": True},
    "paver-repair": {"name": "Paver Repair", "short": "Sunken areas, edge failure, weeds, ants, replacement pieces", "route": "/pavers/repair/", "pillar": "pavers", "enabled": True},
    "paver-retaining-walls-outdoor-living": {"name": "Retaining Walls & Outdoor Living", "short": "Decorative segmental walls, seat walls, fire pits, summer kitchens", "route": "/pavers/retaining-walls-outdoor-living/", "pillar": "pavers", "enabled": True},
    "paver-artificial-turf": {"name": "Artificial Turf", "short": "Turf strips, side yards and putting-green areas tied into hardscape", "route": "/pavers/artificial-turf/", "pillar": "pavers", "enabled": True},
    "paver-outdoor-lighting": {"name": "Outdoor Lighting", "short": "Low-voltage lighting built into pavers, steps and pillars", "route": "/pavers/outdoor-lighting/", "pillar": "pavers", "enabled": True},
    "coatings-garage-floors": {"name": "Epoxy & Polyaspartic Garage Floors", "short": "Flake and solid-color garage floor coatings", "route": "/coatings/garage-floors/", "pillar": "coatings", "enabled": True},
    "exterior-stucco": {"name": "Stucco Installation & Repair", "short": "Patch, crack and full-wall stucco work", "route": "/exterior/stucco/", "pillar": "coatings", "enabled": False},
}
SERVICE_ORDER = [k for k, v in SERVICES.items() if v["enabled"]]
CONCRETE_SERVICES = [k for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "concrete"]
PAVER_SERVICES = [k for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "pavers"]
COATING_SERVICES = [k for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "coatings"]

# ---------------------------------------------------------------------------
# Cities. tier 1 = city hub + selected city×service; tier 2 = city hub only;
# county = county hub. miles = straight line from 28.2920,-81.4076 (Census
# Gazetteer 2024 internal points). drive = rough estimate (miles*1.3/32 mph).
# ---------------------------------------------------------------------------
CITIES = {
    "kissimmee": {"name": "Kissimmee", "route": "/areas/kissimmee/", "county": "Osceola", "tier": 1, "miles": 0, "jurisdiction": "city-of-kissimmee", "alt_jurisdiction": "osceola-county", "pop": "87,442 (city, 2025 EDR)"},
    "st-cloud": {"name": "St. Cloud", "route": "/areas/st-cloud/", "county": "Osceola", "tier": 1, "miles": 8.5, "jurisdiction": "city-of-st-cloud", "alt_jurisdiction": "osceola-county", "pop": "76,970 (city, 2025 EDR)"},
    "celebration": {"name": "Celebration", "route": "/areas/celebration/", "county": "Osceola", "tier": 1, "miles": 8.8, "jurisdiction": "osceola-county", "pop": "CDP"},
    "poinciana": {"name": "Poinciana", "route": "/areas/poinciana/", "county": "Osceola / Polk", "tier": 1, "miles": 12.7, "jurisdiction": "osceola-county", "alt_jurisdiction": "polk-county", "pop": "CDP"},
    "buenaventura-lakes": {"name": "Buenaventura Lakes", "route": "/areas/buenaventura-lakes/", "county": "Osceola", "tier": 1, "miles": 4.4, "jurisdiction": "osceola-county", "pop": "CDP"},
    "four-corners": {"name": "Four Corners", "route": "/areas/four-corners/", "county": "Osceola / Polk / Lake / Orange", "tier": 1, "miles": 14.9, "jurisdiction": "polk-county", "alt_jurisdiction": "osceola-county", "pop": "CDP"},
    "champions-gate": {"name": "ChampionsGate", "route": "/areas/champions-gate/", "county": "Osceola", "tier": 1, "miles": 15, "jurisdiction": "osceola-county", "pop": "community"},
    "reunion": {"name": "Reunion", "route": "/areas/reunion/", "county": "Osceola", "tier": 1, "miles": 13, "jurisdiction": "osceola-county", "pop": "community"},
    "davenport": {"name": "Davenport", "route": "/areas/davenport/", "county": "Polk", "tier": 1, "miles": 15.3, "jurisdiction": "polk-county", "pop": "14,031 (city, 2025 EDR)"},
    "haines-city": {"name": "Haines City", "route": "/areas/haines-city/", "county": "Polk", "tier": 1, "miles": 17.8, "jurisdiction": "polk-county", "pop": "44,215 (city, 2025 EDR)"},
    "harmony": {"name": "Harmony & Narcoossee", "route": "/areas/harmony/", "county": "Osceola", "tier": 1, "miles": 14, "jurisdiction": "osceola-county", "pop": "communities"},
    "winter-haven": {"name": "Winter Haven", "route": "/areas/winter-haven/", "county": "Polk", "tier": 2, "miles": 26.1, "jurisdiction": "polk-county", "pop": "60,837 (city, 2025 EDR)"},
    "auburndale": {"name": "Auburndale", "route": "/areas/auburndale/", "county": "Polk", "tier": 2, "miles": 26.9, "jurisdiction": "polk-county", "pop": "21,677 (city, 2025 EDR)"},
    "lake-alfred": {"name": "Lake Alfred", "route": "/areas/lake-alfred/", "county": "Polk", "tier": 2, "miles": 21.6, "jurisdiction": "polk-county", "pop": "9,038 (city, 2025 EDR)"},
    "dundee": {"name": "Dundee", "route": "/areas/dundee/", "county": "Polk", "tier": 2, "miles": 22.4, "jurisdiction": "polk-county", "pop": "5,847 (town, 2025 EDR)"},
    "lake-wales": {"name": "Lake Wales", "route": "/areas/lake-wales/", "county": "Polk", "tier": 2, "miles": 28.2, "jurisdiction": "polk-county", "pop": "17,748 (city, 2025 EDR)"},
    "polk-city": {"name": "Polk City", "route": "/areas/polk-city/", "county": "Polk", "tier": 2, "miles": 26.8, "jurisdiction": "polk-county", "pop": "3,007 (town, 2025 EDR)"},
}
TIER1 = [k for k, v in CITIES.items() if v["tier"] == 1]
TIER2 = [k for k, v in CITIES.items() if v["tier"] == 2]
CITY_ORDER = TIER1 + TIER2

COUNTY_HUBS = {
    "osceola-county": {"name": "Osceola County", "route": "/areas/osceola-county/"},
    "polk-county": {"name": "Polk County", "route": "/areas/polk-county/"},
    "orange-county-south": {"name": "South Orange County", "route": "/areas/orange-county-south/"},
}


def drive_estimate(miles):
    """Rough drive time in minutes from Kissimmee (labelled as an estimate wherever shown)."""
    if not miles:
        return 0
    return int(round(miles * 1.3 / 32 * 60 / 5.0) * 5)


# city×service pages actually built (44). Kissimmee is the anchor of the service pages.
CITY_SERVICES = [
    ("st-cloud", "concrete-driveways"), ("st-cloud", "concrete-slabs"), ("st-cloud", "concrete-repair"), ("st-cloud", "paver-driveways"), ("st-cloud", "paver-pool-decks"), ("st-cloud", "paver-sealing"),
    ("celebration", "paver-driveways"), ("celebration", "paver-pool-decks"), ("celebration", "paver-sealing"), ("celebration", "paver-walkways-steps"), ("celebration", "concrete-repair"),
    ("poinciana", "concrete-driveways"), ("poinciana", "concrete-patios"), ("poinciana", "concrete-repair"), ("poinciana", "paver-driveways"),
    ("buenaventura-lakes", "concrete-driveways"), ("buenaventura-lakes", "concrete-repair"), ("buenaventura-lakes", "concrete-resurfacing"), ("buenaventura-lakes", "paver-driveways"),
    ("four-corners", "paver-pool-decks"), ("four-corners", "paver-sealing"), ("four-corners", "paver-driveways"), ("four-corners", "concrete-repair"),
    ("champions-gate", "paver-pool-decks"), ("champions-gate", "paver-sealing"), ("champions-gate", "paver-driveways"), ("champions-gate", "concrete-repair"),
    ("reunion", "paver-pool-decks"), ("reunion", "paver-travertine"), ("reunion", "paver-sealing"), ("reunion", "paver-driveways"),
    ("davenport", "concrete-driveways"), ("davenport", "paver-driveways"), ("davenport", "paver-pool-decks"), ("davenport", "concrete-repair"), ("davenport", "concrete-slabs"),
    ("haines-city", "concrete-driveways"), ("haines-city", "concrete-patios"), ("haines-city", "concrete-repair"), ("haines-city", "paver-driveways"),
    ("harmony", "concrete-driveways"), ("harmony", "concrete-slabs"), ("harmony", "paver-driveways"), ("harmony", "paver-pool-decks"),
]


def city_service_route(city_key, service_key):
    return SERVICES[service_key]["route"] + city_key + "/"


# ---------------------------------------------------------------------------
# Permit jurisdictions (facts verified 2026-09-10; see research/05-*.md)
# ---------------------------------------------------------------------------
JURISDICTIONS = {
    "city-of-kissimmee": {"name": "City of Kissimmee", "route": "/permits/city-of-kissimmee/", "phone": "407-518-2278", "office": "Engineering Division, 101 Church Street, 3rd Floor, Kissimmee, FL 34741", "portal": "https://cityofkissimmeefl-energovweb.tylerhost.net/apps/selfservice", "portal_name": "EnerGov Citizen Self Service"},
    "osceola-county": {"name": "Unincorporated Osceola County", "route": "/permits/osceola-county/", "phone": "407-742-0200", "office": "1 Courthouse Square, Suite 1400, Kissimmee, FL 34741", "portal": "https://permits.osceola.org/", "portal_name": "Osceola County Permit Center (Accela)"},
    "city-of-st-cloud": {"name": "City of St. Cloud", "route": "/permits/city-of-st-cloud/", "phone": "407-957-7300", "office": "Building Department, 1300 9th Street, St. Cloud, FL 34769", "portal": "https://stcloudflpermits.selectpaytoday.com/", "portal_name": "St. Cloud Building Permit Portal"},
    "polk-county": {"name": "Polk County (unincorporated)", "route": "/permits/polk-county/", "phone": "(863) 534-6080", "office": "Building Division, 330 W. Church Street, Bartow, FL 33830; Northeast Government Center, 200 Government Center Blvd, Lake Alfred, FL 33850", "portal": "https://www.polkfl.gov/services/building/permitting/", "portal_name": "Polk County Building Permitting"},
    "orange-county": {"name": "Orange County (unincorporated)", "route": "/permits/orange-county/", "phone": "407-836-5550", "office": "Division of Building Safety, 201 S. Rosalind Ave, Orlando, FL 32801", "portal": "https://www.orangecountyfl.net/PermitsLicenses/", "portal_name": "Orange County Fast Track"},
}

HOAS = {
    "poinciana-apv": {"name": "Association of Poinciana Villages (APV)", "route": "/hoa/poinciana-apv/", "city": "poinciana"},
    "solivita": {"name": "Solivita", "route": "/hoa/solivita/", "city": "poinciana"},
    "celebration": {"name": "Celebration (CROA)", "route": "/hoa/celebration/", "city": "celebration"},
    "bellalago": {"name": "Bellalago & Isles of Bellalago", "route": "/hoa/bellalago/", "city": "kissimmee"},
    "solterra": {"name": "Solterra Resort", "route": "/hoa/solterra/", "city": "davenport"},
}

COMPARISONS = {
    "concrete-vs-pavers": {"name": "Concrete vs. Pavers", "route": "/compare/concrete-vs-pavers/"},
    "travertine-vs-concrete-pavers": {"name": "Travertine vs. Concrete Pavers", "route": "/compare/travertine-vs-concrete-pavers/"},
    "stamped-vs-pavers": {"name": "Stamped Concrete vs. Pavers", "route": "/compare/stamped-vs-pavers/"},
    "resurface-vs-replace": {"name": "Resurface vs. Replace", "route": "/compare/resurface-vs-replace/"},
    "4-inch-vs-6-inch": {"name": "4-Inch vs. 6-Inch Concrete", "route": "/compare/4-inch-vs-6-inch/"},
    "rebar-vs-fiber-vs-mesh": {"name": "Rebar vs. Fiber vs. Wire Mesh", "route": "/compare/rebar-vs-fiber-vs-mesh/"},
    "cool-deck-vs-pavers": {"name": "Cool Deck vs. Pavers", "route": "/compare/cool-deck-vs-pavers/"},
    "sealer-types": {"name": "Sealer Types Compared", "route": "/compare/sealer-types/"},
}

TOOLS = {
    "permit-finder": {"name": "Permit & Jurisdiction Finder", "route": "/tools/permit-finder/", "short": "Type an address; see whether it is City of Kissimmee, St. Cloud, unincorporated Osceola, Polk or Orange, and what that means for a driveway, patio, slab or pavers"},
    "concrete-paver-calculator": {"name": "Concrete & Paver Calculator", "route": "/tools/concrete-paver-calculator/", "short": "Cubic yards, bags, base depth, paver count, polymeric sand and a dated planning range"},
    "concrete-vs-pavers": {"name": "Concrete vs. Pavers Decision Tool", "route": "/tools/concrete-vs-pavers/", "short": "Answer eight questions about use, budget, HOA, heat and resale; get a recommendation with reasons"},
    "hoa-packet-checklist": {"name": "HOA / ARC Packet Checklist", "route": "/tools/hoa-packet-checklist/", "short": "What APV, Solivita, Celebration, Bellalago and Solterra ask for before they approve pavers or a driveway change"},
    "pour-calendar": {"name": "Pour Calendar", "route": "/tools/pour-calendar/", "short": "Rain days, highs and lows by month from the Kissimmee 2 NOAA station, with the pour window we recommend"},
    "ask-the-estimator": {"name": "Ask the Estimator", "route": "/tools/ask-the-estimator/", "short": "Short answers to real questions we get by phone and form, added as they come in"},
    "project-brief": {"name": "Project Brief Generator", "route": "/tools/project-brief/", "short": "Build a one-page brief with size, material, finish, drainage, access and HOA notes so three contractors quote the same job"},
}
TOOL_ORDER = list(TOOLS.keys())

GUIDES = {
    "why-concrete-cracks-osceola": {"name": "Why Concrete Cracks in Osceola County (and Which Cracks Matter)", "route": "/guides/why-concrete-cracks-osceola/"},
    "rust-stains-irrigation-well-water": {"name": "Rust Stains From Well-Water Irrigation: Identify, Remove, Prevent", "route": "/guides/rust-stains-irrigation-well-water/"},
    "driveway-widening-rules-osceola": {"name": "Driveway Widening Rules: Osceola County, Kissimmee and St. Cloud", "route": "/guides/driveway-widening-rules-osceola/"},
    "rainy-season-concrete-scheduling": {"name": "Pouring Concrete in the Rainy Season: How We Schedule Around Afternoon Storms", "route": "/guides/rainy-season-concrete-scheduling/"},
    "how-to-verify-a-concrete-contractor-florida": {"name": "How to Check a Concrete or Paver Contractor Before You Sign", "route": "/guides/how-to-verify-a-concrete-contractor-florida/"},
    "vacation-rental-owner-hardscape-guide": {"name": "Pool Decks and Driveways for Vacation Rental Owners in Four Corners, ChampionsGate and Reunion", "route": "/guides/vacation-rental-owner-hardscape-guide/"},
    "tree-roots-driveways-central-florida": {"name": "Live Oak Roots and Driveways: What Lifts a Slab and What to Do", "route": "/guides/tree-roots-driveways-central-florida/"},
    "paver-base-flatwoods-vs-ridge": {"name": "Paver Base on Flatwoods Sand vs. Ridge Sand: Osceola and Polk Are Not the Same", "route": "/guides/paver-base-flatwoods-vs-ridge/"},
    "buenaventura-lakes-driveway-replacement": {"name": "Replacing a 1980s Driveway in Buenaventura Lakes: What We Find Under the Old Slab", "route": "/guides/buenaventura-lakes-driveway-replacement/"},
    "septic-drainfield-concrete-driveway": {"name": "Septic Drainfields and Driveways on Rural St. Cloud and Harmony Lots", "route": "/guides/septic-drainfield-concrete-driveway/"},
    "polymeric-sand-guide": {"name": "Polymeric Sand: When It Works, When It Fails, and How We Install It", "route": "/guides/polymeric-sand-guide/"},
    "concrete-curing-florida-heat": {"name": "Curing Concrete in Central Florida Heat: 7 Days, 28 Days and What Happens In Between", "route": "/guides/concrete-curing-florida-heat/"},
    "surface-temperature-pool-decks": {"name": "How Hot Does a Pool Deck Get? Surface Temperatures by Material", "route": "/guides/surface-temperature-pool-decks/"},
    "hb-803-permit-exemption": {"name": "Florida's $7,500 Permit Exemption (HB 803) and Small Concrete Jobs", "route": "/guides/hb-803-permit-exemption/"},
}
GUIDE_ORDER = list(GUIDES.keys())

FAQ_HUBS = {
    "faq": {"name": "FAQ", "route": "/faq/"},
    "faq-concrete": {"name": "Concrete FAQ", "route": "/faq/concrete/"},
    "faq-pavers": {"name": "Paver FAQ", "route": "/faq/pavers/"},
    "faq-permits-hoa": {"name": "Permits & HOA FAQ", "route": "/faq/permits-hoa/"},
    "faq-cost": {"name": "Cost FAQ", "route": "/faq/cost/"},
}

NAV_PRIMARY = [
    ("Concrete", "/concrete/"),
    ("Pavers", "/pavers/"),
    ("Areas", "/areas/"),
    ("Pricing", "/pricing/"),
    ("Permits", "/permits/"),
    ("Tools", "/tools/"),
    ("Guides", "/guides/"),
]
FOOTER_LEGAL = [("Privacy", "/privacy/"), ("Terms", "/terms/"), ("Accessibility", "/accessibility/"), ("Editorial standards", "/editorial-standards/"), ("Data & methods", "/data-and-methods/")]

# Cost Index (Q3 2026 release). Planning ranges, installed, Kissimmee/Osceola market.
# Sources and method: content_pricing.py and /data-and-methods/. Not quotes.
COST_INDEX_RELEASE = {"label": "Q3 2026", "date": "2026-09-10", "next": "2026-12-10", "version": "1.0"}
COST_INDEX = [
    # key, service, unit, low, high, notes
    ("concrete-driveway-broom", "Concrete driveway, broom finish, 4 in, 3,000 psi, fiber + rebar at edges", "sq ft", 8.50, 13.50, "New pour on prepared base; demolition of an old slab adds $2.00–$4.00"),
    ("concrete-driveway-6in", "Concrete driveway, 6 in, 4,000 psi with #4 rebar grid (RV/boat loads)", "sq ft", 11.50, 17.00, "Thicker slab, more steel, same forming and finishing labor"),
    ("concrete-patio", "Concrete patio, 4 in, broom or smooth", "sq ft", 8.00, 12.50, "Small pours cost more per foot; under 200 sq ft expect the top of the range"),
    ("stamped-concrete", "Stamped concrete, integral color + release + sealer", "sq ft", 14.00, 22.00, "Pattern complexity and two-color work push toward the top"),
    ("concrete-slab-pad", "Concrete pad (shed, AC, generator, hot tub), 4 in", "sq ft", 9.00, 15.00, "Minimum-charge jobs; a 10x12 pad typically lands at $1,200–$1,900"),
    ("concrete-sidewalk", "Concrete walkway, 4 in, broom", "lin ft (4 ft wide)", 34.00, 52.00, "About $8.50–$13.00 per sq ft"),
    ("concrete-removal", "Demolition and haul-off of existing concrete", "sq ft", 2.00, 4.00, "Thicker slabs and limited access cost more"),
    ("concrete-resurfacing", "Polymer overlay / resurfacing over sound concrete", "sq ft", 5.00, 9.50, "Only over slabs with a stable base"),
    ("paver-driveway-concrete", "Paver driveway, concrete pavers (60–80 mm), 6 in limerock base", "sq ft", 14.00, 22.00, "Borders, bands and cuts add; removal of old concrete adds $2.00–$4.00"),
    ("paver-driveway-premium", "Paver driveway, premium line (Belgard Luxury, large format)", "sq ft", 20.00, 34.00, "Material-driven"),
    ("paver-patio", "Paver patio, concrete pavers, 4–5 in base", "sq ft", 13.00, 21.00, ""),
    ("paver-pool-deck", "Paver pool deck over existing deck (thin pavers, coping)", "sq ft", 15.00, 24.00, "Coping and drain work priced separately"),
    ("travertine-pool-deck", "Travertine pool deck, tumbled, sand-set or thin-set", "sq ft", 20.00, 36.00, "Marble and large-format porcelain run higher"),
    ("paver-walkway", "Paver walkway", "sq ft", 14.00, 24.00, "Narrow runs cost more per foot"),
    ("paver-sealing", "Paver clean, re-sand (polymeric) and seal", "sq ft", 1.75, 3.25, "Stripping an old failed sealer adds $0.75–$1.50"),
    ("paver-repair", "Paver lift-and-relay of a sunken area", "sq ft", 9.00, 16.00, "Minimum charge applies to small areas"),
    ("epoxy-garage", "Garage floor coating, flake system with polyaspartic top coat", "sq ft", 6.00, 10.00, "2-car garage (400–480 sq ft): $2,600–$4,600"),
    ("ready-mix", "Ready-mix concrete, 3,000–4,000 psi, delivered (Orlando market)", "cu yd", 175.00, 280.00, "Supplier public price lists, Sept 2026; short-load and fuel surcharges extra"),
]

SOURCES = {
    "osceola-22-50-6": ("Osceola County Code of Ordinances §22-50.6", "https://library.municode.com/fl/osceola_county/codes/code_of_ordinances"),
    "osceola-faq": ("Osceola County Building Office Frequent Questions", "https://www.osceola.org/Doing-Business/Building-and-Permits/Permit-Information/Building-Office-Frequent-Questions"),
    "osceola-permits": ("Osceola County Permit Center", "https://permits.osceola.org/"),
    "kissimmee-driveway": ("City of Kissimmee — Apply for Driveway / Sidewalk Construction", "https://www.kissimmee.gov/Business-Development/Development/Engineering/Apply-for-Driveway-Sidewalk-Construction"),
    "stcloud-permits": ("City of St. Cloud — Permit Information", "https://www.stcloudfl.gov/50/Permit-Information"),
    "polk-faq": ("Polk County Building Division FAQ", "https://www.polkfl.gov/services/building/faqs/"),
    "polk-paver-release": ("Polk County Concrete Driveway Paver Release Form (PD BLD 40)", "https://www.polkfl.gov/wp-content/uploads/2023/07/concrete-driveway-paver-release-form.pdf"),
    "orange-permit": ("Orange County — Do I Need a Permit", "https://www.orangecountyfl.net/PermitsLicenses/DoINeedaPermit.aspx"),
    "hb803": ("CS/CS/HB 803 (2026) Building Permits and Inspections — Florida Senate summary", "https://www.flsenate.gov/Committees/billsummaries/2026/html/803"),
    "apv": ("Poinciana Villages Design Control Board Criteria (2021)", "https://www.apvcommunity.com/association-of-poinciana-villages-o"),
    "solivita": ("Solivita Community Association Architectural Review Requirements (2013)", "https://aristainflorida.com/wp-content/uploads/2017/09/Solivita.5.Architectural-Review-Requirements-Final-11.22.13.pdf"),
    "celebration": ("Celebration Residential Owners Association — Architectural Review Committee", "https://celebration.fl.us/"),
    "bellalago": ("Bellalago HOA — Architectural Review", "https://bellalagohoa.com/architectural-review"),
    "solterra": ("Solterra Resort HOA — Architectural Guidelines, Standards & Criteria (2020)", "https://solterraresorthoa.com/documents/"),
    "noaa": ("NOAA NCEI U.S. Climate Normals 1991–2020, station USC00084625 Kissimmee 2, FL", "https://www.ncei.noaa.gov/access/us-climate-normals/"),
    "sda": ("USDA NRCS Soil Data Access (Osceola County FL097, Polk County FL105)", "https://sdmdataaccess.sc.egov.usda.gov/"),
    "fbc-r506": ("2023 Florida Building Code, Residential, Section R506 (concrete floors on ground)", "https://codes.iccsafe.org/content/FLRC2023P1"),
    "aci332": ("ACI 332 Residential Code Requirements for Structural Concrete", "https://www.concrete.org/"),
    "icpi": ("Concrete Masonry & Hardscapes Association (formerly ICPI) — installation guidance", "https://www.masonryandhardscapes.org/"),
    "edr": ("Florida EDR — 2025 estimates of population by county and municipality", "https://edr.state.fl.us/Content/local-government/data/county-municipal/2025adjpops.pdf"),
    "census": ("U.S. Census Bureau QuickFacts — Osceola County, Florida", "https://www.census.gov/quickfacts/osceolacountyflorida"),
    "gazetteer": ("U.S. Census Bureau 2024 Gazetteer Files (places)", "https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html"),
    "tigerweb": ("U.S. Census Bureau TIGERweb (city and county boundaries)", "https://tigerweb.geo.census.gov/"),
    "belgard": ("Belgard — find a dealer", "https://www.belgard.com/find-dealer/"),
    "tremron": ("Tremron — locations", "https://www.tremron.com/locations/"),
    "oldcastle": ("Oldcastle APG / Coastal — Florida masonry and hardscape", "https://www.oldcastlecoastal.com/"),
    "sunbiz": ("Florida Division of Corporations (Sunbiz)", "https://search.sunbiz.org/"),
    "dbpr": ("Florida DBPR license verification", "https://www.myfloridalicense.com/wl11.asp"),
}


def src(key, label=None):
    name, url = SOURCES[key]
    return f'<a href="{url}" rel="noopener" target="_blank">{label or name}</a>'
