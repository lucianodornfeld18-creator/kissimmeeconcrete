# -*- coding: utf-8 -*-
"""Extra local depth for Four Corners, ChampionsGate, Reunion and Davenport city×service pages."""
from _helpers import sec, table, faq

SECTIONS = {}
FAQS = {}

# ========================================================== FOUR CORNERS (4)
SECTIONS["/pavers/pool-decks/four-corners/"] = sec(
    "A rental deck is a different specification",
    """<p>Four Corners is where Osceola, Polk, Lake and Orange counties meet along US-27 and US-192, and it is dominated by vacation homes with private pools. A deck on one of those houses is walked on by a different family every few days, in flip flops, with sunscreen, drinks and pool toys, and nobody rinses it. That is a harder service life than a family home deck, and specifying for it saves money over five years.</p>
<p>What changes. Light colour, because a dark deck in July generates complaints in reviews and guests simply stay indoors. A textured or tumbled surface rather than a smooth one, because wet grip with children running is the liability. A penetrating sealer rather than a glossy film, for the same reason. Joints sanded with a polymeric product and sealed, because loose joints plus pressure washing between guests is a fast route to a field that needs re-sanding every year. And a drain channel at the screen line, because water pooling on a lanai is the second most common complaint after heat.</p>""",
    eyebrow="Rental duty") + sec(
    "Scheduling around a booking calendar",
    table(["Scope", "Days on site", "Deck out of use", "Booking gap to hold"],
          [("Clean, re-sand and seal an existing deck", "1", "24 hours after sealing", "2 to 3 days"),
           ("Thin paver overlay on a sound deck", "3 to 4", "Through the work", "5 days"),
           ("Full deck rebuild with base and drainage", "5 to 7", "Through the work", "8 to 10 days"),
           ("Repair a settled section", "1 to 2", "Through the work", "3 days"),
           ("Coping replacement only", "2 to 3", "Pool usable, deck restricted", "4 days")],
          caption="Working durations for a typical 600 square foot resort-home deck. Architectural approval runs ahead of all of them and is the longer lead time."),
    cls="alt")
FAQS["/pavers/pool-decks/four-corners/"] = [
    faq("Which county issues the permit in Four Corners?", "It depends which side of the intersection the house is on. Most of the vacation-home inventory sits in Polk and Osceola, and the rules differ, so we check the parcel rather than the address."),
    faq("Can a deck be done between bookings?", "A clean, re-sand and seal fits a two to three day gap. An overlay or a rebuild needs a deliberate block in the calendar."),
]

SECTIONS["/pavers/sealing/four-corners/"] = sec(
    "Sealing on a property that is cleaned constantly",
    """<p>Vacation homes get pressure washed far more often than owner-occupied houses, usually by the same management company that does the turnovers, and usually at whatever pressure the machine is set to. That is the single biggest destroyer of paver joints in this corridor. Every aggressive wash removes joint sand, and a field with empty joints loses interlock, which is what lets edges roll and units rock under foot.</p>
<p>So our sealing scope on a rental almost always includes a full re-sand, and we ask to speak with the cleaning contractor about pressure and nozzle choice. A surface cleaner at moderate pressure gets the deck just as clean without excavating the joints. Where the management company will not change its method, we tell the owner to budget for re-sanding every two years rather than every four, because that is what will actually happen.</p>""",
    eyebrow="Maintenance reality") + sec(
    "What a sealed deck does and does not prevent",
    """<p>A joint-stabilizing sealer locks the polymeric sand, slows organic growth in the joints, makes sunscreen and drink spills easier to remove, and keeps colour from washing out under UV. It does not stop a settled area from settling further, it does not prevent rust staining where a well irrigation head reaches the deck, and it does not make a dark deck cooler.</p>
<p>The honest sequence on a resort property is therefore: fix any settlement, treat existing staining, re-sand, then seal. Sealing first is the sequence that produces a call six months later asking why the deck looks worse than before, and the answer is that the sealer is now sitting on top of the problem.</p>""",
    cls="alt")
FAQS["/pavers/sealing/four-corners/"] = [
    faq("How often should a rental pool deck be sealed?", "Every two to three years in this corridor, more often than an owner-occupied deck because of the cleaning frequency and the UV exposure."),
    faq("Can the cleaning company damage the pavers?", "Not the pavers so much as the joints. High pressure removes joint sand, and a field with empty joints loses its interlock."),
]

