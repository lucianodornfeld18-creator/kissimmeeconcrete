# -*- coding: utf-8 -*-
"""Garage floor coatings (published) and stucco (written, disabled until the owner confirms capacity)."""
from _data import SERVICES, COST_INDEX_RELEASE
from _helpers import cap, sec, table, svc, tool, guide, compare, hoa, faq, cost_rows, cost_range, steps, esc


def garage():
    k = "coatings-garage-floors"
    body = sec("What a garage floor coating costs in Kissimmee and what lasts",
        cap(f"A flake garage floor system with a moisture-tolerant epoxy base and a UV-stable polyaspartic top coat runs {cost_range('epoxy-garage')} installed in the {COST_INDEX_RELEASE['label']} Cost Index; a two-car garage of 400 to 480 square feet is $2,600 to $4,600. One to two days, cars back on the floor in 48 to 72 hours. The slab is diamond-ground, not acid-etched, and moisture-tested first, because Osceola slabs sit a foot above a wet-season water table."),
        eyebrow="Quick answer")
    body += sec("Epoxy, polyaspartic or both?",
        cap("Epoxy is thick, bonds hard to ground concrete, and yellows in sunlight. Polyaspartic (a polyurea) cures in hours, stays clear under UV and tolerates the heat of a west-facing garage, but is thinner and costs more. The system that holds up here is an epoxy or polyaspartic base coat for build and bond, a full broadcast of vinyl flake, and a polyaspartic top coat for UV and chemical resistance. Google Trends for the Orlando market shows 'polyaspartic vs epoxy' as the fastest-rising garage-floor query of the past five years.")
        + table(["", "100% solids epoxy", "Polyaspartic", "Hybrid (epoxy base + polyaspartic top)"], [
            ("Cure to drive on", "5–7 days", "24–48 hours", "48–72 hours"),
            ("UV", "yellows and chalks at the door", "stable", "stable top coat"),
            ("Hot-tire pickup", "possible on thin coats", "rare", "rare"),
            ("Moisture tolerance", "good with a moisture-mitigating primer", "lower; needs a dry, primed slab", "primer handles it"),
            ("Cost", "lowest", "highest", "middle"),
            ("Working time in a Kissimmee summer", "long", "15–20 minutes; crew-dependent", "manageable"),
        ]))
    body += sec("Why moisture testing comes first in Osceola County",
        f"""<p>Garage slabs in Kissimmee, St. Cloud and Poinciana sit on flatwoods sand with a water table about 12 inches down in summer, and most were poured without a vapor barrier before the 1990s. Moisture moving up through the slab is what lifts a coating in blisters within a year. We test with a calcium chloride kit or an in-situ probe; readings above the coating maker's limit get a moisture-mitigating epoxy primer or, in bad cases, a recommendation not to coat. Grinding rather than acid-etching opens the surface for bond and removes the curing compound builders leave behind. Cracks are routed and filled, and the cove at the wall is coated so water from a car does not sit at the joint.</p>""", cls="alt")
    body += sec("Process", steps([
        "Moisture test and inspection; move-out of the garage arranged (we can supply a pod for a day).",
        "Diamond grind to a CSP-2/3 profile, vacuum, crack and spall repair, joints filled or honored.",
        "Primer or base coat, rolled; full flake broadcast to rejection while wet.",
        "Scrape and vacuum the flake the next morning; polyaspartic top coat with anti-slip additive.",
        "Foot traffic in 6 to 12 hours, cars in 48 to 72, heavy shelving after 5 days.",
    ]))
    body += sec("Permits and HOA", f"<p>A floor coating is finish work; no permit in any of our jurisdictions. HOAs do not review interior garage floors. Coatings on exterior slabs (a lanai or a front walk) are a different product family and are reviewed where visible; Solterra allows only clear matte sealers on concrete without approval ({hoa('solterra')}).</p>", cls="alt")
    body += sec(f"Garage floor costs ({COST_INDEX_RELEASE['label']})", cost_rows(["epoxy-garage", "concrete-resurfacing"]) + "<p>Solid color without flake costs about 15 percent less; metallic epoxy about 40 percent more; adding the step and the apron a few hundred dollars. Three-car garages price by area. Moisture mitigation adds $1.50 to $2.50 per square foot when a test calls for it.</p>")
    faqs = [
        faq("How much does an epoxy garage floor cost in Kissimmee?", f"About {cost_range('epoxy-garage')} for a flake system with a polyaspartic top coat; a two-car garage is $2,600 to $4,600 in the {COST_INDEX_RELEASE['label']} index."),
        faq("Epoxy or polyaspartic?", "Both, in layers: an epoxy or polyaspartic base for bond, a flake broadcast, and a polyaspartic top coat for UV and hot tires. Pure epoxy yellows at the door; pure polyaspartic costs more and is less forgiving on damp slabs."),
        faq("Why did my last coating peel?", "Usually moisture from below or a slab that was acid-etched instead of ground. Grinding, testing and a mitigating primer are the difference."),
        faq("How long until I can park on it?", "48 to 72 hours for the hybrid system, 24 to 48 for full polyaspartic, 5 to 7 days for 100 percent solids epoxy."),
        faq("Is it slippery?", "Full flake gives texture; we add an anti-slip aggregate to the top coat as standard."),
        faq("Can you coat a lanai or pool deck?", "Exterior slabs take a different, UV-stable, textured system; see concrete resurfacing and pool decks for the options we use outdoors."),
    ]
    return {"route": SERVICES[k]["route"], "title": "Epoxy & Polyaspartic Garage Floors in Kissimmee, FL – Cost", "meta_description": "Garage floor coatings in Kissimmee: epoxy vs. polyaspartic vs. hybrid flake systems, moisture testing on slabs over a 12-inch water table, diamond grinding, cure times, cost for a two-car garage.", "h1": "Epoxy and polyaspartic garage floors in Kissimmee, FL", "breadcrumbs": [("Home", "/"), ("Pavers & coatings", "/pavers/"), (SERVICES[k]["name"], None)], "body_html": body, "faqs": faqs, "kind": "service", "service_key": k, "nav_active": "/pavers/", "sources": ["sda"]}


