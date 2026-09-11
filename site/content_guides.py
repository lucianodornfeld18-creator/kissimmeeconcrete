# -*- coding: utf-8 -*-
"""Guides index + 14 guides."""
from _data import GUIDES, GUIDE_ORDER, COST_INDEX_RELEASE
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_range, steps, callout, related, esc

R = COST_INDEX_RELEASE["label"]


def page(key, title, desc, body, faqs, sources, h1=None):
    g = GUIDES[key]
    return {"route": g["route"], "title": title, "meta_description": desc, "h1": h1 or g["name"], "breadcrumbs": [("Home", "/"), ("Guides", "/guides/"), (g["name"], None)], "body_html": body, "faqs": faqs, "kind": "guide", "nav_active": "/guides/", "sources": sources}


def index():
    body = sec("Guides written for Osceola County and the Polk ridge", cap("Fourteen guides on the questions that come up on estimates here: why slabs crack on this sand, rust from well water, driveway widening rules, pouring in the rainy season, verifying a contractor when there is no license to check, vacation-rental scheduling, oak roots, ridge sand versus flatwoods sand, the 1980s Buenaventura Lakes driveways, septic drainfields, polymeric sand, curing in heat, pool-deck surface temperatures and the new $7,500 permit exemption."), eyebrow="Guides")
    body += sec("All guides", cards([(GUIDES[k]["name"], "", GUIDES[k]["route"], "Read the guide") for k in GUIDE_ORDER], cols=2))
    return {"route": "/guides/", "title": "Concrete & Paver Guides for Kissimmee and Osceola County", "meta_description": "Local guides on cracking, rust stains, driveway widening rules, rainy-season scheduling, contractor verification, vacation rentals, oak roots, ridge vs. flatwoods sand, BVL driveways, septic, polymeric sand, curing, deck heat and HB 803.", "h1": "Guides", "breadcrumbs": [("Home", "/"), ("Guides", None)], "body_html": body, "kind": "page", "nav_active": "/guides/", "no_cta": True}


def cracks():
    body = sec("Why does concrete crack in Osceola County?",
        cap("Three reasons account for nearly every cracked slab we inspect here: shrinkage that had no joint to go to, a base that lost support when water moved through the fine sand under it, and a slab that was too thin for the load at its edge. The ground is the constant. Smyrna, Myakka and Immokalee fine sands hold a water table about 12 inches down from June through September; Basinger sand is wet to the surface. Concrete poured flush on that ground with a downspout at its edge is a crack waiting for its first summer."),
        eyebrow="Guide")
    body += sec("Which cracks are normal and which are not",
        table(["Crack", "What it looks like", "Cause", "Worry?"], [
            ("Plastic shrinkage", "Short, shallow, parallel hairlines within hours of the pour", "Surface dried faster than the interior (heat, wind, no cure)", "No; cosmetic. Fiber and curing prevent it"),
            ("Drying shrinkage at a joint", "Straight crack running along or near a control joint", "Joints too far apart or cut too late; the slab found its own joint", "No, if it stays tight; seal it"),
            ("Random drying-shrinkage crack", "One long hairline across the panel", "No joints, or joints spaced beyond ~10 ft on a 4-in slab", "No if under 1/16 in and level; watch it"),
            ("Settlement crack", "Crack with a step from one side to the other, usually at the garage or apron", "Base washed out or never compacted; water under the slab", "Yes; the base moved"),
            ("Corner break", "Triangle broken off at the apron or driveway corner", "Truck wheels on an unreinforced thin edge", "Yes for the corner; replace at 6 in with edge steel"),
            ("Heave crack at a tree", "Slab lifted, crack over the root line", "Live oak roots", "Yes; root barrier and panel replacement"),
            ("Map cracking / crazing", "Fine network on the surface", "Over-finishing on bleed water, too much water in the mix", "Cosmetic; can be resurfaced"),
            ("Spalling / scaling", "Surface flaking, pits", "Finishing on bleed water, sealer trapping moisture, salt", "Cosmetic to moderate; overlay"),
        ]), cls="alt")
    body += sec("What the water table does",
        f"<p>USDA Soil Data Access lists Smyrna fine sand (188,635 acres) and Myakka fine sand (122,954 acres) as the two largest map units in Osceola County, both poorly drained with a wet-season water table about 12 inches below the surface; Basinger fine sand (44,637 acres) at 6 inches; depressional Basinger and Placid at the surface. Fine sand loses bearing when saturated and, worse, moves: roof water from a downspout at the slab edge washes fines out from under the edge every storm, leaving a void that the panel drops into. The result is the stepped garage panel we see on almost every 1980s driveway in Buenaventura Lakes and the older Poinciana villages. The fix is not more concrete; it is a compacted base, a slab that sheds water at ⅛ inch per foot, downspouts extended past the slab, and edge steel ({svc('concrete-driveways')}).</p>")
    body += sec("What joints do", "<p>Concrete shrinks as it cures, about 1/16 inch per 10 feet, and it will crack somewhere to relieve that. Control joints are planned weak lines, tooled or saw-cut to a quarter of the slab depth, spaced about 10 feet on a 4-inch slab (roughly two and a half times the thickness in feet, per ACI 332 guidance), cut within 12 hours before the shrinkage starts. A slab with joints cracks in the joints; a slab without them cracks across the middle. Re-entrant corners (where the drive meets the garage or a walk) get a joint or a diagonal bar because cracks start there.</p>", cls="alt")
    body += sec("What thickness and steel do (and don't)", f"<p>Thickness carries load: 4 inches for cars, 6 for boats and trucks ({compare('4-inch-vs-6-inch')}). Reinforcement holds a crack tight once it forms and stiffens edges; it does not prevent cracking, and wire mesh lying on the bottom of a 4-inch slab does nothing at all ({compare('rebar-vs-fiber-vs-mesh')}). Fiber in the mix stops the plastic shrinkage cracks of the first hours. None of it substitutes for base and drainage.</p>")
    body += sec("Heat and the rainy season", f"<p>July's normal high at the Kissimmee 2 station is 91.5 °F and the month averages 16.7 rain days. Hot weather makes the surface set before the interior, which is the recipe for plastic shrinkage cracking unless the mix is retarded, the slab is poured early and cured wet or with a compound the same day. Rain during finishing washes cement out of the surface and leaves a weak skin that scales. Our rules are in {guide('rainy-season-concrete-scheduling')} and {guide('concrete-curing-florida-heat')}.</p>", cls="alt")
    body += sec("What to do about a cracked slab", f"<p>Hairlines: seal them or leave them. Stepped or hollow: fix the water first, then lift or replace the panel ({svc('concrete-repair')}). Widespread on a 1980s slab: replace ({compare('resurface-vs-replace')}). A worn but stable slab: resurface ({svc('concrete-resurfacing')}). On the Polk ridge the cause flips from water to dry-placed base that settled when it finally got wet; the fix is the same, a rebuilt base ({guide('paver-base-flatwoods-vs-ridge')}).</p>")
    body += sec("How we read a driveway before we quote a repair",
        f"""<p>An inspection takes about twenty minutes and produces four facts. First, the crack map: we mark every crack on a sketch and note width with a crack comparator card, because 1/16 inch and 3/16 inch lead to different answers. Second, the step: a straight edge across each crack tells us whether one side has dropped, and anything over 1/8 inch of vertical offset means the base moved. Third, the sound: a chain or a hammer dragged across the panel rings on supported concrete and thuds where there is a void underneath. Fourth, the water: we run the homeowner's downspouts and irrigation and watch where the water actually goes, because the crack almost always sits downhill of the answer.</p>
<p>That is why our repair quotes name a cause. A quote that says "replace cracked section, $X" and nothing else has skipped the diagnosis, and the replacement panel will do what the first one did. If the fix starts with an extended downspout or a regraded swale, we say so, even though that part is cheap and sometimes not our work at all.</p>""")
    body += sec("What a crack costs to live with",
        table(["Condition", "Do nothing", "Seal or grind", "Replace the panel", "Replace the drive"], [
            ("Hairline under 1/16 in, level", "Fine indefinitely", "Optional, keeps water out", "No", "No"),
            ("1/8 to 1/4 in, level, tight", "Widens slowly; weeds", "Route and seal, minimum charge visit", "Not yet", "No"),
            ("Step over 1/8 in at the garage", "Gets worse each wet season", "Grinding hides a trip hazard only", "Yes, after the water is fixed", "If other panels are cracked too"),
            ("Corner broken at the apron", "Chips further under truck wheels", "No", "Yes, at 6 in with edge steel", "Consider, if the drive is 30+ years old"),
            ("Multiple panels, 1980s slab", "Deteriorates", "Money down the drain", "Buys two or three years", "Usually the better dollar"),
            ("Surface scaling, slab sound", "Cosmetic", "No", "No", "No; resurface instead"),
        ], caption="What we tell homeowners at the door. Prices for each route are on the repair and resurfacing pages."), cls="alt")
    body += sec("The one thing that actually prevents cracking here",
        f"""<p>If a homeowner takes one idea from this page, it should be this: on Osceola sand the enemy is moving water, not weak concrete. A 4-inch slab at 3,000 psi on a properly compacted base, sloped to shed water, with downspouts carried past the edge and joints cut on time, outlasts a 6-inch slab at 4,000 psi poured flush on raw sand with a downspout dumping at its corner. We have replaced the second kind many times and rarely the first.</p>
<p>The same logic applies to pavers, with one advantage: when the base under pavers washes out, the pavers do not crack. They settle, and they can be lifted, the base rebuilt and the same pavers reset ({svc('paver-repair')}). That repairability is a real argument for pavers on a lot with known drainage trouble, and it is covered in {compare('concrete-vs-pavers')}.</p>""")
    faqs = [
        faq("Is a crack in a new driveway normal?", "A hairline shrinkage crack, yes, especially if the joints were spaced wide or cut late. A crack with a step, a hollow sound or a broken corner is not."),
        faq("Will my new driveway crack?", "It will develop hairline cracks; the joints are there to put them where you planned. It should not step or break if the base was built and water is kept off the edges."),
        faq("Does 4,000 psi stop cracking?", "No. Strength above the load does nothing for shrinkage or settlement. Base, joints, curing and water control do."),
        faq("Why did my driveway crack at the garage?", "Roof water washing sand out from under the slab edge; the panel dropped. Extend the downspout, then repair."),
        faq("Can cracks be repaired invisibly?", "No. Routed and sealed cracks show as a clean line; a resurfacing hides them if the slab is stable."),
        faq("How wide does a crack have to be before it matters?", "Width matters less than offset. A 1/4-inch crack with both sides level is a sealing job; a 1/8-inch crack with a step is a base problem. We measure both."),
        faq("Can I seal a crack myself?", "A tight hairline, yes, with a flexible polyurethane crack sealant from any supply house; clean and dry it first. A crack with a step will re-open whatever you put in it."),
        faq("Does the concrete supplier warranty cracks?", "No supplier or contractor in Florida warranties concrete against hairline shrinkage cracking; that is why our proposals specify joints, base and drainage instead of promising a crack-free slab."),
    ]
    return page("why-concrete-cracks-osceola", "Why Concrete Cracks in Osceola County (and Which Cracks Matter)", "Why slabs crack on Osceola's Smyrna and Myakka sand with a 12-inch water table: shrinkage vs. settlement vs. edge loads, a crack-by-crack table, what joints, thickness and steel do and don't do, and what to fix.", body, faqs, ["sda", "aci332", "noaa"])