SECTIONS["/pavers/driveways/four-corners/"] = sec(
    "Driveways that take fleet traffic",
    """<p>A vacation home's driveway sees rental SUVs, shuttle vans, delivery vehicles, pool service trucks, landscaping trailers and, several times a week, a cleaning crew's vehicle. That is closer to light commercial duty than to a family driveway, and it shows up at the edges first: the outside course rolls, the apron corner breaks, and the field near the street develops rutting where vehicles turn in.</p>
<p>What we specify differently. Eighty millimetre pavers rather than sixty everywhere, including any walkway that a vehicle might clip. A concrete edge restraint rather than spiked aluminium on the sides that see turning traffic. A poured concrete apron at the right-of-way where the jurisdiction allows or requires it, because that is the part taking the worst of the turning loads. And six inches of base compacted in two lifts as a minimum, not a starting point for negotiation.</p>""",
    eyebrow="Traffic") + sec(
    "The Polk County paver release, and why it exists",
    """<p>If any part of the paver driveway sits in the county right-of-way, Polk County asks the owner to sign a release form that is notarised and recorded with the Clerk, accepting responsibility for maintaining that section and indemnifying the county. It exists because the county has to be able to cut the right-of-way for utility work without becoming liable for restoring a decorative surface.</p>
<p>It is a five-minute step if you know about it and a two-week delay if you do not. We include the form in the packet on Polk-side jobs and walk the owner through it. On the Osceola side, the county driveway permit covers pavers and the twenty-four foot width cap applies instead.</p>""",
    cls="alt")
FAQS["/pavers/driveways/four-corners/"] = [
    faq("Do I need to record anything for pavers in the right-of-way?", "In Polk County, yes. A notarised release form is recorded with the Clerk accepting maintenance responsibility for the section in the right-of-way."),
    faq("Are sixty millimetre pavers strong enough for a driveway?", "For a family car on a good base, they can be. On a rental driveway with shuttle vans and service trucks we specify eighty millimetre throughout."),
]

SECTIONS["/concrete/repair/four-corners/"] = sec(
    "Repairs that have to be invisible by Friday",
    """<p>On a rental property a concrete repair is judged by two things: whether it is safe and whether it photographs. A trip lip on the walk to the front door is a liability item that has to be dealt with before the next check-in, and a patched panel that reads as a patch in the listing photographs is a different kind of cost.</p>
<p>That pushes the decisions in a particular direction. Grinding a lip is a same-week fix and is often the right immediate action even when a panel replacement is the eventual answer. A visible panel in the entry sequence is usually better replaced as a whole element, or resurfaced across the full area, than patched. And cracks that are cosmetic get sealed and left alone, because the alternative is a repair that looks worse than the crack.</p>""",
    eyebrow="Rental priorities") + sec(
    "Four counties, four sets of paperwork",
    table(["Where the house is", "Permit office", "Repair in the same footprint", "Apron or right-of-way work"],
          [("Osceola side", "Osceola County Building Office", "No permit", "County driveway permit"),
           ("Polk side", "Polk County Building Division", "No permit", "Permit; paver release if pavers"),
           ("Lake side", "Lake County", "No permit", "County right-of-way approval"),
           ("Orange side", "Orange County", "Minor repairs generally exempt", "Permit; six inch, three thousand psi apron with no steel")],
          caption="A Four Corners address can be in any of the four. We resolve it from the parcel before quoting, because filing with the wrong office costs weeks."),
    cls="alt")
FAQS["/concrete/repair/four-corners/"] = [
    faq("How fast can a trip hazard be fixed before a check-in?", "Grinding a lip is usually a same-week visit. A panel replacement needs two days plus cure, so we grind first when the calendar is tight and schedule the permanent fix around a gap."),
    faq("Will a repaired panel be noticeable in listing photos?", "For about a year, yes; new concrete is lighter. Replacing the whole element or resurfacing the area avoids it."),
]

