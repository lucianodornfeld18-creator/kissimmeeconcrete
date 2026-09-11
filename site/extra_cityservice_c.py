# -*- coding: utf-8 -*-
"""Extra local depth for the Haines City and Harmony city×service pages."""
from _helpers import sec, table, faq

SECTIONS = {}
FAQS = {}

# =========================================================== HAINES CITY (4)
SECTIONS["/concrete/driveways/haines-city/"] = sec(
    "An old downtown wrapped in new subdivisions",
    """<p>Haines City is two building eras with very little in between. The streets around the historic downtown and along Hinson Avenue carry houses from the 1920s through the 1970s, with narrow driveways, deep setbacks and mature oaks. Around them, since roughly 2015, a ring of new subdivisions has gone up along Highway 17-92, Commerce Avenue and out toward Lake Hamilton, with builder-standard driveways poured to a production specification.</p>
<p>The work splits accordingly. Downtown is replacement work with root problems, awkward widths and street edges that have been patched several times. The new subdivisions are extensions, widenings and pads: the driveway is fine, but it is sixteen feet wide with two cars, a boat and a work van to accommodate. Those are additive projects where matching the existing slab is the first question and usually the reason the answer turns out to be pavers.</p>""",
    eyebrow="Two eras") + sec(
    "Widening a builder driveway without it looking added on",
    """<p>A production driveway poured five years ago has a colour, a finish direction and a joint pattern. New concrete beside it will be lighter for a year, will not match the broom direction unless we copy it deliberately, and will show a cold joint down the length of the drive. There are three ways to handle that and they cost differently.</p>
<p>Pour the extension and accept the seam, which is cheapest and looks like what it is. Pour the extension and resurface the whole drive so the surface is uniform, which adds roughly the resurfacing rate across the original area. Or replace the whole drive, or cover it in pavers, so there is no seam to explain. On a house the owner intends to sell within a few years the first is usually right; on a long-term home the second or third often is.</p>""",
    cls="alt")
FAQS["/concrete/driveways/haines-city/"] = [
    faq("Can a driveway extension be made to match?", "Not exactly. New concrete is lighter for about a year and the joint is permanent. Resurfacing the whole drive after the extension, or covering it in pavers, are the two ways to get a uniform surface."),
    faq("Does Haines City or Polk County issue the permit?", "Haines City has its own building department for addresses inside the city limits; the surrounding area is unincorporated Polk County. We check the parcel before filing."),
]

SECTIONS["/concrete/patios/haines-city/"] = sec(
    "Rear yards on new subdivision lots",
    """<p>The subdivisions built around Haines City since 2015 typically hand over a house with a small covered lanai and a large, empty, flat rear yard, and the first project most owners take on is a patio. Three things about those lots shape the design. The rear setback is often generous, so there is room. The lot was graded by the builder to drain to a swale between properties, and that route has to stay open. And the builder's lanai slab is usually four inches with a thickened edge only where the roof columns land.</p>
<p>Extending that slab means doweling into it, matching the elevation exactly so there is no lip at the transition, and carrying the fall away from the house. Building a detached patio instead avoids the matching problem entirely and is often the better looking answer, with a paver or concrete walk connecting the two.</p>""",
    eyebrow="New-build lots") + sec(
    "Planning now for the screen room later",
    table(["If you might add", "What the slab needs now", "Cost of doing it now", "Cost of retrofitting"],
          [("A screen enclosure", "A thickened edge or footing at the perimeter", "A modest addition to the pour", "Saw-cutting and underpinning the slab edge"),
           ("A pergola on posts", "Footings at the post locations", "Small, if located now", "Core-drilling and epoxy anchors, or new footings"),
           ("An outdoor kitchen", "A thickened section under the run plus conduit and a sleeve", "Small", "Cutting the slab for services"),
           ("A hot tub", "Five inches with a grid under the tub footprint", "Modest", "Adding a separate pad beside the patio"),
           ("Nothing", "Standard four inch slab", "Baseline", "Not applicable")],
          caption="The pattern on new-build lots is that the patio comes first and the structures follow within a few years. Deciding now costs very little; retrofitting costs several times more."),
    cls="alt")