def rust():
    body = sec("Orange streaks come from well-water irrigation",
        cap("Outside the city utility areas of Kissimmee and St. Cloud, most homes irrigate from wells, and Central Florida well water carries dissolved iron that oxidizes the moment it hits air and concrete. The orange or brown streaks that follow the sprinkler arc across a driveway, walk or pool deck are rust, not a defect in the surface. They come off with the right chemistry and they come back unless the water stops hitting the hardscape."),
        eyebrow="Guide")
    body += sec("Identify the stain first",
        table(["Stain", "Looks like", "Where", "Test", "Remover"], [
            ("Iron / rust", "Orange to brown streaks in an arc or a drip line; darker where water pooled", "Sprinkler arc, downspout, near the well head", "Does not lift with a degreaser; brightens with an acid-based rust product on a test spot", "Oxalic-acid or proprietary rust removers (concrete only); a stone-safe iron remover on travertine"),
            ("Tannin", "Brown to black blotches, leaf shapes", "Under live oaks and magnolias", "Lifts partially with a sodium-percarbonate cleaner", "Percarbonate (oxygen) cleaner"),
            ("Oil", "Dark, glossy when fresh, absorbs into the surface", "Parking spots", "Beads water; smells", "Degreaser and a poultice; repeat"),
            ("Efflorescence", "White haze or crystals", "New concrete pavers, first rainy season", "Disappears when wet, returns when dry", "Efflorescence cleaner (mild acid); wait it out"),
            ("Mold / algae", "Black or green film, slippery", "Shade, north sides, under trees", "Lifts with a mild bleach solution", "Sodium hypochlorite solution or a house-wash product"),
            ("Battery / fertilizer", "White or bleached spots, sometimes rust-edged", "Garage floor, lawn edge", "Location tells", "Neutralize, rinse; fertilizer with iron leaves rust dots"),
        ], caption="Using the wrong product makes stains worse: acid rust removers etch travertine and marble; bleach does nothing to iron; pressure alone drives oil deeper."), cls="alt")
    body += sec("Removing rust without damaging the surface", steps([
        "Test a hidden square foot. Concrete and concrete pavers tolerate oxalic-acid and commercial rust removers; travertine, marble and colored or stamped concrete need a stone-safe or neutral iron remover, or they etch and lighten.",
        "Wet the surface, apply the remover to the stain only, let it work for the label time (usually 5–15 minutes), agitate with a stiff brush, rinse thoroughly.",
        "Repeat on old stains; a first pass lifts 60–80 percent.",
        "Neutralize acid products with a baking-soda rinse where the runoff reaches plants or a pool.",
        "Let the surface dry two days, then seal (penetrating on stone, film or penetrating on concrete) so the next stain sits on the sealer and lifts easily.",
    ]))
    body += sec("Stopping it from coming back", f"<p>Sealer helps with removal; it does not prevent staining. Prevention is about the water. First, adjust the sprinkler heads so no zone throws onto the driveway, walk or deck; most rust arcs come from one or two heads. Second, where the pattern cannot avoid the hardscape, an iron filter or a sequestering-agent injector on the irrigation line keeps the iron dissolved so it does not oxidize on the surface; rust-control services install these across Central Florida. Third, reroute a downspout that feeds an iron-rich drip line. On the newest paver driveways in Narcoossee, Sunbridge and the Polk ridge subdivisions, doing this in the first month saves a lifetime of orange edges ({svc('paver-sealing')}).</p>", cls="alt")
    body += sec("Surfaces that show it most", f"<p>Light pavers, ivory travertine and white marble show iron within weeks; gray broom concrete hides it longest. If you are choosing a pool-deck material on a well-irrigated lot, that is a factor ({compare('travertine-vs-concrete-pavers')}). Rust that has been sealed over needs the sealer stripped first, which is the expensive version of this job ({compare('sealer-types')}).</p>")
    body += sec("How we remove an iron stain, step by step",
        steps([
            "Identify it first with the table above. Using a rust remover on a tannin stain wastes a trip and can darken the tannin.",
            "Wet the surrounding concrete or stone so the chemical stays where it is applied and does not wick into dry areas.",
            "Apply an oxalic-acid or proprietary iron remover at the label dilution, working in shaded conditions; a hot slab in July flashes the product off before it works.",
            "Dwell for the time on the label, usually 5 to 15 minutes, agitating with a stiff nylon brush. Never a wire brush on pavers or stone.",
            "Rinse thoroughly and neutralize if the label calls for it; acid left in a joint eats the sand and the paver edges.",
            "Repeat on a deep stain rather than increasing strength or dwell time. Two mild passes beat one aggressive one.",
            "Let the surface dry for 48 hours, then seal if the surface was sealed before or if you want the next stain to sit on top instead of soaking in.",
        ]))
    body += sec("Stop it coming back",
        table(["Option", "What it does", "Rough cost", "Catch"], [
            ("Adjust or move sprinkler heads", "Keeps iron water off the hardscape", "An hour of an irrigation tech's time", "Not always possible on a narrow side yard; wind still carries mist"),
            ("Change head type or arc", "Lower trajectory, tighter arc, less overspray", "$8 to $25 per head installed", "Coverage has to be rechecked so the lawn is not starved"),
            ("Iron filter or sequestering injector on the well", "Treats the water before it sprays", "$400 to $1,500 typical for an injection system", "Needs refilling and periodic service; sizing is a well contractor's job"),
            ("Penetrating sealer on the hardscape", "Slows absorption so the next stain lifts more easily", "$1.75 to $3.25 per sq ft with clean and re-sand", "Does not prevent rust; it buys cleaning time"),
            ("Rust-inhibitor products in the irrigation line", "Binds iron so it does not oxidize on the surface", "Varies by system", "Must be maintained or staining resumes"),
        ], caption="Costs are planning figures from local service pricing in September 2026, outside our own Cost Index because irrigation work is not our trade."), cls="alt")
    body += sec("What not to do",
        f"""<p>Muriatic acid is the most common bad advice on this subject. On concrete it etches the surface, leaving a lighter, rougher patch that catches the next stain faster; on travertine, marble and any calcareous stone it dissolves the surface outright and there is no undoing it. Pressure washing at 3,000 psi and up removes the stain by removing the top of the concrete and blowing the joint sand out of pavers, which then have to be re-sanded ({svc('paver-sealing')}). Household bleach does nothing to iron and will kill the plants at the slab edge. And sealing over a stain locks it in.</p>
<p>One more local note. Efflorescence on new concrete pavers looks like a white haze and shows up in the first wet season; it is salts moving out of the pavers, not a failure, and it usually stops on its own. Cleaning it too early with an acid product can etch the paver face. We wait, then clean and seal at the 60 to 90 day mark ({guide('polymeric-sand-guide')} covers the joints at the same visit).</p>""")
    faqs = [
        faq("What causes rust stains on a concrete driveway in Florida?", "Iron in well water sprayed by the irrigation system; it oxidizes on the surface as orange streaks along the sprinkler arc."),
        faq("How do I remove rust stains from concrete?", "An oxalic-acid or commercial rust remover on concrete; a stone-safe iron remover on travertine or marble; test first, apply to the stain, brush, rinse, repeat."),
        faq("Will sealing stop rust stains?", "No; it makes them easier to remove. Adjusting heads or filtering the well water stops them."),
        faq("Does bleach remove rust?", "No. Bleach handles mold and algae; rust needs an acid or chelating iron remover."),
        faq("Can pressure washing remove rust?", "Not by itself; it drives the stain in. Chemistry first, then a rinse."),
        faq("Will the stain come back after cleaning?", "Yes, if the same water keeps hitting the same spot. Cleaning without changing the irrigation is a recurring expense; head adjustment is the cheapest permanent fix."),
        faq("Can rust be removed from travertine and marble?", "Yes, with a stone-safe iron remover. Never an acid meant for concrete, which dissolves calcareous stone."),
        faq("How much does professional rust removal cost?", "Cleaning specialists in this market typically price by the square foot with a minimum visit; it is not part of our Cost Index because we sub it or refer it when a job is stain removal only."),
    ]
    return page("rust-stains-irrigation-well-water", "Rust Stains From Well-Water Irrigation: Identify, Remove, Prevent", "Orange streaks on driveways, pavers and pool decks in Osceola County are iron from well-water sprinklers. A stain identification table, safe removers by surface, and the head adjustment or iron filter that stops it.", body, faqs, [])


def widening():
    body = sec("What the county and the cities allow when you widen",
        cap("In unincorporated Osceola County a residential driveway may not exceed 24 feet in width without a conditional use, and construction or widening requires a county driveway permit (Code §22-50.6, Ordinance 12-10, 2012). Inside Kissimmee the Engineering Division reviews width with the Driveway / Sidewalk Construction application; inside St. Cloud the Building Department and Public Works do. Widening onto the strip between the sidewalk and the street is right-of-way work everywhere. HOAs often set a tighter limit than the county."),
        eyebrow="Guide")
    body += sec("Rules by jurisdiction",
        table(["Where", "Width rule", "Permit", "Right-of-way", "Source"], [
            ("Unincorporated Osceola", "24 ft max unless a conditional use is approved", "County driveway permit for construction or widening", "LDC 4.12.2; the apron follows the county detail", juris("osceola-county")),
            ("City of Kissimmee", "Reviewed with the application (published maximum not verified by us)", "Driveway / Sidewalk Construction application (Engineering)", "Public Works & Engineering approval", juris("city-of-kissimmee")),
            ("City of St. Cloud", "Reviewed by the city", "Building Department; pavers via Public Works", "Public Works and Engineering approval", juris("city-of-st-cloud")),
            ("Unincorporated Polk", "Setbacks and LDC apply", "Permit for the right-of-way and setback portions", "Paver Release Form if pavers reach the right-of-way", juris("polk-county")),
            ("Unincorporated Orange", "Permit for any concrete or pavers", "Building / Zoning", "6 in / 3,000 psi apron, no steel, 3 ft from the property line", juris("orange-county")),
        ]), cls="alt")
    body += sec("HOA limits are usually tighter",
        f"<p>Solterra caps an expanded driveway at three cars wide and prohibits added walking area ({hoa('solterra')}). Poinciana's DCB ties duplex driveways to the existing width requirement and requires approval for any paved area ({hoa('poinciana-apv')}). Solivita reviews extensions individually ({hoa('solivita')}). Celebration's front-loaded lots have street trees and setbacks that leave little room ({hoa('celebration')}). In resort communities the practical question is where the extra car goes: a paver parking strip beside the drive is reviewed the same way as the driveway. The {tool('hoa-packet-checklist')} lists what to submit.</p>")
    body += sec("How a widening is built so it does not look like one", f"<p>The new strip gets the same base and thickness as the existing drive, a straight saw-cut seam with a doweled expansion joint, and the same finish; a contrasting border or a paver band can make the seam intentional. Color will differ for about a year on concrete; on pavers a matched line hides it. If the existing drive is on a failing base, we say so, because a new strip beside a moving slab will step within a season. Boat and RV strips go to 6 inches with a rebar grid ({svc('concrete-driveways')}, {svc('paver-driveways')}, {compare('4-inch-vs-6-inch')}).</p>", cls="alt")
    body += sec("Parking on the widened area", "<p>Osceola's §22-50.6 sits in the parking chapter of the code because widening and parking are linked: the county regulates parking of vehicles on private property, and a widened drive is the lawful place to park a second or third vehicle rather than the lawn. Boat and RV parking is a separate HOA question in most communities and is prohibited or screened in many.</p>")
    body += sec("Four widening scenarios and what each one needs",
        table(["Scenario", "Permit", "Width limit", "What we watch"], [
            ("Add 4 ft on one side, unincorporated Osceola", "County driveway permit", "24 ft total (§22-50.6)", "Setback to the property line; the apron is tied into the county detail"),
            ("Add a parking pad beside the garage, not touching the street", "Usually none; HB 803 exemption request under $7,500", "No county width rule; HOA may cap it", "Drainage toward the neighbor is the usual complaint"),
            ("Widen inside Kissimmee city limits", "Driveway / Sidewalk Construction application, Engineering", "City reviews width with the application", "Right-of-way work needs Public Works; sidewalk section has to stay to grade"),
            ("Widen in a Polk County resort community", "Permit for the right-of-way and setback portions; Paver Release Form if pavers go in the right-of-way", "HOA rules bind first; Solterra caps expansion at three cars wide", "Association wants a survey and the installer's insurance certificate"),
        ], caption="Rules verified on the official pages on 2026-09-10; the jurisdiction pages quote each source."), cls="alt")
    body += sec("The apron is a different animal",
        f"""<p>The part of your driveway between the property line and the street is in the public right-of-way, and it belongs to the jurisdiction even though you maintain it. That is why widening projects stall: the homeowner and the contractor agree on the new width, and then the county detail requires the apron to flare at a set radius, to be 6 inches thick, and in some jurisdictions to carry no steel at all so the utility can cut it cleanly. Orange County publishes exactly that requirement for driveways in its right-of-way. Osceola handles it through the driveway permit and LDC 4.12.2; the City of Kissimmee through the Engineering Division application.</p>
<p>Practically, this means two things for your quote. The apron section is priced differently from the rest of the drive, and the sidewalk crossing, where there is one, has to be replaced to the current detail rather than patched. Neither is optional and neither is a surprise if it is in the proposal, which is why ours separates the apron line from the driveway line.</p>""")
    body += sec("Parking on the widened area is its own rule",
        f"""<p>Widening a driveway and being allowed to park on it are separate questions. Osceola County's parking ordinance regulates where vehicles may stand on residential property, and communities layer their own rules on top: several associations in Poinciana, Celebration and the Four Corners resort corridor restrict boats, trailers and commercial vehicles regardless of how much paving exists. Solterra's guidelines run the other way and tie the paving itself to a car count, capping an expanded driveway at three cars wide and barring extra walking areas alongside it.</p>
<p>So the order of operations is: check the association rule, then the county width rule, then design. Reversing that order produces a driveway that is legal and unusable, or approved by the county and torn out by the board. Our {tool('hoa-packet-checklist')} assembles what the association wants to see, and {hoa('solterra')} quotes one association's text in full as an example of how specific these documents get.</p>""")
    faqs = [
        faq("How wide can a driveway be in Osceola County?", "24 feet in unincorporated Osceola without a conditional use; the cities review width with the application."),
        faq("Do I need a permit to widen my driveway?", "Yes: the county driveway permit under §22-50.6, or the city's application inside Kissimmee or St. Cloud."),
        faq("Can I widen onto the grass by the street?", "That strip is usually public right-of-way; the widening needs the driveway permit and the apron follows the jurisdiction's detail."),
        faq("Will the HOA allow a third-car width?", "Solterra allows up to three cars; others vary. Approval comes before the permit."),
        faq("Can I widen my driveway to the property line?", "Not usually. Side setbacks apply, and in unincorporated Osceola the total width is capped at 24 feet without a conditional use. We check the plat and the setback before designing."),
        faq("Do I need a survey to widen?", "The county does not always require one, but most associations do, and it settles setback questions before the concrete is ordered."),
        faq("Can the widened strip be pavers instead of concrete?", "Yes, and it is a good use for pavers because the seam between old and new concrete never matches. In Polk County pavers in the right-of-way need the recorded release form."),
    ]
    return page("driveway-widening-rules-osceola", "Driveway Widening Rules: Osceola County, Kissimmee and St. Cloud", "How wide a residential driveway can be and what widening requires in unincorporated Osceola (24 ft, §22-50.6), Kissimmee, St. Cloud, Polk and Orange, plus HOA limits like Solterra's three-car rule and how a widening is built.", body, faqs, ["osceola-22-50-6", "kissimmee-driveway", "stcloud-permits", "polk-faq", "orange-permit", "solterra"])


