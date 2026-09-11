# -*- coding: utf-8 -*-
"""Extra depth for pricing, FAQ, HOA, permit, tool and institutional pages."""
from _helpers import sec, table, faq

SECTIONS = {}
FAQS = {}

# ---------------------------------------------------------------- PRICING
SECTIONS["/pricing/"] = sec(
    "What actually moves a price in this market",
    table(["Factor", "Effect on the number", "Why"],
          [("Removing an existing surface", "Adds $2.00 to $4.00 per sq ft", "Breaking, loading and tipping is a day and a truck"),
           ("Job size under about 200 sq ft", "Pushes to the top of every range", "Truck minimum, short-load fee and a crew day are fixed"),
           ("Access a machine cannot reach", "Adds 15 to 30 percent on excavation", "Hand work and wheelbarrows instead of a skid steer"),
           ("Structural fill where the base has washed out", "Quoted after the slab is up", "Nobody can see it until the old surface is gone"),
           ("Borders, bands and curves in a paver field", "Adds 8 to 18 percent in waste and cutting", "Every perimeter unit is a cut"),
           ("Six inches and a rebar grid instead of four", "About $3.00 per sq ft", "Half again the concrete, plus steel and chairs"),
           ("Premium paver or natural stone", "Doubles the material line", "Material is 35 to 50 percent of a paver job"),
           ("Drainage work", "Priced separately and itemised", "A channel drain, a dry well or a swale is its own scope"),
           ("Permit and notice of commencement", "A few hundred dollars", "Fee plus filing and inspection time"),
           ("Spring scheduling, March to May", "No price change, longer lead time", "Paver demand peaks in April and May every year")],
          caption="These are the lines that make two quotes for nominally the same job differ. A quote that shows none of them is hiding them, not avoiding them."),
    eyebrow="Cost drivers") + sec(
    "How to compare three quotes properly",
    """<p>Square-foot price is close to useless as a comparison unless the specification behind it is the same, and it usually is not. The three numbers we would put side by side instead are base depth and material, slab thickness with mix strength and reinforcement, and what the quote says about drainage. Those three account for most of the variation in this market, and all three are invisible once the job is finished.</p>
<p>A worked example. Two quotes for a 480 square foot driveway, one at $4,300 and one at $5,900. The cheaper one is four inches of three thousand psi on two inches of sand with wire mesh; the dearer one is four inches of three thousand five hundred psi with fibre and edge bars on four inches of compacted limerock, with the downspouts extended and joints cut at ten feet. That is not a thirty percent price difference for the same thing. Our {pb} produces a one-page specification you can hand to every bidder so they are pricing the same job.</p>""".format(pb='<a href="/tools/project-brief/">project brief tool</a>'),
    cls="alt") + sec(
    "What we will not quote over the phone",
    """<p>We will give a range over the phone all day, because the ranges are published here anyway. What we will not do is give a firm number without seeing the site, and the reason is the list above: nobody can price structural fill, access, drainage or what is under an existing slab from a description.</p>
<p>The pattern we see most is a homeowner with three phone quotes, two of which are lower than ours and neither of which mentions base, and then a change order on day two when the old slab comes up. A written proposal after a site visit is slower and it is the only way the number at the top means anything at the end.</p>""")

SECTIONS["/pricing/concrete/"] = sec(
    "Worked examples on real footprints",
    table(["Project", "Size", "Assumptions", "Planning range"],
          [("Two-car driveway replacement", "20 by 24 ft, 480 sq ft", "Remove old slab, 4 in base, 4 in slab", "$5,040 to $8,400"),
           ("Two-car driveway, new pour on bare ground", "480 sq ft", "No removal", "$4,080 to $6,480"),
           ("Driveway widened by 8 ft", "8 by 40 ft, 320 sq ft", "New pour beside existing, matched finish", "$2,720 to $4,320"),
           ("Twelve by twelve patio", "144 sq ft", "4 in, broom, small pour", "$1,300 to $1,900"),
           ("Sixteen by twenty patio", "320 sq ft", "4 in, broom", "$2,560 to $4,000"),
           ("Stamped patio", "320 sq ft", "Integral plus release colour, sealed", "$4,480 to $7,040"),
           ("Front walk", "4 by 40 ft, 160 sq ft", "4 in, broom, joints at 4 ft", "$1,400 to $2,100"),
           ("Shed pad", "10 by 12 ft, 120 sq ft", "4 in, raised above grade", "$1,200 to $1,900"),
           ("RV pad", "12 by 40 ft, 480 sq ft", "6 in, 4,000 psi, rebar grid", "$6,500 to $9,500"),
           ("Pool deck replacement", "600 sq ft", "Remove and re-pour, textured finish", "$6,000 to $9,900"),
           ("Driveway resurfacing", "480 sq ft", "Sound slab, textured overlay", "$2,400 to $4,560")],
          caption="Current Cost Index rates applied to footprints we quote regularly. Structural fill, drainage work, permits and access constraints are separate lines. None of these is a quote."),
    eyebrow="By project") + sec(
    "Where the money goes on a concrete driveway",
    table(["Component", "Roughly what share", "Note"],
          [("Ready-mix concrete", "20 to 30 percent", "About one cubic yard per 81 sq ft at 4 inches"),
           ("Demolition and haul-off", "15 to 25 percent on a replacement", "Nothing on a new pour"),
           ("Base material and compaction", "10 to 15 percent", "The line that gets cut in a cheap quote"),
           ("Forming and finishing labour", "25 to 35 percent", "A crew day whether the slab is 300 or 600 sq ft"),
           ("Steel, fibre and chairs", "3 to 8 percent", "Higher on a 6-inch grid"),
           ("Permit, notice of commencement, inspections", "3 to 6 percent", "Fixed cost, proportionally heavy on small jobs"),
           ("Overheads, insurance, warranty reserve", "The balance", "What makes the warranty mean something")],
          caption="Approximate shares for a typical residential replacement in this market. They explain why small jobs cost more per square foot and why the cheapest quote is usually cheap in the base line."),
    cls="alt")

