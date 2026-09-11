# -*- coding: utf-8 -*-
"""Extra depth for the service pages. One block per service, written for that service."""
from _helpers import sec, table, faq

SECTIONS = {}
FAQS = {}

# --------------------------------------------------------------- CONCRETE
SECTIONS["/concrete/patios/"] = sec(
    "Sizing a patio to the furniture, not to the yard",
    table(["Use", "Working size", "Why"],
          [("Bistro set, two chairs", "8 by 8 ft", "A chair needs about three feet to push back from the table"),
           ("Four-seat dining table", "12 by 12 ft", "Table plus pull-back on all four sides"),
           ("Six-seat dining table", "12 by 16 ft", "The long sides are what run short"),
           ("Dining plus a seating group", "16 by 20 ft", "Two zones need a circulation path between them"),
           ("Grill station alone", "6 by 8 ft", "Plus clearance from the house and any screen"),
           ("Fire pit with chairs around it", "16 ft circle or 16 by 16 ft", "Seven feet clear around the pit is the comfortable minimum")],
          caption="Sizes we lay out with paint on the site visit before anything is quoted. Almost every patio we are asked to extend later was built to the yard rather than to the furniture."),
    eyebrow="Layout") + sec(
    "The details that decide how a patio ages",
    """<p>Four things separate a patio that still looks intentional at year ten from one that does not, and none of them is the concrete itself. The first is the edge. A formed edge with a tooled radius holds up; an edge poured against sod crumbles within a few seasons and cannot be repaired neatly. The second is the joint layout. Joints on the centrelines of a square patio read as a design; joints placed wherever the crew happened to stop read as cracks that were planned badly.</p>
<p>The third is the transition to the house. A slab that meets the stem wall without an expansion joint pushes against it as it moves, and on a Florida block house that shows up as a hairline crack in the stucco above. The fourth is the fall. A quarter inch per foot away from the house feels level underfoot and moves water decisively; an eighth is the minimum and anything less ponds after the first storm. All four cost almost nothing at pour time and cannot be added afterwards.</p>""",
    cls="alt")
FAQS["/concrete/patios/"] = [faq("What size patio do I actually need?", "Size it to the furniture, not the yard. A four-seat dining table wants about 12 by 12 feet once chairs pull back; a fire pit with seating wants about 16 feet across.")]

SECTIONS["/concrete/pool-decks/"] = sec(
    "Deck width, traffic and the things people trip on",
    """<p>A pool deck has to do three jobs at once: give people somewhere to stand while getting in and out, let two people pass behind a lounger, and get water away from the pool. Three feet of deck on the long sides is the bare minimum for the first, four to five feet is comfortable, and eight to twelve feet on one side is what makes a deck usable for furniture rather than circulation. Where an existing deck is three feet all the way round, widening one side is usually a better spend than resurfacing all of it.</p>
<p>The trip hazards on a Florida deck are predictable: the step down from the lanai slab to the deck, the lip where a previous overlay ended, the screen enclosure track, the drain grate that sits proud, and the coping edge where the deck has settled away from the pool. We measure each of those on the inspection, because a deck project that does not resolve them is a cosmetic project.</p>""",
    eyebrow="Dimensions") + sec(
    "Cool decking, textures and what they are made of",
    table(["Finish", "What it is", "Grip when wet", "Renewal", "Notes"],
          [("Broom finish concrete", "The concrete surface itself, brushed", "Good", "None, or a penetrating sealer", "Cheapest, and perfectly serviceable"),
           ("Knock-down texture", "A cementitious or acrylic overlay, sprayed then flattened", "Very good", "Re-coat every 5 to 8 years", "The classic Florida pool deck look"),
           ("Spray texture", "Same family, sprayed and left", "Excellent", "Re-coat every 5 to 8 years", "More aggressive underfoot; some find it rough"),
           ("Exposed aggregate", "Surface washed to expose the stone", "Very good", "Sealer optional", "Hard to repair invisibly"),
           ("Smooth trowel", "Steel-troweled surface", "Poor when wet", "Sealer", "Not for an open deck; acceptable under a roof"),
           ("Stamped", "Pattern pressed into the fresh slab", "Depends on sealer and grit", "Re-seal every 2 to 3 years", "Needs an anti-slip additive around a pool")],
          caption="What we install and what each one costs to keep up. Colour, not finish, is what determines how hot the deck gets."),
    cls="alt")
FAQS["/concrete/pool-decks/"] = [faq("How wide should a pool deck be?", "Three feet is the minimum to stand on, four to five is comfortable, and eight to twelve on one side is what makes a deck usable for furniture. Widening one side often beats resurfacing everything.")]