# ========================================================= CHAMPIONSGATE (4)
SECTIONS["/pavers/pool-decks/champions-gate/"] = sec(
    "Resort-grade decks on tight rear lots",
    """<p>ChampionsGate went in from 2001 onward on the Osceola side of the I-4 and US-27 interchange, and the vacation-home phases were built with deep, narrow lots and pools that fill most of the rear yard. A deck rebuild there is a project with very little working room: the pool, the screen enclosure and the rear property line are often within a few feet of each other, so material and spoil move through the house side yard or over the front.</p>
<p>The design opportunity is that a small deck responds well to large-format units and a simple border, which makes the space read larger than a busy pattern would. The design constraint is that the deck has to take the enclosure footer, the equipment pad access and a drain line without any of it looking like an afterthought. We lay it out on paper with those three fixed before choosing a pattern.</p>""",
    eyebrow="Site") + sec(
    "Approvals in a resort community",
    """<p>ChampionsGate's residential phases sit under community associations with architectural review, and separately the whole area is unincorporated Osceola County for permitting. The two run on different clocks and the association is normally the longer one. What boards in resort communities consistently want to see is a site plan or survey with the work marked, the product and colour, the pattern, a drainage note showing where deck water goes, and the installer's certificate of insurance, sometimes naming the association as an additional interest.</p>
<p>We have not obtained and read the current written architectural criteria for every ChampionsGate sub-association, so we do not quote rules we have not verified. What we do is contact the management company for the specific address, get the current packet requirements in writing, and put them in the proposal. Where we have read and verified a community's criteria, such as Solterra in Davenport, we quote them directly.</p>""",
    cls="alt")
FAQS["/pavers/pool-decks/champions-gate/"] = [
    faq("Who approves a pool deck change in ChampionsGate?", "The sub-association for your phase, through its architectural review process, and separately Osceola County for any permitted scope. We confirm the current packet requirements with the management company for the address."),
    faq("Is there room for machinery on a ChampionsGate lot?", "Rarely. Most of these rear yards are hand-worked with wheelbarrow access, which we price into the job rather than absorbing."),
]

SECTIONS["/pavers/sealing/champions-gate/"] = sec(
    "Sealing a deck that is twenty years old",
    """<p>The earliest ChampionsGate paver decks are now around twenty years old, and they arrive at a sealing visit with a specific history: multiple sealer applications from different contractors, joint sand that has been topped up with whatever was on the shelf, and in some cases a film-forming product applied over a damp surface at some point that left a permanent haze in patches.</p>
<p>The first decision on those decks is whether to seal over or strip back. Sealing over an old acrylic that is peeling or clouded just adds a layer to the problem. Stripping is chemical, slow and costs roughly what the sealing itself does, and it is the right answer when the existing film is failing. We test a small area before quoting rather than guessing from the kerb, because the two paths differ by a factor of two in price.</p>""",
    eyebrow="Existing coatings") + sec(
    "What we do about the joints on an older field",
    """<p>Twenty years of storms, pressure washing and settlement leaves joints that are partly empty, partly filled with organic matter and partly filled with old polymeric sand that has lost its binder. Sweeping new sand on top of that does not work; it sits high, never reaches depth, and crusts.</p>
<p>So the joints are cleaned out mechanically to at least the depth of the paver, the field is blown clean, and new polymeric sand goes in dry, is vibrated down with a plate compactor on a protective pad, topped up, blown clean again and then watered in stages per the product instructions. It is most of the labour in the visit and it is the part that decides whether the sealing lasts three years or one.</p>""",
    cls="alt")
FAQS["/pavers/sealing/champions-gate/"] = [
    faq("My deck has a cloudy white film. Can it be fixed?", "Usually. A failed or moisture-trapped acrylic is stripped chemically and the deck is resealed once it is dry. We test a small area first because stripping roughly doubles the job."),
    faq("Can new joint sand go on top of the old?", "No. Old sand has to come out to at least the paver depth or the new sand crusts at the surface and pops out.")
]

