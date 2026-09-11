# -*- coding: utf-8 -*-
"""Extra depth for the city hubs and county hubs."""
from _helpers import sec, table, faq

SECTIONS = {}
FAQS = {}

# ------------------------------------------------------------ TIER 1 CITIES
SECTIONS["/areas/kissimmee/"] = sec(
    "Neighbourhood by neighbourhood",
    table(["Area", "Roughly when built", "ZIP", "What we are usually called for"],
          [("Downtown and the lakefront", "1900s to 1960s", "34741", "Narrow driveway replacements, oak-root lifts, brick street edges"),
           ("Bermuda Avenue and Vine Street corridor", "1960s to 1980s", "34741, 34744", "Full driveway replacement, apron repair"),
           ("Kissimmee Bay and Partin Settlement", "1980s to 1990s", "34744", "Driveway replacement, pool deck resurfacing"),
           ("Buenaventura Lakes", "Late 1970s to 1990s", "34743", "Driveway replacement, panel repair, downspout drainage"),
           ("Remington and Eagle Lake", "1990s to 2000s", "34744, 34746", "Paver driveways, lanai extensions, pool decks"),
           ("Bellalago and Isles", "2000s to 2010s", "34746", "Paver driveways, travertine decks, architectural review packets"),
           ("Tapestry and Storey Lake", "2010s to 2020s", "34741, 34746", "Patio extensions, pavers, summer kitchens"),
           ("Windsor Hills and the 192 resort corridor", "2000s", "34747", "Rental pool decks, sealing, apron repair"),
           ("Poinciana side, Pleasant Hill Road", "1970s onward", "34758, 34759", "Driveway replacement under APV review")],
          caption="Where our Kissimmee work actually is. The ZIP codes overlap city and county jurisdictions, which is why the permit answer depends on the parcel rather than the address."),
    eyebrow="Where we work") + sec(
    "City limits, county pockets and why it matters",
    """<p>Kissimmee's boundary is not a simple ring. Annexations along John Young Parkway, Osceola Parkway and the 192 corridor have left county pockets inside what looks like the city, and large residential areas with Kissimmee mailing addresses, Buenaventura Lakes and most of the Pleasant Hill Road corridor among them, are entirely unincorporated Osceola County.</p>
<p>The practical difference is the permit. Inside the city, a driveway goes through the Engineering Division's Driveway and Sidewalk Construction application on the EnerGov portal, with plan review of at least two business days and issuance at least two business days after payment. Outside it, the county driveway permit under section 22-50.6 applies with its twenty-four foot width cap, and the Building Office reviews residential applications in roughly three to five days. Filing with the wrong office costs a fortnight, so we resolve the parcel before quoting.</p>""",
    cls="alt")

SECTIONS["/areas/st-cloud/"] = sec(
    "The four St. Clouds",
    table(["Area", "Era", "ZIP", "Typical work"],
          [("Historic grid and lakefront", "1909 to 1960", "34769", "Narrow drive replacement, oak roots, brick street edges"),
           ("Nova Road and Canoe Creek corridor", "1980s to 2000s", "34769, 34772", "Two-car driveway replacement, boat pads"),
           ("Old Hickory Tree and east", "1990s to 2010s", "34772", "Long drives, RV pads, workshop slabs"),
           ("Narcoossee, Sunbridge, Weslyn Park", "2015 to 2026", "34771", "New-build patios, paver driveways, pool decks"),
           ("Harmony", "2003 onward", "34773", "Patios, pool decks, larger-lot driveways"),
           ("Rural south and east toward Holopaw", "Mixed", "34773", "Long rural drives, septic routing, truck access")],
          caption="St. Cloud covers more ground than any other city in our territory, and the job changes completely between the 1909 grid and the 2026 subdivisions."),
    eyebrow="Areas") + sec(
    "What the city does and does not permit",
    """<p>St. Cloud publishes its own list, and it is unusually clear. Work that needs no permit includes resealing an existing asphalt driveway on a single-family or duplex property, and pavers for driveways and sidewalks, which are referred to Public Works instead. Work that does need a permit includes patios, decks, screen enclosures, roofing, windows, sheds and solar. Anything in the right-of-way needs Public Works and Engineering approval regardless of the category.</p>
<p>The city also adopted the state's new exemption for single-family work valued under seven thousand five hundred dollars, effective the first of July 2026, with the exclusions the statute carries for structural, electrical, plumbing, mechanical and gas work and for property in a flood hazard area. A written request for exemption is part of that process rather than an automatic waiver, and the Building Department at 1300 9th Street is where it goes.</p>""",
    cls="alt")

