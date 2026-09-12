# -*- coding: utf-8 -*-
"""Closing pass: short, page-specific additions for the pages still under their floor."""
from _helpers import sec, table

SECTIONS = {}
FAQS = {}


def _s(route, heading, html, eyebrow=None, cls=""):
    SECTIONS[route] = SECTIONS.get(route, "") + sec(heading, html, cls=cls, eyebrow=eyebrow)


# ---------------------------------------------------------------- HUBS
_s("/compare/", "Where a comparison stops being useful",
   """<p>Three of these decisions cannot be settled by reading. Whether your existing slab can carry an overlay depends on a tap test and a string line, not on a table. Whether pavers are worth the premium on your lot depends on the drainage history of that lot. And whether a material is approvable depends on a document your association holds rather than on anything general about the material.</p>
<p>So each page states plainly where the reading ends and a site visit or a document begins. That is the boundary we try to draw across this whole site: publish everything that is knowable in advance, and be explicit about what is not. A comparison that claimed to settle all three would be easier to write and worth less.</p>""",
   eyebrow="Limits")

_s("/guides/", "How the guides relate to the rest of the site",
   """<p>The service pages carry the specification: thickness, strength, reinforcement, base depth, joint spacing, cost. The city and county pages carry the local facts: which office, which soil, which association, how far. The guides carry the reasoning, which is why something happens rather than what to build.</p>
<p>That separation is deliberate and it is why a guide will send you to a service page for a number and a service page will send you to a guide for an explanation, rather than each repeating the other. If you are trying to decide what to do, start with a comparison. If you are trying to understand why your driveway did what it did, start here. If you are ready to price something, start with the service page or the cost guide.</p>""",
   eyebrow="Structure", cls="alt")

_s("/faq/", "Questions we cannot answer on a web page",
   """<p>Some questions look general and are not. What will my driveway cost, exactly. Can my pool deck be resurfaced. Will my association approve this. Do I need a permit at this address. Each of those depends on something specific: a measurement, a tap test, a document, a parcel boundary.</p>
<p>Where that is the case, this site says so rather than giving an average that would be wrong for most readers. The published ranges, the finder and the tools narrow the question as far as it can be narrowed in advance; the last step is a visit or a phone call to an office. That is not a sales funnel, it is the honest shape of the information.</p>""",
   eyebrow="Limits")

# ------------------------------------------------------------- PRICING
_s("/pricing/", "When these numbers will change",
   """<p>The index is refreshed quarterly, and the two inputs that move it are ready-mix pricing and paver material pricing. Both have moved more in the last several years than they did in the decade before, which is why every figure on this site carries a release label rather than being presented as a standing price.</p>
<p>If you are reading a figure here more than three months after the release date shown, check the current release before relying on it. The machine-readable copies carry the release date in the payload for exactly that reason, so a number reused elsewhere keeps its vintage attached.</p>""",
   eyebrow="Currency")

_s("/pricing/concrete/", "What is not in these numbers",
   """<p>Structural fill where a washed-out base is found under an old slab. Drainage work beyond extending a downspout: a channel drain, a French drain, a dry well or a regraded swale. Tree root work, including barriers and any arborist involvement. Access constraints that rule out a machine or require a pump truck. Engineered work of any kind. Sales tax where it applies to materials. Association fees.</p>
<p>All of those are real and none of them is hidden; they appear as their own lines in a proposal after a site visit. The reason they are excluded from the index rather than averaged into it is that averaging them would make every figure wrong for every job: too high for the straightforward ones, too low for the difficult ones.</p>""",
   eyebrow="Exclusions", cls="alt")

_s("/pricing/pavers/", "Two paver quotes that look different and are not",
   """<p>A worked example from this market. Quote A: a paver driveway at sixteen dollars a square foot, material named, six inches of base, concrete edge restraint, polymeric sand, removal of the old slab listed separately. Quote B: a paver driveway at thirteen dollars a square foot, material not named, base not mentioned, removal included.</p>
<p>Quote B looks cheaper by three dollars and includes the removal, which is worth two to four. The questions that resolve it are what paver, what base depth and what edge restraint. If the answers are a builder-grade sixty millimetre unit on two inches of sand with spiked restraint, the two quotes are not for the same driveway, and the difference will be visible in about three wet seasons. That is the entire reason we publish a specification rather than a rate.</p>""",
   eyebrow="Worked comparison")

_s("/pricing/kissimmee-concrete-cost-index/", "Who we built this for",
   """<p>Four audiences, in the order they use it. Homeowners sanity-checking a quote, which is the main one. Realtors and property managers budgeting repairs on a listing or a portfolio, who need a defensible number rather than a precise one. Other contractors, including ones who compete with us, because a market with published reference points is a better market to work in than one without. And answer engines and research tools, which is why it exists as structured data with a licence rather than only as a page.</p>
<p>That last audience is the reason for the format decisions: a stable URL, a dated release, a machine-readable copy, an explicit licence and a written method. Anyone can reproduce the table; what makes it citable is that the method is published alongside it and the vintage travels with the data.</p>""",
   eyebrow="Audience", cls="alt")

