# -*- coding: utf-8 -*-
"""Final depth pass: index hubs, pricing, comparisons, guides, services, cities and legal pages."""
from _helpers import sec, table, faq

SECTIONS = {}
FAQS = {}


def _add(route, html):
    SECTIONS[route] = SECTIONS.get(route, "") + html


# ============================================================== INDEX HUBS
_add("/guides/", sec(
    "What each guide is for",
    table(["Guide", "Answers", "Written for"],
          [("Why concrete cracks in Osceola County", "Which cracks are cosmetic and which mean the base moved", "Anyone looking at a cracked driveway"),
           ("Rust stains from well-water irrigation", "How to tell rust from tannin, oil and efflorescence, and remove each", "Well-irrigated properties outside the city utility areas"),
           ("Driveway widening rules", "Width caps, the apron, the right-of-way and the parking rules on top", "Anyone adding width in Osceola, Kissimmee or St. Cloud"),
           ("Pouring in the rainy season", "What we do when rain arrives at each stage of a pour", "Anyone scheduling between June and September"),
           ("How to check a contractor before you sign", "Insurance, entity, references, contract and spec", "Everyone getting quotes"),
           ("Vacation rental hardscape", "Turnover scheduling, guest-proof specification and the approval chain", "Owners in the Four Corners and resort corridor"),
           ("Live oak roots and driveways", "Which trees lift slabs and what can be done about it", "Older Kissimmee, St. Cloud and Haines City streets"),
           ("Flatwoods sand versus ridge sand", "Why an Osceola base method fails on the Polk ridge", "Anyone comparing quotes across the county line"),
           ("Buenaventura Lakes driveway replacement", "What is under a 1980s Landstar driveway and what replacement costs", "BVL and the older Poinciana villages"),
           ("Septic drainfields and driveways", "Why concrete over a drainfield shortens its life, and the alternatives", "Rural St. Cloud, Harmony and Narcoossee lots"),
           ("Polymeric sand", "How it is installed, when it fails and when not to use it", "Anyone with a paver field"),
           ("Curing in Florida heat", "What the slab is doing for 28 days and when you can use it", "Anyone who has just had concrete poured"),
           ("Pool deck surface temperature", "What published figures say and how we intend to measure it here", "Anyone choosing a barefoot surface"),
           ("The $7,500 permit exemption", "What the 2026 law covers, what it does not, and how to file", "Anyone planning a small pad or patio")],
          caption="Fourteen guides, each owning one question. Where a guide overlaps a service page, the service page carries the specification and the guide carries the reasoning."),
    eyebrow="Index") + sec(
    "How these are kept current",
    """<p>Permit rules, association criteria and cost figures move, and a guide that was accurate in 2024 can be misleading now. So each of these pages carries a publication date, a last-reviewed date and a line saying what changed at the last update. The permit guides are reviewed whenever a jurisdiction changes a published rule, and all of them are reviewed at least quarterly alongside the Cost Index release.</p>
<p>Where something is genuinely unsettled, such as how individual building departments are implementing the new state permit exemption, the guide says so rather than presenting a snapshot as final. If you find something out of date, the contact form reaches the person who maintains these pages, and corrections go in within two business days with the change noted.</p>""",
    cls="alt"))

_add("/compare/", sec(
    "How to use a comparison page",
    """<p>Each of these pages sets out the real trade-offs between two options that homeowners in this area are genuinely choosing between, with the numbers from the current Cost Index, the climate and soil facts that apply here, and the association angle where one exists. None of them concludes that one option is always right, because none of them is.</p>
<p>What they do instead is name the conditions under which each option wins. Concrete beats pavers on a large area with a tight budget and a well-drained lot; pavers beat concrete on a lot with a drainage history, mature trees or an association palette already built around them. A textured coating beats a paver overlay on a sound deck where budget matters; a paver rebuild beats both where the elevation or the drainage has to change. Reading the conditions and matching them to your lot is the point.</p>""",
    eyebrow="How to read these") + sec(
    "The eight decisions, and which page settles each",
    table(["The decision", "Page", "What usually settles it"],
          [("Concrete or pavers for a driveway", "Concrete vs. pavers", "Budget against repairability, and what the association already approves"),
           ("Travertine or concrete pavers for a pool deck", "Travertine vs. concrete pavers", "Barefoot temperature against cost and acid sensitivity"),
           ("Stamped concrete or pavers for a patio", "Stamped vs. pavers", "Whether you will maintain a sealer every two to three years"),
           ("Resurface or replace a driveway", "Resurface vs. replace", "The tap test, the string line and the hose test"),
           ("Four inches or six", "4-inch vs. 6-inch", "What will actually park on it"),
           ("Rebar, fibre or wire mesh", "Rebar vs. fibre vs. mesh", "Whether the steel can be held at mid-depth at all"),
           ("Textured coating or pavers on a pool deck", "Cool deck vs. pavers", "Whether the slab underneath is sound"),
           ("Which sealer", "Sealer types", "What the surface is made of and whether it has to breathe")],
          caption="Where a decision depends on something only a site visit can establish, the page says so rather than guessing."),
    cls="alt") + sec(
    "Prefer a recommendation to a comparison",
    """<p>The {t} asks eight questions about use, budget, association, heat, trees, drainage, resale and maintenance, and produces a recommendation with the reasoning shown. It runs in your browser and sends nothing to us.</p>
<p>It will not answer the question it cannot answer honestly, which is whether one material adds more resale value than another in this market. We have no local sales data that would support a claim either way, and inventing one would be the easiest thing on this site to get away with and the least defensible.</p>""".format(t='<a href="/tools/concrete-vs-pavers/">decision tool</a>')))