def rainy():
    body = sec("Pouring concrete in the rainy season",
        cap("From June through September the Kissimmee 2 NOAA station averages 15.8, 16.7, 17.7 and 14.3 days a month with measurable rain, and 12 or 13 of those days bring more than a tenth of an inch, almost all of it in afternoon sea-breeze storms. We pour through the season with one rule: the truck is on site at first light, the slab is placed, finished, jointed and covered before 2 p.m., and a morning forecast over 60 percent for rain before 2 p.m. moves the pour a day."),
        eyebrow="Guide")
    body += sec("What rain does to concrete at each stage",
        table(["Stage", "Light rain", "Downpour", "What we do"], [
            ("Before the pour (forms and base set)", "Nothing", "Saturates the base; standing water in forms", "Pump or wait; never pour into standing water"),
            ("During placement", "Fine; slightly more water at the surface", "Washes cement out of the top; ruins the surface", "Cover with plastic immediately; stop the truck"),
            ("Finishing (bleed water, edging, brooming)", "Delays finishing; risk of marks", "Weak, scaling surface for life", "Cover; re-broom after it passes if still workable"),
            ("First hours after finishing", "Helpful (moist curing)", "Pitting if very heavy in the first hour", "Cover with plastic held off the surface; joints cut on time"),
            ("After 24 hours", "Helpful", "Helpful", "Nothing; concrete cures better wet"),
        ]), cls="alt")
    body += sec("The day-of routine", steps([
        "Radar and forecast at 5 a.m.; the decision is made before the truck is dispatched.",
        "Forms, base and steel are done the day before; the crew is standing when the truck arrives at daylight.",
        "Pours are sized to be finished by late morning; a 480-square-foot driveway is one truck and done by 10.",
        "Plastic sheeting and stakes are on site; if a cell builds early, the slab is covered before the first drops.",
        "Joints are tooled during finishing or saw-cut the same afternoon once the surface can take a saw.",
        "Cure compound or wet cover goes on before the crew leaves; the storm that arrives at 3 p.m. is then good for the slab.",
    ]))
    body += sec("Overlays, sand and sealers are less forgiving", f"<p>A polymer overlay is a fraction of an inch thick and a downpour 30 minutes after placement takes it off. Polymeric sand needs a dry day and a dry night to harden; sealers need 24 hours without rain to cure clear. For those we book a morning with a clear radar and we reschedule rather than gamble; expect one lost day in a rainy-season schedule and none from October to April. The {tool('pour-calendar')} shows the month-by-month numbers and the plan for each type of work.</p>", cls="alt")
    body += sec("Hurricane season", "<p>June 1 to November 30. A named storm in the five-day forecast pauses scheduling: no forms left open, no material staged in a yard that will flood, no pours the day before landfall. After a storm the queue is long; homeowners with a driveway that flooded or a slab that lifted get triage visits first.</p>")
    body += sec("What happens if rain arrives at each stage",
        table(["Stage", "Rain during it", "What we do", "Effect on the finished slab"], [
            ("Base preparation", "Light", "Keep working; limerock compacts better slightly damp", "None"),
            ("Base preparation", "Heavy", "Stop; the subgrade turns to soup and cannot be compacted", "Delay of a day or two while it drains"),
            ("Placing concrete", "Light shower", "Keep placing; do not add water; cover finished areas", "Usually none if the surface is not worked wet"),
            ("Placing concrete", "Downpour", "Stop the truck, tarp what is down, resume or cut a cold joint", "A planned joint instead of a random one"),
            ("Floating and troweling", "Any", "Stop and cover; working rainwater into the surface is what causes scaling", "Scaling and a dusty surface if ignored"),
            ("First 2 hours after finishing", "Any", "Cover with plastic on supports so it does not touch the surface", "Pitting and washed-out cement paste if uncovered"),
            ("After 12 hours", "Any", "Nothing; rain is now helping the cure", "None"),
        ], caption="Our field rules. The risk window is narrow, which is why an early start matters more than the daily forecast."), cls="alt")
    body += sec("Reading a Central Florida forecast for a pour",
        f"""<p>A 60 percent chance of rain in Kissimmee in July does not mean a 60 percent chance your pour gets wet. It usually means the sea-breeze collision will fire storms somewhere in the county between 2 and 6 p.m. The number that matters to us is the timing, not the probability, so we watch the morning radar and the hourly breakdown rather than the daily percentage. A slab placed at 7 a.m. and finished by 11 is out of the risk window before the first cell forms.</p>
<p>The NOAA normals for the Kissimmee 2 station tell the same story in averages: June through September carry 15.8, 16.7, 17.7 and 14.3 days with measurable rain, and 12.3, 12.2, 13.0 and 9.5 of those days exceed a tenth of an inch. October through April drop to between 5.7 and 8.7 days. The rain is not spread through the day; it is concentrated in the afternoon, which is exactly why the pour window exists. The month-by-month table is in the {tool('pour-calendar')}.</p>""")
    body += sec("Hurricane season and the schedule",
        f"""<p>The Atlantic season runs June 1 to November 30, and its effect on our schedule is less about the storm than about the week around it. When a named system is forecast to affect Central Florida, we stop starting new excavations three days out, because an open base trench fills and has to be rebuilt. Freshly placed concrete is safe once it has set; a slab poured two days before a storm is in better shape than a base sitting open.</p>
<p>After a system passes, the ground stays saturated for several days on flatwoods sand, and that is the delay homeowners feel. The Polk ridge drains faster, so Davenport and Haines City jobs restart a day or two before Osceola jobs do ({guide('paver-base-flatwoods-vs-ridge')}). We reschedule in order of who was interrupted, and we say so in advance rather than promising a date we cannot hold.</p>""")
    faqs = [
        faq("Can you pour concrete in the rain in Florida?", "Not during rain. We pour before the afternoon storms, finish and cover; rain after the first hours helps the cure."),
        faq("What if it rains on fresh concrete?", "In the first hour a downpour can pit or wash the surface; covered, it is fine. After 24 hours rain is good for it."),
        faq("Is summer a bad time for a driveway?", "It is the busiest and the wettest; the work is fine with early starts. Sealing and sanding lose the occasional day."),
        faq("What time do you start?", "Trucks at daylight in summer; a two-car driveway is finished by mid-morning."),
        faq("Will you pour if rain is forecast?", "Often yes, with an early start, because the forecast is for the afternoon. We move the pour when the morning hours themselves look wet."),
        faq("Does rain ruin fresh concrete?", "Rain during finishing does, by washing cement from the surface and causing scaling. Rain after the slab has set is harmless and helps the cure."),
        faq("What is the best month for a driveway in Kissimmee?", "October through April, when rain days drop to six or seven a month. May and the early fall work well too; the constraint is the afternoon storm, not the month."),
    ]
    return page("rainy-season-concrete-scheduling", "Pouring Concrete in the Rainy Season: Scheduling Around Storms", "June–September average 14–18 rain days a month at the Kissimmee 2 station. What rain does at each stage of a pour, the first-light routine, the 60-percent rule, why overlays, polymeric sand and sealers wait for dry days, hurricane season.", body, faqs, ["noaa"])


def verify():
    body = sec("There is no license to check. Here is what to check instead.",
        cap("Florida issues no state contractor license for concrete flatwork, pavers or stucco; those trades are not among the categories in s. 489.105, and s. 489.117(4)(a) lists 'driveway or tennis court installation', 'decorative stone, tile, marble, granite, or terrazzo installation' and 'stuccoing' among job scopes for which a local government may not require a license, a preemption that took full effect July 1, 2023. So 'licensed' on a driveway contractor's truck either refers to a license for other work or means nothing. Check five things that do exist: insurance, the legal entity, references, the written contract, and the spec."),
        eyebrow="Guide")
    body += sec("The five checks", steps([
        "<strong>Insurance certificate.</strong> Ask for a certificate of insurance showing general liability and workers' compensation (or a valid exemption), with the agent's contact. Call the agent to confirm it is current. HOAs like Solterra can require the certificate to name the association.",
        "<strong>Legal entity.</strong> Ask for the exact business name and check it on Sunbiz (search.sunbiz.org): active status, filing date, principal address, registered agent. A fictitious name (DBA) should be registered too. If the name on the contract, the truck and Sunbiz do not match, ask why.",
        "<strong>References and addresses.</strong> Two or three jobs of the same type from the last two years, with addresses you can drive past. Look at the apron seam, the joints and the edges, not the middle of the slab.",
        "<strong>The written contract.</strong> Scope, thickness, PSI, reinforcement and how it is held, base depth and compaction, joint layout, drainage, what happens to the old surface, permit and HOA responsibility, exclusions, schedule, payment terms, and the workmanship warranty in words. Full payment up front is a red flag; a deposit for materials and permits is normal.",
        "<strong>The spec against the load.</strong> Four inches with fiber and edge steel for cars; six with a grid for boats and RVs; 6 inches of base under pavers; a concrete apron at the street. A quote that says 'four inches with mesh' and nothing about base is describing a different job.",
    ]))
    body += sec("What a license does and does not tell you", f"<p>A contractor who holds a Florida building, residential or general contractor license (verifiable at myfloridalicense.com) is licensed for structures; that license is real and relevant if the job includes footings, a retaining wall over 4 feet, a pool shell or a room addition, and s. 489.119(5)(b) requires the number in that contractor's advertising. It says nothing about how the contractor compacts base. For flatwork and pavers, the checks above are the whole story. Our own position is on the <a href=\"/about/\">About page</a>: we state the entity, insurance and warranty in every proposal and we do not claim a license we do not need.</p>", cls="alt")
    body += sec("Signs of trouble", "<ul><li>No street address or Sunbiz record for the name on the quote.</li><li>'Licensed and insured' with no certificate and no number when asked.</li><li>Price far below the range for the spec, with base or steel missing from the description.</li><li>Cash discount for skipping the permit.</li><li>Pressure to sign today; a crew 'in the area with leftover material'.</li><li>No written warranty, or a warranty that is a phone number.</li></ul>")
    body += sec("Tools for the comparison", f"<p>The {tool('project-brief')} fixes the spec so every bidder quotes the same job; the {tool('concrete-paver-calculator')} gives the planning range; the <a href=\"/pricing/\">cost guides</a> explain the ranges. Permit responsibility by office: <a href=\"/permits/\">permits hub</a>.</p>", cls="alt")
    body += sec("The five-minute verification anyone can do",
        steps([
            "Search the business name on Sunbiz, the Florida Division of Corporations site. You want an active entity, a registered agent, and a name that matches the one on the proposal. A contractor who cannot be found there is either brand new or trading under a name nobody registered.",
            "Ask for the certificate of insurance and read the dates and the limits. It should name the insurer, the policy period covering your job, general liability, and workers' compensation or a valid exemption. Ask for it to be sent by the agent, not forwarded as a photo.",
            "Check the DBPR license lookup only for the trades that need one. Concrete flatwork, pavers and stucco will not appear there, and that is expected under s. 489.117(4)(a); a pool, a structural wall or a room addition will.",
            "Ask which office will issue the permit for your address and listen for a specific answer. Someone who works here daily will say 'Osceola County driveway permit' or 'the city's EnerGov application' without hesitating.",
            "Ask for two addresses of jobs finished more than two years ago in your area, and drive past them. New work looks good; two-year-old work tells you about the base.",
        ]))
    body += sec("What the contract should contain",
        table(["Item", "Why it matters"], [
            ("Legal entity name and address", "It is who you would sue and who the insurance covers"),
            ("Scope with dimensions", "Square footage, thickness, PSI, reinforcement, base depth, joint layout, finish"),
            ("Drainage and slope", "The most common source of disputes here; it should be stated, not assumed"),
            ("Who pulls the permit and who pays the fee", "Under Florida law the owner signs the application and often the notice of commencement"),
            ("Notice of commencement responsibility", "Required in Osceola County for jobs of $5,000 or more and recorded before the first inspection"),
            ("Payment schedule tied to milestones", "Deposit, base and forms, pour, completion. A large deposit with no milestones is a risk"),
            ("Change-order process in writing", "Site surprises happen; the process should not be a phone call"),
            ("Workmanship warranty term and what it excludes", "A warranty with no exclusions listed is not a warranty"),
            ("Lien-law disclosure", "Florida's construction lien law requires specific notices; the contract should reference them"),
            ("Cure and use restrictions", "When you can walk, park and load the slab"),
        ]), cls="alt")
    body += sec("Red flags we hear about from homeowners",
        f"""<p>The pattern is consistent. A door knock offering leftover material from a job down the street. A price quoted per job with no dimensions. A deposit of half or more before anything is delivered. A refusal to put thickness and PSI in writing. A promise that the slab will never crack. A company name that changes between the truck, the invoice and the bank deposit instruction. A quote that is forty percent below three others, which usually means 2½ inches of concrete on raw sand and no permit.</p>
<p>None of these is illegal on its own, and plenty of good crews are small and informal. But each one removes a piece of your recourse, and on a driveway you will live with for twenty-five years the recourse is the point. The counterweight is simple: a written scope, an insurance certificate from the agent, a permit number, and a payment schedule that keeps you slightly ahead of the work.</p>""")
    faqs = [
        faq("Do concrete contractors need a license in Florida?", "No state license exists for flatwork, pavers or stucco, and since July 1, 2023 local governments may not require one for driveway or decorative stone and paver work (s. 489.117(4)(a)). Structural work (footings, walls over 4 ft, pools) needs a state-licensed contractor."),
        faq("How do I verify a contractor's insurance?", "Ask for the certificate and call the agent listed on it to confirm it is in force."),
        faq("How do I check a business on Sunbiz?", "Search the exact name at search.sunbiz.org; confirm it is active and note the filing date and principal address."),
        faq("Is a deposit normal?", "A deposit for materials and permit fees at signing is normal; full payment up front is not."),
        faq("Are you licensed?", "For flatwork and pavers there is no license to hold; we are insured and put the entity name, certificate and warranty in every proposal."),
        faq("Is it legal for an unlicensed person to pour my driveway in Florida?", "Yes for flatwork, pavers and stucco, because no state license category covers them and local licensing is preempted. It is not legal for structural work, pools or additions, which do require a licensed contractor."),
        faq("What if the contractor has no workers compensation?", "Florida allows officer exemptions for small entities. Ask to see the exemption certificate rather than taking silence for an answer, and understand that an injury on your property without coverage can reach your homeowners policy."),
        faq("Should I pay cash for a discount?", "A discount for cash is common and legal. Paying in cash without a written contract, a receipt and a permit is where people lose their recourse."),
    ]
    return page("how-to-verify-a-concrete-contractor-florida", "How to Verify a Concrete Contractor in Florida (No License)", "Florida does not license concrete flatwork, pavers or stucco and s. 489.117(4)(a) bars local licenses. Five checks that do exist: insurance certificate, Sunbiz entity, references, the written contract, and the spec against the load. Red flags.", body, faqs, ["fs489117", "sunbiz", "dbpr"])