# --------------------------------------------------------- COMPARISONS
_s("/compare/cool-deck-vs-pavers/", "The question to ask before either",
   """<p>Is the slab sound. Everything else on this page is downstream of that answer. A sound slab supports both options and the choice becomes budget and taste. A slab with hollow areas, a step at a crack or separation at the coping supports neither, and money spent on either will follow the movement within a season or two.</p>
<p>It takes ten minutes to establish with a tap, a straight edge and a hose, and it is the first thing we do on a pool deck visit. Any quote for a deck surface that arrives without someone having done it is a quote for a surface treatment on an unknown substrate.</p>""",
   eyebrow="First question")

_s("/compare/4-inch-vs-6-inch/", "What six inches does not fix",
   """<p>It does not stop shrinkage cracking, which is controlled by joints and curing. It does not stop settlement, which is controlled by base and drainage. It does not compensate for a base that was never compacted, because a thicker slab over a void still bridges a void, just for slightly longer. And it does not make a slab watertight or stain-resistant.</p>
<p>What it does is carry a heavier load without cracking, resist edge breakage under concentrated wheel loads, and give reinforcement somewhere useful to sit. Those are real and specific benefits, and specifying six inches for any other reason is buying concrete instead of buying the thing that was actually needed.</p>""",
   eyebrow="Honest limits", cls="alt")

_s("/compare/stamped-vs-pavers/", "The five-year question",
   """<p>Ask yourself one thing before choosing stamped concrete: will you re-seal it. Not whether you intend to, but whether you realistically will, on a two to three year cycle, for as long as you own the property. The surface depends on it. A stamped patio that has been sealed on schedule at year ten looks close to new; one that has not looks tired, with worn traffic lanes and flattened colour.</p>
<p>Pavers ask for less discipline. A field that is three years past its re-sanding looks slightly loose in the joints and cleans up when it is finally done. There is no equivalent forgiveness in a failed acrylic. If the honest answer is that maintenance will be deferred, that is a genuine argument for pavers rather than a sales point.</p>""",
   eyebrow="The real variable")

_s("/compare/sealer-types/", "Reading a sealer label",
   """<p>Four things on the container tell you most of what matters. The chemistry, which will say silane, siloxane, acrylic, urethane or epoxy, and determines whether it penetrates or forms a film. The solids content, which determines how much material is actually left after the carrier evaporates. The carrier, solvent or water, which affects the sheen, the smell and the recoat behaviour. And the substrate list, which tells you whether the manufacturer intends it for concrete, for pavers, for natural stone or for all three.</p>
<p>The label will also carry a coverage rate, and exceeding it is the most common application error. More sealer is not more protection; on a film-forming product it is a thicker film that traps more moisture and fails sooner. Two thin coats beat one heavy one on every product we use.</p>""",
   eyebrow="Practical", cls="alt")

_s("/compare/rebar-vs-fiber-vs-mesh/", "What fibre actually does",
   """<p>Synthetic fibre is often described as replacing steel, which oversells it, and sometimes dismissed as marketing, which undersells it. What it does is specific: it controls plastic shrinkage cracking during the first hours, while the concrete is still soft and the surface is drying faster than the interior. In a Kissimmee July that is a real and common failure mode, and fibre substantially reduces it.</p>
<p>What it does not do is carry load or hold a structural crack tight. A slab that cracks because the ground under it moved will crack the same way with fibre in it. So fibre goes in every mix we order, and it sits alongside the steel rather than instead of it.</p>""",
   eyebrow="Specifics")

_s("/compare/travertine-vs-concrete-pavers/", "A note on what people actually regret",
   """<p>From the callbacks and remodels we do, two regrets come up repeatedly and neither is about the material choice itself. The first is colour: owners who chose a darker shade for appearance and then found the deck too hot to use barefoot in July. That is the most common one, and it applies to both materials equally.</p>
<p>The second is sealer: a glossy film applied to either surface, which looks impressive on handover day and is slippery when wet and cloudy within two years. Neither regret is about travertine versus concrete pavers. Both are about decisions made at the finish stage that are harder to undo than the material choice would have been.</p>""",
   eyebrow="Common regrets", cls="alt")

_s("/compare/resurface-vs-replace/", "What we do when the tests disagree",
   """<p>Occasionally a slab rings solid everywhere, shows no step across any crack, and still has water running under its edge from a downspout. That is a slab that passes two tests and fails the third, and the answer is not to resurface it and hope.</p>
<p>It is to fix the water first, wait a season, and re-test. If the slab has been losing support slowly, the movement shows up in that time and the resurfacing would have cracked. If it has not, you have a sound slab with the cause removed and an overlay that will last its full life. Waiting a few months is a hard recommendation to make and it is the right one often enough that we make it.</p>""",
   eyebrow="Edge cases")