SECTIONS["/areas/celebration/"] = sec(
    "Villages, and why they are not interchangeable",
    """<p>Celebration is organised into villages that were built in phases from 1996 onward, and each carries its own character within the community's overall design framework. North Village and South Village hold much of the original housing stock; Lake Evalyn is small and distinctive; West Village and Artisan Park came later with different housing types; Roseville Corner, Spring Park and Georgetown each read differently again. Alley-loaded homes with rear garages are common in some villages and absent from others.</p>
<p>For us that means two things. The driveway on an alley-loaded home is a short apron with awkward access and a neighbourly scheduling problem, while a front-loaded home in an older village has a narrow drive with street trees close to the edge. And an architectural approval from one village is not a precedent for another, so we submit for the specific address rather than assuming.</p>""",
    eyebrow="Villages") + sec(
    "Working inside a community with a designed streetscape",
    """<p>Celebration's covenants reach further than most Florida communities: approved products, patterns, colours and edge details, with the architectural review committee meeting monthly on the third Monday. That cadence is the practical constraint on scheduling, and the reason we assemble the full packet before the first submission rather than iterating.</p>
<p>The jurisdictional answer is simpler than the architectural one. Celebration is unincorporated Osceola County, so the county's rules apply for anything permitted, including the driveway permit and the twenty-four foot width cap. The Town Hall on Celebration Avenue handles the architectural side and is where completed applications go.</p>""",
    cls="alt")

SECTIONS["/areas/poinciana/"] = sec(
    "Nine villages across two counties",
    """<p>Poinciana was platted in the early 1970s and built out over five decades across both Osceola and Polk counties. The original villages carry houses from the 1970s and 1980s on modest lots; later phases run through the 1990s and 2000s; Solivita, the age-restricted community inside Poinciana, was developed from around 2000 into the 2020s with its own association and its own architectural requirements.</p>
<p>Two administrative facts shape every job here. The Association of Poinciana Villages reviews exterior work through its Design Control Board, whose published criteria require prior written approval and treat an unanswered application as disapproved after thirty days. And the county line runs through the community, so the building department handling your permit depends on the village rather than the mailing address, which is Kissimmee on both sides.</p>""",
    eyebrow="Structure") + sec(
    "What fifty-year-old flatwork looks like here",
    """<p>The driveways that went in with the first Poinciana houses are now around fifty years old, poured thin on native sand before a base was routine for residential flatwork. What we find under them matches what we find in Buenaventura Lakes: no rock, a channel scoured out along the downspout line, and wire mesh, where there was any, lying rusted at the bottom of the slab.</p>
<p>At that age one repaired panel is surrounded by panels of the same vintage and construction, so we price the panel and the replacement together and let the numbers decide. Solivita is a different case entirely, with much younger flatwork whose failures are genuinely local, irrigation, roots or a utility trench, and therefore genuinely repairable.</p>""",
    cls="alt")

SECTIONS["/areas/buenaventura-lakes/"] = sec(
    "One development, one era, one set of problems",
    """<p>Buenaventura Lakes is a Landstar Homes development built out from the late 1970s through the 1990s in unincorporated Osceola County, with a Kissimmee mailing address and the 34743 ZIP. Because it went in as a single programme, the flatwork across whole streets shares a construction date, a specification and a failure mode, and neighbours tend to reach the same decision within a year or two of each other.</p>
<p>The specification was roughly four inches of concrete on graded native sand, wire mesh laid on the ground rather than chaired, and shallow or absent control joints. On Smyrna and Myakka fine sand with a wet-season water table around twelve inches and downspouts discharging at the slab edge, that has produced the stepped garage panel and the cracked apron we are called out for almost every week.</p>""",
    eyebrow="Development history") + sec(
    "What to do first, regardless of budget",
    """<p>Whatever a homeowner decides about the driveway itself, one thing is worth doing immediately and costs very little: get the roof water away from the slab edge. Extended downspouts, a splash block that actually directs water, or a short drain line to the swale removes the cause of most panel settlement here. Doing it before a replacement protects the new slab; doing it instead of a replacement slows the deterioration of the old one.</p>
<p>The second cheap item is sealing tight, level cracks so water stops entering the base through them. The third is grinding any trip lip on the front walk, which on a rental property is a liability item as much as a maintenance one. None of those is a substitute for a replacement when the slab has gone, but all three buy time and none of them is wasted afterwards.</p>""",
    cls="alt")