SECTIONS["/concrete/stamped/"] = sec(
    "Patterns we install, and where each one suits",
    table(["Pattern", "Look", "Suits", "Watch out for"],
          [("Ashlar slate", "Rectangular stone in a repeating layout", "Patios, pool decks, large areas", "The repeat becomes visible on very large fields"),
           ("Random stone", "Irregular flagstone", "Curved patios, garden paths", "Harder to align around a fixed edge"),
           ("Wood plank", "Board texture with grain", "Contemporary patios, lanai floors", "Grain direction has to be planned; joints show"),
           ("European fan / cobble", "Small radial units", "Driveway borders, entry courts", "Slow to stamp; higher labour"),
           ("Herringbone brick", "Brick in a running herringbone", "Walkways, aprons", "Reads as brick, so colour choice matters"),
           ("Texture skin", "Stone texture with no joint lines", "Pool decks where a pattern would compete", "Colour variation carries the whole look")],
          caption="Pattern choice is a labour decision as much as a design one. The small-unit patterns take longer to stamp before the slab sets, which matters in a Kissimmee summer."),
    eyebrow="Patterns") + sec(
    "The maintenance commitment nobody mentions at the quote",
    """<p>Stamped concrete is the one flatwork finish that has a standing maintenance obligation, and it is fair to know that before choosing it. In full Central Florida sun a solvent-based acrylic sealer holds its look for two to three years; under a lanai roof, three to five. When it goes, it does not fail gracefully. It wears through in traffic lanes first, so the driveway develops a dull stripe where the tyres run and the patio dulls where the chairs move.</p>
<p>Recoating is straightforward for the first two or three cycles. After that the acrylic has built up and the honest answer is to strip and start again, which costs roughly what the original sealing did. Budgeting for a recoat every two to three years and a strip-and-reseal every ten or so is what stamped work actually costs to own, and it is why we recommend it enthusiastically for covered areas and cautiously for an open driveway.</p>""",
    cls="alt")
FAQS["/concrete/stamped/"] = [faq("How much maintenance does stamped concrete need?", "A re-seal every two to three years in full sun, three to five under a roof, and a strip-and-reseal roughly every decade once the acrylic has built up. That is the real cost of owning it.")]

SECTIONS["/concrete/slabs/"] = sec(
    "How much concrete a pad actually takes",
    table(["Pad", "Size", "Thickness", "Cubic yards", "Ready-mix cost at $175 to $280/yd"],
          [("AC or generator pad", "4 by 8 ft", "4 in", "0.4", "$70 to $112, subject to a short-load fee"),
           ("Shed pad", "10 by 12 ft", "4 in", "1.5", "$263 to $420"),
           ("Hot tub pad", "8 by 10 ft", "5 in", "1.3", "$228 to $364"),
           ("Boat pad", "10 by 30 ft", "6 in", "5.6", "$980 to $1,568"),
           ("RV pad", "12 by 40 ft", "6 in", "8.9", "$1,558 to $2,492"),
           ("Workshop slab", "30 by 40 ft", "6 in", "22.2", "$3,885 to $6,216")],
          caption="Material only, before base, forming, steel, labour, permit and haul-off. Small pours also carry a short-load fee. The installed ranges are in the Cost Index."),
    eyebrow="Volumes") + sec(
    "What sits on the pad decides what goes in it",
    """<p>The load on a pad is almost never spread evenly, and that is what people get wrong when they size one. A travel trailer puts most of its weight on four jack feet, each one a few square inches. A hot tub full of water and eight people is around six thousand pounds on a footprint that is mostly empty in the middle. A metal building puts its whole load into the anchor bolts at the column lines. A generator concentrates its weight on a frame that is narrower than the pad.</p>
<p>So we ask what is going on it, and then we design for that: a grid rather than fibre alone under point loads, five inches rather than four under a spa, a thickened edge where a building's columns land, and six inches with a grid under anything on jack feet. The pad that fails is almost always the one that was sized by area and thickness without anyone asking what would stand on it.</p>""",
    cls="alt")
FAQS["/concrete/slabs/"] = [faq("How many cubic yards is a 12 by 40 RV pad?", "About 8.9 yards at six inches. At current Orlando-market ready-mix prices that is roughly $1,560 to $2,490 in material before base, steel, forming and labour.")]

SECTIONS["/concrete/sidewalks-walkways/"] = sec(
    "Width, route and the things that make a walk feel right",
    """<p>Three feet is a path. Four feet is a walkway two people can use. Five feet is what a public sidewalk detail usually calls for. Those numbers matter more than they sound, because a three-foot front walk on a house with a wide façade looks like an afterthought, and a five-foot walk on a small bungalow looks like a runway. We mark the outline in paint and look at it from the street before anything is priced.</p>
<p>Route matters as much as width. A walk that runs straight from the driveway to the door is efficient and often ugly; one that curves for no reason is worse. The rule that works is to follow the line people already walk, which is usually visible as a worn track in the grass, and to widen slightly at the door so there is somewhere to stand while it opens. Steps get a consistent rise; a flight where one riser differs by more than about a quarter inch is a trip hazard and it is always the odd one that catches people.</p>""",
    eyebrow="Design") + sec(
    "Where walkways fail, and the fix at pour time",
    table(["Failure", "Cause", "Prevented by"],
          [("Crumbled edges", "Formed against sod, or forms pulled too early", "A proper form, a tooled radius, forms left overnight"),
           ("Panels lifted at a tree", "Roots crossing the route", "Routing around the canopy, or a root barrier at pour time"),
           ("Water running along the walk", "No cross-fall", "An eighth to a quarter inch per foot of cross-slope"),
           ("Cracks between joints", "Joints spaced too far for a narrow slab", "Joints every four to five feet on a four-foot walk"),
           ("A lip at the driveway", "No expansion joint at the junction", "A half-inch expansion joint at every junction"),
           ("Settlement at the downspout", "Roof water under the slab", "Downspout carried past the walk")],
          caption="All six are decided before the concrete arrives. None of them can be corrected afterwards without replacing the affected panels."),
    cls="alt")
FAQS["/concrete/sidewalks-walkways/"] = [faq("How wide should a front walk be?", "Four feet lets two people walk together and suits most houses. Three feet reads as a path; five is usually only for a public sidewalk detail or a very wide façade.")]