# ------------------------------------------------------------ SERVICES
_s("/pavers/artificial-turf/", "What turf does not solve",
   """<p>It does not fix drainage. Turf over a compacted base drains at the rate that base allows, and on a flat lot with nowhere for water to go the area will still hold water, now under a surface you cannot see it through. Where drainage is the reason grass is failing, drainage is the thing to fix.</p>
<p>It does not eliminate maintenance, only mowing. Rinsing, brushing the pile upright in traffic lanes, topping up infill and clearing leaf litter are all ongoing, and in a pet area the rinse schedule is not optional. And it does not last indefinitely; ten to fifteen years in Florida sun is a realistic expectation for a quality product, less in full exposure.</p>""",
   eyebrow="Expectations")

_s("/pavers/marble-porcelain/", "Cutting and handling",
   """<p>Large-format porcelain needs a wet saw with a blade rated for porcelain and an operator who has cut it before; a masonry blade chips the glazed edge and the chip is visible on a finished deck. Marble is softer and cuts cleanly but chips at the arris if it is handled carelessly, and both materials are heavy enough in large formats that two people handle each unit.</p>
<p>That is worth knowing because it affects who should install it. A crew that installs concrete pavers well does not automatically install two centimetre porcelain well, and the failure mode shows up at every cut edge. We do both, and where a job is entirely large-format we say which of our people is doing it.</p>""",
   eyebrow="Craft", cls="alt")

_s("/concrete/architectural/", "Managing expectations about variation",
   """<p>Concrete is a site-cast material and it varies. Colour differs slightly between truckloads, a honed surface exposes aggregate unevenly where the finishing depth varied, and a board-formed wall carries the character of the boards including their knots and grain. Every one of those is normal and several of them are the point.</p>
<p>The sample panel exists to set that expectation in physical form before anything is committed. What we ask a client to approve is not a colour but a range: this is roughly what it will look like, with this much variation. A client who wants no variation wants a manufactured product rather than architectural concrete, and it is much better to establish that at the sample stage than at handover.</p>""",
   eyebrow="Variation")

_s("/concrete/commercial/", "Who we are a good fit for",
   """<p>Property managers with a portfolio of small flatwork items who want one crew that turns up, works around the tenants and finishes. HOA and CDD boards with amenity-centre walkways, pool decks and parking that need doing without closing the facility. Churches and small institutions where the work has to happen between services. Vacation-rental management companies with amenity areas across several communities.</p>
<p>Who we are not a good fit for: anyone who needs a general contractor of record, site drainage design, structural slabs or a full parking lot with subgrade and paving scopes. We will say that on the first call rather than after a site visit, because a quote that quietly omits the engineering is worse than a declined enquiry.</p>""",
   eyebrow="Fit", cls="alt")

_s("/pavers/outdoor-lighting/", "Maintenance of a low-voltage system",
   """<p>Low-voltage landscape lighting is durable and not maintenance-free. Fixtures set into a paver field collect debris and want clearing. Lenses cloud in Florida sun and are usually replaceable. Connections corrode where they were made with the wrong connector or left in standing water, which is the most common cause of a section going dark. And transformers have timers or photocells that drift and eventually fail.</p>
<p>None of that is expensive if the system was installed with accessible connections and a transformer sized with headroom. All of it is expensive if the connections are buried under a paver field with no junction access, which is why we place junctions where they can be reached and note their locations on the same drawing that records the conduit sleeves.</p>""",
   eyebrow="Over time")

_s("/concrete/resurfacing/", "How long you have to stay off it",
   """<p>Foot traffic returns about twenty-four hours after the overlay is placed, vehicles at roughly seventy-two hours in warm weather. If the surface is being sealed, add a day for the sealer and another twelve hours before furniture goes back. So a driveway resurfacing typically takes the vehicle off the drive for four days rather than for the two days the crew is on site, which is the part owners most often under-plan.</p>
<p>In the rainy season the placement itself needs a dry window, and a thin overlay caught by a downpour within the first half hour is ruined rather than damaged. We watch the radar the same way we do on a pour day and move the work rather than risk it.</p>""",
   eyebrow="Downtime", cls="alt")

_s("/pavers/retaining-walls-outdoor-living/", "The wall we most often decline",
   """<p>A wall holding a driveway or a pool deck above a neighbouring property, where the surcharge from the vehicles or the deck bears on the wall. That is a structural retaining wall regardless of its height, it needs an engineered design, and building it to a manufacturer's generic detail because it is only three feet tall is how walls fail.</p>
<p>We will build the decorative wall in front of an engineered structure, the seat wall on top of it, and the hardscape around it. We will not be the designer of record for the structural element, and when the honest answer is that a job needs an engineer we say so early, because finding out later usually means the work comes out.</p>""",
   eyebrow="Scope limits")

