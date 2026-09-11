# -*- coding: utf-8 -*-
"""FAQ hub and four topic FAQs. Short answers with the canonical page linked; long answers live on the canonical pages."""
from _data import FAQ_HUBS, COST_INDEX_RELEASE
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_range, related, esc

R = COST_INDEX_RELEASE["label"]


def hub():
    body = sec("Questions Kissimmee homeowners ask about concrete and pavers",
        cap("Short answers, grouped by topic, each pointing to the page that answers in full. Cost questions use the current Cost Index; permit questions quote the office; HOA questions quote the community's criteria where we have read them. If your question is not here, send it through the form and it will show up on Ask the Estimator."),
        eyebrow="FAQ")
    body += sec("By topic", cards([
        ("Concrete FAQ", "Thickness, PSI, reinforcement, cure time, cracks, color, cement vs. concrete, lifespan, insurance.", "/faq/concrete/", "Concrete questions"),
        ("Paver FAQ", "Base, polymeric sand, weeds and ants, efflorescence, sealing, pressure washing, brick vs. concrete pavers, travertine care.", "/faq/pavers/", "Paver questions"),
        ("Permits & HOA FAQ", "Who pulls the permit, licenses, HOA approval, what happens without it, HB 803, right-of-way.", "/faq/permits-hoa/", "Permit and HOA questions"),
        ("Cost FAQ", "What contractors charge, deposits, financing, asphalt vs. concrete vs. pavers, booking before spring.", "/faq/cost/", "Cost questions"),
    ], cols=4))
    body += sec("The six we hear most", "", cls="alt")
    faqs = [
        faq("How much does a concrete driveway cost in Kissimmee?", f"{cost_range('concrete-driveway-broom')} installed for a 4-inch broom finish in the {R} index; a two-car driveway is roughly $4,100 to $6,500 before removal. Full breakdown on the <a href=\"/pricing/concrete/\">concrete cost guide</a>."),
        faq("Do I need a permit for a driveway?", "Yes in every jurisdiction here: Kissimmee's Engineering application, Osceola's county driveway permit (24-ft max), St. Cloud's Building Department, Polk's right-of-way rule, Orange's general rule. <a href=\"/permits/\">Permits hub</a>."),
        faq("Are you licensed?", "Florida does not license concrete flatwork, pavers or stucco at the state level, and s. 489.117(4)(a) bars local licenses for driveway and paver work. We are insured and put the entity name, insurance and warranty in every proposal. <a href=\"/guides/how-to-verify-a-concrete-contractor-florida/\">How to verify a contractor</a>."),
        faq("Pavers or concrete?", "Concrete costs less; pavers can be lifted and relaid and suit HOA palettes. <a href=\"/compare/concrete-vs-pavers/\">The comparison</a> and <a href=\"/tools/concrete-vs-pavers/\">the decision tool</a>."),
        faq("Can you pour in the rainy season?", "Yes, with first-light starts; June through September average 14 to 18 rain days a month at the Kissimmee 2 station. <a href=\"/tools/pour-calendar/\">Pour Calendar</a>."),
        faq("Does my HOA have to approve it?", "Every planned community here requires written approval before work; APV, Solivita, Celebration, Bellalago and Solterra rules are quoted on the <a href=\"/hoa/\">HOA pages</a>."),
    ]
    return {"route": "/faq/", "title": "Concrete Questions Kissimmee Homeowners Ask (Answered)", "meta_description": "Short answers to the questions Kissimmee, St. Cloud and Osceola County homeowners ask about concrete and pavers: cost, permits, licenses, pavers vs. concrete, rainy-season pours, HOA approval, with links to full answers.", "h1": "Frequently asked questions", "breadcrumbs": [("Home", "/"), ("FAQ", None)], "body_html": body, "faqs": faqs, "kind": "faq", "sources": ["fs489117", "noaa"]}


