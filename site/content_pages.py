# -*- coding: utf-8 -*-
"""About, editorial standards, data & methods, warranty, contact, gallery, legal, 404, thank-you."""
from _data import BUSINESS, EMAIL, PUBLIC_NAME, COST_INDEX_RELEASE, SERVICES, CITIES, TIER1, TOOLS, GUIDES, COMPARISONS, src
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, lead_form, faq, callout, related, esc
from _photos import PHOTOS, figure_html


def about():
    body = f'''
<section class="tight"><div class="wrap">
<p class="lede">Kissimmee Concrete is the Osceola County and Polk ridge service brand of a Central Florida concrete and paver contractor. The crews, trucks and estimators are the same ones behind our sister brands in West Orange and South Lake counties; this site exists because the permits, soils, HOAs and prices in Osceola and northern Polk are different enough to deserve their own pages.</p>
</div></section>'''
    body += sec("What we do and don't do",
        f"""<p>We install and repair poured concrete flatwork (driveways, patios, pool decks, slabs, walkways, small commercial pads), pavers and natural stone (driveways, pool decks, patios, walkways, steps, sealing and repair), decorative segmental retaining walls and seat walls, artificial turf and low-voltage lighting tied into the hardscape, and epoxy or polyaspartic garage floor coatings. We do not build foundations, footings, structural retaining walls or pool shells; those belong to other trades, and we will tell you so and step aside rather than take work that is outside what we do.</p>
<p>What you get from us in writing, on every job, is the legal entity name, the insurance certificate and the workmanship warranty. How to check those three things on any contractor you are considering is in {guide('how-to-verify-a-concrete-contractor-florida')}.</p>""")
    body += sec("How we work",
        f"""<ul>
<li><strong>Free on-site estimate, written proposal.</strong> We measure, probe the ground, check the soil map unit, photograph access and note HOA and permit requirements. The proposal lists thickness, PSI, reinforcement, base depth, joint layout and drainage so it can be compared line by line.</li>
<li><strong>Permits pulled by us.</strong> City of Kissimmee, City of St. Cloud, Osceola County or Polk County, whichever your address falls in. You sign the application and, where required, the Notice of Commencement.</li>
<li><strong>HOA packet prepared by us.</strong> Survey or site plan markup, product and color sample, pattern, drainage note, insurance certificate naming the association when the board asks for it.</li>
<li><strong>Weather planned around.</strong> Rainy-season pours start at first light and finish before the afternoon storms; the {tool('pour-calendar')} shows the numbers.</li>
<li><strong>Warranty in writing.</strong> Workmanship warranty terms are in the contract and summarized on the <a href="/warranty/">warranty page</a>.</li>
</ul>""", cls="alt")
    body += sec("Who writes this site",
        f"""<p>The estimators and crew leads who price and build the work write the pages, with an editor who checks every number against its source. We cite primary sources (county code, city permit pages, Florida Statutes, NOAA, USDA, manufacturers, the Florida Building Code) and we date every page. Where we don't know something, such as a community's written ARC criteria we haven't obtained, the page says so instead of guessing. Our <a href="/editorial-standards/">editorial standards</a> and <a href="/data-and-methods/">data and methods</a> pages explain the rules.</p>
<p>Photos on this site are job photos from our crews around Central Florida unless marked "concept rendering"; we do not claim a photo was taken in a particular city unless it was. We do not publish reviews, ratings, years in business or project counts we cannot document. When the Google Business Profile for Kissimmee Concrete is live and has reviews, they will appear here with a link to the profile.</p>""")
    body += sec("Contact",
        f"<p>Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> or use the <a href=\"/contact/\">estimate form</a>. Hours: {esc(BUSINESS['hours'])}. Service area: {esc(BUSINESS['service_area_short'])}; see the <a href=\"/areas/\">area map</a>.</p>", cls="alt")
    return {"route": "/about/", "title": "About Kissimmee Concrete – Who We Are and How We Work", "meta_description": "Kissimmee Concrete is the Osceola County and Polk ridge service brand of a Central Florida concrete and paver contractor. What we install, what we don't, and what we put in writing.", "h1": "About Kissimmee Concrete", "breadcrumbs": [("Home", "/"), ("About", None)], "body_html": body, "kind": "page", "sources": []}