SECTIONS["/areas/four-corners/"] = sec(
    "One intersection, four counties, one economy",
    """<p>Four Corners is the area around the meeting point of Osceola, Polk, Lake and Orange counties along US-27 and US-192, and it exists as a place because of the vacation-home market rather than because of any municipal boundary. Windsor Hills, Windsor at Westside, Encore, Solterra just to the south and the ChampionsGate communities just to the east are all part of the same economy: short-term rental homes with private pools, managed by companies rather than occupied by owners.</p>
<p>That gives the work a distinct character. Pool decks are the dominant scope, the calendar is set by bookings rather than by the owner's convenience, the approvals run through a management company and an association, and the specification favours light colours, textured surfaces and penetrating sealers because guests, not owners, use the surfaces.</p>""",
    eyebrow="Context") + sec(
    "Which county are you actually in",
    table(["Community", "County", "Permit office", "Note"],
          [("Windsor Hills", "Osceola", "Osceola County Building Office", "Driveway permit and the 24 ft width cap apply"),
           ("Windsor at Westside", "Osceola", "Osceola County", "Same"),
           ("Solterra Resort", "Polk", "Polk County Building Division", "Association guidelines are unusually specific"),
           ("Providence", "Polk", "Polk County", "Own architectural review"),
           ("ChampionsGate residential", "Osceola", "Osceola County", "Sub-association review"),
           ("Loughman area", "Polk", "Polk County", "Often no association at all"),
           ("West of US-27 toward Lake County", "Lake", "Lake County", "Different right-of-way process")],
          caption="A Four Corners address tells you very little about which office issues the permit. We resolve it from the parcel, because filing in the wrong county costs weeks."),
    cls="alt")

SECTIONS["/areas/champions-gate/"] = sec(
    "A resort community on the Osceola side of the interchange",
    """<p>ChampionsGate developed from around 2001 at the I-4 and US-27 interchange, with golf, a resort hotel and a large residential component split between owner-occupied and short-term rental homes. The residential phases, including Stoneybrook South and the villages around the Oasis Club, sit in unincorporated Osceola County, which means county permitting and the twenty-four foot residential driveway width cap apply.</p>
<p>Lots are generally deep and narrow with pools filling much of the rear yard, so pool deck work is constrained by access rather than by area. Material and spoil move through a side yard or over the front, hand excavation is normal, and a machine that would do the work in an hour elsewhere simply does not fit. We price that honestly rather than absorbing it.</p>""",
    eyebrow="Community") + sec(
    "Approvals here, and what we will not claim",
    """<p>ChampionsGate's residential phases sit under community associations with architectural review, administered by management companies. We have not obtained and read the current written architectural criteria for every sub-association here, so we do not quote rules we have not verified. What we do instead is contact the management company for the specific address, get the current packet requirements in writing, and attach them to the proposal.</p>
<p>Where we have read and verified a community's criteria, we quote them directly with the section numbers, as on our pages for Poinciana, Solivita, Celebration, Bellalago and Solterra. Where we have not, we say so. That distinction is deliberate: a confident summary of a rule we have not read is worse than no summary at all when a board rejects an application over it.</p>""",
    cls="alt")

SECTIONS["/areas/reunion/"] = sec(
    "A resort with three sets of governing documents",
    """<p>Reunion Resort developed from around 2004 through 2015 in unincorporated Osceola County, with three golf courses and a housing mix that runs from villas and terraces to large single-family homes. Administration is split: Artemis Lifestyles handles the single-family and several other product types, Greystone manages the north and south villas, and Southwest Property Management handles the terraces. Which one reviews your application depends on your product type, not on where the house sits.</p>
<p>For permitting the whole resort is unincorporated Osceola County, so the county's rules apply. The work is dominated by pool decks and driveways on properties that are largely short-term rentals, which puts the booking calendar and the management company at the centre of the scheduling conversation.</p>""",
    eyebrow="Administration") + sec(
    "Decks at ten to twenty years old",
    """<p>Reunion's flatwork is now old enough that the quality of the original installation is visible. Decks built on a properly compacted base are flat and need cleaning, re-sanding and sealing. Decks built on thin or dry-compacted base have settled at the most loaded edges, typically at a spa or at the sliding-door traffic line, and those need the field lifted and the base rebuilt under the affected area.</p>
<p>The coping is the quickest indicator. Bonded, level coping that has not separated from the deck suggests the deck has not moved against the pool structure; lifted coping or a gap that keeps opening suggests it has. That check plus a tap test distinguishes a maintenance visit from a rebuild, and the two numbers are far enough apart to be worth the twenty minutes.</p>""",
    cls="alt")

