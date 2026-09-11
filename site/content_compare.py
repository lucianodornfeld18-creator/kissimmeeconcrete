# -*- coding: utf-8 -*-
"""Comparison pages (index + 8)."""
from _data import COMPARISONS, COST_INDEX_RELEASE
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, callout, related, esc

R = COST_INDEX_RELEASE["label"]


def page(key, title, desc, h1, body, faqs, sources):
    c = COMPARISONS[key]
    return {"route": c["route"], "title": title, "meta_description": desc, "h1": h1, "breadcrumbs": [("Home", "/"), ("Compare", "/compare/"), (c["name"], None)], "body_html": body, "faqs": faqs, "kind": "compare", "sources": sources}


def index():
    body = sec("Side-by-side decisions for Central Florida lots",
        cap("Eight comparisons homeowners in Kissimmee, St. Cloud and the Polk ridge ask for most, each with the numbers from the current Cost Index, the heat and rain facts that matter here, and the HOA angle. None of them says one answer is always right; each says when it is."),
        eyebrow="Compare")
    body += sec("Comparisons", cards([
        (COMPARISONS["concrete-vs-pavers"]["name"], "First cost, repairability, HOA preference, heat, resale.", COMPARISONS["concrete-vs-pavers"]["route"], "Read"),
        (COMPARISONS["travertine-vs-concrete-pavers"]["name"], "Barefoot temperature, cost, sealing, salt pools, repair.", COMPARISONS["travertine-vs-concrete-pavers"]["route"], "Read"),
        (COMPARISONS["stamped-vs-pavers"]["name"], "The stone look two ways: cost, maintenance, cracking, HOA.", COMPARISONS["stamped-vs-pavers"]["route"], "Read"),
        (COMPARISONS["resurface-vs-replace"]["name"], "The tap test, the string line, and the math on a 1980s driveway.", COMPARISONS["resurface-vs-replace"]["route"], "Read"),
        (COMPARISONS["4-inch-vs-6-inch"]["name"], "Which loads need the extra two inches and what they cost.", COMPARISONS["4-inch-vs-6-inch"]["route"], "Read"),
        (COMPARISONS["rebar-vs-fiber-vs-mesh"]["name"], "What each does, what each cannot, and why mesh on the bottom is nothing.", COMPARISONS["rebar-vs-fiber-vs-mesh"]["route"], "Read"),
        (COMPARISONS["cool-deck-vs-pavers"]["name"], "Textured coatings versus pavers around the pool.", COMPARISONS["cool-deck-vs-pavers"]["route"], "Read"),
        (COMPARISONS["sealer-types"]["name"], "Film-forming, penetrating, joint-stabilizing: what to put on what.", COMPARISONS["sealer-types"]["route"], "Read"),
    ], cols=4))
    body += sec("Prefer a recommendation?", f"<p>The {tool('concrete-vs-pavers')} asks eight questions and gives one with reasons.</p>", cls="alt")
    return {"route": "/compare/", "title": "Concrete vs. Pavers, Travertine, Stamped & More – Comparisons", "meta_description": "Eight side-by-side comparisons for Central Florida: concrete vs. pavers, travertine vs. concrete pavers, stamped vs. pavers, resurface vs. replace, 4 vs. 6 inches, rebar vs. fiber vs. mesh, cool deck vs. pavers, sealer types.", "h1": "Comparisons", "breadcrumbs": [("Home", "/"), ("Compare", None)], "body_html": body, "kind": "page", "no_cta": True}


