# -*- coding: utf-8 -*-
"""Extra local depth for the St. Cloud, Celebration, Poinciana and Buenaventura Lakes city×service pages."""
from _helpers import sec, table, svc, city, tool, guide, compare, juris, hoa, faq, cost_range, steps, cs

SECTIONS = {}
FAQS = {}

# ============================================================ ST. CLOUD (6)
SECTIONS["/concrete/driveways/st-cloud/"] = sec(
    "Three street types, three different driveways",
    """<p>The 1909 grid between 13th Street and the lakefront was laid out with narrow lots, alley access on some blocks and live oaks that are now a century old. Driveways there are short, often twelve feet wide, and the constraint is almost never the concrete. It is the root plate under the apron and the brick street edge the new pour has to meet cleanly. We saw-cut to the brick line rather than pouring over it, and where a root has already lifted the old slab we price the root barrier and the arborist's opinion as separate lines instead of quietly pouring over it.</p>
<p>The 1980s and 1990s ranch streets off Nova Road, Canoe Creek Road and Old Hickory Tree Road are the volume work. Twenty by twenty-four is the common size, the slab is four inches on nothing, and the failure is a stepped panel at the garage. Those are straight replacements with a real base and a downspout extension.</p>
<p>East and south toward Holopaw and along Narcoossee the lots get large and the drives get long. A hundred and twenty feet of drive is four times the concrete of a suburban replacement and brings its own questions: where the mixer turns around, whether the culvert at the county road will take a loaded truck, and where the septic drainfield sits. We walk that route on the site visit and put the answer in the proposal.</p>""",
    eyebrow="St. Cloud streets") + sec(
    "What a long rural drive costs here",
    table(["Length at 12 ft wide", "Square feet", "4 in, 3,000 psi", "6 in with a rebar grid"],
          [("60 ft", "720", "$6,120 to $9,720", "$8,280 to $12,240"),
           ("100 ft", "1,200", "$10,200 to $16,200", "$13,800 to $20,400"),
           ("150 ft", "1,800", "$15,300 to $24,300", "$20,700 to $30,600"),
           ("Add a 30 ft turnaround", "360", "$3,060 to $4,860", "$4,140 to $6,120")],
          caption="Current Cost Index rates applied to lengths we quote regularly east of St. Cloud. A pump truck, structural fill or a culvert crossing is priced separately. Not a quote."),
    cls="alt")
FAQS["/concrete/driveways/st-cloud/"] = [
    faq("Can a concrete truck reach a lot off Old Hickory Tree Road?", "Usually, but not always. A loaded mixer is over thirty tons and needs a firm route, about twelve feet of clearance and somewhere to turn. We walk the route at the site visit and price a pump truck or buggies when it will not work."),
    faq("Do the brick streets downtown change anything?", "They change the edge detail. We saw-cut to the brick rather than lapping over it, and the city reviews anything in the right-of-way through Public Works and Engineering."),
]

SECTIONS["/concrete/slabs/st-cloud/"] = sec(
    "Sizing a pad for what will actually park on it",
    """<p>The most common mistake on a St. Cloud pad is building it to the vehicle instead of to the vehicle plus the way it is used. A twenty-four foot travel trailer needs more than twenty-four feet of pad, because the tongue jack lands ahead of the box and the stabilizers land outside the wheel track. A bass boat on a tandem trailer needs room to swing the tow vehicle. A workshop slab has to hold the building, the anchor bolts, and a door apron that keeps rain out of the building.</p>
<p>Our starting sizes, which we adjust on site: travel trailer up to thirty feet, twelve by forty; fifth wheel or Class A, fourteen by fifty; bass boat and trailer, ten by thirty; a tandem-axle utility trailer, ten by twenty-four. All at six inches with a number four grid at eighteen inches on chairs, because the loads are point loads on jack feet and trailer tongues rather than spread loads.</p>""",
    eyebrow="Sizing") + sec(
    "Pad elevation and the wet season",
    """<p>Smyrna and Myakka fine sand in this part of Osceola County holds a wet-season water table about twelve inches down, and EauGallie and Basinger soils east of the city hold it higher. A pad poured flush with the lawn is a pad that stands in water from June to September, and a trailer parked on it is a trailer whose tires sit in standing water for a third of the year.</p>
<p>So we build up. Two to four inches above finished grade, on four to six inches of compacted limerock, with the top sloped a quarter inch per foot so rain runs off, and the downspouts and irrigation heads moved clear of the edge. On the lots near Alligator Lake and East Lake Toho where the map unit is Basinger, we bring fill and raise it further, and we say so in the proposal rather than discovering it on excavation day.</p>""",
    cls="alt")
FAQS["/concrete/slabs/st-cloud/"] = [
    faq("How big should an RV pad be for a fifth wheel?", "Fourteen by fifty is our starting point, at six inches with a rebar grid. The extra length is for the tow vehicle and the jack feet, which land outside the box."),
    faq("Can a pad be added to an existing driveway later?", "Yes, doweled to the existing slab with an expansion joint at the seam. The new concrete will be lighter for about a year."),
]