SECTIONS["/areas/davenport/"] = sec(
    "A small city inside a much larger unincorporated area",
    """<p>The City of Davenport is compact, and most addresses with a Davenport mailing address sit in unincorporated Polk County rather than inside the city. Providence, Solterra, the Loughman area and much of the development along Ronald Reagan Parkway and US-27 are county, permitted through the Polk County Building Division out of Bartow or the Northeast Government Center in Lake Alfred. Inside the city limits it is the city's own department.</p>
<p>The 33837, 33896 and 33897 ZIP codes span both, so the postal address settles nothing. We check the parcel before filing, because the two processes and their timelines differ and a misfiled application simply waits.</p>""",
    eyebrow="Jurisdiction") + sec(
    "Ridge sand, and the base method it demands",
    """<p>Davenport sits on the Lake Wales Ridge, where the dominant soils are Candler and Astatula sands: deep, single-grained and excessively drained. The water table is far below anything flatwork cares about, which removes the saturation problem that dominates Osceola County and replaces it with a compaction problem.</p>
<p>Dry ridge sand shears under a compactor instead of densifying. A base built dry looks finished, passes a visual inspection and consolidates the first time a heavy storm soaks it, which settles the slab or the paver field in its first wet season rather than its tenth. Wetting each lift before compaction and probing after it is the method that works, and it is the single most useful thing to ask a contractor about on this side of the county line.</p>""",
    cls="alt")

SECTIONS["/areas/haines-city/"] = sec(
    "The fastest-growing town in our Polk territory",
    """<p>Haines City has grown substantially since 2015, with new subdivisions along US-17-92, Commerce Avenue and out toward Lake Hamilton wrapping around a historic core whose houses date from the 1920s through the 1970s. The Florida Economic and Demographic Research estimate puts the city at 44,215 for 2025, which makes it the largest Polk municipality in our service area.</p>
<p>That growth produces a particular mix of work. In the new subdivisions the driveways are five to ten years old and sound, so the projects are extensions, widenings, patios and pads, all of which raise the question of how to add concrete beside existing concrete without it reading as an addition. In the older core the projects are replacements, with root problems, previous patching and narrow widths to work around.</p>""",
    eyebrow="Growth") + sec(
    "City or county, and who reviews what",
    """<p>Haines City operates its own building department for addresses inside the city limits; everything outside is unincorporated Polk County. Polk's published guidance permits slabs adjacent to or supporting a structure, elevated slabs, sidewalks and the portions of driveways in the right-of-way or within minimum setbacks, and requires all slabs to meet the minimum setbacks from property lines and easements except sidewalks and driveways.</p>
<p>Easements are the trap on new subdivision lots, because they are recorded on the plat rather than visible on the ground, and a slab placed over a drainage or utility easement can be required to come out. We pull the plat before staking anything, which is a fifteen-minute step that has saved several customers a much larger problem.</p>""",
    cls="alt")

SECTIONS["/areas/harmony/"] = sec(
    "Harmony, Narcoossee and the new communities on the corridor",
    """<p>This part of eastern Osceola County covers three quite different things. Harmony, planned from 2003 with a conservation ethos, generous lots and a dark-sky lighting standard. The Narcoossee corridor along Narcoossee Road, where Sunbridge and Weslyn Park have been building since around 2021. And the working rural parcels around and beyond them, on Nova Road, Jones Road and out toward Holopaw, where driveways are measured in hundreds of feet and septic systems and wells are the norm.</p>
<p>All three are unincorporated Osceola County for permitting, which means the county driveway permit and the twenty-four foot width cap apply to driveway work, and the Building Office at 1 Courthouse Square reviews residential applications in about three to five days.</p>""",
    eyebrow="Three areas") + sec(
    "Wetter than it looks",
    """<p>It is natural to assume that large rural lots drain better than suburban ones. East of St. Cloud the opposite is often true. The soil map units out this way include EauGallie and Basinger fine sands and, in the low areas, depressional phases that sit at or near the surface through the wet season. A long driveway will frequently cross more than one of them, which is why a single rate per square foot across a rural run produces a slab that dips where the ground is worst.</p>
<p>Access is the other rural constraint that gets underestimated. A loaded mixer weighs over thirty tons and needs a firm route, working clearance and somewhere to turn, and the culvert at the county road has to carry it. We walk the whole route at the site visit and price a pump truck or buggies where it will not work, rather than discovering it with a truck idling at the gate.</p>""",
    cls="alt")