def concrete_vs_pavers():
    body = sec("Pavers or concrete for a driveway in Central Florida?",
        cap(f"Concrete costs less up front ({cost_range('concrete-driveway-broom')} for a broom finish in the {R} index versus {cost_range('paver-driveway-concrete')} for standard pavers), gives a clean uniform surface and is easier to keep. Pavers cost 50 to 70 percent more, can be lifted and relaid after settling or a utility cut, come in the palettes most Osceola and Polk HOAs already approved, and let you widen later with matching units. On this sand both need the same thing to last: a compacted base and water kept away."),
        eyebrow="Comparison")
    body += sec("Side by side",
        table(["", "Concrete (broom finish)", "Concrete pavers"], [
            ("Installed cost, driveway", cost_range("concrete-driveway-broom"), cost_range("paver-driveway-concrete") + " (premium " + cost_range("paver-driveway-premium") + ")"),
            ("480 sq ft two-car drive", "$4,080–$6,480", "$6,720–$10,560"),
            ("Time on site", "2–3 days + 7 days before parking", "3–5 days; usable immediately"),
            ("Base", "4 in compacted limerock", "6 in compacted limerock + 1 in sand"),
            ("Cracking", "Hairline shrinkage cracks normal; base movement cracks through", "Units don't crack; base movement shows as dips, fixable"),
            ("Repair", "Cut out and replace a panel (lighter for a year)", "Lift and relay the area, same units"),
            ("Utility cut through the drive", "Patch shows", "Relay, invisible"),
            ("Widening later", "New slab, color mismatch", "Matching units, if the line still exists"),
            ("Surface heat (published)", "Light gray: moderate", "By color: light similar to concrete, dark hotter"),
            ("Maintenance", "Optional seal; pressure wash", "Seal every 3–4 years; polymeric sand; weeds/ants if neglected"),
            ("HOA", "Accepted everywhere; some resort communities prefer pavers", "Preferred in most planned communities; palette rules"),
            ("Permits", "Same driveway permit", "Same; Polk Paver Release Form if pavers reach the right-of-way"),
            ("Resale", "Neutral", "Often a plus in paver communities"),
            ("Lifespan", "25–30+ years with base and joints", "30+ years; base is the limit"),
        ], caption=f"Ranges from the {R} Kissimmee Concrete Cost Index; heat figures from published installer measurements collected on the surface-temperature page."), cls="alt")
    body += sec("When concrete is the right call", "<p>A straight two-car driveway on a lot without an HOA palette, a budget that wants the most surface for the dollar, a look that matches the street, and a homeowner who values low upkeep. Buenaventura Lakes, the older Poinciana villages and the mid-century streets of St. Cloud and Haines City are concrete neighborhoods for good reason.</p>")
    body += sec("When pavers are the right call", "<p>A planned or resort community whose ARC has a paver palette on file, a driveway that will see utility work or a future widening, a lot where a sunken area will need relaying rather than cutting, a pool deck (pavers or stone, almost always), and an owner who wants the pattern and border. Celebration, Reunion, ChampionsGate, Solterra and the Bellalago estate sections are paver neighborhoods.</p>", cls="alt")
    body += sec("What both need on this ground", f"<p>Smyrna and Myakka sand with a 12-inch summer water table on the Osceola side, Candler sand that compacts only wet on the Polk ridge: the surface does not fix a base problem. Concrete on a compacted base with joints and edge steel and downspouts extended; pavers on 6 inches of base with restraint and polymeric sand. The base guide is {guide('paver-base-flatwoods-vs-ridge')}; the cracking guide is {guide('why-concrete-cracks-osceola')}. The eight-question {tool('concrete-vs-pavers')} turns this page into a recommendation.</p>")
    body += sec("Cost over twenty-five years, not on the invoice",
        table(["Line", "Poured concrete driveway", "Concrete paver driveway"], [
            ("Installed today, 480 sq ft", "$4,080 to $6,480", "$6,720 to $10,560"),
            ("Removal of the existing slab", "$960 to $1,920", "$960 to $1,920"),
            ("Sealing in year one", "Optional; $0 to $700", "Recommended at 60 to 90 days; $840 to $1,560"),
            ("Routine maintenance to year 25", "Crack sealing every few years; a resurfacing around year 15", "Re-sand and re-seal about every 3 to 4 years"),
            ("A settled area at year 10", "Saw-cut and replace the panel; new concrete will not match", "Lift, rebuild the base, relay the same pavers; it matches"),
            ("A utility cut across the drive", "Saw-cut, patch, visible seam forever", "Lift the affected field and relay"),
            ("Typical look at year 25", "Weathered, joint cracks, patches visible", "Colour softened, joints topped up, individual replacements blend"),
        ], caption="Installed figures from the current Cost Index for a 480 square foot two-car drive. Maintenance intervals are our field practice for this climate, not a manufacturer claim."), cls="alt")
    body += sec("Which one your association already expects",
        f"""<p>In the communities we work in most, the answer is often decided before the homeowner weighs anything. Poinciana's Design Control Board names concrete, asphalt or brick pavers as the acceptable driveway materials and requires prior written approval for any change. Solivita requires a replacement driveway to match the original builder's style and materials, which on most of those streets means what is already there. Solterra prohibits painting or staining concrete and allows a clear matte sealer only on request, which pushes owners who want colour toward pavers. Celebration's pattern book runs to approved paver patterns and a narrow colour palette.</p>
<p>That is not a reason to choose pavers everywhere. It is a reason to read the document before the design meeting. The {tool('hoa-packet-checklist')} assembles the submission, and the verified criteria are quoted on {hoa('poinciana-apv')}, {hoa('solivita')}, {hoa('solterra')} and {hoa('celebration')}.</p>""")
    body += sec("Where each one clearly wins",
        f"""<p>Concrete wins when the budget is the constraint, when the look wanted is clean and uniform, when the drive is long and the square footage makes the paver premium painful, and when the lot drains well and has no mature trees at the edge. A 6-inch concrete pad is also the right answer under an RV or a boat, where paver bedding sand under a concentrated wheel load is working against itself.</p>
<p>Pavers win when the lot has a drainage history, because settling is repairable rather than terminal. They win under mature live oaks for the same reason ({guide('tree-roots-driveways-central-florida')}). They win when the association's palette is already paver-based, when the driveway will be cut for a utility or a pool installation later, and when the owner wants colour and pattern without a coating that has to be renewed. On a vacation rental in the Four Corners corridor, the ability to pull and relay a section between guests is worth real money ({guide('vacation-rental-owner-hardscape-guide')}).</p>""", cls="alt")
    faqs = [
        faq("Which is cheaper, pavers or a concrete driveway?", f"Concrete, by 50 to 70 percent: {cost_range('concrete-driveway-broom')} versus {cost_range('paver-driveway-concrete')} installed in the current index."),
        faq("Is a paver driveway better than concrete?", "Better at being repaired and matched later; not better at being cheap or low-maintenance. It depends on the community and what you value."),
        faq("Do pavers last longer than concrete?", "Both outlast their base. A concrete drive on a real base lasts 25 to 30 years or more; pavers can be relaid on a rebuilt base indefinitely."),
        faq("Which stays cooler?", "Light concrete and light pavers are similar; dark pavers are hotter. For barefoot areas, travertine and marble beat both."),
        faq("Can pavers go over my existing concrete driveway?", "Not on a driveway; the overlay would raise the apron and trap water. Pavers over concrete is a pool-deck technique."),
        faq("Do pavers add more resale value than concrete?", "We have no local sales data that would let us put a number on it, so we will not. What we can say is that both are expected finishes here and a failing driveway of either kind is a negotiating point at inspection."),
        faq("Are pavers slippery when wet?", "Less than a smooth-troweled concrete slab, about the same as a broom finish. Sealer choice changes it more than material does; a glossy film-forming sealer on either surface is the slippery combination."),
    ]
    return page("concrete-vs-pavers", "Pavers vs. Concrete Driveway in Central Florida: Cost & Heat", "Concrete vs. pavers for a driveway or patio in Kissimmee and Osceola County: installed cost per sq ft and per two-car drive, repairability, HOA preference, heat, maintenance and lifespan, and when each is the right call.", "Concrete vs. pavers: which is right for your driveway or patio", body, faqs, ["icpi", "polk-paver-release"])


