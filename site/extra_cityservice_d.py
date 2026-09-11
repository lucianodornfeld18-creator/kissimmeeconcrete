# -*- coding: utf-8 -*-
"""Final per-page detail for the city×service pages: one specific angle each."""
from _helpers import sec, faq

SECTIONS = {}
FAQS = {}


def _s(route, heading, html, eyebrow="On this job"):
    SECTIONS[route] = sec(heading, html, eyebrow=eyebrow)


# ------------------------------------------------------------- ST. CLOUD
_s("/concrete/driveways/st-cloud/", "The apron detail at a brick street",
   """<p>Several downtown blocks still have their original brick paving under or alongside the asphalt, and where a driveway meets one the detail matters. We saw-cut a straight line at the brick edge rather than feathering concrete over it, set the apron to the existing street elevation so there is no lip for a low car, and leave the brick intact. Where the city's right-of-way approval covers the apron, that detail is what gets reviewed.</p>
<p>The other downtown constraint is width. Many of these lots were platted for a single car and a side yard, and the drive between the house and the property line is twelve feet or less. Widening usually is not available, so the design question becomes whether a turnaround or a parking pad can go behind the house instead, which is a different application and a different conversation with Public Works.</p>""")

_s("/concrete/slabs/st-cloud/", "Sequencing a pad with a building on it",
   """<p>Where a pad is going under a metal building or a carport, the order of operations is fixed and getting it wrong is expensive. The building supplier's drawings come first, because they carry the anchor bolt layout and the reaction loads. The pad is then designed around those, with a thickened edge or a perimeter footing where the columns land. The slab is poured, the anchors are set to the template rather than drilled afterwards where the supplier allows it, and the building goes up on a cured slab.</p>
<p>Owners frequently order the building first and ask us to pour to it, which works, and sometimes order the pad first from a generic size, which does not. A slab poured to the wrong bolt pattern cannot be adjusted, and the building cannot be adjusted to the slab either.</p>""")

_s("/concrete/repair/st-cloud/", "What a repair visit produces here",
   """<p>You get a marked sketch of the driveway or the walk with every crack drawn on it, the width of each measured with a comparator card, the panels that sounded hollow shaded, and the route the roof and irrigation water actually takes drawn in. Then two or three priced options rather than one number, because on a St. Cloud lot the right answer often depends on whether you are staying five years or twenty.</p>
<p>What we will not do is quote a patch over a crack with a step in it. It fails at the bond line within a year and has to be removed before a proper repair, so it makes the eventual job worse and more expensive. If that is the only thing in the budget right now, sealing the crack and fixing the downspout is the better use of the same money.</p>""")

_s("/pavers/driveways/st-cloud/", "Choosing a pattern for a wide St. Cloud drive",
   """<p>Lots here are generally wider than in Kissimmee's older subdivisions, and a wide paver field shows pattern more than a narrow one does. A forty-five degree herringbone is our default in the driving and turning area because of the interlock, but on a drive over about eighteen feet wide the field can carry a change: a soldier-course border with a banded grid, or a running-bond field with a herringbone apron where the turning loads concentrate.</p>
<p>That is a design choice with a cost attached, since every band and border is a line of cuts. We show the options with the waste factor attached to each rather than quoting one number and choosing the pattern later, because the difference between a plain field and a banded one on a wide drive is real money.</p>""")

_s("/pavers/pool-decks/st-cloud/", "Coping on an older St. Cloud pool",
   """<p>A good share of St. Cloud pools date from the 1980s and 1990s and still carry their original cantilevered concrete coping, which is the poured lip that overhangs the tile line. When a deck is being redone, that coping is usually the deciding cost. If it is sound and bonded, a thin paver overlay can run up to it with a clean joint. If it is cracked, hollow or has separated from the bond beam, it has to come off and be replaced with bullnose paver or stone coping, which means working right at the pool shell.</p>
<p>We check it with a tap and a straight edge before quoting, because the difference between a deck with coping included and one without is large enough that a quote which does not mention coping is not a quote for the same job.</p>""")