def concrete():
    faqs = [
        faq("How thick should a concrete driveway be in Florida?", f"Four inches for cars on a compacted base, six with a rebar grid for boats, RVs and trucks. The Florida Building Code's residential minimum for a slab on ground is 3½ inches (R506). {compare('4-inch-vs-6-inch')}."),
        faq("3,000 or 4,000 PSI for a driveway?", "3,000 to 3,500 psi for cars; 4,000 for heavy loads. Strength beyond the load does not prevent cracking; base and joints do."),
        faq("Rebar, wire mesh or fiber?", f"Fiber plus #4 rebar at the edges on 4-inch work; a #4 grid on chairs in 6-inch slabs. Wire mesh that ends up on the bottom of a 4-inch slab does nothing. {compare('rebar-vs-fiber-vs-mesh')}."),
        faq("How long before I can walk or drive on new concrete?", "Walk after 24 to 48 hours, park a car after 7 days, heavy vehicles after 28 days. Heat speeds the surface set, not the strength curve."),
        faq("Will my concrete driveway crack?", f"Hairline shrinkage cracks, yes; joints are there to make them happen in the joint. Cracks over 1/8 inch, stepped, or running from a corner mean the base moved. {guide('why-concrete-cracks-osceola')}."),
        faq("Why does new concrete look blotchy?", "Uneven curing and moisture: a slab that dried faster in one area than another, or was covered unevenly. It evens out over months; a light acid wash or a penetrating sealer can even the tone sooner."),
        faq("What is the difference between cement and concrete?", "Cement is the powder that binds; concrete is cement plus sand, stone and water. A 'cement driveway' is a concrete driveway."),
        faq("Should I seal a new concrete driveway?", "Optional on broom concrete; a penetrating sealer after 28 days helps with oil and rust stains and is standard on stamped concrete."),
        faq("How long does a concrete driveway last in Central Florida?", "Twenty-five to thirty years or more on a compacted base with joints and water kept off the edges; the 1980s slabs poured on raw sand in Buenaventura Lakes lasted about that long with no base at all."),
        faq("Does homeowners insurance cover a cracked driveway?", "Usually not for settling, roots or wear; sudden damage from a covered event sometimes is. We supply photos and a written assessment for a claim."),
        faq("Can you pour concrete in the rain?", f"Not in it. In the rainy season we start at first light and finish and cover before the afternoon storms; more than a 60 percent chance before 2 p.m. moves the pour. {tool('pour-calendar')}."),
        faq("What slope does a patio need?", "At least ⅛ inch per foot away from the house; on flat Kissimmee lots that usually means a slot drain at the far edge."),
        faq("Can you match my existing driveway when adding a section?", "Finish and joint layout, yes; color will be lighter for about a year. A straight joint at the seam makes it read as intentional."),
        faq("Do you pour over septic drainfields?", f"No. On rural St. Cloud and Harmony lots we locate the system from the county record and stay clear. {guide('septic-drainfield-concrete-driveway')}."),
        faq("What is control-joint spacing?", "About 10 feet on a 4-inch slab (roughly 2½ times the thickness in feet), cut to a quarter of the depth within 12 hours, per ACI 332 guidance."),
        faq("Asphalt or concrete for a driveway in Florida?", "Concrete: asphalt softens in Florida heat and needs sealing every few years; it is rare on residential lots here except long rural drives."),
    ]
    body = sec("Concrete questions", cap("Sixteen questions about thickness, mix, reinforcement, curing, cracks and care, answered short with the full page linked. Costs are on the cost FAQ and the pricing pages."), eyebrow="FAQ")
    body += sec("Related", related([svc("concrete-driveways"), svc("concrete-patios"), svc("concrete-repair"), guide("concrete-curing-florida-heat"), guide("why-concrete-cracks-osceola")]), cls="alt")
    return {"route": "/faq/concrete/", "title": "Concrete FAQ – Thickness, PSI, Rebar, Curing, Cracks (Kissimmee)", "meta_description": "Concrete questions answered for Kissimmee and Osceola County: how thick a driveway should be, 3,000 vs. 4,000 psi, rebar vs. mesh vs. fiber, cure time, why concrete cracks, blotchy color, sealing, lifespan, insurance, rain.", "h1": "Concrete FAQ", "breadcrumbs": [("Home", "/"), ("FAQ", "/faq/"), ("Concrete", None)], "body_html": body, "faqs": faqs, "kind": "faq", "sources": ["fbc-r506", "aci332"]}