# ------------------------------------------------------------ TIER 2 CITIES
SECTIONS["/areas/winter-haven/"] = sec(
    "Between the Chain of Lakes and the ridge",
    """<p>Winter Haven is the largest Polk city in our service area at 60,837 for 2025, and it sits at a soil boundary that matters for flatwork. The neighbourhoods on the ridge sit on Candler and Tavares sands, deep and free-draining, where the base has to be wetted before it will compact. The neighbourhoods in the flats between the lakes sit on Pomona and similar soils with a much shallower water table, where the Osceola-style saturation problem applies instead.</p>
<p>Which one your lot is on is not obvious from the street, and it changes the base method. We look up the map unit for the parcel before the visit and probe on site, because getting this backwards produces either a base that never compacted or a slab sitting in water.</p>""",
    eyebrow="Two soil regimes") + sec(
    "What we take on at this distance",
    """<p>Winter Haven is about 26 miles from Kissimmee, roughly an hour each way for a crew, so we are selective rather than unavailable. Full driveway replacements, paver driveways, pool decks and patios are all jobs where a multi-day mobilisation makes sense. A single panel repair or a small pad usually does not, and we will say so and suggest a local crew rather than pricing a day's travel into a half-day job.</p>
<p>Where we do work here, permitting is Polk County for unincorporated addresses and the City of Winter Haven for those inside the limits. The county's rules on slabs, setbacks and right-of-way work are the same as they are in Davenport and Haines City.</p>""",
    cls="alt")

SECTIONS["/areas/auburndale/"] = sec(
    "Lakes, groves and a growing ring of subdivisions",
    """<p>Auburndale sits between Winter Haven and Lakeland at about 27 miles from Kissimmee, with an estimated 21,677 residents for 2025. The older parts of town date from the citrus era and carry flatwork of a similar age and construction to Haines City's core, while the newer subdivisions off Berkley Road and toward Lake Alfred have gone in over the last decade.</p>
<p>The soils here are mixed, Candler and Tavares on the higher ground and Pomona and similar in the flats, so the base method is decided lot by lot rather than by town. The work we take at this distance is the same as elsewhere on the ridge: full driveways, paver fields, pool decks and patios, where a multi-day mobilisation is justified.</p>""",
    eyebrow="Context") + sec(
    "Permitting on the Polk ridge",
    """<p>Auburndale has its own building department for addresses inside the city; outside it, Polk County's Building Division handles the work from Bartow or the Northeast Government Center in Lake Alfred, which is the closer office for this part of the county. The county's published guidance permits slabs adjacent to or supporting structures, elevated slabs, sidewalks and portions of driveways in the right-of-way or within setbacks, and applies Building Code and Land Development Code drainage requirements regardless.</p>
<p>Pavers placed in the county right-of-way trigger the recorded release form, notarised and filed with the Clerk, in which the owner accepts maintenance responsibility for that section. It is a short step if it is planned for and a two-week delay if it is not.</p>""",
    cls="alt")

SECTIONS["/areas/lake-alfred/"] = sec(
    "A small town with the county's northeast office in it",
    """<p>Lake Alfred is small, about 9,038 residents for 2025, and sits roughly 22 miles from Kissimmee, which makes it one of the closer Polk towns we serve. It is also where Polk County's Northeast Government Center sits, at 200 Government Center Boulevard, which is the permitting office for a large part of the unincorporated county north and east of Bartow.</p>
<p>The housing is a mix of older town lots and newer subdivisions, and the soils are ridge soils, Candler and Tavares, with the same wetted-lift base requirement as Davenport and Haines City. The work is straightforward: driveway replacements, paver driveways, patios and pads.</p>""",
    eyebrow="Context") + sec(
    "What is worth a trip from Kissimmee",
    """<p>At this distance the economics favour jobs that occupy a crew for more than a day. A driveway replacement, a paver field, a pool deck or a substantial patio all qualify. A single panel repair, a small AC pad or a trip-hazard grind generally does not, and we would rather point you to a local crew than build an hour of travel each way into a half-day price.</p>
<p>Where several neighbours on the same street want work at the same time, which happens more often than people expect on streets where the flatwork shares an age, the mobilisation is shared and the numbers improve for everyone. It is worth asking the neighbours before scheduling.</p>""",
    cls="alt")

SECTIONS["/areas/dundee/"] = sec(
    "Small-town Polk on the ridge",
    """<p>Dundee is a town of roughly 5,847 residents for 2025, about 22 miles from Kissimmee on the Lake Wales Ridge between Winter Haven and Lake Wales. The housing stock is a mix of older town lots along US-27 and Highway 542 and newer subdivision phases that have gone in over the past decade as growth moved south from Winter Haven.</p>
<p>The soils are classic ridge: Candler and Astatula sands, deep and excessively drained, with the water table far below the slab. The base problem is compaction rather than saturation, and the method is to wet each lift before compacting it and probe after, which is the single specification detail worth asking any contractor about on this side of the county.</p>""",
    eyebrow="Context") + sec(
    "Who issues the permit",
    """<p>The Town of Dundee handles addresses inside its limits; the surrounding area is unincorporated Polk County, permitted from Bartow or the Northeast Government Center in Lake Alfred. Polk's rules are consistent across the unincorporated county: slabs adjacent to or supporting a structure, elevated slabs, sidewalks and the portions of driveways in the right-of-way or within minimum setbacks need permits, and all slabs must meet setbacks from property lines and easements except sidewalks and driveways.</p>
<p>We check the parcel rather than the address before filing, because the boundary between town and county is not visible from the street and a misfiled application waits rather than being redirected.</p>""",
    cls="alt")