SECTIONS["/pavers/driveways/champions-gate/"] = sec(
    "Driveways in a community built for arrivals",
    """<p>Vacation homes in ChampionsGate typically have a two-car garage, a driveway long enough for two more vehicles, and a steady rotation of guests who park where there is room. The wear pattern is at the edges and at the turn-in, and the aesthetic pressure is at the entry sequence, because the driveway is in every listing photograph.</p>
<p>A paver driveway suits both. The edge courses take the loads if they are restrained properly, and a border in a contrasting tone defines the parking area without any signage. Where a previous owner has widened the drive with a strip of concrete that no longer matches, replacing the whole field in pavers usually costs less than trying to make two vintages of concrete look intentional.</p>""",
    eyebrow="Use") + sec(
    "Permits on the Osceola side of the interchange",
    """<p>ChampionsGate is unincorporated Osceola County, so a new or widened driveway needs the county driveway permit, and residential driveways are capped at twenty-four feet wide without a conditional use under section 22-50.6. The Building Office reviews residential applications in roughly three to five days, and a Notice of Commencement is recorded before the first inspection on jobs of five thousand dollars or more.</p>
<p>The association's approval comes first regardless. In practice the sequence that works is: get the architectural approval, then file the county application with the approved product and layout attached, then schedule. Reversing it produces a permitted driveway that the board has not agreed to.</p>""",
    cls="alt")
FAQS["/pavers/driveways/champions-gate/"] = [
    faq("How wide can a ChampionsGate driveway be?", "The county caps residential driveways at twenty-four feet without a conditional use. The association may be tighter, and its rule governs."),
    faq("Can two vintages of concrete be made to match?", "Not reliably. Where a drive has been widened at a different time, re-covering the whole field in pavers usually looks better and often costs less than the alternatives."),
]

SECTIONS["/concrete/repair/champions-gate/"] = sec(
    "What fails first on a twenty-year-old resort lot",
    """<p>The concrete on these lots is mostly original to the 2001 to 2015 build-out, and the failures follow the water. The lanai slab cracks where the screen enclosure footer meets it, because that is a restrained edge. The walk between the driveway and the front door settles where the downspout discharges. The apron cracks at the corner under turning delivery vehicles. And the equipment pad behind the house sinks because it was poured thin on unprepared ground.</p>
<p>All four are ordinary and repairable. What makes them a rental problem rather than a maintenance problem is that two of them, the entry walk and the apron, are in the guest's first thirty seconds on the property. That usually moves them up the priority list ahead of things that matter more structurally.</p>""",
    eyebrow="Failure patterns") + sec(
    "Coordinating with the property manager",
    """<p>On managed properties we work to the manager's calendar and their access process rather than the owner's, because they hold the gate codes, the lock box and the guest schedule. What we need from them is a confirmed window, access details, a contact who can approve a small change on the day, and confirmation that the pool service and cleaning schedules are paused for the work.</p>
<p>What we give back is a start and finish time for each day, photographs at the end of each day so an out-of-state owner can see progress, and a written note of anything discovered that changes the scope. On a rental, a surprise that costs a booking is worse than the repair it came from, so we say it the day we find it.</p>""",
    cls="alt")
FAQS["/concrete/repair/champions-gate/"] = [
    faq("Can you work with my property manager rather than me?", "Yes, and on managed properties it is usually faster. We need a confirmed access window and a contact who can approve a minor change on the day."),
    faq("Why does my lanai slab crack at the screen footer?", "Because that edge is restrained while the rest of the slab moves. It is common, usually cosmetic, and sealed rather than replaced unless there is a step.")
]

# =============================================================== REUNION (4)
SECTIONS["/pavers/pool-decks/reunion/"] = sec(
    "Three management companies, one county",
    """<p>Reunion is administered in parts. Artemis Lifestyles handles the single-family and several other product types, Greystone manages the Villas north and south, and Southwest Property Management handles the Terraces. Which one reviews your pool deck depends on which product type your home is, not on where it sits geographically, and a submission sent to the wrong company simply waits.</p>
<p>For permitting, the whole resort is unincorporated Osceola County. A paver deck overlay that does not tie into the pool structure is generally flatwork; a rebuild that touches the bond beam, the enclosure footer or the elevation at a door is a conversation with the Building Office before we quote. We resolve both questions at the site visit and put the answers in the proposal.</p>""",
    eyebrow="Governance") + sec(
    "Decks built between 2004 and 2015, and what they need now",
    """<p>Most Reunion decks are ten to twenty years old, and that is the age at which the original installation's quality becomes visible. Decks built on a properly compacted base are still flat and need cleaning, re-sanding and sealing. Decks built on thin or uncompacted base have settled at the loaded edges, usually where the spa or the outdoor kitchen sits, and those need the field lifted and the base rebuilt under the affected area.</p>
<p>The coping is often the deciding element. Original bullnose coping that has stayed bonded and level indicates the deck has not moved against the pool; coping that has lifted or separated indicates it has. That single check, plus a tap test, tells us whether you are buying a maintenance visit or a rebuild, and the difference between those two numbers is large enough to be worth the twenty minutes.</p>""",
    cls="alt")