def str_guide():
    body = sec("Hardscape for vacation-rental owners in Four Corners, ChampionsGate, Reunion and Windsor Hills",
        cap("A rental pool deck sees more feet, more chemicals and more pressure-washing in a year than a family home's sees in five, the work has to fit a turnover gap, the HOA and the property manager both sign off, and the owner is often out of state. This guide covers the surfaces that hold up, how we schedule, what the associations require, and what it costs in the current index."),
        eyebrow="Guide")
    body += sec("Surfaces that survive rental use",
        table(["Surface", "Rental verdict", "Why"], [
            ("Sealed concrete pavers (60 mm deck, 80 mm drive)", "Best value", "Tough, cheap to relay, colors on file with every resort HOA; anti-slip sealer and polymeric sand rated for cleaning"),
            ("Travertine, tumbled, penetrating sealer with grit", "Premium listings", "Cooler barefoot; needs the right sealer and a monthly rinse on salt pools; stone-safe cleaners only"),
            ("Textured coating (cool deck)", "Budget refresh", "Cheapest on a sound deck; re-coat every 5–8 years; patches show"),
            ("Marble, large-format porcelain", "Luxury listings", "Coolest and cleanest; porcelain is stain-proof; higher cost"),
            ("Plain gray concrete", "Avoid on decks", "Hot, stains, slick when sealed glossy"),
            ("Artificial turf", "Side yards only", "Hot in sun; pet-friendly; not a deck surface"),
        ]), cls="alt")
    body += sec("Scheduling in a turnover gap", steps([
        "The manager sends the booking calendar; we pick a gap: one night for sealing, two for a repair, three to four for a deck overlay, five to seven for a rebuild.",
        "Material is staged the day before check-out (pavers, coping, sand) in the driveway or garage with the manager's OK.",
        "Work starts the morning of check-out; coping mortar goes in on day one so it has 48 hours before guests.",
        "Sealer is applied on the last morning; walkable in four hours, dry for evening check-in.",
        "The manager gets photos and the permit or ARC letter for the file; we leave spare pavers boxed in the garage.",
    ]) + "<p>Group days: several homes under one manager cleaned on day one and sealed on day two bring the per-home price to the low end of the range.</p>")
    body += sec("Sign-off from the manager, the HOA and the county",
        f"<p>Every resort community reviews visible changes. Solterra's guidelines are verified and cap expanded driveways at three cars, prohibit painted or stained concrete, and allow the Board to require the installer's insurance certificate naming the association ({hoa('solterra')}). Windsor Hills, Windsor Palms, Emerald Island, ChampionsGate, Storey Lake and the Reunion sections use management forms whose written criteria we have not published; Reunion's three management companies are listed on the {city('reunion')} page. County: Osceola for Windsor Hills, Emerald Island, ChampionsGate and Reunion; Polk for Solterra, Solara, Bella Vida and Paradise Palms; an overlay outside setbacks is flatwork, a deck tied to the cage footer is confirmed ({tool('permit-finder')}, {tool('hoa-packet-checklist')}).</p>", cls="alt")
    body += sec(f"What it costs ({R})", table(["Job", "Range", "Gap needed"], [
        ("Seal a 500 sq ft deck + 400 sq ft driveway", f"$1,575–$2,925 ({cost_range('paver-sealing')})", "1–2 nights"),
        ("Paver overlay on a 600 sq ft deck", f"$9,000–$14,400 + coping ({cost_range('paver-pool-deck')})", "3–4 nights"),
        ("Travertine on a 600 sq ft deck", f"$12,000–$21,600 + coping ({cost_range('travertine-pool-deck')})", "4–5 nights"),
        ("Lift-and-relay a settled driveway, 440 sq ft", f"$3,960–$7,040 ({cost_range('paver-repair')})", "2–3 nights"),
        ("Replace an apron corner", "$500–$900", "1–2 nights"),
    ], caption=f"{R} Kissimmee Concrete Cost Index ranges; resort access and scheduling put jobs toward the top."))
    body += sec("Owner checklist", "<ul><li>Give the manager and us the same spec (use the project brief).</li><li>Ask for the ARC letter and the permit number for the file; a buyer's inspector will.</li><li>Keep a box of spare pavers in the garage.</li><li>Put sealing on a two- to three-year cycle in the maintenance budget.</li><li>Tell the cleaning crew to use a wide tip and to stay off the joints.</li></ul>", cls="alt")
    body += sec("The turnover math",
        f"""<p>A short-term rental in Four Corners, ChampionsGate, Reunion or Windsor Hills that is booked at seventy percent occupancy has roughly nine free days a month, and they are rarely consecutive. That is the real constraint on hardscape work, not the weather. So we plan resort jobs backwards from the calendar the property manager sends us.</p>
<p>Rough durations to plan against: a paver pool deck overlay on an existing sound deck, three to four days; a full deck rebuild, five to seven; a paver driveway with the old concrete removed, three to five; sealing an existing deck, one day plus 24 hours of cure before furniture returns; a concrete repair of one or two panels, two days. Add the association's review time in front of all of it, which in the communities we have verified runs from a two-week cycle to a monthly meeting.</p>""")
    body += sec("What guests actually damage",
        table(["Surface", "Typical failure in a rental", "What we specify instead"], [
            ("Sealed concrete pool deck with a glossy coating", "Slips when wet, wears in traffic lanes within a season", "Textured finish or a matte penetrating sealer with grit"),
            ("Dark paver pool deck", "Surface heat complaints in July; guests stay off it", "Light travertine, marble or a light concrete paver"),
            ("Sand-set pavers at the grill and dining area", "Joint sand washes out under table legs and pressure washing", "Polymeric sand, sealed; a concrete pad under the grill"),
            ("Thin concrete apron at the drive entry", "Cracks under delivery vans and rental SUVs", "6 inches with edge steel at the apron"),
            ("Unsealed travertine coping", "Stains from sunscreen and drinks", "Penetrating stone sealer at handover and every two to three years"),
        ], caption="Patterns we see on rental properties in the resort corridor; the fix is specification, not maintenance."), cls="alt")
    body += sec("Who signs off, in order",
        f"""<p>Rental communities have more layers than a normal subdivision. The property manager schedules and usually holds the gate access. The association's architectural committee approves the change, and in Reunion that means one of three management companies depending on which product type your home is. The county issues the permit where one is needed, which for a pool deck overlay in unincorporated Osceola often means none, and for a driveway means the county driveway permit. And the owner, who may be out of state, signs the application and the notice of commencement.</p>
<p>We prepare the packet once and send it to all of them together, because the slowest link sets the start date. What goes in it is on the {tool('hoa-packet-checklist')}, and the community pages for {hoa('solterra')} and {hoa('celebration')} show the level of detail two of these boards actually ask for.</p>""")
    faqs = [
        faq("Can a pool deck be redone between guests?", "An overlay in three to four nights, sealing in one; rebuilds need five to seven and a blocked calendar."),
        faq("Which surface is best for a rental deck?", "Sealed concrete pavers for value; travertine for premium listings; both with an anti-slip penetrating sealer."),
        faq("Do you work with property managers?", "Weekly; we work from the booking calendar and send photos and paperwork to the manager."),
        faq("Will the HOA need my contractor's insurance?", "Solterra can require the certificate naming the association; others may. We provide it."),
        faq("Do you offer group pricing?", "Yes, for several homes under one manager on one day."),
        faq("Can work be done between guests?", "A sealing visit or a single panel repair, yes. A deck rebuild needs a block of five to seven days, which usually means a deliberate gap in the calendar."),
        faq("Do I need to be in Florida for the work?", "No. The owner signs the application and the notice of commencement, which can be handled remotely, and the property manager provides access. We send daily photos on out-of-state jobs."),
        faq("Does a paver deck raise the nightly rate?", "We have no data that would let us claim that, and we will not. What we can say is that surface heat and slip complaints show up in reviews, and both are specification choices."),
    ]
    return page("vacation-rental-owner-hardscape-guide", "Pool Decks & Driveways for Vacation Rental Owners (Four Corners)", "Hardscape for short-term rentals in Four Corners, ChampionsGate, Reunion and Windsor Hills: surfaces that survive rental use, turnover-gap scheduling, manager and HOA sign-off (Solterra verified), county rules and current costs.", body, faqs, ["solterra", "polk-faq", "osceola-faq"])


def roots():
    body = sec("Live oak roots and driveways",
        cap("A live oak planted in a 1980s Kissimmee front yard has a root plate that now runs 30 to 50 feet from the trunk, an inch or two below the surface, and a 4-inch slab across it lifts 1 to 3 inches within a decade. Cutting the roots that lifted the slab endangers the tree and is regulated in some jurisdictions; the working answers are a root barrier at pour time, a thicker bridging section, rerouting the walk, or accepting a periodic panel replacement."),
        eyebrow="Guide")
    body += sec("Options and what they cost",
        table(["Option", "When", "How", "Cost"], [
            ("Grind the lip", "Lift under ¾ in on a walk", "Grind the high edge flush", "Minimum visit"),
            ("Root barrier + replace the panel", "Lift over ¾ in; tree worth keeping", "Cut roots smaller than 2 in at the slab edge, install a 24-in vertical barrier, replace the panel over a compacted base", "$1,300–$2,300 per panel"),
            ("Thicker bridging section", "Roots cannot be cut; slab must cross", "6-in section with a rebar grid spanning the root zone; joints either side", "6-in rates plus removal"),
            ("Reroute the walk", "Walk can curve", "Curve the walk outside the root plate; usually cheaper than fighting it", "Walk rates for the new run"),
            ("Pavers over the root zone", "Patio or walk, not driveway", "Sand-set pavers lift and relay easily as roots grow", "Paver rates; periodic relay"),
            ("Remove the tree", "Last resort; permit often required", "Arborist and permit; stump and root removal before pouring", "Arborist quote + slab"),
        ]), cls="alt")
    body += sec("Where it shows up", f"<p>Downtown Kissimmee and St. Cloud, Kissimmee Bay, Buenaventura Lakes, the older Poinciana villages, Celebration's tree-lined streets and the historic cores of Davenport, Haines City and Lake Wales. New subdivisions plant small trees far from the drive; the problem is a 1980s and 1990s one, and it compounds with the base problems on this sand ({guide('why-concrete-cracks-osceola')}). Tree protection rules exist in Kissimmee, St. Cloud, Celebration (street trees are the CROA's) and the counties; cutting a large root or removing a protected tree can need approval, so we ask before we cut.</p>")
    body += sec("How we build near a tree", "<p>Keep the slab edge as far from the trunk as the layout allows; install a root barrier along the tree side of the pour, 24 inches deep, before the base goes in; keep base compaction light over the root plate; use a thicker, reinforced section where the slab must cross; set joints so a future lift breaks at a joint and one panel can be replaced. On walks, curve away.</p>", cls="alt")
    body += sec("Which trees cause this",
        table(["Tree", "Root habit", "Risk to flatwork", "Typical distance"], [
            ("Live oak (Quercus virginiana)", "Wide, shallow lateral roots that thicken with age", "High; the classic Kissimmee driveway lifter", "Roots commonly reach well past the canopy edge"),
            ("Laurel oak", "Similar but shorter-lived and more surface-rooted", "High", "Similar to live oak"),
            ("Southern magnolia", "Dense shallow mat", "Moderate; lifts walks more than drives", "Near the canopy line"),
            ("Sabal palm", "Fibrous, non-thickening roots", "Low", "Close planting is usually fine"),
            ("Slash pine", "Deeper taproot with laterals", "Low to moderate", "Roots rarely lift a slab"),
            ("Ficus and rubber trees", "Aggressive, invasive", "Very high; also damages pipes", "Keep far from any hardscape"),
        ], caption="Behaviour we see on jobs in Osceola County. A certified arborist is the right person to judge a specific tree's health and root spread before roots are cut."), cls="alt")
    body += sec("Root barriers, and their limits",
        f"""<p>A root barrier is a rigid panel, usually ribbed polyethylene 18 to 24 inches deep, set vertically in a trench between the tree and the slab. The ribs direct roots downward rather than letting them run along the barrier face. Installed at pour time it is cheap; retrofitted later it means a trench, and the trench cuts roots, which is where an arborist has to weigh in on whether the tree survives it.</p>
<p>What a barrier does not do is stop a root that is already under the slab, and it does not protect a slab poured directly over the root plate. On a mature live oak, the honest options are to route the driveway around the canopy, to thicken and reinforce the section crossing the root zone so it spans rather than follows the lift, to build that section in pavers so it can be relaid when it moves, or to accept a shorter service life. We price those alternatives side by side rather than quietly pouring over the roots.</p>""")
    body += sec("Cutting roots is a decision with consequences",
        f"""<p>Rules on tree removal and root pruning vary by jurisdiction and by association, and mature trees are often protected. Before we cut anything larger than about two inches in diameter we want an arborist's opinion in writing, because removing a significant share of a live oak's root plate on one side can destabilize a tree that has stood for eighty years, and a fallen oak costs far more than a lifted driveway. Where the tree is protected or the risk is real, the design changes instead of the tree.</p>
<p>This is one of the few places where pavers have a decisive advantage. A paver driveway crossing a root zone will still lift, but lifting it back is a maintenance visit, not a demolition. The comparison is in {compare('concrete-vs-pavers')}, and the repair scope is on {svc('paver-repair')}.</p>""")
    faqs = [
        faq("Can you cut the roots that lifted my driveway?", "Small roots at the slab edge, with a barrier. Large structural roots near the trunk, no; that kills or destabilizes the tree and may need approval."),
        faq("Will a root barrier stop it for good?", "For a decade or more; roots eventually grow under or around. It is the best value short of rerouting."),
        faq("Should I just remove the oak?", "Only as a last resort; it usually needs a permit and the shade is worth more than the panel."),
        faq("Pavers or concrete near a tree?", "Pavers on a patio or walk; they relay easily. On a driveway, concrete with a barrier and a bridging section."),
        faq("Can you just cut the roots and pour over them?", "We will not cut significant roots without an arborist signing off. A large live oak destabilized by root loss is a much bigger problem than the slab."),
        faq("Will a root barrier fix an existing lift?", "No. It stops future roots from following the same path. The lifted panel still has to be replaced or, if it is pavers, relaid."),
        faq("How far from an oak should a driveway be?", "Farther than most lots allow, which is why design usually means routing, spanning or choosing pavers rather than achieving a safe distance."),
    ]
    return page("tree-roots-driveways-central-florida", "Live Oak Roots and Driveways: What Lifts a Slab and What to Do", "Live oak roots lift 4-inch slabs in Kissimmee's older neighborhoods within a decade. Options with costs: grind, root barrier plus panel replacement, thicker bridging sections, rerouting, pavers over the root zone, and when removal is the last resort.", body, faqs, [])