# ================================================================ PRICING
_add("/pricing/", sec(
    "Why we publish prices at all",
    """<p>Most contractors in this market do not publish ranges. The reasoning is understandable: every job is different, a number in public invites a comparison you cannot control, and a competitor can undercut a published figure. We publish anyway, for two reasons.</p>
<p>The first is that homeowners are going to find a number somewhere, and the numbers available are national averages from lead-generation sites that have never seen Osceola County. A local range with a stated method is more useful than a national average with none. The second is that the alternative, where nobody publishes anything, advantages the contractor who is relying on you having nothing to compare against. We would rather compete on what is in the base than on who kept the number hidden longest.</p>""",
    eyebrow="Why") + sec(
    "Reading a range correctly",
    """<p>Every figure on these pages is a range, and the spread is not padding. The low end assumes straightforward access, sound subgrade, a simple rectangular layout, standard material and no surprises. The high end assumes removal of an existing surface, constrained access, borders and cuts, premium material, or a site that needs work before the surface goes down.</p>
<p>Most jobs land in the middle, and the position within the range is decided by things that can be established at a site visit rather than over the phone. The one line we genuinely cannot bracket in advance is structural fill where an old slab has been hiding a washed-out base, which is why it appears as a stated possibility in the proposal rather than as a number.</p>""",
    cls="alt"))

_add("/pricing/concrete/", sec(
    "What changes the concrete price from city to city",
    """<p>The concrete itself costs the same everywhere in our territory. What varies is around it. A Kissimmee or Buenaventura Lakes job frequently needs structural fill once the old slab is up, because the base washed out over forty years. A Celebration or Poinciana job carries an architectural submission and a wait. A St. Cloud rural job carries access questions and sometimes a pump truck. A Davenport or Haines City job needs the ridge base method, which is the same materials with more water and more passes. A Winter Haven or Lake Wales job carries an hour of travel each way.</p>
<p>None of those changes the rate per square foot for the concrete. All of them change the total, which is why we itemise rather than quoting a single blended number that quietly absorbs them.</p>""",
    eyebrow="By city"))

_add("/pricing/pavers/", sec(
    "Where the money goes on a paver job",
    table(["Component", "Roughly what share", "Note"],
          [("Pavers", "35 to 50 percent", "Premium lines and natural stone push this well above half"),
           ("Base material and compaction", "10 to 15 percent", "Six inches in two lifts on a driveway"),
           ("Demolition and haul-off", "10 to 20 percent on a replacement", "Nothing on new ground"),
           ("Installation labour", "20 to 30 percent", "Cutting is the variable; a herringbone with borders costs more than a running bond"),
           ("Edge restraint, bedding sand, polymeric sand", "5 to 8 percent", "Small line, large consequences if skipped"),
           ("Permit, release form, association submission", "2 to 5 percent", "Higher where a board meets monthly"),
           ("Overheads, insurance, warranty reserve", "The balance", "")],
          caption="Approximate shares for a residential paver driveway in this market. The material share is why a premium line changes the total so sharply."),
    eyebrow="Cost structure"))

_add("/pricing/kissimmee-concrete-cost-index/", sec(
    "Reading the table without being misled",
    """<p>Three cautions. A range is not a distribution; the midpoint is not the most likely price, it is just the midpoint. A rate per square foot multiplied by an area is a planning figure and nothing more, because fixed costs do not scale and small jobs carry a minimum. And a figure for an item you have not specified fully, a paver driveway without a material line or a pool deck without coping, is incomplete rather than wrong.</p>
<p>The index is most useful for three things: sanity-checking a quote that seems far outside it, budgeting a project before you are ready for a site visit, and comparing options against each other, where the relative spacing between the lines is more reliable than any single line's absolute value.</p>""",
    eyebrow="Cautions"))

# ============================================================ COMPARISONS
_add("/compare/concrete-vs-pavers/", sec(
    "What the choice looks like on three real lots",
    """<p><strong>A 1985 Buenaventura Lakes driveway.</strong> The old slab has failed because roof water washed the sand from under its edge, and that water is not going anywhere. Concrete costs less and will do the same thing more slowly with a proper base and extended downspouts. Pavers cost more and, when the ground moves again, get lifted and relaid rather than cracked. Either is defensible; the drainage history is the argument for pavers.</p>
<p><strong>A 2019 Haines City driveway that needs widening.</strong> The existing slab is sound. Adding concrete beside it produces a permanent seam and a colour difference. Covering the whole footprint in pavers removes both and costs roughly the same as extending plus resurfacing. Pavers win on appearance rather than on engineering.</p>
<p><strong>A 200-foot rural drive off Nova Road.</strong> Pavers across the whole run multiply the most expensive surface by the largest area on the property. Concrete for the run with a paver apron and turnaround puts each material where it earns its price. Concrete wins on scale.</p>""",
    eyebrow="Three lots"))

_add("/compare/travertine-vs-concrete-pavers/", sec(
    "A decision table for a pool deck",
    table(["If this matters most", "Choose", "Because"],
          [("Barefoot temperature in July", "Light travertine", "Every published comparison puts it well below grey concrete pavers"),
           ("Lowest installed cost", "Concrete pavers", "Roughly $15 to $24 per sq ft against $20 to $36"),
           ("Colour and pattern choice", "Concrete pavers", "Far more sizes, colours and patterns available"),
           ("Resistance to pool chemistry", "Concrete pavers", "Travertine is calcareous and etches with acid"),
           ("Appearance as natural stone", "Travertine", "Because it is"),
           ("Wet grip", "Tumbled travertine or a textured concrete paver", "Both are good; honed or polished anything is not"),
           ("Ease of matching a repair in ten years", "Concrete pavers, if the line is current", "Stone varies by lot, which usually blends anyway"),
           ("Low maintenance", "Concrete pavers", "Joint-stabilising sealer every three to four years against penetrating sealer every two to three")],
          caption="Where two rows conflict, the one at the top of your list wins. Most owners in this market weight temperature and cost above everything else."),
    eyebrow="Decision table"))