SECTIONS["/concrete/repair/"] = sec(
    "What we bring to a repair inspection, and what you get",
    """<p>A repair visit is a diagnosis, not a measurement. We bring a crack comparator card to measure width, a straight edge to find vertical offset, something to tap with to find voids, and a hose to see where water actually goes. Twenty minutes produces a marked-up sketch of the slab with every crack, every hollow panel and the drainage route on it.</p>
<p>What you get is that sketch, the cause we think is behind each defect, and two or three priced options rather than one number. On a driveway that means typically: seal the cosmetic cracks and do nothing else; replace the one failed panel and fix the water; or replace the driveway. Which one is right depends on how long you intend to be in the house, and that is your information, not ours, so we give you the numbers and stay out of the decision.</p>""",
    eyebrow="Inspection") + sec(
    "Repairs we decline, and why",
    """<p>There are three jobs we turn down regularly. Patching over a crack that has a vertical step, because the patch will fail at the bond line inside a year and make the eventual repair harder. Resurfacing a slab that sounds hollow, for the same reason at ten times the price. And injecting foam under a slab while the downspout that emptied the sand out from under it is still pointed at the edge, because the void will simply re-form.</p>
<p>In each case there is a version of the job we will do: route and seal the crack and monitor it, replace the failed panel, or fix the drainage first and then lift. Saying so costs us work occasionally. It costs less than being the second contractor a homeowner has paid to fix the same thing.</p>""",
    cls="alt")
FAQS["/concrete/repair/"] = [faq("Do you charge for a repair inspection?", "No. An estimate visit is free and produces a marked-up sketch of the slab with the causes and two or three priced options.")]

SECTIONS["/concrete/resurfacing/"] = sec(
    "Which overlay system goes on which surface",
    table(["System", "Thickness", "Best on", "Finish options", "Life here"],
          [("Polymer-modified microtopping", "1/16 to 1/8 in", "Sound slabs with a good profile", "Smooth, trowelled, coloured", "8 to 12 years"),
           ("Spray or knock-down texture", "1/8 in", "Pool decks, patios, walkways", "Textured, coloured", "5 to 8 years before re-coat"),
           ("Stamped overlay", "1/4 to 1/2 in", "Patios and entries where a pattern is wanted", "Stamped patterns, integral plus release colour", "10 to 15 years with re-sealing"),
           ("Broom-finish resurfacer", "1/4 in", "Driveways", "Broom", "10 to 15 years"),
           ("Self-levelling underlayment", "1/4 in and up", "Interior or covered slabs out of level", "Smooth", "Indefinite under a covering")],
          caption="Chosen by what the slab is doing and where it is, not by preference. All of them require a sound, profiled, dry substrate."),
    eyebrow="Systems") + sec(
    "Surface preparation is most of the job",
    """<p>An overlay is a bond, and a bond is only as good as what it is bonded to. So the preparation is where the time goes: pressure washing at around three and a half thousand psi to remove everything loose, grinding or acid-etching to open the surface profile, routing and filling cracks with a flexible sealant so they do not telegraph immediately, grinding spalled areas back to sound concrete, and treating stains chemically rather than covering them, because oil and rust will bleed through an overlay.</p>
<p>Then it has to be dry. An overlay placed on a damp slab, or a slab that is still releasing moisture from below because it has no vapour barrier, fails in sheets. On a shaded deck in the rainy season that can mean waiting two or three days after the washing before anything is placed, which is a scheduling reality rather than a delay.</p>""",
    cls="alt")
FAQS["/concrete/resurfacing/"] = [faq("How long does an overlay last?", "Eight to fifteen years depending on the system, on a sound slab, with a re-seal or a re-coat on the interval for that product. On a moving slab, one or two seasons.")]

SECTIONS["/concrete/architectural/"] = sec(
    "Why a sample panel comes first",
    """<p>Architectural concrete is judged on appearance, and appearance in concrete is the product of a dozen variables that do not appear on a price list: the aggregate in the local mix, the pigment dose, the cement colour, the form material, the release agent, the finishing sequence, the weather on the day and the sealer. Two crews working from the same specification produce visibly different results, which is why every architectural job we take starts with a sample panel of about two feet square, poured on site with the actual mix, cured the way the real pour will be cured, and approved by you before we form anything.</p>
<p>The panel also settles expectations about variation. Concrete is not a manufactured tile; a board-formed wall will show the boards' character and an integrally coloured slab will vary slightly between loads. Seeing that on a sample makes it a feature; seeing it for the first time on a finished lanai makes it a complaint.</p>""",
    eyebrow="Process") + sec(
    "What architectural work costs relative to standard flatwork",
    table(["Finish", "Relative to a standard broom slab", "Why"],
          [("Integral colour only", "1.2 to 1.4 times", "Pigment plus a single-load pour discipline"),
           ("Exposed aggregate", "1.3 to 1.6 times", "Seeding, washing, and the timing window"),
           ("Saw-cut panel grid", "1.2 to 1.3 times", "Layout and cutting labour"),
           ("Honed or polished", "2 to 3 times", "Multiple grinding passes, densifier, sealer"),
           ("Board-formed wall", "2.5 to 4 times", "Form construction is most of the cost"),
           ("Cast concrete counter", "Priced per piece", "Formwork, reinforcement, grinding, food-safe sealing")],
          caption="Multipliers we use for early budgeting. Every architectural job is quoted from drawings and an approved sample rather than from a rate."),
    cls="alt")
