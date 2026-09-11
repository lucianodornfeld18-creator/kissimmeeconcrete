# -*- coding: utf-8 -*-
"""Last depth pass: comparisons, pricing and the handful of pages still short."""
from _helpers import sec, table

SECTIONS = {}
FAQS = {}


def _s(route, heading, html, eyebrow=None, cls=""):
    SECTIONS[route] = SECTIONS.get(route, "") + sec(heading, html, cls=cls, eyebrow=eyebrow)


# =========================================================== COMPARISONS
_s("/compare/", "The comparisons we have not written, and why",
   """<p>Asphalt against concrete for a residential driveway, because asphalt is uncommon on residential lots in this market and we do not install it, so we would be comparing one thing we do against one we do not. Gravel against concrete, for the same reason on all but the most rural parcels. Poured concrete against a concrete overlay on a new installation, because an overlay is a renewal product rather than a new surface.</p>
<p>And any comparison that turns on resale value, because we have no local sales data that would support a claim and every published figure we have found on the subject traces back to a national survey with no Osceola County component. It is the single easiest claim to make in this trade and the least defensible, which is why it appears nowhere on this site.</p>""",
   eyebrow="Deliberate gaps")

_s("/compare/concrete-vs-pavers/", "Repair economics over twenty years",
   """<p>The difference that most often decides this in practice is not the installed price. It is what happens the first time something goes wrong, and on a Central Florida lot something usually does: a utility cut, a settled area by a downspout, a root, a pool installation that needs access across the drive.</p>
<p>On concrete each of those is a saw cut and a patch, and the patch is visible for the life of the slab. On pavers each is a lift and a relay, and the result is invisible. Over twenty years a driveway might see two or three such events. Whether that difference is worth the premium depends entirely on how likely those events are on your lot, which is why the drainage history and the trees matter more to this decision than any general property of either material.</p>""",
   eyebrow="Over time")

_s("/compare/travertine-vs-concrete-pavers/", "Where each one is installed most around here",
   """<p>Pattern from our own work rather than a general claim. Travertine and marble concentrate on the resort corridor and the higher-end lakefront lots: Reunion, ChampionsGate, the larger Bellalago and Celebration homes, and newer builds around Narcoossee. Concrete pavers dominate everywhere else, including most of Kissimmee, St. Cloud, Poinciana and the Polk ridge subdivisions.</p>
<p>The split is mostly cost and partly expectation. In a community where the surrounding homes have travertine decks, a concrete paver deck reads as a downgrade in a way it does not on a street where every deck is concrete pavers. That is a real consideration on a rental property competing on photographs, and much less of one on a family home.</p>""",
   eyebrow="Local pattern", cls="alt")

_s("/compare/stamped-vs-pavers/", "What each one looks like at year fifteen",
   """<p>A stamped patio that has been re-sealed on schedule looks close to its original state, with softened release colour and a slightly flatter pattern relief where furniture has moved. One that has not looks dull, with pale traffic lanes and the antiqued highlights largely gone, and the fix at that point is a strip and reseal rather than a top-up coat.</p>
<p>A paver patio at fifteen years has softened in colour fairly evenly, has had its joints topped up three or four times, and probably has a few replaced units somewhere that are only visible if you know where to look. It has almost certainly been lifted and relaid in at least one area. Neither is better; they age in different directions and the maintenance each one asks for is different in kind rather than in amount.</p>""",
   eyebrow="Ageing")

_s("/compare/resurface-vs-replace/", "The cost of getting it wrong, both ways",
   """<p>Resurfacing a slab that needed replacing costs the overlay, then the replacement, then the removal of the overlay as part of the demolition. On a 480 square foot driveway that is roughly $2,400 to $4,560 wasted on top of the eventual $5,040 to $8,400, and a year or two of a driveway that looked good and then cracked.</p>
<p>Replacing a slab that only needed resurfacing costs the difference between the two, roughly $2,600 to $3,800 on the same footprint, and gains a longer service life for it. That is a poor decision rather than a disaster. The asymmetry is the reason we test rather than guess, and the reason we will tell an owner who wants the bigger job that the smaller one is sufficient.</p>""",
   eyebrow="Asymmetry", cls="alt")