SECTIONS["/concrete/repair/st-cloud/"] = sec(
    "What repair actually costs, by symptom",
    table(["What you have", "What we do", "Range", "How long it lasts"],
          [("One stepped panel at the garage, rest sound", "Extend the downspout, remove and replace the panel with a rebuilt base", "$1,020 to $1,620 plus removal", "As long as a new slab"),
           ("Tight crack, both sides level", "Route to a clean V and fill with flexible polyurethane sealant", "Minimum-charge visit", "Three to five years"),
           ("Trip lip on a downtown walk under an oak", "Grind flush, or replace the panel with a root barrier", "Hourly for grinding; panel at walk rates", "A year for grinding; a decade with the barrier"),
           ("Apron corner broken at the brick street", "Replace the apron section at six inches with edge steel", "Priced per section with the city right-of-way approval", "Twenty years plus"),
           ("Lakefront slab sinking into Basinger sand", "Raise with fill, rebuild the base, replace the slab with a swale", "Full replacement rates plus fill", "Decades if the water is managed")],
          caption="Ranges use the current Cost Index. The right answer depends on the tap test and the string line, which we do before quoting."),
    eyebrow="By symptom") + sec(
    "Why the lakefront is its own problem",
    """<p>The blocks between the old town grid and East Lake Tohopekaliga sit on soils that grade from Smyrna fine sand into Basinger and, in places, organic muck. Basinger holds water about six inches down in the wet season and the depressional phases sit at the surface. Concrete laid flush on that does not fail from load; it fails because the ground under it swells and shrinks with the water table and the slab has nowhere to shed to.</p>
<p>Patching those slabs is money spent twice. The repair that works is a raised replacement: fill to get the slab above the seasonal water, a compacted base, a positive slope, and a swale or a drain that takes the runoff somewhere. That is a bigger number than a patch and we say so at the door, with the soil map unit for the parcel in the proposal so the reasoning is checkable.</p>""",
    cls="alt")
FAQS["/concrete/repair/st-cloud/"] = [
    faq("Is a repair worth it on a 1990s driveway?", "If one panel has failed and the others ring solid under a tap, yes. If three or more are cracked through, the replacement is usually the better dollar and we price both."),
    faq("Do I need a permit to replace one panel?", "No, a repair in the same footprint is maintenance. Replacing the apron in the right-of-way does need the city's approval or the county driveway permit."),
]

SECTIONS["/pavers/driveways/st-cloud/"] = sec(
    "The city sends paver driveways to Public Works",
    """<p>St. Cloud publishes a list of work that does not need a building permit, and pavers for driveways and sidewalks are on it with a note to refer to Public Works. That is not the same as needing no approval. Public Works and Engineering reviews anything in the right-of-way, which includes the apron where your drive meets the street and any sidewalk crossing, and they care about the apron detail, the sidewalk elevation and drainage at the gutter line.</p>
<p>In practice this makes a St. Cloud paver driveway a little simpler than the same job in unincorporated Osceola, where the county driveway permit and the twenty-four-foot width cap apply. It also makes it easy to get wrong, because a contractor who has only worked the county side will file the wrong paperwork and lose two weeks. We confirm the jurisdiction with the {finder} before quoting, and {city_page} explains where the city line actually runs.</p>""".format(finder='<a href="/tools/permit-finder/">permit finder</a>', city_page='<a href="/areas/st-cloud/">our St. Cloud area guide</a>'),
    eyebrow="Approvals") + sec(
    "Base depth on a lakefront lot versus a Narcoossee lot",
    """<p>Six inches of compacted limerock in two lifts, one inch of screeded bedding sand, eighty millimetre pavers on a driveway, a concrete or spiked edge restraint and polymeric sand in the joints. That is the specification everywhere, and what changes across St. Cloud is what sits under it.</p>
<p>Toward the lake, the subgrade is wet for months and has to be proof-rolled and, in low spots, raised with structural fill before any rock goes down. Out toward Narcoossee and Sunbridge, the newer subdivisions sit on engineered fill placed during development, which is usually good material but is sometimes still settling on the most recently platted phases. In both cases the check is the same steel probe after each lift, and in both cases the failure we are called back to fix by other people's work is a base that was never compacted at all.</p>""",
    cls="alt")
FAQS["/pavers/driveways/st-cloud/"] = [
    faq("Do paver driveways need a permit in St. Cloud?", "The city lists driveway and sidewalk pavers as not needing a building permit and refers them to Public Works, which reviews work in the right-of-way. Outside the city, the Osceola County driveway permit applies."),
    faq("Will pavers sink on a lakefront lot?", "Not if the subgrade is raised and compacted first. Pavers on unprepared wet sand settle exactly like concrete cracks on it, and the base is where the money has to go."),
]