FAQS["/concrete/architectural/"] = [faq("Why does architectural concrete cost two to three times a normal slab?", "Because the labour is in the finishing rather than the placing: grinding passes on a honed floor, form construction on a board-formed wall, and a sample panel and mix discipline on everything.")]

SECTIONS["/concrete/commercial/"] = sec(
    "What a commercial job needs that a residential one does not",
    table(["Requirement", "What it means on site"],
          [("Engineered drawings", "Thickness, mix, steel and jointing come from the engineer, not from our standard"),
           ("Compaction testing", "An independent lab tests the base to a specified density before we place"),
           ("Concrete testing", "Cylinders taken at the truck and broken at 7 and 28 days"),
           ("Traffic control", "Cones, signage and sometimes a flagger to keep a centre operating"),
           ("Night or weekend work", "Priced in, because the business cannot close"),
           ("ADA compliance", "Ramp slopes, landings, cross-slopes and detectable warnings to the standard"),
           ("Insurance and prequalification", "Certificates naming the owner and the manager, sometimes a payment bond"),
           ("Phasing", "Half the drive lane at a time so access is never lost")],
          caption="These are the items that separate a commercial quote from a residential one, and the reason the same square footage prices differently."),
    eyebrow="Requirements") + sec(
    "The commercial work that suits a flatwork crew",
    """<p>We are a flatwork crew with a residential base, and the commercial jobs where that is an advantage are the small, access-constrained ones that a large site contractor prices high because mobilising for them is inefficient. A dumpster pad behind a restaurant on US-192. A church walkway and ramp in St. Cloud. The amenity-centre pool deck and walkways at a vacation-rental community. Twenty parking spaces at an HOA clubhouse in Poinciana. Drive-lane panel replacement at a shopping centre, done overnight.</p>
<p>What we do not take on is anything requiring a general contractor of record, site drainage design, structural slabs, or large parking lots with subgrade and paving scopes. Saying that early is more useful to a property manager than a quote that quietly leaves out the engineering.</p>""",
    cls="alt")
FAQS["/concrete/commercial/"] = [faq("Do you work nights and weekends on occupied properties?", "Yes, and it is priced into the quote. Phasing so that access is never fully lost is usually part of the same conversation.")]

# ----------------------------------------------------------------- PAVERS
SECTIONS["/pavers/driveways/"] = sec(
    "Patterns, borders and the waste factor nobody explains",
    table(["Pattern", "Look", "Cutting", "Waste factor", "Suits"],
          [("Running bond", "Simple, linear", "Low", "About 5 percent", "Long straight drives, contemporary homes"),
           ("Herringbone 45 degrees", "Strongest interlock under turning loads", "High at every edge", "8 to 12 percent", "Driveways; the default for vehicle areas"),
           ("Herringbone 90 degrees", "Strong, more formal", "Moderate", "6 to 10 percent", "Driveways and aprons"),
           ("Random ashlar", "Mixed sizes, natural stone look", "Moderate", "6 to 10 percent", "Wide drives, courtyards"),
           ("Basketweave", "Traditional, busy at scale", "Low", "About 5 percent", "Small areas, borders"),
           ("Circle kit with a field", "Formal focal point", "Very high", "12 to 18 percent", "Entry courts and turnarounds")],
          caption="Waste factor is real material you pay for and is the reason two quotes for the same driveway in different patterns are not comparable on a per-square-foot basis."),
    eyebrow="Pattern") + sec(
    "Why a herringbone is the default in a vehicle area",
    """<p>Interlock is what makes a paver field behave as a surface rather than a collection of blocks, and it comes from three things: the pattern, the joint sand and the edge restraint. Of the three, pattern is the one chosen at design time and then never revisited. A forty-five degree herringbone resists the horizontal forces that a turning tyre applies better than a running bond, because no continuous joint line runs in the direction of the force. That is why it is the standard for driveways and why we steer people toward it in the parking and turning areas even when the field elsewhere is something else.</p>
<p>The cost of that choice is cutting. Every paver at the perimeter of a herringbone field is a diagonal cut, which is slower and produces more waste than the square cuts a running bond needs. A border course absorbs some of it and gives the field a clean edge, which is why almost every driveway we build has one.</p>""",
    cls="alt")
FAQS["/pavers/driveways/"] = [faq("Which paver pattern is best for a driveway?", "A forty-five degree herringbone, because no continuous joint runs in the direction a turning tyre pushes. It costs more in cutting and waste, which is why quotes in different patterns are not directly comparable.")]

SECTIONS["/pavers/patios/"] = sec(
    "Building a patio that can grow",
    """<p>Most paver patios we are asked to extend were built to a budget that ended at the edge of the first phase, and extending them later is harder than it looks: the paver line may be discontinued, the colour of a five-year-old field has softened, and the base under the new area has to tie into the old without a differential settlement line at the joint. None of that is fatal, but all of it costs more than building the larger patio at once.</p>
<p>So when a patio is likely to grow, we do two things at the first phase. We buy and store a small surplus of the field paver, enough to blend a future edge or repair a damaged area. And we set the base and the edge restraint at the planned future line rather than the current one where the budget allows, so the extension is a paving job rather than an excavation job. Both are cheap now and expensive later.</p>""",
    eyebrow="Planning") + sec(
    "Fire pits, kitchens and the loads they add",
    table(["Feature", "What it weighs", "What the base needs"],
          [("Portable fire bowl", "Under 100 lb", "Standard patio base; a non-combustible surface under it"),
           ("Built masonry fire pit", "1,500 to 3,000 lb", "A concrete footing below the paver base, not pavers alone"),
           ("Seat wall, 20 linear ft", "3,000 lb and up", "A continuous concrete footing"),
           ("Outdoor kitchen with counters", "2,000 to 5,000 lb", "A footing or a thickened slab under the run, plus conduit and gas sleeves placed first"),
           ("Pergola on posts", "Light, but concentrated and wind-loaded", "Footings sized for uplift at each post"),
           ("Hot tub", "About 6,000 lb filled", "A five inch reinforced concrete pad, not a paver field")],
          caption="Anything built or heavy sits on a footing that goes in before the pavers. Retrofitting a footing under an existing field means lifting it."),
    cls="alt")