_add("/compare/stamped-vs-pavers/", sec(
    "Ten-year ownership, side by side",
    table(["Year", "Stamped concrete patio, 400 sq ft", "Paver patio, 400 sq ft"],
          [("0", "Installed, $4,480 to $7,040", "Installed, $5,200 to $8,400"),
           ("0 to 1", "Cure 28 days, then seal", "Seal and stabilise joints at 60 to 90 days"),
           ("2 to 3", "Re-seal", "Nothing"),
           ("3 to 4", "Nothing", "Clean, re-sand, re-seal"),
           ("5 to 6", "Re-seal", "Nothing"),
           ("7 to 8", "Nothing", "Clean, re-sand, re-seal"),
           ("8 to 10", "Strip and re-seal as the acrylic builds up", "Nothing"),
           ("Any year, if the base moves", "The slab cracks through the pattern", "Units settle; lift, rebuild, relay"),
           ("Any year, if a utility is cut", "Saw-cut and patch; the pattern will not line up", "Lift and relay the field")],
          caption="Maintenance intervals are our field practice for Central Florida sun and rain. Both surfaces last well; they demand attention on different schedules."),
    eyebrow="Over ten years"))

_add("/compare/resurface-vs-replace/", sec(
    "The conversation we have at the door",
    """<p>Homeowners almost always want to hear that resurfacing will work, because it costs about half. So the honest version of this conversation has a shape. We do the three tests in front of you, we show you what a hollow panel sounds like compared with a solid one, and we put the straight edge across the crack so you can see the step yourself rather than taking our word for it.</p>
<p>If it passes, resurfacing is genuinely the better spend and we will say so even though it is the smaller job. If it fails, we explain what will happen to an overlay on a moving slab, in what timeframe, and we price both anyway so the decision is yours with the numbers in front of you. What we will not do is take the resurfacing money on a slab we know is moving, because the second call is worse for everyone than the first honest answer.</p>""",
    eyebrow="In practice"))

_add("/compare/4-inch-vs-6-inch/", sec(
    "The hybrid specification most driveways should have",
    """<p>Almost no residential driveway needs one thickness across its whole area, and specifying a single thickness is either overbuilding the parking area or underbuilding the apron. What we most often propose is four inches through the field where cars sit, six inches at the apron where delivery vehicles and the occasional heavy truck turn in, and six inches with a grid on any pad where a boat, a camper or a trailer will stand.</p>
<p>The cost of that hybrid is modest, because the six-inch sections are a small share of the total area, and it puts the concrete where the loads are. A proposal that quotes four inches everywhere on a property with a boat, or six inches everywhere on a property with two saloon cars, has not asked what will use it.</p>""",
    eyebrow="Practical answer"))

_add("/compare/rebar-vs-fiber-vs-mesh/", sec(
    "What to ask a contractor who specifies mesh",
    """<p>Wire mesh in a four-inch slab is not automatically wrong; mesh correctly chaired at mid-depth does a job. The problem is that a four-inch slab leaves very little room for chairs, mesh and adequate cover on both faces, and the common field practice of hooking the mesh upward during the pour leaves it at random depths, mostly near the bottom.</p>
<p>So the question worth asking is simply how the mesh will be held at mid-depth, and the answer tells you a great deal. A contractor who says chairs at a stated spacing has thought about it. A contractor who says they pull it up as they pour has described the thing that does not work. Our own answer on four-inch work is fibre in the mix plus number four bars at the edges, which sidesteps the problem rather than managing it.</p>""",
    eyebrow="The question to ask"))

_add("/compare/cool-deck-vs-pavers/", sec(
    "Three budgets, three sensible answers",
    """<p><strong>Under $6,000 on a 600 square foot deck.</strong> A textured coating on a sound slab, in a light colour, with grit in the top coat. It renews the surface, improves grip and takes the edge off the heat, and it is the right answer far more often than the industry admits.</p>
<p><strong>$9,000 to $15,000.</strong> A thin paver overlay on a sound slab, or travertine if the barefoot temperature is the priority. This is where most resort-corridor rental decks land, because the surface is part of the product.</p>
<p><strong>Above that, or any budget where the slab has failed.</strong> A full rebuild on a new base, which fixes the elevation and the drainage rather than covering them. Spending the middle budget on a deck that needed the top one is the expensive path, and the three tests on the resurface-versus-replace page tell you which you are in.</p>""",
    eyebrow="By budget"))

_add("/compare/sealer-types/", sec(
    "A quick reference by surface",
    table(["Surface", "Use", "Never use", "Interval here"],
          [("Poured concrete driveway", "Penetrating silane or siloxane, or nothing", "A glossy film in full sun", "5 to 10 years, or never"),
           ("Stamped or coloured concrete", "Solvent-based acrylic with grit outdoors", "Nothing, if you want the colour to last", "2 to 3 years in sun"),
           ("Concrete pavers", "Joint-stabilising acrylic after re-sanding", "A sealer applied over loose joints", "3 to 4 years"),
           ("Travertine and marble", "Penetrating stone sealer", "Any film-forming product; any acid", "2 to 3 years in sun"),
           ("Large-format porcelain", "Usually nothing", "Anything that leaves a film on a non-porous surface", "Not applicable"),
           ("Garage floor", "The coating system's own top coat", "An exterior sealer", "5 to 10 years indoors"),
           ("Textured pool deck coating", "The manufacturer's compatible sealer", "A different brand's acrylic over it", "5 to 8 years")],
          caption="The two rules behind the whole table: stone needs to breathe, and a sealer is maintenance rather than repair."),
    eyebrow="Quick reference"))