_s("/coatings/garage-floors/", "What a coated floor is like to live with",
   """<p>Easier to sweep, far easier to mop, and oil wipes off rather than soaking in. Hot tyres are a non-issue on a properly cured polyaspartic top coat. Dropped tools chip the coating in the same way they would chip concrete, and a chip in a flake system is less visible than one in a solid colour, which is a practical argument for flake beyond appearance.</p>
<p>What it is not is indestructible. A jack stand dragged across it will scratch it, a grinder spark shower will pit it, and a battery leak will discolour it. Spot repair is possible on a flake system and near-invisible; on a solid colour it always shows.</p>""",
   eyebrow="Living with it", cls="alt")

_s("/pavers/repair/", "When we recommend doing nothing",
   """<p>Slight unevenness that has stopped moving, joints that are a little low but still full, and minor colour variation are all things a paver field does with age, and none of them needs intervention. Lifting and relaying a field for cosmetic unevenness disturbs a base that has settled into equilibrium, and the result is often less flat than it was.</p>
<p>The things worth acting on are movement that is continuing, joints that have dropped below the chamfer, edges that have started to roll, and any area that rocks underfoot. Those get worse and they get worse faster once they start. The distinction is worth making because a great deal of paver repair work sold in this market is cosmetic.</p>""",
   eyebrow="Honest advice")

_s("/pavers/walkways-steps/", "Handrails and where they are required",
   """<p>Where a flight has enough risers, a handrail becomes a code requirement rather than a preference, and the threshold depends on the applicable code and the jurisdiction. On residential entry steps that question comes up more often than owners expect, particularly when a landing is being raised or a flight is being rebuilt with a different rise.</p>
<p>We raise it at the design stage rather than at inspection. Where a rail is required, the post fixings have to be planned into the step construction; retrofitting them into finished paver treads means coring and epoxy anchors and rarely looks as good as a planned detail.</p>""",
   eyebrow="Code", cls="alt")

# -------------------------------------------------------------- AREAS
_s("/areas/orange-county-south/", "What to do if you are near the line",
   """<p>Several neighbourhoods along the Osceola and Orange boundary have streets where one side is in each county, and a few parcels are split. If your address is anywhere near it, the jurisdiction question has to be settled from the parcel rather than from the street name or the mailing address, because the rules genuinely differ.</p>
<p>The finder on this site checks the address against the Census boundaries and flags results within a few hundred feet of a line. For anything flagged, the property appraiser's parcel record or a call to either building department settles it definitively, and we make that call before quoting rather than after.</p>""",
   eyebrow="Boundary cases") + None if False else None
_s("/areas/orange-county-south/", "Travel and scheduling from Kissimmee",
   """<p>Hunters Creek, Meadow Woods and Southchase are fifteen to twenty minutes from our base outside peak hours, which makes them among the closer parts of our service area. Williamsburg, Taft and the Lake Hart area are similar. That means we can take smaller jobs here than we can in Polk County, including single panel repairs and small pads, without travel dominating the price.</p>
<p>The practical caveat is the John Young Parkway and Orange Blossom Trail corridors at rush hour, which can double those times. Deliveries and pours are scheduled early for that reason, which suits the concrete anyway.</p>""",
   eyebrow="Logistics", cls="alt")

_s("/areas/polk-county/", "Two offices, and which one to use",
   """<p>Polk County's Building Division operates from 330 West Church Street in Bartow and from the Northeast Government Center at 200 Government Center Boulevard in Lake Alfred, both reachable on 863-534-6080. For the parts of the county we work in, Davenport, Haines City, Loughman, Winter Haven, Auburndale, Lake Alfred, Dundee, Lake Wales and Polk City, the Lake Alfred office is generally the closer and more convenient of the two.</p>
<p>Where a city has its own building department, and most of those listed do for addresses inside their limits, the city handles it instead. The distinction is by parcel rather than by mailing address, which in Polk County is a more common source of confusion than anywhere else we work because several city addresses cover large unincorporated areas.</p>""",
   eyebrow="Where to file")

_s("/areas/osceola-county/", "Growth, and what it means for flatwork",
   """<p>Osceola County has been among the faster-growing counties in Florida for two decades, with an estimated population around 481,700 in 2025 and more than half of residents identifying as Hispanic or Latino according to Census data. For a flatwork contractor that shows up in two ways. The housing stock is bifurcated between subdivisions of the 1970s to 1990s whose original driveways are now failing, and subdivisions of the last decade whose owners are adding patios, pads and pool decks to new houses.</p>
<p>It also shows up in language. A meaningful share of the homeowners we quote prefer to discuss the work in Spanish, which is why a Spanish section of this site is under consideration rather than dismissed. Until it exists, the notes field on the estimate form takes Spanish as readily as English, and so do we on the phone.</p>""",
   eyebrow="Context", cls="alt")