SECTIONS["/pricing/pavers/"] = sec(
    "Worked examples on real footprints",
    table(["Project", "Size", "Assumptions", "Planning range"],
          [("Paver driveway, standard concrete paver", "480 sq ft", "Remove old slab, 6 in base, 80 mm pavers", "$7,680 to $12,480"),
           ("Paver driveway, premium line", "480 sq ft", "Same, premium material", "$10,560 to $17,280"),
           ("Paver patio", "320 sq ft", "4 to 5 in base, 60 mm pavers", "$4,160 to $6,720"),
           ("Paver pool deck overlay", "600 sq ft", "Thin pavers over a sound deck, coping separate", "$9,000 to $14,400"),
           ("Travertine pool deck", "600 sq ft", "Tumbled travertine, penetrating sealer", "$12,000 to $21,600"),
           ("Paver walkway", "4 by 40 ft, 160 sq ft", "Narrow run, border course", "$2,240 to $3,840"),
           ("Clean, re-sand and seal a driveway", "480 sq ft", "Polymeric sand, joint-stabilising sealer", "$840 to $1,560"),
           ("Lift and relay a settled area", "80 sq ft", "Base rebuilt, same pavers reset", "$720 to $1,280 with a minimum charge"),
           ("Paver apron only", "12 by 20 ft, 240 sq ft", "At the right-of-way, concrete edge restraint", "$3,360 to $5,280")],
          caption="Current Cost Index rates on footprints we quote regularly. Coping, drainage, lighting conduit and permits are itemised separately. None of these is a quote."),
    eyebrow="By project") + sec(
    "What changes the paver price from community to community",
    """<p>The material and the base are the same across our territory. What changes is everything around them. A Celebration or Poinciana job carries an architectural submission and a wait for a committee. A Polk-side job with pavers in the right-of-way carries a notarised, recorded release form. A resort-community job in Four Corners or Reunion carries a booking calendar and a management company. A Harmony or rural St. Cloud job carries access questions and a longer haul. A Buenaventura Lakes job carries structural fill that cannot be quantified until the old slab is up.</p>
<p>None of those is a large line on its own and together they are why the same nominal driveway prices differently in two communities twelve miles apart. We itemise them rather than folding them into a square-foot rate, so the comparison with another quote is on something real.</p>""",
    cls="alt")

SECTIONS["/pricing/kissimmee-concrete-cost-index/"] = sec(
    "How to cite and reuse this index",
    """<p>The index is published under a Creative Commons Attribution 4.0 licence, which means anyone may reproduce, adapt and republish it, including commercially, provided attribution is given. If you are a Realtor putting a cost slide in a listing presentation, a property manager budgeting a portfolio, a journalist writing about construction costs in Osceola County or another contractor who wants a reference point, you are welcome to use it.</p>
<p>Attribution we ask for: Kissimmee Concrete Cost Index, with the release label and a link to this page. The machine-readable copies are at <a href="/api/cost-index.json">/api/cost-index.json</a> and <a href="/api/cost-index.csv">/api/cost-index.csv</a>, both of which carry the release, the date and the licence in the payload so a reuse cannot accidentally drop the vintage. If you republish it, please keep the release date attached, because a two-year-old construction cost figure presented as current is worse than no figure.</p>""",
    eyebrow="Licence and reuse") + sec(
    "What this index is not",
    """<p>It is not a quote, and no line in it should be read as one. It is not a survey of what other contractors charge, because we have not surveyed them. It is not a claim about the cheapest or the most expensive price available in this market. It is not adjusted for the busiest weeks of spring, when crew availability tightens across the trade. And it does not include sales tax where it applies, financing charges, association fees or the cost of anything discovered under an existing surface.</p>
<p>It is a market composite built from three inputs: current supplier pricing, published regional cost references, and our own takeoffs for standard job sizes, assembled for the Kissimmee and Osceola County market and stated as a range with the assumptions written down. The full method, including what changes in the next release, is on our <a href="/data-and-methods/">data and methods</a> page.</p>""",
    cls="alt") + sec(
    "How the next release will differ",
    """<p>The current release is a composite rather than a sample of executed contracts, and we have said so in the method note rather than implying otherwise. From the next release onward, anonymised executed quotes will be added to the sample, recorded as service, city, square footage, price and date, with no customer-identifying information. The release note will state the count behind each line.</p>
<p>Items with fewer than five quotes behind them will stay labelled as market composite rather than being presented as a measured range, because five is already a thin sample and pretending otherwise would make the index less useful, not more. Releases are quarterly. Anyone who wants to be told when a release is published can ask through the contact form; there is no mailing list yet.</p>""")

# -------------------------------------------------------------------- FAQ
SECTIONS["/faq/"] = sec(
    "The five questions we are asked before any others",
    """<p><strong>What will it cost?</strong> Ranges for every service are published on this site with the method behind them, because a contractor who will not put a range in public is usually relying on you having nothing to compare against. Your number comes from a site visit.</p>
<p><strong>Do I need a permit?</strong> It depends which side of a municipal line your address is on, and in this county that is genuinely hard to tell from the street. The finder resolves it, and each jurisdiction page quotes the rule with its source.</p>
<p><strong>Are you licensed?</strong> Florida does not license concrete flatwork, pavers or stucco, and since 2023 counties and cities may not require a local licence for driveway installation or decorative stone and paver work either. So there is no number to show. Insurance, entity registration and a written contract are what can be checked, and the guide explains how.</p>
<p><strong>How long will it take?</strong> Two to three days on site for a typical driveway, three to five for pavers, plus permit and association time in front of it and cure time behind it.</p>
<p><strong>When can I use it?</strong> Foot traffic in a day or two, cars at seven days, boats and RVs at twenty-eight. Pavers are usable as soon as the joints are sanded and compacted.</p>""",
    eyebrow="Start here") + sec(
    "Where the rest of the answers live",
    table(["If you are asking about", "Go to"],
          [("Cost of a specific job", "The concrete and paver cost guides, and the Cost Index for the method"),
           ("Whether you need a permit", "The permit hub and the jurisdiction page for your address"),
           ("What your association will require", "The HOA guides and the packet checklist"),
           ("Cracks, sinking, stains or failures", "The repair pages and the guides"),
           ("Which material to choose", "The comparisons and the decision tool"),
           ("Thickness, strength, base and joints", "The service page for that job"),
           ("Timing around rain and hurricane season", "The pour calendar and the rainy-season guide"),
           ("How to check any contractor", "The contractor verification guide")],
          caption="Every question on this site has one page that owns the answer; the others link to it rather than repeating it."),
    cls="alt")