def base_guide():
    body = sec("Two soils, two base problems",
        cap("Osceola County's flatwoods (Smyrna, Myakka, Immokalee, EauGallie fine sands) are level and wet: a water table about 12 inches down in summer, and fine sand that loses support when water moves through it. The Polk ridge (Candler, Astatula, Tavares sands) is dry and deep: no water table, but sand with so few fines that it will not compact until it is wetted. The same 6-inch limerock base is placed differently on each, and most local settling traces to getting that wrong."),
        eyebrow="Guide")
    body += sec("The two soils, from the USDA survey",
        table(["", "Flatwoods (Osceola)", "Ridge (Polk)"], [
            ("Map units", "Smyrna 188,635 ac, Myakka 122,954, Immokalee 70,229, EauGallie 42,853, Basinger 44,637 (+47,191 depressional)", "Candler 97,496 ac, Tavares 53,679, Astatula 34,785 (Polk survey)"),
            ("Drainage class", "Poorly to very poorly drained", "Excessively to moderately well drained"),
            ("Wet-season water table", "~12 in (Basinger 6 in; depressional: surface)", "None near the surface (except lake margins)"),
            ("Failure mode", "Saturation and washout under the slab edge; settling at downspouts", "Base placed dry never compacted; settles the first rainy season"),
            ("Base placement", "Proof-roll, remove muck, geotextile if wet, compact in lifts, drain to a swale", "Wet the subgrade and each lift, compact, probe; fewer drainage issues"),
            ("Slab elevation", "Raise 2–8 in on fill in low spots", "At grade is fine; slope matters more (lots roll)"),
            ("Where", "Kissimmee, St. Cloud, BVL, Poinciana (Osceola side), Harmony, Narcoossee, Celebration", "Four Corners, ChampionsGate, Davenport, Haines City, Lake Alfred, Auburndale, Winter Haven, Dundee, Lake Wales"),
        ], caption="USDA NRCS Soil Data Access, survey areas FL097 and FL105, queried 2026-09-10."), cls="alt")
    body += sec("The flatwoods routine", f"<p>Excavate to depth, proof-roll the subgrade, dig out any muck or root mass and replace with fill in 4-inch lifts, lay geotextile where the subgrade is wet or organic, place limerock in 3-inch lifts and compact each to refusal, check with a probe rod, and build the surface to fall at least ⅛ inch per foot to a swale or drain. Extend downspouts past the slab. On Basinger or Placid units, raise the whole assembly on fill; a slab poured flush there is under water every June ({city('harmony')}, {city('st-cloud')}).</p>")
    body += sec("The ridge routine", f"<p>Candler sand has no silt or clay to bind it; dry, it stays loose under a plate compactor no matter how many passes. Wet the subgrade with a hose until it holds a footprint, compact, then wet and compact each lift of limerock the same way, and probe. The first rainy season will not then do the compaction for you. Slopes are steeper on the ridge, so a drive that falls to the garage gets a trench drain and a patio on a sloped lot gets stepped or built up ({city('davenport')}, {city('haines-city')}, {city('lake-wales')}).</p>", cls="alt")
    body += sec("Why builder driveways fail in both places", f"<p>Production crews on a schedule place base in an afternoon and pour the next day. On the flatwoods that base went on saturated sand in July; on the ridge it went on dry sand and read compacted when it was not. Five years later the garage panel has dropped in both subdivisions for opposite reasons. The repair is the same, a base rebuilt the right way for the soil ({svc('paver-repair')}, {svc('concrete-repair')}, {guide('why-concrete-cracks-osceola')}).</p>")
    body += sec("The soil under each city we work in",
        table(["Area", "Dominant map units (USDA)", "Drainage class", "Wet-season water table", "What it means for base"], [
            ("Kissimmee, Buenaventura Lakes, Poinciana (Osceola side)", "Smyrna fine sand; Myakka fine sand", "Poorly drained", "About 12 in", "Compact subgrade before base; slab must shed water; raise low areas"),
            ("St. Cloud, Narcoossee, Harmony", "Smyrna, Myakka, EauGallie; Basinger in the lows", "Poorly to very poorly drained", "12 in, 6 in on Basinger, at surface in depressions", "Fill and raise on low lots; swale to carry water off"),
            ("Celebration, ChampionsGate, Reunion", "Smyrna and Myakka, engineered fill over them", "Poorly drained, managed by community stormwater", "Varies with the pond system", "Check the as-built grade; do not block the lot's drainage path"),
            ("Davenport, Haines City, Loughman (ridge)", "Candler sand 0 to 5 percent; Astatula; Tavares", "Excessively drained", "Deep, rarely a factor", "Base will not compact dry; wet each lift and proof-roll"),
            ("Winter Haven, Auburndale, Lake Alfred", "Candler, Tavares, Pomona in the flats", "Mixed", "Deep on the ridge, shallow in flats", "Identify which side of the ridge line the lot is on"),
            ("Lake Wales, Dundee, Polk City", "Candler, Astatula, Archbold", "Excessively drained", "Deep", "Dry sand behaves like a liquid until it is wetted and compacted"),
        ], caption="Map-unit acreage and drainage class from USDA Soil Data Access queries for survey areas FL097 and FL105, run 2026-09-10. A single lot can differ from its map unit, which is why we probe on site."), cls="alt")
    body += sec("How we compact each one",
        f"""<p>On flatwoods sand the failure mode is saturation. The subgrade is proof-rolled first, soft pockets are dug out and replaced with structural fill in four-inch lifts, and limerock goes down in two lifts with a plate compactor or a roller depending on the area. We probe with a steel rod after each lift; a rod that pushes in by hand means the lift is not done. Moisture is usually already right, and in the wet season it is often too high, which is the reason a June job sometimes waits two days after a storm.</p>
<p>On ridge sand the failure mode is the opposite. Candler and Astatula sands are single-grained and almost cohesionless; dry, they shear under the compactor instead of densifying, and a base that looks compacted settles the first time a summer storm soaks it. So we wet each lift deliberately, compact it, and check it. Homeowners in Davenport who have watched a previous contractor run a plate compactor over bone-dry sand for ten minutes have seen the wrong method being applied with real effort.</p>""")
    body += sec("Base depth we specify",
        table(["Application", "Flatwoods sand (Osceola)", "Ridge sand (Polk)", "Note"], [
            ("Concrete driveway", "4 in compacted limerock", "4 in, wetted and compacted", "Subgrade prep matters more than an extra inch of rock"),
            ("Concrete patio or walk", "2 to 4 in", "2 to 4 in", "Thinner is acceptable on pedestrian loads"),
            ("Paver driveway", "6 in limerock in two lifts, 1 in bedding sand", "6 in, wetted", "Celebration's pattern book specifies 6 in for driveways"),
            ("Paver patio or pool deck", "4 to 5 in", "4 to 5 in", "Plus the bedding course"),
            ("RV, boat, workshop slab", "4 to 6 in", "4 to 6 in", "Under a 6-in slab with a rebar grid"),
            ("Low or depressional lot", "Structural fill to raise, then base", "Rarely needed", "The fill, not the slab, solves it"),
        ]))
    body += sec("Why this shows up in the price",
        f"""<p>Base is invisible once the job is done, which is exactly why it is the first thing cut in a cheap quote. Two proposals for the same driveway can differ by thirty percent because one includes proof-rolling, undercutting soft spots and six inches of rock in lifts and the other includes a skim of sand and a vibrating plate. Twelve months later they look identical. At year five, on Osceola sand, they do not.</p>
<p>So our proposals state base depth and material by name, and we would rather lose a job on that line than win it by matching a number that leaves the base out. If you are comparing quotes, the {tool('project-brief')} produces a one-page specification you can hand to three contractors so the base is priced the same way by all of them.</p>""", cls="alt")
    faqs = [
        faq("What soil is my lot on?", "Most of Osceola is Smyrna, Myakka or Immokalee fine sand; the Polk ridge is Candler, Astatula or Tavares sand. The permit finder shows the county, and we probe on site."),
        faq("Why wet the base on the ridge?", "Candler sand compacts only with moisture; dry base settles the first rainy season."),
        faq("Do flatwoods lots need fill?", "Low spots on Basinger, Placid or muck do; typical Smyrna lots need a compacted base and drainage, not fill."),
        faq("Is 6 inches of base always needed?", "Under a driveway, yes; 4 to 5 under patios and pool decks; 2 to 4 under a concrete patio."),
        faq("Is limerock or crushed concrete better?", "Both work. Crushed concrete is often cheaper and compacts well; limerock is the regional standard and is what most details specify. We use whichever the job and supply favour and name it in the proposal."),
        faq("Can base be skipped on sandy soil?", "Sand is not a base. It has no cohesion, it moves with water, and on the ridge it does not even compact until it is wetted. Every slab and paver field we build gets a base."),
        faq("How do you know which soil my lot has?", "We look up the USDA map unit for the parcel before the visit, then probe on site, because a single lot can differ from the mapped unit."),
    ]
    return page("paver-base-flatwoods-vs-ridge", "Paver Base on Flatwoods vs. Ridge Sand: Osceola and Polk", "Osceola's Smyrna/Myakka flatwoods (wet, 12-inch water table) and Polk's Candler ridge sand (dry, compacts only wet) need different base placement under pavers and slabs. USDA map units, the two routines, and why builder driveways fail in both.", body, faqs, ["sda", "icpi"])