_s("/pavers/sealing/st-cloud/", "Timing a sealing visit around the weather",
   """<p>Sealing needs a dry surface, a dry joint and a rain-free window after application. Between June and September at the Kissimmee 2 station there are fifteen to eighteen days a month with measurable rain, most of it after two in the afternoon, which leaves a workable morning window but very little margin if the field is large. So we schedule sealing work in the drier half of the year where the customer can wait, and where they cannot, we split the job: clean and re-sand on one visit, seal on a settled morning.</p>
<p>The failure we are called to fix is a sealer applied to a field that was still damp in the joints, which turns milky within days and has to be stripped. Waiting two days is cheaper than stripping.</p>""")

# ----------------------------------------------------------- CELEBRATION
_s("/pavers/driveways/celebration/", "Working an alley without blocking it",
   """<p>On alley-loaded homes the working area is the alley itself, which is also how your neighbours reach their garages and how refuse collection runs. So the job is staged rather than spread: the apron is broken out and the base built in one day with the lane kept passable, material is delivered in smaller drops rather than one pallet run, and the lane is swept and open by the end of each day.</p>
<p>We also tell the neighbours either side before we start, because a note the day before prevents most of the friction. Where the association has published work hours, those govern, and they are worth checking before scheduling a delivery for seven in the morning.</p>""")

_s("/pavers/pool-decks/celebration/", "Making a small deck read as larger",
   """<p>Courtyard pools on compact lots leave deck areas that are generous on one side and tight on the other, and the instinct to fill the space with a busy pattern makes it feel smaller. What works is the opposite: a large-format unit, a simple layout running the long dimension, and a single border that follows the deck edge rather than breaking it into zones.</p>
<p>The other move is to treat the narrow side deliberately. A strip that is three feet wide looks like a mistake if the rest is eight; the same strip finished as a defined border course with a different unit reads as intentional. That is a design decision made on paper before anything is ordered, and it is the part of a small deck that most repays the time.</p>""")

_s("/pavers/sealing/celebration/", "A note on joint sand colour",
   """<p>Polymeric sand comes in several tones, and on a driveway field the joint colour reads at a distance almost as strongly as the paver does. A field re-sanded in a darker tone than the original looks like a different driveway from the street, which in a community with a designed streetscape is a visible change rather than a maintenance detail.</p>
<p>So we match the existing joint tone unless the owner is deliberately changing it, and where the original is no longer available we test a small area and look at it from the kerb before committing to the whole field. It costs nothing to check and it is not correctable once the joints are cured.</p>""")

_s("/pavers/walkways-steps/celebration/", "The transition to the public sidewalk",
   """<p>A Celebration front walk meets a public sidewalk that is part of the community's streetscape and sits at a fixed elevation. The private walk has to arrive at that elevation cleanly, with no lip, no change of slope at the joint and no cut into the sidewalk itself. Where the existing walk has settled and the sidewalk has not, the new walk is built back up to meet it rather than the other way round.</p>
<p>That junction is also where a mitred or squared border detail either looks deliberate or looks improvised, so it is set out on the ground with string before any base goes down. It is a small area that gets looked at more than any other part of the job.</p>""")

_s("/concrete/repair/celebration/", "What a tap test on a Celebration lanai finds",
   """<p>The lanai slabs on these homes are typically original and are restrained on at least two sides, by the house and by the screen enclosure footer. That restraint concentrates movement at the joint between them, so the crack we most often find runs along the footer line rather than across the slab. It is usually tight, level and cosmetic, and the right answer is to route and seal it rather than replace anything.</p>
<p>Where the tap test finds a hollow area it is almost always at the outside corner furthest from the house, which is where roof water from the enclosure has been discharging for twenty years. That one is a base problem and the repair starts with the water.</p>""")

# ------------------------------------------------------------- POINCIANA
_s("/concrete/driveways/poinciana/", "Sizing to the village, not to the catalogue",
   """<p>Lot widths vary considerably across the Poinciana villages, and the standard two-car driveway that fits comfortably in one village crowds the side setback in another. Before designing a replacement or a widening we pull the plat for the parcel and mark the setbacks, because the Design Control Board criteria and the county width cap both sit on top of a lot line that is where it is.</p>
<p>On the narrower lots the practical answer to a parking shortage is often not a wider drive at all but a parking pad behind the front building line where the criteria permit it, which is a different application. We would rather have that conversation at the design stage than submit a widening that gets refused on setback.</p>""")