SECTIONS["/faq/concrete/"] = sec(
    "Questions about the concrete itself",
    """<p><strong>What is the difference between cement and concrete?</strong> Cement is the powder that binds; concrete is the finished material of cement, water, sand and stone. Nobody pours a cement driveway, though almost everybody calls it that, and we know what you mean.</p>
<p><strong>Why is my new slab a different colour in places?</strong> Usually uneven curing, sometimes plastic sheeting touching the surface, sometimes a difference between two truckloads. Most of it evens out over the first year.</p>
<p><strong>Why does new concrete look blotchy after rain?</strong> Moisture moves through the slab unevenly as it cures, so the surface dries in patches for the first few weeks. It is not a defect.</p>
<p><strong>Can concrete be poured in winter here?</strong> Easily. Central Florida rarely gets cold enough to matter, and the cooler months are the best pouring season because there are six or seven rain days a month instead of sixteen.</p>
<p><strong>What is efflorescence?</strong> Soluble salts moving to the surface and crystallising, which looks like a white haze. On new concrete it usually weathers off; on pavers it is common in the first wet season and is cleaned before sealing.</p>""",
    eyebrow="Material") + sec(
    "Questions about living with it",
    """<p><strong>Should I seal a plain concrete driveway?</strong> Not necessarily. A penetrating sealer helps with stain resistance and makes rust and oil easier to remove later, but plain broom-finish concrete is perfectly serviceable unsealed.</p>
<p><strong>How do I clean it?</strong> A surface cleaner at moderate pressure and the right chemistry for the stain. Identify the stain first, because rust, tannin, oil and efflorescence each need a different product and using the wrong one can set the stain.</p>
<p><strong>Does homeowners insurance cover a cracked driveway?</strong> Usually not for settling, roots or wear. Sudden damage from a covered event sometimes is. We provide photographs and a written assessment for a claim.</p>
<p><strong>How long does a concrete driveway last here?</strong> Twenty-five years and more when the base was built and the water is managed. The 1980s slabs we replace across Buenaventura Lakes and Poinciana had neither.</p>
<p><strong>Can I add a section myself and have you do the rest?</strong> We would rather not split a slab between two crews, because the joint between them is where the argument lands if anything moves.</p>""",
    cls="alt")

SECTIONS["/faq/pavers/"] = sec(
    "Questions about the system",
    """<p><strong>What is the difference between a brick and a paver?</strong> A clay brick is fired clay; a concrete paver is moulded concrete with pigment. Clay holds its colour indefinitely and comes in fewer shapes; concrete offers far more sizes, colours and patterns and softens in colour over years.</p>
<p><strong>What thickness do I need?</strong> Sixty millimetres for patios and walkways, eighty for driveways and anywhere a vehicle can reach. On rental properties we use eighty everywhere.</p>
<p><strong>What holds the edge?</strong> An edge restraint, either a poured concrete haunch or a spiked aluminium profile, buried so it does not show. Without it the outside course rolls outward and the field loses its interlock.</p>
<p><strong>Why herringbone on a driveway?</strong> Because no continuous joint line runs in the direction a turning tyre pushes, so the field resists the load better than a running bond.</p>
<p><strong>Do pavers need a concrete base?</strong> No. They need a compacted aggregate base and a bedding course. Pavers set in mortar on a slab are a different, rigid system with different failure modes.</p>""",
    eyebrow="System") + sec(
    "Questions about keeping them",
    """<p><strong>How often do joints need re-sanding?</strong> Every three to five years on a driveway in this climate, sooner if the field is pressure washed often or a downspout crosses it.</p>
<p><strong>Why are there ants?</strong> Loose or missing joint sand gives them somewhere to tunnel. Cleaning the joints to depth and filling with polymeric sand closes it.</p>
<p><strong>What about weeds?</strong> Same cause. Seed germinates in open joints; a properly filled and cured polymeric joint gives it nothing.</p>
<p><strong>Can I pressure wash them?</strong> At moderate pressure with a surface cleaner, yes. A turbo nozzle at three thousand psi excavates the joints and erodes the paver face.</p>
<p><strong>Will the colour fade?</strong> Concrete pavers soften over years rather than fading unevenly, which is why a repair blended through a field disappears and a solid patch does not. Clay brick holds its colour.</p>
<p><strong>What if my paver is discontinued?</strong> We lift units from a hidden area for the visible repair and blend a current product into the donor area. It is the standard answer to a fifteen-year-old field.</p>""",
    cls="alt")

SECTIONS["/faq/permits-hoa/"] = sec(
    "Permits, plainly",
    """<p><strong>Who pulls it?</strong> We do, as the contractor. You sign the application, and in Osceola County on jobs of five thousand dollars or more you also sign a notice of commencement that is recorded at the courthouse before the first inspection.</p>
<p><strong>How long does it take?</strong> Osceola residential plan review is normally three to five days. The City of Kissimmee's driveway application takes at least two business days to review and at least two more to issue after payment. St. Cloud and Polk vary by scope.</p>
<p><strong>What does it cost?</strong> A few hundred dollars for residential flatwork in our jurisdictions, itemised in the proposal rather than buried.</p>
<p><strong>What happens if work is done without one?</strong> It surfaces at resale, when a title search or a buyer's inspector finds unpermitted work, and resolving it afterwards costs more than the permit would have. We do not take jobs on the basis of skipping it.</p>
<p><strong>Does the new $7,500 exemption help?</strong> For a qualifying stand-alone pad or patio, yes, with a written request to the building official. Not for a driveway in the right-of-way, not for structural work, and not in a flood hazard area.</p>""",
    eyebrow="Permits") + sec(
    "Associations, plainly",
    """<p><strong>Do I need approval?</strong> In a community with an architectural review body, for anything visible, almost always. That includes changing material or colour, widening, and often drainage work.</p>
<p><strong>How long?</strong> It ranges from a two-week cycle to a monthly meeting. Celebration's committee meets the third Monday; Bellalago's meets twice a month; Poinciana's Design Control Board treats an unanswered application as disapproved after thirty days.</p>
<p><strong>What goes in the packet?</strong> Typically a survey or site plan with the work marked, the product and colour, the pattern, a drainage note and the installer's certificate of insurance, sometimes naming the association.</p>
<p><strong>Can the board require a permit first?</strong> No. The 2026 legislation bars an association from requiring a building permit as a precondition of architectural review, which removes a long-standing circular problem.</p>
<p><strong>What if I skip it?</strong> The association can require removal, and the cost of that lands entirely on the owner. It is the most expensive shortcut available on a hardscape project.</p>""",
    cls="alt")

SECTIONS["/faq/cost/"] = sec(
    "Money questions we are asked directly",
    """<p><strong>What deposit is normal?</strong> A deposit that covers material and mobilisation, with the balance tied to milestones such as base and forms, pour, and completion. A demand for half or more up front with no milestones is a risk, whoever is asking.</p>
<p><strong>Do you offer financing?</strong> Financing options are an owner decision that has not been finalised for this brand, so rather than name a partner we have not signed with, the honest answer today is to ask when you call.</p>
<p><strong>Is there a discount for doing several things at once?</strong> Yes, and it is real rather than a sales line. A patio, a walkway and a pad poured in one visit share the mobilisation, the truck minimum and the crew day, which is usually twenty to thirty percent better than three separate visits.</p>
<p><strong>Is there a discount for cash?</strong> Paying by cash is fine. Paying without a written contract, a receipt and a permit is where people lose their recourse, and we will not do that regardless of the payment method.</p>
<p><strong>Why is the small job so expensive per square foot?</strong> Because the ready-mix truck has a minimum load and a short-load fee, and the crew is on site for the same half day whether the slab is 144 or 400 square feet.</p>""",
    eyebrow="Money") + sec(
    "Questions about comparing quotes",
    """<p><strong>Why is your quote higher?</strong> Sometimes it is not, and sometimes it is because of base depth, slab thickness, reinforcement or drainage that the other quote does not mention. Those three or four lines account for most of the variation in this market, and all of them are invisible once the job is done.</p>
<p><strong>Should I take the cheapest?</strong> If the specification is genuinely the same, yes, and we will tell you so. The comparison only means something when all three quotes describe the same base, the same thickness and mix, the same reinforcement and the same drainage.</p>
<p><strong>What is a change order and will I get one?</strong> A written change to the scope and the price, agreed before the work is done. The common cause here is structural fill that nobody could see until the old slab came up, and we flag the possibility in the proposal rather than springing it.</p>
<p><strong>Will the price hold?</strong> Our proposals carry a validity period because ready-mix and paver pricing move. If material moves between proposal and start, we say so rather than absorbing it silently or adding it quietly.</p>""",
    cls="alt")