def editorial():
    body = sec("Rules every page on this site follows",
        f"""<ol>
<li><strong>Primary sources or nothing.</strong> Permit rules come from the city or county page or code section, quoted and linked. Climate numbers come from NOAA normals for the Kissimmee 2 station. Soils come from USDA Soil Data Access for Osceola (FL097) and Polk (FL105). Statutes come from the Florida Legislature's site. Manufacturer specs come from the manufacturer.</li>
<li><strong>Dates on everything.</strong> Every page shows its publication date and its last review date, plus a one-line note of what changed. Cost ranges carry the Cost Index release label ({COST_INDEX_RELEASE['label']}) and its date.</li>
<li><strong>No invented proof.</strong> No reviews, star ratings, "years in business", project counts, awards or team bios that we cannot document. When those exist, they will link to their source.</li>
<li><strong>Photos labelled.</strong> Job photos are from our crews in Central Florida and are not asserted to be in a specific city. AI concept renderings are marked "concept rendering" in the badge, the caption and the alt text.</li>
<li><strong>Ranges, not quotes.</strong> Every price on this site is a planning range with a published method. Your price is in your written proposal after a site visit.</li>
<li><strong>Say what we don't know.</strong> If we have not read a community's architectural criteria, the page says "not verified" and gives the management contact instead of a guess.</li>
<li><strong>One answer per question.</strong> Each question homeowners ask has one canonical page on this site; other pages link to it rather than repeating it.</li>
<li><strong>Written for people who live here.</strong> Plain language, contractions, real neighborhoods, no filler. Every 150 words or so should contain a fact you could check.</li>
<li><strong>Corrections.</strong> Email {EMAIL} with the page URL and the error. We correct within two business days and log the change in the page's update note.</li>
</ol>""")
    body += sec("What we will not do", "<ul><li>Copy text, tables, tools, photos or layouts from other contractors' sites.</li><li>Create pages for cities we don't serve or swap a city name into a template.</li><li>Use stock photos as if they were our work.</li><li>Claim a credential, an award or a rating we cannot show you.</li><li>Sell or share your contact details.</li></ul>", cls="alt")
    return {"route": "/editorial-standards/", "title": "Editorial Standards – How We Write and Check Pages", "meta_description": "Primary sources only, dates on every page, no invented reviews or stats, labelled photos, ranges not quotes, and a correction policy. How this site is written and checked.", "h1": "Editorial standards", "breadcrumbs": [("Home", "/"), ("Editorial standards", None)], "body_html": body, "kind": "page"}