_s("/areas/lake-alfred/", "What a typical job here looks like",
   """<p>Most Lake Alfred work that reaches us is a full driveway replacement or a paver driveway on a lot where the original concrete has reached the end of its life, plus the occasional pool deck. Lots tend to be generous by Central Florida standards and access is usually straightforward, which keeps excavation costs down relative to the tighter subdivisions closer to Kissimmee.</p>
<p>Scheduling is the main difference. We work here in consecutive-day blocks rather than fitting a job around closer work, and we confirm ready-mix delivery from the Polk plants before committing to a start date rather than on the morning of the pour.</p>""",
   eyebrow="Practicalities")

_s("/areas/dundee/", "Before you call us here",
   """<p>Worth a straightforward note. If the job is a driveway, a paver field, a pool deck or a substantial patio, we will quote it and the price will be competitive. If it is a single panel, a small pad or a trip-hazard grind, a crew based in Winter Haven or Lake Wales will serve you better and cost you less, and we will tell you that rather than pricing the travel in.</p>
<p>Where we do work here the standards do not change: the ridge base method with each lift wetted and compacted, the same thickness and reinforcement decisions for the load, the same joint spacing and the same drainage design. Distance changes logistics, not specification.</p>""",
   eyebrow="Straight answer", cls="alt")

_s("/areas/auburndale/", "The lake-flats caveat",
   """<p>Parts of Auburndale sit low between the lakes on soils that behave much more like Osceola's flatwoods than like the ridge, with a shallower water table and poor drainage. On those lots the ridge base method is the wrong one: the subgrade needs proof-rolling and sometimes raising, and the slab needs to shed water decisively rather than simply sitting on a compacted base.</p>
<p>Because the two conditions can occur within a few hundred feet of each other here, we look up the map unit for the parcel and probe on site before specifying. It is a short step and it decides the whole approach to the base.</p>""",
   eyebrow="Soil caution")

_s("/areas/lake-wales/", "Material lead times at this distance",
   """<p>Two supply notes for a Lake Wales job. Ready-mix comes from Polk plants and is priced from the plant that will actually serve the site. Pavers and stone come from the same Orlando-area distributors we use elsewhere, which means the delivery is a longer run and the drop has to be scheduled rather than assumed, particularly for a full pallet order on a residential street.</p>
<p>Neither adds much to the price. Both add to the lead time, and the practical consequence is that a Lake Wales job wants a start date confirmed a little further ahead than a Kissimmee one.</p>""",
   eyebrow="Supply", cls="alt")

_s("/areas/polk-city/", "What we would need to know on the first call",
   """<p>The scope and rough size, so we can say honestly whether the distance makes sense. Whether the address is inside the city or in unincorporated Polk County, which decides the permitting. Whether there is an association. And whether access is straightforward for a ready-mix truck or a delivery, because on the larger lots around here that is not a given.</p>
<p>With those four answers we can usually tell you on the phone whether to book a visit or look closer to home, which saves everyone a trip.</p>""",
   eyebrow="First call")

_s("/areas/reunion/", "Scheduling around the resort calendar",
   """<p>Reunion's occupancy peaks around the winter season and major events, and the gaps in an individual property's calendar narrow accordingly. The practical consequence is that deck and driveway work here is best planned in the shoulder periods, and that architectural approval should be obtained well before the intended window rather than in parallel with it.</p>
<p>We work to the management company's access process and the owner's calendar together, and we will hold a block of consecutive days rather than starting a deck we cannot finish before the next check-in.</p>""",
   eyebrow="Timing", cls="alt")

_s("/areas/champions-gate/", "A note on gate access and deliveries",
   """<p>Gated phases here require access arrangements for the crew and, separately, for deliveries: a ready-mix truck, a paver delivery on a flatbed with a moffett, and a dumpster all need to be cleared in advance and sometimes need a specific gate. Getting that wrong costs a morning.</p>
<p>We ask for the access details and the delivery gate at the site visit and confirm them with the management company before the start date, rather than arriving with a truck and a gate code that does not work for commercial vehicles.</p>""",
   eyebrow="Access")

# ---------------------------------------------------------------- HOA
_s("/hoa/bellalago/", "Lakefront and waterway lots",
   """<p>A good share of Bellalago and Isles of Bellalago backs onto water, and on those lots two extra questions apply to any hardscape project. Where does the additional runoff go, since a new deck or a widened drive sends more water toward the same low point. And does the work sit within any conservation or drainage easement recorded on the plat.</p>
<p>We include the elevation and drainage note in the architectural submission for waterfront lots as a matter of course, because the committee reasonably asks about it and answering in advance avoids a round trip. Where a project would materially change where runoff goes, we design the alternative route as part of the same application rather than treating it as a later fix.</p>""",
   eyebrow="Waterfront lots")

_s("/hoa/celebration/", "Working hours and neighbour notice",
   """<p>Compact lots, alley access and a walkable street pattern mean construction here is closer to neighbours than in most subdivisions. Where the community sets permitted working hours, those govern, and they are worth confirming before scheduling a seven o'clock delivery.</p>
<p>Beyond the rules, we tell the immediate neighbours the day before we start on any job that will occupy an alley or a shared frontage. It is not required by anything and it prevents almost all of the friction that these jobs otherwise generate.</p>""",
   eyebrow="Neighbours", cls="alt")