FAQS["/pavers/patios/"] = [faq("Can a hot tub sit on a paver patio?", "Not on the paver field alone. A filled spa is around six thousand pounds and wants a five inch reinforced concrete pad, which we pour as part of the patio and finish around.")]

SECTIONS["/pavers/pool-decks/"] = sec(
    "Coping, drainage and the two details that decide everything",
    """<p>A paver pool deck is judged at two lines: where it meets the pool and where the water goes. The coping is the bullnose course at the pool edge, and it does three jobs, capping the bond beam, giving a comfortable edge to hold, and creating a clean stop for the deck field. It has to be bonded, level and separated from the deck by a flexible joint so the deck can move slightly without pushing on the pool structure. Coping that has been mortared solid to both the beam and the deck is coping that will crack.</p>
<p>Drainage is the other. Inside a screen enclosure the roof concentrates water at the screen line, so a channel drain there is normal rather than an upgrade. On an open deck the fall has to take water away from the pool and away from the house, to somewhere that can accept it. A deck that drains into the pool puts sunscreen, leaf litter and fertiliser in the water; a deck that drains to the house is a stem-wall problem waiting to happen.</p>""",
    eyebrow="Key details") + sec(
    "What each deck option costs on a 600 square foot deck",
    table(["Option", "Rate per sq ft", "600 sq ft", "Notes"],
          [("Clean, re-sand and seal an existing paver deck", "$1.75 to $3.25", "$1,050 to $1,950", "Maintenance, not a change"),
           ("Textured overlay on sound concrete", "$5.00 to $9.50", "$3,000 to $5,700", "Renews the surface only"),
           ("Thin paver overlay on sound concrete", "$15.00 to $24.00", "$9,000 to $14,400", "Adds about an inch"),
           ("Travertine over sound concrete", "$20.00 to $36.00", "$12,000 to $21,600", "Coolest surface; penetrating sealer"),
           ("Full paver rebuild with new base", "Priced per site", "Higher than an overlay", "Fixes elevation and drainage"),
           ("Remove existing deck", "$2.00 to $4.00", "$1,200 to $2,400", "Hand work near the shell costs more")],
          caption="Current Cost Index rates on a deck around a typical 14 by 28 pool. Coping and drain work are itemised separately."),
    cls="alt")
FAQS["/pavers/pool-decks/"] = [faq("Should the coping be replaced with the deck?", "Usually yes if it is being disturbed. Coping has to be bonded, level and separated from the deck by a flexible joint; reusing coping that was mortared solid to both sides just rebuilds the original problem.")]

SECTIONS["/pavers/travertine/"] = sec(
    "Grades, finishes and what the words on the quote mean",
    table(["Term", "What it means", "Why it matters here"],
          [("Tumbled", "Edges and surface softened in a tumbler", "Best wet grip; the standard for pool decks"),
           ("Brushed or honed", "Machine-smoothed surface", "Smoother underfoot; more slippery when wet"),
           ("Filled", "Natural voids filled with resin or cement", "Smoother, but fills can pop out and need repair"),
           ("Unfilled", "Voids left open", "More texture and grip; holds more dirt"),
           ("Premium or first grade", "Fewer voids, tighter colour range", "Costs more; looks more uniform"),
           ("Standard or commercial grade", "More voids and colour variation", "Cheaper; reads as more natural, or as inconsistent"),
           ("French pattern", "A repeating set of four sizes", "The common pool-deck layout; needs a planned start point"),
           ("3 cm paver vs 1.2 cm tile", "Thickness", "The thick unit is sand-set; the thin one is thin-set on concrete")],
          caption="The same word means different things at different suppliers, so we put the grade, finish and thickness in the proposal rather than just the word travertine."),
    eyebrow="Specification") + sec(
    "Living with a stone deck in Central Florida",
    """<p>Travertine is a calcium carbonate stone, which explains most of what it needs. Acids etch it, so the acidic cleaners sold for concrete driveways are off the list permanently, muriatic acid above all. Pool water chemistry that drifts acidic will dull the coping over years, which is an argument for keeping the water balanced that has nothing to do with the pool surface. And it is porous, so sunscreen, oils and drinks soak in rather than sitting on top, which makes a penetrating sealer a practical necessity rather than a nicety.</p>
<p>What it gives back is the surface temperature, which every published comparison puts well below grey concrete at midday, and a wet grip in the tumbled finish that is genuinely good. On a deck that children run on in July, those two things are the whole argument, and they are why we keep recommending it in this market despite the price.</p>""",
    cls="alt")
FAQS["/pavers/travertine/"] = [faq("What is French pattern travertine?", "A repeating layout of four different sizes that reads as natural stonework. It needs a planned start point so the repeat lands sensibly against the pool and the house.")]