# ================================================================= GUIDES
_add("/guides/tree-roots-driveways-central-florida/", sec(
    "What it costs to deal with a root problem",
    table(["Approach", "Rough order", "Buys you", "Risk"],
          [("Grind the lip", "Hourly, a same-week visit", "About a year", "None to the tree"),
           ("Replace the panel only", "Panel rates plus removal", "Two to five years", "Root regrows under the new panel"),
           ("Replace with a root barrier", "Panel rates plus the barrier and trench", "A decade or more", "Trenching cuts roots; arborist opinion needed"),
           ("Reroute the drive around the canopy", "Design change plus additional area", "Indefinite", "Needs room on the lot"),
           ("Build that section in pavers", "Paver rates for that area", "Indefinite, with periodic relaying", "None; relaying is a maintenance visit"),
           ("Remove the tree", "Arborist and tree service", "Indefinite", "Protected trees, permits, and the loss of the tree")],
          caption="Priced separately from the driveway because the right answer depends on the tree, not on the slab."),
    eyebrow="Options and cost"))

_add("/guides/hb-803-permit-exemption/", sec(
    "Where this sits among the other 2026 changes",
    """<p>The exemption did not arrive alone. The same legislative push has been reshaping the relationship between owners, contractors, associations and building departments across Florida, and one other element matters directly for hardscape work: associations may no longer require a building permit before they will carry out an architectural review, which removes a circular problem that used to cost weeks.</p>
<p>The direction of travel is toward fewer procedural gates and more responsibility on the owner and the contractor to build correctly without them. That is a reasonable trade when the contractor is competent and a poor one when they are not, which is precisely why the checking guide on this site exists and why we keep pointing people at insurance, entity registration, references and a written contract.</p>""",
    eyebrow="Context"))

_add("/guides/surface-temperature-pool-decks/", sec(
    "Why we will not publish a number we did not measure",
    """<p>It would be easy to reproduce the figures at the top of this page as if they were ours. Every competitor page we have read does exactly that, and several state them to the degree without saying who measured what, when, with which instrument or in what conditions. A surface temperature reading is meaningless without air temperature, time of day, cloud cover and the instrument's emissivity setting, and none of the widely circulated figures carry any of that.</p>
<p>So this page cites them as published figures from installers and manufacturers, labels them as such, and commits to a measurement protocol we will actually run. When we have our own readings they will replace the citations, with the method, the date, the instrument and the raw numbers published alongside. That is slower than asserting a figure and it is the only version of this page we are willing to put our name on.</p>""",
    eyebrow="A note on method"))

_add("/guides/polymeric-sand-guide/", sec(
    "Cost, coverage and what to budget",
    table(["Item", "Typical figure", "Note"],
          [("Coverage, 1/4 in joints, 60 mm pavers", "About 100 sq ft per 50 lb bag", "Manufacturer charts vary; check the bag"),
           ("Coverage, 1/2 in joints, 80 mm pavers", "About 40 to 50 sq ft per bag", "Wide joints consume far more than people expect"),
           ("Clean, re-sand and seal, installed", "$1.75 to $3.25 per sq ft", "From the current Cost Index"),
           ("Re-sand only on a clean field", "Lower, with a minimum charge", "Rarely worth a separate visit"),
           ("Stripping a failed sealer first", "Adds $0.75 to $1.50 per sq ft", "Chemical, slow, and sometimes unavoidable"),
           ("480 sq ft driveway, clean, re-sand and seal", "$840 to $1,560", "The maintenance visit every three to four years")],
          caption="Coverage figures are the manufacturers'; installed prices are from the current Cost Index."),
    eyebrow="Budgeting"))

_add("/guides/septic-drainfield-concrete-driveway/", sec(
    "Questions to ask before buying a rural lot",
    """<p>This problem is far cheaper to avoid than to solve, and the moment to avoid it is before purchase. Four questions settle most of it. Where are the tank and the drainfield, and is there a permit on file at the county health department showing the layout? Where is the replacement drainfield area, since most permits designate one and building over it is the same mistake in slower motion? Where will the driveway, the parking and any future workshop actually go, and do they clear both? And is the system sized for the house you intend to have rather than the one that is there?</p>
<p>A seller who cannot answer is not necessarily hiding anything; on older rural parcels the records are genuinely thin. But a buyer who does not ask inherits the problem, and the first time it surfaces is usually when the system backs up under a slab that was poured over it.</p>""",
    eyebrow="Before you buy"))

_add("/guides/concrete-curing-florida-heat/", sec(
    "What you can do while it cures",
    table(["Days after the pour", "Do", "Do not"],
          [("0 to 1", "Keep everyone and every pet off it", "Walk on it, water it if a curing compound was applied"),
           ("1 to 3", "Light foot traffic at the edges after 24 to 48 hours", "Put furniture on it, drive on it"),
           ("3 to 7", "Normal foot traffic; light furniture", "Park on it"),
           ("7", "Park cars", "Park a boat, an RV or a loaded truck"),
           ("7 to 28", "Normal use; keep heavy loads off", "Seal decorative work before 28 days"),
           ("28", "Full use; seal stamped and decorative work", "Assume an overlay or sealer can go on a damp slab"),
           ("Any time", "Keep sprinklers off a fresh slab if a curing compound was used", "Add water to the surface to 'help' it cure")],
          caption="The calendar we put on every proposal. Cooler months slow early strength slightly; the 28-day rule for heavy loads does not move."),
    eyebrow="Your part"))

_add("/guides/rainy-season-concrete-scheduling/", sec(
    "What a postponement actually costs",
    """<p>Homeowners sometimes push for a pour to go ahead on a marginal morning because a delay feels like lost time. It is worth knowing what the two options really cost. A postponement is one day, occasionally two if the ground needs to drain, and nothing else changes. A slab finished in the rain can mean a surface that scales and dusts within a year, which is a resurfacing job at half the cost of the original pour, or in a bad case a slab that comes out.</p>
<p>So our default is to move the pour, and we would rather have that argument in the morning than the conversation about scaling eight months later. The forms, the base and the steel keep; the concrete does not.</p>""",
    eyebrow="The trade"))