FAQS["/pavers/pool-decks/reunion/"] = [
    faq("Which Reunion management company handles my application?", "It depends on your product type: Artemis for single-family and several others, Greystone for the Villas, Southwest for the Terraces. We confirm before submitting."),
    faq("How do I know if my deck needs a rebuild rather than a clean and seal?", "Check the coping and tap the deck. Bonded, level coping and a solid ring mean maintenance. Lifted coping or hollow areas mean the base has moved."),
]

SECTIONS["/pavers/travertine/reunion/"] = sec(
    "Why travertine suits this particular market",
    """<p>Reunion's homes are at the upper end of the vacation rental market, competing on photographs and on guest experience, and travertine does well on both counts. It photographs as stone rather than as concrete, it stays noticeably cooler underfoot than grey concrete pavers at two in the afternoon in July, and tumbled travertine has good wet grip, which matters when the deck is full of children.</p>
<p>The trade-offs are real and worth stating. It costs more, roughly twenty to thirty-six dollars a square foot installed against fifteen to twenty-four for a concrete paver overlay. It is a calcareous stone, so acidic cleaners and acidic pool chemistry etch it and muriatic acid destroys it. And it wants a penetrating sealer every two to three years on a deck in full sun, never a film-forming one.</p>""",
    eyebrow="Material fit") + sec(
    "Set on sand or thin-set on the existing deck",
    table(["", "Sand-set travertine", "Thin-set over existing concrete"],
          [("Base", "Compacted limerock plus bedding course", "The existing slab, which must be sound"),
           ("Height added", "Set to the design elevation", "About an inch, which has to clear thresholds"),
           ("If the ground moves later", "Lift and relay the affected area", "The stone has to be broken out"),
           ("Suits", "Rebuilds, new decks, decks with drainage problems", "Sound, well-drained decks with no hollow areas"),
           ("Cost", "Higher, includes excavation and base", "Lower, no excavation"),
           ("Deciding test", "Not applicable", "Tap test and string line across the coping")],
          caption="The decision is made by the condition of the existing deck, not by preference. A thin-set stone deck over a moving slab is the most expensive mistake available here."),
    cls="alt")
FAQS["/pavers/travertine/reunion/"] = [
    faq("Is travertine worth it on a rental?", "It is cooler underfoot and photographs as stone, both of which matter in this market. It also costs more and needs a penetrating sealer every two to three years."),
    faq("Can travertine be laid over my existing pool deck?", "Only if the deck is sound. Thin-set stone over a slab that later moves has to be broken out, and the stone rarely survives removal."),
]

SECTIONS["/pavers/sealing/reunion/"] = sec(
    "Sealing stone and sealing concrete are different jobs",
    """<p>Reunion decks are a mix of concrete pavers, travertine and marble, sometimes on the same property, and the products are not interchangeable. Concrete pavers take a joint-stabilizing acrylic that locks the polymeric sand and gives a light sheen. Travertine and marble take a penetrating silane or siloxane that soaks in and changes nothing visually. Putting the acrylic on the stone traps moisture and hazes it; putting the penetrating product on concrete pavers leaves the joints unstabilised.</p>
<p>On a property with both, that means two products, two application methods and a clear line between them, which is worth confirming in the proposal rather than discovering afterwards. We also check what is already on each surface, because sealing a new product over an incompatible old one is the other common failure.</p>""",
    eyebrow="Product choice") + sec(
    "Cleaning without etching the stone",
    """<p>The chemistry that safely cleans a concrete paver will damage travertine. Acidic efflorescence removers and rust removers formulated for concrete dissolve the surface of calcareous stone, leaving a dull, rough patch that cannot be polished out. That applies to muriatic acid absolutely, and to several products sold for driveway cleaning at the big box stores.</p>
<p>On stone we use neutral or alkaline cleaners, stone-safe iron removers where there is irrigation staining, and mechanical agitation with a nylon brush rather than aggressive pressure. Organic growth in shaded areas responds to a percarbonate cleaner. Sunscreen and body oils, which are the characteristic rental stain, come out with an alkaline degreaser and a poultice on anything that has soaked in.</p>""",
    cls="alt")