SECTIONS["/areas/lake-wales/"] = sec(
    "At the top of the Lake Wales Ridge",
    """<p>Lake Wales sits at the highest part of the ridge that gives the landform its name, about 28 miles from Kissimmee, with an estimated 17,748 residents for 2025. It is the furthest regular point of our Polk coverage and the most distinctly ridge-like in its soils: Candler, Astatula and Archbold sands, deep, dry and free-draining.</p>
<p>The housing mixes an older core with newer subdivision growth, and the work follows that split. Older properties bring replacements with the usual accumulated history of patches and root lifts; newer ones bring extensions, patios and pads on lots where the builder's flatwork is still sound.</p>""",
    eyebrow="Context") + sec(
    "Why dry sand is not an easier base",
    """<p>Homeowners on the ridge sometimes assume that free-draining sand is a gift to a concrete contractor, since there is no standing water and no wet-season water table to design around. The catch is that single-grained sand with no moisture and no fines has almost no cohesion, so a compactor run over it dry displaces it rather than densifying it.</p>
<p>The base that results looks finished and is not. It consolidates the first time a summer storm saturates it, and the slab or the paver field above settles in its first wet season. Wetting each lift, compacting it and probing to check is the whole method, and it is why a proposal for a Lake Wales job should not read identically to one for a Kissimmee job.</p>""",
    cls="alt")

SECTIONS["/areas/polk-city/"] = sec(
    "The northern edge of our Polk coverage",
    """<p>Polk City is small, roughly 3,007 residents for 2025, and sits about 27 miles from Kissimmee near the northern end of the county between Lakeland and the I-4 corridor. It is at the edge of what we cover regularly, and the honest position is that we take multi-day jobs here and decline half-day ones rather than pricing travel into small work.</p>
<p>The soils are ridge soils with the associated compaction requirement, and permitting is the Polk County Building Division for unincorporated addresses or the city for those inside the limits. The Van Fleet Trail and the lakes shape the lot patterns more than any single subdivision does.</p>""",
    eyebrow="Context") + sec(
    "What to expect from a quote at this distance",
    """<p>Two things differ in a quote for a job this far out. Mobilisation is a real line rather than an absorbed cost, because a crew and equipment travelling an hour each way is an hour each way whether the job is large or small. And scheduling is less flexible: we will commit to consecutive days rather than fitting a job around closer work, because splitting a distant job across non-consecutive days doubles the travel.</p>
<p>What does not change is the specification. The base method, the thickness and steel for the load, the joint spacing and the drainage design are the same as they would be in Kissimmee, adjusted for ridge sand rather than flatwoods sand. Distance changes logistics, not standards.</p>""",
    cls="alt")