SECTIONS["/pavers/pool-decks/st-cloud/"] = sec(
    "Screened lanai or open deck changes the job",
    """<p>Most St. Cloud pools built since the late 1990s sit inside a screen enclosure, and that changes three things about a paver deck. The enclosure footer runs around the deck perimeter and the pavers have to be cut to it cleanly, which is slow work. Water that lands on the screen roof runs down the frame and concentrates at the base, so a channel drain along the screen line is usually part of the job rather than an upgrade. And the enclosure limits access, so material moves in by wheelbarrow through a door rather than by machine.</p>
<p>Open decks, common on the older lakefront homes and on the larger Narcoossee lots, are faster to build and harder to drain, because there is no obvious place to put the water. On those we set the deck to fall away from the pool at an eighth to a quarter inch per foot toward a swale or a dry well, and we check the fall with a level before the bedding sand goes down rather than after.</p>""",
    eyebrow="Lanai or open") + sec(
    "Overlay or rebuild, decided by the coping",
    """<p>The coping tells us more than the deck does. If the bullnose coping is still bonded, level and not cracked away from the bond beam, the deck underneath is usually stable and a thin-paver overlay works. If the coping has lifted, if there is a gap between the coping and the deck that keeps opening, or if tapping the deck near the pool gives a hollow sound, the deck has moved against the pool structure and an overlay would ride on the movement.</p>
<p>An overlay adds about an inch, which has to be checked at the sliding door threshold and at the enclosure track. A rebuild sets the elevation wherever it should have been, fixes the drainage, and costs more. Both are on {deck}, and the inspection that decides between them is the same one described in {cmp}.</p>""".format(deck='<a href="/pavers/pool-decks/">the pool deck page</a>', cmp='<a href="/compare/resurface-vs-replace/">resurface versus replace</a>'),
    cls="alt")
FAQS["/pavers/pool-decks/st-cloud/"] = [
    faq("Can pavers go over my existing pool deck?", "If the coping is sound and tapping the deck rings solid, yes, and it adds about an inch that has to clear the door threshold and the screen track."),
    faq("Does the screen enclosure have to come out?", "No. We cut to the footer and work through the door. It slows the job by a day or so on a typical deck."),
]

SECTIONS["/pavers/sealing/st-cloud/"] = sec(
    "A schedule that matches how the deck is used",
    table(["Surface", "First seal", "Re-seal", "Why this interval here"],
          [("Paver driveway, full sun", "60 to 90 days after install", "Every 3 to 4 years", "Tire traffic and about 52 inches of rain a year"),
           ("Paver pool deck inside a screen", "60 to 90 days", "Every 3 to 4 years", "Less UV, but pool chemistry and splash-out"),
           ("Open paver pool deck, full sun", "60 to 90 days", "Every 2 to 3 years", "UV plus chemistry is the hardest combination"),
           ("Travertine deck", "At handover", "Every 2 to 3 years", "Penetrating sealer only; never a film"),
           ("Front walkway, shaded", "60 to 90 days", "Every 4 to 5 years", "Little traffic, little UV"),
           ("Any surface after a re-sand", "After the sand cures", "Same as above", "Sealing loose joints glues the problem in place")],
          caption="Our intervals for this climate. The signal that it is due is water no longer beading and joint sand loosening at the edges."),
    eyebrow="Schedule") + sec(
    "Well water is the local complication",
    """<p>Outside the city utility service area, most St. Cloud homes irrigate from a well, and Central Florida well water carries iron. The orange arc that follows the sprinkler across a paver driveway is rust, and it will come back through a fresh sealer if the water keeps hitting the same spot. So on a well-irrigated property we do the sequence in this order: clean and treat the iron staining, re-sand, seal, and then talk about the sprinkler heads, because the cheapest permanent fix is usually an irrigation tech moving two heads.</p>
<p>Sealing a stained surface without treating the stain locks it under the film, where it is far harder to reach. That is the single most common reason we are asked to strip a sealer. The stain identification table and the removal sequence are in {g}.</p>""".format(g='<a href="/guides/rust-stains-irrigation-well-water/">the rust guide</a>'),
    cls="alt")
FAQS["/pavers/sealing/st-cloud/"] = [
    faq("How soon can new pavers be sealed?", "Sixty to ninety days, so efflorescence can work its way out first. Sealing sooner traps it and leaves a white haze under the film."),
    faq("Will sealing stop rust stains from my well water?", "No. It makes them easier to remove next time. Stopping them means adjusting the heads or treating the water."),
]

# =========================================================== CELEBRATION (5)
SECTIONS["/pavers/driveways/celebration/"] = sec(
    "What the Pattern Book actually controls",
    """<p>Celebration was master planned in the mid 1990s with architectural covenants that are unusually specific for Florida, and driveways are one of the things they reach. Approved paver products, patterns, colours and edge details are set out in the community's design guidance, and the architectural review committee meets monthly, on the third Monday, to consider applications. That cadence is the real schedule constraint: miss a meeting and the job moves a month.</p>
<p>Two details catch people out. The first is that joint sand colour and border courses are part of what gets reviewed, not just the field paver. The second is that the villages are not identical; North Village, South Village, Lake Evalyn, West Village and Artisan Park each carry their own accents, so an approval from a neighbour's project two streets over is not a precedent. We submit the product, the pattern, the colour and the edge detail together, with photographs, which is what the committee is looking for.</p>""",
    eyebrow="Architectural review") + sec(
    "Alleys, rear garages and where the driveway actually is",
    """<p>A large share of Celebration homes are rear-loaded from an alley, which means the driveway is a short apron between the alley pavement and the garage rather than a run from the street. Those are small jobs with awkward access, and the work has to be staged so the alley stays passable for neighbours and for refuse collection. We schedule alley work to open the lane by the end of each day and we tell the neighbours on either side before we start.</p>
<p>Front-loaded homes in the older villages have short, narrow drives with street trees close to the edge. The six-inch compacted limerock base the community's guidance calls for is the same, but the cutting is heavier because of the curves and the tree wells, and the waste factor on a curved field runs higher than on a rectangle. Both are priced by the square foot at the paver driveway rates on {p}.</p>""".format(p='<a href="/pavers/driveways/">the paver driveway page</a>'),
    cls="alt")