_add("/guides/driveway-widening-rules-osceola/", sec(
    "Two questions to settle before you design",
    """<p>First, what does the association allow, if there is one. That is the tighter constraint in almost every planned community here, and it is the one that is checked after the fact by neighbours rather than by an inspector. Second, what does the jurisdiction allow, which in unincorporated Osceola County means twenty-four feet without a conditional use and a driveway permit for any construction or widening.</p>
<p>Only then does the design question, how much extra parking do we actually need and where should it go, become answerable. Reversing that order produces designs that have to be redrawn, and occasionally paving that has to come out.</p>""",
    eyebrow="Order of operations"))

_add("/guides/vacation-rental-owner-hardscape-guide/", sec(
    "A pre-season checklist",
    """<p>Before the winter season, when occupancy climbs and gaps disappear, five things are worth checking while there is still a calendar to work with. Walk the entry sequence and look for any lip over a quarter of an inch on the path from the driveway to the front door. Tap the pool deck near the coping for hollow areas. Look at the joints across the paver field and note anywhere the sand has dropped below the chamfer. Check where the downspouts discharge relative to the hardscape edge. And run the irrigation and watch whether any head reaches the deck or the drive.</p>
<p>Four of those five are cheap to fix now and expensive to fix in February. The fifth, the irrigation, is usually a twenty-minute job for a technician and prevents the staining that otherwise reappears every season no matter how often the deck is cleaned.</p>""",
    eyebrow="Checklist"))

# =============================================================== SERVICES
_add("/pavers/artificial-turf/", sec(
    "What turf costs and what it saves",
    table(["Line", "Figure", "Note"],
          [("Installed, typical residential", "Quoted per project", "Material grade and base depth drive it; not in our Cost Index"),
           ("Base preparation", "3 to 4 in compacted", "The same discipline as a paver base"),
           ("Infill", "Per square foot by type", "Pet installations use a different infill"),
           ("Expected life", "10 to 15 years in Florida UV", "Shaded areas last longer"),
           ("Water saved", "The irrigation for that area", "Genuinely significant on a side yard"),
           ("Mowing saved", "All of it for that area", "The usual reason people ask"),
           ("Maintenance still needed", "Rinsing, brushing, occasional infill top-up", "Pet areas need a rinse schedule")],
          caption="Turf is quoted per project rather than carried in the Cost Index, because grade and base vary more than they do in flatwork."),
    eyebrow="Numbers") + sec(
    "Where turf and hardscape meet",
    """<p>The detail that decides whether a turf installation looks deliberate is the edge where it meets concrete or pavers. Turf butted loosely against a slab edge lifts and frays within a season. What works is a bonded edge, either turf trimmed tight and secured to a treated timber or composite edge set flush with the hardscape, or the hardscape itself acting as the restraint with the turf tucked and adhered to it.</p>
<p>Drainage is the other junction. Water that sheds off a driveway onto turf with a compacted base under it has to have somewhere to go, and a turf strip between driveway ribbons sits exactly where the runoff lands. We build those with a more open base and, on flat lots, a collection point, because turf over saturated ground develops an odour and a soft feel that no amount of brushing resolves.</p>""",
    cls="alt"))

_add("/concrete/commercial/", sec(
    "How a commercial quote is put together",
    """<p>A residential quote starts with a measurement. A commercial quote starts with a drawing or, where there is none, a scope discussion with whoever is responsible for the property. What we need before pricing is the intended use and loading, the drawings if they exist, whether a compaction and concrete testing regime is required, the hours work may be performed, whether the area can be closed or has to be phased, and who is responsible for engineering and site drainage.</p>
<p>What comes back is a scope with the thickness, mix, reinforcement and jointing stated, the phasing described, testing and traffic control itemised, and the exclusions listed explicitly. The exclusions matter more on commercial work than residential, because the gap between a flatwork scope and a site scope is where disputes live.</p>""",
    eyebrow="Process") + sec(
    "Working around an operating business",
    """<p>Almost every commercial job we take is on a property that cannot close. A restaurant needs its dumpster accessible, a church needs Sunday, a shopping centre needs its drive lane, an amenity centre needs the pool open for the weekend. So phasing is designed before pricing rather than improvised on site: half the drive lane at a time, the dumpster pad poured with a temporary location arranged, the walkway done in sections with a marked route maintained.</p>
<p>Cure time is the constraint that surprises property managers most. A drive lane panel is not driveable for seven days, which means the phase plan has to account for a week per section rather than a day. Where that is impossible, a high-early mix shortens it at additional cost, and we would rather price that at the start than discover the constraint mid-job.</p>""",
    cls="alt"))

_add("/pavers/outdoor-lighting/", sec(
    "A typical fixture schedule",
    table(["Area", "Fixtures", "Purpose"],
          [("Driveway entry", "2 pillar or column lights", "Marking the entrance from the street"),
           ("Driveway field", "4 to 8 paver lights", "Edge definition rather than illumination"),
           ("Front walk", "4 to 6 path lights or recessed step lights", "Safe footing and approach"),
           ("Entry steps", "1 riser light per step, or 2 per flight", "The single most useful safety lighting on a property"),
           ("Seat wall or planter", "Under-cap lights every 4 to 6 ft", "Washing the surface below"),
           ("Pool deck perimeter", "Under-coping or in-deck lights", "Defining the water edge at night"),
           ("Feature trees", "1 to 2 well lights each", "Uplighting palms and oaks"),
           ("Transformer", "1, sized for the total load plus headroom", "Undersizing it is the common mistake")],
          caption="A representative schedule for a house with a paver driveway, a front walk and a pool deck. Conduit for all of it is placed before the hardscape."),
    eyebrow="Planning") + sec(
    "Why we sleeve even where no light is planned",
    """<p>A conduit sleeve under a driveway or a walk costs very little during construction and is the difference between a future addition being a half-day job and a demolition. So we run sleeves at every hardscape crossing on any job where lighting is even a possibility, and we photograph and mark the ends so they can be found later.</p>
<p>The same logic applies to irrigation crossings, low-voltage runs for a future gate, and the conduit for a summer kitchen that is two years away. None of it is visible in the finished job and all of it is expensive to retrofit. It is the kind of thing that separates a contractor thinking about the next ten years on the property from one thinking about this week's invoice.</p>""",
    cls="alt"))