def data_methods():
    body = sec("Kissimmee Concrete Cost Index",
        cap(f"Release {COST_INDEX_RELEASE['label']} ({COST_INDEX_RELEASE['date']}) is a market composite. Each of the 18 items is an installed range per unit for the Kissimmee and Osceola County market, built from three inputs: supplier price lists (ready-mix $175–$280 per cubic yard delivered in the Orlando market, September 2026), published regional ranges from national cost references, and our own labor and material takeoffs for standard job sizes. It is not yet a sample of executed contracts.")
        + f"""<p><strong>What goes into each range.</strong> Material at current supplier pricing, base and haul-off, labor for a typical crew day, permit and disposal fees, and a minimum-charge floor for small jobs. Low end assumes straightforward access, sound subgrade and standard finishes; high end assumes tear-out of an old slab, tight access, borders and bands, or premium material. Anything outside those assumptions (structural fill, tree roots, drainage work, engineered walls) is priced separately and is not in the index.</p>
<p><strong>What the index does not do.</strong> It does not price your job. It does not include sales tax on materials where applicable, financing charges or HOA fees. It does not reflect the busiest weeks of spring when crew availability tightens.</p>
<p><strong>How it will change.</strong> From the next release, anonymized executed quotes (service, city, square footage, price, date) will be added to the sample and the release note will state the count per item. Items with fewer than five quotes will stay market-composite and be labelled as such. Releases are quarterly ({COST_INDEX_RELEASE['next']} is next). Machine-readable copies: <a href="/api/cost-index.json">JSON</a>, <a href="/api/cost-index.csv">CSV</a>, license CC BY 4.0 with attribution to Kissimmee Concrete and a link to this page.</p>""")
    body += sec("Climate data behind the Pour Calendar", "<p>Monthly normals for maximum and minimum temperature, precipitation and number of days with precipitation at or above 0.01 and 0.10 inch come from NOAA NCEI U.S. Climate Normals 1991–2020, station USC00084625 (Kissimmee 2, FL, 28.2764 N, 81.4239 W), downloaded September 10, 2026. Orlando International (USW00012815) is kept as a comparison series. The 'pour window' recommendation is our rule of thumb: months with 12 or more days of 0.10 inch or more are treated as storm-season months where pours start at daylight and finish before 2 p.m.</p>", cls="alt")
    body += sec("Soils", "<p>Map-unit acreage, drainage class and wet-season water-table depth come from USDA NRCS Soil Data Access queries for survey areas FL097 (Osceola County) and FL105 (Polk County), run September 10, 2026. 'Typical water table about 12 inches' is the minimum depth reported for Smyrna, Myakka, Immokalee and EauGallie fine sands in the wet months; Basinger is 6 inches and depressional Basinger and Placid are at the surface. A specific lot can differ from its map unit; we probe on site.</p>")
    body += sec("Jurisdiction finder", "<p>City and county boundaries are the U.S. Census Bureau's 2024 TIGERweb polygons, simplified to about 0.0006 degrees (roughly 200 feet) to keep the file small. Addresses are geocoded by the Census Bureau's public geocoder in your browser; nothing you type is sent to us. A result within a few hundred feet of a city line should be confirmed with the county's property appraiser or the city.</p>", cls="alt")
    body += sec("Distances and populations", "<p>Distances are straight-line from downtown Kissimmee (28.2920, −81.4076) to the Census internal point of each place (2024 Gazetteer). Drive times are an estimate (distance × 1.3 ÷ 32 mph) rounded to five minutes. Populations are Florida EDR 2025 adjusted estimates for incorporated cities; Census-designated places and unincorporated communities have no municipal figure and are labelled accordingly.</p>")
    body += sec("Surface temperature table", "<p>The pool-deck temperature comparison currently cites published measurements from installers and manufacturers and labels them as such. Our own measurements (infrared thermometer, 2 p.m., clear July day, six materials side by side on the same deck) are planned for the next summer and will replace the cited figures with method, date and instrument noted.</p>", cls="alt")
    body += sec("Demand and questions", "<p>The questions this site answers come from Google and Bing autocomplete (collected September 10, 2026), Google Trends for the Orlando DMA (five-year seasonality and related queries), the Google Ads Keyword Planner export for Florida markets (August 2025–July 2026), competitor FAQ gaps and the questions our estimators hear. Each question is assigned to one canonical page.</p>")
    return {"route": "/data-and-methods/", "title": "Data & Methods – Cost Index, Climate, Soils and Finder Sources", "meta_description": "How the Kissimmee Concrete Cost Index is built, where the NOAA climate and USDA soil numbers come from, how the jurisdiction finder works, and what each dataset does not do.", "h1": "Data and methods", "breadcrumbs": [("Home", "/"), ("Data & methods", None)], "body_html": body, "kind": "page", "sources": ["noaa", "sda", "tigerweb", "gazetteer", "edr"]}