FAQS["/pavers/sealing/reunion/"] = [
    faq("Can the same sealer be used on travertine and concrete pavers?", "No. Stone needs a penetrating sealer; concrete pavers need a joint-stabilizing product. Using the acrylic on stone traps moisture and hazes it."),
    faq("What removes sunscreen stains from a stone deck?", "An alkaline degreaser and, for anything that has soaked in, a poultice. Never an acidic cleaner on travertine or marble."),
]

SECTIONS["/pavers/driveways/reunion/"] = sec(
    "Driveways on a golf-course resort lot",
    """<p>Reunion's streets are narrow by design, many homes sit on a curve, and a fair number of driveways are short with a turning movement right at the garage. That geometry, rather than the traffic, drives the specification. Short drives with a turn concentrate steering loads in a small area, which is exactly where edge restraint and base compaction get tested.</p>
<p>On those we run a concrete edge restraint on the turning side rather than spiked aluminium, use eighty millimetre pavers throughout, and pay attention to the transition at the street, because a lip at the apron on a narrow curved street is where a rental car scrapes. Curved fields also carry a higher waste factor for cuts, which we state in the proposal rather than absorbing into a square-foot number that then looks inexplicably high.</p>""",
    eyebrow="Geometry") + sec(
    "What to do about an original concrete drive",
    """<p>Many Reunion homes still have their original poured concrete driveways from the 2004 to 2015 build-out. At that age they are typically sound but tired: hairline map cracking, joint edges spalled, staining at the parking spots, and a colour that has gone grey and blotchy. There are three sensible paths and they differ by a factor of three in cost.</p>
<p>Clean and seal is the cheapest and changes little. Resurfacing with a textured overlay renews the surface for ten to fifteen years on a sound slab and can take colour and a pattern. Replacing with pavers changes the look completely, adds repairability, and needs architectural approval. For a rental competing on photographs, the second and third options are the ones that show up in the listing, and we price all three so the choice is made with numbers.</p>""",
    cls="alt")
FAQS["/pavers/driveways/reunion/"] = [
    faq("Do short driveways cost less per square foot?", "No, usually more. Fixed costs like mobilisation, the base crew day and the cutting on a curved field do not scale down with area."),
    faq("Should I resurface or replace my original concrete drive?", "If the slab is sound, resurfacing renews it for ten to fifteen years at about half the cost of replacement. If it is moving, neither resurfacing nor pavers over the top will hold."),
]

# ============================================================= DAVENPORT (5)
SECTIONS["/concrete/driveways/davenport/"] = sec(
    "Ridge sand behaves the opposite way to Kissimmee sand",
    """<p>Davenport sits on the Lake Wales Ridge, and the dominant soils are Candler and Astatula sands: deep, single-grained and excessively drained, with the water table far below anything a driveway cares about. After years of building on Osceola's wet flatwoods, the instinct is to relax. That is the mistake.</p>
<p>Dry ridge sand will not compact. Run a plate compactor over it in July and the surface shears and fluffs rather than densifying, so a base that looks finished is loose, and it consolidates the first time a heavy storm soaks it, which on the ridge means the slab settles in its first wet season rather than its tenth. The method that works is to wet each lift deliberately, compact it, and check it with a probe, and it is the reason a proposal from a contractor who works both counties should read differently for a Davenport job than for a Kissimmee one.</p>""",
    eyebrow="Ridge soils") + sec(
    "City of Davenport or Polk County",
    """<p>The City of Davenport is small and most of the addresses with a Davenport mailing address, including Providence, Solterra and the Loughman area, are actually unincorporated Polk County. That distinction decides the permit office. Polk County's Building Division, out of Bartow or the Northeast Government Center in Lake Alfred, permits slabs adjacent to or supporting structures, elevated slabs, sidewalks, and the portions of driveways that sit in the right-of-way or within minimum setbacks.</p>
<p>Inside the city limits it is the city's own department. Neither is obvious from the street or the ZIP code, which covers a large area of unincorporated county. We resolve it from the parcel at the site visit, and the Polk rules are quoted with their source on our Polk County permit page.</p>""",
    cls="alt")