# ------------------------------------------------------------------- HOA
SECTIONS["/hoa/"] = sec(
    "What every board asks for, and what only some do",
    table(["Item", "Nearly always", "Sometimes", "Note"],
          [("Completed application form", "Yes", "", "Usually the association's own form"),
           ("Survey or site plan with the work marked", "Yes", "", "A recent survey is worth having anyway"),
           ("Product name, colour and a sample or photograph", "Yes", "", "Physical sample for pavers, colour chip for concrete"),
           ("Pattern and layout sketch", "Yes", "", "Including borders and the edge detail"),
           ("Drainage note", "", "Common", "Where the water currently goes and where it will go"),
           ("Contractor insurance certificate", "", "Common", "Sometimes naming the association"),
           ("Neighbour acknowledgement", "", "Occasionally", "More common where a change is visible from a shared boundary"),
           ("Estimated start and finish dates", "", "Common", "Some communities restrict work hours and days"),
           ("Deposit or compliance bond", "", "Rare", "Refundable on satisfactory completion")],
          caption="Assembled from the criteria we have read across the communities in our service area. The packet checklist tool builds this for a specific community."),
    eyebrow="The packet") + sec(
    "Communities where we have read the documents, and where we have not",
    """<p>We publish detailed pages only for communities whose written architectural criteria we have actually obtained and read: Poinciana through the Association of Poinciana Villages, Solivita, Celebration, Bellalago and Solterra. On those pages the rules are quoted with their section references so you can check them against the source.</p>
<p>For Storey Lake, Tapestry, Windsor Hills, Providence, the ChampionsGate sub-associations and Reunion's three management companies we have contacts but not verified written criteria, and we will not summarise a rule we have not seen. What we do instead is contact the management company for the specific address, obtain the current packet requirements in writing, and attach them to the proposal. If you have a copy of your community's current criteria and are willing to share it, we will read it and, with permission, add a page.</p>""",
    cls="alt")

SECTIONS["/hoa/poinciana-apv/"] = sec(
    "The thirty-day clock, and why it is the important clause",
    """<p>Most architectural provisions are about what you may build. The clause worth planning around in Poinciana is about time: under the published Design Control Board criteria, an application that has not been acted on within thirty days is deemed disapproved rather than approved. Silence is a denial.</p>
<p>That inverts the normal assumption. In many communities an applicant who hears nothing assumes tacit consent and proceeds; here that produces work without approval, which the association can require to be removed. So the process we follow is to submit a complete packet, obtain written confirmation of receipt, diary the thirtieth day, and follow up in good time before it. An incomplete application that sits waiting for a missing sample is the common way the clock runs out.</p>""",
    eyebrow="Process") + sec(
    "What the criteria say about surfaces",
    """<p>The criteria name concrete, asphalt and brick pavers as the driveway materials, and require walks to be of the same materials unless the board approves otherwise. Any walkway adjacent to the dwelling is limited to two feet in width without approval. Pavers are required to finish flush with the connecting driveway, walkway or roadway, which on a replacement means excavating deeper rather than building up. Prior written approval is required before any driveway, patio, drainage work or paved area is begun. And the owner is responsible for keeping driveways, walks and patios clean and maintained.</p>
<p>Read together, those provisions are more permissive on material than people expect and stricter on dimension and process than people expect. A paver driveway is straightforward to approve; a wider walk beside the house is not.</p>""",
    cls="alt")

SECTIONS["/hoa/solivita/"] = sec(
    "Matching the original builder is the governing idea",
    """<p>Solivita's architectural requirements are built around consistency with the original construction. Replacement driveways and walkways are expected to be built in the same style and of the same materials the original builder used, and requests for an extension or modification of a driveway go through the review process. Requests involving paint, roofing, pavers, doors, awnings, shutters and similar items are expected to include a colour sample or a photograph.</p>
<p>The practical effect is that a like-for-like replacement is a simple application and a change of material or colour is a real one. Owners who want pavers where the builder used concrete are not excluded, but they are making a modification request rather than a maintenance notification, and the packet needs to reflect that.</p>""",
    eyebrow="The principle") + sec(
    "What that means for an ageing community",
    """<p>Solivita's homes date from around 2000 into the 2020s, so its flatwork is young by comparison with the older Poinciana villages. The failures we see are specific rather than systemic: irrigation-driven settlement, a tree root under a walk, a utility trench that consolidated. Those are genuinely repairable, and a single panel replacement in matching material is both the technically right answer and the easiest one to get approved.</p>
<p>The place where owners get caught is colour. New concrete next to twenty-year-old concrete is lighter for about a year, which is not a material change but does look like one from the street. We note it in the application rather than letting it become a complaint, and where an owner would rather avoid it entirely, replacing the whole element is the alternative.</p>""",
    cls="alt")

SECTIONS["/hoa/celebration/"] = sec(
    "A monthly meeting is the scheduling constraint",
    """<p>Celebration's architectural review committee meets on the third Monday of each month unless otherwise posted, and that cadence sets the timeline for every project in the community. A complete application submitted in good time is considered at the next meeting; an incomplete one waits a month. There is no practical way to shorten it, so the sensible approach is to assemble everything before the first submission rather than iterating across meetings.</p>
<p>Completed applications go to the Town Hall at 851 Celebration Avenue, and the office can be reached on 407-566-1200 extension 2206. Owners also have access to the community's own resident portal, where the current guidelines and forms live.</p>""",
    eyebrow="Timeline") + sec(
    "What gets reviewed that owners do not expect",
    """<p>Three things catch people out. Joint sand colour, which reads strongly across a driveway field at a distance and is part of the appearance the committee is considering. Border and edge details, which are not just a design flourish but part of the approved treatment. And the transition where a private walk meets the public sidewalk, which has to hold the existing elevation and alignment.</p>
<p>The other point worth knowing is that villages carry their own accents within the community framework, so an approval granted for a house in one village is not a precedent for a house in another. We submit for the specific address with photographs of the existing condition, which is what the committee is actually comparing against.</p>""",
    cls="alt")