# ---------------------------------------------------------------- FAQ
_s("/faq/cost/", "Why we publish ranges when most competitors do not",
   """<p>Because the alternative helps the wrong people. When nobody publishes, the homeowner's only reference points are national averages from lead-generation sites that have never seen this county, and the contractor who is relying on you having nothing to compare against has an advantage over the one who is not.</p>
<p>A published range with a stated method is checkable. If our number is out of line with the market, you can see it; if a quote you have received is far outside it in either direction, that is worth asking about. We would rather compete on what is in the base than on who kept the number hidden longest, and that position is easier to hold with the ranges in public.</p>""",
   eyebrow="Transparency")

# ------------------------------------------------------------- GUIDES
_s("/guides/tree-roots-driveways-central-florida/", "Planting near new flatwork",
   """<p>If a driveway or a walk is going in and landscaping follows, the species and the distance chosen now decide whether this page is relevant to you in ten years. Sabal palms and most small ornamentals are safe close to hardscape. Live oaks, laurel oaks and southern magnolias are not, and the distance that would actually be safe is usually more than a suburban lot allows.</p>
<p>Where a large shade tree is wanted anyway, and there are good reasons to want one in this climate, a root barrier installed at planting is the cheapest version of this intervention by a wide margin. Retrofitting one twenty years later means trenching through an established root plate, which is a decision for an arborist rather than for a paving crew.</p>""",
   eyebrow="Planning ahead")

_s("/guides/hb-803-permit-exemption/", "What we expect to change over the next year",
   """<p>Local implementation is still settling. In the first months after the effective date, different building departments in this region have taken visibly different approaches to the written request, from a dedicated form to an application with fees waived. That will converge, and this page will be updated as it does.</p>
<p>Two things are unlikely to change. The exclusions are statutory rather than local, so structural, electrical, plumbing, mechanical, gas and flood-zone work stay outside the exemption everywhere. And a driveway touching the right-of-way remains a right-of-way approval rather than a building permit question, which is the point most often misunderstood about this law.</p>""",
   eyebrow="Watch this", cls="alt")

_s("/guides/surface-temperature-pool-decks/", "What shade actually buys",
   """<p>The single most effective intervention on a hot deck is not the material. It is shade over the part of the deck people occupy. A pergola, a shade sail, a screen enclosure roof panel or a mature tree removes the direct solar load entirely from that area, and a shaded surface of any material sits far closer to air temperature than an exposed one of the best material available.</p>
<p>So the sequence we suggest is shade first for the lounging area, light colour second for the walking surfaces, and material third. Reversing that, choosing an expensive cool material and leaving the whole deck exposed, spends the most money on the smallest part of the effect.</p>""",
   eyebrow="The bigger lever")

_s("/guides/polymeric-sand-guide/", "Storing the leftovers",
   """<p>Polymeric sand activates with moisture, and a part-used bag left in a Florida garage through a summer will often be solid by the time it is wanted. If you keep leftovers for future top-ups, double-bag them, seal them and keep them somewhere genuinely dry.</p>
<p>The same applies to the surplus pavers worth keeping from any installation. Stored flat, off the ground and out of direct sun, they stay usable for years and are the difference between an invisible repair and a hunt for a discontinued line. We leave a small surplus on site for that reason and tell the owner what it is for.</p>""",
   eyebrow="Practical", cls="alt")

_s("/guides/concrete-curing-florida-heat/", "Cold-weather notes, briefly",
   """<p>Central Florida does occasionally drop near freezing, and when it does the rules change in the other direction. Concrete gains strength more slowly below about fifty degrees and very slowly below forty, so the seven-day and twenty-eight-day milestones stretch. Fresh concrete should not be allowed to freeze in its first day, which on the rare cold night here means covering it with insulating blankets rather than plastic alone.</p>
<p>It comes up a handful of times a winter and it is worth mentioning because the advice is the opposite of the hot-weather advice: instead of pouring early and cooling the mix, we start later in the morning when the ground and the air have warmed, and we protect the slab overnight.</p>""",
   eyebrow="The other extreme")

_s("/guides/septic-drainfield-concrete-driveway/", "Signs a system is already under stress",
   """<p>Worth noticing before adding anything on top of it. Grass that is noticeably greener and faster-growing over the drainfield than elsewhere, soft or spongy ground over the field, standing water or odour after heavy rain, slow drains inside the house, or a tank that needs pumping more often than it used to.</p>
<p>Any of those means the system is working hard already, and covering part of the field with a slab is a reliable way to shorten what is left of its life. Where we see them on a site visit we say so and suggest a septic contractor look at it before we quote paving that goes anywhere near it.</p>""",
   eyebrow="Warning signs", cls="alt")