def travertine_vs_pavers():
    body = sec("Travertine or concrete pavers for a pool deck?",
        cap(f"Travertine stays cooler barefoot (published measurements: 105 to 120 °F at midday versus 115 to 145 °F for concrete pavers depending on color), costs more ({cost_range('travertine-pool-deck')} versus {cost_range('paver-pool-deck')} for a paver overlay in the {R} index), needs a penetrating sealer rather than a film, and reads as natural stone. Concrete pavers cost less, come in more colors and patterns, take any sealer, and hold up to rental traffic. Both are lifted and relaid the same way."),
        eyebrow="Comparison")
    body += sec("Side by side",
        table(["", "Travertine", "Concrete pavers"], [
            ("Installed, pool deck", cost_range("travertine-pool-deck"), cost_range("paver-pool-deck") + " overlay; " + cost_range("paver-patio") + " new"),
            ("600 sq ft deck", "$12,000–$21,600 + coping", "$9,000–$14,400 + coping"),
            ("Surface heat, published", "105–120 °F (light grades)", "115–145 °F by color"),
            ("Wet grip", "Tumbled: good; honed: good; polished: poor (not used outdoors)", "Good; sealer with grit"),
            ("Look", "Natural stone, variation, French pattern", "Uniform; many colors and patterns"),
            ("Sealer", "Penetrating, breathable only", "Film or penetrating"),
            ("Pool chemicals / salt", "Seal; rinse salt-pool decks monthly", "Tolerant"),
            ("Stains", "Porous; iron from well water shows fast on ivory", "Porous; seal"),
            ("Rental traffic", "Fine with anti-slip penetrating sealer", "Very good"),
            ("Repair", "Lift and reset; keep spares (lots vary)", "Lift and reset; match from current lines"),
            ("Driveway use", "Thick pavers only, strong pattern, HOA permitting", "Standard"),
        ], caption=f"Ranges from the {R} index. Temperature figures are cited from published installer and manufacturer measurements; our own July measurements are planned ({guide('surface-temperature-pool-decks', 'method')})."), cls="alt")
    body += sec("Marble and porcelain, for completeness", f"<p>Marble is lighter and cooler than travertine and costs more; 2 cm large-format porcelain is stain-proof and uniform but must be set on a rigid base or pedestals, and dark porcelain gets hot. Both are on {svc('paver-marble-porcelain')}. Coated concrete (cool deck) is the fourth option: {compare('cool-deck-vs-pavers')}.</p>")
    body += sec("Which we recommend where", f"<p>Travertine or marble for a primary-home pool deck used barefoot in summer, for lakefront and estate lots in Bellalago, Reunion, Celebration and St. Cloud, and wherever the owner wants stone. Concrete pavers for rental decks in Four Corners, ChampionsGate and Windsor Hills, for budgets that need the lower number, and for HOAs with a paver palette and no stone in it. Either way the deck drains to a channel at the screen line and the coping goes on the bond beam with an expansion joint ({svc('paver-pool-decks')}, {svc('paver-travertine')}).</p>", cls="alt")
    body += sec("Cost, side by side, for a 600 square foot deck",
        table(["Line", "Concrete pavers", "Travertine"], [
            ("Installed range per sq ft", "$15.00 to $24.00 (overlay) or $13.00 to $21.00 (patio build)", "$20.00 to $36.00"),
            ("600 sq ft deck", "$9,000 to $14,400", "$12,000 to $21,600"),
            ("Coping", "Bullnose paver coping, included in the deck range", "Bullnose travertine coping, higher unit cost"),
            ("Sealer at handover", "Optional; joint stabilizer common", "Penetrating stone sealer recommended"),
            ("Re-seal interval here", "3 to 4 years", "2 to 3 years on a deck in full sun"),
            ("Replacement piece availability", "Good while the line is current; colours drift", "Good; stone varies by lot, which usually blends"),
        ], caption="From the current Cost Index. Marble and large-format porcelain sit at or above the travertine range."), cls="alt")
    body += sec("Salt systems, chemicals and what the surface has to survive",
        f"""<p>Most new residential pools in Osceola County run salt chlorine generators, and the splash-out from a salt pool is a mild brine that dries on the deck every day. On concrete pavers that shows up as efflorescence and, over years, surface erosion at the splash line. On travertine, which is a calcium carbonate stone, the concern is different: acidic pool chemistry and acidic cleaners etch it, while the salt itself is largely a cosmetic issue that a penetrating sealer manages.</p>
<p>Practical consequences. Neither material should be cleaned with muriatic acid, and on travertine that rule is absolute. Both benefit from being rinsed after a heavy splash day, which most owners will not do, so both get sealed instead. And the tablet feeder or the chlorine bucket should never sit on either surface; the ring it leaves is permanent on stone and near-permanent on a light paver.</p>""")
    body += sec("Repair and replacement over time",
        f"""<p>A concrete paver deck that settles by a downspout is a half-day repair: pull the field, rebuild the base, relay. Travertine set on a sand bed behaves the same way. Travertine thin-set onto an existing concrete deck does not, and that is the distinction buyers rarely hear at the showroom. A thin-set stone deck over a slab that later moves has to be broken out, and the stone rarely survives removal.</p>
<p>So the question we ask before recommending thin-set over sand-set is what the slab underneath is doing. A sound, well-drained deck takes thin-set stone happily and gains almost no height. A deck with hollow spots and a step at the coping needs the base fixed first, which usually means a sand-set rebuild. That inspection is the same tap test and string line described in {compare('resurface-vs-replace')}, and the pool-deck scope is on {svc('paver-pool-decks')}.</p>""", cls="alt")
    faqs = [
        faq("Does travertine get hot around a pool?", "Warm, not scorching: published measurements put light travertine around 105 to 120 °F on a 95-degree afternoon, 20 to 30 degrees below dark concrete pavers."),
        faq("Is travertine better than pavers?", "Cooler and more natural-looking; more expensive and more particular about sealers. Concrete pavers are cheaper, tougher under rental use and more flexible in color."),
        faq("How much more is travertine?", "About 30 to 50 percent more than a concrete-paver overlay on the same deck in the current index."),
        faq("Which is more slippery?", "Neither, in tumbled or honed finishes with an anti-slip sealer. Polished stone is not used outdoors."),
        faq("Can I use travertine with a salt pool?", "Yes, sealed and rinsed monthly; salt is harder on unsealed stone."),
        faq("Does travertine need to be sealed?", "On a pool deck in full sun, yes, with a penetrating breathable sealer every two to three years. Never a film-forming sealer, which traps moisture from the bedding course and hazes."),
        faq("Is travertine slippery?", "Tumbled and brushed travertine has good wet grip, better than polished stone or a smooth-troweled slab. Honed and filled travertine is the slippery variant and is not what we install around a pool."),
    ]
    return page("travertine-vs-concrete-pavers", "Travertine vs. Concrete Pavers for a Pool Deck in Florida", "Travertine vs. concrete pavers for a Central Florida pool deck: barefoot temperature (published 105–120 °F vs. 115–145 °F), cost per sq ft and per 600 sq ft deck, sealers, salt pools, rental use, repair.", "Travertine vs. concrete pavers for a pool deck", body, faqs, ["icpi"])