SECTIONS["/hoa/bellalago/"] = sec(
    "How the review runs",
    """<p>Bellalago and Isles of Bellalago are managed by FirstService Residential, and architectural review is required before changes to the exterior of a home. Applications are submitted through the resident portal, and the committee meets approximately twice a month, which makes the turnaround shorter than in communities that meet monthly. A twenty-four hour resident line is available on 866-378-1099 for questions about the process.</p>
<p>Because the meeting cycle is comparatively quick, the realistic timeline for a Bellalago project is usually set by material lead time rather than by the association. That is worth knowing when planning a job around a season: a special-order travertine or a discontinued paver match will take longer than the approval will.</p>""",
    eyebrow="Process") + sec(
    "What we prepare for a Bellalago submission",
    """<p>A marked-up site plan or survey showing the existing surface and the proposed footprint with dimensions. The product name, manufacturer, colour and size, with a physical sample where pavers or stone are involved and a colour chip where concrete colour is. A pattern and border layout. A note on drainage saying where water currently goes and where it will go after the work. Our certificate of insurance. And photographs of the existing condition from the street and from the rear, because the committee is comparing against what is there now.</p>
<p>That packet is assembled by the {pk}, which produces it as a single printable page. On lakefront and waterway lots we also include the elevation note, because raising a deck or a drive on those lots changes where runoff goes and the committee reasonably asks about it.</p>""".format(pk='<a href="/tools/hoa-packet-checklist/">packet checklist tool</a>'),
    cls="alt")

SECTIONS["/hoa/solterra/"] = sec(
    "The most specific driveway rules in our territory",
    """<p>Solterra Resort's published architectural guidelines say more about paving than any other document we have read in this market. An expanded driveway may not exceed three cars in width. No additional walking area may be added alongside an expanded driveway. Painting or staining of concrete paved surfaces is prohibited, and concrete surfaces may be sealed in a clear matte finish only, with a request submitted first. Rear setbacks are stated for structures and pool decks. Applications are expected to include a survey of the lot, a sketch of the proposed work and a material sample, and the board may require the installer's certificate of insurance naming the association, with general liability and workers compensation. An incomplete application gives the applicant fifteen days to complete it.</p>
<p>Artemis Lifestyles administers the community and can be reached on 407-705-2190. The guidelines are published by the association and are worth reading in full before any design work starts, because they will shape the design more than the county rules will.</p>""",
    eyebrow="What the document says") + sec(
    "How those rules change the design conversation",
    """<p>The three-car cap is the one that most often changes a plan. An owner with two cars, a work van and guest parking wants four spaces, and the guidelines do not allow the driveway to grow to hold them. The alternatives are a parking court set back from the driveway where the guidelines permit it, or accepting three.</p>
<p>The prohibition on painting and staining is the second. Owners who want colour on a concrete surface cannot get it through a coating here, which is why a significant share of Solterra colour projects become paver projects. And the clear matte sealer requirement means even a maintenance sealing on concrete goes through a request, which owners routinely do not expect. We put all three in the proposal so the constraint is visible before any material is chosen.</p>""",
    cls="alt")

# ---------------------------------------------------------------- PERMITS
SECTIONS["/permits/city-of-kissimmee/"] = sec(
    "What the application actually involves",
    """<p>The city's Driveway and Sidewalk Construction application is submitted through the EnerGov Citizen Self Service portal rather than on paper. What goes with it is a site plan showing the existing and proposed driveway with dimensions, the property lines and the right-of-way, details of the apron and any sidewalk crossing, and the contractor's information. Plan review takes at least two business days, and once the fee is paid the permit issues at least two business days after that, so a realistic minimum from submission to permit in hand is about a week.</p>
<p>Work in the right-of-way needs Public Works and Engineering approval alongside the building side, which is why the Engineering Division on the third floor at 101 Church Street on 407-518-2278 is the contact for driveway questions rather than the building counter. General permitting questions go to permitting@kissimmee.org or 407-518-2379.</p>""",
    eyebrow="Process") + sec(
    "The city line is not where people think it is",
    """<p>Kissimmee's boundary has grown by annexation along John Young Parkway, Osceola Parkway and the 192 corridor, leaving unincorporated pockets inside what looks like the city and large residential areas with Kissimmee addresses that are entirely county. Buenaventura Lakes is county. Most of the Pleasant Hill Road corridor is county. Parts of streets are split.</p>
<p>Because filing with the wrong office means starting again rather than being redirected, we resolve the parcel before preparing anything. The {finder} does it from an address against the Census city boundary, and for anything within a few hundred feet of the line we call the office rather than trusting the polygon.</p>""".format(finder='<a href="/tools/permit-finder/">permit finder</a>'),
    cls="alt")

SECTIONS["/permits/city-of-st-cloud/"] = sec(
    "The city's own lists, quoted",
    table(["Needs a permit", "Does not need a permit"],
          [("Patios", "Driveway reseal for single family or duplex, existing asphalt only"),
           ("Decks", "Pavers for driveways and sidewalks, referred to Public Works"),
           ("Screen enclosures", "Interior painting"),
           ("Roofing", "Carpet and flooring"),
           ("Windows and doors", "Cabinets"),
           ("Sheds and accessory structures", "Like-for-like repairs in the same footprint"),
           ("Solar", "")],
          caption="From the City of St. Cloud's published permit information, checked on 2026-09-10. Anything in the right-of-way needs Public Works and Engineering approval regardless of which column it falls in."),
    eyebrow="The lists") + sec(
    "Payments, portal and the new exemption",
    """<p>St. Cloud moved to cashless payment for permits from the first of January 2025, so fees are paid through the portal or by card at the counter rather than in cash. Applications go through the city's permit portal, and the Building Department is at 1300 9th Street on 407-957-7300.</p>
<p>The city has also taken up the state's exemption for single-family work valued under seven thousand five hundred dollars, effective the first of July 2026. It requires a written request for exemption rather than applying automatically, and it does not extend to structural, electrical, plumbing, mechanical or gas work, or to property in a FEMA special flood hazard area. For flatwork that means a qualifying stand-alone patio or pad may be exempted, while a driveway touching the right-of-way still goes through the normal route.</p>""",
    cls="alt")