FAQS["/concrete/patios/haines-city/"] = [
    faq("Can my builder lanai slab be extended?", "Yes, doweled with an expansion joint at the seam and matched at the elevation so there is no lip. The colour will differ for about a year."),
    faq("Should I plan for a screen room now?", "If there is any chance of one, yes. A thickened edge poured now costs very little; retrofitting a footing under an existing slab costs several times more."),
]

SECTIONS["/concrete/repair/haines-city/"] = sec(
    "Downtown repairs, oaks and a century of patching",
    """<p>The concrete around Haines City's older streets has been repaired before, often several times, and that history is part of the job. We commonly find a 1960s slab with a 1980s patch and a 2000s overlay on top, each bonded to the last with whatever was available, and each delaminating at a different rate. Grinding into that to find sound concrete is the first hour of the work and it sometimes changes the recommendation.</p>
<p>Oaks are the other constant. The trees planted along these streets when the houses were built are now large, and their root plates run under driveways, walks and the public sidewalk. Where a root has lifted a panel, the honest options are the same as anywhere: grind for a year, replace the panel with a root barrier for a decade, or reroute. What differs downtown is that many of those trees are prominent and some are protected, so cutting significant roots is a decision for an arborist, not for us with a saw.</p>""",
    eyebrow="Downtown") + sec(
    "The newer subdivisions have their own short list",
    """<p>On houses built since 2015 we are called for a narrow set of things. Settlement at the driveway apron where the utility trench crossed and the backfill consolidated. A cracked or dished section where the builder's base was placed on dry ridge sand and compacted without wetting. Hairline map cracking on a south-facing slab, which is cosmetic. And separation at the joint between the garage slab and the driveway, which is normal movement at an expansion joint and needs sealing rather than repair.</p>
<p>Most of those are inexpensive, and several of them are worth raising with the builder if the house is still inside its warranty period. We will say so when it applies, and put the observation in writing so it can be used, even though it means we are not doing the work.</p>""",
    cls="alt")
FAQS["/concrete/repair/haines-city/"] = [
    faq("My new-build driveway has already cracked. Is that normal?", "Hairline cracking is. A dished area or a step is base consolidation, and if the house is still inside its builder warranty that is worth raising with the builder first. We will put the observation in writing."),
    faq("Can a root-lifted panel be ground flat?", "It can be ground to remove the trip hazard, which buys about a year. A lasting fix means replacing the panel with a root barrier, and cutting significant roots needs an arborist's opinion."),
]

SECTIONS["/pavers/driveways/haines-city/"] = sec(
    "Pavers as the answer to a matching problem",
    """<p>A large share of the paver driveways we install in Haines City start as a widening question. The owner needs more parking, the existing slab is sound but five years old, and there is no way to add concrete beside it that does not read as an addition. Covering the whole footprint in pavers removes the problem: one surface, one colour, one date, and the extra width is not distinguishable from the original.</p>
<p>Whether the existing slab stays under the pavers or comes out depends on its condition and on the finished elevation. A sound slab can sometimes take a paver overlay with an appropriate bedding detail, which saves the removal cost but raises the driveway by two to three inches and creates a lip at the street and at the garage door that has to be resolved. More often, on a driveway that will be widened anyway, the slab comes out and the whole field is built on a proper base at the right elevation.</p>""",
    eyebrow="Why pavers here") + sec(
    "Base method on the ridge, stated plainly",
    """<p>Haines City sits on the same Candler and Tavares sands as the rest of this stretch of Polk County, and the base method is the ridge method: six inches of limerock in two lifts, each one wetted before compaction, probed after compaction, then a one inch screeded bedding course. Compacting ridge sand dry produces a base that passes a visual inspection and consolidates in its first heavy wet season.</p>
<p>Edge restraint matters more here than on a cohesive soil, because there is no cohesion in the surrounding ground to help hold the outside course. We use a concrete edge restraint on any side that takes turning traffic and spiked restraint elsewhere, and we set the finished level so the field sheds water rather than trapping it against the garage.</p>""",
    cls="alt")
FAQS["/pavers/driveways/haines-city/"] = [
    faq("Can pavers go over my existing concrete driveway?", "Sometimes, on a sound slab, but it raises the surface by two to three inches and creates a lip at the street and the garage. On a drive that is being widened anyway, removing the slab is usually the better answer."),
    faq("Why do you wet the base before compacting?", "Because dry ridge sand shears rather than densifies. Wetting each lift is what makes the compaction real, and it is the difference between a field that stays flat and one that settles in its first wet season."),
]