# ------------------------------------------------------------- COUNTY HUBS
SECTIONS["/areas/osceola-county/"] = sec(
    "Every jurisdiction inside the county, and what each one requires",
    table(["Jurisdiction", "Driveway", "Patio or slab", "Pavers", "Contact"],
          [("City of Kissimmee", "Driveway and Sidewalk Construction application through Engineering; review at least 2 business days, issue at least 2 more after payment", "Building Division; confirm scope", "Same application when in the right-of-way", "Engineering, 101 Church St, 3rd Floor, 407-518-2278"),
           ("City of St. Cloud", "Building Department; right-of-way work through Public Works and Engineering", "Patios and decks are on the permit-required list", "Driveway and sidewalk pavers referred to Public Works", "1300 9th St, 407-957-7300"),
           ("Unincorporated Osceola", "County driveway permit required for construction or widening; 24 ft residential maximum under §22-50.6", "Building Office; residential plan review normally 3 to 5 days; NOC at $5,000 and above", "Covered by the driveway permit; right-of-way under LDC 4.12.2", "1 Courthouse Square, Suite 1400, 407-742-0200")],
          caption="Verified on the official pages on 2026-09-10. The jurisdiction pages quote each source in full."),
    eyebrow="Jurisdictions") + sec(
    "What is under the county",
    """<p>USDA Soil Data Access lists Smyrna fine sand as the largest map unit in Osceola County at about 188,635 acres, followed by Myakka fine sand at about 122,954, open water at about 97,698, Immokalee fine sand at about 70,229, depressional Basinger fine sand at about 47,191, Basinger fine sand at about 44,637, EauGallie at about 42,853, ponded Placid at about 38,664, Samsula muck at about 27,882 and Malabar at about 27,596.</p>
<p>Almost all of those are flatwoods soils and almost all are poorly drained. Smyrna, Myakka, Immokalee and EauGallie carry a wet-season water table that comes within about twelve inches of the surface; Basinger is nearer six; the depressional and ponded phases sit at the surface. That single fact drives most of what we do differently here: compacted base, positive slope, designed drainage, and raised slabs on the low lots.</p>""",
    cls="alt") + sec(
    "Communities with architectural review we have verified",
    table(["Community", "Body", "What the published criteria actually say", "Where"],
          [("Poinciana", "APV Design Control Board", "Concrete, asphalt or brick pavers for driveways; walkway adjacent to the dwelling limited to 2 ft without approval; prior written approval required; no answer within 30 days is a disapproval", "401 Walnut St, Poinciana, 863-427-0900"),
           ("Solivita", "Solivita Community Association ARC", "Replacement driveways and walkways in the original builder's style and materials; driveway modifications go through review; samples or photographs with every request", "Within Poinciana"),
           ("Celebration", "Celebration Residential Owners Association ARC", "Approved products, patterns and colours; committee meets the third Monday of each month", "Town Hall, 851 Celebration Ave, 407-566-1200 ext. 2206"),
           ("Bellalago and Isles of Bellalago", "Community association, FirstService Residential", "Architectural review required before exterior changes; applications through the resident portal; committee meets twice monthly", "Resident line 866-378-1099")],
          caption="Communities whose written criteria we have obtained and read. For Storey Lake, Tapestry, Windsor Hills, ChampionsGate sub-associations and Reunion's three managers we have contacts but not verified written criteria, and we say so rather than summarising rules we have not seen.")) + sec(
    "NOAA normals for Kissimmee 2 (1991 to 2020)",
    table(["Month", "Avg high °F", "Avg low °F", "Rain in.", "Days ≥ 0.01 in", "Days ≥ 0.10 in"],
          [("January", "71.8", "48.3", "2.67", "7.6", "4.1"), ("February", "74.4", "50.7", "2.37", "6.5", "4.0"),
           ("March", "77.9", "54.4", "3.07", "6.2", "4.2"), ("April", "83.0", "59.7", "2.43", "5.7", "3.6"),
           ("May", "87.4", "65.8", "4.17", "7.8", "5.7"), ("June", "90.0", "71.8", "9.18", "15.8", "12.3"),
           ("July", "91.5", "73.5", "7.21", "16.7", "12.2"), ("August", "91.4", "74.1", "8.38", "17.7", "13.0"),
           ("September", "89.5", "72.8", "5.88", "14.3", "9.5"), ("October", "84.6", "66.2", "3.07", "8.7", "5.7"),
           ("November", "78.6", "57.3", "1.99", "5.8", "3.1"), ("December", "73.5", "51.5", "2.15", "6.5", "3.5")],
          caption="Station USC00084625, Kissimmee 2, FL, NOAA NCEI U.S. Climate Normals 1991 to 2020. June through September carry about 58 percent of the annual rainfall and 15 to 18 rain days a month, nearly all of it in the afternoon."),
    cls="alt")