_s("/concrete/patios/poinciana/", "Keeping the neighbour's drainage open",
   """<p>Poinciana lots were platted with lot-to-lot drainage patterns, and on a modest rear yard a patio can occupy the exact route water currently takes. That shows up two doors down after the first heavy storm, and the complaint goes to the association rather than to the county.</p>
<p>So we run a hose before we design. Where the patio has to sit on the drainage path, the path gets replaced with a swale alongside or a drain line to a legal discharge point, and that work goes into the same Design Control Board application as the patio, since the published criteria require prior approval for drainage work as well as for paving. Adding it later as a fix is a second application and a second wait.</p>""")

_s("/concrete/repair/poinciana/", "Why one panel is rarely the whole answer here",
   """<p>On a fifty-year-old Village driveway the panel that failed is not special. It is the one where the downspout happened to discharge, and its neighbours are the same concrete of the same age on the same absent base. Replacing it produces a good new panel beside four old ones, and the next call is usually within two or three years.</p>
<p>We will still do it, and for an owner who is selling soon or working to a fixed budget it is the right call. What we will not do is present it as a fix for the driveway. The sketch we leave shows the condition of every panel so the decision is made with the whole picture rather than the one that is currently worst.</p>""")

_s("/pavers/driveways/poinciana/", "The flush requirement in practice",
   """<p>The Design Control Board criteria require pavers to finish flush with the connecting driveway, walkway or roadway. On a replacement that is a construction requirement rather than a finishing detail, because eighty millimetre pavers on an inch of bedding sand over six inches of base is a thicker build-up than the four-inch slab coming out.</p>
<p>The consequence is deeper excavation and more spoil to haul, which is a real line in the quote rather than an oversight. A paver driveway installed at the existing grade without that excavation sits proud of the street, creates a lip at the garage and at the road, and does not meet the criterion. It is one of the more common reasons a paver job in Poinciana fails inspection by the board rather than by the county.</p>""")

# --------------------------------------------------- BUENAVENTURA LAKES
_s("/concrete/driveways/buenaventura-lakes/", "What the neighbours' driveways tell us",
   """<p>Because BVL went in street by street on a single programme, the driveways on either side of yours are the best available forecast for what yours will do. On a site visit we look at them: whether they have been replaced, where they have stepped, which way the cracks run. A street where three of the last five houses have replaced is a street where the original construction has reached its end, and that is worth knowing before deciding between a repair and a replacement.</p>
<p>It also helps with the practical side. Neighbours who are considering the same work in the same season share the mobilisation, and on a street where several drives are due it is worth asking before scheduling. The numbers improve for everyone and the street ends up looking coordinated rather than patched.</p>""")

_s("/concrete/repair/buenaventura-lakes/", "The downspout fix, in detail",
   """<p>The single highest-value thing on most BVL lots costs very little. A downspout that discharges within a foot of the slab edge is putting several hundred gallons a storm into the fine sand under it, and that is what hollows out the panel. The fix is to carry the discharge past the edge of the slab and onto grass or into a swale, either with a rigid extension, a buried drain line to a pop-up emitter, or a splash block long enough to actually move the water.</p>
<p>We do it as part of a repair and we recommend it even when no repair is being done, because it slows the deterioration of the slab you already have. It is the rare piece of advice on this site that costs almost nothing to act on.</p>""")

_s("/concrete/resurfacing/buenaventura-lakes/", "A candid pass rate",
   """<p>Of the BVL driveways we have inspected specifically for resurfacing, the majority have failed at least one of the three tests, most often the tap test. That is not a sales position; it is what a forty-year-old four-inch slab poured on unprepared fine sand with roof water at its edge does. The ones that pass tend to share a feature, usually a roof and gutter arrangement that happens to discharge away from the drive.</p>
<p>So the honest expectation for a BVL owner asking about resurfacing is that it is worth testing for and probably will not apply. Where it does, it is excellent value and we say so. Where it does not, we would rather tell you at the door than take the money and have the cracks come through next summer.</p>""")