SECTIONS["/permits/osceola-county/"] = sec(
    "Section 22-50.6 in full, and what it means",
    """<p>The county's paving and driveway restriction reads, in the version published in the Code of Ordinances: residential driveways shall not exceed twenty-four feet in width unless approved by conditional use, and residential driveway construction or widening shall be authorised by the issuance of a driveway permit by Osceola County.</p>
<p>Two things follow. First, twenty-four feet is a hard cap for a residential driveway in the unincorporated county without going through a conditional use process, which is a planning application rather than a building one and is not a routine step. Second, the permit requirement attaches to construction or widening, so a replacement in the same footprint still needs the permit because the apron sits in the right-of-way. Applicants are also asked to attest that they have read Land Development Code section 4.12.2, which governs right-of-way work.</p>""",
    eyebrow="The ordinance") + sec(
    "Facts from the Building Office worth knowing before you apply",
    table(["Item", "What the office publishes"],
          [("Code in force", "The 2023, eighth edition Florida Building Code with the 2020 NEC, effective from 31 December 2023"),
           ("Residential plan review", "Normally three to five days"),
           ("Notice of commencement", "Required on jobs of $5,000 and above, recorded before the first inspection"),
           ("Inspection scheduling", "Requested before 3 p.m. for the following day"),
           ("Saturday inspections", "By request made by Thursday at 3 p.m."),
           ("After-hours inspection fee", "A minimum charge applies"),
           ("Where", "1 Courthouse Square, Suite 1400, Kissimmee, on 407-742-0200"),
           ("Portal", "The county's Accela-based permit centre")],
          caption="From the Building Office's published frequent questions and permit information, checked on 2026-09-10."),
    cls="alt")

SECTIONS["/permits/orange-county/"] = sec(
    "Why this page exists at all",
    """<p>Orange County sits immediately north of our home county, and a significant slice of our estimating radius crosses into it: Hunters Creek, Meadow Woods, Southchase, Williamsburg, Taft and the Lake Hart area are all closer to our base than several of the Polk towns we serve. So the rules are worth knowing even though the bulk of our work is on the Osceola side.</p>
<p>What makes Orange different is the breadth of the permit requirement. The county's published guidance states that any time you are pouring concrete or placing pavers, a permit is required, which is materially broader than unincorporated Osceola's treatment of detached flatwork or Polk's location-based test. Pavers additionally require a Zoning permit.</p>""",
    eyebrow="Context") + sec(
    "The right-of-way driveway detail",
    """<p>Orange County publishes a specific construction standard for the portion of a driveway that sits in its right-of-way: a minimum of six inches of three thousand psi concrete, with no steel reinforcement in the right-of-way section, including the sidewalk crossing, and driveways set back a minimum of three feet from the property line. Restoration of sidewalks, curb and driveways has to be consistent with the applicable accessibility standards, with a minimum width stated for longitudinal driveway cuts.</p>
<p>The no-steel provision surprises people, and the reason is practical: the county has to be able to saw and remove that section for utility work, and reinforcement makes that slower and more expensive. It is a good illustration of why the apron is priced as a separate line from the driveway field. The Division of Building Safety is at 201 South Rosalind Avenue, Orlando, on 407-836-5550.</p>""",
    cls="alt")

# ------------------------------------------------------------------ TOOLS
SECTIONS["/tools/"] = sec(
    "Why we built these rather than a quote form",
    """<p>Every tool here answers a question a homeowner has before they are ready to talk to a contractor. Which office issues my permit. How much concrete is in a pad this size. Whether pavers or concrete suits my situation. What my association will ask for. Which month to pour in. What to put in front of three bidders so their numbers mean something.</p>
<p>None of them asks for your contact details, none of them sends anything to us, and all of them run in your browser. The permit finder sends the address you type to the Census Bureau's public geocoder and nowhere else. That is deliberate: a tool that harvests a lead in exchange for an answer is an advertisement, and these are meant to be useful whether or not you ever call us.</p>""",
    eyebrow="Approach") + sec(
    "What each one is good for",
    table(["Tool", "Use it when", "What it will not do"],
          [("Permit and jurisdiction finder", "You do not know which city or county your address is in", "Replace a call to the office for an address near a boundary"),
           ("Concrete and paver calculator", "You need volume, bags, base depth or a planning cost range", "Account for waste on a curved field or for structural fill"),
           ("Concrete versus pavers decision tool", "You are weighing the two and want reasons, not a preference", "Know your association's rules"),
           ("HOA and ARC packet checklist", "You are assembling an architectural submission", "Substitute for your community's own current form"),
           ("Pour calendar", "You are choosing a month or worried about rain", "Predict a specific day's weather"),
           ("Ask the estimator", "You want to see what other homeowners here are asking", "Answer a question about your specific lot"),
           ("Project brief generator", "You are getting three quotes and want them comparable", "Price the job")],
          caption="Each tool states its own assumptions on its page. They are planning aids, not substitutes for a site visit."),
    cls="alt")

SECTIONS["/tools/permit-finder/"] = sec(
    "How the finder works, and where it can be wrong",
    """<p>When you enter an address, it is sent to the U.S. Census Bureau's public geocoding service, which returns a latitude and longitude. That point is then tested against city and county boundary polygons from the Census Bureau's TIGERweb data, simplified to roughly two hundred feet so the file stays small enough to load quickly. Nothing you type is sent to us and nothing is stored.</p>
<p>Two consequences. An address a few hundred feet from a municipal boundary can fall on the wrong side of a simplified polygon, so the tool flags results near a line and tells you to confirm with the office. And a very new address may not be in the geocoder yet, in which case the tool falls back to a ZIP-based answer, which is less precise because several ZIP codes here span both city and county.</p>""",
    eyebrow="Method") + sec(
    "What to do with the answer",
    """<p>The result tells you the jurisdiction and summarises what that office requires for a driveway, a patio or slab, and pavers. It is a starting point for a conversation, not an authority. For anything that matters, the jurisdiction pages on this site quote the official source and give the office's phone number, and the office itself is the final word.</p>
<p>If you are getting quotes, the most useful thing to do with the result is to tell each bidder which office applies and ask how they intend to handle the permit. A contractor who works this county daily will answer without hesitating; one who does not will often propose to skip it, which is the answer you were looking for.</p>""",
    cls="alt")

SECTIONS["/tools/concrete-paver-calculator/"] = sec(
    "What the calculator assumes",
    table(["Input", "Assumption", "When to override it"],
          [("Concrete volume", "Area times thickness, plus 10 percent for subgrade variation", "A very uneven subgrade needs more"),
           ("Bags versus ready-mix", "An 80 lb bag yields about 0.6 cubic feet", "Below about half a yard, bags are usually more practical"),
           ("Base depth", "4 in under concrete, 6 in under a paver driveway", "Ridge sand and poor subgrade both change it"),
           ("Paver count", "Area divided by unit area, plus the waste factor you choose", "Herringbone and curves need 8 to 18 percent"),
           ("Bedding sand", "1 in screeded", "Not a levelling layer; it does not fix a bad base"),
           ("Polymeric sand", "Coverage from the manufacturer's chart by joint width and paver thickness", "Wide joints consume far more"),
           ("Cost range", "The current Cost Index rate for that item", "Your site conditions are not in the index")],
          caption="The calculator is a takeoff aid. It does not know your soil, your access or what is under an existing surface."),
    eyebrow="Assumptions") + sec(
    "The number people get wrong most often",
    """<p>Waste. A rectangular patio in a running bond wastes about five percent. The same area in a forty-five degree herringbone with a border wastes eight to twelve, because every perimeter unit is a diagonal cut. A curved driveway with a circle feature can reach eighteen. Ordering to the calculated area and no more is the most common way a job stops on day two waiting for material, and on a discontinued or special-order line that can mean weeks rather than days.</p>
<p>The second is depth. Base depth is a compacted depth, not a loose one, and loose limerock compacts by roughly a fifth. Ordering four inches of loose material and compacting it produces a base of about three and a quarter inches, which is not what the specification said.</p>""",
    cls="alt")