_add("/concrete/architectural/", sec(
    "Working with an architect or a designer",
    """<p>Most architectural concrete work reaches us through a designer or an architect rather than directly from an owner, and the projects that go well share a pattern. The finish is specified early enough to affect the mix and the formwork rather than being chosen after the slab is designed. A sample panel is built and approved before anything is formed. The tolerance expectation is written down, because concrete flatness and colour tolerances are real and a drawing that implies tile-like precision is setting up a dispute. And someone has decided who owns the sealing, because the finish and the sealer are one system and a sealer chosen later can change the appearance entirely.</p>
<p>Where a designer has not specified a mix, we will propose one and say what it will and will not do. Where a drawing calls for something the material cannot deliver, a joint-free thirty-foot expanse of coloured concrete, for example, we say so at the drawing stage rather than at the pour.</p>""",
    eyebrow="Collaboration"))

_add("/pavers/marble-porcelain/", sec(
    "Three ways to set large-format units",
    table(["Method", "How", "Suits", "Limits"],
          [("Sand-set", "Compacted base, bedding course, joints sanded", "Thick marble and stone pavers on grade", "Not for 2 cm porcelain; too thin to bed"),
           ("Thin-set on concrete", "Bonded to a sound, flat slab with the correct mortar", "Porcelain and thin stone over an existing deck", "The slab has to be sound and flat; tolerance is tight"),
           ("Pedestal system", "Units sit on adjustable pedestals over a drained surface", "Roof decks, over-membrane installations, precise levels", "Height build-up; edges need detailing"),
           ("Open-joint gravel set", "Units on a compacted open-graded base with gravel joints", "Contemporary garden paths and patios", "Not for vehicle loads")],
          caption="The method is chosen by the substrate and the unit thickness, not by preference. Getting it wrong produces cracked units rather than settled ones."),
    eyebrow="Installation methods"))

_add("/concrete/resurfacing/", sec(
    "What an overlay will not hide",
    """<p>Worth being explicit, because the marketing for these systems implies otherwise. An overlay will not hide a crack that moves; it will crack along the same line, usually within a season. It will not hide a step between panels, because it is a quarter of an inch thick and the step is not. It will not hide a hollow area, which will sound hollow afterwards and will eventually break through. It will not fix drainage, because it follows the existing slope. And it will not fix a slab that is failing from below, which on Osceola sand is most of the slabs people ask us to resurface.</p>
<p>What it does beautifully is renew a sound but tired surface, change the colour and texture, and cover a slab that is stained, spalled or scarred by a previous coating. On the right slab it is one of the best value jobs in flatwork. On the wrong slab it is the most expensive mistake available.</p>""",
    eyebrow="Honest limits"))

_add("/pavers/retaining-walls-outdoor-living/", sec(
    "What an outdoor kitchen needs from us before the appliances arrive",
    """<p>The structure, the surface and the services, in that order. The structure is a block or paver-faced frame on a footing sized for the load, built to the appliance manufacturer's cut-out dimensions rather than to a generic drawing, with ventilation where a built-in grill requires it. The surface is the counter, cast concrete, stone or porcelain, with the overhang and the edge profile decided early because they affect the frame.</p>
<p>The services are gas, electrical and sometimes water, all of which are licensed trades we coordinate rather than perform, and all of which need their runs placed before the structure is closed. The most common sequencing failure on these projects is a finished kitchen with no way to get a gas line into it, and the fix at that point is opening the structure back up.</p>""",
    eyebrow="Sequencing"))

_add("/coatings/garage-floors/", sec(
    "What to move, and what we move",
    """<p>The garage has to be empty, and the practical question is where the contents go for two days. On most jobs the owner clears it into the driveway under a tarp, which works in the dry season and is uncomfortable in August. We can arrange a container on site for a day where that is easier, and we say so at the estimate rather than leaving it as your problem.</p>
<p>Two things need particular attention. Anything stored on the floor that cannot get dusty should leave entirely, because grinding produces fine dust even with vacuum extraction. And the water heater, the electrical panel and any wall-mounted equipment stay in place, with the floor coated up to and around them, which is why the cove detail at the wall is part of the specification rather than an extra.</p>""",
    eyebrow="Before we start"))

_add("/concrete/sidewalks-walkways/", sec(
    "Right-of-way sidewalk work, which is its own thing",
    """<p>The sidewalk crossing your frontage belongs to the jurisdiction even though you maintain the grass either side of it, and replacing a panel in it is a different job from replacing your private walk. It follows the jurisdiction's detail for thickness, mix, width, cross-slope and jointing, it has to meet accessibility requirements for slope and surface, and it needs the right-of-way approval before any saw touches it.</p>
<p>Orange County's published detail, for example, requires a minimum width for longitudinal driveway cuts and restoration consistent with the applicable accessibility standards. Inside Kissimmee it goes through the Engineering Division's application. In unincorporated Osceola it falls under the right-of-way provisions of the Land Development Code. We handle the approval as part of the job and price the sidewalk section separately from the private walk, because the two are built to different requirements.</p>""",
    eyebrow="Public sidewalk"))