_s("/pavers/driveways/buenaventura-lakes/", "Working on a narrow BVL lot",
   """<p>The standard lot here leaves little room either side of the driveway, so demolition spoil, base material and pallets of pavers all have to be staged somewhere, and that somewhere is usually the front lawn. We put plywood and boards down under the staging area, work the material off as the field progresses rather than dropping everything at once, and restore the lawn at the end.</p>
<p>Where a lot backs onto a lake or a conservation easement, spoil handling matters more, because material washed into a waterbody is both an association problem and a regulatory one. On those lots we stage away from the rear boundary and use silt protection where the grade runs that way.</p>""")

# ----------------------------------------------------------- FOUR CORNERS
_s("/pavers/pool-decks/four-corners/", "Deck drainage inside a rental screen enclosure",
   """<p>A screened lanai on a rental home is cleaned harder and more often than an owner-occupied one, and standing water on the deck after a wash shows up in guest photographs. So the drainage detail matters more here. A channel drain along the screen line takes both the roof runoff from the enclosure and the wash water, and it wants a real outlet rather than a pipe that ends under the deck.</p>
<p>Where we are overlaying an existing deck we check whether the original drain still functions before building over it, because a blocked or collapsed line under a new paver field is a much worse problem than it was under the old concrete. Camera inspection of an existing line is cheap compared with lifting a finished deck.</p>""")

_s("/pavers/sealing/four-corners/", "Talking to the cleaning contractor",
   """<p>On a managed rental the person who most affects how long your sealing lasts is not you and not us; it is whoever pressure washes the deck between guests. A turbo nozzle at three thousand psi will strip joint sand from a sealed field in a single pass, and the field then loses interlock whatever was applied on top.</p>
<p>So we ask to speak to them, or at least to leave written guidance with the manager: a surface cleaner rather than a wand, moderate pressure, and no direct blasting of joints. Where that will not happen, we tell the owner to budget re-sanding every two years instead of every four, because that is what the maintenance regime will actually produce.</p>""")

_s("/pavers/driveways/four-corners/", "Where the guest vehicles actually turn",
   """<p>On a rental property the wear is not spread evenly across the driveway. It concentrates where vehicles turn in from the street and where they swing to line up with the garage, and on a short drive those two points can be the same place. That is where edge courses roll and where the field ruts if the base is thin.</p>
<p>We look at the tyre marks on the existing surface before designing, because they show exactly where the loads land. The turning zone gets a concrete edge restraint, the full six inches of base without negotiation, and where the geometry allows it a wider radius at the street so the turn is less severe. Those three decisions are worth more than any material upgrade.</p>""")

_s("/concrete/repair/four-corners/", "Photographing a repair for an out-of-state owner",
   """<p>Most owners here are not in Florida, so the report matters as much as the repair. We photograph the defect before, the excavation or the preparation, and the finished work, and we send them the same day rather than at the end of the job. Where we find something that changes the scope, the photograph goes with the explanation before any additional work happens.</p>
<p>It is a small discipline and it removes most of the friction on remote jobs. An owner who can see the void under the panel does not need to be persuaded that the panel needed replacing, and a manager who has the photographs can answer the owner without calling us.</p>""")

# ---------------------------------------------------------- CHAMPIONSGATE
_s("/pavers/pool-decks/champions-gate/", "Getting material into a ChampionsGate rear yard",
   """<p>The typical lot here is deep and narrow with the pool filling most of the back, and the side yard is often four to six feet between the house and the fence. That is wide enough for a wheelbarrow and not for a machine, which sets the method: hand excavation, spoil out by barrow, material in the same way, and a skip or a dumpster staged on the driveway rather than the lawn.</p>
<p>It roughly doubles the excavation labour compared with an open lot, and it is a line in the quote rather than a hidden assumption. Where a gate can be temporarily removed or a fence panel dropped, we ask, because a six-foot opening instead of a four-foot one changes what equipment can reach the back.</p>""")