SECTIONS["/tools/concrete-vs-pavers/"] = sec(
    "What the tool weighs, and why",
    """<p>The eight questions map onto the factors that actually differ between the two materials in this market: first cost, how long you intend to stay, whether the lot has a drainage history, whether mature trees are near the surface, what the association already approves, whether the surface will be walked on barefoot, whether utilities are likely to be cut through it, and how you feel about ongoing maintenance.</p>
<p>Some of those push hard. A lot with a known drainage problem or mature live oaks near the slab pushes toward pavers, because settlement is repairable rather than terminal. A tight budget on a large area pushes toward concrete, because the premium scales with square footage. An association with a paver-only palette settles it. Others barely move the answer, and the tool says so rather than pretending every input matters equally.</p>""",
    eyebrow="Logic") + sec(
    "Where it will not commit",
    """<p>The tool will not tell you that one material adds more resale value than the other, because we have no local sales data that would support the claim and we are not going to invent one. It will not tell you that pavers are always cooler, because colour matters more than material and a dark paver is hotter than a light slab. And it will not produce a single answer when the inputs genuinely balance; in that case it says the decision is a preference and explains what each choice would mean.</p>
<p>If the recommendation surprises you, the reasoning is shown alongside it, and the underlying comparison with numbers is on the {c} page. The decision is yours; the tool is there to make the trade-offs visible rather than to make the choice.</p>""".format(c='<a href="/compare/concrete-vs-pavers/">concrete versus pavers</a>'),
    cls="alt")

SECTIONS["/tools/hoa-packet-checklist/"] = sec(
    "Why a checklist beats a form",
    """<p>Every association has its own application form, and none of them can be replaced by something on our site. What can be replaced is the back-and-forth that happens when a packet goes in missing the survey, or with a photograph instead of a sample, or without the drainage note the board asks about every time. The checklist assembles what the boards in this area actually ask for, so the first submission is the complete one.</p>
<p>That matters most where the meeting cycle is long. In Celebration, where the committee meets monthly, an incomplete packet costs a month. In Poinciana, where an application not acted on within thirty days is deemed disapproved, an incomplete packet can cost the application itself.</p>""",
    eyebrow="Purpose") + sec(
    "What we supply and what only you can supply",
    table(["Item", "Who provides it"],
          [("Association application form", "You, from your community portal or manager"),
           ("Survey or site plan of the lot", "You; we mark the work on it"),
           ("Dimensioned sketch of the proposed work", "Us"),
           ("Product name, manufacturer, colour and size", "Us"),
           ("Physical sample or colour chip", "Us"),
           ("Pattern and border layout", "Us"),
           ("Drainage note", "Us"),
           ("Contractor certificate of insurance", "Us, through our agent"),
           ("Photographs of the existing condition", "Us at the site visit"),
           ("Owner signature and any neighbour acknowledgement", "You")],
          caption="On a typical job the owner supplies two items and signs a third. Everything else comes with the proposal."),
    cls="alt")

SECTIONS["/tools/pour-calendar/"] = sec(
    "Reading the calendar",
    """<p>The calendar is built from the NOAA 1991 to 2020 normals for the Kissimmee 2 station, and the number that drives our recommendation is days with at least a tenth of an inch of rain rather than total rainfall. A month with nine inches spread over thirteen wet days is harder to schedule around than a month with four inches on six days, and the totals alone hide that.</p>
<p>Months with twelve or more such days, June through August with September close behind, are treated as storm-season months: first-light starts, slab finished and covered before the early afternoon, base work not left open overnight when a system is forecast. October through April, at roughly three to six such days a month, are ordinary scheduling.</p>""",
    eyebrow="Method") + sec(
    "What the calendar cannot do",
    """<p>It cannot forecast. Normals are thirty-year averages and tell you what a typical August looks like, not what next Tuesday will. The working forecast we actually use is the morning radar and the hour-by-hour outlook on the day, and the decision to pour or postpone is made that morning rather than a week out.</p>
<p>It also does not capture the other seasonal constraint, which is demand. Google Trends for the Orlando market shows paver interest peaking in April and May every year for the past five years, and pool deck interest with it. That is a scheduling constraint of a different kind: the weather in March is excellent and the calendar is full. Booking in the autumn for spring work is the practical response.</p>""",
    cls="alt")

SECTIONS["/tools/ask-the-estimator/"] = sec(
    "How this page is compiled",
    """<p>These are questions our estimators are actually asked, on the phone and standing in driveways, written down and answered briefly. Nothing here is invented to fill a page, and nothing identifies the person who asked. Where a question includes a detail that would identify a property, the detail is generalised or removed.</p>
<p>The page is updated as questions accumulate rather than on a schedule, and each entry carries the date it was added. There is an RSS feed at <a href="/feed.xml">/feed.xml</a> for anyone who wants to follow it. Questions that turn out to be common enough to deserve a full treatment get promoted into a guide or a FAQ page, and the entry here then links to it.</p>""",
    eyebrow="Sourcing") + sec(
    "Ask one",
    """<p>If you have a question about concrete or pavers in this area, send it through the {c} and say it is for this page. We will answer it directly by email whether or not it ends up published, and if it is published it will be anonymised.</p>
<p>The questions that are most useful to other people are the specific ones: why does this happen on my street, what does this cost here, which office handles this, is this normal for a house of this age. General questions about concrete are answered better by the service pages, and we will point you there rather than duplicating them.</p>""".format(c='<a href="/contact/">contact form</a>'),
    cls="alt")