_s("/guides/rainy-season-concrete-scheduling/", "What we tell customers in June",
   """<p>Expect the start date to be a window rather than a date. Expect an early start, often before seven. Expect the crew to make the call on the morning based on radar rather than on the forecast from three days earlier. And expect one postponement in a typical rainy-season job, which is normal rather than a sign that anything is wrong.</p>
<p>What you should not expect is a pour going ahead in the rain because the schedule said so. The forms and the base keep; the concrete does not, and a slab finished under a downpour is a resurfacing job within a year.</p>""",
   eyebrow="Expectations")

_s("/guides/rust-stains-irrigation-well-water/", "Where the iron comes from",
   """<p>Groundwater across much of Central Florida carries dissolved iron picked up from the aquifer, and it is invisible while it is under pressure and dissolved. The moment it leaves a sprinkler head and meets air, it oxidises, and what lands on concrete or stone is iron oxide, which is rust.</p>
<p>That is why the staining follows the sprinkler arc so precisely, why it is worse where a head overshoots onto hardscape and worse still where water pools, and why properties on city water rarely have the problem. It is also why treatment at the source works: if the iron is sequestered or filtered before the water reaches the head, there is nothing left to oxidise on the driveway.</p>""",
   eyebrow="The chemistry", cls="alt")

_s("/guides/driveway-widening-rules-osceola/", "One more thing to check",
   """<p>The utility boxes, meters and irrigation control valves that sit in the strip between the sidewalk and the street, or along the side of a driveway. Widening frequently runs into one of them, and paving over a utility box is not permitted and not sensible, since the utility will open it eventually.</p>
<p>The options are to design around it, to have the utility relocate it, which is their process and their timeline rather than ours, or to reduce the widening. All three are easier to handle at the design stage than after the forms are set, so we mark them with the setbacks when we stake the job out.</p>""",
   eyebrow="Utilities")

_s("/guides/buenaventura-lakes-driveway-replacement/", "Timing the work",
   """<p>Two seasonal notes for BVL specifically. The dry half of the year, roughly October through April, makes this work straightforward: six or seven rain days a month instead of sixteen, and a base that stays where it is put. And spring, from about March, is when demand climbs across this trade, so a driveway booked in the autumn gets a better date than the same driveway enquired about in April.</p>
<p>The work itself is three days on site plus permit time in front and cure time behind, so the vehicle is off the driveway for about ten days in total. On a street where several neighbours are replacing in the same season, sharing the mobilisation improves the numbers for everyone.</p>""",
   eyebrow="Scheduling", cls="alt")

_s("/guides/how-to-verify-a-concrete-contractor-florida/", "One more check worth two minutes",
   """<p>Search the business name and the phone number together. A contractor who has traded under several names, or a number that appears attached to different business names in different places, is not automatically a problem and is worth a question. So is a business address that turns out to be a mail drop when the proposal implies a yard and a workshop.</p>
<p>None of this is about size. Excellent work is done in this trade by two-person crews with a truck and no premises. It is about whether the entity you are contracting with is the one that will still be there when you need the warranty honoured.</p>""",
   eyebrow="Final check")

# ------------------------------------------------------- CITY×SERVICE
_s("/concrete/resurfacing/buenaventura-lakes/", "If the slab passes, what you get",
   """<p>A driveway that looked forty years old looking new for ten to fifteen, at roughly half the cost of replacement, in two to three days with the vehicle off the drive for four. On the BVL slabs that do pass the tests, it is the best value job on this site.</p>
<p>What we do first is fix the reason the slab survived being questionable, which is usually nothing at all, and the reason it might not survive the next decade, which is usually the downspout. Resurfacing over a slab while roof water keeps running under its edge is spending half the money and starting the clock again.</p>""",
   eyebrow="The upside")

_s("/pavers/sealing/reunion/", "Sealing before the winter season",
   """<p>The practical window for sealing a Reunion deck is the autumn, after the summer rain has eased and before occupancy climbs. Doing it then means a dry application, a full cure, and a surface that looks its best through the season when the property is photographed and occupied most.</p>
<p>Leaving it until spring means competing for dates with everyone else who left it, in a period when the calendar is already tight, and often accepting a compromise on the weather window.</p>""",
   eyebrow="Timing")

_s("/concrete/repair/champions-gate/", "A short list for a pre-season walk",
   """<p>Check the path from the driveway to the front door for any lip over a quarter inch. Tap the lanai slab near the enclosure footer and near the outside corner. Look at the driveway apron corner where delivery vehicles turn. And look at the equipment pad behind the house.</p>
<p>Those four take ten minutes and cover the great majority of what we are called out for here. Three of the four are inexpensive if caught early and considerably less so once a guest has tripped or a pool line has cracked.</p>""",
   eyebrow="Ten-minute check")