_s("/pavers/sealing/champions-gate/", "Testing before quoting a strip",
   """<p>On a twenty-year-old deck with an unknown sealing history, the only way to price the work honestly is to test. We clean a small area, apply a stripper to part of it, and see what comes off and what does not. That tells us whether the existing film is a single acrylic that will lift cleanly, several layers that will take repeated passes, or a product that is bonded well enough to seal over.</p>
<p>The difference between those outcomes is roughly a factor of two in the price, which is too large to guess at. A quote for a deck like this that does not mention testing has assumed one of the three, and it is usually the cheapest one.</p>""")

_s("/pavers/driveways/champions-gate/", "Matching an existing community palette",
   """<p>Where a community has a prevailing paver colour and the association reviews changes, the safest route for a replacement is to match what is there. That is harder than it sounds after twenty years: the original line may be discontinued, and even the current version of the same product will be brighter than a weathered field.</p>
<p>What we do is take a sample from the existing drive, compare it against current products in daylight rather than under a showroom light, and where nothing matches closely, propose a deliberate change that will read as intentional rather than a near-miss. A near-miss looks worse than a clear difference, and boards are generally more receptive to a considered change than to a failed match.</p>""")

_s("/concrete/repair/champions-gate/", "The equipment pad nobody looks at",
   """<p>Behind most of these houses is a small slab carrying the pool pump, the filter and sometimes the heater, and it is almost always the thinnest, least prepared concrete on the property. When it settles, the plumbing takes the strain, and a cracked union on a pool line is a more expensive problem than the pad.</p>
<p>It is worth checking when anything else is being done, because replacing a four by six pad while a crew is on site is a minor addition and a separate visit for it is not. We look at it as part of any rear-yard inspection and mention it whether or not it is what you called about.</p>""")

# ---------------------------------------------------------------- REUNION
_s("/pavers/pool-decks/reunion/", "Spa and water-feature edges",
   """<p>Many Reunion decks include a raised spa, a water feature or a fire bowl, and those are where deck problems concentrate. A raised spa is a concentrated load on a deck built for foot traffic, so the base under it has to be built for the load or the deck settles around it within a few years. A water feature puts a constant splash line on one area, which accelerates whatever the surface does with water.</p>
<p>When we rebuild a deck with any of those, the base under and around them is built separately from the field, usually on a footing rather than on compacted aggregate alone, and the surface immediately around a splash line is sealed on a shorter interval than the rest.</p>""")

_s("/pavers/travertine/reunion/", "Ordering stone for a large deck",
   """<p>A six or eight hundred square foot travertine deck is a large enough order that lot variation becomes visible. Natural stone changes between quarry lots in colour range, void pattern and sometimes thickness, and a deck finished from two lots can show a line where the second one started.</p>
<p>Where the quantity allows it we order the whole deck from a single lot and confirm that with the supplier in writing rather than assuming. Where it does not, we blend across the field from all pallets as we lay rather than working one pallet at a time, which distributes the variation instead of concentrating it. On a French pattern the blending has to be planned with the repeat, which is one more reason the layout is set out on paper first.</p>""")

_s("/pavers/sealing/reunion/", "Two surfaces, one property, two products",
   """<p>It is common here for a property to have concrete pavers on the driveway and travertine or marble on the pool deck, and they need different sealers applied by different methods. The driveway takes a joint-stabilising acrylic that locks the polymeric sand; the stone deck takes a penetrating sealer that changes nothing visually and lets the stone breathe.</p>
<p>The mistake, which we are called to correct more often than any other on stone, is one product used across the whole property because it was one visit. A film-forming sealer on travertine traps moisture from the bedding course and hazes it, and removing it is slow, chemical and not always complete. Our proposals name the product for each surface separately for exactly this reason.</p>""")

_s("/pavers/driveways/reunion/", "Short drives, tight radii and rental cars",
   """<p>Reunion's streets curve and several driveways meet them at an angle, which means a driver turning in at anything above walking pace clips the inside edge. On a paver field that is where the outside course rolls; on a concrete apron it is where the corner breaks.</p>
<p>Two design responses help. Widening the radius at the street where the right-of-way allows it, so the turn is less severe. And building the inside edge as a poured concrete restraint set flush, so the course that takes the hit has something continuous behind it. Neither is expensive at build time, and both are cheaper than repairing the same corner every few years.</p>""")