# =============================================== HARMONY AND NARCOOSSEE (4)
SECTIONS["/concrete/driveways/harmony/"] = sec(
    "Long drives, big lots and where the truck can go",
    """<p>Harmony was planned from 2003 with a conservation ethos and generous lots, and the newer Sunbridge and Weslyn Park communities along Narcoossee Road have continued the pattern from 2021 onward. Between and around them are working rural parcels on Nova Road, Jones Road and out toward Holopaw with driveways measured in hundreds of feet rather than tens.</p>
<p>On a long rural drive the concrete is the straightforward part. The questions are whether a loaded mixer can reach the pour, whether it can turn around without using the neighbour's field, whether the culvert at the county road will carry thirty tons, and where the septic tank and drainfield sit. We walk the whole route at the site visit, and where the truck cannot reach we price a pump truck or concrete buggies as a line item rather than discovering the problem with a truck idling at the gate.</p>""",
    eyebrow="Rural access") + sec(
    "Soils east of St. Cloud are wetter, not drier",
    """<p>It is tempting to assume that large rural lots drain better than suburban ones. East of St. Cloud the opposite is often true. The map units out toward Harmony and Holopaw include EauGallie and Basinger fine sands and, in the low areas, depressional phases that sit at or near the surface through the wet season. A hundred-foot driveway will frequently cross more than one of them.</p>
<p>Practically that means a long drive is rarely a single specification. The sections crossing low ground get raised on structural fill with a swale alongside; the sections on higher ground get the standard base. Pricing a long rural drive at one rate per square foot ignores that, and the resulting slab dips where the ground is worst. Our proposals break the run into sections with the treatment for each.</p>""",
    cls="alt")
FAQS["/concrete/driveways/harmony/"] = [
    faq("Will a concrete truck reach my rural driveway?", "We walk the route at the site visit, including the culvert at the county road and the turnaround. Where it will not work we price a pump truck or buggies rather than finding out on pour day."),
    faq("Why does a long driveway need more than one specification?", "Because it usually crosses more than one soil condition. Low sections need fill and a swale; higher sections do not. One rate across the whole run produces a slab that dips where the ground is worst."),
]

SECTIONS["/concrete/slabs/harmony/"] = sec(
    "Workshop slabs, barns and equipment pads",
    """<p>The rural parcels around Harmony, Narcoossee and Holopaw are where we pour the largest pads in our territory: metal building slabs for workshops, equipment pads for tractors and trailers, pads for feed and hay storage, and generator pads on properties where an outage lasts longer than it does in town. Those are engineered differently from a suburban shed pad.</p>
<p>A pre-engineered metal building needs a slab designed around the supplier's anchor bolt layout and reaction loads, usually with a thickened edge or a perimeter footing that the building drawings specify. We build to those drawings rather than to a rule of thumb, and where the building supplier has not provided them we ask for them before quoting. A slab poured to the wrong bolt pattern is not adjustable.</p>""",
    eyebrow="Rural pads") + sec(
    "Septic, wells and everything else buried on a rural lot",
    table(["What is buried", "How we find it", "Clearance we work to"],
          [("Septic tank and drainfield", "County health department permit file, then probe", "Keep the pad and the truck route entirely clear"),
           ("Potable well and supply line", "Owner, wellhead location, visible line route", "Clear of the pad and clear of heavy equipment tracking"),
           ("Irrigation well and lines", "Owner, head positions, probe", "Relocate or sleeve where a crossing is unavoidable"),
           ("Propane tank and line", "Owner and supplier records", "Supplier clearances govern"),
           ("Electric to a barn or pump house", "Owner; 811 covers regulated utilities only", "Locate before excavation"),
           ("Drainage ditches and culverts", "Visible, plus the plat", "Truck route has to cross on something rated for it")],
          caption="Private lines on private property are outside the 811 system, which is why the owner's knowledge is part of the site visit on a rural parcel."),
    cls="alt")
FAQS["/concrete/slabs/harmony/"] = [
    faq("Do you need the building drawings before quoting a workshop slab?", "Yes. The anchor bolt layout and the reaction loads come from the building supplier, and a slab poured to the wrong pattern cannot be adjusted afterwards."),
    faq("Does 811 locate my well and septic?", "No. 811 covers regulated utilities. Private lines, wells and septic systems are located from the county file, the owner's knowledge and careful probing."),
]