_s("/compare/4-inch-vs-6-inch/", "How to specify this in your own words",
   """<p>If you are writing a brief for three contractors, the useful phrasing is by use rather than by number. Four inches at three thousand psi with fibre and number four bars at the edges through the parking area. Six inches at four thousand psi with a number four grid at eighteen inches on chairs under the boat pad and at the apron. Base as specified, compacted in lifts. Joints at ten feet in the four inch work, twelve to fifteen in the six.</p>
<p>Written that way, a contractor either prices it or explains why they would do something different, and both answers are useful. Written as a single thickness for the whole job, you get three quotes for three different things.</p>""",
   eyebrow="For your brief")

_s("/compare/rebar-vs-fiber-vs-mesh/", "Cover, and why it matters in Florida",
   """<p>Cover is the depth of concrete between the steel and the surface, and it is what keeps the steel from corroding. In a humid climate with a high water table and, in the coastal parts of the state, salt in the air, inadequate cover is how a slab ends up with rust staining at the surface and, eventually, spalling where the expanding corrosion pushes the concrete off.</p>
<p>That is a second reason mesh lying on the subgrade is worse than no steel at all: it has no cover below it and it sits in the wettest part of the slab. Properly chaired steel in a six inch slab has around two inches of cover top and bottom, which is what the standards intend and what keeps it working for decades.</p>""",
   eyebrow="Durability", cls="alt")

_s("/compare/cool-deck-vs-pavers/", "Thresholds, coping and the inch that matters",
   """<p>Before recommending a paver overlay we measure three things: the clearance under the sliding door threshold, the height of the screen enclosure track above the deck, and the relationship between the existing coping and the deck surface. A thin paver overlay adds about an inch, and any of those three can be the constraint that rules it out.</p>
<p>A textured coating adds effectively nothing, which is a genuine advantage on a deck where the thresholds are already tight. It is the kind of practical detail that decides these jobs more often than the aesthetic comparison does, and it is why the tape measure comes out before the sample board.</p>""",
   eyebrow="Measure first")

_s("/compare/sealer-types/", "How often is too often",
   """<p>Over-sealing is a real and common problem, particularly on paver driveways where an owner has engaged a different company each time. Each acrylic application adds film, each film traps more of what is beneath it, and after three or four cycles the surface looks plastic, hazes in patches and becomes slippery when wet.</p>
<p>The signal to seal is not the calendar; it is the surface. Water no longer beading, colour looking flat and chalky, joint sand loosening at the edges. If those signs are absent at the three-year mark, wait. A field that looks good and sheds water does not need another coat, and the money is better kept for the re-sanding it will eventually want.</p>""",
   eyebrow="Restraint", cls="alt")

# =============================================================== PRICING
_s("/pricing/", "A short glossary for reading a quote",
   table(["Term", "What it means"],
        [("Flatwork", "Horizontal concrete: driveways, patios, slabs, walks. Not footings or walls"),
         ("Base", "Compacted aggregate under the slab or the pavers; not the sand it is bedded on"),
         ("Subgrade", "The native ground under the base"),
         ("Proof-roll", "Loading the subgrade to find soft spots before building on it"),
         ("Lift", "One layer of base placed and compacted before the next goes on"),
         ("Control joint", "A tooled or saw-cut line that decides where a shrinkage crack goes"),
         ("Expansion joint", "A compressible separation between a slab and another structure"),
         ("Apron", "The section of driveway between the property line and the street"),
         ("Right-of-way", "The public strip containing the street, verge and sidewalk"),
         ("Edge restraint", "The buried edge that stops a paver field spreading"),
         ("Bedding course", "The one inch of screeded sand pavers are set into"),
         ("Polymeric sand", "Joint sand with a binder that hardens when watered"),
         ("Short load", "A ready-mix delivery below the truck minimum, carrying a surcharge"),
         ("Structural fill", "Imported material replacing unsuitable ground, compacted in lifts")],
        caption="If a term in a quote is not on this list and is not explained, it is fair to ask what it means and what it costs."),
   eyebrow="Glossary")