FAQS["/pavers/driveways/celebration/"] = [
    faq("How long does Celebration ARC approval take?", "The committee meets on the third Monday of each month, so plan on a month from a complete submission. An incomplete packet means the next meeting."),
    faq("Are all Celebration villages under the same rules?", "The core guidance is community-wide, but villages carry their own accents. We submit for the specific address rather than relying on a neighbour's approval."),
]

SECTIONS["/pavers/pool-decks/celebration/"] = sec(
    "Small lots, screened decks, tight access",
    """<p>Celebration lots are compact by design and many pools sit in a courtyard or a narrow rear yard between the house and the alley. That shapes the job more than the material choice does. Material comes in through a gate or across a neighbour's frontage, spoil goes out the same way, and a machine that would do the excavation in an hour on a Harmony lot does not fit at all. We price hand work honestly rather than discovering it on day one.</p>
<p>The design consequence is that every square foot counts. A deck that is eight feet wide on one side and three on the other looks like an accident; setting the pattern and the border to make the narrow side read as deliberate is most of the design work. Large-format pavers make small decks look larger and are usually approvable; the products and thicknesses we install are on {mp}.</p>""".format(mp='<a href="/pavers/marble-porcelain/">the marble and porcelain page</a>'),
    eyebrow="Courtyard decks") + sec(
    "Deck drainage in a community with engineered stormwater",
    """<p>Celebration's stormwater is a designed system of ponds, swales and inlets, and every lot was graded to send water to a specific place. A pool deck rebuilt to a new elevation can block that path, which shows up as water standing against a neighbour's foundation two doors down after the first heavy storm. So the first thing we check on a Celebration deck is the original lot grading and where the low point is, and the deck is set to keep that route open.</p>
<p>Inside a screen enclosure we run a channel drain along the screen line and tie it into the existing discharge rather than adding a new one. On an open courtyard deck we hold the fall away from the house at an eighth to a quarter inch per foot and, where the courtyard has no outlet, add a dry well sized for the deck area. Neither is optional in a community where the drainage is a shared system.</p>""",
    cls="alt")
FAQS["/pavers/pool-decks/celebration/"] = [
    faq("Can a machine get to my Celebration pool deck?", "Often not. Courtyard and alley-loaded lots usually mean hand excavation and wheelbarrow access, which we price rather than absorb."),
    faq("Do I need a permit for a pool deck in Celebration?", "Celebration is unincorporated Osceola County, so a deck not tied to the pool structure is usually flatwork. The architectural review is the binding approval; we confirm the permit question for the specific scope."),
]

SECTIONS["/pavers/sealing/celebration/"] = sec(
    "Sealing inside a community with an approved palette",
    """<p>Sealer changes how a paver looks. A wet-look solvent acrylic deepens colour significantly, and on a street where the approved palette is part of the architectural scheme that is a visible change, not a maintenance detail. In Celebration we default to a matte or low-sheen joint-stabilizing product that keeps the paver close to its approved appearance, and where an owner wants the wet look we suggest asking the committee first, because it is cheaper to ask than to strip.</p>
<p>The same logic covers the joint sand. Polymeric sand comes in several tones and the joint colour reads strongly at a distance across a driveway field. We match the joint to what is already on the street unless the owner is deliberately changing it with approval.</p>""",
    eyebrow="Appearance") + sec(
    "Cleaning without damaging a twenty-five-year-old field",
    """<p>Many Celebration paver fields are original to the build-out between 1996 and 2010, which means the pavers have a worn, softened surface and the joints have been topped up several times. Pressure washing at the settings a driveway cleaner uses on newer work strips the surface of a paver that age and blows out joint sand that then has to be replaced. We wash at reduced pressure with a surface cleaner, treat organic staining chemically rather than mechanically, and plan on a full re-sand as part of every sealing visit on an older field.</p>
<p>Efflorescence, the white bloom that appears on concrete pavers after rain, behaves differently on an aged field than on a new one: on old pavers it is usually mineral deposits from irrigation rather than salts migrating out of the unit, so an efflorescence cleaner may not touch it and a different chemistry is needed. Identifying which one you have before buying a product is the whole trick, and the identification table is in {g}.</p>""".format(g='<a href="/guides/rust-stains-irrigation-well-water/">our stain guide</a>'),
    cls="alt")
FAQS["/pavers/sealing/celebration/"] = [
    faq("Does sealing need architectural approval?", "A clear matte sealer is normally maintenance. A wet-look product visibly changes the colour, and in a community with an approved palette it is worth asking before applying it."),
    faq("Can twenty-five-year-old pavers be cleaned up?", "Usually yes, at reduced pressure with the right chemistry and a full re-sand. Aggressive washing does more harm than the dirt."),
]