SECTIONS["/pavers/marble-porcelain/"] = sec(
    "Where each material earns its cost",
    table(["Material", "Typical thickness", "Installation", "Strengths", "Limits"],
          [("Marble pavers", "1¼ in (3 cm)", "Sand-set or thin-set", "The lightest, coolest common deck surface", "Acid-sensitive; shows etching readily"),
           ("Large-format porcelain", "¾ in (2 cm)", "Thin-set, pedestals, or a gravel set", "Stain-proof, frost-proof, dimensionally perfect", "Needs a rigid, flat substrate; cutting needs the right blade"),
           ("Porcelain plank", "¾ in", "Thin-set", "Wood look with none of the maintenance", "Long thin units show any base irregularity"),
           ("Shell-stone / coral", "1¼ in", "Sand-set", "Distinctive texture, cool underfoot", "Softer; chips at edges"),
           ("Bluestone", "1 to 1½ in", "Sand-set or thin-set", "Dense, dark, formal", "Dark colour means a hot surface")],
          caption="What we install and what each one demands from the base. The substrate requirement, not the material price, is usually what decides these jobs."),
    eyebrow="Materials") + sec(
    "Large format is a base problem, not a paving problem",
    """<p>A 24 by 24 inch porcelain paver is unforgiving in a way a 6 by 9 inch concrete paver is not. A small unit bedded in sand accommodates a base that is a few millimetres out because each unit finds its own level and the joint absorbs the difference. A large rigid unit spans the irregularity and either rocks or, on a thin-set installation, cracks. The larger the unit, the flatter the substrate has to be.</p>
<p>That is why large-format work costs more even when the material is comparable: the base is screeded to a tighter tolerance, thin-set installations need a properly flat and sound slab, and pedestal systems need each pedestal adjusted. It is also why we will decline to thin-set large-format porcelain over a slab that fails a tap test, because the failure mode there is cracked tile rather than a settled paver.</p>""",
    cls="alt")
FAQS["/pavers/marble-porcelain/"] = [faq("Can large-format porcelain go over my existing deck?", "Only over a slab that is sound and flat. Large rigid units span irregularities instead of absorbing them, so the substrate tolerance is much tighter than for small sand-set pavers.")]

SECTIONS["/pavers/walkways-steps/"] = sec(
    "Step geometry is a safety item, not a style choice",
    """<p>The single most common defect we find in existing paver steps is inconsistent riser height. A flight where the risers vary by half an inch is a flight people trip on, and they trip on the odd one, because the body learns the rhythm from the first two steps. Consistency matters more than the actual dimension.</p>
<p>What we build to: a riser between six and seven and a half inches, a tread depth of at least eleven inches and preferably twelve to fourteen on an entry flight, every riser in a flight within about a quarter inch of the others, and a landing at the door at least as deep as the door is wide. Where an existing concrete flight has bad geometry, capping it in pavers preserves the bad geometry, so on those we rebuild rather than cap and we say why.</p>""",
    eyebrow="Geometry") + sec(
    "How a paver step is actually built",
    """<p>A paver step is not a stack of pavers. Underneath is a structural core, either poured concrete or a compacted base with a solid bearing under each nosing, because the tread edge is where the load lands and an unsupported nosing works loose within a season. The riser face is bonded rather than sand-set, so it cannot be pushed out by water or foot pressure. Behind the risers, drainage takes water away rather than letting it collect and push.</p>
<p>Lighting is worth deciding at this stage rather than later. Riser lights and recessed step lights need conduit run before the core is built, and retrofitting them afterwards means cutting into finished work. On an entry flight it is a small addition at build time and a significant one later, which is why our step proposals always ask the question.</p>""",
    cls="alt")
FAQS["/pavers/walkways-steps/"] = [faq("Can my existing concrete steps be capped with pavers?", "If the geometry is good, yes. Capping preserves whatever rise and run are already there, so a flight with inconsistent risers should be rebuilt rather than capped.")]

SECTIONS["/pavers/sealing/"] = sec(
    "A maintenance calendar for a paver surface in this climate",
    table(["Interval", "Driveway", "Pool deck", "Walkway"],
          [("At 60 to 90 days", "First clean, re-sand and seal", "First clean, re-sand and seal", "First clean, re-sand and seal"),
           ("Annually", "Rinse; spot-treat oil", "Rinse; spot-treat sunscreen and organics", "Rinse"),
           ("Every 2 to 3 years", "Check joints; top up", "Re-sand and re-seal if in full sun", "Check joints"),
           ("Every 3 to 4 years", "Clean, re-sand, re-seal", "Re-sand and re-seal if screened", "Clean, re-sand, re-seal"),
           ("Every 8 to 12 years", "Consider a strip and reseal", "Consider a strip and reseal", "Consider a strip and reseal"),
           ("As needed", "Lift and relay any settled area before sealing", "Same", "Same")],
          caption="Our schedule for Central Florida sun and about 52 inches of rain a year. The trigger to move early is water no longer beading or joint sand loosening at the edges."),
    eyebrow="Calendar") + sec(
    "What the visit actually involves",
    """<p>A sealing visit is mostly cleaning and sanding. We start with a survey for settled areas, because sealing a field that needs lifting glues the problem in place. Then organic growth and staining are treated chemically and by type, iron staining with a stone-safe or concrete-appropriate rust remover, tannin with a percarbonate cleaner, oil with a degreaser and a poultice. Washing is done with a surface cleaner at moderate pressure rather than a turbo nozzle, because the object is to clean the paver without excavating the joint.</p>
<p>Then the joints are cleaned to depth, the field is dried, polymeric sand goes in dry, is vibrated down with a plate compactor on a protective pad, topped up and blown completely clean. Water goes on in stages per the product instructions. The sealer follows only once the sand has cured, which on a large field usually means a return visit rather than the same afternoon.</p>""",
    cls="alt")