_add("/pavers/travertine/", sec(
    "Buying travertine without surprises",
    """<p>Three things to settle before the order goes in. The grade, because the difference between a premium and a commercial grade is the number of voids and the width of the colour range, and both are visible on a large deck. The finish, tumbled for grip around a pool, and whether it is filled or unfilled, since fills can pop out and need attention. And the lot, because natural stone varies between quarry lots and a deck finished from two lots can show a line where they meet.</p>
<p>We order the whole deck from one lot where the quantity allows it, and where it does not we blend across the field rather than working from one pallet at a time, which is the same technique that makes a paver repair disappear. Special-order sizes and premium grades add two to four weeks of lead time, which is worth knowing when a project is being scheduled around a season.</p>""",
    eyebrow="Ordering"))

_add("/concrete/stamped/", sec(
    "A realistic timeline for a stamped patio",
    """<p>Day one is demolition where there is something to remove, then base and forms. Day two is the pour, and it is a longer day than a plain slab: place, screed, float, apply the colour hardener or verify the integral colour, broadcast the release, stamp in sections before the set catches up, and detail the edges by hand. In a Kissimmee summer that work happens between first light and late morning, because the window between finishing and set is short.</p>
<p>Day three is washing off the release and tooling the joints. Then the slab cures for twenty-eight days before it is sealed, which means a return visit roughly a month later. Owners are often surprised that the job is not finished when the crew leaves, and the sealing visit is the moment the colour actually appears, since the release residue leaves the surface looking dusty and flat until then.</p>""",
    eyebrow="Timeline"))

# ================================================================= CITIES
_add("/areas/dundee/", sec(
    "What a job here looks like in practice",
    """<p>A Dundee project runs as a block rather than as a series of visits. We mobilise, work consecutive days and finish, because splitting a job at this distance across non-consecutive days doubles the travel for no benefit. That shapes what we take on: driveways, paver fields, pool decks and substantial patios, rather than single panel repairs.</p>
<p>The other practical note is supply. Ready-mix for this part of the ridge comes from Polk County plants rather than the Orlando-area plants that serve our Osceola work, and the delivered price differs slightly as a result. It is a small line, and we price from the plant that will actually serve the site rather than from a blended average.</p>""",
    eyebrow="How we work here"))

_add("/areas/lake-alfred/", sec(
    "The permitting advantage of being here",
    """<p>Polk County's Northeast Government Center is in Lake Alfred, which makes this one of the easier parts of the unincorporated county to permit in: submissions, questions and inspections are handled from an office in the town rather than from Bartow. For a homeowner that mostly means faster answers when something needs clarifying mid-job.</p>
<p>The substantive rules are the county's rules and do not change: permits for slabs adjacent to or supporting a structure, elevated slabs, sidewalks and the portions of driveways in the right-of-way or within setbacks, all slabs meeting setbacks from property lines and easements, and the recorded release form where pavers occupy the right-of-way.</p>""",
    eyebrow="Local office"))

_add("/areas/auburndale/", sec(
    "Reading the lot before quoting",
    """<p>Auburndale sits where the ridge meets the lake flats, and on a given street the soil can change within a few hundred feet. That matters because the two conditions need opposite base methods: ridge sand has to be wetted to compact at all, while flatwoods soils in the low ground need the subgrade proof-rolled and sometimes raised. Quoting one method across a town like this is how a base gets built wrong.</p>
<p>So we look up the USDA map unit for the parcel before the visit and probe on site to confirm it. It takes a few minutes and it changes the specification, which is the sort of thing that does not show up in a price comparison and shows up clearly in year three.</p>""",
    eyebrow="Soil check"))

_add("/areas/lake-wales/", sec(
    "At the edge of the service area, honestly",
    """<p>Lake Wales is the furthest point we cover regularly, about twenty-eight miles and the better part of an hour from our base. We are straightforward about what that means. Multi-day jobs work well and we quote them competitively. Half-day jobs do not, and rather than build two hours of travel into a small price we will say so and suggest you find someone closer.</p>
<p>Where we do work here, the specification and the standards are identical to a Kissimmee job, adjusted for ridge sand. What changes is scheduling: we commit to consecutive days rather than fitting the job around closer work, and we confirm material delivery from the Polk plants before the start date rather than on the morning.</p>""",
    eyebrow="Scope"))

_add("/areas/polk-city/", sec(
    "What we would tell a neighbour",
    """<p>If you are in Polk City and the job is a driveway, a paver field or a pool deck, call us and we will quote it properly. If it is a cracked panel, a shed pad or a trip hazard, you will get better value from a crew based in Lakeland or Winter Haven, and we will say so rather than pricing an hour of travel each way into a half-day job.</p>
<p>That is not modesty; it is how the numbers work. A crew travelling two hours for a three-hour job has spent most of the day on the road, and someone pays for that. We would rather be the people who told you than the people who quoted it.</p>""",
    eyebrow="Straight answer"))

_add("/areas/winter-haven/", sec(
    "Which plant, which office, which soil",
    """<p>Three practical facts for a Winter Haven job. Ready-mix comes from Polk County plants, which is a slightly different delivered price from our Osceola work and is priced from the actual plant. Permitting is the City of Winter Haven inside the limits and Polk County outside, and the boundary is not obvious in the areas that have grown outward. And the soil depends on whether the lot is on the ridge or in the lake flats, which changes the base method.</p>
<p>None of those is complicated, and all three are worth establishing before a number is given. A quote that has not identified the plant, the permitting office or the soil condition has been produced from a template rather than from the site.</p>""",
    eyebrow="Three checks"))

_add("/areas/polk-county/", sec(
    "Working across a county line, week to week",
    """<p>Roughly a third of our work is on the Polk side, and the two counties genuinely need different habits rather than the same habits applied with a different letterhead. The base method changes, because ridge sand behaves the opposite way to flatwoods sand. The permitting logic changes, from Osceola's activity-based rules to Polk's location-based ones. The paperwork changes, because of the recorded paver release form. And the plants change, which affects the delivered price of concrete.</p>
<p>Crews that work both sides know this. Crews that work one side and take an occasional job on the other often do not, and the tell is a proposal for a Davenport job that reads word for word like one for Kissimmee. It is worth asking any contractor quoting on the ridge how they will compact the base, and listening for whether the answer mentions water.</p>""",
    eyebrow="Practice"))