SECTIONS["/pavers/walkways-steps/celebration/"] = sec(
    "Front walks are part of the streetscape here",
    """<p>In most subdivisions a front walk is a private detail. In Celebration it is part of a designed streetscape with a consistent relationship between the sidewalk, the front walk, the porch and the street trees, and the architectural guidance treats it that way. Width, alignment, material and the way the walk meets the public sidewalk all get reviewed, and a walk that is wider or more elaborate than the pattern is the kind of thing that comes back with conditions.</p>
<p>Practically, the work is small and fussy. A typical Celebration front walk is three to four feet wide and fifteen to thirty feet long, with a step or two at the porch, tree roots to route around, and irrigation directly under the route. The cutting is a large share of the labour because of the border course and the transition at the public sidewalk, which has to stay at the existing elevation.</p>""",
    eyebrow="Streetscape") + sec(
    "Steps, risers and the details that fail",
    """<p>Paver steps fail in three predictable ways. The riser height varies because the treads were set to the ground rather than to a consistent rise, which is both ugly and a trip hazard. The tread nosing is unsupported and works loose under foot traffic. And water gets behind the riser face and pushes it out over a few wet seasons.</p>
<p>What we do instead: set a consistent rise and run for the whole flight, build the step core in poured concrete or compacted base with a solid bearing under each nosing, bond the riser face rather than relying on sand, and drain behind the risers so water leaves rather than collecting. On a porch with existing concrete steps, capping with large-format treads is often better than rebuilding, and that is the detail shown in the entry-step photograph in {gal}.</p>""".format(gal='<a href="/gallery/">the gallery</a>'),
    cls="alt")
FAQS["/pavers/walkways-steps/celebration/"] = [
    faq("Can I widen my front walk?", "Possibly, with approval. The community's guidance treats the front walk as part of the streetscape, so width and alignment are reviewed rather than assumed."),
    faq("Can my concrete porch steps be capped with pavers?", "Often yes, with large-format treads bonded to sound concrete. It avoids demolition and gives a consistent rise, which a rebuilt flight does not always achieve."),
]

SECTIONS["/concrete/repair/celebration/"] = sec(
    "A twenty-five-year-old community's concrete is at an age",
    """<p>The first Celebration homes were occupied in 1996 and the build-out ran into the 2010s, so the oldest flatwork in the community is approaching thirty years and the newest is fifteen. Concrete at that age on Osceola's fine sand shows a consistent set of things: joint edges spalled where they were cut shallow, hairline map cracking on south-facing slabs, panel settlement where a downspout or an irrigation line has been running under an edge, and lifted sections where a street tree has matured.</p>
<p>Almost none of that is a failure of the original work. It is what flatwork does here after a quarter century, and the question is which parts are worth replacing now and which will last another decade. We tap-test and string-line each panel and give you the map rather than a single number, because on a Celebration lot the front walk and the driveway apron often need different answers.</p>""",
    eyebrow="Ageing") + sec(
    "Matching, approvals and the alternative to matching",
    """<p>New concrete next to twenty-five-year-old concrete does not match, and on a street with a designed appearance that matters more than usual. There are three honest options. Replace the whole element so it is uniform, which costs more but looks intentional. Replace the failed section and accept a lighter panel for a year or two while it weathers in. Or change the element to pavers, which sidesteps the matching problem and is often already in the approved palette.</p>
<p>The third option is why so many Celebration repair enquiries end as paver jobs. It needs architectural approval, which the second option usually does not, so the timeline changes. We price all three and let the committee calendar inform the choice; the submission contents are on {pk}.</p>""".format(pk='<a href="/tools/hoa-packet-checklist/">the packet checklist</a>'),
    cls="alt")
FAQS["/concrete/repair/celebration/"] = [
    faq("Will a replaced concrete panel match the rest?", "Not at first. New concrete is lighter for roughly a year and never matches a twenty-five-year-old slab exactly. Replacing the whole element or switching to pavers avoids the problem."),
    faq("Does a concrete repair need architectural approval?", "A like-for-like repair usually does not. Changing the material or the appearance does."),
]

# ============================================================ POINCIANA (4)
SECTIONS["/concrete/driveways/poinciana/"] = sec(
    "Which county you are in decides the permit",
    """<p>Poinciana straddles the Osceola and Polk county line, and the village you live in determines which building department handles your driveway. On the Osceola side the county driveway permit under section 22-50.6 applies, with the twenty-four foot residential width cap and the Building Office at 1 Courthouse Square in Kissimmee reviewing it. On the Polk side it is the Polk County Building Division out of Bartow or the Northeast Government Center in Lake Alfred, with its own rules about slabs in setbacks and in the right-of-way.</p>
<p>Nothing about the street tells you which one you are on, and the mailing address does not either, since both sides use Kissimmee addresses with the 34758 and 34759 ZIP codes. The {finder} resolves it from the address, and the two rule sets are quoted on {o} and {p}.</p>""".format(finder='<a href="/tools/permit-finder/">permit finder</a>', o='<a href="/permits/osceola-county/">the Osceola page</a>', p='<a href="/permits/polk-county/">the Polk page</a>'),
    eyebrow="Two counties") + sec(
    "The Design Control Board comes first, and it can run out the clock",
    """<p>Whichever county issues the permit, the Association of Poinciana Villages reviews the work first. Its Design Control Board criteria name concrete, asphalt or brick pavers as the driveway materials, require prior written approval before any driveway, patio, drainage or paved area is started, and treat an application that has not been answered within thirty days as disapproved rather than approved. That last provision is the one worth planning around: silence is not consent, and an application submitted and forgotten is a denial.</p>
<p>So the sequence is submit, confirm receipt, follow up before the thirty days elapse, get the written approval, then permit. We prepare the packet and track the clock, and the criteria we work to are quoted on {h}.</p>""".format(h='<a href="/hoa/poinciana-apv/">the APV page</a>'),
    cls="alt")