def stamped_vs_pavers():
    body = sec("Stamped concrete or pavers for a patio or pool deck?",
        cap(f"Stamped concrete gives a stone look as one continuous slab for {cost_range('stamped-concrete')} in the {R} index; pavers give it in units for {cost_range('paver-patio')}, roughly the same money at the low end and more at the top. Stamped concrete has no joints to sand but needs re-sealing every two to three years and cracks if the base moves; pavers need polymeric sand and sealing but can be lifted and relaid. Most Osceola HOAs have a paver palette on file and no stamped-concrete standard."),
        eyebrow="Comparison")
    body += sec("Side by side",
        table(["", "Stamped concrete", "Concrete pavers"], [
            ("Installed, patio", cost_range("stamped-concrete"), cost_range("paver-patio")),
            ("12×16 patio", "$2,690–$4,220", "$2,500–$4,030"),
            ("Time on site", "2 days + 28 days before sealing", "2–3 days; seal at 60–90 days"),
            ("Look", "Continuous pattern; color from integral + release", "Units; pattern and border options"),
            ("Cracking", "Slab cracks if base moves; joints hidden in grout lines", "Units don't crack; base movement shows as dips"),
            ("Repair", "Hard to patch invisibly", "Lift and relay"),
            ("Maintenance", "Re-seal every 2–3 years; color fades without it", "Re-sand and seal every 3–4 years"),
            ("Slip", "Sealer needs grit", "Sealer needs grit"),
            ("Heat", "By color; dark stamps hot", "By color"),
            ("HOA", "Color and pattern reviewed; Solterra bans painted or stained concrete", "Palette usually on file"),
            ("Summer installation", "Stamping races the set; early pours, small sections", "No weather constraint except sand and sealer days"),
        ], caption=f"Ranges from the {R} index."), cls="alt")
    body += sec("Where each wins", f"<p>Stamped concrete: a covered lanai floor where the sealer lasts and the pattern stays sharp, a border around a plain slab, a patio in a neighborhood with no paver tradition. Pavers: pool decks (repair and coping), planned communities with a palette, any lot where roots or water may move the base. Details: {svc('concrete-stamped')}, {svc('paver-patios')}, {svc('paver-pool-decks')}.</p>")
    body += sec("The same stone look, two different failure modes",
        table(["", "Stamped concrete", "Pavers"], [
            ("Installed cost, 400 sq ft patio", "$5,600 to $8,800", "$5,200 to $8,400"),
            ("Surface renewal", "Re-seal every 2 to 3 years in full sun", "Re-sand and re-seal every 3 to 4 years"),
            ("What ageing looks like", "Release colour softens; sealer wears in traffic lanes", "Colour softens evenly; joints need topping up"),
            ("If the base moves", "The slab cracks through the pattern; repairs are visible", "Units settle; lift, rebuild, relay, no visible repair"),
            ("If a utility has to be cut", "Saw-cut and patch; pattern will not line up", "Lift and relay the field"),
            ("Where it is clearly better", "Continuous surfaces, no joints to maintain, under a lanai roof", "Anywhere the ground or the plans might move"),
        ], caption="Cost figures from the current Cost Index for a 400 square foot patio."), cls="alt")
    body += sec("Heat, grip and the pool-deck question",
        f"""<p>Around a pool the two diverge. Stamped concrete in a dark colour with a glossy sealer is the hottest and slipperiest combination on a Florida deck, and it is also the most commonly sold. The fixes are real but they are choices you have to make at the quote stage: a light colour, a matte or penetrating sealer, and a grit additive broadcast into the top coat. Pavers start ahead on grip because of the chamfered joints and start ahead on heat if the colour is light, and travertine starts further ahead still ({guide('surface-temperature-pool-decks')}).</p>
<p>For a patio away from the pool, the calculus changes and stamped concrete competes well. There is no joint sand to maintain, no ant activity between units, and a single continuous surface reads well under a pergola or a screen room. That is where we most often recommend it.</p>""")
    body += sec("What the association thinks of each",
        f"""<p>Colour and pattern are the two things architectural committees actually regulate, and stamped concrete touches both. Solterra's guidelines prohibit painting or staining concrete surfaces outright and allow a clear matte sealer only with a submitted request, which effectively rules out a coloured stamped patio in that community. Poinciana's Design Control Board requires prior written approval for any paved area and names the acceptable driveway materials. Celebration's pattern book approves specific paver products, patterns and colours.</p>
<p>Pavers are rarely a problem because the approved palettes are already paver palettes. Stamped work needs the colour chip and a photograph of the pattern in the submission, and it needs to go in before the concrete is ordered, because integral colour is dosed at the plant. The packet is on the {tool('hoa-packet-checklist')}.</p>""", cls="alt")
    faqs = [
        faq("Which is cheaper, stamped concrete or pavers?", "About the same at the low end for a patio; stamped runs higher with two colors or complex patterns, pavers higher with premium lines and borders."),
        faq("Does stamped concrete crack?", "Hairline cracks in the grout lines are normal; cracks across the pattern mean the base moved. Pavers move without cracking and are relaid."),
        faq("Which needs more maintenance?", "Stamped concrete: re-sealing every two to three years to keep color and protect the surface. Pavers: sanding and sealing every three to four."),
        faq("Which is better around a pool?", "Pavers or stone, for coping, drainage and repair. Stamped decks work but are harder to fix."),
        faq("Can stamped concrete be made to look like the pavers next door?", "Closely, in pattern, not exactly in edge detail. A paver field has real joints and chamfers that a stamp imitates with a grout line; up close the difference is visible."),
        faq("Which lasts longer?", "Both outlast twenty years when the base is right. Stamped concrete needs its sealer renewed to keep looking new; pavers need joint sand. Neglect shows up faster on stamped work."),
    ]
    return page("stamped-vs-pavers", "Stamped Concrete vs. Pavers in Central Florida: Cost & Upkeep", "Stamped concrete vs. pavers for a patio or pool deck in Kissimmee: cost per sq ft and for a 12x16 patio, cracking and repair, sealing cycles, slip and heat, HOA rules, and where each is the better choice.", "Stamped concrete vs. pavers", body, faqs, ["solterra"])