def bvl_guide():
    body = sec("Replacing a 1980s driveway in Buenaventura Lakes",
        cap("Landstar Homes built Buenaventura Lakes from the late 1970s into the early 1990s, and the driveways were 4-inch slabs poured on graded sand with no base, no edge steel and joints far apart. After 35 to 45 wet seasons the pattern is the same on every street: a stepped panel at the garage, a diagonal crack from the apron corner, panels rocking on washed-out sand. This is what a replacement involves, what we find under the old slab, and what it costs."),
        eyebrow="Guide")
    body += sec("What we find when the slab comes out", "<ul><li><strong>No base.</strong> Concrete directly on Smyrna or Myakka fine sand, sometimes on a thin layer of shell.</li><li><strong>Washout at the garage and apron.</strong> A void an inch or two deep under the edge where roof water ran for decades.</li><li><strong>Wire mesh on the bottom.</strong> When mesh was used, it is lying on the sand, rusted, doing nothing.</li><li><strong>Roots.</strong> From the oaks planted with the house, now under the slab edge.</li><li><strong>Clean sand otherwise.</strong> Proof-rolled and topped with compacted limerock, it is a fine subgrade; imported fill is rare in BVL except near the retention lakes.</li><li><strong>An unpermitted widening.</strong> A second ribbon added without a permit, sometimes taking the total width past the county's 24 feet.</li></ul>", cls="alt")
    body += sec("The replacement, step by step", steps([
        "Site visit: measure, note the total width against the 24-foot rule, find the downspouts and the oak, probe the sand. Written proposal.",
        "County driveway permit (unincorporated Osceola, §22-50.6); Notice of Commencement if the job is $5,000 or more.",
        "Day 1: saw-cut at the garage and apron, break and haul the old slab, excavate, proof-roll, remove roots at the edge and set a root barrier.",
        "Day 1–2: 4 inches of limerock in lifts, compacted; forms set to fall toward the street; #4 bars at the edges and corners; fiber in the mix; expansion joint at the garage and the apron.",
        "Day 2 or 3: pour at first light (summer), broom finish, joints at 10 feet cut within 12 hours, cure.",
        "Downspouts extended past the slab, sod edges dressed, final inspection; cars after 7 days.",
    ]))
    body += sec(f"What it costs ({R})", table(["Item", "Range for a 432 sq ft (18×24) drive"], [
        ("Removal and haul-off", "$860–$1,730"),
        ("New 4-in broom-finish driveway", f"$3,670–$5,830 ({cost_range('concrete-driveway-broom')})"),
        ("Root barrier at the oak", "$250–$400"),
        ("Widening to 22 ft (+4 ft × 24 ft)", "$820–$1,300"),
        ("Pavers instead of concrete", f"$6,050–$9,500 ({cost_range('paver-driveway-concrete')})"),
    ], caption=f"{R} Kissimmee Concrete Cost Index; BVL jobs typically land at the low end because access is easy and the sand is clean."), cls="alt")
    body += sec("Repair, resurface or replace?", f"<p>One stepped panel with the others level: replace the panel and extend the downspout ({cs_link()}). Hairlines everywhere and one step: the drive is on one clock; we quote both. Resurfacing almost never fits in BVL because the slabs are moving ({compare('resurface-vs-replace')}). Concrete or pavers: {compare('concrete-vs-pavers')}. Area page: {city('buenaventura-lakes')}.</p>")
    body += sec("What we find when the old slab comes up",
        f"""<p>Buenaventura Lakes was platted and built out by Landstar Homes from the late 1970s into the 1990s, and the driveways went in the way driveways went in then: roughly four inches of concrete, poured on graded native sand, with wire mesh that ended up on the bottom and joints that were often tooled shallow or skipped. Four decades of wet seasons later we are pulling those slabs up across the neighbourhood, and the picture underneath is consistent.</p>
<p>There is no base. Under the slab is the same Smyrna or Myakka fine sand that is under the lawn, usually with a scoured channel running from wherever the downspout has been discharging. The mesh, when there is any, is lying in the bottom inch, rusted through in the wet zone. Irrigation lines are often directly under the slab edge because they were trenched after the drive went in. And in the older streets the live oaks planted at build-out have put roots under the apron, which is why so many BVL driveways step up near the street rather than at the garage.</p>""")
    body += sec("The sequence on a BVL replacement",
        steps([
            "Locate utilities through 811 and mark the irrigation, which on these lots is rarely where the homeowner thinks it is.",
            "Saw-cut a clean line at the garage slab and at the right-of-way, so the new pour has a straight joint rather than a broken edge.",
            "Break out and haul the old slab the same day; on a typical 480 to 600 square foot BVL drive that is one to one and a half loads.",
            "Excavate to depth, dig out the scoured channel and any soft pocket, and replace it with structural fill compacted in lifts.",
            "Place and compact four inches of limerock in two lifts, probing after each.",
            "Set forms to a positive slope away from the garage, install fiber-reinforced 3,000 to 3,500 psi concrete with #4 edge bars, and cut joints at ten feet within twelve hours.",
            "Extend the downspouts past the new slab edge, because the cause of the failure is roof water and a new slab over the same drainage fails the same way.",
        ]), cls="alt")
    body += sec("What it costs on a typical BVL lot",
        f"""<p>The standard Landstar two-car drive in Buenaventura Lakes measures about 20 by 26 feet, roughly 520 square feet, sometimes with a short walk to the front door. Using the {R} Cost Index: removal of the old slab at $2.00 to $4.00 per square foot is $1,040 to $2,080, and the new four-inch broom-finish drive at {cost_range('concrete-driveway-broom')} is $4,420 to $7,020. A four-foot front walk of 40 feet adds roughly $1,400 to $2,100. Structural fill where we find a scoured channel is extra and is quoted after the slab comes up, which is the one line we cannot fix in advance.</p>
<p>Pavers on the same footprint run {cost_range('paver-driveway-concrete')}, so $7,280 to $11,440 plus the same removal. On a lot with a known drainage problem the repairability of pavers is worth weighing, and the comparison is in {compare('concrete-vs-pavers')}. Neither number is a quote; both come from the published index method at {guide('why-concrete-cracks-osceola', 'the rates we publish')} and on the {tool('concrete-paver-calculator')}.</p>""")
    body += sec("Permits and the association in BVL",
        f"""<p>Buenaventura Lakes is unincorporated Osceola County, not the City of Kissimmee, even though the mailing address says Kissimmee. That means the county driveway permit under §22-50.6 applies to a new or widened driveway, the 24-foot width cap applies, and the Building Office at 1 Courthouse Square reviews it in about three to five days. Replacing a driveway in the same footprint is still a driveway permit because the apron is in the right-of-way. The {tool('permit-finder')} confirms the jurisdiction for a specific address, and {juris('osceola-county')} quotes the rules.</p>
<p>Parts of BVL have active homeowner associations and parts do not, and the coverage is not obvious from the street. We ask at the site visit and check the plat; where an association exists, a driveway replacement in the same material rarely needs more than a notice, but a change to pavers or a widening does.</p>""")
    faqs = [
        faq("Why are all the driveways on my BVL street cracked the same way?", "Same builder, same decade, same slab on sand with no base; the garage step and the apron diagonal are what that does after forty summers."),
        faq("Do I need a permit in BVL?", "Yes, the Osceola County driveway permit; BVL is unincorporated."),
        faq("How long does the replacement take?", "Two to three days on site plus permit time; cars after 7 days."),
        faq("Is there an HOA?", "Most of BVL has none; a few later sections do."),
        faq("Is Buenaventura Lakes in the City of Kissimmee?", "No. BVL is unincorporated Osceola County with a Kissimmee mailing address, so the county driveway permit and the 24-foot width rule apply, not the city process."),
        faq("Can my BVL driveway be resurfaced instead?", "Only if the slab is stable. Most of the 1980s slabs we inspect there have stepped panels and voids, and an overlay over that fails within a season or two."),
        faq("Why does my driveway step up near the street?", "Usually live oak roots from the trees planted at build-out, sometimes the apron settling into a utility trench. We check both before quoting."),
    ]
    return page("buenaventura-lakes-driveway-replacement", "Replacing a 1980s Driveway in Buenaventura Lakes: What's Under It", "What a Buenaventura Lakes driveway replacement involves: what comes out of a Landstar-era slab (no base, washout, mesh on the bottom, roots), the county permit and 24-ft rule, the step-by-step, and costs for an 18x24 drive.", body, faqs, ["osceola-22-50-6", "sda"])


def cs_link():
    from _helpers import cs
    return cs("buenaventura-lakes", "concrete-repair", "BVL repair page")


def septic():
    body = sec("Septic drainfields and driveways on rural lots",
        cap("Rural lots in St. Cloud, Harmony, Narcoossee, Holopaw, Loughman and Polk City run on wells and septic, and the drainfield is usually in the front or side yard exactly where a longer driveway or a boat pad wants to go. Concrete over a drainfield compacts the soil, blocks the evaporation the field depends on, and can crush the laterals; Florida's onsite sewage rules keep driveways and structures off drainfields and set setbacks. We locate the tank and field from the county health department record before we lay out any rural pour."),
        eyebrow="Guide")
    body += sec("How we locate it", steps([
        "Pull the septic permit and as-built from the county record (Osceola or Polk environmental health); it shows the tank and drainfield location and the setbacks.",
        "Confirm on site: tank lid, cleanout, the greener rectangle in the lawn, a probe for the distribution box.",
        "Flag the field and the required setbacks; the driveway, pad or patio is routed clear.",
        "Where the only route crosses the field, the answer is a relocated or replaced drainfield by a licensed septic contractor first, and we say so.",
    ]))
    body += sec("What can and cannot go near a drainfield",
        table(["Element", "Over the drainfield", "Within the setback", "Beyond"], [
            ("Driveway or parking pad", "No", "No", "Yes"),
            ("Concrete patio or slab", "No", "No", "Yes"),
            ("Pavers on sand", "No (compaction and evaporation)", "Generally no", "Yes"),
            ("Turf or gravel path (light foot traffic)", "Foot traffic only", "Yes", "Yes"),
            ("Heavy equipment during construction", "No; a loaded mixer crushes laterals", "No", "Yes"),
            ("Trees with aggressive roots", "No", "No", "Yes"),
        ], caption="Setback distances are in Florida Administrative Code Chapter 64E-6 and on the county as-built; confirm the current rule with the health department."), cls="alt")
    body += sec("Truck access on rural lots", f"<p>A loaded ready-mix truck weighs 30 tons or more. It cannot cross a drainfield, a soft pasture in August, or a culvert built for a pickup, and it needs room to turn. On the site visit we walk the route from the road to the pour; when it fails, we price a pump truck or a concrete buggy rather than risk the field or the culvert. Long rural drives are then poured in sections from the road inward ({city('harmony')}, {city('polk-city')}, {svc('concrete-slabs')}).</p>")
    body += sec("Why concrete and drainfields do not mix",
        f"""<p>A septic drainfield works by letting effluent trickle into unsaturated soil where air, bacteria and evaporation finish the treatment. Three things a concrete slab does break that process. It compacts the soil above and around the laterals, reducing the pore space the system depends on. It seals the surface, cutting the evaporation that helps the field shed moisture in the wet season. And it puts weight and, worse, vehicle loads over shallow-buried pipe and gravel that was never designed to carry them.</p>
<p>The result is not immediate. A drainfield under a driveway typically keeps working for a while and then fails prematurely, and by then the fix involves breaking out the driveway to reach it. On rural St. Cloud, Harmony, Narcoossee and Kenansville lots, where systems are common and lots are large enough that the field often sits in the front yard, this is the single most expensive mistake we see planned.</p>""")
    body += sec("How we find the system before we quote",
        steps([
            "Pull the septic permit record for the parcel from the county health department file, which shows the tank and field layout as permitted.",
            "Walk the yard for the visible clues: the cleanout, the tank lids, a rectangle of greener or faster-growing grass, and the slight crown over a mounded field.",
            "Probe carefully with a soil probe along the expected lines to confirm depth and extent, without striking the laterals.",
            "Mark the tank, the field and a working setback around both on the site plan that goes into the proposal.",
            "Design the driveway, pad or patio to clear them, and put the marked plan in the file so the crew on pour day is working from the same drawing.",
        ]), cls="alt")
    body += sec("What to do when the only route crosses the field",
        table(["Option", "How it works", "Consider when", "Rough order of cost"], [
            ("Reroute the drive", "Move the alignment to clear the field, often with a curve or a turnaround relocated", "There is room on the lot", "Design change only"),
            ("Narrow to a ribbon drive", "Two concrete strips with turf between, reducing the sealed area over the field", "The field is wide and traffic is light", "Similar to a full slab of the same area"),
            ("Permeable pavers over a clean corridor", "Open-graded base and permeable joints let air and water through", "Crossing an edge of the field is unavoidable", "Higher than concrete; specified case by case"),
            ("Relocate the drainfield first", "A licensed septic contractor permits and builds a new field elsewhere on the lot", "There is no workable route", "A separate project, permitted through the health department"),
            ("Do not build it", "Keep the parking where it is", "The lot cannot take it", "Nothing, and sometimes correct"),
        ]))
    body += sec("Well heads, lines and the rest of a rural lot",
        f"""<p>The septic system is not the only thing buried on these lots. The potable well head and its supply line, the irrigation well and its lines, propane tanks and lines, and the electrical service to a barn or workshop all tend to be undocumented. We call 811 for the regulated utilities, but private lines on private property are outside that system, so we ask the owner, look for the obvious surface evidence, and probe.</p>
<p>Access is the other rural constraint. A loaded ready-mix truck runs over thirty tons and will not cross a soft pasture, a culvert built for a pickup or a bridge over a drainage ditch. On site visits east of St. Cloud we walk the route the truck would take, and where it does not work we price a pump truck or concrete buggies into the proposal instead of finding out on pour day ({svc('concrete-slabs')}).</p>""")
    faqs = [
        faq("Can I put a driveway over my drainfield?", "No. It compacts the soil, stops evaporation and can crush the pipes; the rules keep driveways off drainfields."),
        faq("How do you know where the drainfield is?", "From the county health department's septic permit and as-built, confirmed on site."),
        faq("What if the only route crosses it?", "Relocate the drainfield through a licensed septic contractor first; we route the driveway after."),
        faq("Can a mixer truck drive across my yard?", "Not across a drainfield or soft ground; we price a pump or buggy instead."),
        faq("Can pavers go over a drainfield?", "Standard sand-set pavers on a compacted limerock base have the same compaction and sealing problems as concrete. A permeable system over an open-graded base is the only paving we would consider near a field, and only at an edge."),
        faq("How do I find my drainfield?", "Start with the county health department permit file for the parcel, then confirm on the ground. We do both before designing."),
        faq("What if a previous owner already paved over it?", "It happens, and it usually surfaces when the system backs up. At that point a septic contractor evaluates whether the field can be rehabilitated or has to be relocated, and the paving comes out over the work area."),
    ]
    return page("septic-drainfield-concrete-driveway", "Septic Drainfields and Driveways on Rural Osceola Lots", "Why concrete, pavers and mixer trucks stay off septic drainfields on rural Osceola and Polk lots, how we locate the tank and field from the county record, setbacks, what can go where, and truck access on long driveways.", body, faqs, [])