_s("/concrete/repair/davenport/", "What a consolidation repair involves",
   """<p>Unlike a washout repair, where fixing the water is half the job, a consolidation repair is mostly earthwork. The affected panel comes out, the base under it is excavated to sound material, and it is rebuilt in wetted, compacted lifts with a probe check after each. Then the panel is re-poured, doweled to its neighbours with an expansion joint at each edge.</p>
<p>Because the cause is the original base rather than an ongoing water problem, a properly rebuilt panel here does not recur. That is a meaningful difference from a flatwoods washout, where the same repair without addressing the drainage buys only a few years.</p>""",
   eyebrow="Method")

_s("/pavers/sealing/champions-gate/", "Budgeting for an older deck",
   """<p>For a twenty-year-old field, budget for the possibility of stripping rather than assuming a straight re-seal, and budget for a full joint clean-out and re-sand rather than a top-up. Those two together can double the figure a simple sealing quote implies.</p>
<p>The alternative, sealing over a failing film and topping sand onto compacted debris, costs less this year and produces a deck that needs the full treatment next year anyway, with an extra layer to remove. We test first so the number in the proposal is the real one.</p>""",
   eyebrow="Realistic budget")

_s("/concrete/repair/haines-city/", "When to call the builder instead of us",
   """<p>If the house was built within the last several years and the defect is a dished area, a step at a construction joint or cracking that looks like base consolidation, that is a construction issue rather than a maintenance one, and it may fall within the builder's warranty period.</p>
<p>We will inspect, photograph it and put the observation in writing so you can use it, and then step back. Where the builder declines or the period has passed, the repair is straightforward and we will quote it. Sending you to the builder first costs us the job often enough that it is worth saying we do it anyway.</p>""",
   eyebrow="First call")

_s("/concrete/repair/celebration/", "Sealing rather than replacing a cosmetic crack",
   """<p>On a restrained lanai slab a tight, level crack along the enclosure footer is doing what the slab is supposed to do, which is relieve stress in one predictable place. Replacing the slab to remove it usually produces another crack in the same location within a few years.</p>
<p>The right treatment is to route it to a clean profile and fill it with a flexible polyurethane sealant that moves with the slab, in a colour matched to the concrete. It is a modest job, it keeps water out of the base, and it looks like a joint rather than like a repair.</p>""",
   eyebrow="Right-sized fix")

_s("/concrete/repair/four-corners/", "Documenting for an insurance claim",
   """<p>Where damage is sudden rather than gradual, a vehicle, a fallen tree, a burst line, an insurer will usually want photographs, a written description of the cause and a scope with a price. We produce all three as a matter of course on a repair visit, and we will speak to an adjuster directly if that helps.</p>
<p>What we will not do is characterise gradual settlement or root damage as sudden. It is not, insurers know it is not, and a claim built on that description tends to fail at the point where it would have mattered.</p>""",
   eyebrow="Claims")

_s("/pavers/driveways/champions-gate/", "Protecting the field during the rest of the project",
   """<p>Where a paver driveway goes in while other work is happening on the property, a pool, a screen enclosure, landscaping, the driveway is the route everyone uses and the surface everything gets stacked on. A new field can be damaged more in two weeks of trade traffic than in ten years of use.</p>
<p>So on a multi-trade project we schedule the driveway last where we can, and where we cannot, we protect it with boards under any staging area and agree a route for heavy deliveries. It is an unglamorous conversation and it saves a remedial visit.</p>""",
   eyebrow="Sequencing")

_s("/concrete/repair/poinciana/", "Repair pricing on a modest budget",
   """<p>Where the budget is genuinely fixed, the order that gets the most out of it here is: extend the downspouts, seal the tight cracks, grind any trip lip on the walk, and leave the panels alone. That is a few hundred dollars, it removes the cause of further deterioration, and it keeps the driveway safe.</p>
<p>Replacing one panel with the water problem still live spends several times as much and buys less. We will do whichever you decide, and that is the recommendation we would make to a neighbour.</p>""",
   eyebrow="Priorities")

_s("/concrete/repair/buenaventura-lakes/", "Selling a house with a failing driveway",
   """<p>Two routes and both are defensible. Replace it, which is the larger spend and removes it as a negotiating point, and on a street where several neighbours have replaced it is what buyers now expect. Or disclose it, price the house accordingly and let the buyer deal with it, which is cheaper and honest.</p>
<p>What tends not to work is a cosmetic repair that makes a failing driveway look sound for a viewing. Inspectors tap slabs, the void is found, and the credibility cost across the whole transaction is worse than the driveway ever was.</p>""",
   eyebrow="At resale")

_s("/concrete/driveways/haines-city/", "A note for new-build owners",
   """<p>If your house is recent and you are widening or extending, check whether the driveway is still inside the builder's warranty before we alter it. Cutting into or tying onto a warranted slab can complicate a later claim, and it is worth a call to the builder first.</p>
<p>Where the warranty has expired or the builder confirms no objection, the work is straightforward. Where a defect already exists in the original slab, it is better addressed by the builder before anything new is joined to it.</p>""",
   eyebrow="Warranty check")