def resurface_vs_replace():
    body = sec("Resurface, repair or replace? The decision on a Central Florida slab",
        cap(f"Resurface when the slab is sound: hairline cracks only, no panel stepped more than ¼ inch, no hollow sound when tapped; it costs {cost_range('concrete-resurfacing')} versus {cost_range('concrete-driveway-broom')} plus removal for a new pour. Repair when one panel or the apron has failed and the rest is sound. Replace when a third of the panels have moved, when the drive is 1980s vintage on sand with no base, or when the apron and garage panels that carry the load are cracked through."),
        eyebrow="Decision")
    body += sec("The three tests we run", "<ol><li><strong>Tap test.</strong> A hammer on the slab: a solid ring means support underneath; a hollow thud means a void from washed-out sand.</li><li><strong>String line.</strong> Across the panels: offsets over ¼ inch mean the base moved, and an overlay will crack at the same lines.</li><li><strong>Hose test.</strong> Where does water go? Toward the garage or under the slab edge means the cause of the movement is still active.</li></ol>", cls="alt")
    body += sec("The decision table",
        table(["What we find", "Answer", "Cost, 480 sq ft two-car drive"], [
            ("Hairline cracks, no offsets, solid, worn or stained surface", "Resurface (overlay)", "$2,400–$4,560"),
            ("One panel stepped at the garage, others sound, downspout at the edge", "Fix the water, replace or lift the panel", "$1,100–$1,900 for the panel"),
            ("Apron corner broken, drive sound", "Replace the apron section at 6 in with edge steel", "$500–$900"),
            ("Two or more panels moved, hairlines everywhere, 1980s slab on sand", "Replace", "$5,040–$8,400 incl. removal"),
            ("Slab heaved at a tree", "Root barrier + panel replacement, or reroute", "$1,300–$2,300"),
            ("Pool deck hollow at the coping", "Rebuild the deck (paver or concrete)", "See pool decks"),
            ("Sound slab, want a new look", "Stamped overlay or paver overlay (pool decks only)", "Resurfacing + $4–$6/sq ft"),
        ], caption=f"Ranges from the {R} index; lifting is quoted by injection contractors and referred when it is the right answer."))
    body += sec("About polyurethane lifting", f"<p>Foam injected under a slab raises it in an hour and is sold hard in Kissimmee. It works on an intact, relatively new slab with a small dry void after the water problem is solved. It does not fix the reason the slab sank, and on a cracked 1980s garage panel it lifts the pieces and they keep moving. We recommend it in the first case and replacement in the second, and we say which in writing. Pages: {svc('concrete-repair')}, {svc('concrete-resurfacing')}, {svc('concrete-driveways')}; the BVL case study in {guide('buenaventura-lakes-driveway-replacement')}.</p>", cls="alt")
    body += sec("The three tests that settle it",
        f"""<p><strong>The tap test.</strong> Drag a length of chain or tap a hammer across each panel. Supported concrete rings; concrete over a void thuds. A slab with hollow areas has lost its base, and nothing applied to the top restores it.</p>
<p><strong>The string line.</strong> Lay a straight edge across every crack. Both sides level means shrinkage, which an overlay covers permanently. A step of an eighth of an inch or more means one side has dropped, which means the base moved, which means the overlay will crack along the same line within a season.</p>
<p><strong>The hose test.</strong> Run water where the roof and the irrigation put it and watch. If water ponds against the slab, runs under the edge, or drains toward the garage, the cause of the failure is still live. Fix it first or the money is spent twice.</p>""")
    body += sec("What each route costs on the same driveway",
        table(["Route", "480 sq ft two-car driveway", "Lasts", "When it is the right answer"], [
            ("Do nothing", "$0", "Deteriorates", "Hairline cracks, level, slab sound"),
            ("Route and seal the cracks", "Minimum-charge visit", "3 to 5 years", "Tight cracks you want kept watertight"),
            ("Grind a trip hazard", "Hourly", "Indefinite for that lip", "A single raised edge on a walk"),
            ("Polyurethane lifting", "Quoted by the injection specialist", "Years, if the water is fixed", "Intact newer panel over a small dry void"),
            ("Replace one panel", "$1,020 to $1,620 plus removal", "As long as a new slab", "One failed panel, rest of the drive sound"),
            ("Resurface the whole drive", "$2,400 to $4,560", "10 to 15 years", "Sound slab, tired surface, no steps or hollows"),
            ("Remove and replace", "$5,040 to $8,400", "25 years or more", "Multiple failed panels, 1980s slab, or a base that has to be rebuilt"),
        ], caption="Ranges from the current Cost Index for a 480 square foot driveway; lifting is quoted by the specialist who performs it."), cls="alt")
    body += sec("The trap in the middle",
        f"""<p>The expensive mistake is resurfacing a driveway that needed replacing. It costs roughly half of a replacement, it looks excellent for a season, and then the same cracks come through because the base under them is still moving. At that point the owner has spent half and still faces the whole, and the overlay has to be removed as part of the demolition.</p>
<p>So our rule is simple and we hold to it even when the customer would rather hear otherwise: hollow or stepped means no overlay. On a 1980s Buenaventura Lakes or Poinciana driveway the honest conversation is usually about replacement, and the reasons are laid out with what we find under those slabs in {guide('buenaventura-lakes-driveway-replacement')}. On a 2005 driveway with a tired surface and a solid base, resurfacing is the obvious value and we say that too ({svc('concrete-resurfacing')}).</p>""")
    faqs = [
        faq("Can I resurface a cracked driveway?", "Hairline cracks, yes, after routing and filling. Cracks with an offset or a hollow slab, no; the overlay follows the movement."),
        faq("Is resurfacing worth it before selling?", "On a sound slab it is the cheapest cosmetic fix and a buyer's inspector will see a clean surface. On a moving slab the inspector will see the offset through the overlay."),
        faq("How much cheaper is resurfacing than replacing?", "About half: $2,400 to $4,560 versus $5,040 to $8,400 for a two-car driveway including removal."),
        faq("Is lifting cheaper than replacement?", "Usually, for a single panel; it is quoted by the injection contractor. It is not cheaper if the panel is cracked and has to be replaced anyway a year later."),
        faq("Can you resurface just one section?", "Technically yes, visually no. An overlay patch reads as a patch. If only one panel is bad, replacing that panel and leaving the rest is usually the better looking answer."),
        faq("How long does a resurfacing take?", "Two to three days including cure, with foot traffic after 24 hours and vehicles after about 72 in warm weather."),
    ]
    return page("resurface-vs-replace", "Resurface vs. Replace a Driveway or Pool Deck in Central Florida", "Resurface, repair or replace? The tap test, string line and hose test we run on Kissimmee slabs, a decision table with costs for a 480 sq ft driveway, and when polyurethane lifting is worth it.", "Resurface, repair or replace: the decision", body, faqs, [])


def four_vs_six():
    body = sec("4 inches or 6 inches of concrete?",
        cap(f"Four inches of 3,000 to 3,500 psi with fiber and edge rebar is right for cars, SUVs, patios, walks and pads under sheds and AC units; it runs {cost_range('concrete-driveway-broom')} in the {R} index. Six inches of 4,000 psi with a #4 rebar grid is right for boat trailers, RVs, moving and delivery trucks, workshop slabs and dumpster pads; it runs {cost_range('concrete-driveway-6in')}, 35 to 45 percent more. Thickness does not stop shrinkage cracks; base and joints do."),
        eyebrow="Comparison")
    body += sec("Side by side",
        table(["", "4 in slab", "6 in slab"], [
            ("Mix", "3,000–3,500 psi, fiber", "4,000 psi, fiber"),
            ("Steel", "#4 bars at edges and re-entrant corners", "#4 grid at 18 in on chairs"),
            ("Concrete per 100 sq ft", "1.23 cu yd", "1.85 cu yd"),
            ("Installed cost", cost_range("concrete-driveway-broom"), cost_range("concrete-driveway-6in")),
            ("480 sq ft drive", "$4,080–$6,480", "$5,520–$8,160"),
            ("Loads", "Cars, SUVs, pickups; sheds, AC, generators", "Boats, RVs, box trucks; workshops; dumpster pads (8 in)"),
            ("Joint spacing", "10 ft", "12–15 ft"),
            ("Code minimum (FBC R506)", "3½ in for a residential slab on ground; we do not go below 4 outdoors", "n/a"),
            ("Right-of-way apron (Orange County spec)", "n/a", "6 in, 3,000 psi, no steel"),
        ]), cls="alt")
    body += sec("The honest part", f"<p>Six inches will not save a driveway poured on saturated sand with a downspout at the edge; it will crack later and cost more. A 4-inch slab on 4 inches of compacted limerock with edge steel and joints cut within 12 hours outlasts a 6-inch slab on nothing. Spend on base first, thickness second, and thickness only where the load asks for it. Reinforcement choices are in {compare('rebar-vs-fiber-vs-mesh')}; the cracking mechanics in {guide('why-concrete-cracks-osceola')}.</p>")
    body += sec("What the extra two inches actually buy",
        table(["Load", "4 inches", "6 inches", "Verdict"], [
            ("Passenger cars and SUVs", "Adequate on a compacted base", "Overkill", "4 in"),
            ("Pickup truck, daily", "Adequate", "More margin at the edges", "4 in, 6 in at the apron"),
            ("Boat trailer with a tongue jack", "Cracks at the jack point over time", "Handles the point load", "6 in"),
            ("Motorhome or fifth wheel", "Will crack", "Correct with a rebar grid", "6 in, 4,000 psi"),
            ("Moving truck or concrete truck crossing", "Corner breaks", "Survives occasional crossings", "6 in at the crossing point"),
            ("Workshop with a lift or heavy shelving", "Not adequate", "Correct, with a thickened edge", "6 in plus edge detail"),
            ("Patio, walkway, pool deck", "Correct", "Wasted money", "4 in"),
        ], caption="Our specification practice. The Florida Building Code sets a 3½-inch residential minimum for a slab on ground; these are load-driven choices above that floor."), cls="alt")
    body += sec("What it costs to go thicker",
        f"""<p>A 480 square foot driveway at 4 inches takes about 6 cubic yards of concrete; at 6 inches it takes about 9. At $175 to $280 per delivered yard in this market, that is roughly $525 to $840 of additional material. Add the rebar grid that belongs in a 6-inch slab and the extra excavation and haul-off, and the installed difference in our index is about $3.00 per square foot, so $1,440 on that driveway.</p>
<p>Which is why the right answer is usually a hybrid: 4 inches through the field where the cars sit, 6 inches at the apron where the delivery trucks turn, and 6 inches on the pad where the boat lives. A proposal that specifies one thickness everywhere is either overcharging for the patio or undercharging for the boat pad.</p>""")
    body += sec("Thickness is the last thing to fix a base problem",
        f"""<p>Homeowners frequently ask whether going to 6 inches will stop the cracking they had before. On Osceola's fine sand the answer is usually no. A thicker slab spans a slightly wider void before it cracks and is stiffer at the edges, which helps, but the void keeps growing as long as roof water is washing sand out from under the edge. The same money spent on proper compaction, an extra two inches of limerock and a downspout extension buys more service life than two inches of concrete.</p>
<p>The order of priorities we use when a budget is fixed: drainage first, base second, joints third, thickness fourth, reinforcement fifth, strength last. That ordering surprises people, and it is the same ordering that explains the crack patterns in {guide('why-concrete-cracks-osceola')}.</p>""", cls="alt")
    faqs = [
        faq("How thick should a concrete driveway be in Florida?", "Four inches for cars on a compacted base; six inches with a rebar grid where boats, RVs or trucks park. The code minimum for a residential slab on ground is 3½ inches."),
        faq("Is 6-inch concrete worth the extra cost?", "For vehicle loads above a pickup, yes. For cars only, put the money into base and joints."),
        faq("3,000 or 4,000 psi?", "3,000 to 3,500 for cars; 4,000 for heavy loads. Strength above the load does not stop cracking."),
        faq("How much more does 6 inches cost?", "About 35 to 45 percent more per square foot in the current index."),
        faq("Is 5 inches a thing?", "Occasionally, under a hot tub or a light workshop, where 4 is thin and 6 is more than the load needs. It is a judgement call rather than a standard."),
        faq("Does a thicker slab need bigger joints?", "Joint spacing scales with thickness, so a 6-inch slab is jointed at 12 to 15 feet rather than 10, and the cut goes deeper because it is a quarter of the slab depth."),
    ]
    return page("4-inch-vs-6-inch", "4-Inch vs. 6-Inch Concrete Driveway: Which Loads Need It", "4 in vs. 6 in concrete for driveways, pads and slabs in Central Florida: mix, steel, cost per sq ft and per two-car drive, which loads need six inches, and why base and joints matter more than thickness.", "4-inch vs. 6-inch concrete", body, faqs, ["fbc-r506", "aci332", "orange-permit"])