FAQS["/pavers/sealing/"] = [faq("Can the sealing be done the same day as the sanding?", "Usually not on a large field. The polymeric sand has to cure first, so sealing is often a return visit a day or more later.")]

SECTIONS["/pavers/repair/"] = sec(
    "Diagnosing a settled paver field",
    table(["What you see", "Usual cause", "Repair"],
          [("A dish near a downspout", "Base washed out by roof water", "Fix the downspout, lift, rebuild the base, relay"),
           ("The outside course rolled outward", "Edge restraint failed or was never installed", "Reset the edge with a concrete restraint, relay the affected courses"),
           ("A ridge across the field", "Tree root under the base", "Root barrier, base rebuild, relay; arborist for significant roots"),
           ("Rocking units in one area", "Bedding sand washed out through an open joint", "Re-sand the field, lift and re-bed the rocking area"),
           ("Ant mounds between units", "Loose or missing joint sand", "Clean joints to depth, polymeric sand, seal"),
           ("A sunken strip across the drive", "Utility trench backfill consolidating", "Lift, compact properly, relay"),
           ("Chipped or spalled faces", "Snow-plough style edge damage, or a failing unit", "Replace individual units from stock or a blended source")],
          caption="Almost every one of these is repairable without replacing the field, which is the practical advantage pavers have over a slab."),
    eyebrow="Diagnosis") + sec(
    "Matching a discontinued paver",
    """<p>The hardest part of a paver repair is often not the base work. It is finding units that match a field installed fifteen years ago in a line the manufacturer no longer makes. There are four routes and we work through them in order. Reuse: lift units from a low-visibility area, such as behind a gate or under where a planter sits, and use them for the repair, then fill the donor area with the closest current product. Blend: mix a current product through the repair area and a short way into the surrounding field so there is no hard line. Source: check regional suppliers for old stock, which occasionally exists. Or re-lay the whole field with a new product if the repair area is large enough that no blend will convince.</p>
<p>Colour is the other half. A fifteen-year-old field has weathered, so even the identical current product will not match it. Placing new units in a scattered blend rather than as a solid patch is what makes the repair disappear, and it is worth the extra labour every time.</p>""",
    cls="alt")
FAQS["/pavers/repair/"] = [faq("My paver line is discontinued. Can it still be repaired?", "Usually, by lifting units from a hidden area for the visible repair and blending a current product into the donor area, or by scattering new units through the repair rather than laying them as a solid patch.")]

SECTIONS["/pavers/retaining-walls-outdoor-living/"] = sec(
    "What we build and where the line is",
    """<p>We build decorative segmental walls, seat walls, planters, raised terraces, fire pits, grill surrounds and outdoor kitchen structures in block and paver systems. Those are landscape elements: they hold a modest grade change or they hold themselves up, and they are built with the manufacturer's system, a compacted base, a drainage layer behind the face and geogrid where the system calls for it.</p>
<p>What we do not build is a structural retaining wall, meaning one that holds a significant grade change, carries a surcharge from a driveway or a structure above it, or exceeds the height at which the jurisdiction requires engineering. Those need a design from an engineer and a licensed contractor, and we will say so and step aside rather than build to a rule of thumb. The distinction matters because a wall that fails is not a cosmetic problem.</p>""",
    eyebrow="Scope") + sec(
    "Details that make the difference on a wall that lasts",
    table(["Detail", "Why it matters"],
          [("A compacted, level base course below grade", "Every course above inherits the first one's accuracy"),
           ("Free-draining backfill behind the face", "Water pressure behind a wall is what pushes it out"),
           ("A drain pipe at the base, daylighted", "The water has to leave, not just collect"),
           ("Geogrid at the courses the system specifies", "It ties the wall into the soil mass behind it"),
           ("Capping bonded with the correct adhesive", "Caps are what people sit on and what comes loose first"),
           ("A separation from adjacent flatwork", "So slab movement does not load the wall"),
           ("Conduit run before backfilling", "Lighting and outlets cannot be retrofitted into a finished wall")],
          caption="Most failed decorative walls we are asked to rebuild failed on drainage, not on the blocks."),
    cls="alt")
FAQS["/pavers/retaining-walls-outdoor-living/"] = [faq("Is there a height where a wall needs an engineer?", "Yes, and it varies by jurisdiction and by whether anything is loading the wall from above. We check for the address, and where engineering is required we step aside rather than build to a rule of thumb.")]

