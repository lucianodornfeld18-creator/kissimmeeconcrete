# -*- coding: utf-8 -*-
"""City×service pages: Davenport (5), Haines City (4), Harmony & Narcoossee (4)."""
from _data import COST_INDEX_RELEASE
from _helpers import cap, table, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, cs
from _cityservice import cs_page

R = COST_INDEX_RELEASE["label"]


def get_pages():
    p = []

    # ------------------------------------------------------------- Davenport
    p.append(cs_page("davenport", "concrete-driveways",
        "Concrete Driveways in Davenport, FL – Polk Rules, Ridge Sand",
        "Concrete driveways in Davenport: Polk County's right-of-way and setback permit rules, city vs. unincorporated addresses, Candler ridge sand that compacts only wet, aprons, current cost per sq ft.",
        f"A concrete driveway in Davenport runs {cost_range('concrete-driveway-broom')} installed ({R} Cost Index), $2 to $4 more to remove an old slab. Most Davenport addresses are unincorporated Polk County, where portions of a driveway in the right-of-way or within setbacks need a permit; the small historic city has its own building rules. The ground is Candler sand, which needs wetting before any base will compact.",
        [
            ("Driveways on the ridge", f"<p>Davenport sits on the Lake Wales Ridge: Candler sand at 0 to 5 percent slopes is the dominant map unit (USDA Soil Data Access, FL105), deep and excessively drained, with no water table to fight and no fines to lock the grains together. Base placed dry reads compacted on the plate and settles the first rainy season, which is why many 2015–2026 builder driveways in Providence, Astonia, Cascades and the Loughman subdivisions already show a dip at the garage. We wet the subgrade and each lift of limerock, compact, probe, and then pour 4 inches of 3,000 to 3,500 psi with fiber and #4 edge bars, or 6 inches with a grid for the boats and campers that Loughman-area lots keep ({guide('paver-base-flatwoods-vs-ridge')}). Slopes matter more here than in Kissimmee: a drive that drops from the street to the garage gets a trench drain at the door.</p>"),
            ("Polk County and the city", f"<p>Unincorporated Polk County: the Building Division FAQ requires a permit for 'sidewalks and portions of driveways in the right of way or within the minimum setbacks', and Building Code and Land Development Code drainage requirements apply; offices at 330 W. Church Street, Bartow, and 200 Government Center Blvd, Lake Alfred (863-534-6080). Inside the historic city limits, the City of Davenport reviews building permits; we did not verify its published flatwork rules and confirm by phone. Solterra and Providence add ARC review; Solterra caps expanded driveways at three cars wide ({hoa('solterra')}). Pages: {juris('polk-county')}, {tool('permit-finder')}.</p>"),
        ],
        ("A Providence two-car replacement", f"<p>20-by-24-foot builder drive (480 square feet), 2012, cracked at the garage on settled base. Removal $960 to $1,920; subgrade wetted and compacted; 4-inch base; new 4-inch drive at $8.50 to $13.50 ($4,080 to $6,480); apron to the county detail. Polk permit for the right-of-way portion, HOA approval, three days. Ranges from the {R} index.</p>"),
        ("Do I need a permit for a driveway in unincorporated Davenport?", "For the part in the county right-of-way or within the setbacks, yes, under Polk County's building rules; a replacement in the same footprint on your lot outside setbacks is treated as flatwork, and drainage requirements apply either way. Inside the historic city limits the City of Davenport's building department reviews it. The permit finder tells you which address you have."),
        [
            faq("Why did my 2018 driveway crack already?", "Base placed dry on ridge sand and compacted by the first rainy season instead of the crew. Rebuilding on a wetted, compacted base fixes it."),
            faq("City or county?", "Most Davenport addresses are county; the historic core is city. The finder checks."),
            faq("How thick for a boat?", "Six inches of 4,000 psi with a #4 grid on chairs."),
            faq("How long?", "Two to three days on site; cars after 7 days."),
        ],
        ["polk-faq", "solterra", "sda"],
        [cs("davenport", "paver-driveways"), cs("davenport", "concrete-slabs"), compare("concrete-vs-pavers")]))

    p.append(cs_page("davenport", "paver-driveways",
        "Paver Driveways in Davenport, FL – Paver Release Form, Ridge Base",
        "Paver driveways in Davenport: Polk County's Concrete Driveway Paver Release Form for pavers in the right-of-way, concrete apron alternative, wetted 6-in base on Candler sand, Providence and Solterra ARC rules, costs.",
        f"A paver driveway in Davenport runs {cost_range('paver-driveway-concrete')} ({R} Cost Index) plus $2 to $4 per square foot to remove old concrete. Polk County asks the owner to record a notarized Concrete Driveway Paver Release Form when pavers reach the county right-of-way; a poured concrete apron avoids it. Base on Davenport's Candler sand is wetted before compaction or it settles the first wet season.",
        [
            ("The release form, or a concrete apron", f"<p>Polk's form (PD BLD 40) has the owner accept maintenance and replacement of pavers in the right-of-way if the county has to dig, indemnify the county, and record the obligation so it runs with the land; it gets notarized and recorded with the Clerk before driveway approval. Most owners avoid it by ending the pavers at a soldier course and pouring the apron in concrete to the county detail, which is also what most HOAs prefer. Our section: 6 inches of limerock wetted and compacted in two lifts, restraint on the base, 80 mm pavers, polymeric sand ({svc('paver-driveways')}; {guide('paver-base-flatwoods-vs-ridge')}).</p>"),
            ("Communities", f"<p>Providence, Astonia, Cascades and Champions Reserve review paver driveways through management ARC forms; Solterra's verified guidelines cap an expanded drive at three cars wide, bar added walking area, and let the board require the installer's insurance certificate ({hoa('solterra')}). Polk permits pavers within setbacks or adjacent to structures under the codes; inside the historic city limits the City of Davenport reviews. Pages: {juris('polk-county')}, {tool('permit-finder')}, {tool('hoa-packet-checklist')}.</p>"),
        ],
        ("A Solterra rental driveway rebuild", f"<p>420-square-foot 2016 builder drive dipped at the garage, no edge restraint. Lifted and rebuilt on a wetted 6-inch base with restraint, same pavers reset with matched replacements, concrete apron kept, polymeric sand, seal at 60 days. At {cost_range('paver-repair')}: $3,780 to $6,720. ARC approval with COI, three days in a turnover gap. Ranges from the {R} index.</p>"),
        ("What is Polk County's Paver Release Form and do I need it?", "It is a notarized, recorded agreement the county requires when pavers are installed in its right-of-way: you accept responsibility for maintaining and replacing them if the county ever has to remove them for utility or road work, and the obligation transfers to future owners. You need it only if the pavers reach the right-of-way; a concrete apron at the street avoids it, and that is what we usually recommend."),
        [
            faq("Concrete apron or pavers to the street?", "A concrete apron avoids the release form and is what most HOAs prefer."),
            faq("Why does the base need wetting?", "Candler sand has no fines; it packs only when wet. Dry base settles the first rainy season."),
            faq("Can you widen in Solterra?", "To three cars wide with ARC approval, no added walking area."),
            faq("How long?", "Three to five days for a new field; two to three for a lift-and-relay."),
        ],
        ["polk-paver-release", "polk-faq", "solterra", "sda"],
        [cs("davenport", "concrete-driveways"), cs("davenport", "concrete-repair"), svc("paver-sealing")]))

    p.append(cs_page("davenport", "paver-pool-decks",
        "Paver Pool Decks in Davenport, FL – Providence, Solterra, Rentals",
        "Paver and travertine pool decks in Davenport: overlays on 2005–2016 decks in Providence and the rental communities, Polk County permit position for decks adjacent to structures, pool backfill on ridge sand, costs.",
        f"A paver overlay on a Davenport pool deck runs {cost_range('paver-pool-deck')} and travertine {cost_range('travertine-pool-deck')} ({R} Cost Index). Polk County's FAQ permits slabs adjacent to a principal structure and intended to support one, so a deck tied to the house or the screen enclosure is confirmed with the Building Division before we schedule; a stand-alone overlay on an existing deck outside setbacks is treated as flatwork. Pool backfill on ridge sand is compacted wet before any rebuild.",
        [
            ("Decks in Providence and the resort subdivisions", f"<p>Providence's 2005–2015 primary homes and the rental communities along US-27 have textured concrete or builder-paver decks inside cages; the concrete ones take a 1-inch remodel paver overlay with new bullnose coping and a channel drain at the screen line, the settled paver ones are rebuilt on wetted, compacted backfill. Owners in Providence choose travertine for the look and the cooler surface; rental owners choose sealed concrete pavers with an anti-slip sealer for cost and durability ({guide('vacation-rental-owner-hardscape-guide')}, {compare('travertine-vs-concrete-pavers')}).</p>"),
            ("Polk County's position", f"<p>The county FAQ lists 'concrete slabs adjacent to a principal or accessory structure, intended for support of a structure, elevated slabs' among permit items and requires pavers adjacent to structures to meet the codes, so we confirm each deck's status with the Building Division (863-534-6080) before scheduling; a screen enclosure replacement is its own permitted structure with footers that go in first. HOA review applies in every community here; Solterra's rules are verified ({hoa('solterra')}). {juris('polk-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Providence travertine overlay", f"<p>600-square-foot deck around a 14-by-28 pool inside a cage, 2008 knock-down concrete, sound. ½-inch tumbled travertine thin-set, bullnose coping, channel drain, penetrating sealer with grit. At {cost_range('travertine-pool-deck')}: $12,000 to $21,600 plus coping. Five days; HOA approval in one cycle. Ranges from the {R} index.</p>"),
        ("Does a pool deck overlay need a Polk County permit?", "An overlay on an existing deck outside the setbacks and not supporting a structure is treated as flatwork. A deck that is adjacent to the house and supports the screen enclosure, or one within the setbacks, falls under the county's slab rules, so we confirm with the Building Division for your address before quoting and put the answer in the proposal."),
        [
            faq("Overlay or rebuild?", "Overlay on a sound deck; rebuild on compacted backfill if the coping settled."),
            faq("Which surface for a rental?", "Sealed concrete pavers with an anti-slip sealer; travertine for a primary home wanting a cooler deck."),
            faq("Is the pool out of use?", "No; swimmers stay out only while coping mortar cures."),
            faq("Who approves?", "Your community's ARC; Solterra's written rules are on our HOA page."),
        ],
        ["polk-faq", "solterra", "icpi"],
        [cs("davenport", "paver-driveways"), svc("paver-sealing"), compare("cool-deck-vs-pavers")]))

    p.append(cs_page("davenport", "concrete-repair",
        "Concrete Repair in Davenport, FL – Early Cracks on Ridge Sand",
        "Concrete repair in Davenport: early cracking and settled aprons on 2012–2026 builder driveways placed on dry ridge sand, historic-town walks and oaks, lift vs. replace, Polk right-of-way notes, costs.",
        f"Concrete repair in Davenport is dominated by early failures on builder driveways from the last decade, settled where the base was placed dry on Candler sand, plus older walks and drives in the historic town. Routing and grinding are minimum-charge visits; a replaced panel or apron runs at new-pour rates ({cost_range('concrete-driveway-broom')}) plus removal. Same-footprint repair needs no permit; an apron in the county right-of-way does.",
        [
            ("Why new driveways here crack early", f"<p>Ridge sand does not compact dry. Production crews set forms and poured the same week on base that had never been wetted, and the first rainy season did the compaction, dropping the apron and cracking the panel at the garage. Repair on those drives means a base rebuilt wet and compacted in lifts under the new section, an apron at 6 inches with edge steel, and an honest word about the other panels, which are on the same base ({compare('resurface-vs-replace')}, {guide('why-concrete-cracks-osceola')}). In the historic town, 1920s–1960s walks are lifted by oaks; those get a root barrier and a replaced panel ({guide('tree-roots-driveways-central-florida')}).</p>"),
            ("Permits", f"<p>Same-footprint repair is not permitted separately in Polk County; sidewalks and driveway portions in the right-of-way or within setbacks are, and drainage requirements apply ({juris('polk-county')}, 863-534-6080). Inside the historic city limits the City of Davenport reviews. HOAs get a note on visible repairs; Solterra bars painting or staining concrete to match ({hoa('solterra')}). {tool('permit-finder')}.</p>"),
        ],
        ("A Cascades garage-edge panel", f"<p>One 10-by-12 panel dropped 1 inch at the garage on a 2019 drive, apron intact. Panel removed ($240 to $480), base wetted and rebuilt, new 4-inch panel doweled and poured ($1,020 to $1,620), joint at the garage. One day. Full-drive replacement quoted alongside because the other panels sit on the same base. Ranges from the {R} index.</p>"),
        ("My Davenport driveway is only five years old and already sinking. Is that normal?", "It is common here, and it is a base problem, not a concrete problem. Candler ridge sand packs only when wet; a base placed dry in summer settles in the first rainy season and takes the slab with it. A panel replaced over a wetted, compacted base stays put; the rest of the drive is on the original base and may follow, which is why we quote both."),
        [
            faq("Lift or replace?", "Lift a sound, uncracked panel after the base is stable; replace a cracked one."),
            faq("Do I need a permit?", "Not for same-footprint repair; the apron in the right-of-way, yes."),
            faq("Can you stain the new panel to match?", "Not in Solterra; elsewhere a light tint, and the color evens out in a year."),
            faq("What about the historic-town walks?", "Root barrier and panel replacement over a compacted base."),
        ],
        ["polk-faq", "solterra", "sda"],
        [cs("davenport", "concrete-driveways"), cs("davenport", "paver-driveways"), svc("concrete-resurfacing")]))

    p.append(cs_page("davenport", "concrete-slabs",
        "Concrete Slabs & Pads in Davenport, FL – Loughman, Workshops",
        "RV, boat, workshop, shed and generator pads in Davenport and Loughman: 6 in / 4,000 psi with rebar for vehicles, wetted base on Candler sand, Polk County's slab permit rules, HOA restrictions, costs.",
        f"Pads in Davenport run {cost_range('concrete-slab-pad')} ({R} Cost Index); a 12-by-40 RV pad at 6 inches with a #4 grid is $6,500 to $9,500 and a 30-by-40 workshop slab $13,800 to $20,400. Polk County permits slabs that support a structure, sit within setbacks or are elevated; a free-standing pad outside setbacks is not permitted separately. Loughman and the Ronald Reagan Parkway corridor have the larger lots where most of this work happens.",
        [
            ("Pads on the ridge", f"<p>The good news about Davenport's Candler sand is drainage: no water table to raise a pad above, no muck. The catch is compaction; the subgrade and every lift of base is wetted before the plate goes over it, or the pad settles the first wet season. RV and boat pads get 6 inches of 4,000 psi with a #4 grid on chairs; workshop slabs for metal buildings get a thickened edge and the anchor-bolt layout from the building supplier; shed, AC and generator pads get 4 inches with fiber, set 2 to 4 inches above grade and sloped ¼ inch per foot ({svc('concrete-slabs')}). Access for a 30-ton mixer is checked on the site visit.</p>"),
            ("Permits and HOAs", f"<p>Polk County FAQ: permits for 'concrete slabs adjacent to a principal or accessory structure, intended for support of a structure, elevated slabs'; all slabs meet setbacks except sidewalks and driveways; pre-manufactured storage buildings are permitted structures. A stand-alone pad outside setbacks is flatwork, and HB 803's $7,500 exemption can apply with a written request. Building Division 863-534-6080. Solterra's guidelines regulate sheds and accessory structures; most HOAs here restrict RV and boat parking to screened areas or prohibit it, so check before pouring a pad ({hoa('solterra')}). {juris('polk-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Loughman RV pad", f"<p>14-by-45-foot pad (630 square feet) beside the garage on a half-acre county lot, no HOA. Subgrade and base wetted and compacted, 6 inches of 4,000 psi with a #4 grid at 18 inches on chairs, raised 3 inches above grade. About 12 cubic yards. At $11.50 to $17: $7,250 to $10,700. Not connected to the street, so no driveway permit; no separate slab permit for a pad outside setbacks. Two days. Ranges from the {R} index.</p>"),
        ("Does an RV pad need a permit in Polk County?", "A pad outside the setbacks that does not support a structure is not permitted separately under the county's slab rules, and HB 803 covers most stand-alone pads under $7,500 with a written request. A pad within a setback, an elevated pad, or one that becomes part of the driveway in the right-of-way is permitted. Your HOA is the bigger question: many Davenport communities prohibit RV parking outright."),
        [
            faq("How thick for an RV?", "Six inches of 4,000 psi with a #4 grid on chairs."),
            faq("Will it settle?", "Not on a base that was wetted and compacted in lifts; that is the whole difference on ridge sand."),
            faq("Can you pour a workshop slab?", "Yes, with a thickened edge and the building supplier's anchor layout; the building itself is permitted as an accessory structure."),
            faq("What about the HOA?", "Check before pouring; most communities here restrict or prohibit RV and boat parking."),
        ],
        ["polk-faq", "hb803", "solterra", "sda"],
        [cs("davenport", "concrete-driveways"), tool("concrete-paver-calculator"), guide("paver-base-flatwoods-vs-ridge")]))

    # ------------------------------------------------------------- Haines City
    p.append(cs_page("haines-city", "concrete-driveways",
        "Concrete Driveways in Haines City, FL – Ridge Sand, City vs. Polk",
        "Concrete driveways in Haines City: replacement on the older US-17/92 streets, extensions in the 2015–2026 subdivisions, city vs. Polk County permits, Candler ridge base wetted before compaction, costs.",
        f"A concrete driveway in Haines City runs {cost_range('concrete-driveway-broom')} installed ({R} Cost Index), plus $2 to $4 per square foot for removal. Inside the city limits the City of Haines City's building division reviews the work (we confirm its flatwork rules by phone); unincorporated addresses follow Polk County's right-of-way and setback rules. The ground is Candler and Tavares sand on the Lake Wales Ridge, and base is wetted before compaction or it settles.",
        [
            ("Two kinds of Haines City driveway", f"<p>The 1920s–1990s streets around Lake Eva and off Hinson Avenue and US-17/92 have small lots, narrow drives and mature oaks; the work is tear-out and replacement with a straight expansion joint at the apron and a root barrier where an oak is close. The 2015–2026 subdivisions along US-27 and Ernie Caldwell Boulevard (Hammock Reserve, Magnolia Park, Bradbury Creek, Tower Lakes) have 16-foot builder drives poured on dry-placed base that cracked early; the work there is extensions to fit a third car and replacement of the cracked panel over a wetted, compacted base ({guide('paver-base-flatwoods-vs-ridge')}). Spec: 4 inches of 3,000 to 3,500 psi with fiber and #4 edge bars on 4 inches of compacted limerock; 6 inches with a grid where a boat or camper parks.</p>"),
            ("City or county", f"<p>Unincorporated Polk County: permits for sidewalks and driveway portions in the right-of-way or within setbacks, drainage requirements apply, Building Division 863-534-6080 (Bartow or Lake Alfred). City of Haines City: its building division reviews permits inside the limits; we did not verify its published flatwork rules for this page and confirm before quoting. The subdivisions' HOAs review extensions through management ARC forms ({tool('hoa-packet-checklist')}). Pages: {juris('polk-county')}, {tool('permit-finder')}.</p>"),
        ],
        ("A Hammock Reserve extension", f"<p>16-foot builder drive extended 6 feet over 24 feet of length (144 square feet) and one cracked garage panel replaced (120 square feet). Extension at $8.50 to $13.50 ($1,220 to $1,940); panel removal and replacement ($1,260 to $2,100); base wetted and compacted under both; apron extended to the county detail. HOA approval, Polk permit for the right-of-way portion, two days. Ranges from the {R} index.</p>"),
        ("Does Haines City have its own building department?", "Yes for addresses inside the city limits; unincorporated addresses with a Haines City ZIP use Polk County. We did not verify the city's published rules for flatwork, so for city addresses we call before quoting and put the answer in the proposal. The permit finder shows which side of the line you are on."),
        [
            faq("Why did my 2020 driveway crack?", "Dry-placed base on ridge sand, compacted by the first rainy season. Rebuilding the base wet under the new section fixes it."),
            faq("Can I extend to fit a third car?", "Within the setback and with HOA approval; the Polk right-of-way portion is permitted."),
            faq("How thick?", "Four inches for cars, six with a rebar grid for boats and campers."),
            faq("How long?", "Two to three days on site; cars after 7 days."),
        ],
        ["polk-faq", "sda", "edr"],
        [cs("haines-city", "paver-driveways"), cs("haines-city", "concrete-repair"), compare("concrete-vs-pavers")]))

    p.append(cs_page("haines-city", "concrete-patios",
        "Concrete Patios in Haines City, FL – Lanai Extensions, Ridge Lots",
        "Concrete patios and lanai extensions in Haines City: 4-in slabs on wetted ridge base, drainage on sloped lots, Polk County's slab permit position, HOA review in the new subdivisions, 12x12 and 16x20 costs.",
        f"A concrete patio in Haines City runs {cost_range('concrete-patio')} ({R} Cost Index); a 12-by-12 slab is about $1,300 to $1,900 and a 16-by-20 lanai extension $2,600 to $4,000. A detached patio outside the setbacks is flatwork in Polk County; a slab under a screen room is permitted with the enclosure. Ridge lots drain well but slope, so the slab is set to fall away from the house and the base is wetted before compaction.",
        [
            ("Patios on sloped ridge lots", f"<p>Haines City's newer subdivisions sit on the ridge's rolling ground, and a back yard that falls 2 feet across the lot is common; the patio is stepped or the low side is built up on compacted fill so the slab still falls ⅛ inch per foot away from the house. On the older, flatter streets near Lake Eva the yard is level and a slot drain at the far edge handles the water. Spec: 4 inches of 3,000 psi with fiber on 2 to 4 inches of wetted, compacted base, doweled into an existing lanai slab, broom finish ({svc('concrete-patios')}). If a screen enclosure is coming, its footers change the slab edge; tell us first.</p>"),
            ("Permits and HOA", f"<p>Polk County: slabs adjacent to a structure and intended to support one, within setbacks, or elevated are permitted; a detached patio outside setbacks is not permitted separately, and HB 803's $7,500 exemption can apply with a written request; Building Division 863-534-6080. Inside the city limits, confirm with the city's building division. Hammock Reserve, Magnolia Park, Southern Dunes and the other subdivisions review patios through management ARC forms ({tool('hoa-packet-checklist')}). {juris('polk-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Magnolia Park lanai extension", f"<p>Existing 10-by-14 lanai slab extended to 16 by 24 (244 square feet added) on a lot that falls 14 inches across the yard; low side built up on compacted fill, slab doweled and sloped away from the house, broom finish. At {cost_range('concrete-patio')}: $1,950 to $3,050 plus fill. HOA approval, two days. Ranges from the {R} index.</p>"),
        ("Do I need a permit for a patio slab in Haines City?", "Outside the city, a detached patio slab outside the setbacks is flatwork under Polk County's rules and is not permitted separately; a slab that supports a screen room or sits within a setback is. Inside the city limits the city's building division decides, and we confirm by phone. HOA approval is required in every subdivision built since 2000."),
        [
            faq("How do you handle a sloped yard?", "Build up the low side on compacted fill or step the slab; the top always falls away from the house."),
            faq("Broom or smooth?", "Broom outdoors; smooth under a solid roof only."),
            faq("Can you extend my lanai slab?", "Yes, doweled with an expansion joint at the seam."),
            faq("How soon can I use it?", "Furniture after 3 days, a hot tub after 28."),
        ],
        ["polk-faq", "hb803", "sda"],
        [cs("haines-city", "concrete-driveways"), svc("paver-patios"), compare("stamped-vs-pavers")]))

    p.append(cs_page("haines-city", "concrete-repair",
        "Concrete Repair in Haines City, FL – Early Cracks, Old Walks",
        "Concrete repair in Haines City: early cracking on 2016–2026 builder driveways, settled aprons on ridge sand, oak-lifted walks near Lake Eva, lift vs. replace with costs, Polk and city permit notes.",
        f"Concrete repair in Haines City splits between the new subdivisions, where builder driveways poured on dry-placed ridge base cracked within five years, and the historic streets, where 1920s–1960s walks and drives are lifted by oaks. Routing and grinding are minimum-charge visits; a replaced panel runs at new-pour rates ({cost_range('concrete-driveway-broom')}) plus removal. Same-footprint repair needs no permit; the apron in the right-of-way does.",
        [
            ("New-subdivision cracks", f"<p>Hammock Reserve, Magnolia Park, Bradbury Creek and Tower Lakes drives were poured on base that was never wetted on Candler sand; the first rainy season compacted it and the slab cracked at the garage and dropped at the apron. A panel replaced over a wetted, compacted base stays put; the other panels are on the original base, so we quote the panel and the drive ({compare('resurface-vs-replace')}, {guide('why-concrete-cracks-osceola')}). Aprons broken by delivery trucks are replaced at 6 inches with edge steel.</p>"),
            ("Historic streets and permits", f"<p>Around Lake Eva and off Hinson Avenue, oaks planted decades ago lift walk and drive panels; grinding handles a lip under ¾ inch, a root barrier and a replaced panel handle more ({guide('tree-roots-driveways-central-florida')}). Same-footprint repair is not permitted separately in Polk County; sidewalks and driveway portions in the right-of-way are ({juris('polk-county')}, 863-534-6080). Inside the city limits, confirm with the city's building division. HOAs get a note on visible repairs. {tool('permit-finder')}.</p>"),
        ],
        ("A Bradbury Creek garage panel and apron", f"<p>One 10-by-12 garage panel cracked and dropped ¾ inch on a 2021 drive, apron corner broken. Panel removed and replaced over a wetted base ($1,260 to $2,100); apron corner (30 square feet) at 6 inches with edge bars ($345 to $510 plus $60 to $120 removal). One day; full-drive replacement quoted alongside. Ranges from the {R} index.</p>"),
        ("Is early cracking on a new Haines City driveway covered by the builder?", "Sometimes, within the builder's warranty period and terms, and it is worth asking before paying for a repair; we provide photos and a written assessment. Outside warranty, the fix is a panel replaced over a properly wetted and compacted base, and an honest look at whether the other panels will follow."),
        [
            faq("Lift or replace?", "Lift an uncracked panel once the base is stable; replace a cracked one over a rebuilt base."),
            faq("Do I need a permit?", "Not for same-footprint repair; yes for the apron in the right-of-way."),
            faq("Can you grind the walk lip?", "Under ¾ inch, same week; more than that, a panel over a root barrier."),
            faq("Will the new panel match?", "Lighter for a year; a straight seam makes it read as intentional."),
        ],
        ["polk-faq", "sda"],
        [cs("haines-city", "concrete-driveways"), cs("haines-city", "paver-driveways"), svc("concrete-resurfacing")]))

    p.append(cs_page("haines-city", "paver-driveways",
        "Paver Driveways in Haines City, FL – New Subdivisions, Polk Rules",
        "Paver driveways in Haines City: upgrades and first sealing in the 2015–2026 subdivisions, wetted 6-in base on ridge sand, Polk County's Paver Release Form vs. a concrete apron, HOA approval, costs.",
        f"A paver driveway in Haines City runs {cost_range('paver-driveway-concrete')} ({R} Cost Index) plus $2 to $4 per square foot to remove old concrete. Pavers in the county right-of-way need Polk's recorded Paver Release Form; a concrete apron avoids it. The ridge's Candler sand needs a wetted, compacted base, and the new subdivisions' HOAs approve blends from the major manufacturers' catalogs.",
        [
            ("Upgrading a builder concrete drive to pavers", f"<p>Most requests in Hammock Reserve, Southern Dunes, Randa Ridge and Highland Meadows are to replace a cracked 16-foot builder drive with pavers and widen at the same time. Section: old concrete out, subgrade wetted and compacted, 6 inches of limerock in wetted lifts, restraint on the base, 80 mm pavers in an HOA-approved blend with a soldier border, concrete apron to the county detail, polymeric sand, seal at 60 days ({svc('paver-driveways')}; {guide('paver-base-flatwoods-vs-ridge')}). Builder paver drives in the newest phases need their first seal and, often, edge restraint they never had ({svc('paver-repair')}).</p>"),
            ("Polk County and the HOAs", f"<p>Pavers within setbacks or adjacent to structures must meet the codes; pavers in the right-of-way need the owner's notarized, recorded Concrete Driveway Paver Release Form, which a concrete apron avoids; Building Division 863-534-6080. Inside the city limits, confirm with the city. HOAs review material and color through management ARC forms ({tool('hoa-packet-checklist')}). {juris('polk-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Southern Dunes concrete-to-paver conversion", f"<p>16-by-26-foot builder drive (416 square feet) replaced and widened to 22 feet (572 square feet). Removal $830 to $1,660; pavers at $14 to $22 ($8,010 to $12,580); concrete apron; seal at 60 days. HOA approval, Polk permit for the right-of-way portion, four days. Ranges from the {R} index.</p>"),
        ("Do I have to sign the Paver Release Form for a paver driveway in Haines City?", "Only if the pavers extend into the county right-of-way. The form has you accept maintenance and replacement of those pavers if the county ever digs, and it is recorded against the property. Ending the pavers at a soldier course and pouring the apron in concrete avoids the form and is what most HOAs prefer anyway."),
        [
            faq("Why wet the base?", "Ridge sand packs only when wet; dry base settles the first rainy season."),
            faq("Can I widen at the same time?", "Within the setback and with HOA approval; yes, and it is cheaper together."),
            faq("Concrete apron or pavers to the street?", "Concrete apron; it avoids the release form."),
            faq("How long?", "Three to five days after approval and permit."),
        ],
        ["polk-paver-release", "polk-faq", "sda"],
        [cs("haines-city", "concrete-driveways"), svc("paver-sealing"), compare("concrete-vs-pavers")]))

    # ------------------------------------------------------------- Harmony & Narcoossee
    p.append(cs_page("harmony", "concrete-driveways",
        "Concrete Driveways in Harmony & Narcoossee, FL – Wet Ground",
        "Concrete driveways in Harmony, Narcoossee and Sunbridge: extensions on new lots, long ranchette drives, slabs raised above a surface water table on EauGallie and Basinger sand, septic clearances, Osceola permits, costs.",
        f"A concrete driveway in Harmony or the Narcoossee corridor runs {cost_range('concrete-driveway-broom')} installed ({R} Cost Index), with fill to raise the slab above the seasonal water table priced separately and needed more often here than anywhere else we work. Unincorporated Osceola County's driveway permit and 24-foot rule apply; some Sunbridge addresses are confirmed with St. Cloud. Ranchette drives are quoted by the foot after a truck-access check.",
        [
            ("Building above the water", f"<p>This is the county's low east side: EauGallie fine sand, Smyrna, and Basinger fine sand in the sloughs, with a wet-season water table from the surface to about 12 inches (USDA Soil Data Access, FL097). A driveway poured flush with the lawn sits in water every June and settles unevenly by the third summer. We set the slab on compacted fill 4 to 8 inches above the seasonal high, slope it to a swale, and run downspouts past the edge; on the newest lots in Weslyn Park and Nova Grove the builder's grading usually gives us the elevation, on the ranchettes we build it. Spec: 4 inches of 3,000 to 3,500 psi with fiber and #4 edge bars on 4 inches of compacted limerock, or 6 inches with a grid where boats and trailers park, which on ranchettes is standard ({guide('paver-base-flatwoods-vs-ridge')}).</p>"),
            ("Permits, septic, access", f"<p>Osceola County driveway permit for construction or widening under §22-50.6, 24-foot maximum, Building Office 407-742-0200; Harmony's HOA and the Sunbridge associations review visible changes; some Sunbridge phases carry St. Cloud addresses and are confirmed with the city ({juris('osceola-county')}, {juris('city-of-st-cloud')}, {tool('permit-finder')}). Every ranchette drive is routed clear of the septic tank and drainfield from the county record ({guide('septic-drainfield-concrete-driveway')}), and truck access across pasture and culverts is checked before we quote; a pump or buggy is priced if a 30-ton mixer cannot reach.</p>"),
        ],
        ("A Narcoossee ranchette drive", f"<p>200-foot drive, 12 feet wide (2,400 square feet) from Jones Road to a garage, over ground that floods in June. Fill and compaction to raise the profile ($3,500 to $6,000 priced separately), 4 inches of limerock, 4-inch slab with fiber and edge bars at $8.50 to $13.50 ($20,400 to $32,400), 6-inch turnaround for the boat trailer, swale both sides. Drainfield located and avoided. Five days. Ranges from the {R} index.</p>"),
        ("Do Harmony and Sunbridge lots have drainage problems for driveways?", "The ground does: EauGallie and Basinger sands hold water at or near the surface for weeks each summer. The builders' lot grading in Harmony, Weslyn Park and Nova Grove usually keeps the driveway above it; the problem shows up on extensions and on ranchettes where the drive runs through low ground. The fix is elevation and a swale, not thicker concrete, and it is priced as fill in the proposal."),
        [
            faq("Why does my new driveway sit in water?", "It was poured flush with grade on wet-season ground. Raising it on compacted fill with a swale fixes it."),
            faq("Can a mixer truck reach my lot?", "We check on the site visit; a pump or buggy is priced if not."),
            faq("Is Sunbridge in St. Cloud?", "Parts carry St. Cloud addresses while sitting in unincorporated Osceola; the finder and a call settle it."),
            faq("Do you avoid the drainfield?", "Always; we locate it from the county record first."),
        ],
        ["osceola-22-50-6", "osceola-faq", "stcloud-permits", "sda"],
        [cs("harmony", "concrete-slabs"), cs("harmony", "paver-driveways"), guide("septic-drainfield-concrete-driveway")]))

    p.append(cs_page("harmony", "concrete-slabs",
        "Concrete Slabs & Pads in Harmony & Narcoossee, FL – Raised Pads",
        "Shed, RV, boat, workshop and generator pads in Harmony and the Narcoossee ranchettes: raised 4–8 in above a surface water table on EauGallie and Basinger sand, septic clearances, truck access, Osceola permit rules, costs.",
        f"Pads in Harmony and Narcoossee run {cost_range('concrete-slab-pad')} ({R} Cost Index) plus fill, because on this ground a pad flush with the lawn sits in water every summer. RV and boat pads are 6 inches of 4,000 psi with a #4 grid; shed and generator pads 4 inches with fiber; all raised 4 to 8 inches on compacted fill with the top sloped ¼ inch per foot. Osceola permits the shed, not the pad; a pad connected to the street becomes a driveway.",
        [
            ("Why pads here get built up", f"<p>Basinger fine sand's wet-season water table is at 6 inches, depressional Basinger and Placid at the surface, EauGallie and Smyrna around 12 (USDA Soil Data Access). A generator pad poured at grade is under water in a tropical storm, which is exactly when the generator needs to run. So the pad sits on compacted fill above the seasonal high, with a swale, and the equipment sits on the pad. Ranchette workshop slabs get a thickened edge and the building supplier's anchor layout; RV and boat pads get 6 inches with a grid on chairs ({svc('concrete-slabs')}). Mixer access across pasture, culverts and soft ground is checked before we quote.</p>"),
            ("Permits, septic, HOA", f"<p>Osceola publishes shed permit requirements and permits the shed as an accessory structure with the slab inspected under it; a pad with nothing on it outside setbacks is not permitted separately, and HB 803's $7,500 exemption can apply with a written request; a pad connected to the street needs the driveway permit and fits the 24-foot rule ({juris('osceola-county')}, 407-742-0200). Every rural pad is located clear of the septic tank and drainfield ({guide('septic-drainfield-concrete-driveway')}). Harmony's HOA reviews visible accessory structures ({tool('hoa-packet-checklist')}). {tool('permit-finder')}.</p>"),
        ],
        ("A Harmony generator pad and a ranchette boat pad", f"<p>Generator pad 4 by 8 feet raised 6 inches on compacted fill, 4-inch slab with a #4 grid: $500 to $900 with the small-job minimum. Boat pad on a Bass Road ranchette, 14 by 40 feet (560 square feet) at 6 inches with a grid, raised 6 inches: fill $1,200 to $2,000 plus slab at $11.50 to $17 ($6,440 to $9,520). Two days. Ranges from the {R} index.</p>"),
        ("Does a generator pad need a permit in Osceola County?", "The pad itself, no; the generator's electrical and gas connections are permitted by the licensed trades that install them, and the inspector will look at the pad then. Manufacturer clearances from the house govern where it goes. On this ground the pad is raised above the wet-season water so the unit stays dry in the storms it exists for."),
        [
            faq("How high should the pad be?", "Four to eight inches above grade on this ground, more in a Basinger low."),
            faq("Can you pour a pad over the drainfield?", "No; we locate it from the county record and stay clear."),
            faq("How thick for a boat pad?", "Six inches of 4,000 psi with a #4 grid on chairs."),
            faq("Will the truck reach?", "Checked on the site visit; pump or buggy priced if not."),
        ],
        ["osceola-faq", "hb803", "sda"],
        [cs("harmony", "concrete-driveways"), tool("concrete-paver-calculator"), guide("paver-base-flatwoods-vs-ridge")]))

    p.append(cs_page("harmony", "paver-driveways",
        "Paver Driveways in Harmony & Sunbridge, FL – Rebuilds, First Seal",
        "Paver driveways in Harmony, Weslyn Park, Nova Grove and Bridgewalk: rebuilding 2005-era Harmony pavers on a drained base, first sealing and edge restraint on new builder drives, Osceola permit and 24-ft rule, costs.",
        f"A paver driveway rebuild in Harmony runs {cost_range('paver-repair')} as a lift-and-relay or {cost_range('paver-driveway-concrete')} as a new field ({R} Cost Index). Harmony's 2003–2015 builder pavers are twenty years old and settling where drainage was never addressed; the 2019–2026 Sunbridge communities have new pavers that need edge restraint and a first seal. Osceola County's driveway permit applies to widening; some Sunbridge addresses are confirmed with St. Cloud.",
        [
            ("Twenty-year-old pavers on wet ground", f"<p>Harmony's alley-loaded and front-loaded drives were built on 3 to 4 inches of base over sand that holds water 12 inches down, and the dips at the garage and the rolled outside course are what that produces after two decades of wet seasons. The rebuild is a lift-and-relay on 6 inches of compacted base with the subgrade drained to a swale, restraint on the base, the original pavers reset with matched replacements at the seams ({svc('paver-repair')}; base on flatwoods sand in {guide('paver-base-flatwoods-vs-ridge')}). In Weslyn Park, Nova Grove and Bridgewalk the builder drives are new and the missing pieces are edge restraint and the first seal after efflorescence clears ({svc('paver-sealing')}).</p>"),
            ("Approvals", f"<p>Harmony's HOA and the Sunbridge associations review visible changes; the packet is the survey markup, blend, pattern and border ({tool('hoa-packet-checklist')}). Osceola County driveway permit for widening under §22-50.6, 24-foot maximum, Building Office 407-742-0200; Sunbridge phases with St. Cloud addresses are confirmed with the city, which refers driveway pavers to Public Works ({juris('osceola-county')}, {juris('city-of-st-cloud')}, {tool('permit-finder')}). Apron in concrete to the county detail.</p>"),
        ],
        ("A Harmony lift-and-relay with drainage", f"<p>440-square-foot 2006 driveway dipped 2 inches at the garage, lawn edge rolled. Lifted, base rebuilt to 6 inches, a swale cut along the low side and the downspout extended, restraint set, original pavers reset with 24 matched replacements, polymeric sand, seal at 60 days. At {cost_range('paver-repair')}: $3,960 to $7,040. HOA approval, three days. Ranges from the {R} index.</p>"),
        ("Why is my Harmony paver driveway sinking after all these years?", "Thin base over sand that is saturated for weeks each summer, plus a downspout or the lawn's irrigation feeding the edge. The pavers themselves are fine; the base under them slowly lost support. A lift-and-relay on a thicker, drained base with edge restraint puts the same pavers back for another twenty years."),
        [
            faq("Do you reuse the original pavers?", "Yes; matched replacements go at the seams for broken units."),
            faq("Is a permit needed to relay in the same footprint?", "No; widening needs the county driveway permit."),
            faq("What do the new Sunbridge drives need?", "Edge restraint on the base and a first seal with polymeric sand after 60 to 90 days."),
            faq("How long?", "Two to three days for a lift-and-relay."),
        ],
        ["osceola-22-50-6", "stcloud-permits", "icpi", "sda"],
        [cs("harmony", "concrete-driveways"), cs("harmony", "paver-pool-decks"), guide("polymeric-sand-guide")]))

    p.append(cs_page("harmony", "paver-pool-decks",
        "Paver Pool Decks in Harmony & Sunbridge, FL – New Decks, Drainage",
        "Paver and travertine pool decks in Harmony, Weslyn Park and the Narcoossee communities: new decks with new pools, overlays on 2005-era Harmony decks, lanai drains on wet ground, Osceola flatwork rules, costs.",
        f"A paver overlay on a Harmony pool deck runs {cost_range('paver-pool-deck')} and a travertine deck {cost_range('travertine-pool-deck')} ({R} Cost Index). Half the pool-deck work here is new decks coordinated with pool builders on Sunbridge lots; the other half is overlays on Harmony's 2003–2015 decks. Drainage is the design question on this ground: the lanai drain has to reach a swale or the yard drain, because the soil will not take it.",
        [
            ("New decks and old decks", f"<p>On a new pool in Weslyn Park or Nova Grove we come in after the shell and bond beam, compact the backfill in lifts (uncompacted backfill on this sand settles the deck within two summers), build 4 inches of base and sand-set 60 mm pavers or 1¼-inch travertine with mortar-set bullnose coping and a channel drain at the screen line tied to the lot's drainage. On Harmony's older decks we overlay sound concrete with 1-inch remodel pavers or ½-inch travertine tile and new coping, or rebuild decks that settled. Heat: light travertine and marble measure coolest in published comparisons ({compare('travertine-vs-concrete-pavers')}); sealers get an anti-slip additive.</p>"),
            ("Permits and HOA", f"<p>A deck built with a new pool is under the pool permit; an overlay on an existing deck outside setbacks is flatwork in Osceola County; a deck tied to the bond beam or the screen footer is confirmed with the Building Office (407-742-0200). Harmony's HOA and the Sunbridge associations review visible changes ({tool('hoa-packet-checklist')}). {juris('osceola-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Weslyn Park new-pool deck", f"<p>680-square-foot deck around a 14-by-30 pool on a new lot, after the pool builder's shell and cage footers. Backfill compacted in lifts, 4-inch base, 60 mm pavers in the community blend, bullnose coping, channel drain to the lot's yard drain. At patio rates ({cost_range('paver-patio')}) plus coping: $8,840 to $14,280 plus $28 to $55 per linear foot of coping. Four days. Ranges from the {R} index.</p>"),
        ("Where should a pool deck drain on a Harmony lot?", "To the lot's drainage system, a swale or a yard drain, through a channel drain at the screen line. The soil here (EauGallie, Smyrna, Basinger) is saturated for weeks in summer and will not absorb deck runoff, so a deck that simply sheds water to the cage footer floods the lanai and undermines the slab. Every deck we build here has a piped or graded route for the water."),
        [
            faq("Do you work with pool builders?", "Yes; we come in after the shell, bond beam and cage footers and coordinate coping heights."),
            faq("Why compact the backfill?", "Uncompacted pool backfill on this sand settles the deck within two summers."),
            faq("Overlay or rebuild on a 2005 Harmony deck?", "Overlay if sound; rebuild if the coping settled or the deck sounds hollow."),
            faq("Which surface stays coolest?", "Light travertine and marble, per published measurements; we plan to measure decks here in July."),
        ],
        ["osceola-faq", "icpi", "sda"],
        [cs("harmony", "paver-driveways"), svc("paver-travertine"), compare("cool-deck-vs-pavers")]))

    return p