def rebar_vs_fiber_vs_mesh():
    body = sec("Rebar, fiber or wire mesh in a driveway?",
        cap("Fiber in the mix controls plastic shrinkage cracking in the first hours; rebar carries load across a crack and holds edges and corners; wire mesh does the same as rebar only if it is held at mid-depth, which in a 4-inch slab it rarely is. Our standard: fiber plus #4 rebar at the edges and re-entrant corners on 4-inch work, a #4 grid on chairs at 18 inches in 6-inch work. Mesh walked to the bottom of a slab is doing nothing."),
        eyebrow="Comparison")
    body += sec("What each one does",
        table(["", "Synthetic fiber", "#4 rebar", "6×6 wire mesh"], [
            ("Controls plastic shrinkage (first 24 h)", "Yes", "No", "No"),
            ("Holds a crack tight (load transfer)", "Slightly (macro fibers more)", "Yes", "Yes if at mid-depth"),
            ("Edge and corner strength", "No", "Yes", "Partly"),
            ("Position control", "Throughout the mix", "On chairs, checked before pour", "Hard to hold up in 4 in; usually ends on the bottom"),
            ("Cost per 100 sq ft, installed", "$8–$15", "$25–$45 (edges) / $90–$140 (grid)", "$20–$35"),
            ("Where we use it", "Every slab", "Every slab (edges); grids in 6 in", "Rarely; only chaired in thicker slabs"),
        ]), cls="alt")
    body += sec("Why 'four inches with mesh' is a red flag", f"<p>Wire mesh has to sit in the top third of the slab to do anything. In a 4-inch pour there is no room for chairs, mesh and cover, so the crew pulls it up with a hook as they place, or means to and doesn't, and the mesh ends up on the base. The slab then has no reinforcement at all, which is how so many local driveways got their corner cracks. If a quote says mesh, ask how it is supported. Fiber costs less and works from the moment the concrete is placed; edge rebar handles the corners and the apron. Thickness questions are in {compare('4-inch-vs-6-inch')}; the crack types in {guide('why-concrete-cracks-osceola')}.</p>")
    body += sec("What each one is actually for",
        table(["Reinforcement", "What it does", "What it does not do", "Where we use it"], [
            ("Synthetic fiber in the mix", "Controls plastic shrinkage cracking in the first hours; adds a little toughness", "Nothing structural; will not hold a wide crack tight", "Every slab we pour"),
            ("#4 rebar at edges and corners", "Stiffens the free edge, holds a crack tight once formed, protects re-entrant corners", "Prevent cracking", "All driveways; the apron; where a walk meets a drive"),
            ("#4 rebar grid on chairs", "Distributes concentrated loads, holds cracks tight across the field", "Prevent cracking", "6-inch slabs, RV and boat pads, workshop floors"),
            ("Welded wire mesh, correctly chaired", "Similar to a light grid", "Work at all if it is lying on the ground", "Rarely; a grid is easier to place correctly"),
            ("Welded wire mesh, laid on the subgrade", "Nothing measurable", "Anything", "Never"),
        ], caption="The mesh row is the one that matters, because mesh pulled up with a hook during the pour ends up somewhere between the bottom and the middle, unevenly."), cls="alt")
    body += sec("The mesh problem, explained once",
        f"""<p>Steel only works where it is. In a slab that is bending because the ground under it moved, the tension is in the bottom half near the middle of a span and in the top near a support. Steel sitting on the subgrade under a 4-inch slab is below the zone that is working and has almost no cover, so it corrodes in the wet season and stains the surface. Steel at mid-depth does what it was specified to do.</p>
<p>The practical problem is that a 4-inch slab leaves very little room for chairs, mesh and adequate cover, and the traditional dodge of hooking the mesh up during the pour produces steel at random depths. That is why our standard on 4-inch flatwork is fiber in the mix plus #4 bars at the edges, and why we move to a properly chaired #4 grid when we go to 6 inches. If a quote you are comparing specifies wire mesh in a 4-inch slab, the question worth asking is how it will be held up.</p>""")
    body += sec("What each adds to the price",
        f"""<p>Fiber is the cheapest insurance in concrete, usually a modest per-yard addition at the plant, and it is in every mix we order. Edge bars on a 480 square foot driveway are a small material cost and an hour of labour. A full #4 grid at 18 inches on chairs is the real line item, adding roughly a dollar to a dollar fifty per square foot installed, which is part of why the 6-inch specification in our index sits about three dollars above the 4-inch one.</p>
<p>None of it substitutes for base and drainage, which is the point made in {guide('why-concrete-cracks-osceola')} and repeated here because it is the single most expensive misunderstanding in residential flatwork. Reinforcement decides what a crack does after it forms. Base and water decide whether it forms.</p>""", cls="alt")
    faqs = [
        faq("Do I need rebar in a concrete driveway?", "At the edges and corners on a 4-inch slab, yes; a full grid in a 6-inch slab for heavy loads."),
        faq("Is fiber mesh as good as rebar?", "Different jobs: fiber stops early shrinkage cracks; rebar holds cracks tight under load. We use both."),
        faq("Why not wire mesh?", "It only works at mid-depth, and a 4-inch slab cannot hold it there reliably."),
        faq("Does reinforcement stop cracking?", "No. Base, water control and joints stop cracks from being a problem; reinforcement keeps them tight when they happen."),
        faq("Is fiber enough on its own?", "For a patio or a walkway, usually yes with good joints. For a driveway we add edge bars, because the free edge is where loads concentrate."),
        faq("Will rebar rust and stain my driveway?", "Not with proper cover. Steel too close to the surface or lying in a wet subgrade will, which is another argument against mesh on the ground."),
    ]
    return page("rebar-vs-fiber-vs-mesh", "Rebar vs. Fiber vs. Wire Mesh for a Concrete Driveway", "Rebar, fiber or wire mesh for a driveway or slab: what each controls, what each cannot, cost per 100 sq ft, why mesh on the bottom of a 4-inch slab is nothing, and the standard we pour in Kissimmee.", "Rebar vs. fiber vs. wire mesh", body, faqs, ["aci332"])