FAQS["/concrete/driveways/poinciana/"] = [
    faq("Is my Poinciana address in Osceola or Polk County?", "It depends on the village. Both sides use Kissimmee mailing addresses and the 34758 or 34759 ZIP, so we check the parcel rather than the address."),
    faq("What happens if the Design Control Board does not respond?", "Under the published criteria an application not acted on within thirty days is deemed disapproved. We track the clock and follow up before it runs out."),
]

SECTIONS["/concrete/patios/poinciana/"] = sec(
    "Rear yards, screen rooms and the setback question",
    """<p>The standard Poinciana lot is modest, and a rear patio usually runs from the back of the house toward a rear setback that is closer than owners expect. Before we design, we pull the plat and mark the setback, because a slab that crosses it is a slab that has to come out. A detached slab that sits clear of the setback and carries no structure is generally flatwork; one that is attached to the house, sits within a setback, or will later carry a screen room or a roof is a permitted structure with footings.</p>
<p>That last point is where most Poinciana patio projects go sideways. A patio poured at four inches with no thickened edge cannot take a screen enclosure later without adding footings, and adding footings to an existing slab costs more than building it right the first time. If a screen room is even a possibility, we design for it now.</p>""",
    eyebrow="Layout") + sec(
    "Drainage between neighbours",
    """<p>Poinciana's villages were platted with lot-to-lot drainage patterns that a patio can interrupt. A slab that fills the low corner of a yard sends water to the neighbour, and that is the complaint that reaches the association rather than the county. So we look at where the yard currently drains, keep that route open, and where the patio has to occupy it, we replace the path with a swale or a drain line to a legal discharge point.</p>
<p>The Design Control Board criteria require prior approval for drainage work as well as for paving, which means a French drain added later to fix a problem the patio caused is itself an application. Doing the drainage as part of the original submission is both cheaper and faster.</p>""",
    cls="alt")
FAQS["/concrete/patios/poinciana/"] = [
    faq("Can I screen in my patio later?", "Only if the slab was built for it. A screen enclosure needs a footing at the perimeter, so tell us now and we design the edge for it."),
    faq("Does a patio need Design Control Board approval?", "Yes. The published criteria require prior written approval for any patio, paved area or drainage work."),
]

SECTIONS["/concrete/repair/poinciana/"] = sec(
    "In Villages 1 through 6 the original slabs are done",
    """<p>The earliest Poinciana villages were platted in the 1970s, and the driveways that went in with those houses are now fifty years old. They were poured thin, on native sand, before anyone in Florida routinely specified a base for residential flatwork. What we find when we lift them is consistent with what we find in Buenaventura Lakes and for the same reason: no rock, a scoured channel under the downspout line, and mesh rusted through where there was any.</p>
<p>At that age a single panel repair is rarely the right call. The neighbours' panels are the same age and the same construction, and fixing one is buying a year. We price the panel and the full replacement side by side and let the numbers decide, the same way we do in {g}.</p>""".format(g='<a href="/guides/buenaventura-lakes-driveway-replacement/">the BVL guide</a>'),
    eyebrow="Vintage") + sec(
    "Solivita is a different problem",
    """<p>Solivita's homes date from 2000 onward and were built with better flatwood practice, so the failures there are not age failures. They are irrigation failures, tree-root lifts on the older phases, and settlement where a utility trench crossed a driveway. Those are genuinely repairable, and a single panel replacement or a lift can be the right answer.</p>
<p>The complication in Solivita is the architectural requirement that replacement driveways and walkways match the original builder's style and materials, and that requests for a driveway modification go through architectural review. So a repair that changes nothing visible is straightforward; a repair that means a different colour or finish is an application. The published requirements are on {h}.</p>""".format(h='<a href="/hoa/solivita/">the Solivita page</a>'),
    cls="alt")
FAQS["/concrete/repair/poinciana/"] = [
    faq("Is it worth repairing a 1970s Poinciana driveway?", "Rarely more than once. At fifty years, with no base under the slab, the panel you fix is surrounded by panels of the same age. We price the repair and the replacement together."),
    faq("Can I change materials when I repair in Solivita?", "Only with architectural approval. The published requirements call for replacements in the original builder's style and materials."),
]