_add("/areas/orange-county-south/", sec(
    "What we take on this side of the line",
    """<p>South Orange work comes to us mostly by referral from customers who have moved, or from people who live in Hunters Creek, Meadow Woods or Southchase and found this site looking for Osceola information. We are glad to quote it: these communities are fifteen to twenty-five minutes from our base, closer than several places we serve regularly.</p>
<p>What we do not do is publish a page for every south Orange community and compete with our own sister brands for the same customer. The pages here cover the rules and the ground conditions, and if you want the work done you can call. That is a deliberate choice about how many pages this site should have, and it is the same reason there is no page here for Windermere, Winter Garden or Lake Nona.</p>""",
    eyebrow="Coverage") + sec(
    "The permit difference, worked through",
    table(["Project", "Unincorporated Osceola", "Unincorporated Orange"],
          [("Detached rear patio slab, outside setbacks", "Generally flatwork; confirm scope", "Permit required"),
           ("Paver patio", "Generally flatwork", "Permit plus a Zoning permit"),
           ("New driveway", "County driveway permit; 24 ft cap", "Permit; 6 in / 3,000 psi apron with no steel, 3 ft from the property line"),
           ("Shed pad", "Shed permitted; pad inspected with it", "Permit application for the structure"),
           ("Pool deck overlay", "Flatwork unless tied to the structure", "Permit required"),
           ("Repair in the same footprint", "No permit", "Minor repairs generally exempt")],
          caption="The same project can be unpermitted flatwork on one side of the county line and a permitted job on the other. This is the single most common source of confusion for customers who move between the two."),
    cls="alt"))

# ============================================================== LEGAL PAGES
_add("/accessibility/", sec(
    "What we have actually done",
    """<p>Semantic headings in a logical order on every page, with one first-level heading per page. Landmarks for the header, navigation, main content and footer, and a skip link to the main content. Every form field with a visible label tied to it. A visible focus outline with a contrast ratio that meets the requirement, rather than the browser default removed. Text contrast checked against the palette, with the gold used at a darker value for small text than for large. Touch targets of at least forty-four pixels on buttons and links in the mobile layout. Tables with header cells marked as headers. Images with alt text that describes the image, and concept renderings identified as renderings in the alt text rather than only in the caption.</p>
<p>Motion is minimal by design, and what there is respects the reduced-motion preference. The site works without JavaScript for reading; the calculators and the finder need it, and they say so.</p>""",
    eyebrow="Implementation") + sec(
    "Where we know it falls short",
    """<p>The permit finder depends on an external geocoding service, and when that service is unavailable the tool degrades to a ZIP-based answer with a notice rather than failing silently. That is a graceful fallback rather than a fix. The interactive tools produce results that are announced to screen readers, but they have not yet been tested with a range of assistive technologies by anyone other than us, so we describe them as intended to work rather than verified to.</p>
<p>We have not commissioned an independent accessibility audit. When we do, the findings and what we changed will go on this page. Until then, if something on this site is difficult or impossible for you to use, the contact form reaches us and we will fix confirmed barriers in the next release rather than adding them to a list.</p>""",
    cls="alt"))

_add("/terms/", sec(
    "The parts people actually need to know",
    """<p>Prices on this site are planning ranges with a published method, not offers. Nothing here creates a contract; work is done under a written agreement that states the scope, specification, price, schedule, payment terms and warranty, and that agreement controls over anything on this site if the two ever differ.</p>
<p>Permit and association rules are quoted from official sources as of the date shown on each page. They change, sometimes without notice, and the office or the association is always the authority rather than us. The tools are planning aids that run in your browser; they can be wrong for an unusual lot, an address near a boundary or a project outside their stated assumptions, and they should not be used to order material or to decide that a permit is unnecessary.</p>
<p>The Cost Index data is licensed for reuse under Creative Commons Attribution 4.0, with attribution and the release date kept attached. Everything else on the site, including the photographs, the guides and the tools, is ours. Concept renderings are labelled as renderings and may not be presented anywhere as photographs of completed work.</p>""",
    eyebrow="In short"))

_add("/privacy/", sec(
    "What the tools do and do not send",
    """<p>Worth separating, because it is the question we are asked most about this site. The estimate form sends what you type to our estimating inbox. Nothing else on the site sends anything to us.</p>
<p>The concrete and paver calculator, the decision tool, the packet checklist, the pour calendar and the project brief generator all run entirely in your browser; the numbers you enter never leave your device. The permit finder sends the address you type to the U.S. Census Bureau's public geocoding service to turn it into coordinates, and that request goes from your browser to the Census Bureau directly rather than through us. We do not receive it, log it or store it.</p>
<p>We use Cloudflare Web Analytics, which does not set cookies and does not collect personal data. Cloudflare Turnstile, which checks that a form sender is a person, may set a cookie for that purpose. If we ever add an analytics product that does more than that, this page will change before it goes live and a consent notice will appear where the law requires one.</p>""",
    eyebrow="Tools and data"))

_add("/permits/orange-county/", sec(
    "If you are moving between counties",
    """<p>The most common confusion we deal with is a homeowner who has done this before in another county and assumes the rules travel. They do not. Someone who poured a patio in unincorporated Osceola without a building permit, entirely correctly, and then does the same thing after moving to unincorporated Orange has built without a permit. The reverse also happens, where someone assumes a permit is needed for a rear patio in Osceola because it was in Orange.</p>
<p>Neither person did anything unreasonable. The rules simply differ by jurisdiction in a way that is invisible from the street, which is the entire reason the finder and these jurisdiction pages exist.</p>""",
    eyebrow="A common mistake"))