def warranty():
    body = sec("What the workmanship warranty covers",
        cap("Every job comes with a written workmanship warranty in the contract. It covers defects in our installation: settling caused by inadequate base compaction, edge restraint failure, joints that were not cut or tooled, finishing defects, and pavers that were set out of level or pattern. It does not cover damage from tree roots, vehicles heavier than the slab was specified for, utility repairs, ground movement from broken irrigation or drainage you were advised to fix, or normal hairline shrinkage cracks and color variation.")
        + f"""<p><strong>How a claim works.</strong> Email {EMAIL} with your address and photos. We come out, look, and either fix it under warranty or explain in writing why it falls outside. Most paver warranty work is a lift-and-relay of the affected area; most concrete warranty work is joint or edge repair.</p>
<p><strong>Materials.</strong> Manufacturer warranties on pavers, sealers and coatings pass through to you; we register them where the manufacturer allows. Concrete itself is not warranted against hairline cracks by anyone, which is why our proposals specify joints and base rather than promising a crack-free slab.</p>
<p><strong>Term and transfer.</strong> The term and transfer conditions are stated in your contract. Keep the contract and the permit number; a buyer's inspector will ask for both.</p>""")
    return {"route": "/warranty/", "title": "Workmanship Warranty – What Is Covered and How Claims Work", "meta_description": "What Kissimmee Concrete's written workmanship warranty covers on concrete and paver work, what it excludes, how to make a claim, and how manufacturer warranties pass through.", "h1": "Workmanship warranty", "breadcrumbs": [("Home", "/"), ("Warranty", None)], "body_html": body, "kind": "page"}


def contact():
    body = f'''
<section class="tight"><div class="wrap">
<div class="grid grid-2">
<div>
<p class="lede">Send the form with a photo and rough dimensions and we'll reply during business hours ({esc(BUSINESS['hours'])}) to set up a site visit. Estimates are free and come as a written proposal.</p>
<h2 style="font-size:1.2rem">Other ways to reach us</h2>
<ul><li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Service area: {esc(BUSINESS['service_area_short'])}</li><li>Prefer to gather the facts first? Use the <a href="/tools/project-brief/">project brief tool</a> and paste the result into the notes.</li></ul>
<h2 style="font-size:1.2rem">What happens next</h2>
<ol><li>We call or text to confirm the address and a visit window (two business days in Osceola, three on the Polk ridge).</li><li>On site we measure, probe the ground and photograph access.</li><li>You get a written proposal with specs, price and schedule, usually within two business days of the visit.</li></ol>
<p class="note">Sending a form does not create a contract. We only share your information with the crew that will do your work.</p>
</div>
<div>{lead_form(heading="Request a free on-site estimate")}</div>
</div>
</div></section>'''
    return {"route": "/contact/", "title": "Contact Kissimmee Concrete – Free On-Site Estimate", "meta_description": "Request a free on-site estimate for concrete or paver work in Kissimmee, St. Cloud, Osceola County or the Polk ridge. Attach a photo, pick your city and service, and we reply in business hours.", "h1": "Request a free estimate", "breadcrumbs": [("Home", "/"), ("Contact", None)], "body_html": body, "kind": "page", "no_cta": True}


def gallery():
    real = [p for p in PHOTOS if p["kind"] == "real"]
    rend = [p for p in PHOTOS if p["kind"] == "rendering"]
    body = sec("Job photos", "<p class=\"lede\">Photos from our crews across Central Florida: paver driveways with charcoal banding, marble and travertine-look pool decks inside screened lanais, a raised terrace with a stone wall and cedar pergola, porcelain-capped entry steps, and a driveway mid-installation with the base and bedding sand visible. None of these is asserted to be in a specific city.</p><div class=\"gallery\">" + "".join(figure_html(p) for p in real) + "</div>")
    body += sec("Concept renderings", "<p class=\"lede\">These are AI-generated concept images we use to show a finish, pattern or layout when we have no photo of that exact combination. They are labelled here, in the badge and in the alt text so nobody mistakes them for finished work.</p><div class=\"gallery\">" + "".join(figure_html(p) for p in rend) + "</div>", cls="alt")
    return {"route": "/gallery/", "title": "Gallery – Real Job Photos and Labelled Concept Renderings", "meta_description": "Paver driveways, marble and travertine pool decks, terraces, entry steps and installation-in-progress photos from our Central Florida crews, with AI concept renderings clearly labelled.", "h1": "Photo gallery", "breadcrumbs": [("Home", "/"), ("Gallery", None)], "body_html": body, "kind": "page"}