# -------------------------------------------------------------- DAVENPORT
_s("/concrete/driveways/davenport/", "Asking about water at the quote stage",
   """<p>The question worth asking any contractor quoting a driveway in Davenport is simple: will you wet the base before compacting it. On Candler and Astatula sands a base compacted dry is not compacted, and the answer tells you whether the crew works this soil regularly or has brought an Osceola method across the county line.</p>
<p>The follow-up is how they will check. A steel probe after each lift is the practical field test, and it takes seconds. A crew that runs a plate compactor over dry sand for ten minutes and calls it done has worked hard and achieved very little, and the slab above it will show that in its first wet season.</p>""")

_s("/pavers/driveways/davenport/", "Reading the association document before the design meeting",
   """<p>In Solterra the published guidelines decide the design before any aesthetic conversation starts: three cars wide maximum on an expanded driveway, no additional walking area alongside it, no painting or staining of concrete, and a clear matte sealer only with a submitted request. In Providence and the newer phases the governing documents differ and the developer's standards may still apply.</p>
<p>So the first thing we do on a Davenport paver job is obtain the current document for that specific community, rather than relying on what applied two years ago or on what a neighbour was allowed. Where we have read and verified a document, we quote it with the section reference; where we have not yet, we get it in writing from the manager before designing.</p>""")

_s("/pavers/pool-decks/davenport/", "Where a ridge deck settles first",
   """<p>On free-draining ridge sand a deck rarely fails from water. It fails where the load is, and on a rental-style pool deck that means three places: under and around a raised spa, along the traffic line from the sliding door to the pool steps, and wherever the outdoor furniture actually sits rather than where the plan said it would.</p>
<p>We build the base for those areas rather than for the average. Extra compaction passes along the door-to-steps line, a proper footing under a spa rather than aggregate alone, and where the furniture layout is known, attention to that area too. It is the same material and a little more time, and it is the difference between a flat deck at year five and a dished one.</p>""")

_s("/concrete/repair/davenport/", "Checking the builder warranty first",
   """<p>On the newer Davenport subdivisions, a driveway or lanai slab showing a dished area or a step within the first few years is often a base consolidation issue from the original construction rather than anything the owner has done. Many of those homes are still inside a builder warranty period, and a defect that the builder should address is money the owner does not need to spend.</p>
<p>So when we inspect a house built since about 2018 we say so, put the observation in writing with photographs, and suggest the owner raise it with the builder before commissioning us. It costs us the job more often than not. It is still the right advice, and it is the kind of thing worth knowing about whoever you end up hiring.</p>""")

_s("/concrete/slabs/davenport/", "Marking easements before staking",
   """<p>The single most common reason a pad has to come out in Polk County is not construction quality; it is location. Drainage and utility easements run along rear and side lot lines on most subdivision plats, they are invisible on the ground, and Polk's rules require slabs to meet setbacks from property lines and easements.</p>
<p>We pull the plat for the parcel and mark the easement lines on the ground with the pad outline before anything is excavated. Where the pad the owner wants will not fit clear of them, we say so at the design stage and look at alternatives, rather than building something that a later inspection or a utility crew turns into a demolition.</p>""")

# ------------------------------------------------------------ HAINES CITY
_s("/concrete/driveways/haines-city/", "Matching a builder finish",
   """<p>Production driveways in the newer subdivisions here were finished to a consistent specification, usually a light broom in a single direction with joints at a set spacing. An extension that ignores those details reads as an addition even before the colour difference shows up.</p>
<p>So we copy them deliberately: the same broom direction and texture depth, joints continuing the existing spacing and lining through at the seam, and the same edge tooling. It costs nothing and it is the difference between a widening that looks planned and one that looks bolted on. The colour will still differ for about a year, and there is no technique that avoids that.</p>""")

_s("/concrete/patios/haines-city/", "Keeping the builder's drainage swale open",
   """<p>New subdivision lots here are graded to drain to a swale between properties, and that grading was engineered and inspected as part of the development. A patio that fills or blocks the swale changes where water goes for your neighbour as well as for you, and on a new plat that is the kind of thing that gets noticed.</p>
<p>Before designing we identify the swale, keep the patio clear of it, and where the patio has to encroach, replace the conveyance with a drain line to the same discharge point. It is a small amount of extra work at build time and it avoids a dispute that is genuinely difficult to resolve once the concrete is down.</p>""")