def polymeric():
    body = sec("The other half of a paver job",
        cap("Polymeric sand is joint sand mixed with a polymer binder that hardens when it is misted, locking the pavers together and keeping ants, weeds and washout out of the joints. It works when it is installed dry, swept to just below the chamfer, vibrated in, blown clean off the surface and activated with a light mist, then left 24 hours without rain. It fails, as a crust on the surface or a white haze, when any of those steps is skipped, which is why half the new paver driveways in Osceola have ants by the second summer."),
        eyebrow="Guide")
    body += sec("How we install it", steps([
        "Pavers clean and dry; joints open to full depth (old sand vacuumed out on a re-sand).",
        "Sweep polymeric sand across the field diagonally until joints are full; work in shade if possible.",
        "Vibrate with a plate compactor on a protective pad to settle the sand; top off; repeat until the joint is filled to 1/8 inch below the chamfer.",
        "Blow every grain off the paver surface with a leaf blower; sand left on the surface hazes when wet.",
        "Mist in stages: light showers that wet the joint without flooding it, three passes, ten minutes apart; excess water floats polymer out.",
        "Twenty-four hours dry. Then seal, or wait 60 to 90 days on new pavers for efflorescence to clear.",
    ]), cls="alt")
    body += sec("Where it works and where it doesn't",
        table(["Situation", "Polymeric sand", "Alternative"], [
            ("Driveway, patio, pool deck with 1/8–1/2 in joints", "Yes; standard", "n/a"),
            ("Wide joints (over 1/2 in), large-format pavers", "Wide-joint formula", "Resin-bound jointing"),
            ("Joints that stay wet (shade, poor drainage)", "Fails; never hardens", "Fix drainage first"),
            ("Travertine, marble", "Fine-grade polymeric, or grout on thin-set", "Grout"),
            ("Porcelain on pedestals", "No", "Open joints"),
            ("Permeable pavers", "No; blocks the design", "Open-graded chip"),
            ("Rental decks pressure-washed weekly", "Yes, a joint-stabilizing sealer on top helps", "n/a"),
        ]))
    body += sec("The failures we fix", f"<p>White haze on the surface: sand not blown off before misting, or a film sealer over a damp joint ({compare('sealer-types')}). Crusted top with loose sand below: too little water, or the sand was installed thin. Washout in the first storm: misted too heavily, or rain within 24 hours. Ants and weeds: regular sand, or polymeric that never set. Each is fixed by cleaning the joints out and doing it again properly, usually with a seal on top ({svc('paver-sealing')}; rainy-season timing on the {tool('pour-calendar')}).</p>", cls="alt")
    body += sec("How it is installed, and where it goes wrong",
        steps([
            "The pavers are clean and the joints are empty to a depth of at least the paver thickness, or about an inch and a half minimum. Sweeping new sand onto old dirty sand is the most common failure.",
            "The surface and the joints are bone dry. Any moisture in the joint activates the polymer before the sand is in place, and it sets as a crust.",
            "Sand is swept diagonally across the joints and worked down, then topped up, because it always settles further than it first appears.",
            "A plate compactor with a protective pad vibrates the sand down into the joint and the pavers into the bedding course.",
            "The surface is blown clean with a leaf blower. Sand left on the paver face will haze and set there, and on a textured paver it never fully comes off.",
            "Water is applied in the sequence the manufacturer specifies, usually a shower rather than a jet, in stages, until the joint is saturated but not flooded. Over-watering washes the binder out and leaves weak joints.",
            "Nobody walks on it for the cure time on the bag, and no rain for the window on the bag. That last condition is why we watch the radar on sanding days the same way we do on pour days.",
        ]))
    body += sec("When we do not use it",
        table(["Situation", "Why polymeric sand is wrong", "What we use instead"], [
            ("Permeable paver systems", "The joints are the drainage path; a polymer binder defeats the whole design", "Open-graded chip per the system spec"),
            ("Joints narrower than about 1/16 in", "The sand cannot reach depth, so it crusts and pops out", "A fine joint stabilizer or nothing"),
            ("Joints wider than the product rating", "Typically over 1 to 1½ in depending on brand; the joint cracks and fails", "A wide-joint product rated for it, or a different pattern"),
            ("A deck that is already settling", "Locking the joints does not fix the base and makes lifting harder later", "Rebuild the base first, then sand"),
            ("Travertine and marble set on a sand bed with tight joints", "Polymer haze on calcareous stone is difficult to remove", "Stone-specific joint material and a stone sealer"),
        ], caption="Manufacturer joint-width ratings vary; we work to the spec sheet for the product we are installing."), cls="alt")
    body += sec("Ants, weeds and the real reason joints fail",
        f"""<p>Two complaints bring us back to a paver field more than any other: ant mounds pushing up between the pavers, and weeds sprouting in the joints. Both are symptoms of the same thing, which is loose or missing joint sand. Ants tunnel through unbound sand and deposit it on the surface; weed seed lands in the open joint, finds moisture and germinates. A properly installed, fully cured polymeric joint gives both far less to work with.</p>
<p>What it does not do is make the field permanent. Joint sand is consumed by pressure washing, by storm runoff crossing the field and by the gradual settlement that every sand-set surface has. Topping up joints every few years is normal maintenance, not a defect, and it is cheap compared with waiting until a corner has rolled because the edge lost its support. Our schedule for cleaning, re-sanding and sealing is on {svc('paver-sealing')}.</p>""")
    faqs = [
        faq("Polymeric sand or regular sand?", "Polymeric on any paver surface you want to keep clean; regular sand washes out and hosts ants and weeds."),
        faq("Why did my polymeric sand turn white?", "Sand left on the surface before misting, or too much water floating the polymer. Clean and redo."),
        faq("How long does polymeric sand last?", "Three to five years on a driveway with sealing; re-sand when joints drop below the chamfer."),
        faq("Can it be installed in the rainy season?", "On a dry morning with a dry night forecast; we reschedule rather than risk it."),
        faq("How often does polymeric sand need topping up?", "Every three to five years on a driveway in this climate, sooner if the field is pressure washed often or a downspout crosses it."),
        faq("Can polymeric sand be installed over old sand?", "No. The joints have to be cleaned out to depth first, which is most of the labour in a re-sanding visit."),
        faq("Why is there a white haze on my pavers after sanding?", "Either sand left on the paver face when the water went on, or the binder washed up out of the joint by over-watering. It can usually be removed with the manufacturer haze remover; prevention is a leaf blower and a controlled watering sequence."),
    ]
    return page("polymeric-sand-guide", "Polymeric Sand: When It Works, When It Fails, How We Install", "What polymeric sand is, the six-step installation that makes it hold on Central Florida pavers, where it does and does not belong, and the white haze, crusting, washout and ant failures we fix.", body, faqs, ["icpi"])


def curing():
    body = sec("Curing concrete in Central Florida heat",
        cap("Concrete reaches about 70 percent of its design strength at 7 days and its rated strength at 28, at normal temperatures with moisture present. Kissimmee's normal July high is 91.5 °F, which sets the surface fast but does not speed strength gain, and dries the surface before the interior has cured unless the slab is kept moist or sealed with a curing compound the day it is poured. So the calendar is the same in July as in January: walk in 24 to 48 hours, cars at 7 days, boats and trucks at 28."),
        eyebrow="Guide")
    body += sec("What happens by day",
        table(["Time", "What the concrete is doing", "What is allowed", "What we do"], [
            ("0–4 hours", "Placing, bleeding, initial set; surface can be finished", "Nothing on it", "Finish, joint, cure compound or wet cover"),
            ("4–12 hours", "Final set; shrinkage begins", "Nothing", "Saw-cut joints if tooled joints were not used"),
            ("24–48 hours", "About 30–40% strength", "Foot traffic", "Keep it moist or covered; forms off"),
            ("3 days", "About 50%", "Light furniture on a patio", "n/a"),
            ("7 days", "About 70%", "Cars on a driveway", "n/a"),
            ("28 days", "Rated strength", "Boats, RVs, trucks; sealing stamped concrete", "Seal if specified"),
        ], caption="Approximate percentages for a standard mix at normal temperatures; the proposal states the mix."), cls="alt")
    body += sec("Hot-weather rules", "<ul><li>Pour at first light; the truck's mix temperature matters and so does the sun on the forms.</li><li>Retarder in the mix in summer; no water added on site, which weakens the surface.</li><li>Finish on schedule, not on the bleed water: floating water back in causes scaling.</li><li>Cure the same day: curing compound sprayed after finishing, or wet burlap and plastic; a bare slab in a July afternoon loses its surface water in an hour.</li><li>Joints within 12 hours; shrinkage starts early in heat.</li><li>Keep it moist for 3 days if you can; an afternoon storm on a covered slab is a gift.</li></ul>")
    body += sec("Cool-weather notes", "<p>Osceola winters are mild (December normal low 51.5 °F) and rarely cold enough to matter, but a cold front the night after a pour slows the set; we watch for it and hold finishing. Overlays and coatings are the products most sensitive to temperature swings.</p>", cls="alt")
    body += sec("Why sealing waits", f"<p>Concrete keeps releasing moisture for weeks. A film sealer applied at day 3 traps it and turns white; stamped concrete is sealed at 28 days on a dry slab; broom concrete can take a penetrating sealer sooner but there is no hurry. Pavers wait 60 to 90 days for efflorescence for the same reason ({compare('sealer-types')}, {guide('rainy-season-concrete-scheduling')}).</p>")
    body += sec("What the slab is doing in the first 28 days",
        table(["Time after the pour", "Approximate share of 28-day strength", "What it means for you", "What we are doing"], [
            ("6 to 12 hours", "Set, almost no strength", "Stay off it", "Tooling or saw-cutting the control joints"),
            ("24 hours", "Roughly a sixth", "Light foot traffic at the edge", "Curing compound or wet cover maintained"),
            ("3 days", "About 40 percent", "Foot traffic, light furniture", "Forms stripped, edges dressed"),
            ("7 days", "About 65 to 70 percent", "Passenger cars", "Cure period normally ends; sealing decisions start"),
            ("14 days", "Around 85 percent", "Normal use", "Nothing"),
            ("28 days", "100 percent of design strength", "Boats, RVs, moving trucks, hot tubs", "Sealing on stamped and decorative work"),
        ], caption="Approximate strength gain for a normal Portland cement mix under Florida conditions. The mix design and the weather shift the curve; the calendar rules on the proposal are set conservatively."), cls="alt")
    body += sec("Curing methods and what we use when",
        f"""<p>Curing means keeping water in the concrete long enough for the cement to hydrate. There are three practical ways to do that on flatwork, and in a Kissimmee July all three are working against 91.5 degree afternoons and a breeze that pulls moisture off the surface faster than it bleeds up.</p>
<p>A liquid membrane-forming curing compound sprayed on as soon as the surface can take it is our default on driveways, because it is reliable and does not depend on someone returning to wet the slab. Wet curing with burlap or a cover kept damp gives the best result and is what we use on high-value decorative work where colour uniformity matters. Plastic sheeting is the third option and the one with a catch: laid directly on a fresh slab it mottles the surface, so it goes on supports, and on coloured or stamped work we avoid it entirely. On stamped concrete the curing compound also has to be compatible with the sealer that follows, which is a detail that ruins finishes when it is missed.</p>""")
    body += sec("Hot-weather practices we apply from May to September",
        f"""<p>Industry hot-weather concreting guidance targets the same problems we see here: the mix arriving too warm, the surface drying before the concrete bleeds, and the set arriving before the crew is ready to finish. Our working rules are to schedule the first truck at daylight, to order a retarding admixture in the mix from May through September, to dampen the base before placement so it does not draw water out of the bottom of the slab, to shade or fog the surface when the breeze is strong, and to never add water at the truck to make placement easier, which is the single most common cause of a weak, dusty surface.</p>
<p>The other half is the calendar. The Kissimmee 2 NOAA station's normals put the July high at 91.5 degrees with 16.7 rain days, and August at 91.4 degrees with 17.7. Those are the months where a pour that starts at seven finishes clean and a pour that starts at ten does not. The month-by-month view is on the {tool('pour-calendar')}, and what we do when a storm arrives mid-pour is in {guide('rainy-season-concrete-scheduling')}.</p>""")
    faqs = [
        faq("How long before I can drive on new concrete?", "Seven days for cars, 28 for heavy vehicles, in any month."),
        faq("Does concrete cure faster in Florida heat?", "It sets faster; it does not gain strength faster, and it dries out before it cures unless it is kept moist or sealed with a curing compound."),
        faq("Should I water new concrete?", "Keeping it moist for the first three days helps; a covered slab needs less. Do not flood it in the first hours."),
        faq("When can stamped concrete be sealed?", "At 28 days on a dry slab."),
        faq("Should I water my new driveway?", "If we left you with wet curing, yes, on the schedule we give you. If we applied a curing compound, no; the membrane is doing the work and watering over it achieves nothing."),
        faq("Why is my new slab a different colour in patches?", "Usually uneven curing or plastic sheeting touching the surface, sometimes a difference between trucks. Most of it evens out over the first year."),
        faq("Can I park on it after 7 days in winter?", "Yes. Cooler weather slows early strength gain slightly but the seven-day rule already has margin for it. The 28-day rule for heavy loads does not change."),
    ]
    return page("concrete-curing-florida-heat", "Curing Concrete in Central Florida Heat: 7 vs. 28 Days", "How concrete gains strength by the day, why Kissimmee's 91-degree summers set the surface fast without speeding the cure, hot-weather pour rules, when cars and trucks can use it, and why sealing waits.", body, faqs, ["noaa"])


