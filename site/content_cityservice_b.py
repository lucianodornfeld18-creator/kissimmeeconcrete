# -*- coding: utf-8 -*-
"""City×service pages: Buenaventura Lakes (4), Four Corners (4), ChampionsGate (4), Reunion (4)."""
from _data import COST_INDEX_RELEASE
from _helpers import cap, table, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, cs
from _cityservice import cs_page

R = COST_INDEX_RELEASE["label"]


def get_pages():
    p = []

    # ------------------------------------------------------------- Buenaventura Lakes
    p.append(cs_page("buenaventura-lakes", "concrete-driveways",
        "Concrete Driveways in Buenaventura Lakes, FL – 1980s Replacement",
        "Replacing a 1978–1995 Landstar-era driveway in Buenaventura Lakes: what is under the old slab, Osceola County driveway permit and 24-ft rule, oaks, two-car costs from the Cost Index.",
        f"A BVL driveway replacement runs {cost_range('concrete-driveway-broom')} for the new 4-inch slab plus $2 to $4 per square foot to remove the old one ({R} Cost Index): roughly $4,200 to $8,400 all-in for a 400- to 480-square-foot two-car drive. BVL is unincorporated Osceola County, so the county driveway permit and the 24-foot width rule apply, and there is no HOA on most streets. Two to three days on site.",
        [
            ("What comes out of a BVL driveway", f"<p>Landstar poured these drives from the late 1970s into the early 1990s as 4-inch slabs directly on graded Smyrna and Myakka fine sand, no base, no edge steel, joints far apart. Forty summers of a 12-inch water table and a downspout at the slab edge later, the pattern is the same on every street off Buenaventura Boulevard and Florida Parkway: a stepped panel at the garage, a diagonal crack from the apron corner, panels rocking on washed-out sand. When it comes out we find clean sand under it, which is good news: proof-rolled and topped with 4 inches of compacted limerock, it is a fine subgrade. Our replacement is 4 inches of 3,000 to 3,500 psi with fiber and #4 edge bars, joints at 10 feet cut within 12 hours, sloped to the street, downspouts extended past the slab. The full walkthrough with photos is {guide('buenaventura-lakes-driveway-replacement')}.</p>"),
            ("Permit, width and oaks", f"<p>BVL is entirely unincorporated Osceola County: a county driveway permit is required for construction or widening under §22-50.6, width is capped at 24 feet without a conditional use, the Building Office at 1 Courthouse Square (407-742-0200) reviews residential applications in about 3 to 5 days, and jobs of $5,000 or more record a Notice of Commencement. Many BVL drives were widened over the years with an unpermitted ribbon; we measure the total before quoting a widening. Live oaks planted in the 1980s now lift the drive edge and the walk on many lots; a root barrier at pour time costs little ({guide('tree-roots-driveways-central-florida')}). Pages: {juris('osceola-county')}, {tool('permit-finder')}.</p>"),
        ],
        ("A typical BVL two-car replacement", f"<p>18-by-24-foot drive (432 square feet), 1984 slab in four panels with a 2-inch garage step and a broken apron corner. Removal $860 to $1,730, new 4-inch drive at $8.50 to $13.50 ($3,670 to $5,830), apron to the county detail, root barrier at the oak ($250 to $400). Three days after the county permit; cars on day 10. Ranges from the {R} index, not a quote.</p>"),
        ("Should I replace my BVL driveway in concrete or pavers?", "Most BVL owners choose concrete: it costs about 40 percent less than pavers, matches the street, and with a real base and edge steel it will outlast the original by decades. Pavers make sense if you want the look, expect utility work through the drive, or plan to widen later with matching units; the comparison page has the numbers. Resurfacing is rarely right in BVL because the slabs are moving, not just worn."),
        [
            faq("Do I need a permit in BVL?", "Yes; the Osceola County driveway permit for a new or widened driveway. We pull it."),
            faq("Can I go wider than 24 feet?", "Only with a conditional use approved by the county. Most BVL lots fit 20 to 24 feet."),
            faq("What if only one panel is bad?", "We price the panel and the full replacement; in BVL the other panels are usually on the same clock."),
            faq("How long before I can park?", "Seven days for cars, 28 for heavy vehicles."),
        ],
        ["osceola-22-50-6", "osceola-faq", "sda"],
        [cs("buenaventura-lakes", "paver-driveways"), cs("buenaventura-lakes", "concrete-repair"), compare("concrete-vs-pavers")]))

    p.append(cs_page("buenaventura-lakes", "concrete-repair",
        "Concrete Repair in Buenaventura Lakes, FL – Panels and Aprons",
        "Concrete repair on Buenaventura Lakes' 1980s driveways and walks: stepped garage panels, apron corners, trip hazards, when a single-panel repair makes sense and when the whole drive is due, costs.",
        f"Single-panel replacement on a BVL driveway runs at new-pour rates ({cost_range('concrete-driveway-broom')}) plus removal, so a 10-by-12 garage-edge panel is roughly $1,100 to $1,900; routing cracks or grinding a walk lip is a minimum-charge visit. Because BVL drives are 35 to 45 years old, we always price the panel and the full replacement side by side. Same-footprint repair needs no county permit.",
        [
            ("The BVL failure set", f"<p>Stepped panel at the garage from roof water washing out the sand; diagonal crack from the apron corner where trucks turn in; center panels rocking on voids; front walk lifted at the oak; apron edge crumbling where the county's road overlay raised the street. Each has a repair: fix the downspout then replace or lift the panel; replace the apron section at 6 inches with edge steel; grind or replace the walk panel over a root barrier. Each also has a limit: a panel repair on a drive whose other panels show the same hairline pattern buys two to four years, which is fine if that is the plan ({compare('resurface-vs-replace')}).</p>"),
            ("Lifting versus replacing here", f"<p>Polyurethane lifting is sold hard in BVL and it works on a sound slab with a small dry void once the water is fixed. It does not work on a cracked-through 1980s garage panel that carries the car; the foam lifts the pieces and they keep moving. Our rule: lift a sound panel under ten years old, replace a cracked one, and replace the drive when a third of the panels have moved. No county permit for same-footprint repair; the apron in the right-of-way is under the driveway permit ({juris('osceola-county')}).</p>"),
        ],
        ("A stepped garage panel on Florida Parkway", f"<p>10-by-12 panel stepped 1¾ inches at the garage, 1986 drive, other panels level with hairlines. Downspout extended, panel removed ($240 to $480), base rebuilt, new panel doweled and poured ($1,020 to $1,620), joint at the garage. One day plus cure; full-drive replacement quoted alongside at $4,200 to $8,400. Ranges from the {R} index.</p>"),
        ("Why is my BVL driveway sinking at the garage?", "The roof edge or a downspout dumps every storm at the slab edge, and Smyrna sand loses support quickly once water runs through it; the panel drops and cracks. It is the single most common driveway failure in the neighborhood. Extend the downspout past the slab first; then the panel can be lifted or replaced and it will stay put."),
        [
            faq("Can you fix just the one panel?", "Yes, and we price the whole drive alongside so you can decide."),
            faq("Is lifting worth it in BVL?", "For a sound panel after the water is fixed; not for a cracked 1980s panel."),
            faq("Do you need a permit?", "Not for same-footprint repair; the apron in the right-of-way is under the driveway permit."),
            faq("What about the walk lip at the oak?", "Grind under ¾ inch; replace the panel over a root barrier above that."),
        ],
        ["osceola-22-50-6", "sda"],
        [cs("buenaventura-lakes", "concrete-driveways"), cs("buenaventura-lakes", "concrete-resurfacing"), guide("why-concrete-cracks-osceola")]))

    p.append(cs_page("buenaventura-lakes", "concrete-resurfacing",
        "Concrete Resurfacing in Buenaventura Lakes, FL – When It Works",
        "Concrete resurfacing in Buenaventura Lakes: the minority of 1980s slabs that are worn but not moving, overlay cost vs. replacement, what a tap test shows, and why most BVL drives need a new pour instead.",
        f"Resurfacing a sound BVL slab with a polymer overlay runs {cost_range('concrete-resurfacing')} ({R} Cost Index), about half of a new pour, and it is the right answer for perhaps one drive in five here: the ones that were poured on better ground, never had a downspout at the edge, and are worn and stained rather than cracked and stepped. For the rest, an overlay follows the movement within a season and the money is better spent on replacement.",
        [
            ("The test that decides", f"<p>We tap the slab with a hammer for hollow spots, run a string line across the panels for offsets, and hose the drive to see where water goes. Hairline cracks, no offset, solid sound: resurface. Any panel stepped more than ¼ inch, any hollow area, or a crack you can fit a coin into: replace ({compare('resurface-vs-replace')}). On a resurfacing, cracks are routed and filled, the surface is pressure-washed and etched or ground, rust from well irrigation is removed with the right cleaner ({guide('rust-stains-irrigation-well-water')}), and a polymer-modified overlay goes on in a knock-down, spray or broom texture, sealed after 24 hours.</p>"),
            ("No permit, and what to expect", f"<p>Resurfacing is maintenance in Osceola County; no permit and, in BVL, no HOA on most streets. Ten to fifteen years of life on a sound slab with a re-seal every three to five years. In the rainy season overlays are placed early on a clear morning, because a downpour on a fresh overlay ruins it ({tool('pour-calendar')}). Details: {svc('concrete-resurfacing')}.</p>"),
        ],
        ("A sound 1990 drive off Simpson Road", f"<p>400 square feet, worn and rust-stained, hairline cracks only, no offsets, solid tap test. Rust removed, cracks routed and filled, surface profiled, broom-textured overlay, penetrating sealer. At {cost_range('concrete-resurfacing')}: $2,000 to $3,800, versus $4,200 to $8,400 to replace. Two days plus cure. Ranges from the {R} index.</p>"),
        ("Can I resurface my BVL driveway instead of replacing it?", "If it is sound: hairline cracks only, no panel stepped more than a quarter inch, no hollow sound when tapped. That describes a minority of BVL's 1980s drives. If yours is stepped at the garage or rocking on voids, an overlay will crack the same way within a season; we say so on the site visit and price the replacement instead."),
        [
            faq("How long does a resurfaced drive last?", "Ten to fifteen years on a sound slab, with a re-seal every three to five."),
            faq("Will it hide the rust stains?", "Yes, once removed with an iron cleaner; the stains return on the overlay unless the sprinklers are adjusted."),
            faq("Can you change the color?", "Yes; integral color in the overlay or a textured two-tone finish."),
            faq("Do I need a permit?", "No; resurfacing is maintenance."),
        ],
        ["sda"],
        [cs("buenaventura-lakes", "concrete-driveways"), cs("buenaventura-lakes", "concrete-repair"), compare("sealer-types")]))

    p.append(cs_page("buenaventura-lakes", "paver-driveways",
        "Paver Driveways in Buenaventura Lakes, FL – Cost, Permit",
        "Paver driveways in Buenaventura Lakes: replacing a 1980s concrete drive with 80 mm pavers on a 6-in base, Osceola County driveway permit and 24-ft width, concrete apron at the street, no HOA on most streets, costs.",
        f"A paver driveway in BVL runs {cost_range('paver-driveway-concrete')} plus $2 to $4 per square foot to remove the old concrete ({R} Cost Index): roughly $6,400 to $12,500 for a 400- to 480-square-foot two-car drive. Osceola County's driveway permit and 24-foot rule apply; most BVL streets have no HOA, so pattern and color are yours to choose. Three to five days.",
        [
            ("Why some BVL owners choose pavers", f"<p>The look, the ability to widen later with matching units, and repairability: a paver drive that sinks at the garage after the next decade of roof water can be lifted and relaid in a day, where a concrete panel has to be cut out. On the cost side, pavers run 50 to 70 percent more than a broom-finish slab. Our section over the cleaned subgrade is 6 inches of compacted limerock in two lifts, 1 inch of bedding sand, 80 mm pavers in herringbone or running bond, restraint on the base and polymeric sand, with a poured concrete apron at the street and a soldier course at the seam ({svc('paver-driveways')}). Downspouts get extended before the base goes in; that detail is the whole reason the old slab failed.</p>"),
            ("Permit and width", f"<p>Unincorporated Osceola County: driveway permit under §22-50.6 for construction or widening, 24-foot maximum width, Building Office at 1 Courthouse Square (407-742-0200). The apron in the right-of-way follows the county detail in concrete. Where a BVL street does have a later HOA section, approval comes first ({tool('hoa-packet-checklist')}). Pages: {juris('osceola-county')}, {tool('permit-finder')}; base on this sand: {guide('paver-base-flatwoods-vs-ridge')}.</p>"),
        ],
        ("A Buenaventura Boulevard conversion", f"<p>460-square-foot 1988 concrete drive replaced with 80 mm gray pavers, charcoal soldier border, concrete apron. Removal $920 to $1,840, pavers at $14 to $22 ($6,440 to $10,120), seal at 60 days ($800 to $1,500). Four days after the county permit. Ranges from the {R} index.</p>"),
        ("Is a paver driveway worth the extra cost in BVL?", "It depends on what you want from the next twenty years. Concrete on a real base will last and costs less; pavers cost more, look different, and can be lifted and relaid when something moves, which in a neighborhood whose soil has already sunk one generation of driveways is a real advantage. The comparison page puts the numbers side by side."),
        [
            faq("Do pavers need a permit in BVL?", "Yes, the Osceola County driveway permit, same as concrete."),
            faq("Can pavers run to the street?", "The apron in the right-of-way is poured concrete to the county detail; pavers stop at a soldier course."),
            faq("How much more than concrete?", "About 50 to 70 percent more up front; repairable later."),
            faq("Is there an HOA?", "Most BVL streets, no; a few later sections, yes. We check."),
        ],
        ["osceola-22-50-6", "icpi"],
        [cs("buenaventura-lakes", "concrete-driveways"), compare("concrete-vs-pavers"), svc("paver-sealing")]))

    # ------------------------------------------------------------- Four Corners
    p.append(cs_page("four-corners", "paver-pool-decks",
        "Paver Pool Decks in Four Corners, FL – Rentals, Turnovers, HOAs",
        "Paver and travertine pool decks for vacation rentals in Four Corners: overlays between guests, Windsor Hills and Solterra HOA rules, Osceola vs. Polk by community, anti-slip sealers, cost for a 600 sq ft deck.",
        f"A paver overlay on a Four Corners rental pool deck runs {cost_range('paver-pool-deck')} and travertine {cost_range('travertine-pool-deck')} ({R} Cost Index); a 600-square-foot deck is $9,000 to $14,400 as an overlay. The job is scheduled in the two- to four-day gap between guests, the HOA reviews the visible change (Solterra's written rules are verified; Windsor Hills and the others go through their managers), and the county is Osceola or Polk depending on the community.",
        [
            ("Decks that see more traffic than a family home's", f"<p>Windsor Hills, Windsor Palms, Emerald Island, Solterra, Solara, Paradise Palms and the rest were built between 2001 and 2022 with textured concrete or builder-paver decks inside screen cages, and twenty years of rental guests, weekly pressure-washing by cleaning crews and pool chemicals have worn them out faster than a primary home's. Overlays in 1-inch remodel pavers or ½-inch travertine tile go over sound decks with new bullnose coping and a channel drain at the screen line; decks that settled on pool backfill get rebuilt on compacted base. Sealer gets an anti-slip additive and polymeric sand is rated for frequent cleaning ({guide('vacation-rental-owner-hardscape-guide')}). Heat matters for guests barefoot in July: light travertine measures coolest in published comparisons ({compare('travertine-vs-concrete-pavers')}).</p>"),
            ("Manager, HOA, county", f"<p>We work from the property manager's turnover calendar, stage material the day before check-out, and finish coping mortar 48 hours before check-in. Solterra's guidelines require ARC review of exterior changes and let the board ask for the installer's insurance certificate naming the association ({hoa('solterra')}); Windsor Hills and the other communities use management ARC forms whose criteria we have not published. County: Windsor Hills, Windsor Palms, Emerald Island and Windsor at Westside are Osceola (flatwork outside setbacks); Solterra, Solara, Bella Vida and Paradise Palms are Polk (slabs adjacent to structures are permitted). {tool('permit-finder')}; {juris('osceola-county')}; {juris('polk-county')}.</p>"),
        ],
        ("A Windsor Hills turnover overlay", f"<p>580-square-foot deck around a 12-by-24 pool inside a cage, 2005 knock-down concrete, sound. Three-night gap: day 1 clean and level, remodel pavers set; day 2 coping and channel drain; day 3 polymeric sand and anti-slip sealer, dry by evening. At {cost_range('paver-pool-deck')}: $8,700 to $13,900 plus coping. Ranges from the {R} index.</p>"),
        ("Can a pool deck be done between guests?", "Yes, if the gap is at least three nights and the deck is sound enough for an overlay. We stage material the day before check-out, set pavers and coping in two days, sand and seal on the third morning, and the sealer is walkable by the afternoon. A full rebuild needs five to seven days and a longer block on the calendar; your manager and we pick it together."),
        [
            faq("Which county is my rental in?", "Windsor Hills, Windsor Palms, Emerald Island: Osceola. Solterra, Solara, Bella Vida, Paradise Palms: Polk. The permit finder checks."),
            faq("Does the HOA need to approve an overlay?", "Yes for visible changes in every resort community here; Solterra's rules are on our HOA page."),
            faq("Which surface holds up to rental use?", "Sealed concrete pavers or travertine with an anti-slip penetrating sealer and polymeric sand rated for cleaning."),
            faq("Do you insure the association?", "When the board requires it, our certificate names the association as additional insured."),
        ],
        ["solterra", "polk-faq", "osceola-faq", "icpi"],
        [cs("four-corners", "paver-sealing"), cs("four-corners", "paver-driveways"), svc("paver-travertine")]))

    p.append(cs_page("four-corners", "paver-sealing",
        "Paver Sealing in Four Corners, FL – Rental Decks and Driveways",
        "Paver sealing for vacation rentals in Four Corners: anti-slip sealers on pool decks, polymeric sand that survives weekly cleaning, group pricing for several homes, turnover scheduling, ridge-sand dust, cost per sq ft.",
        f"Sealing a Four Corners rental deck or driveway runs {cost_range('paver-sealing')} including cleaning and polymeric re-sanding ({R} Cost Index); a 600-square-foot deck is $1,050 to $1,950 and several homes sealed for one manager on the same day come in below that. Rental surfaces are on a two- to three-year cycle because of cleaning crews and pool chemicals; we use an anti-slip additive on every deck and schedule the dry 24 hours the sealer needs into the turnover gap.",
        [
            ("What rental use does to pavers", f"<p>Weekly pressure-washing at high pressure strips joint sand and etches tumbled surfaces; pool chemicals splash unsealed pavers; guests track ridge-sand grit that abrades the sealer. So the cycle is shorter than a family home's, the joint sand has to be polymeric and vibrated in, and the sealer has to be a penetrating or joint-stabilizing product with grit added, not a glossy film that is slick when wet and hazes under a cleaning crew's hose ({compare('sealer-types')}). Efflorescence on the newer Solterra and Solara pavers clears in the first season and is cleaned before the first seal ({svc('paver-sealing', 'full process')}).</p>"),
            ("Group scheduling", f"<p>Property managers with several homes in Windsor Hills or Solterra book a sealing day: we clean on day one across all the homes, re-sand and seal on day two, and the per-home price drops with the shared mobilization. Turnover gaps of one night are enough for a seal if the deck was cleaned on the previous gap. No permit; a like-for-like clear seal is maintenance, and Solterra's rule that concrete surfaces are sealed only in a clear matte finish applies to any concrete on the lot ({hoa('solterra')}, {guide('vacation-rental-owner-hardscape-guide')}).</p>"),
        ],
        ("Four Solterra homes in one day", f"<p>Four rental homes, each a 500-square-foot pool deck and a 400-square-foot driveway (3,600 square feet total). Day one: clean and rust-treat all four; day two: polymeric re-sand and anti-slip penetrating sealer. At the low end of {cost_range('paver-sealing')} for the volume: about $6,300 to $8,600 total, $1,575 to $2,150 per home. Ranges from the {R} index.</p>"),
        ("How often should a rental pool deck be sealed?", "Every two to three years, versus three to four for a family home, because cleaning crews and pool chemicals wear the sealer faster. The tell is water no longer beading and joints dropping below the chamfer. Skipping it costs more later: unsealed pavers stain from rust and sunscreen and lose their joint sand to the hose."),
        [
            faq("Is the deck usable the same day?", "Foot traffic four hours after the last coat; we finish by noon so it is dry for evening check-in."),
            faq("Do you do several homes at once?", "Yes; group days for one manager lower the per-home price."),
            faq("Wet look on a rental?", "We advise against it: slick when wet and high maintenance under cleaning crews. Matte penetrating sealer with grit."),
            faq("Do you need HOA approval to seal?", "Not for a clear seal in the existing finish."),
        ],
        ["solterra", "icpi"],
        [cs("four-corners", "paver-pool-decks"), cs("four-corners", "paver-driveways"), guide("polymeric-sand-guide")]))

    p.append(cs_page("four-corners", "paver-driveways",
        "Paver Driveways in Four Corners, FL – Rebuilding on Ridge Sand",
        "Paver driveway rebuilds in Four Corners resort communities: why builder driveways settled on dry-placed ridge sand, lift-and-relay vs. new field, Solterra's three-car rule, Polk Paver Release Form, Osceola permits, costs.",
        f"Rebuilding a settled rental driveway in Four Corners runs {cost_range('paver-repair')} for a lift-and-relay on a rebuilt base or {cost_range('paver-driveway-concrete')} for a new field ({R} Cost Index). Most of the settling traces to base placed on dry Candler sand, which does not compact until it is wetted. Solterra caps an expanded driveway at three cars wide; Polk requires a recorded Paver Release Form for pavers in the right-of-way; Osceola communities use the county driveway permit.",
        [
            ("Ridge sand and the builder's base", f"<p>Four Corners sits on the northern end of the Lake Wales Ridge: Candler and Astatula sands, deep, dry and free-draining, with none of the fines that let flatwoods sand pack. Production crews placing base in an August afternoon got a compactor reading that meant nothing; the first rainy season packed the sand and the driveway dipped at the garage and rolled at the edges. The fix is the lift-and-relay: pavers up and stacked, failed base out, subgrade and each lift of new limerock wetted and compacted, restraint on the base, same pavers reset, polymeric sand. Where the whole field moved we rebuild from the subgrade. {guide('paver-base-flatwoods-vs-ridge')} has the soil science; {svc('paver-repair')} the repair scope.</p>"),
            ("Rules by community", f"<p>Solterra (Polk): expanded driveways no wider than three cars, no added walking area, ARC review, installer COI on request ({hoa('solterra')}); pavers reaching the county right-of-way need the owner's notarized, recorded Paver Release Form, which a concrete apron avoids ({juris('polk-county')}). Windsor Hills, Windsor Palms, Emerald Island (Osceola): county driveway permit for widening under §22-50.6 with the 24-foot limit, management ARC review ({juris('osceola-county')}). Work happens between guests with the manager's calendar ({guide('vacation-rental-owner-hardscape-guide')}). {tool('permit-finder')} sorts the county.</p>"),
        ],
        ("A Solara lift-and-relay", f"<p>440-square-foot 2016 builder driveway dipped 2 inches at the garage and along both edges. Lifted, base removed and rebuilt to 6 inches with wetted lifts, spiked restraint, same pavers reset with 20 matched replacements, polymeric sand, seal at 60 days. At {cost_range('paver-repair')}: $3,960 to $7,040 versus $6,160 to $9,680 for a new field. Three days in a turnover gap. Ranges from the {R} index.</p>"),
        ("Why did my builder's paver driveway sink?", "Because the base under it was placed on dry ridge sand and read as compacted when it was not. Candler sand packs only when wet; the first rainy season did the compaction the builder skipped, and the driveway followed it down. Rebuilding the base with wetted, compacted lifts under the same pavers fixes it for good."),
        [
            faq("Can you widen a Solterra driveway?", "To three cars wide with ARC approval and no added walking area, per the community guidelines."),
            faq("What is the Paver Release Form?", "Polk County's recorded form for pavers in its right-of-way; a concrete apron avoids it."),
            faq("Do you reuse the pavers?", "Yes; the same units go back in the same pattern, with matched replacements for broken ones."),
            faq("How long does it take?", "Two to three days for a lift-and-relay, three to five for a new field."),
        ],
        ["solterra", "polk-paver-release", "osceola-22-50-6", "sda"],
        [cs("four-corners", "paver-sealing"), cs("four-corners", "concrete-repair"), compare("concrete-vs-pavers")]))

    p.append(cs_page("four-corners", "concrete-repair",
        "Concrete Repair in Four Corners, FL – Aprons, Garage Slabs, Walks",
        "Concrete repair for Four Corners rental homes: settled garage aprons and sidewalk panels on ridge sand, cracked lanai slabs before an overlay, HOA notes for visible repairs, work scheduled between guests.",
        f"Concrete repair in Four Corners is mostly settled aprons and sidewalk panels on the 2001–2022 rental homes, plus lanai slabs being prepared for a paver overlay. Routing, filling and grinding are minimum-charge visits; a replaced apron or panel runs at new-pour rates ({cost_range('concrete-driveway-broom')}, or $11.50 to $17 at 6 inches for an apron) plus removal. Same-footprint repair needs no county permit; visible work is noted to the HOA and scheduled between guests.",
        [
            ("What fails on ridge sand", f"<p>The same dry-placed base that sank the paver driveways also settled the concrete aprons, sidewalk panels and lanai slabs poured with them: a panel drops ½ to 1 inch where the sand packed after the first rainy season, the apron corner cracks under delivery trucks, and the lanai slab cracks at the pool coping where the backfill was never compacted. Repairs: replace the apron section at 6 inches with edge steel; replace or lift a dropped sidewalk panel over a rebuilt, wetted base; route and fill lanai cracks before an overlay, or rebuild the deck if it heaved ({compare('resurface-vs-replace')}). Roots are rare here; the communities are young and the trees are palms.</p>"),
            ("Approvals and scheduling", f"<p>Same-footprint repair needs no permit in Osceola or Polk; an apron in the right-of-way is under the Osceola driveway permit or Polk's right-of-way rule, and the community's private streets make the ARC the practical gate. New concrete is lighter for a year, so visible repairs get a note to the manager's ARC; Solterra prohibits painting or staining concrete, so color-matching by stain is not an option there ({hoa('solterra')}). Work fits a turnover gap: a panel is a one-day pour and a 24-hour cure before foot traffic ({guide('vacation-rental-owner-hardscape-guide')}).</p>"),
        ],
        ("An Emerald Island sidewalk panel and apron corner", f"<p>One 5-by-5 sidewalk panel dropped ¾ inch and one apron corner cracked on a 2004 rental. Panel removed and replaced over a wetted, compacted base ($330 to $520); apron corner (30 square feet) replaced at 6 inches with edge bars ($345 to $510 plus $60 to $120 removal). One day in a two-night gap. Ranges from the {R} index.</p>"),
        ("Can a cracked lanai slab be overlaid with pavers?", "If the cracks are hairline and the slab is level and solid when tapped, yes: route and fill, then overlay. If a corner heaved at the coping or a section sounds hollow, the pool backfill under it moved and an overlay follows the movement; that deck gets rebuilt on compacted base before any pavers go down."),
        [
            faq("Do repairs need HOA approval?", "Visible ones are noted to the ARC because new concrete is lighter for a year."),
            faq("Can it be done between guests?", "A panel or apron is a one-day pour with 24 hours before foot traffic; a two-night gap works."),
            faq("Why did the apron settle?", "Dry-placed base on ridge sand packed after the first rainy season; the fix is a wetted, compacted base under the new section."),
            faq("Can you stain the new panel to match?", "Not in Solterra, where painting or staining concrete is prohibited; elsewhere a light tint helps and the color evens out within a year."),
        ],
        ["solterra", "polk-faq", "osceola-faq", "sda"],
        [cs("four-corners", "paver-pool-decks"), cs("four-corners", "paver-driveways"), guide("why-concrete-cracks-osceola")]))

    # ------------------------------------------------------------- ChampionsGate
    p.append(cs_page("champions-gate", "paver-pool-decks",
        "Paver Pool Decks in ChampionsGate, FL – Rentals and Country Club",
        "Paver and travertine pool decks in ChampionsGate: overlays on The Retreat rental homes between guests, travertine in the Country Club sections, Osceola County flatwork rules, resort ARC review, ridge sand base, costs.",
        f"A paver overlay on a ChampionsGate pool deck runs {cost_range('paver-pool-deck')} and travertine {cost_range('travertine-pool-deck')} ({R} Cost Index). ChampionsGate is Osceola County despite the Davenport ZIP, so an overlay outside setbacks is flatwork; the community's ARC reviews visible changes; rentals in The Retreat are scheduled between guests. The Country Club's primary homes lean toward travertine and marble.",
        [
            ("Two ChampionsGate markets", f"<p>The Retreat and the townhome sections rent by the week and their 2013–2022 decks take the same treatment as Four Corners' rentals: a 1-inch remodel paver overlay with new coping and a channel drain, polymeric sand rated for cleaning crews, anti-slip penetrating sealer, all in a three-night gap ({guide('vacation-rental-owner-hardscape-guide')}). The Country Club and The Vistas are primary homes whose owners ask for tumbled travertine, marble or large-format porcelain on the deck and the lanai, often with a seat wall or a summer kitchen added at the same time ({svc('paver-retaining-walls-outdoor-living')}). Both sit on ridge sand where pool backfill has to be compacted wet before a deck is rebuilt ({guide('paver-base-flatwoods-vs-ridge')}).</p>"),
            ("County and ARC", f"<p>Osceola County treats an overlay on a deck outside setbacks as flatwork; a deck tied to the pool bond beam or the screen footer is confirmed with the Building Office (407-742-0200). The community's ARC reviews visible changes through the management company's form; we have not published its written criteria because we have not verified them, and the {tool('hoa-packet-checklist')} lists what the form usually asks for. {juris('osceola-county')}; {tool('permit-finder')} confirms the county for the Davenport ZIP.</p>"),
        ],
        ("A Country Club travertine deck", f"<p>700-square-foot deck around a 15-by-32 pool, 2015 pavers settled at the coping on uncompacted backfill. Deck removed, backfill compacted wet in lifts, 4-inch base, tumbled ivory travertine sand-set, mortar-set bullnose coping, channel drain at the cage line, penetrating sealer with grit at 30 days. At {cost_range('travertine-pool-deck')}: $14,000 to $25,200 plus coping. Seven days. Ranges from the {R} index.</p>"),
        ("What is different about pool decks for ChampionsGate vacation homes?", "Three things: the deck sees guest traffic, cleaning crews and chemicals every week, so it gets polymeric sand rated for cleaning and an anti-slip penetrating sealer on a two- to three-year cycle; the work has to fit a turnover gap, so we stage material the day before and finish coping 48 hours before check-in; and the community's ARC and your manager both sign off before we start."),
        [
            faq("Is ChampionsGate in Osceola or Polk?", "Osceola, despite the Davenport ZIP; permits go through Osceola County."),
            faq("Overlay or rebuild?", "Overlay if the deck is sound; rebuild on compacted backfill if it settled at the coping, which is common on the ridge."),
            faq("Can you do it between guests?", "Overlays in three nights; rebuilds need five to seven days blocked on the calendar."),
            faq("Travertine or pavers for a rental?", "Sealed concrete pavers cost less and hold up; travertine stays cooler and reads as premium. Both work with the right sealer."),
        ],
        ["osceola-faq", "sda", "icpi"],
        [cs("champions-gate", "paver-sealing"), cs("champions-gate", "paver-driveways"), compare("travertine-vs-concrete-pavers")]))

    p.append(cs_page("champions-gate", "paver-sealing",
        "Paver Sealing in ChampionsGate, FL – Rental Cycle, Group Days",
        "Paver sealing in ChampionsGate: two- to three-year cycle on rental decks and driveways, anti-slip penetrating sealers, polymeric re-sanding, group days for property managers, ridge-sand grit, cost per sq ft.",
        f"Sealing in ChampionsGate runs {cost_range('paver-sealing')} with cleaning and polymeric re-sanding ({R} Cost Index); rental decks and driveways are on a two- to three-year cycle and managers book group days that bring the per-home price toward the low end. The builder's 2013–2022 driveways in The Retreat were never sealed and have lost their joint sand to ants and cleaning crews; the first seal fixes both.",
        [
            ("Sealing in a resort community", f"<p>Grit tracked in from ridge sand abrades film sealers, cleaning crews strip loose joint sand every week, and pool chemicals mark unsealed pavers. The product that lasts is a penetrating, joint-stabilizing sealer with an anti-slip additive over polymeric sand vibrated in dry ({compare('sealer-types')}, {guide('polymeric-sand-guide')}). Efflorescence on the newer pavers is cleaned before the first seal, never sealed under. Timing: one dry night for the sand, one for the sealer, so a two-night gap works if cleaning happened in the previous gap ({svc('paver-sealing')}).</p>"),
            ("No permit, ARC for finish changes", f"<p>Sealing is maintenance in Osceola County. A like-for-like clear seal needs no ARC review; switching a matte drive to a wet-look finish is a visible change the community's committee may want to see, and it is a poor idea on a rental anyway. Managers with several homes: one group day, one invoice, per-home pricing at the low end ({guide('vacation-rental-owner-hardscape-guide')}).</p>"),
        ],
        ("Six Retreat homes on a group day", f"<p>Six rentals, each a 450-square-foot deck and 380-square-foot driveway (4,980 square feet). Day one: clean, rust and efflorescence treated; day two: polymeric re-sand, anti-slip penetrating sealer. At the low end of {cost_range('paver-sealing')}: about $8,700 to $11,900 total, $1,450 to $1,980 per home. Ranges from the {R} index.</p>"),
        ("Do rental driveways in ChampionsGate need sealing more often?", "Yes: every two to three years instead of three to four, because weekly cleaning strips joint sand and grit wears the sealer. The first seal on a builder driveway that never had one is the biggest single improvement, since it replaces the regular sand the ants live in with polymeric sand and locks the field."),
        [
            faq("How long until guests can use the deck?", "Four hours after the last coat; we finish by noon."),
            faq("Do you need ARC approval to seal?", "Not for a clear seal in the existing finish."),
            faq("Wet look?", "Not on a rental; slick when wet and short-lived under cleaning crews."),
            faq("Group pricing?", "Yes, for several homes under one manager on one day."),
        ],
        ["icpi"],
        [cs("champions-gate", "paver-pool-decks"), cs("champions-gate", "paver-driveways"), guide("rust-stains-irrigation-well-water")]))

    p.append(cs_page("champions-gate", "paver-driveways",
        "Paver Driveways in ChampionsGate, FL – Rules & Rebuilds",
        "Paver driveway rebuilds and widening in ChampionsGate: Osceola County driveway permit and 24-ft rule despite the Davenport ZIP, ARC review, settled builder base on ridge sand, matching community blends, costs.",
        f"A paver driveway rebuild in ChampionsGate runs {cost_range('paver-repair')} as a lift-and-relay or {cost_range('paver-driveway-concrete')} as a new field ({R} Cost Index). Widening needs the Osceola County driveway permit (24-foot maximum) and the community's ARC approval; the Davenport ZIP does not move the county line. Builder driveways from 2013 onward settled on dry-placed ridge sand and are the most common rebuild.",
        [
            ("Rebuilds and widening", f"<p>The Retreat's and the Country Club's builder driveways are 16 to 18 feet wide and settle at the garage where the base was placed dry; owners widen to fit a third car or a golf cart and fix the dip at the same time. Our section: 6 inches of limerock wetted and compacted in two lifts, restraint on the base, 80 mm pavers in the community's approved blend (matched from the manufacturers' current lines), a concrete apron to the county detail at the street, polymeric sand ({svc('paver-driveways')}; ridge base in {guide('paver-base-flatwoods-vs-ridge')}). Widening within the setback and the 24-foot limit is drawn on the survey for the ARC.</p>"),
            ("Osceola permit, resort ARC", f"<p>Unincorporated Osceola County: driveway permit for construction or widening under §22-50.6, 24-foot maximum width, Building Office at 1 Courthouse Square (407-742-0200), 3- to 5-day residential review. The ARC application through the management company comes first and includes the survey markup, product, color and pattern ({tool('hoa-packet-checklist')}). Rentals are scheduled between guests ({guide('vacation-rental-owner-hardscape-guide')}). {juris('osceola-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Country Club widening", f"<p>18-foot builder drive widened to 24 feet over 26 feet of length (156 square feet added) and the original 468 square feet lifted and relaid on a rebuilt base. New area at $14 to $22 ($2,180 to $3,430), lift-and-relay at $9 to $16 ($4,210 to $7,490), matched pavers from the current line, concrete apron extension. County permit and ARC; four days. Ranges from the {R} index.</p>"),
        ("Can I widen my ChampionsGate driveway to fit a third car?", "Within the county's 24-foot limit and your section's ARC rules, yes. The application shows the new width on the survey; the county driveway permit follows the ARC approval. Most 16- to 18-foot builder drives have room for 6 feet before the setback; the ARC decides whether the extra width is acceptable on your lot."),
        [
            faq("Which county issues the permit?", "Osceola, despite the Davenport mailing address."),
            faq("Can you match the builder's pavers?", "From the manufacturers' current equivalents; original units are used at the visible seam."),
            faq("Why did the driveway sink?", "Dry-placed base on ridge sand; rebuilding the base wet under the same pavers fixes it."),
            faq("How long?", "Three to five days after ARC and permit."),
        ],
        ["osceola-22-50-6", "osceola-faq", "sda"],
        [cs("champions-gate", "paver-sealing"), cs("champions-gate", "concrete-repair"), compare("concrete-vs-pavers")]))

    p.append(cs_page("champions-gate", "concrete-repair",
        "Concrete Repair in ChampionsGate, FL – Aprons, Panels, Lanais",
        "Concrete repair in ChampionsGate: settled aprons and sidewalk panels on 2001–2022 homes built on ridge sand, cracked lanai slabs before an overlay, Osceola County right-of-way notes, ARC notes, turnover scheduling.",
        f"Concrete repair in ChampionsGate is settled aprons, dropped sidewalk panels and cracked lanai slabs on homes built since 2001 on ridge sand. Routing, filling and grinding are minimum-charge visits; a replaced apron or panel runs at new-pour rates ({cost_range('concrete-driveway-broom')}, or $11.50 to $17 at 6 inches) plus removal. Same-footprint repair needs no Osceola permit; the apron in the right-of-way is under the driveway permit; visible work is noted to the ARC.",
        [
            ("Ridge-sand settlement", f"<p>Base placed dry on Candler sand packs after the first rainy season, and everything poured on it drops: the apron by ½ to 1 inch, a sidewalk panel, the lanai slab at the coping where the pool backfill was never compacted. Repairs replace the apron section at 6 inches with edge steel over a wetted, compacted base; replace or lift a dropped panel; route and fill lanai cracks before an overlay, or rebuild a heaved deck ({compare('resurface-vs-replace')}, {guide('paver-base-flatwoods-vs-ridge')}). Delivery trucks at rental homes break apron corners more often than at primary homes; the 6-inch replacement with #4 edge bars stops the repeat.</p>"),
            ("Permits and scheduling", f"<p>Same-footprint repair needs no county permit; an apron in the county right-of-way is under the Osceola driveway permit (§22-50.6, Building Office 407-742-0200). The community's ARC gets a note on visible work because new concrete is lighter for a year. A panel or apron is a one-day pour with 24 hours before foot traffic, which fits a two-night rental gap ({guide('vacation-rental-owner-hardscape-guide')}). {juris('osceola-county')}.</p>"),
        ],
        ("A Retreat apron and sidewalk panel", f"<p>Apron corner (36 square feet) cracked by a delivery truck and one 5-by-5 sidewalk panel dropped ¾ inch on a 2016 rental. Apron section replaced at 6 inches with edge bars ($415 to $610 plus $70 to $145 removal), panel replaced over a wetted, compacted base ($330 to $520). One day in a two-night gap. Ranges from the {R} index.</p>"),
        ("Why is the sidewalk in front of my ChampionsGate home sinking?", "The base under it was placed on dry ridge sand and compacted only when the first rainy season packed it, taking the panel down with it. A dropped panel is replaced over a base that is wetted and compacted in lifts, which is what the original should have had; grinding the lip is a stopgap for a lift under three-quarters of an inch."),
        [
            faq("Do I need a permit for a repair?", "Not in the same footprint; the apron in the right-of-way is under the driveway permit."),
            faq("Can it be done between guests?", "A one-day pour with 24 hours before foot traffic fits a two-night gap."),
            faq("Will the new concrete match?", "Lighter for about a year; a straight joint at the seam makes it read as intentional."),
            faq("Can a cracked lanai slab take pavers?", "Hairline cracks, yes, after routing and filling; a heaved corner means a rebuild first."),
        ],
        ["osceola-22-50-6", "sda"],
        [cs("champions-gate", "paver-pool-decks"), cs("champions-gate", "paver-driveways"), guide("why-concrete-cracks-osceola")]))

    # ------------------------------------------------------------- Reunion
    p.append(cs_page("reunion", "paver-pool-decks",
        "Paver Pool Decks in Reunion, FL – Overlays, Three Managers",
        "Paver pool decks in Reunion Resort: overlays on 2005-era decks, which management company reviews your section (Artemis, Greystone, Southwest), Osceola County flatwork rules, rental scheduling, costs for a 600 sq ft deck.",
        f"A paver overlay on a Reunion pool deck runs {cost_range('paver-pool-deck')} and travertine {cost_range('travertine-pool-deck')} ({R} Cost Index). Reunion is unincorporated Osceola County (an overlay outside setbacks is flatwork) and its architectural review runs through three management companies by section: Artemis Lifestyles for single-family homes and most condo sections, Greystone for the Villas, Southwest Property Management for the Terraces. Villas and estate homes are scheduled between guests.",
        [
            ("Reunion's 2004 to 2015 pavers are ready for stone", f"<p>Reunion's first decade of homes were built with paver pool decks on pool backfill that was rarely compacted; twenty years on, coping has settled, joints have opened, and owners upgrading a rental villa or an estate home ask for travertine, marble or large-format porcelain. Sound decks get a thin-set travertine or porcelain overlay with new bullnose coping and a channel drain at the cage line; settled decks are rebuilt on wetted, compacted backfill and base ({guide('paver-base-flatwoods-vs-ridge')}). Rental decks get anti-slip penetrating sealer and polymeric sand rated for cleaning crews ({guide('vacation-rental-owner-hardscape-guide')}); the heat comparison is in {compare('travertine-vs-concrete-pavers')}.</p>"),
            ("Who approves, who permits", f"<p>Approval: Artemis Lifestyles (407-705-2190, reunionhoa@artemislifestyles.com) for single-family homes, Seven Eagles, Eagle Trace, Carriage Pointe, Centre Court Ridge, Heritage Crossing, Spectrum+ and the Grande; Greystone (407-645-4945) for Villas North and South; Southwest Property Management (407-656-1081) for the Terraces. We submit the packet to the right one ({tool('hoa-packet-checklist')}). Permit: Osceola County treats an overlay outside setbacks as flatwork; a deck tied to the bond beam or screen footer is confirmed with the Building Office (407-742-0200). {juris('osceola-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Seven Eagles travertine overlay", f"<p>620-square-foot deck around a 14-by-30 pool inside a cage, 2006 pavers sound but faded. Pavers removed and slab prepared, ½-inch tumbled travertine thin-set, mortar-set bullnose coping, channel drain, penetrating sealer with grit at 30 days. At {cost_range('travertine-pool-deck')}: $12,400 to $22,300 plus coping. Five days between bookings; Artemis approval in one cycle. Ranges from the {R} index.</p>"),
        ("Who approves a pool deck change in Reunion?", "The management company for your section: Artemis Lifestyles for single-family homes and most condominium sections, Greystone Management for Villas North and South, and Southwest Property Management for the Terraces. Each has its own ARC form; we prepare the packet (site plan, sample, color, pattern, drainage note, our insurance certificate) and submit it to the right office before the county paperwork."),
        [
            faq("Is a permit needed for an overlay?", "An overlay on a deck outside setbacks is flatwork in Osceola; a deck tied to the pool or screen structure is confirmed first."),
            faq("Can you work while the home is rented?", "Between bookings; overlays take four to five days, rebuilds seven."),
            faq("Travertine or marble?", "Both stay cool; marble is lighter and costs more. Samples on the deck decide it."),
            faq("What happened to the coping?", "Settled pool backfill; a rebuild compacts it before the new deck goes down."),
        ],
        ["osceola-faq", "sda", "icpi"],
        [cs("reunion", "paver-travertine"), cs("reunion", "paver-sealing"), svc("paver-marble-porcelain")]))

    p.append(cs_page("reunion", "paver-travertine",
        "Travertine in Reunion, FL – Pool Decks, Lanais, Cool Surfaces",
        "Travertine pool decks and lanais in Reunion Resort: tumbled ivory and silver grades, sand-set vs. thin-set over 2005 decks, penetrating sealers only, which management company approves, Osceola County rules, cost per sq ft.",
        f"A travertine pool deck in Reunion runs {cost_range('travertine-pool-deck')} installed ({R} Cost Index) in 1¼-inch tumbled pavers or ½-inch tile thin-set over a sound existing deck, with matching bullnose coping. It is the surface Reunion owners ask for by name because it stays cooler barefoot than concrete pavers and reads as stone on an estate lot. Approval goes through your section's management company; the county treats the work as flatwork.",
        [
            ("Travertine on Reunion's lots", f"<p>Estate homes on the golf courses use tumbled ivory or silver travertine in the French pattern on the deck and the lanai, often continued to a summer kitchen and a seat wall; rental villas use the same material in a tighter pattern with an anti-slip sealer. Over a sound 2005 paver or concrete deck we thin-set ½-inch tile; on a rebuilt deck we sand-set 1¼-inch pavers on compacted base. Coping is mortar-set bullnose on the bond beam with an expansion joint to the field. Sealer: penetrating and breathable only; film sealers haze white on stone over bedding sand within a year ({compare('sealer-types')}). Rust from irrigation shows fast on ivory stone; Reunion is on utility water, so the usual culprit is a well-fed irrigation zone on an estate lot ({guide('rust-stains-irrigation-well-water')}).</p>"),
            ("Approval and permit", f"<p>Artemis Lifestyles (407-705-2190) for single-family and most condo sections, Greystone (407-645-4945) for the Villas, Southwest Property Management (407-656-1081) for the Terraces; the packet includes a stone sample, pattern, coping profile and drainage note ({tool('hoa-packet-checklist')}). Osceola County: flatwork outside setbacks; a deck tied to the pool or cage structure is confirmed with the Building Office (407-742-0200). {juris('osceola-county')}; the full material page is {svc('paver-travertine')}.</p>"),
        ],
        ("An estate-lot travertine deck and lanai", f"<p>1,100 square feet of deck and lanai around a 16-by-36 pool, plus 40 linear feet of seat wall. Tumbled ivory travertine in the French pattern, sand-set on a rebuilt base, mortar-set bullnose coping, channel drain at the cage line, travertine-capped seat wall. Deck at {cost_range('travertine-pool-deck')}: $22,000 to $39,600; coping $28 to $55 per linear foot; seat wall $75 to $130 per linear foot. Ten days. Ranges from the {R} index.</p>"),
        ("Does travertine get too hot for a Reunion pool deck in July?", "Warm, not scorching. Published installer measurements put light travertine at 105 to 120 °F on a 95-degree afternoon, versus 130 to 145 for dark concrete pavers; ivory and silver grades are the coolest of the travertine range. We cite those numbers rather than our own until we measure decks here in July, and we publish the method when we do."),
        [
            faq("Sand-set or thin-set?", "Thin-set tile over a sound existing deck; sand-set pavers on a rebuilt base. The proposal states which and why."),
            faq("Which sealer?", "Penetrating, breathable, with an anti-slip additive on rentals. Never a film-forming acrylic on stone."),
            faq("Who approves?", "Your section's management company; we submit the packet."),
            faq("How much for a 600 sq ft deck?", "About $12,000 to $21,600 plus coping in the current index."),
        ],
        ["osceola-faq", "icpi"],
        [cs("reunion", "paver-pool-decks"), cs("reunion", "paver-sealing"), compare("travertine-vs-concrete-pavers")]))

    p.append(cs_page("reunion", "paver-sealing",
        "Paver & Travertine Sealing in Reunion, FL – Rental Cycle",
        "Sealing pavers and travertine in Reunion Resort: penetrating sealers for stone, anti-slip products for rental decks, polymeric re-sanding, two- to three-year cycle, group days for managers, cost per sq ft.",
        f"Sealing in Reunion runs {cost_range('paver-sealing')} with cleaning and polymeric re-sanding ({R} Cost Index). Rental villas are on a two- to three-year cycle and estate homes three to four; travertine and marble take a penetrating sealer only, concrete pavers can take either type. No permit, and a clear seal in the existing finish needs no management review.",
        [
            ("Stone and pavers, different products", f"<p>Reunion has more travertine and marble per street than anywhere else we work, and the most common sealing mistake here is a wet-look acrylic on stone: it traps moisture from the bedding sand and hazes white in a season, and stripping it costs more than the sealing did. Stone gets a penetrating siloxane or fluoropolymer sealer; concrete pavers on driveways can take a film sealer if the owner wants the wet look and the drive dries fully, or the same penetrating product for a matte finish ({compare('sealer-types')}). Rental decks get an anti-slip additive and polymeric sand rated for weekly cleaning ({guide('vacation-rental-owner-hardscape-guide')}); the process is on {svc('paver-sealing')}.</p>"),
            ("Scheduling and managers", f"<p>One dry night for polymeric sand, one for sealer; a two-night gap works if the deck was cleaned in the previous gap. Managers with several villas book group days at the low end of the range. No county permit; a like-for-like clear seal needs no review from Artemis, Greystone or Southwest, while a finish change on a visible driveway may.</p>"),
        ],
        ("An estate-home travertine deck and paver driveway", f"<p>900-square-foot travertine deck and 700-square-foot paver driveway. Deck: stone cleaner, penetrating sealer with grit. Driveway: pressure wash, polymeric re-sand, penetrating sealer. 1,600 square feet at {cost_range('paver-sealing')}: $2,800 to $5,200. Two mornings. Ranges from the {R} index.</p>"),
        ("Why did my travertine turn white after the last company sealed it?", "A film-forming sealer over stone that was still holding moisture from the bedding sand. The film trapped the water and clouded. The fix is to strip the film and re-seal with a penetrating, breathable product on a dry deck; travertine and marble should never get a film sealer in this climate."),
        [
            faq("How often for a rental villa?", "Every two to three years; estate homes three to four."),
            faq("Can you strip the old sealer?", "Yes; stripping adds $0.75 to $1.50 per square foot and is the expensive part."),
            faq("Do you need approval to seal?", "Not for a clear seal in the existing finish."),
            faq("Group pricing for several villas?", "Yes, on one manager's group day."),
        ],
        ["icpi"],
        [cs("reunion", "paver-travertine"), cs("reunion", "paver-pool-decks"), guide("polymeric-sand-guide")]))

    p.append(cs_page("reunion", "paver-driveways",
        "Paver Driveways in Reunion, FL – Premium Lines, Osceola Permit",
        "Paver driveway rebuilds in Reunion Resort: premium blends matched to the streetscape, 6-in base on ridge sand, Osceola County driveway permit and 24-ft rule, section-by-section management approval, costs.",
        f"A Reunion driveway rebuild runs {cost_range('paver-driveway-premium')} in the premium lines the streetscape uses, or {cost_range('paver-driveway-concrete')} in standard pavers where a section allows it ({R} Cost Index). Widening needs the Osceola County driveway permit (24-foot limit) after the section's management company approves; the builder's 2004–2015 base settled on dry ridge sand and is rebuilt wet under the same or new pavers.",
        [
            ("Matching a resort streetscape", f"<p>Reunion's sections were built with specific premium blends and borders, and a rebuild is judged on how well it disappears into the street. We identify the original line, source the current equivalent from Belgard, Tremron or Oldcastle, and use original units at the visible seams. Section: 6 inches of limerock wetted and compacted, restraint on the base, 80 mm pavers, concrete apron to the county detail, polymeric sand ({svc('paver-driveways')}; ridge base in {guide('paver-base-flatwoods-vs-ridge')}). Estate lots add pillars, bands and integrated lighting ({svc('paver-outdoor-lighting')}).</p>"),
            ("Approval and permit", f"<p>Artemis Lifestyles (407-705-2190) for single-family and most condo sections, Greystone (407-645-4945) for the Villas, Southwest (407-656-1081) for the Terraces; the packet shows the survey markup, blend, pattern and border ({tool('hoa-packet-checklist')}). Then Osceola County's driveway permit for construction or widening under §22-50.6, 24-foot maximum, Building Office at 1 Courthouse Square (407-742-0200). Rental homes are scheduled between guests. {juris('osceola-county')}; {tool('permit-finder')}.</p>"),
        ],
        ("A Carriage Pointe rebuild with lighting", f"<p>520-square-foot 2007 driveway settled at the garage, premium blend discontinued. Lifted and rebuilt on a wetted 6-inch base with the current equivalent line, original units at the apron seam, charcoal double border, eight paver lights in the border on a transformer. Field at {cost_range('paver-driveway-premium')}: $10,400 to $17,700; lighting $1,400 to $2,600. Five days after Artemis approval and the county permit. Ranges from the {R} index.</p>"),
        ("Can I change my driveway pavers to a different color in Reunion?", "With your section's management approval, within the palette the community's guidelines allow, which we have not published because we have not verified the written criteria. In practice the committees approve blends that match the streetscape and reject ones that stand out; we bring samples of the current equivalent lines to the site visit so the packet shows a match."),
        [
            faq("Who approves a driveway change?", "Your section's management company; then the Osceola County driveway permit for widening."),
            faq("Can you match the original blend?", "From the manufacturers' current lines, with original units at the seams."),
            faq("Why did the base fail?", "Placed dry on ridge sand; rebuilt wet and compacted it holds."),
            faq("Lighting at the same time?", "Yes; conduit goes in under the pavers before the field is laid."),
        ],
        ["osceola-22-50-6", "osceola-faq", "sda", "belgard"],
        [cs("reunion", "paver-sealing"), cs("reunion", "paver-pool-decks"), svc("paver-outdoor-lighting")]))

    return p