def pavers():
    faqs = [
        faq("How much base do pavers need on Florida sand?", f"Six inches of compacted limerock under a driveway, four to five under a patio or pool deck, plus 1 inch of bedding sand, edge restraint and polymeric sand. {svc('paver-driveways')}."),
        faq("What is polymeric sand?", f"Joint sand with a polymer binder that hardens when misted, locking the field and keeping ants and weeds out. Installed dry, vibrated in, activated with a light mist. {guide('polymeric-sand-guide')}."),
        faq("Why are there weeds and ants in my joints?", "Regular sand, or polymeric sand installed thin or wet. Clean out, re-sand with polymeric, seal."),
        faq("What is the white haze on my new pavers?", "Efflorescence: salts migrating out of concrete pavers during the first rainy season. Normal; it washes off with an efflorescence cleaner before sealing. Do not seal over it."),
        faq("Should pavers be sealed in Florida?", f"Concrete pavers, yes, 60 to 90 days after installation and every three to four years on a driveway, two to three on a pool deck. Travertine and marble take a penetrating sealer only; porcelain none. {svc('paver-sealing')}."),
        faq("Why did my pavers turn white after sealing?", f"A film sealer over moisture or efflorescence. Strip and re-seal on a dry deck with a breathable product. {compare('sealer-types')}."),
        faq("Can I pressure wash pavers?", "Yes, with a surface cleaner and a wide tip at 2,500 to 3,000 psi; a narrow tip etches the surface and blows out joint sand, which then needs replacing."),
        faq("Why are my pavers sinking?", f"Base washout at a downspout or sprinkler, thin base, or no edge restraint. Fix the water, lift, rebuild the base, relay. {svc('paver-repair')}."),
        faq("Brick pavers or concrete pavers?", "Clay brick keeps its color forever and suits traditional homes; concrete pavers cost less, come in more sizes and colors, and interlock better under tires in 80 mm."),
        faq("How long do pavers last?", "The units outlast the base; a paver drive on a rebuilt base can be relaid indefinitely."),
        faq("Is travertine slippery around a pool?", f"Tumbled and honed travertine grip well wet; polished is not used outdoors. {svc('paver-travertine')}."),
        faq("What is a soldier course?", "A border row of pavers set end-on (long side across the path); a sailor course is set long side along the path. Both frame the field and stiffen the edge."),
        faq("How thick should driveway pavers be?", "80 mm (3⅛ in) on driveways; 60 mm on patios and walks."),
        faq("Can pavers go over my concrete pool deck?", f"Usually, with 1-inch remodel pavers, if the deck is sound and the extra inch works at the doors and coping. {svc('paver-pool-decks')}."),
        faq("Which pavers do you install?", "Belgard, Tremron and Oldcastle Coastal lines, clay brick, permeable systems, travertine, marble and large-format porcelain; HOA palettes first."),
        faq("How do I get rust stains off pavers?", f"An iron-specific cleaner, then adjust the sprinkler heads or filter the well water or it returns. {guide('rust-stains-irrigation-well-water')}."),
    ]
    body = sec("Paver questions", cap("Sixteen questions about base, joint sand, sealing, stains, settling and materials, answered short with the full page linked."), eyebrow="FAQ")
    body += sec("Related", related([svc("paver-driveways"), svc("paver-pool-decks"), svc("paver-sealing"), svc("paver-repair"), guide("paver-base-flatwoods-vs-ridge")]), cls="alt")
    return {"route": "/faq/pavers/", "title": "Paver FAQ – Base, Polymeric Sand, Sealing, Sinking (Kissimmee)", "meta_description": "Paver questions answered for Kissimmee and Osceola County: base depth on sand, polymeric sand, weeds and ants, efflorescence, sealing schedule and failures, pressure washing, sinking, brick vs. concrete, travertine, rust stains.", "h1": "Paver FAQ", "breadcrumbs": [("Home", "/"), ("FAQ", "/faq/"), ("Pavers", None)], "body_html": body, "faqs": faqs, "kind": "faq", "sources": ["icpi"]}