SECTIONS["/pavers/driveways/poinciana/"] = sec(
    "Pavers are an approved material, with conditions",
    """<p>The Design Control Board criteria name brick pavers among the acceptable driveway materials, which makes a paver driveway straightforward to approve in principle. The conditions are where attention is needed. Pavers have to sit flush with the connecting driveway, walkway or roadway, so the transition at the street and at the garage cannot have a lip. Any walkway adjacent to the dwelling is limited to two feet in width unless the board approves otherwise. And approval has to be in hand before work starts.</p>
<p>The flush requirement is a real constraint on a replacement, because eighty millimetre pavers plus a one inch bedding course plus six inches of base is thicker than the four inch slab coming out. Either we excavate deeper, which is normal, or the finished surface sits proud of the street. We excavate.</p>""",
    eyebrow="Approval") + sec(
    "Base depth on a lot with a fifty-year-old drive",
    """<p>Replacing a 1970s concrete driveway with pavers in Villages 1 through 6 means removing the slab, and what is underneath is not a base. It is the original sand with whatever the last fifty years of roof water has done to it, usually including a washed channel along one edge. That material has to come out to full depth, soft pockets have to be replaced with structural fill compacted in lifts, and then the six inches of limerock goes in.</p>
<p>Contractors who price a paver driveway off the square footage alone and assume they can screed sand over the existing grade produce a field that settles within two wet seasons. Our proposals separate the removal, the fill and the base so the comparison with another quote is on the same terms; the {pb} produces a specification you can hand to everyone bidding.</p>""".format(pb='<a href="/tools/project-brief/">project brief tool</a>'),
    cls="alt")
FAQS["/pavers/driveways/poinciana/"] = [
    faq("Are pavers allowed in Poinciana?", "Yes. The published Design Control Board criteria name brick pavers among the acceptable driveway materials, with the condition that they finish flush with the connecting driveway, walkway or roadway."),
    faq("Why does a paver driveway need deeper excavation than the old slab?", "Because eighty millimetre pavers on a one inch bedding course over six inches of base is thicker than the four inch slab being removed, and the finished surface has to stay flush with the street."),
]

# ==================================================== BUENAVENTURA LAKES (4)
SECTIONS["/concrete/driveways/buenaventura-lakes/"] = sec(
    "A neighbourhood built in one decade, failing on one schedule",
    """<p>Buenaventura Lakes went in as a Landstar Homes development from the late 1970s through the 1990s, which means most of the driveways on a given street were poured within a few years of each other, to the same specification, by the same crews. They are failing on the same schedule too, which is why the street can look like a coordinated replacement programme once one neighbour starts.</p>
<p>The specification then was about four inches of concrete on graded native sand, with wire mesh that was laid on the ground rather than chaired, and control joints that were often tooled shallow or left out. Nothing about that was unusual for the period. It simply has no margin on Smyrna and Myakka fine sand, where a wet-season water table around twelve inches and roof water at the slab edge remove support from underneath.</p>""",
    eyebrow="Vintage") + sec(
    "What a BVL replacement costs, line by line",
    table(["Line", "Typical BVL two-car drive, 520 sq ft", "Note"],
          [("Remove and haul the existing slab", "$1,040 to $2,080", "One to one and a half loads"),
           ("Structural fill where the base washed out", "Quoted after the slab is up", "Usually along one edge, under the downspout line"),
           ("4 in base and new 4 in slab, 3,000 to 3,500 psi", "$4,420 to $7,020", "Fiber plus number four edge bars, joints at ten feet"),
           ("Apron section at 6 in with edge steel", "Priced separately", "County right-of-way detail"),
           ("Downspout extensions past the slab edge", "Small line, not optional", "The cause of the original failure"),
           ("Front walk, 4 ft by 40 ft, if it goes at the same time", "$1,400 to $2,100", "Cheaper in the same visit than as a return trip")],
          caption="Current Cost Index rates on the standard Landstar footprint. Your drive is measured at the site visit; this is a planning shape, not a quote."),
    cls="alt")
FAQS["/concrete/driveways/buenaventura-lakes/"] = [
    faq("Why do so many BVL driveways fail at the same time?", "Because they were poured within a few years of each other to the same specification. Same construction, same soil, same roof water, same outcome."),
    faq("Is BVL in the City of Kissimmee?", "No. Buenaventura Lakes is unincorporated Osceola County with a Kissimmee mailing address, so the county driveway permit and the twenty-four foot width cap apply."),
]

SECTIONS["/concrete/repair/buenaventura-lakes/"] = sec(
    "When one panel is worth fixing and when it is not",
    """<p>We get called to BVL for a single stepped panel at the garage more than for anything else. The honest assessment usually goes like this. Tap the other panels. If they ring solid and the cracks in them are hairline and level, replacing the one failed panel and fixing the downspout buys real years, and it costs a fraction of a replacement. If two or three panels sound hollow or show a step, the base under the whole drive is going and a panel is a deposit on a job you will do anyway.</p>
<p>The middle case is the awkward one: one bad panel, one suspicious panel, and a homeowner who is not selling for five years. There we will do the repair and say plainly that the second panel is likely inside that window, so the decision is a cash-flow choice rather than a technical one.</p>""",
    eyebrow="Judgement") + sec(
    "The repairs that are almost always worth it",
    """<p>Independent of the driveway's overall condition, three BVL repairs pay for themselves. Extending a downspout past the slab edge, which costs very little and removes the cause of most panel settlement. Routing and sealing tight cracks so water stops entering the base through them. And grinding or replacing a trip lip on a front walk, which is a liability question as much as a maintenance one, particularly on a rental.</p>
<p>The repair that is almost never worth it is a surface patch over a moving crack. Bagged mortar troweled over a crack that has a step in it fails at the bond line within a year and makes the eventual proper repair harder, because the patch has to come off first. The full repair menu with costs is on {r}.</p>""".format(r='<a href="/concrete/repair/">the repair page</a>'),
    cls="alt")