_s("/concrete/repair/haines-city/", "Finding sound concrete under old repairs",
   """<p>On the older streets a slab has often been repaired two or three times across several decades, each layer bonded to the last with whatever product was current. Those layers delaminate at different rates, so the surface can look like one problem and turn out to be three.</p>
<p>The first hour of the work is grinding into it to find sound concrete, and occasionally that changes the recommendation: what looked like a surface repair turns out to be a slab with two inches of accumulated patching over a failed original. We price the investigation as part of the job rather than as an extra, and where the finding changes the scope we stop and show you before continuing.</p>""")

_s("/pavers/driveways/haines-city/", "Deciding whether the old slab stays",
   """<p>Where a sound concrete driveway is being covered in pavers, there are two routes. Leaving the slab and building on it saves the removal cost but raises the finished surface by two to three inches, which creates a lip at the street and at the garage door and usually needs a transition detail at both. Removing it lets the field sit at the correct elevation and lets us build a proper base, at the cost of the demolition.</p>
<p>On a drive that is being widened anyway, removal is almost always the better answer, because half the area is being excavated regardless and matching the two halves at different build-ups is awkward. On a straight overlay of an unchanged footprint with good thresholds, leaving it can work. We measure the door threshold and the street elevation before recommending either.</p>""")

# ------------------------------------------------- HARMONY AND NARCOOSSEE
_s("/concrete/driveways/harmony/", "Pricing a long drive in sections",
   """<p>A hundred and fifty foot driveway is not one job at one rate. It typically crosses more than one soil condition, may cross a swale or a culvert, and often changes width between the road entry, the run and the parking area at the house. Quoting it at a single rate per square foot produces a number that is wrong in both directions: too high for the easy sections and too low for the difficult ones.</p>
<p>Our proposals for rural drives break the run into sections with the base treatment, thickness and any fill stated for each, plus separate lines for the apron at the county road and the turnaround. It is a longer document and it is the only way the total means anything.</p>""")

_s("/concrete/slabs/harmony/", "Dark-sky lighting and other community standards",
   """<p>Harmony was planned with a dark-sky lighting standard, which affects anything we build that carries a light: a workshop slab with a wall pack, a pad with a security light, a walkway with path lighting. Fixtures have to be shielded and downward-directed, and colour temperature is typically restricted.</p>
<p>It is not our approval to give, and the community's current standards govern rather than our summary of them. What we do is raise it at the design stage, because a lighting fixture chosen for a pad and then rejected is a small but entirely avoidable delay, and because the standard is one of the things that makes the community what it is.</p>""")

_s("/pavers/driveways/harmony/", "Where the paver section should start and stop",
   """<p>On a long rural drive the paver section earns its cost at the two ends and not in the middle. At the road, a paver apron takes the turning loads, tolerates the utility cuts that happen in a right-of-way, and defines the entrance. At the house, a paver parking court handles the manoeuvring and is the surface people actually stand on.</p>
<p>Between them, concrete carries the run at a fraction of the cost. The junctions are where the design attention goes: a clean transition detail at each, with an expansion joint and a restrained paver edge, so the change of material reads as deliberate. We show the hybrid and the all-paver option with both numbers, because the difference is usually large enough to be a real decision.</p>""")

_s("/pavers/pool-decks/harmony/", "Tannin, shade and joints that stay damp",
   """<p>An open deck under mature oaks collects leaf litter, and oak tannin stains light surfaces. It also stays damp in shade long after the rest of the deck has dried, which is where organic growth establishes in the joints. Both are manageable and neither is a reason to avoid the trees.</p>
<p>What changes is the maintenance specification. Shaded joints get attention on a shorter interval than sunlit ones. Tannin comes out with a percarbonate cleaner rather than a rust or efflorescence product, and using the wrong one sets it. And a breathable penetrating sealer suits a deck that stays damp better than a film, which can cloud where moisture cannot escape. We set the schedule to the shaded areas rather than to the average of the deck.</p>""")