_s("/pricing/concrete/", "What a written proposal from us contains",
   """<p>Dimensions and total area for each element. Demolition and haul-off where it applies. Base depth and material. Slab thickness, mix strength, fibre and reinforcement with spacing and how it is supported. Joint layout and spacing. The finish. The drainage design, including any downspout work. Permit and notice of commencement responsibility. Access notes and anything about the site that affects the method. Exclusions, stated rather than implied. The payment schedule tied to milestones. The workmanship warranty and its exclusions. And a validity period, because material prices move.</p>
<p>That is longer than a one-line quote and it is the document that makes a comparison possible. If another contractor's proposal is missing four of those lines, the difference in the numbers is partly a difference in what is being bought.</p>""",
   eyebrow="What you get", cls="alt")

_s("/pricing/pavers/", "Lead times, which are part of the price of a decision",
   table(["Item", "Typical lead time", "Note"],
        [("Common concrete paver lines in stock", "Days", "Most of the standard palette"),
         ("Less common colour or size", "1 to 3 weeks", "Worth confirming before design is finalised"),
         ("Premium lines", "2 to 4 weeks", "Sometimes made to order"),
         ("Travertine, standard sizes and grades", "1 to 3 weeks", "Lot consistency matters on large orders"),
         ("Travertine or marble, premium grade or special size", "3 to 6 weeks", "Sometimes imported to order"),
         ("Large-format porcelain", "2 to 4 weeks", "Fewer local distributors"),
         ("Architectural review approval", "2 weeks to a month", "Usually the longest single item"),
         ("County or city permit", "3 days to 2 weeks", "Depends on jurisdiction and scope")],
        caption="Indicative lead times for this market. The association approval and the material are usually the two that set the start date, not our schedule."),
   eyebrow="Timelines")

_s("/pricing/kissimmee-concrete-cost-index/", "Change log",
   """<p><strong>Release Q3 2026, published 10 September 2026.</strong> First release. Eighteen items covering concrete flatwork, paver and stone work, sealing, repair and garage floor coatings, plus a delivered ready-mix reference. Built as a market composite from current supplier pricing in the Orlando market, published regional cost references and our own takeoffs for standard job sizes. No executed-contract sample yet, and the method note says so.</p>
<p><strong>Planned for the next release.</strong> Anonymised executed quotes added to the sample, with the count stated per line; items with fewer than five quotes remaining labelled as market composite. A per-project view alongside the per-unit table. And, if the measurement has been completed by then, the surface temperature figures for pool deck materials measured here rather than cited from elsewhere.</p>
<p>Each release keeps its label and date attached in the page, the JSON and the CSV, so a figure reused elsewhere carries its vintage with it.</p>""",
   eyebrow="Releases", cls="alt")

# ======================================================== OTHER PAGES
_s("/areas/orange-county-south/", "Soil and stormwater, one more note",
   """<p>Much of south Orange was developed after Florida's stormwater rules tightened, so lots here were graded to a designed system of swales, inlets and retention ponds, and the as-built grading is recorded. That is an advantage when it is respected and a liability when it is not: a patio or deck that blocks a designed route sends water to a neighbour, and on a plat where the route is documented that is straightforward to demonstrate.</p>
<p>So the first thing we establish on a south Orange lot is where the lot is supposed to drain. It takes a hose and ten minutes, and it decides the elevation of everything we build.</p>""",
   eyebrow="Stormwater")

_s("/areas/polk-county/", "A last practical note on ready-mix",
   """<p>Concrete for Polk jobs comes from Polk plants rather than the Orlando-area plants that serve our Osceola work, and the delivered price differs. We price from the plant that will actually serve the site rather than from a blended average, which means a Davenport quote and a Kissimmee quote can carry slightly different material lines for the same slab.</p>
<p>It also affects scheduling. A plant serving a fast-growing part of the county in spring has less spare capacity, and a first-light delivery slot has to be booked rather than assumed. We confirm the slot before committing to a pour date rather than on the morning.</p>""",
   eyebrow="Supply")