FAQS["/concrete/driveways/davenport/"] = [
    faq("Why does ridge sand need to be wetted before compaction?", "Because dry single-grained sand shears instead of densifying. A base compacted dry looks finished and consolidates the first time it gets soaked, which settles the slab."),
    faq("Is my Davenport address in the city or the county?", "Most are unincorporated Polk County despite the Davenport mailing address. We check the parcel, because it decides which office issues the permit."),
]

SECTIONS["/pavers/driveways/davenport/"] = sec(
    "Solterra's driveway rules are unusually specific",
    """<p>Solterra Resort publishes architectural guidelines that address driveways directly, and they are worth reading before designing anything. An expanded driveway may not exceed three cars in width. No additional walking area may be added alongside an expanded driveway. Painting or staining of concrete paved surfaces is prohibited, and concrete may be sealed only in a clear matte finish and only after a submitted request. Applications for paver work are expected to include a survey of the lot, a sketch of the proposed work and a material sample, and the board may require the installer's certificate of insurance naming the association.</p>
<p>Those provisions shape the design more than the county rules do. A three-car-wide cap on a lot where the owner wanted four spaces is the constraint that decides the layout, and the prohibition on staining is the reason several Solterra owners move from concrete to pavers when they want colour.</p>""",
    eyebrow="Association rules") + sec(
    "Providence, Loughman and the rest of the corridor",
    """<p>Providence, platted from around 2005, is a golf community with larger lots and its own architectural review. Loughman and the older unincorporated pockets along US-17-92 have no association at all, which makes the county rules the only rules and shortens the timeline considerably. The newest phases along Ronald Reagan Parkway and out toward Highway 27 are still being built, and on those the developer's builder standards apply until the association takes over.</p>
<p>What is constant across all of them is the soil and the base method. What varies is who has to say yes, and how long that takes. We establish the governing documents for the address before the design conversation, because designing first and asking afterwards is how a paver pattern gets rejected after the material has been ordered.</p>""",
    cls="alt")
FAQS["/pavers/driveways/davenport/"] = [
    faq("How wide can a driveway be in Solterra?", "The published guidelines cap an expanded driveway at three cars wide and prohibit adding walking area alongside it."),
    faq("Can I stain or paint my concrete driveway in Solterra?", "No. The guidelines prohibit painting and staining of concrete paved surfaces and allow a clear matte sealer only with a submitted request."),
]

SECTIONS["/pavers/pool-decks/davenport/"] = sec(
    "Vacation-home decks on the Polk side",
    """<p>Solterra, Providence, Windsor Island and the other Davenport-area resort communities are full of private pools on compact lots, and the deck is a marketing surface as much as a functional one. The same rental-duty specification applies here as across the corridor: light colour for heat, textured surface for wet grip, penetrating sealer rather than a glossy film, polymeric joints, and a drain at the screen line.</p>
<p>The Polk-side difference is underneath. Candler sand drains so freely that standing water on a deck is rarely the problem; the problem is base consolidation. A deck built on dry-compacted base settles at the loaded edges, typically where the spa sits or where the sliding door traffic concentrates, and it does it within the first few years rather than slowly over a decade. Wetting and compacting each lift is the whole prevention.</p>""",
    eyebrow="Ridge conditions") + sec(
    "Approval, permit and the order they go in",
    """<p>Solterra's architectural process wants the survey, the sketch, the material sample and often the installer's insurance certificate, and the board can require the certificate to name the association. Polk County permits the portions of the work that sit in setbacks or attach to a structure, and treats a free-standing deck outside setbacks as unpermitted flatwork subject to the drainage rules.</p>
<p>The order that works is association first, county second, schedule third. A permit obtained before approval is not wasted exactly, but a board that asks for a different paver changes the application. We put both approvals in the packet and track them together, and where a community's written criteria are ones we have actually read, we quote them rather than paraphrasing.</p>""",
    cls="alt")
FAQS["/pavers/pool-decks/davenport/"] = [
    faq("Why do Davenport decks settle at the edges?", "Almost always base consolidation. Ridge sand compacted dry looks solid and settles once it is thoroughly wetted, which shows up at the most loaded edges first."),
    faq("Does Polk County permit a pool deck?", "It permits work in setbacks or attached to a structure. A free-standing deck outside setbacks is generally unpermitted flatwork, but the drainage rules still apply. We confirm for the parcel."),
]