def privacy():
    body = sec("What we collect", f"<p>When you send the estimate form we receive the name, phone, email, city, service, property type, timeline, notes, preferred language and optional photo you enter, plus the page you sent it from, the referring site, any campaign tags in the URL (utm_*, gclid), a timestamp and the country of your connection. Cloudflare Turnstile checks that the sender is a person; it may set a cookie for that purpose. We do not collect anything from the calculators, the permit finder or the project brief tool: they run in your browser and the address you type into the permit finder is sent only to the U.S. Census Bureau geocoder, not to us.</p>")
    body += sec("How we use it", f"<p>To contact you about your estimate by phone, text or email, to schedule and perform the work, and to keep a record of the job. If you check the consent box we may text you about your project; standard message rates apply and you can reply STOP at any time. We do not sell your information and we do not share it with anyone other than the crew that performs your work and the service providers that deliver our email and hosting (Cloudflare).</p>", cls="alt")
    body += sec("Analytics", "<p>We use Cloudflare Web Analytics, which does not use cookies or store personal data. If Google Analytics or Microsoft Clarity are added, this page will be updated and a consent notice will appear where the law requires one.</p>")
    body += sec("Retention and your rights", f"<p>Estimate requests that do not become jobs are deleted after 24 months. Job records are kept for the warranty term plus the period Florida law requires for contracts. Email {EMAIL} to see, correct or delete what we hold about you. Florida residents may also have rights under the Florida Digital Bill of Rights where it applies.</p>", cls="alt")
    body += sec("Calls", "<p>Calls to our number may be answered by a call-forwarding service. If calls are ever recorded, you will hear a notice at the start of the call.</p>")
    return {"route": "/privacy/", "title": "Privacy Policy – Kissimmee Concrete", "meta_description": "What Kissimmee Concrete collects when you request an estimate, how it is used, who it is shared with, how long it is kept, and how to see, correct or delete it.", "h1": "Privacy policy", "breadcrumbs": [("Home", "/"), ("Privacy", None)], "body_html": body, "kind": "legal"}


def terms():
    body = sec("Using this site", "<p>The content on kissimmeeconcrete.com is general information about concrete and paver work in Central Florida. It is not a quote, not engineering advice and not legal advice. Prices are planning ranges with a published method; your price is in your written proposal. Permit and HOA rules are quoted from official sources as of the date shown on each page and can change; confirm with the office or association before you rely on them.</p>")
    body += sec("Tools and calculators", "<p>The calculator, permit finder, decision tool, pour calendar and project brief run in your browser and produce estimates and planning notes. They can be wrong for an unusual lot, an address near a boundary, or a project outside the assumptions stated on the tool. Use them to prepare for an estimate, not to order materials or file a permit.</p>", cls="alt")
    body += sec("Estimates and contracts", "<p>Sending the estimate form does not create a contract. Work is performed under a written contract that states scope, specifications, price, schedule, payment terms and the workmanship warranty. The contract controls over anything on this site.</p>")
    body += sec("Content and reuse", "<p>Text, photos and tools are ours unless stated. The Cost Index data at /api/cost-index.json and .csv is licensed CC BY 4.0: reuse it with attribution to Kissimmee Concrete and a link to the index page. Concept renderings are labelled as such and may not be presented as photographs of finished work.</p>", cls="alt")
    body += sec("Liability", "<p>To the extent permitted by Florida law, we are not liable for decisions made on the basis of general information on this site. Nothing here limits the rights you have under a signed contract or under law.</p>")
    return {"route": "/terms/", "title": "Terms of Use – Kissimmee Concrete", "meta_description": "How to read the information, prices and tools on kissimmeeconcrete.com, what an estimate request does and does not create, and how the Cost Index data may be reused.", "h1": "Terms of use", "breadcrumbs": [("Home", "/"), ("Terms", None)], "body_html": body, "kind": "legal"}