def cool_deck_vs_pavers():
    body = sec("Cool deck (textured coating) or pavers around the pool?",
        cap(f"A textured acrylic coating over concrete (the product family people call cool deck) costs the least, {cost_range('concrete-resurfacing')} plus a texture coat on a sound deck, stays cooler and grippier than bare concrete, and needs re-coating every five to eight years. Pavers or stone cost more ({cost_range('paver-pool-deck')} as an overlay; travertine {cost_range('travertine-pool-deck')}), can be lifted and relaid, take new coping and drains, and are what most HOAs on the resort corridor expect."),
        eyebrow="Comparison")
    body += sec("Side by side",
        table(["", "Textured coating on concrete", "Pavers or stone"], [
            ("Installed cost", cost_range("concrete-resurfacing") + " + texture $3–$6/sq ft", cost_range("paver-pool-deck") + " (overlay); stone " + cost_range("travertine-pool-deck")),
            ("600 sq ft deck", "$4,800–$9,300", "$9,000–$14,400 (paver overlay); $12,000–$21,600 (travertine)"),
            ("Requires", "A sound, level concrete deck", "A sound deck (overlay) or a rebuilt base"),
            ("Heat (published)", "Light coatings: moderate, cooler than bare gray concrete", "Light travertine and marble coolest; pavers by color"),
            ("Grip", "Good when new; wears", "Good; sealer with grit"),
            ("Life before major work", "5–8 years to re-coat", "Seal every 2–4 years; units last decades"),
            ("Repair", "Patch shows; re-coat the deck", "Lift and relay"),
            ("Coping and drains", "Kept as is", "New bullnose coping; channel drain added"),
            ("Deck that is heaving or hollow", "Coating follows the movement", "Rebuild on compacted base"),
            ("HOA", "Color reviewed", "Palette usually on file"),
        ], caption=f"Ranges from the {R} index."), cls="alt")
    body += sec("Which we recommend", f"<p>Coating when the deck is sound, the budget is tight, and the coping and drains are fine. Pavers or stone when the deck has moved, when you want new coping or a drain, when the HOA expects it, or when the deck is a rental that gets pressure-washed weekly. Both need the deck to drain away from the pool; both get an anti-slip finish. Pages: {svc('concrete-pool-decks')}, {svc('paver-pool-decks')}, {svc('paver-travertine')}, {compare('travertine-vs-concrete-pavers')}.</p>")
    body += sec("What each one is",
        f"""<p>A textured acrylic deck coating, which most people still call cool decking after an early brand name, is a thin cementitious or acrylic layer troweled or sprayed onto a sound concrete deck and finished with a knock-down or spray texture. It renews a tired surface, adds grip and, in a light colour, takes the edge off the heat. It is a surface treatment and it inherits whatever the slab underneath is doing.</p>
<p>A paver deck is a structural change. Either thin pavers are laid over the existing sound slab, or the deck is rebuilt on a compacted base with a bedding course. It costs two to three times a coating, it adds height that has to be checked at door thresholds and pool coping, and it can be lifted and relaid for the rest of its life.</p>""")
    body += sec("The comparison that matters around a pool",
        table(["", "Textured coating", "Paver overlay", "Full paver rebuild"], [
            ("Installed, 600 sq ft", "$3,000 to $5,700", "$9,000 to $14,400", "Higher; base rebuild priced per site"),
            ("Time on site", "2 to 3 days", "3 to 4 days", "5 to 7 days"),
            ("Height added", "Negligible", "About an inch; check thresholds and coping", "Set to the required elevation"),
            ("If the slab later moves", "Cracks with it", "Settles; lift and relay", "Base was rebuilt, so less likely"),
            ("Barefoot heat", "Depends almost entirely on colour", "Depends on colour and material", "Same, and travertine is an option"),
            ("Renewal", "Re-coat every 5 to 8 years", "Re-sand and re-seal every 3 to 4 years", "Same"),
            ("Best when", "Slab is sound, budget matters, look is fine", "Slab is sound, want stone or paver look", "Slab is failing or elevation has to change"),
        ], caption="Ranges from the current Cost Index for a 600 square foot deck around a typical 14 by 28 pool."), cls="alt")
    body += sec("Deciding in the right order",
        f"""<p>Start with the slab, not the finish. Tap it and string-line it as described in {compare('resurface-vs-replace')}. If it is hollow at the coping or stepped at a crack, a coating is off the table and a thin overlay is a bad idea, because both follow the slab. If it is sound, the decision becomes budget and taste, and either answer is defensible.</p>
<p>Then decide the colour before the material, because colour is doing most of the work on barefoot heat ({guide('surface-temperature-pool-decks')}). A light coating beats a dark paver on a July afternoon. Finally, check the thresholds: a thin-paver overlay that puts the deck an inch higher can leave a sliding door with no clearance, and the fix at that point is expensive.</p>""")
    faqs = [
        faq("What is cool deck?", "A brand name that became the generic term for textured acrylic coatings over concrete pool decks; several manufacturers make current versions."),
        faq("Is cool deck cheaper than pavers?", "Yes, roughly half the cost of a paver overlay on a sound deck."),
        faq("Which stays cooler?", "Light coatings are cooler than bare gray concrete; light travertine and marble are cooler still."),
        faq("Can pavers go over a coated deck?", "Yes, if the deck under the coating is sound; the coating is cleaned or ground for bond."),
        faq("Can a coating go over pavers?", "No. Coatings are for concrete. Pavers get cleaned, re-sanded and sealed instead."),
        faq("Will a coating fix my cracked deck?", "It hides hairline cracks and nothing else. A cracked, hollow or stepped deck needs the base addressed first."),
    ]
    return page("cool-deck-vs-pavers", "Cool Deck vs. Pavers for a Florida Pool Deck: Cost & Heat", "Textured 'cool deck' coating vs. pavers or travertine around a Central Florida pool: cost for a 600 sq ft deck, heat and grip, life before re-coating, repair, coping and drains, HOA expectations.", "Cool deck coating vs. pavers around the pool", body, faqs, [])