def surface_temp():
    body = sec("How hot does a pool deck get? What is published, and what we plan to measure",
        cap("Published measurements from Florida installers and manufacturers put light travertine at roughly 105 to 120 °F at midday on a 95-degree day, light concrete pavers 10 to 20 degrees warmer, gray broom concrete around 120 to 135, and dark concrete pavers or dark porcelain 130 to 145. Skin discomfort starts around 120 °F and burns become possible above 140 with sustained contact. We cite those figures rather than our own because we have not yet measured decks here; the measurement is planned for July and this page will change when it is done."),
        eyebrow="Guide")
    body += sec("Published figures, with the caveats",
        table(["Surface", "Published midday range", "Notes"], [
            ("Travertine, light, tumbled", "105–120 °F", "Multiple installer comparisons in South and Central Florida; 'walkable but warm'"),
            ("Marble, light", "At or below travertine", "Installer reports; lightest color"),
            ("Concrete pavers, light (sand, ivory)", "115–130 °F", "Color drives it more than material"),
            ("Broom concrete, gray", "120–135 °F", "Installer measurements"),
            ("Textured coating, light", "Cooler than bare gray concrete", "Manufacturer claims; magnitude varies"),
            ("Concrete pavers, dark (charcoal)", "130–145 °F", "Installer measurements"),
            ("Porcelain, dark", "Similar to dark pavers", "Non-porous, stores heat"),
            ("Artificial turf", "Above pavers", "Manufacturer guidance; cooling infill helps"),
        ], caption="Sources are installer blogs and manufacturer pages found in September 2026; none publishes instrument, time and sky condition consistently, which is why these are ranges and why we intend to measure."), cls="alt")
    body += sec("How we will measure", "<ol><li>One deck with six samples set side by side on the same base: light travertine, marble, light concrete paver, dark concrete paver, light porcelain, broom concrete (plus a coated sample if available).</li><li>Infrared thermometer with a stated emissivity setting, checked against a contact probe.</li><li>Readings at 10 a.m., noon, 2 p.m. and 4 p.m. on a clear day in July, air temperature and cloud cover logged from the Kissimmee 2 station and on site.</li><li>Three readings per sample per time, averaged.</li><li>Published here with date, instrument, method and raw numbers; the cited figures above will then be replaced.</li></ol>")
    body += sec("What to do with it", f"<p>If the deck is for barefoot summer use, color and material both matter and light stone wins; if it is a rental, sealed light pavers with grit are the practical middle; a coating is the budget fix on a sound deck. Comparisons: {compare('travertine-vs-concrete-pavers')}, {compare('cool-deck-vs-pavers')}; decision tool: {tool('concrete-vs-pavers')}.</p>", cls="alt")
    body += sec("What the published figures actually say",
        table(["Surface", "Reported midday surface temperature", "Source type", "How to read it"], [
            ("Standard grey concrete paver", "About 130 to 145 °F", "Installer and manufacturer comparisons", "Widely quoted range; test conditions rarely stated"),
            ("Light or tan concrete paver", "About 120 to 135 °F", "Same", "Colour is doing most of the work"),
            ("Poured grey concrete, broom finish", "About 125 to 140 °F", "Same", "Similar to a grey paver of the same shade"),
            ("Travertine, light tumbled", "About 105 to 120 °F", "Same", "The coolest common deck material in these comparisons"),
            ("Marble", "Similar to or cooler than travertine", "Same", "Light colour plus density"),
            ("Dark porcelain or charcoal paver", "Highest of the group", "Same", "Avoid on a barefoot deck regardless of material"),
        ], caption="Figures collected from installer and manufacturer comparisons in September 2026 and reproduced here as published. None of them states instrument, time of day, air temperature or sky condition, which is why we treat them as indicative rather than measured."), cls="alt")
    body += sec("The measurement we intend to publish",
        f"""<p>We are not comfortable citing other people's numbers indefinitely, so here is the protocol we plan to run next July and publish in full, including the raw readings. Six sample panels of about four square feet each, laid on the same deck with the same exposure: light travertine, marble, a light concrete paver, a standard grey concrete paver, a broom-finished poured concrete section and a dark large-format porcelain paver. Readings with a calibrated infrared thermometer at a fixed distance and emissivity setting, taken hourly from 10 a.m. to 4 p.m. on a clear day, with air temperature, relative humidity, wind and cloud cover recorded at each reading, plus a shaded control for each material.</p>
<p>Until that exists, the honest position is the one at the top of this page: the ranking is consistent across every published comparison we have read, light stone is cooler than light concrete which is cooler than dark anything, and the size of the gap varies more than the order does. The method will go on {guide('surface-temperature-pool-decks', 'this page')} and in our <a href="/data-and-methods/">data and methods</a> notes when the readings are taken.</p>""")
    body += sec("What actually reduces deck heat",
        f"""<p>Colour first. A light surface reflects more of the solar load, and that single choice moves the number more than the material does. Second, shade, whether from a screen enclosure, a pergola over the lounge area or the mature oaks that some Kissimmee lots already have. Third, texture and porosity: a tumbled travertine surface with open pores feels cooler underfoot than a dense sealed slab at the same measured temperature, partly because of the contact area and partly because water evaporating from the pores cools it. Fourth, wetting, which is why the traditional Florida move of hosing the deck before the kids come out works.</p>
<p>What does not help much: a coating sold as cool decking on a dark colour, a sealer marketed as heat-reducing on top of a hot substrate, or a paver marketed as cool in a charcoal finish. If a barefoot deck is the goal, choose the light material and then choose the shade. The material comparison with cost is in {compare('travertine-vs-concrete-pavers')}, and the coated-concrete option is in {compare('cool-deck-vs-pavers')}.</p>""")
    faqs = [
        faq("Which pool deck material stays coolest?", "Light marble and travertine in published comparisons, then light concrete pavers, then coatings, then gray concrete, with dark pavers and dark porcelain hottest."),
        faq("Does travertine get too hot to walk on?", "Warm, not scorching: published figures put it around 105 to 120 °F at midday."),
        faq("Do you have your own measurements?", "Not yet; a side-by-side test is planned for July with the method above, and this page will be updated."),
        faq("Does color matter more than material?", "Within concrete pavers, yes; between stone and concrete, both matter."),
        faq("Is travertine really cooler than pavers?", "Every published comparison we have read puts light travertine below standard grey concrete pavers, usually by 15 to 30 degrees at midday. We have not measured it ourselves yet and we say so."),
        faq("Does a cool-deck coating work?", "A light-coloured textured coating is cooler than dark bare concrete, yes. The colour is doing most of it; a dark cool-deck coating is not cool."),
        faq("What is the cheapest way to make a hot deck usable?", "Shade over the part people sit on, and a light-coloured surface where they walk. Both beat any product claim."),
    ]
    return page("surface-temperature-pool-decks", "How Hot Does a Pool Deck Get? Surface Temperatures by Material", "Published midday surface temperatures for travertine, marble, light and dark concrete pavers, coatings, broom concrete and porcelain on Florida pool decks, with caveats, and the July side-by-side measurement we plan to publish.", body, faqs, [])


def hb803():
    body = sec("Florida's $7,500 building-permit exemption and small concrete jobs",
        cap("CS/CS/HB 803, signed May 6, 2026 and effective July 1, 2026, exempts an owner of a single-family dwelling (and the owner's contractor) from obtaining a building permit for work on that property valued under $7,500, after a written request for exemption to the local government, and excludes structural, electrical, plumbing, mechanical and gas work and property in a flood hazard area. It also bars homeowners' associations from requiring a building permit as a precondition of architectural review."),
        eyebrow="Guide")
    body += sec("What it changes for driveways, patios and pads",
        table(["Project", "Before July 1, 2026", "After", "Why"], [
            ("Detached backyard patio slab under $7,500 in St. Cloud or Orange County", "Building permit required", "Exempt with a written request", "Flatwork under the threshold, no excluded system"),
            ("Shed pad, AC pad, generator pad", "Varied by office", "Pad exempt; the generator's electrical/gas still permitted", "Excluded systems keep their permits"),
            ("Driveway, new or widened", "Driveway permit", "Driveway permit still required", "Right-of-way and driveway permits are not building permits; §22-50.6 is a traffic-code rule"),
            ("Pool deck tied to the screen enclosure", "Permit", "Permit", "Structural tie"),
            ("Any work in a FEMA special flood hazard area", "Permit", "Permit", "Excluded"),
            ("Work over $7,500", "Permit", "Permit", "Threshold"),
        ]), cls="alt")
    body += sec("How the exemption is requested", f"<p>The law keeps a written request for exemption, submitted to the building department, which then confirms the work qualifies; St. Cloud has published its adoption and the exclusions. We prepare the request where a job qualifies and put the answer in the proposal, and we still schedule the inspection-free work to the same spec, because the exemption removes the permit, not the code. Jurisdiction pages: {juris('city-of-st-cloud')}, {juris('osceola-county')}, {juris('city-of-kissimmee')}, {juris('polk-county')}, {juris('orange-county')}.</p>")
    body += sec("The HOA clause", f"<p>Associations used to ask for the building permit before they would review an application; the law now prohibits that precondition. The ARC still reviews the work itself, with the packet it always asked for ({tool('hoa-packet-checklist')}, <a href=\"/hoa/\">HOA hub</a>).</p>", cls="alt")
    body += sec("What the exemption covers and what it does not",
        table(["Work", "Covered by the $7,500 exemption?", "Why"], [
            ("Stand-alone concrete pad or patio under $7,500, outside a flood hazard area", "Generally yes, with the written request", "No structural, electrical, plumbing, mechanical or gas component"),
            ("Driveway or apron in the public right-of-way", "No", "A driveway permit is a right-of-way approval, not a building permit"),
            ("Slab supporting a structure, a screen room or a roof", "No", "Structural"),
            ("Any work in a FEMA special flood hazard area", "No", "Explicitly excluded by the bill"),
            ("Electrical for outdoor lighting, gas to a summer kitchen", "No", "Excluded trades, and they need a licensed contractor"),
            ("Pool deck tied into the pool structure", "No", "Structural connection"),
            ("Resurfacing, sealing or a repair in the same footprint", "Not needed", "Maintenance was never a permitted activity here"),
        ], caption="Read against the bill as passed and effective 2026-07-01; local implementation is still settling, which is why we confirm with the office for every job."), cls="alt")
    body += sec("How the written request works in practice",
        f"""<p>This is not an automatic exemption. The bill contemplates the owner or the contractor submitting a written request for exemption to the local building official, identifying the work and its value, before the work starts. Jurisdictions are building their own forms and processes for it, and in the first months after the effective date the answer you get depends partly on who picks up the phone. Some offices want the request on their own form with a scope description and a value; others are still asking for a permit application and waiving fees.</p>
<p>Our practice is straightforward. Where the job plainly qualifies and the office has a process, we file the request and give you the response in writing with the proposal. Where the office is not ready or the job is near the threshold, we pull a permit, because a permit costs a few hundred dollars and an unpermitted slab that turns up in a title search costs far more. The value threshold is the whole job value, not the materials, and splitting one project into two invoices to stay under it is exactly the kind of thing a building official will recognise.</p>""")
    body += sec("The part that matters to anyone in an association",
        f"""<p>The same bill addresses a long-standing tangle between associations and building departments by barring a homeowners association from requiring an applicant to produce a building permit before the association will review an architectural application. That ordering problem was real: the association would not approve until the county issued, and the county would not issue until the association approved.</p>
<p>What it does not do is remove the association's authority. Architectural review still applies, the board can still require a survey, a product sample, a drainage note and the installer's insurance certificate, and the deed restrictions still bind. So the sequence for a paver driveway in Poinciana, Celebration or a Four Corners resort community is unchanged in substance: assemble the packet, get architectural approval, then permit or file the exemption request. The {tool('hoa-packet-checklist')} covers the first step and {hoa('poinciana-apv')} shows how specific one board's criteria are.</p>""")
    faqs = [
        faq("Does HB 803 mean I don't need a permit for a driveway?", "No. Driveway permits are right-of-way and traffic-code rules, not building permits; Osceola's §22-50.6 still applies."),
        faq("Does a patio under $7,500 need a permit now?", "Generally not, with a written exemption request, unless it is attached, roofed, in a flood zone or tied to a structure."),
        faq("Can my HOA still require a permit before reviewing?", "No; the law bars that precondition."),
        faq("Does the exemption lower the spec?", "No; the code still applies. We build to the same spec with or without a permit."),
        faq("Does the exemption mean I can skip inspections?", "It means no building permit and therefore no building inspections for qualifying work. It does not waive the code; the work still has to comply, and you still carry the consequences if it does not."),
        faq("Can a driveway be split into two jobs to stay under $7,500?", "No. The threshold is the value of the work, and a building official will treat a split project as one project. A driveway touching the right-of-way needs its driveway permit regardless of value."),
        faq("Who files the written request?", "Either the owner or the contractor, before work starts. We file it and give you the response with the proposal when the job qualifies and the office has a process for it."),
    ]
    return page("hb-803-permit-exemption", "HB 803: Florida's $7,500 Permit Exemption and Concrete Jobs", "What Florida's HB 803 (effective July 1, 2026) changes for patios, pads and driveways under $7,500: the written request, the exclusions (structural, electrical, plumbing, gas, flood zones), why driveway permits remain, and the HOA clause.", body, faqs, ["hb803", "stcloud-permits", "osceola-22-50-6"])


def get_pages():
    return [index(), cracks(), rust(), widening(), rainy(), verify(), str_guide(), roots(), base_guide(), bvl_guide(), septic(), polymeric(), curing(), surface_temp(), hb803()]