SECTIONS["/pavers/artificial-turf/"] = sec(
    "Where turf works alongside hardscape, and where it does not",
    """<p>Artificial turf earns its place in specific situations rather than as a lawn replacement everywhere. It works in the strips between driveway ribbons, where grass never survives the shade and the tyres. It works in narrow side yards that get no sun and stay muddy. It works in a pet run, in a small courtyard where a mower cannot reach, and as a putting surface. It works under a screen enclosure where grass simply will not grow.</p>
<p>It works less well as a large open lawn on a Florida lot, for two reasons that are worth saying plainly. Surface temperature on turf in full July sun is high, higher than most hardscape surfaces, which surprises people who chose it for children. And it is a drainage decision: turf over a compacted base changes how that part of the lot handles a storm, which on a flat lot with a designed drainage path is not a neutral change.</p>""",
    eyebrow="Suitability") + sec(
    "What goes under it",
    """<p>The installation that lasts is mostly base. Existing sod and organics are stripped, three to four inches of compacted crushed base goes down and is screeded to the finished contour, a weed barrier is placed where the situation calls for it, and the turf is stretched, seamed and secured at the edges with nails or a bonded edge against the hardscape. Infill is then brushed in, which keeps the blades upright and weights the sheet.</p>
<p>For pet areas the specification changes: a more open base for drainage, an infill chosen for odour control rather than appearance, and a deodorising rinse schedule that the owner has to actually follow. Turf installed over a base that does not drain becomes an odour problem within a season, and no amount of infill fixes it afterwards.</p>""",
    cls="alt")
FAQS["/pavers/artificial-turf/"] = [faq("Does artificial turf get hot?", "Yes, and in full July sun it runs hotter than most light hardscape surfaces. It suits shaded side yards, driveway ribbons and pet runs better than a large open lawn where children play barefoot.")]

SECTIONS["/pavers/outdoor-lighting/"] = sec(
    "Lighting that is built into the hardscape rather than added to it",
    table(["Fixture", "Where it goes", "Decided at which stage"],
          [("Paver lights", "Set flush in a driveway or walkway field", "Before the field is laid; conduit under the base"),
           ("Riser lights", "In the face of a step", "During step construction"),
           ("Wall and cap lights", "Under a seat-wall cap or in a pillar", "Before capping"),
           ("Well lights", "Uplighting a palm or a façade", "Trenching before the hardscape edge is set"),
           ("Path lights", "Beside a walk", "Can be retrofitted, but conduit is cheaper now"),
           ("Under-coping lights", "Below the pool coping", "During deck construction"),
           ("Transformer and timer", "At the house, near the panel", "Sized once the fixture schedule is known")],
          caption="Almost every item here is cheap before the pavers go down and expensive afterwards, which is why lighting is a design conversation rather than an upsell at the end."),
    eyebrow="Planning") + sec(
    "Low voltage, and who does what",
    """<p>Landscape lighting here is low-voltage, typically twelve volts from a transformer plugged into or wired to an existing exterior outlet. The low-voltage side, meaning the transformer's output, the runs, the fixtures and the conduit in the hardscape, is work we do as part of the hardscape. The line-voltage side, meaning a new circuit, a new outlet or anything inside the panel, is a licensed electrician's work and we coordinate it rather than performing it.</p>
<p>Two practical notes. Size the transformer for the final fixture count plus headroom, because adding fixtures to a fully loaded transformer means replacing it. And run conduit sleeves under every hardscape crossing even where no fixture is planned, since the sleeve costs almost nothing during construction and is the difference between a future addition being a half-day job or a demolition.</p>""",
    cls="alt")
FAQS["/pavers/outdoor-lighting/"] = [faq("Can lighting be added to my existing paver driveway?", "Path lights beside it, yes. Lights set into the field mean lifting pavers and trenching the base, so the conduit is far cheaper to place during the original installation.")]

SECTIONS["/coatings/garage-floors/"] = sec(
    "What happens on each of the two days",
    """<p>Day one is preparation and it is the whole job. The garage is emptied, the slab is diamond-ground to an open profile rather than acid-etched, and the dust is collected by a vacuum on the grinder rather than left to settle on everything. Cracks are routed and filled, spalled areas are patched, and control joints are either filled or deliberately honoured depending on the system. A moisture test has already been done at the estimate, and where it called for one, a moisture-mitigating primer goes down. Then the base coat is rolled and the vinyl flake is broadcast into it to rejection, which is to say until the surface will not take any more.</p>
<p>Day two is the finish. The loose flake is scraped and vacuumed, which is what produces a smooth surface rather than a gritty one, and the polyaspartic top coat goes on with an anti-slip aggregate suspended in it. Foot traffic returns in six to twelve hours, vehicles in forty-eight to seventy-two, and heavy shelving after about five days.</p>""",
    eyebrow="Timeline") + sec(
    "Why coatings fail, in order of frequency",
    table(["Failure", "Cause", "Prevention"],
          [("Peeling in sheets", "Moisture from below on a slab with no vapour barrier", "Moisture test and a mitigating primer"),
           ("Peeling at the edges and joints", "Acid etching instead of grinding; weak bond", "Diamond grinding to profile"),
           ("Hot-tire pickup", "A thin or under-cured coating", "Correct film build and full cure before parking"),
           ("Yellowing at the door", "Pure epoxy exposed to UV", "A polyaspartic top coat"),
           ("Bubbles or pinholes", "Applied too hot, or over a slab that was outgassing", "Temperature control and correct timing"),
           ("Gritty, uneven surface", "Loose flake not scraped before the top coat", "The day-two scrape and vacuum")],
          caption="Five of the six are decided by preparation. The estimate that skips the moisture test is the one to question."),
    cls="alt")
FAQS["/coatings/garage-floors/"] = [faq("Why does the slab have to be ground rather than acid-etched?", "Grinding opens a consistent profile for the coating to key into and removes the curing compound builders leave behind. Acid etching is inconsistent and is behind a large share of the edge peeling we are called to fix.")]