SECTIONS["/concrete/repair/davenport/"] = sec(
    "Two different repair populations in one town",
    """<p>Davenport's concrete splits into two groups that need different conversations. The historic town core and the older unincorporated pockets have driveways from the 1950s through the 1980s, thin slabs on unprepared ridge sand, and at that age the repair question is usually the replacement question. The resort and subdivision phases from 2005 onward have much younger concrete, and their failures are specific and fixable: base consolidation at a loaded edge, a settled apron where a utility trench crossed, a cracked lanai slab at the enclosure footer.</p>
<p>Telling which population a property belongs to takes one look at the plat date and one tap test. It changes the advice completely, and it is the reason a single price per square foot for concrete repair across a town like this is close to meaningless.</p>""",
    eyebrow="Two populations") + sec(
    "What consolidated base looks like from above",
    table(["Symptom", "What it usually means on ridge sand", "Repair"],
          [("A dished area in the middle of a slab", "Base consolidated under a concentrated load", "Lift, or remove and rebuild the base under that panel"),
           ("A step at a construction joint", "Differential consolidation between two pours", "Replace the lower panel with a rebuilt base"),
           ("Apron settled at the street", "Utility trench backfill consolidating", "Replace the apron section to the county detail"),
           ("Cracking radiating from a downspout", "The one place water concentrates on a free-draining lot", "Extend the downspout, then repair"),
           ("Hairline map cracking only", "Surface, not structural", "Seal or resurface"),
           ("Lanai slab cracked at the enclosure footer", "Restrained edge", "Seal; replace only if there is a step")],
          caption="Ridge-sand failures cluster around consolidation rather than saturation, which is the opposite of the pattern in Osceola County."),
    cls="alt")
FAQS["/concrete/repair/davenport/"] = [
    faq("My driveway sank in the middle rather than at the edge. Why?", "On ridge sand that usually means the base consolidated under a concentrated load rather than washing out. The repair is the same: rebuild the base under that panel."),
    faq("Is a 1960s Davenport driveway worth repairing?", "Rarely more than once. At that age on unprepared ridge sand, we price the repair and the replacement together so the choice is made with numbers."),
]

SECTIONS["/concrete/slabs/davenport/"] = sec(
    "Pads on free-draining ground",
    """<p>The good news about a pad on the ridge is that the elevation problem largely goes away. There is no wet-season water table to keep the slab above, so a pad can sit close to grade without standing in water for a third of the year. The bad news is the same base issue as everywhere else in Polk: dry sand that will not compact until it is wetted, under a slab that will carry a concentrated load.</p>
<p>For a shed or an equipment pad that matters less, because the loads are light and spread. For an RV pad, a boat pad or a workshop slab it matters a great deal, because a jack foot or a trailer tongue puts several thousand pounds on a few square inches, and a base that consolidates under it drops that corner. Six inches of concrete at four thousand psi with a number four grid, over base compacted in wetted lifts, is the specification, and it is the same one we use in Osceola for a different reason.</p>""",
    eyebrow="Ridge pads") + sec(
    "Setbacks are the Polk County permit question",
    """<p>Polk County's published guidance is specific: slabs adjacent to a principal or accessory structure, slabs intended to support a structure, elevated slabs, sidewalks and portions of driveways in the right-of-way or within the minimum setbacks require permits, and all slabs have to meet the minimum setbacks from property lines and easements except sidewalks and driveways. Building Code and Land Development Code drainage requirements apply regardless.</p>
<p>What that means in practice on a Davenport lot is that the location of the pad decides whether it is permitted, not its size. A pad against the house or inside a side setback is permitted work; a free-standing pad in the middle of the rear yard usually is not. Easements are the trap, because they are on the plat rather than visible on the ground, and a pad over a drainage or utility easement can be required to come out. We check the plat before we stake anything.</p>""",
    cls="alt")
FAQS["/concrete/slabs/davenport/"] = [
    faq("Does a shed pad need a permit in Polk County?", "It depends on location. A slab adjacent to or supporting a structure, or inside a setback, needs one. A free-standing pad clear of setbacks usually does not, but the drainage rules still apply."),
    faq("Can a pad go over an easement?", "Generally no, and easements do not show on the ground. We check the plat before staking, because a slab over an easement can be required to be removed."),
]