def permits_hoa():
    faqs = [
        faq("Do you need a license to pour concrete in Florida?", f"No state license exists for concrete flatwork, pavers or stucco, and s. 489.117(4)(a) bars counties and cities from requiring a local license for driveway installation or decorative stone and paver work (since July 1, 2023). Verify insurance, Sunbiz registration and references instead. {guide('how-to-verify-a-concrete-contractor-florida')}."),
        faq("Who pulls the permit, the contractor or the homeowner?", "We do, as the contractor of record; Osceola's FAQ says any owner, licensed contractor or authorized agent may bring in the application but only the applicant signs. You sign the application and, at $5,000 or more in Osceola, the Notice of Commencement."),
        faq("Do I need a permit for a driveway in Osceola County?", f"Yes: §22-50.6 requires a county driveway permit for construction or widening and caps width at 24 feet. {juris('osceola-county')}."),
        faq("Do I need a permit for a patio in St. Cloud?", f"Yes; patios and decks are on the city's permit list. {juris('city-of-st-cloud')}."),
        faq("Do pavers need a permit?", "In Osceola, under the driveway permit; in St. Cloud, referred to Public Works; in Polk, within setbacks or with a Paver Release Form in the right-of-way; in Orange, a Zoning permit."),
        faq("Does my HOA have to approve a like-for-like driveway replacement?", f"In every verified community here, yes; APV requires prior written approval for any driveway or paved area. {hoa('poinciana-apv')}."),
        faq("What happens if I install pavers without ARC approval?", "The association can require you to remove or redo the work at your cost; APV's criteria say the applicant must rectify violations after notice. Get the letter first."),
        faq("Can the HOA require a building permit before it reviews my project?", f"Not since July 1, 2026; HB 803 prohibits it. {guide('hb-803-permit-exemption')}."),
        faq("What is the $7,500 exemption?", "HB 803 (effective July 1, 2026) exempts single-family work valued under $7,500 from a building permit with a written request, excluding structural, electrical, plumbing, mechanical, gas and flood-zone work. It does not cover driveway permits."),
        faq("What is a Notice of Commencement?", "A recorded notice required in Osceola for projects of $5,000 or more before the first inspection; we prepare it, you sign before a notary, it is recorded at the courthouse."),
        faq("How long does approval take?", "APV: deemed denied at 30 days without action. Celebration: third Monday monthly. Bellalago: twice monthly. Osceola plan review: 3 to 5 days. Kissimmee driveway application: 2 business days plus 2 to issue."),
        faq("Can I widen my driveway onto the grass by the street?", f"That strip is usually public right-of-way; widening needs the driveway permit and the county's width limit applies. {guide('driveway-widening-rules-osceola')}."),
        faq("Which office covers my address?", f"The {tool('permit-finder')} checks city and county boundaries; addresses near a line get a call to the office."),
        faq("Is a right-of-way apron a separate permit?", "In Kissimmee it is part of the Driveway / Sidewalk application; in Osceola it falls under LDC 4.12.2 with the driveway permit; in Polk the right-of-way portion is what triggers the permit."),
    ]
    body = sec("Permit and HOA questions", cap("Fourteen questions about licenses, permits by office, HOA approval and the new $7,500 exemption, answered short with the quoted source linked."), eyebrow="FAQ")
    body += sec("Related", related(['<a href="/permits/">Permits hub</a>', '<a href="/hoa/">HOA / ARC hub</a>', tool("permit-finder"), tool("hoa-packet-checklist")]), cls="alt")
    return {"route": "/faq/permits-hoa/", "title": "Permits & HOA FAQ – Licenses, Approvals, HB 803 (Osceola & Polk)", "meta_description": "Permit and HOA questions for Kissimmee, St. Cloud, Osceola and Polk: no license for flatwork under s. 489.117, who pulls the permit, driveway and patio rules by office, HOA approval and violations, HB 803's $7,500 exemption.", "h1": "Permits and HOA FAQ", "breadcrumbs": [("Home", "/"), ("FAQ", "/faq/"), ("Permits & HOA", None)], "body_html": body, "faqs": faqs, "kind": "faq", "sources": ["fs489117", "osceola-22-50-6", "osceola-faq", "stcloud-permits", "polk-faq", "apv", "hb803"]}