SECTIONS["/tools/project-brief/"] = sec(
    "What a brief changes about the quotes you get",
    """<p>Three contractors looking at the same driveway will quote three different jobs unless someone writes down what the job is. One assumes four inches of base, one assumes two, one assumes none. One includes removing the old slab, one assumes you have arranged it. One prices drainage, two do not mention it. The spread between the numbers then tells you nothing about who is better value.</p>
<p>A brief fixes the specification so the comparison is real. It states the area and dimensions, the surface being removed, the base depth and material, the slab thickness with mix strength and reinforcement or the paver thickness and pattern, the drainage requirement, the permit expectation and the finish. Hand the same page to everyone and the numbers become comparable.</p>""",
    eyebrow="Purpose") + sec(
    "Questions the brief tells you to ask",
    table(["Question", "What a good answer sounds like"],
          [("What base depth and material?", "A specific depth of a named material, compacted in lifts"),
           ("What thickness, strength and reinforcement?", "A number, a psi and how the steel is held at depth"),
           ("Where does the water go?", "A described route, not a shrug"),
           ("Which office issues the permit and who files it?", "The correct office named without hesitation"),
           ("What happens if you find soft ground under the old slab?", "A stated change-order process, not silence"),
           ("Joint spacing and when they are cut?", "About ten feet on a four inch slab, within twelve hours"),
           ("What does the warranty exclude?", "A list; a warranty with no exclusions is not one"),
           ("When can I park on it?", "Seven days for cars, twenty-eight for heavy")],
          caption="The brief prints with these questions at the bottom. The answers tell you more about a contractor than the price does."),
    cls="alt")

# --------------------------------------------------------- INSTITUTIONAL
SECTIONS["/about/"] = sec(
    "What a service brand is, said plainly",
    """<p>Kissimmee Concrete is a trading identity for a Central Florida concrete and paver contractor that also operates under other names in other parts of the metro. The crews, the equipment, the estimators and the insurance are the same; the brand exists because the permits, soils, associations and prices in Osceola County and northern Polk are different enough from West Orange or South Lake to be worth writing about separately.</p>
<p>We say that here rather than leaving you to infer it, because a website that implies a separate local company with a separate office and a separate history when none exists is a misrepresentation, whatever the marketing convention. What you get is the same crew you would get under another name, and a set of pages written specifically about the county you live in. The legal entity that contracts with you, its registration and its insurance appear on the proposal itself.</p>""",
    eyebrow="Disclosure") + sec(
    "What is still being finalised",
    """<p>This site is new. Several things that a mature site would show are deliberately absent rather than invented. There are no reviews or star ratings on it, because the profile that will carry them is not live yet; when it is, they will link to the source. There is no years-in-business claim, no project count and no award. The workmanship warranty terms appear in the contract and are summarised here without a term, because the owner has not finalised it across brands.</p>
<p>There is also no phone number yet, which is the most visible gap. A dedicated tracked number is being provisioned; until it is live, the estimate form and the email address are the way to reach us, and both are monitored during business hours. We would rather show you an accurate site with gaps than a complete-looking one with placeholders in it.</p>""",
    cls="alt")

SECTIONS["/editorial-standards/"] = sec(
    "How a page gets written here",
    """<p>Every page starts with the question a homeowner actually asks, taken from what our estimators hear, from what people search, and from what competitors leave unanswered. The question is assigned to exactly one page, which owns the answer; other pages link to it rather than repeating it, which is why this site has fewer pages than a template-driven competitor and more on each one.</p>
<p>Then the facts are gathered from primary sources, which for us means the jurisdiction's own page or code, the Florida Statutes, NOAA for climate, USDA for soils, the Census for boundaries and populations, and manufacturers for product specification. Each fact is written with its source, and the source list at the foot of the page is what we actually read, not a decorative bibliography.</p>
<p>Then it is drafted by someone who does this work, edited against the sources, and run through an automated check that looks for marketing filler, for phrases used by our sister brands, for placeholder text, and for pages where the density of checkable facts has fallen too low. Pages that fail go back.</p>""",
    eyebrow="Process") + sec(
    "What we do when we get something wrong",
    """<p>Two things. We fix it within two business days of being told, and we note the change in the update line at the foot of the page rather than silently editing. That line exists so a reader can tell whether a page has been reviewed since the last time a rule changed, which on permit pages matters a great deal.</p>
<p>Rules do change. The state permit exemption that took effect in July 2026 changed several of these pages, and the local implementation of it is still settling. Where a page describes something in flux, it says so rather than presenting a snapshot as settled. If you find something here that is out of date or wrong, the contact form is the fastest route and we would rather hear it from you than leave it.</p>""",
    cls="alt")

SECTIONS["/contact/"] = sec(
    "What to include so the first reply is useful",
    """<p>The three things that let us answer properly in one message rather than four are the address or at least the community, a rough size, and a photograph. Size can be as loose as "about two cars wide and four cars long"; we will measure it properly at the visit. A photograph from the street and one from close up tells us more about a failing slab than several paragraphs will.</p>
<p>If you know what your association requires, or if you have a survey, mentioning it early saves a week. If you are getting three quotes and want them comparable, the {pb} produces a page you can attach.</p>""".format(pb='<a href="/tools/project-brief/">project brief tool</a>'),
    eyebrow="Before you send") + sec(
    "What happens to what you send",
    """<p>The form goes to our estimating inbox and nowhere else. It is not sold, not shared with a lead broker, and not passed to other contractors. The only people who see it are the person who replies to you and the crew that would do the work. Estimate requests that do not become jobs are deleted after twenty-four months; the full detail is in the <a href="/privacy/">privacy policy</a>.</p>
<p>You will get a reply during business hours, which are Monday to Friday half past seven to six and Saturday eight to one. If a form submission fails for any reason, the email address on this page reaches the same inbox directly, and we would rather you use it than assume we ignored you.</p>""",
    cls="alt")

SECTIONS["/warranty/"] = sec(
    "How a warranty claim actually goes",
    """<p>Email the address on the contract with the property address and photographs. We come out, usually within a week, and look at it with the same tools we use on an estimate: a straight edge, something to tap with, and a hose. Then you get a written answer that says either this is covered and here is when we will fix it, or this is not covered and here is why, in terms of the exclusions in your contract.</p>
<p>Most paver warranty work is a lift and relay of the affected area, which takes a day. Most concrete warranty work is joint or edge repair. Where a claim turns out to be caused by something outside our scope, a broken irrigation line, a new downspout arrangement, a tree that has grown, we will say so and quote the repair separately rather than either absorbing it or arguing about it.</p>""",
    eyebrow="Claims") + sec(
    "What is genuinely not covered, and why",
    table(["Excluded", "Reason"],
          [("Hairline shrinkage cracks", "All concrete develops them; no contractor in Florida warrants against them"),
           ("Colour variation and weathering", "Concrete is not a manufactured tile; it varies between loads and fades with UV"),
           ("Efflorescence on pavers", "A property of the units, not of the installation"),
           ("Damage from vehicles heavier than the specified load", "A slab specified for cars is not a slab for a loaded truck"),
           ("Movement from a utility cut or a new irrigation leak", "Ground disturbed after we left"),
           ("Tree root damage", "Growth after installation, unless a barrier we installed failed"),
           ("Drainage we recommended and you declined", "Noted in the proposal at the time"),
           ("Staining from well-water irrigation", "Water chemistry, not workmanship")],
          caption="These are stated in the contract rather than discovered at claim time. A warranty that lists no exclusions is not being honest about what concrete does."),
    cls="alt")