def stucco():
    """DISABLED until the owner confirms stucco capacity (registry: not_confirmed_do_not_use)."""
    k = "exterior-stucco"
    body = sec("Stucco repair and installation in Kissimmee",
        cap("Hairline stucco cracks at window corners and control joints are normal on Central Florida block homes; cracks wider than 1/16 inch, bulging, hollow sounds or staining at the bottom of a wall point to water behind the stucco and need a patch or a re-lath. Florida does not license stucco work at the state level and s. 489.117(4)(a) bars local licensing; check insurance and references instead."),
        eyebrow="Quick answer")
    body += sec("What we repair", "<p>Crack repair with elastomeric patch and texture matching, patching around new windows and doors, re-stucco of damaged wall sections over new lath and paper, and full re-texture where a previous repair shows. Painted finishes are matched by texture (sand, knockdown, dash) and primed for the painter.</p>")
    faqs = [faq("Are stucco cracks normal?", "Hairline cracks at corners and joints are. Wider, stepped or wet cracks are not."), faq("Do you need a license for stucco in Florida?", "No state license exists and local licensing is preempted by s. 489.117(4)(a). Verify insurance, Sunbiz registration and references.")]
    return {"route": SERVICES[k]["route"], "title": "Stucco Repair & Installation in Kissimmee, FL", "meta_description": "Stucco crack repair, patching and re-stucco on block homes in Kissimmee and Osceola County: which cracks matter, texture matching, and what to verify since Florida does not license stucco work.", "h1": "Stucco repair and installation in Kissimmee, FL", "breadcrumbs": [("Home", "/"), ("Exterior", "/pavers/"), (SERVICES[k]["name"], None)], "body_html": body, "faqs": faqs, "kind": "service", "service_key": k, "nav_active": "/pavers/", "sources": ["fs489117"]}


def get_pages():
    pages = [garage()]
    if SERVICES["exterior-stucco"]["enabled"]:
        pages.append(stucco())
    return pages