SECTIONS["/areas/polk-county/"] = sec(
    "How permitting works on this side of the line",
    """<p>Polk decides by location rather than by activity. Whether a slab needs a permit here depends on where it sits relative to the structure, the setbacks and the right-of-way, not on how big it is or what it is for. That is a genuinely different logic from Osceola's, and it is the thing that catches out homeowners and contractors who move between the two counties.</p>
<p>The consequence for a homeowner is that the plat matters more than the tape measure. Easements and setback lines are recorded rather than visible, and a pad that would be unpermitted flatwork in the middle of a rear yard becomes permitted work, or is not allowed at all, a few feet closer to a boundary. We pull the plat before staking anything on a Polk lot. The rule itself, quoted in full with its source and the office contacts, is on our <a href="/permits/polk-county/">Polk County permit page</a>.</p>""",
    eyebrow="The rule") + sec(
    "The Concrete Driveway Paver Release Form",
    """<p>Where a paver driveway or sidewalk occupies the county right-of-way, Polk County asks the owner to sign a release form, notarised and recorded with the Clerk of Court, accepting responsibility for maintaining that section and indemnifying the county. The form exists because the county has to be able to open the right-of-way for utility work without inheriting an obligation to restore a decorative surface.</p>
<p>It costs nothing but a notary and a recording fee, and it takes a week or two if it is anticipated. It is a common cause of delay when it is not, which is why it goes in our packet on any Polk-side paver job that reaches the right-of-way. The county's offices are at 330 West Church Street in Bartow and at the Northeast Government Center, 200 Government Center Boulevard in Lake Alfred, on 863-534-6080.</p>""",
    cls="alt") + sec(
    "Ridge sand turns the base problem around",
    """<p>Soil Data Access returns a different picture for Polk than for Osceola. The largest map units include Smyrna and Myakka fine sands at about 144,718 acres, but then Candler sand at 0 to 5 percent slopes at about 97,496 acres, Pomona at about 91,570, Tavares at about 53,679, Astatula at about 34,785 and Immokalee at about 30,288. Candler and Astatula are the Lake Wales Ridge soils, deep and excessively drained, and they are what the Davenport, Haines City, Dundee and Lake Wales work sits on.</p>
<p>On those soils the water table is not a design factor and saturation is not the failure mode. Compaction is. Dry single-grained sand shears under a plate compactor rather than densifying, so a base placed and compacted dry looks finished, passes inspection and consolidates when the first heavy storm soaks it. Wetting each lift before compaction, and probing after, is the method, and a proposal that reads identically for a Polk job and an Osceola job has not accounted for it.</p>""") + sec(
    "Cities with their own building departments",
    table(["City or town", "2025 population", "Distance from Kissimmee", "Permitting"],
          [("Davenport", "14,031", "15.3 mi", "City inside the limits; most Davenport-addressed property is county"),
           ("Haines City", "44,215", "17.8 mi", "City department; surrounding area is county"),
           ("Winter Haven", "60,837", "26.1 mi", "City department"),
           ("Auburndale", "21,677", "26.9 mi", "City department"),
           ("Lake Alfred", "9,038", "21.6 mi", "City department; county's northeast office is here"),
           ("Dundee", "5,847", "22.4 mi", "Town inside the limits"),
           ("Lake Wales", "17,748", "28.2 mi", "City department"),
           ("Polk City", "3,007", "26.8 mi", "City inside the limits")],
          caption="Populations from the Florida Economic and Demographic Research 2025 adjusted estimates; distances are straight-line from downtown Kissimmee to the Census internal point of each place."),
    cls="alt")

SECTIONS["/areas/orange-county-south/"] = sec(
    "Orange County permits concrete work that other counties do not",
    """<p>Orange County's published guidance is the most sweeping in our territory: any time you are pouring concrete or placing pavers, a permit is required. That is a real difference from unincorporated Osceola, where a detached patio slab outside setbacks is generally treated as flatwork, and from Polk, where location decides the question.</p>
<p>The county also publishes a specific driveway detail for work in its right-of-way: a minimum of six inches of three thousand psi concrete with no steel reinforcement in the right-of-way section including the sidewalk crossing, and driveways set back a minimum of three feet from the property line. Pavers additionally need a Zoning permit. The Division of Building Safety is at 201 South Rosalind Avenue in Orlando on 407-836-5550.</p>""",
    eyebrow="The rule here") + sec(
    "Which south Orange communities this page covers",
    """<p>This page exists for the part of south Orange County that is close to Kissimmee and is not covered by our sister brands in West Orange. That means the communities along the Osceola line and the southern edge of Orlando: Hunters Creek, Meadow Woods, Southchase, Williamsburg, Taft, Pine Castle, Sky Lake, Oak Ridge and the Lake Hart area. Those are typically a fifteen to twenty-five minute drive from our Kissimmee base, closer than several of the Polk towns we serve.</p>
<p>What this page does not cover is Windermere, Dr. Phillips, Horizon West, Winter Garden, Ocoee, Apopka and the rest of West Orange, or Lake Nona. Those areas have their own coverage elsewhere, and we do not publish competing city pages for them. If you are in one of them and want work from us, call and we will tell you honestly whether we are the right crew for it.</p>""",
    cls="alt") + sec(
    "Soil and drainage on this side of the line",
    """<p>The soils in south Orange are continuous with Osceola's: the same flatwoods association of Smyrna, Myakka, Immokalee and EauGallie fine sands, poorly drained, with a wet-season water table close to the surface, and the same depressional Basinger and Placid phases in the low areas. The base method is therefore the Osceola method rather than the ridge method: compact the subgrade, undercut soft material, build the base in lifts, slope the slab to shed, and design where the water goes.</p>
<p>What differs is the stormwater context. Much of south Orange was developed later and under stricter stormwater rules, so the lots were graded to drain to a designed system of swales, inlets and ponds. A patio or a deck that blocks that route causes a problem for a neighbour rather than for the owner, which is a good reason to establish the lot's drainage path before designing anything.</p>""")