FAQS["/concrete/repair/buenaventura-lakes/"] = [
    faq("How do I know whether the rest of my driveway is about to go?", "Tap each panel. Solid ring means supported concrete; a dull thud means a void underneath. That plus a straight edge across each crack is the whole diagnosis."),
    faq("Is a surface patch ever the right fix?", "Over a tight, level crack, yes as a sealant. Over a stepped crack, no; it fails at the bond line and has to be removed before a proper repair."),
]

SECTIONS["/concrete/resurfacing/buenaventura-lakes/"] = sec(
    "The one question that decides it in BVL",
    """<p>Resurfacing a Buenaventura Lakes driveway is attractive because it costs about half of a replacement and transforms the look in two days. It is also the most common wasted spend in the neighbourhood, because the slabs are forty years old on no base and most of them are moving. An overlay is a surface treatment; it inherits every void and every step under it.</p>
<p>So the question is whether the slab is stable, and it is answered with a tap test, a string line across every crack and a hose test of where the roof and irrigation water actually go, not with a look from the kerb. A 1985 slab that passes all three is a genuinely good candidate, and there are some: the ones on lots where the downspouts happen to discharge away from the drive.</p>""",
    eyebrow="Suitability") + sec(
    "What resurfacing does and does not buy",
    table(["", "Resurfacing a sound BVL slab", "Replacing it"],
          [("Cost, 520 sq ft", "$2,600 to $4,940", "$5,460 to $9,100 including removal"),
           ("Time on site", "Two to three days", "Three days plus cure"),
           ("Life", "Ten to fifteen years with a re-seal", "Twenty-five years or more"),
           ("Fixes the base", "No", "Yes"),
           ("Fixes drainage", "No", "Yes, the slab is re-sloped"),
           ("Look", "Uniform, new texture and colour", "New concrete, lighter for a year"),
           ("If the slab moves later", "The overlay cracks with it", "Not applicable")],
          caption="Current Cost Index rates on the standard 520 square foot BVL footprint."),
    cls="alt")
FAQS["/concrete/resurfacing/buenaventura-lakes/"] = [
    faq("Can a forty-year-old driveway be resurfaced?", "Only if it is stable: no hollow panels, no steps across cracks, and water that runs away from it. Most BVL slabs of that age fail at least one of those tests."),
    faq("How long does a resurfaced driveway last?", "Ten to fifteen years on a sound slab with a re-seal every three to five years. On a moving slab, one or two seasons."),
]

SECTIONS["/pavers/driveways/buenaventura-lakes/"] = sec(
    "Why pavers make sense on a lot with a drainage history",
    """<p>Almost every Buenaventura Lakes driveway we replace failed because water moved sand out from under it. That history is the strongest argument for pavers on these lots, and it has nothing to do with appearance. When a paver field settles, the pavers do not break. The affected area is lifted, the base is rebuilt, the same units go back, and the repair is invisible. When a concrete slab settles, it cracks, and the repair is a lighter panel with a joint around it.</p>
<p>On a street where the roof drainage is what it is and the neighbours' drives are cracking one by one, that difference is worth the premium to some owners and not to others. The current spread on a 520 square foot drive is roughly $4,420 to $7,020 for concrete against $7,280 to $11,440 for concrete pavers, both before removal.</p>""",
    eyebrow="Why pavers here") + sec(
    "The base is the whole job on a 1980s lot",
    """<p>Removing a forty-year-old slab in BVL exposes native fine sand, not a base, usually with a scoured channel along the downspout line and sometimes with irrigation pipe that was trenched in after the driveway went down. All of that is dealt with before any rock is placed: pipe relocated or sleeved, soft material dug out, structural fill compacted in lifts, then six inches of limerock in two lifts with a probe check after each.</p>
<p>A paver driveway installed over that ground without the base work looks identical on handover day and settles within two wet seasons, which is why comparing quotes on square-foot price alone is a trap here. Our proposals break out removal, fill and base as separate lines, and the {pb} generates a specification you can give to every bidder so the comparison is real.</p>""".format(pb='<a href="/tools/project-brief/">project brief tool</a>'),
    cls="alt")
FAQS["/pavers/driveways/buenaventura-lakes/"] = [
    faq("Are pavers worth the extra cost in BVL?", "On a lot where the old slab failed from water moving the sand under it, the repairability of pavers is a real advantage. On a well-drained lot it is a preference rather than a technical argument."),
    faq("Can pavers be laid over the existing concrete?", "We do not recommend it on a forty-year-old BVL slab. The slab is the problem; leaving it in place leaves the problem in place."),
]