def cost():
    faqs = [
        faq("How much do concrete contractors charge in Kissimmee?", f"By the square foot, installed: {cost_range('concrete-driveway-broom')} for a broom-finish driveway, {cost_range('concrete-patio')} for a patio, {cost_range('stamped-concrete')} for stamped work in the {R} index, with minimum charges on small jobs. <a href=\"/pricing/concrete/\">Concrete cost guide</a>."),
        faq("How much do pavers cost per square foot installed?", f"{cost_range('paver-driveway-concrete')} for a driveway in standard pavers, {cost_range('paver-patio')} for a patio, {cost_range('paver-pool-deck')} for a pool-deck overlay, {cost_range('travertine-pool-deck')} for travertine. <a href=\"/pricing/pavers/\">Paver cost guide</a>."),
        faq("Why is a small job so expensive per square foot?", "The ready-mix truck minimum, the short-load fee and the crew day are the same whether the slab is 100 or 400 square feet. Combine small jobs in one visit."),
        faq("What is a normal deposit?", "A deposit covering materials and permit fees at signing, with the balance on completion, is typical for residential flatwork; the contract states the schedule. We do not ask for full payment up front."),
        faq("Do you offer financing?", "Ask on the estimate; a financing partner will be listed on the pricing page once one is in place."),
        faq("Is asphalt cheaper than concrete or pavers?", "Per square foot, asphalt is the cheapest and the shortest-lived in Florida heat; it is rare on residential lots here except long rural drives."),
        faq("Which is cheaper, pavers or a concrete driveway?", f"Concrete, by 50 to 70 percent. {compare('concrete-vs-pavers')}."),
        faq("How much does it cost to remove an old driveway?", f"{cost_range('concrete-removal')}; $960 to $1,920 for a two-car drive."),
        faq("How much does paver sealing cost?", f"{cost_range('paver-sealing')} with cleaning and polymeric re-sanding; about $840 to $1,560 for a two-car driveway."),
        faq("How far ahead should I book?", "Two to three weeks most of the year; four to six in March through May, when paver and pool-deck demand peaks in the Orlando market according to Google Trends."),
        faq("Are your prices quotes?", "No; they are planning ranges with a published method. Your price is in a written proposal after a site visit."),
        faq("Do prices differ by city?", "Slightly: the Polk ridge runs a little lower on labor, the resort corridor a little higher on scheduling and ARC requirements. The index ranges span both."),
    ]
    body = sec("Cost questions", cap(f"Twelve questions about what things cost, how we price, deposits and timing, answered from the {R} Cost Index with the full guides linked."), eyebrow="FAQ")
    body += sec("Related", related(['<a href="/pricing/">Pricing hub</a>', '<a href="/pricing/kissimmee-concrete-cost-index/">Cost Index</a>', tool("concrete-paver-calculator"), tool("project-brief")]), cls="alt")
    return {"route": "/faq/cost/", "title": "Cost FAQ – What Concrete & Pavers Cost in Kissimmee (2026)", "meta_description": f"Cost questions for Kissimmee and Osceola County answered from the {R} Cost Index: contractor rates per sq ft, why small jobs cost more, deposits, financing, asphalt vs. concrete vs. pavers, removal, sealing, when to book.", "h1": "Cost FAQ", "breadcrumbs": [("Home", "/"), ("FAQ", "/faq/"), ("Cost", None)], "body_html": body, "faqs": faqs, "kind": "faq"}


def get_pages():
    return [hub(), concrete(), pavers(), permits_hoa(), cost()]