def sealer_types():
    body = sec("Which sealer goes on which surface?",
        cap("Three families. Film-forming acrylics (solvent- or water-based) sit on top, give a wet or satin look, and need re-coating every two to three years; over moisture they haze white. Penetrating sealers (silane/siloxane, fluoropolymer) soak in, leave the look natural, breathe, and last three to five years; they are the only choice for travertine and marble. Joint-stabilizing sealers do both jobs on pavers by hardening the polymeric sand. Porcelain needs none."),
        eyebrow="Comparison")
    body += sec("Side by side",
        table(["", "Film-forming acrylic", "Penetrating (silane/siloxane, fluoropolymer)", "Joint-stabilizing"], [
            ("Look", "Wet or satin", "Natural", "Natural to light satin"),
            ("Life in Central Florida sun", "2–3 years", "3–5 years", "3–4 years"),
            ("Breathes", "No (hazes over moisture)", "Yes", "Mostly"),
            ("Slip", "Needs grit additive", "Minimal change", "Needs grit on decks"),
            ("Concrete pavers", "Yes, on a fully dry deck", "Yes", "Yes (best for driveways)"),
            ("Travertine / marble", "No", "Yes (only choice)", "No"),
            ("Stamped concrete", "Yes (standard)", "Yes (matte)", "n/a"),
            ("Broom concrete", "Optional", "Yes", "n/a"),
            ("Porcelain", "No", "Grout only", "No"),
            ("Stripping if it fails", "Expensive", "Not needed", "Rare"),
            ("HOA note", "Solterra allows only clear matte on concrete", "Fits matte rules", "Fits matte rules"),
        ]), cls="alt")
    body += sec("Failures we fix and what caused them", f"<p>White, cloudy pavers: a film sealer applied over moisture or over unfinished efflorescence. Peeling: film over a dusty or previously sealed surface. Slick pool deck: glossy film with no grit. Rust bleeding through a sealer: iron from well water sealed in before removal ({guide('rust-stains-irrigation-well-water')}). The process that avoids all four is on {svc('paver-sealing')}; polymeric sand, the other half of a paver deck's life, in {guide('polymeric-sand-guide')}.</p>")
    body += sec("The four families and what each is for",
        table(["Type", "How it works", "Look", "Renew", "Right for"], [
            ("Penetrating silane or siloxane", "Soaks in and repels water from within the pore structure", "No change; matte", "5 to 10 years", "Travertine, marble, natural stone, concrete where no sheen is wanted"),
            ("Acrylic, solvent-based", "Forms a film on the surface", "Wet look, high sheen", "2 to 3 years in full sun", "Stamped and decorative concrete, colour enrichment"),
            ("Acrylic, water-based", "Forms a thinner film", "Low to medium sheen", "3 to 4 years", "Pavers where a light sheen is wanted, indoor-adjacent areas"),
            ("Joint-stabilizing paver sealer", "Film plus a binder that locks the joint sand", "Low sheen; darkens slightly", "3 to 4 years", "Paver driveways and decks after re-sanding"),
            ("Urethane and epoxy top coats", "Hard chemical-resistant film", "Gloss", "5 to 10 years indoors", "Garage floors, not exterior flatwork"),
        ], caption="Renewal intervals are our practice for Central Florida sun and rain, which are harder on a film-forming sealer than a northern climate."), cls="alt")
    body += sec("The mistakes that cost the most",
        f"""<p><strong>Sealing too early.</strong> New concrete needs 28 days; new pavers need 60 to 90 days so efflorescence can work its way out. Sealing over either traps moisture and the sealer clouds.</p>
<p><strong>Film over a damp substrate.</strong> The most common failure we are called to fix. A deck sealed the morning after a rain, or a paver field sealed while the bedding sand is still wet, turns milky white within days. Stripping it is more work than the original sealing.</p>
<p><strong>A film-forming sealer on travertine or marble.</strong> Calcareous stone holds moisture and moves it; a film traps it, and the stone hazes or spalls at the surface. Penetrating only.</p>
<p><strong>Gloss on a pool deck without grit.</strong> A high-sheen acrylic on a wet deck is genuinely dangerous. Anti-slip aggregate broadcast into the final coat solves it and costs almost nothing.</p>
<p><strong>Recoating without stripping.</strong> Acrylic builds up, and each layer traps more of what is under it. There is a point where the only correct answer is to strip back and start again.</p>""")
    body += sec("What we seal, and when",
        f"""<p>Poured concrete driveways: usually nothing, unless the owner wants stain resistance, in which case a penetrating product at 28 days. Stamped and coloured concrete: a solvent-based acrylic at 28 days, renewed every two to three years, with grit where feet go. Concrete pavers: clean, re-sand with polymeric sand, then a joint-stabilizing sealer at 60 to 90 days and every three to four years after ({svc('paver-sealing')}). Travertine and marble: penetrating stone sealer at handover, renewed every two to three years on a sunny deck. Garage floors: the coating system carries its own top coat and needs nothing else ({svc('coatings-garage-floors')}).</p>
<p>One rule cuts across all of them. A sealer is a maintenance product, not a repair. Sealing a stained surface locks the stain in, sealing a moving slab does nothing for the movement, and sealing a paver field with washed-out joints just glues the problem in place. Clean, repair, re-sand, then seal, in that order.</p>""", cls="alt")
    faqs = [
        faq("Wet look or natural?", "Wet look is a film acrylic with more maintenance and slip risk; natural is a penetrating sealer with longer life. Stone must be natural."),
        faq("Why did my pavers turn white?", "A film sealer trapped moisture or efflorescence. Strip and re-seal dry with a breathable product."),
        faq("What sealer for travertine?", "Penetrating and breathable only, with an anti-slip additive on pool decks."),
        faq("How often?", "Film: every two to three years. Penetrating: three to five. Rental decks: every two to three regardless."),
        faq("How do I know when it is time to re-seal?", "Water stops beading and the colour looks flat and chalky. On a paver field, joint sand starting to loosen at the edges is the other signal."),
        faq("Can I seal it myself?", "Yes, and plenty of homeowners do. The two things that go wrong are sealing a damp surface and applying too much, both of which are harder to undo than to avoid."),
    ]
    return page("sealer-types", "Paver & Concrete Sealers Compared: Film vs. Penetrating", "Which sealer for which surface in Central Florida: film-forming acrylics vs. penetrating silane/siloxane and fluoropolymer vs. joint-stabilizing products, life in the sun, slip, stone rules, HOA matte rules, and the failures each causes.", "Sealer types compared", body, faqs, ["solterra"])


def get_pages():
    return [index(), concrete_vs_pavers(), travertine_vs_pavers(), stamped_vs_pavers(), resurface_vs_replace(), four_vs_six(), rebar_vs_fiber_vs_mesh(), cool_deck_vs_pavers(), sealer_types()]