_s("/faq/", "How this site is organised, in one paragraph",
   """<p>Two pillars, concrete and pavers, each with service pages carrying specification and cost. Area pages for the cities and counties we work in, carrying jurisdiction, soil and community facts. Permit pages, one per jurisdiction, quoting the official rule. HOA pages for the communities whose written criteria we have read. Comparisons for the decisions people are actually weighing. Guides for the reasoning behind what happens. Tools for what can be calculated. Pricing for what things cost and how we worked it out. And these FAQ pages for the short answers.</p>
<p>Each question has one page that owns it. If you have landed somewhere that mentions your question but sends you elsewhere for the answer, that is deliberate rather than an oversight.</p>""",
   eyebrow="Map")

_s("/areas/champions-gate/", "Ready-mix and delivery timing here",
   """<p>ChampionsGate sits close to the I-4 interchange, which is convenient for delivery and inconvenient for timing, since the same interchange carries the morning traffic. A first-light pour needs the truck booked for a slot that gets it here before the corridor fills, and a mid-morning delivery can lose forty minutes to the approach.</p>
<p>We schedule accordingly, which in practice means pours here start earlier than on comparable jobs further from the interstate. It is a small logistical point that makes the difference between finishing before the afternoon heat and chasing it.</p>""",
   eyebrow="Logistics")

_s("/guides/", "Reading order, if you are starting from scratch",
   """<p>If you are about to replace a driveway and have never done it before, four pages in order will tell you most of what you need. Start with why concrete cracks here, which explains what went wrong with the one you have. Then the flatwoods versus ridge base guide, which explains what has to go under the new one. Then the contractor verification guide, which tells you what to check on whoever quotes it. Then the widening rules page if you are changing the footprint.</p>
<p>That is about half an hour of reading and it will make every quote you receive legible. Everything else here is for a specific situation rather than for the general case.</p>""",
   eyebrow="Where to start", cls="alt")

_s("/pavers/artificial-turf/", "The questions we ask before quoting turf",
   """<p>What is the area used for, and by whom. Does it get sun, and how much. Is there a pet, and if so what size and how many. Where does water currently go from that area. Is the ground level or does it need shaping. Is there an irrigation system in it that needs capping or relocating. And what is the edge condition on every side, since the junction with hardscape, fence or planting determines the detail.</p>
<p>Those seven answers change the base depth, the infill type, the drainage detail and the product grade, which is why turf is quoted per project rather than at a rate per square foot.</p>""",
   eyebrow="Scoping")

_s("/pavers/marble-porcelain/", "Slip resistance on stone and porcelain",
   """<p>Worth being specific, because the marketing language around this is vague. A honed or polished marble is slippery when wet and is not a pool deck surface. A tumbled or brushed finish on marble or travertine has good wet grip. Porcelain is manufactured to a stated slip rating, and outdoor-rated products are textured on the surface for that reason; an indoor porcelain tile used outside is genuinely dangerous around water.</p>
<p>So when we specify porcelain for a deck we name the product and its rating rather than describing it as outdoor porcelain, and when a client brings a tile they have chosen for its appearance we check the rating before agreeing to install it around a pool.</p>""",
   eyebrow="Safety", cls="alt")

_s("/concrete/architectural/", "Budgeting an architectural project realistically",
   """<p>Two pieces of advice from projects that went well. Decide the finish early, because it affects the mix, the formwork and sometimes the structure, and a finish chosen after the slab is designed is a finish that compromises. And budget for the sample panel as a line item rather than expecting it free, because a properly built sample is a small pour with real material and real labour and treating it as a giveaway is how it ends up being done carelessly.</p>
<p>The projects that go badly almost always share one feature: a finish specified from a photograph of work done elsewhere, in a different climate, with different aggregate, without anyone asking whether it is achievable here. The sample panel is the cheapest possible answer to that question.</p>""",
   eyebrow="Advice")

_s("/concrete/commercial/", "Insurance and prequalification",
   """<p>Commercial clients routinely ask for more than a residential certificate of insurance: specific limits, the owner and the management company named as additional insureds, a waiver of subrogation, and sometimes evidence of workers compensation coverage rather than an exemption. Some require prequalification before bidding and some require a payment or performance bond on larger scopes.</p>
<p>We can meet the standard commercial requirements and we will say plainly when a requirement, typically a bond on a scope above our usual size, is outside what we carry. It is better established at the enquiry stage than after a bid has been prepared, which is why we ask about it on the first call.</p>""",
   eyebrow="Requirements", cls="alt")