def accessibility():
    body = sec("Our target", f"<p>We aim for WCAG 2.2 Level AA across the site: semantic headings and landmarks, labelled form fields, visible keyboard focus, text contrast of at least 4.5:1, touch targets of at least 44 pixels, no content that depends on color alone, reduced motion respected, and every image described in alt text (with renderings identified). Tables have header rows; tools work with a keyboard and announce results.</p>")
    body += sec("Known limitations", "<p>The permit finder depends on a third-party geocoder; if it is unavailable the tool falls back to a ZIP-code lookup with a note. PDF downloads are not offered; the project brief prints from the page instead.</p>", cls="alt")
    body += sec("Report a barrier", f"<p>Email {EMAIL} with the page URL and what happened. We respond within two business days and fix confirmed barriers in the next release.</p>")
    return {"route": "/accessibility/", "title": "Accessibility Statement – Kissimmee Concrete", "meta_description": "Kissimmee Concrete targets WCAG 2.2 AA: landmarks, labels, focus, contrast, touch targets, reduced motion and described images. Known limitations and how to report a barrier.", "h1": "Accessibility", "breadcrumbs": [("Home", "/"), ("Accessibility", None)], "body_html": body, "kind": "legal"}


def notfound():
    body = sec("That page isn't here", f"<p class=\"lede\">The address may have a typo, or the page moved. Try one of these:</p>" + related(['<a href="/concrete/">Concrete services</a>', '<a href="/pavers/">Pavers &amp; hardscape</a>', '<a href="/areas/">Service area</a>', '<a href="/pricing/">Pricing &amp; Cost Index</a>', '<a href="/permits/">Permits</a>', '<a href="/tools/">Tools</a>', '<a href="/guides/">Guides</a>', '<a href="/faq/">FAQ</a>', '<a href="/contact/">Contact</a>']))
    return {"route": "/404/", "title": "Page Not Found – Kissimmee Concrete", "meta_description": "That page does not exist on kissimmeeconcrete.com. Jump to concrete or paver services, the service-area map, pricing, permits, tools, guides or the estimate form.", "h1": "Page not found", "breadcrumbs": [("Home", "/"), ("Not found", None)], "body_html": body, "kind": "legal", "noindex": True, "no_cta": True}


def thankyou():
    body = sec("We have your request", f"<p class=\"lede\">Thanks. Someone will be in touch to agree a time for the site visit, and you will have a written proposal shortly after it. Photos and measurements are welcome any time at <a href=\"mailto:{EMAIL}\">{EMAIL}</a>, and they usually shorten the visit.</p><p>Three things worth doing while you wait. Run the <a href=\"/tools/permit-finder/\">permit finder</a> so you know which office has jurisdiction over your address. Look at the <a href=\"/pricing/\">current price ranges</a> so the proposal arrives in a context. And if you are in a community with architectural review, start the <a href=\"/tools/hoa-packet-checklist/\">packet</a>, because that approval is usually the longest item in the schedule rather than anything we control.</p>")
    return {"route": "/thank-you/", "title": "Request Received – Kissimmee Concrete", "meta_description": "Your estimate request reached Kissimmee Concrete. We reply during business hours to schedule a site visit and send a written proposal.", "h1": "Request received", "breadcrumbs": [("Home", "/"), ("Thank you", None)], "body_html": body, "kind": "legal", "noindex": True, "no_cta": True}


def get_pages():
    return [about(), editorial(), data_methods(), warranty(), contact(), gallery(), privacy(), terms(), accessibility(), notfound(), thankyou()]