SECTIONS["/pavers/driveways/harmony/"] = sec(
    "Pavers on a long drive, and when they stop making sense",
    """<p>Pavers work well on the entry section of a rural driveway and much less well on the whole length of one. A paver apron and the first thirty or forty feet give the arrival sequence a finished look, take the turning loads at the road, and can be lifted if the culvert or the utilities under them ever need attention. Continuing the same field for another hundred and fifty feet multiplies the cost of the most expensive surface by the largest area on the property.</p>
<p>The hybrid we most often recommend on these lots is a paver apron and entry, a poured concrete run, and a paver turnaround or parking court at the house. It costs less than pavers throughout, looks deliberate rather than compromised, and puts each material where it earns its price. We show both layouts and both numbers so the choice is informed.</p>""",
    eyebrow="Layout strategy") + sec(
    "Edge restraint where there is no kerb",
    """<p>In a subdivision a paver driveway is bounded by a kerb, a garage slab and a lawn that has been graded to the paver level. On a rural lot there is often nothing on either side but pasture, sand and a drainage swale, and the field has to hold its own edge against soil that will erode in the first heavy storm.</p>
<p>So the edge detail changes. We use a poured concrete edge restraint on both sides rather than spiked aluminium, set slightly below the finished paver level so it disappears, and we stabilise the shoulder beside it with sod or gravel so runoff does not undercut the restraint. Where the drive crosses a swale, the restraint and the base are carried through and the swale is reformed to its original section afterwards. Skipping any of that produces a field with a rolled edge within two seasons.</p>""",
    cls="alt")
FAQS["/pavers/driveways/harmony/"] = [
    faq("Should I do the whole rural driveway in pavers?", "Usually not. A paver apron and entry with a concrete run and a paver parking court at the house puts each material where it earns its cost, and we price both layouts."),
    faq("What holds the edge of a paver drive with no kerb?", "A poured concrete edge restraint set just below the paver level, with the shoulder beside it stabilised so runoff does not undercut it."),
]

SECTIONS["/pavers/pool-decks/harmony/"] = sec(
    "Decks on larger lots, without a screen",
    """<p>A lot of Harmony, Sunbridge and Narcoossee pools are built without a screen enclosure, which is less common in Osceola County than it is in the rest of the state and changes the deck job in three ways. There is no footer to cut to and no track to clear, so the layout is free. There is no roof concentrating water at a screen line, so drainage is a matter of falling to the yard rather than to a channel. And there is nothing between the deck and the oaks, which means leaf litter, tannin staining and organic growth in shaded joints.</p>
<p>Material choice follows. Tannin from oak leaves stains light concrete pavers noticeably and travertine less so; joints in shade need sealing more than joints in sun; and a deck that sits under a canopy stays damp long enough after a storm that a breathable, penetrating sealer is a better choice than a film.</p>""",
    eyebrow="Open decks") + sec(
    "Where the deck water goes on an acre lot",
    """<p>On a small suburban lot the deck's drainage problem is that there is nowhere to put the water. On an acre the problem is the opposite: there is somewhere, and it is usually the lowest corner of the property, which on the flatwoods soils east of St. Cloud may already be wet for months of the year. Sending several hundred square feet of additional runoff there turns a seasonal wet area into a standing one.</p>
<p>So the deck falls away from the pool at an eighth to a quarter inch per foot, and the runoff is directed to a route that can accept it, which sometimes means a shallow swale to a different part of the lot rather than the obvious low point. On parcels with a septic drainfield, the route also has to keep the additional water off the field, because saturating a drainfield with roof and deck runoff is one way to shorten its life.</p>""",
    cls="alt")
FAQS["/pavers/pool-decks/harmony/"] = [
    faq("Do I need a screen enclosure over a pool deck here?", "Many Harmony and Narcoossee pools do not have one. Without a screen the layout is freer, but leaf litter, tannin staining and damp shaded joints become the maintenance issues."),
    faq("Where should deck runoff go on a large lot?", "To a route that can accept it, which is not always the obvious low corner. On flatwoods soils that corner may already be seasonally wet, and it should never be the septic drainfield."),
]
