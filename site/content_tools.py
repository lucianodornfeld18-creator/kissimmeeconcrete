# -*- coding: utf-8 -*-
"""Tools hub and the P1 tools. Each tool is plain HTML + one inline script (hashed into the CSP by build.py)."""
import json
from _data import TOOLS, TOOL_ORDER, COST_INDEX, COST_INDEX_RELEASE, JURISDICTIONS, CITIES, TIER1
from _helpers import cap, sec, table, cards, svc, city, tool, guide, compare, juris, hoa, faq, cost_range, steps, callout, related, esc

R = COST_INDEX_RELEASE["label"]
D = COST_INDEX_RELEASE["date"]
INDEX_JS = json.dumps({k: [lo, hi] for k, n, u, lo, hi, note in COST_INDEX})

NOAA = [("Jan", 71.8, 48.3, 2.67, 7.6, 4.1), ("Feb", 74.4, 50.7, 2.37, 6.5, 4.0), ("Mar", 77.9, 54.4, 3.07, 6.2, 4.2), ("Apr", 83.0, 59.7, 2.43, 5.7, 3.6), ("May", 87.4, 65.8, 4.17, 7.8, 5.7), ("Jun", 90.0, 71.8, 9.18, 15.8, 12.3), ("Jul", 91.5, 73.5, 7.21, 16.7, 12.2), ("Aug", 91.4, 74.1, 8.38, 17.7, 13.0), ("Sep", 89.5, 72.8, 5.88, 14.3, 9.5), ("Oct", 84.6, 66.2, 3.07, 8.7, 5.7), ("Nov", 78.6, 57.3, 1.99, 5.8, 3.1), ("Dec", 73.5, 51.5, 2.15, 6.5, 3.5)]

# Ask the Estimator entries: real question patterns from estimating calls, anonymized; no names, no addresses.
ASK_ENTRIES = [
    {"id": "q-2026-09-01", "date": "2026-09-10", "rfc822": "Thu, 10 Sep 2026 12:00:00 -0400", "q": "My driveway in BVL has a 2-inch step at the garage. Can you just fix that panel?", "a_html": "<p>Yes, if the rest of the drive is sound, and we price the whole drive alongside because in Buenaventura Lakes the other panels are usually on the same clock. First the downspout gets extended past the slab; then the panel comes out and goes back on a compacted base. About $1,100 to $1,900 for a 10-by-12 panel in the current index.</p>", "a_text": "Yes, if the rest of the drive is sound; we price the panel and the whole drive. Fix the downspout first. About $1,100 to $1,900 for a 10-by-12 panel.", "link": "/concrete/repair/buenaventura-lakes/"},
    {"id": "q-2026-09-02", "date": "2026-09-10", "rfc822": "Thu, 10 Sep 2026 12:05:00 -0400", "q": "We're in Solterra. Can we widen the driveway to fit a third car?", "a_html": "<p>Solterra's guidelines cap an expanded driveway at three cars wide and bar adding walking area, so a third-car width is usually approvable with the ARC packet (survey markup, product sample, our insurance certificate if the Reviewer asks). Polk County permits the right-of-way portion. Plan on the ARC cycle before the work.</p>", "a_text": "Solterra allows up to three cars wide with ARC approval; no added walking area; Polk permits the right-of-way portion.", "link": "/hoa/solterra/"},
    {"id": "q-2026-09-03", "date": "2026-09-10", "rfc822": "Thu, 10 Sep 2026 12:10:00 -0400", "q": "Our new pavers in Weslyn Park have a white haze. Did the builder use bad pavers?", "a_html": "<p>No. That is efflorescence, salts migrating out of concrete pavers during the first rainy season. It washes off with an efflorescence cleaner and then the pavers get their first seal. The mistake would be sealing over it.</p>", "a_text": "It is efflorescence, normal in the first season; clean it, then seal. Never seal over it.", "link": "/pavers/sealing/st-cloud/"},
    {"id": "q-2026-09-04", "date": "2026-09-10", "rfc822": "Thu, 10 Sep 2026 12:15:00 -0400", "q": "Is my Poinciana house in Osceola or Polk for the permit?", "a_html": "<p>It depends on the village; the county line runs through the community. The permit finder on this site checks the address against the Census county boundary, and APV's office at 401 Walnut Street can confirm your village. Either way the DCB application goes in first.</p>", "a_text": "Depends on the village; the permit finder checks the county boundary; the DCB application comes first either way.", "link": "/areas/poinciana/"},
    {"id": "q-2026-09-05", "date": "2026-09-10", "rfc822": "Thu, 10 Sep 2026 12:20:00 -0400", "q": "Can you pour a patio in July or should we wait?", "a_html": "<p>We pour in July with a first-light start and the slab finished and covered before the afternoon storms; the Kissimmee 2 station averages 16.7 rain days in July, almost all after 2 p.m. If the morning forecast shows more than a 60 percent chance before 2 p.m. we move a day. Waiting for October means a drier calendar but a longer queue.</p>", "a_text": "Yes, with a first-light start; July averages 16.7 rain days, almost all afternoon. Over 60 percent chance before 2 p.m. moves the pour.", "link": "/tools/pour-calendar/"},
    {"id": "q-2026-09-06", "date": "2026-09-10", "rfc822": "Thu, 10 Sep 2026 12:25:00 -0400", "q": "Why does everyone say 'licensed and insured' if there's no license for concrete?", "a_html": "<p>Habit, mostly. Florida has no state license for concrete flatwork, pavers or stucco, and since July 1, 2023 counties and cities may not require a local one for driveway or paver work (s. 489.117(4)(a)). Some contractors hold a building or general contractor license for other work and say so; anyone claiming a license should show the number and category. What you can verify on everyone: insurance certificate, Sunbiz registration, references, a written contract.</p>", "a_text": "Florida does not license flatwork or pavers and local licensing is preempted; verify insurance, Sunbiz and references instead.", "link": "/guides/how-to-verify-a-concrete-contractor-florida/"},
]


def hub():
    body = sec("Tools built for lots in Kissimmee, Osceola County and the Polk ridge",
        cap("Seven tools that run in your browser: a jurisdiction finder that tells you which permit office covers an address, a concrete and paver calculator with current index ranges, a concrete-versus-pavers decision tool, an HOA packet checklist built from the criteria we have read, a pour calendar from the Kissimmee 2 NOAA station, a running log of real questions from estimates, and a project-brief generator so three contractors quote the same job."),
        eyebrow="Tools")
    body += sec("The tools", cards([(TOOLS[k]["name"], TOOLS[k]["short"], TOOLS[k]["route"], "Open") for k in TOOL_ORDER], cols=3))
    body += sec("How they work and what they don't do", "<p>Everything computes locally; the only outside call is the permit finder's address lookup to the U.S. Census Bureau geocoder, which we never see. Results are planning estimates: the calculator uses the current Cost Index ranges, the finder uses simplified Census boundaries (confirm addresses within a few hundred feet of a line with the county), and the decision tool weighs the factors we would weigh on a site visit. None of them replaces the visit.</p>", cls="alt")
    return {"route": "/tools/", "title": "Concrete & Paver Tools – Permit Finder, Calculator, Pour Calendar", "meta_description": "Free tools for Kissimmee and Osceola County lots: permit and jurisdiction finder by address, concrete and paver calculator with current cost ranges, concrete vs. pavers decision tool, HOA packet checklist, pour calendar, project brief.", "h1": "Tools", "breadcrumbs": [("Home", "/"), ("Tools", None)], "body_html": body, "kind": "tool", "nav_active": "/tools/", "no_cta": True}


def permit_finder():
    rules = {
        "Kissimmee": ("city-of-kissimmee", "City of Kissimmee"),
        "St. Cloud": ("city-of-st-cloud", "City of St. Cloud"),
        "Osceola": ("osceola-county", "Unincorporated Osceola County"),
        "Polk": ("polk-county", "Unincorporated Polk County"),
        "Orange": ("orange-county", "Unincorporated Orange County"),
    }
    rule_json = json.dumps({
        "city-of-kissimmee": {"name": "City of Kissimmee", "route": "/permits/city-of-kissimmee/", "phone": "407-518-2278", "driveway": "Driveway / Sidewalk Construction application on the EnerGov portal (Engineering Division). Plan review at least 2 business days; permit at least 2 business days after payment. Right-of-way work needs Public Works & Engineering approval.", "patio": "Building Division reviews by scope; a detached slab outside setbacks is often flatwork. HB 803 written-request exemption under $7,500. Confirm at permitting@kissimmee.org.", "pavers": "Same driveway application for a paver driveway; patios per the patio rule.", "who": "We file as contractor; you sign."},
        "city-of-st-cloud": {"name": "City of St. Cloud", "route": "/permits/city-of-st-cloud/", "phone": "407-957-7300", "driveway": "Building Department; work in the right-of-way needs Public Works and Engineering approval. Asphalt reseal is exempt; a new concrete driveway is not.", "patio": "Patios and decks are on the city's permit-required list. HB 803 exemption adopted for qualifying work under $7,500 with a written request.", "pavers": "'Pavers for driveways/sidewalks: refer to Public Works' (no building permit).", "who": "We file; cashless payments since 2025-01-01."},
        "osceola-county": {"name": "Unincorporated Osceola County", "route": "/permits/osceola-county/", "phone": "407-742-0200", "driveway": "County driveway permit required for construction or widening; residential driveways may not exceed 24 ft wide without a conditional use (Code §22-50.6). Residential plan review normally 3–5 days. Notice of Commencement at $5,000+.", "patio": "A detached slab outside setbacks is generally flatwork; attached, roofed, in-setback or flood-zone slabs are permitted. HB 803 written-request exemption under $7,500.", "pavers": "Covered by the driveway permit; the apron follows the county detail.", "who": "We file; you sign the application and the NOC."},
        "polk-county": {"name": "Unincorporated Polk County", "route": "/permits/polk-county/", "phone": "(863) 534-6080", "driveway": "Permit for sidewalks and driveway portions in the right-of-way or within the minimum setbacks; drainage requirements apply.", "patio": "A detached slab outside setbacks is not permitted separately; slabs adjacent to or supporting a structure, elevated, or within setbacks are.", "pavers": "Pavers within setbacks or adjacent to structures must meet the codes; pavers in the right-of-way need the owner's recorded Concrete Driveway Paver Release Form (a concrete apron avoids it).", "who": "We file; Bartow or the Northeast Government Center in Lake Alfred."},
        "orange-county": {"name": "Unincorporated Orange County", "route": "/permits/orange-county/", "phone": "407-836-5550", "driveway": "'Anytime you are pouring concrete or placing pavers, a permit is required.' Right-of-way apron: 6 in, 3,000 psi, no steel, 3 ft from the property line.", "patio": "Permit required for poured concrete.", "pavers": "Zoning permit.", "who": "We file."},
        "other-city": {"name": "A city with its own building department", "route": "/permits/polk-county/", "phone": "", "driveway": "This address is inside a city that reviews its own permits (Davenport, Haines City, Winter Haven, Auburndale, Lake Alfred, Dundee, Lake Wales, Polk City, Orlando, Windermere, etc.). We did not verify that city's published flatwork rules; we call before quoting.", "patio": "Confirm with the city's building department.", "pavers": "Confirm with the city.", "who": "We call the city and put the answer in the proposal."},
    })
    body = sec("Which office permits work at your address?",
        cap("Type a street address in Osceola, Polk or south Orange County. Your browser sends it to the U.S. Census Bureau's public geocoder (not to us), gets coordinates back, and checks them against simplified Census city and county boundaries stored on this site. You then see the permit rules we have verified for that jurisdiction, for a driveway, a patio or slab, and pavers. Addresses within a few hundred feet of a line should be confirmed with the county."),
        eyebrow="Permit & Jurisdiction Finder")
    body += f'''
<section><div class="wrap">
<div class="tool" id="finder">
  <div class="field"><label for="pf-addr">Street address, city, ZIP</label><input id="pf-addr" type="text" placeholder="e.g. 123 Example St, Kissimmee, FL 34744" autocomplete="street-address"></div>
  <div class="cta-row"><button class="btn btn-primary" id="pf-go" type="button">Find my jurisdiction</button><span class="note" id="pf-status" aria-live="polite"></span></div>
  <div class="result" id="pf-result" hidden></div>
  <details style="margin-top:14px"><summary class="small">No result or no internet for the geocoder? Look up by ZIP (rougher)</summary>
    <div class="field" style="margin-top:8px"><label for="pf-zip">ZIP code</label><input id="pf-zip" type="text" inputmode="numeric" maxlength="5" placeholder="34744"></div>
    <button class="btn btn-outline" id="pf-zip-go" type="button">Look up ZIP</button>
    <p class="note">ZIPs cross city lines; this fallback tells you the likely county and the offices to call, not the definitive jurisdiction.</p>
  </details>
</div>
<p class="note" style="margin-top:12px">Boundaries: U.S. Census Bureau TIGERweb 2024, simplified. Rules: verified on the official pages on 2026-09-10; see each linked permit page for the source. Nothing you type is stored by us.</p>
</div></section>
<script>
(function(){{
var RULES={rule_json};
var ZIPS={{"34741":"Kissimmee","34743":"Osceola","34744":"Kissimmee","34745":"Kissimmee","34746":"Osceola","34747":"Osceola","34758":"Osceola","34759":"Polk","34769":"St. Cloud","34771":"Osceola","34772":"Osceola","34773":"Osceola","33837":"Polk","33896":"Osceola","33897":"Polk","33844":"Polk","33845":"Polk","33880":"Polk","33881":"Polk","33884":"Polk","33853":"Polk","33859":"Polk","33823":"Polk","33850":"Polk","33838":"Polk","33868":"Polk","32837":"Orange","32824":"Orange","32821":"Orange","32827":"Orange","32809":"Orange","32812":"Orange"}};
var CITY_OWN={{"Kissimmee":"city-of-kissimmee","St. Cloud":"city-of-st-cloud"}};
var COUNTY_KEY={{"Osceola":"osceola-county","Polk":"polk-county","Orange":"orange-county"}};
var data=null;
function q(s){{return document.querySelector(s);}}
function status(t){{q('#pf-status').textContent=t;}}
function pip(pt,ring){{var x=pt[0],y=pt[1],inside=false;for(var i=0,j=ring.length-1;i<ring.length;j=i++){{var xi=ring[i][0],yi=ring[i][1],xj=ring[j][0],yj=ring[j][1];var inter=((yi>y)!==(yj>y))&&(x<(xj-xi)*(y-yi)/(yj-yi)+xi);if(inter)inside=!inside;}}return inside;}}
function inPolys(pt,polys){{for(var p=0;p<polys.length;p++){{var rings=polys[p];if(pip(pt,rings[0])){{var hole=false;for(var r=1;r<rings.length;r++){{if(pip(pt,rings[r]))hole=true;}}if(!hole)return true;}}}}return false;}}
function classify(lon,lat){{var pt=[lon,lat];var county=null,place=null;for(var i=0;i<data.counties.length;i++){{if(inPolys(pt,data.counties[i].polys)){{county=data.counties[i].name;break;}}}}for(var j=0;j<data.places.length;j++){{if(inPolys(pt,data.places[j].polys)){{place=data.places[j].name;break;}}}}return {{county:county,place:place}};}}
function render(c,label){{var r=RULES[c];if(!r)return;var h='<h3>'+label+'</h3>';h+='<p><strong>Driveway (new, replaced, widened):</strong> '+r.driveway+'</p>';h+='<p><strong>Patio, slab, pad, pool-deck overlay:</strong> '+r.patio+'</p>';h+='<p><strong>Pavers:</strong> '+r.pavers+'</p>';h+='<p><strong>Who files:</strong> '+r.who+(r.phone?' Office: '+r.phone+'.':'')+'</p>';h+='<p><a class="btn btn-outline" href="'+r.route+'">Read the '+r.name+' permit page</a> <a class="btn btn-primary" href="/contact/">Request an estimate</a></p>';var out=q('#pf-result');out.innerHTML=h;out.hidden=false;if(window.kcTrack)window.kcTrack('tool_permit_finder',{{result:c}});}}
function decide(res){{if(!res.county)return null;if(res.place&&CITY_OWN[res.place])return {{key:CITY_OWN[res.place],label:res.place+' city limits ('+res.county+' County)'}};if(res.place)return {{key:'other-city',label:res.place+' city limits ('+res.county+' County)'}};var k=COUNTY_KEY[res.county];if(k)return {{key:k,label:'Unincorporated '+res.county+' County'}};return {{key:null,label:res.county+' County'}};}}
function load(cb){{if(data)return cb();status('Loading boundaries…');fetch('/static/data/jurisdictions.json').then(function(r){{return r.json();}}).then(function(j){{data=j;cb();}}).catch(function(){{status('Could not load boundaries. Use the ZIP lookup below.');}});}}
q('#pf-go').addEventListener('click',function(){{var a=q('#pf-addr').value.trim();if(!a){{status('Enter an address.');return;}}load(function(){{status('Looking up address…');var url='https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?benchmark=Public_AR_Current&format=json&address='+encodeURIComponent(a);fetch(url).then(function(r){{return r.json();}}).then(function(j){{var m=j.result&&j.result.addressMatches&&j.result.addressMatches[0];if(!m){{status('No match from the Census geocoder. Check the address or use the ZIP lookup.');return;}}var res=classify(m.coordinates.x,m.coordinates.y);var d=decide(res);if(!d||!d.key){{status('That address is outside Osceola, Polk and Orange counties (or on a line). Call us and we will check.');return;}}status('Matched: '+m.matchedAddress);render(d.key,d.label);}}).catch(function(){{status('The geocoder did not respond. Use the ZIP lookup below.');}});}});}});
q('#pf-zip-go').addEventListener('click',function(){{var z=q('#pf-zip').value.trim();var c=ZIPS[z];if(!c){{status('ZIP not in our table; call us.');return;}}var key=CITY_OWN[c]||COUNTY_KEY[c];status('ZIP '+z+': likely '+c+'. Confirm with the address lookup.');render(key,'Likely: '+(CITY_OWN[c]?c+' (city)':'Unincorporated '+c+' County')+' — by ZIP');}});
q('#pf-addr').addEventListener('keydown',function(e){{if(e.key==='Enter'){{e.preventDefault();q('#pf-go').click();}}}});
}})();
</script>'''
    body += sec("The rules behind the results", table(["Jurisdiction", "Driveway", "Patio / slab", "Pavers", "Page"], [
        ("City of Kissimmee", "Driveway / Sidewalk application; 2 + 2 business days", "By scope; HB 803 < $7,500", "Same application", juris("city-of-kissimmee")),
        ("Unincorporated Osceola", "County driveway permit; 24 ft max (§22-50.6)", "Detached outside setbacks: flatwork", "Under the driveway permit", juris("osceola-county")),
        ("City of St. Cloud", "Building Dept; right-of-way via Public Works", "Permit required", "Refer to Public Works", juris("city-of-st-cloud")),
        ("Unincorporated Polk", "Right-of-way and setback portions", "Not permitted separately if detached", "Paver Release Form in the right-of-way", juris("polk-county")),
        ("Unincorporated Orange", "Permit required; 6 in apron", "Permit required", "Zoning permit", juris("orange-county")),
    ]), cls="alt")
    faqs = [
        faq("Does the finder store my address?", "No. Your browser sends it to the Census geocoder and checks the result against boundary data on this site; nothing reaches us."),
        faq("How accurate are the boundaries?", "Census 2024 TIGERweb polygons simplified to about 200 feet. Within a few hundred feet of a city line, confirm with the county property appraiser or the city."),
        faq("My address is in Davenport but the finder says Polk County?", "Most Davenport addresses are unincorporated Polk; only the small historic core is inside the city. The same is true of ChampionsGate (Osceola, not Polk) and many 'Kissimmee' addresses (county, not city)."),
        faq("What if the geocoder is down?", "Use the ZIP lookup; it gives the likely county and the offices to call."),
    ]
    return {"route": TOOLS["permit-finder"]["route"], "title": "Permit & Jurisdiction Finder – Kissimmee, Osceola, Polk (Address)", "meta_description": "Type an address in Osceola, Polk or south Orange County and see whether it is City of Kissimmee, St. Cloud, unincorporated Osceola, Polk or Orange, and the verified permit rules for a driveway, patio, slab or pavers there.", "h1": "Permit and jurisdiction finder", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Permit finder", None)], "body_html": body, "faqs": faqs, "kind": "tool", "nav_active": "/tools/", "sources": ["tigerweb", "kissimmee-driveway", "osceola-22-50-6", "stcloud-permits", "polk-faq", "polk-paver-release", "orange-permit"]}


def calculator():
    body = sec("Concrete and paver calculator for Central Florida jobs",
        cap(f"Enter length, width and the surface you want. The calculator gives cubic yards and 80-lb bags for concrete (with a waste allowance you can change), base tonnage, paver count and polymeric sand for pavers, and a planning range from the {R} Kissimmee Concrete Cost Index ({D}). It does not know your subgrade, access or HOA; the site visit does. Print the result to compare quotes line by line."),
        eyebrow="Concrete & Paver Calculator")
    body += f'''
<section><div class="wrap">
<div class="tool" id="calc">
  <div class="row-2">
    <div class="field"><label for="c-type">Surface</label><select id="c-type">
      <optgroup label="Concrete"><option value="concrete-driveway-broom">Concrete driveway, 4 in broom (cars)</option><option value="concrete-driveway-6in">Concrete driveway / pad, 6 in with rebar grid (boats, RVs)</option><option value="concrete-patio">Concrete patio, 4 in</option><option value="stamped-concrete">Stamped concrete, 4 in</option><option value="concrete-slab-pad">Concrete pad (shed, AC, generator, hot tub)</option><option value="concrete-sidewalk">Concrete walkway, 4 in</option></optgroup>
      <optgroup label="Pavers"><option value="paver-driveway-concrete">Paver driveway, 80 mm concrete pavers</option><option value="paver-driveway-premium">Paver driveway, premium line</option><option value="paver-patio">Paver patio, 60 mm</option><option value="paver-pool-deck">Paver pool-deck overlay</option><option value="travertine-pool-deck">Travertine pool deck</option><option value="paver-walkway">Paver walkway</option></optgroup>
      <optgroup label="Maintenance"><option value="paver-sealing">Paver clean, re-sand and seal</option><option value="concrete-resurfacing">Concrete resurfacing / overlay</option><option value="paver-repair">Paver lift-and-relay</option></optgroup>
    </select></div>
    <div class="field"><label for="c-remove">Remove existing concrete first?</label><select id="c-remove"><option value="0">No</option><option value="1">Yes (adds $2–$4 per sq ft)</option></select></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="c-len">Length (ft)</label><input id="c-len" type="number" min="1" step="0.5" value="24" inputmode="decimal"></div>
    <div class="field"><label for="c-wid">Width (ft)</label><input id="c-wid" type="number" min="1" step="0.5" value="20" inputmode="decimal"></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="c-thick">Concrete thickness (in)</label><select id="c-thick"><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="8">8</option></select></div>
    <div class="field"><label for="c-waste">Waste allowance (%)</label><input id="c-waste" type="number" min="0" max="25" step="1" value="8" inputmode="numeric"></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="c-paver">Paver size</label><select id="c-paver"><option value="0.3125">4×12 in (0.33 sq ft)</option><option value="0.5">6×12 in (0.5 sq ft)</option><option value="1" selected>12×12 in (1 sq ft)</option><option value="2">12×24 in (2 sq ft)</option><option value="4">24×24 in (4 sq ft)</option><option value="0.39">4×8 brick (0.22 sq ft, 4.5 per sq ft)</option></select></div>
    <div class="field"><label for="c-base">Base depth (in)</label><select id="c-base"><option value="4">4 (patio, walk, concrete slab)</option><option value="6" selected>6 (paver driveway)</option><option value="8">8 (commercial)</option></select></div>
  </div>
  <div class="cta-row"><button class="btn btn-primary" id="c-go" type="button">Calculate</button><button class="btn btn-outline" type="button" id="c-print">Print</button></div>
  <div class="result" id="c-result" hidden></div>
</div>
<p class="note" style="margin-top:12px">Assumptions: 1 cubic yard = 27 cu ft; one 80-lb bag ≈ 0.6 cu ft; limerock base ≈ 1.5 tons per cubic yard compacted; bedding sand 1 in; polymeric sand coverage ≈ 60–80 sq ft per 50-lb bag for standard joints. Ranges are installed planning figures, not quotes; small jobs sit at the top of a range because of truck minimums.</p>
</div></section>
<script>
(function(){{
var IDX={INDEX_JS};
var PAVER_KEYS=['paver-driveway-concrete','paver-driveway-premium','paver-patio','paver-pool-deck','travertine-pool-deck','paver-walkway'];
var CONC_KEYS=['concrete-driveway-broom','concrete-driveway-6in','concrete-patio','stamped-concrete','concrete-slab-pad','concrete-sidewalk','concrete-resurfacing'];
function q(s){{return document.querySelector(s);}}
function money(v){{return '$'+Math.round(v).toLocaleString('en-US');}}
function calc(){{
 var t=q('#c-type').value,L=parseFloat(q('#c-len').value)||0,W=parseFloat(q('#c-wid').value)||0,th=parseFloat(q('#c-thick').value),waste=parseFloat(q('#c-waste').value)||0,ps=parseFloat(q('#c-paver').value),bd=parseFloat(q('#c-base').value),rem=q('#c-remove').value==='1';
 var area=L*W;if(area<=0){{return;}}
 var r=IDX[t]||[0,0];var lo=r[0],hi=r[1];
 var unitNote='';
 if(t==='concrete-sidewalk'){{lo=lo/4;hi=hi/4;unitNote=' (converted from per linear foot at 4 ft wide)';}}
 var small=area<200&&(CONC_KEYS.indexOf(t)>=0||PAVER_KEYS.indexOf(t)>=0);
 var costLo=area*lo,costHi=area*hi;
 if(small){{costLo=Math.max(costLo,area*((lo+hi)/2));}}
 var h='<h3>'+area.toLocaleString('en-US')+' sq ft ('+L+' × '+W+' ft)</h3>';
 if(CONC_KEYS.indexOf(t)>=0&&t!=='concrete-resurfacing'){{
  var thick=t==='concrete-driveway-6in'?Math.max(th,6):th;
  var cy=area*(thick/12)/27;var cyw=cy*(1+waste/100);var bags=Math.ceil(cyw*27/0.6);
  var baseT=area*(bd/12)/27*1.5;
  h+='<p><strong>Concrete:</strong> '+cy.toFixed(2)+' cu yd at '+thick+' in; order about <strong>'+cyw.toFixed(2)+' cu yd</strong> with '+waste+'% waste ('+bags.toLocaleString('en-US')+' bags of 80 lb if bagged; over ~1.5 cu yd, ready-mix is the sensible choice). Ready-mix in the Orlando market: '+money(IDX['ready-mix'][0]*cyw)+' – '+money(IDX['ready-mix'][1]*cyw)+' for the material alone.</p>';
  h+='<p><strong>Base:</strong> '+bd+' in compacted limerock ≈ '+baseT.toFixed(1)+' tons.</p>';
  h+='<p><strong>Mix and steel we would specify:</strong> '+(thick>=6?'4,000 psi with a #4 rebar grid at 18 in on chairs':'3,000–3,500 psi with fiber and #4 bars at edges and re-entrant corners')+'; joints every '+(thick>=6?'12–15':'10')+' ft, cut within 12 hours.</p>';
 }}
 if(PAVER_KEYS.indexOf(t)>=0){{
  var count=Math.ceil(area/ps*(1+waste/100));var baseT2=area*(bd/12)/27*1.5;var sand=area*(1/12)/27;var poly=Math.ceil(area/70);
  h+='<p><strong>Pavers:</strong> about <strong>'+count.toLocaleString('en-US')+'</strong> units at '+ps+' sq ft each including '+waste+'% waste (more for curves and borders).</p>';
  h+='<p><strong>Base:</strong> '+bd+' in compacted limerock ≈ '+baseT2.toFixed(1)+' tons; <strong>bedding sand:</strong> '+sand.toFixed(2)+' cu yd; <strong>polymeric sand:</strong> about '+poly+' bags (50 lb).</p>';
  h+='<p><strong>Edge restraint:</strong> about '+Math.round(2*(L+W))+' linear ft if the whole perimeter is free (less where it meets the house or the apron).</p>';
 }}
 h+='<p><strong>Planning range ('+'{R}'+' Kissimmee Concrete Cost Index):</strong> <strong>'+money(costLo)+' – '+money(costHi)+'</strong> installed'+unitNote+(small?' (small-job floor applied)':'')+'.</p>';
 if(rem){{h+='<p><strong>Removal of existing concrete:</strong> '+money(area*2)+' – '+money(area*4)+'.</p>';}}
 h+='<p class="note">Not a quote. Excludes fill to raise a slab above the water table, drainage, root barriers, pump trucks, permit and HOA fees. Index release '+'{D}'+'; method on the Data &amp; methods page.</p>';
 var out=q('#c-result');out.innerHTML=h;out.hidden=false;if(window.kcTrack)window.kcTrack('tool_calculator',{{type:t,area:area}});
}}
q('#c-go').addEventListener('click',calc);
q('#c-print').addEventListener('click',function(){{calc();window.print();}});
q('#c-type').addEventListener('change',function(){{var t=this.value;if(t==='concrete-driveway-6in')q('#c-thick').value='6';if(PAVER_KEYS.indexOf(t)>=0)q('#c-base').value=(t.indexOf('driveway')>=0?'6':'4');}});
}})();
</script>'''
    body += sec("How to use the numbers", f"<p>Compare quotes on the same basis: thickness, PSI, reinforcement, base depth, joint layout, drainage and what is excluded. A quote that is far below the range is usually missing base or steel; one far above may include real site work (fill, drains, access). The {tool('project-brief')} writes those specs into a one-page brief. Cost guides: <a href=\"/pricing/concrete/\">concrete</a>, <a href=\"/pricing/pavers/\">pavers</a>.</p>", cls="alt")
    faqs = [
        faq("How much concrete do I need for a 20x24 driveway at 4 inches?", "About 5.9 cubic yards, or 6.4 with an 8 percent waste allowance; ready-mix, not bags."),
        faq("How many pavers for 400 square feet?", "About 432 12-by-12 units with 8 percent waste, or 1,944 4-by-8 bricks; more for curves and borders."),
        faq("Why is the low end sometimes higher than area × low rate?", "Small jobs under 200 square feet carry truck minimums and a full crew day, so the calculator applies a floor."),
        faq("Does this include removing my old driveway?", "Only if you select it; removal adds $2 to $4 per square foot."),
    ]
    return {"route": TOOLS["concrete-paver-calculator"]["route"], "title": "Concrete & Paver Calculator – Yards, Bags, Base, Cost (Kissimmee)", "meta_description": f"Calculate cubic yards and bags of concrete, limerock base, paver count and polymeric sand for a driveway, patio, pad or pool deck, with a planning cost range from the {R} Kissimmee Concrete Cost Index. Printable.", "h1": "Concrete and paver calculator", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Calculator", None)], "body_html": body, "faqs": faqs, "kind": "tool", "nav_active": "/tools/"}


def decision():
    body = sec("Concrete or pavers? Eight questions, one recommendation",
        cap("Answer eight questions about the job and the lot and get a recommendation with the reasons, weighted the way we weigh them on a site visit: budget, HOA, use, repair expectations, heat, resale, drainage and how long you plan to stay. It is a starting point for the conversation, not the estimate."),
        eyebrow="Decision tool")
    body += '''
<section><div class="wrap">
<form class="tool" id="dt" onsubmit="return false">
  <div class="field"><label for="d1">1. What is the surface?</label><select id="d1"><option value="driveway">Driveway</option><option value="patio">Patio or lanai extension</option><option value="pool">Pool deck</option><option value="walk">Walkway or entry</option></select></div>
  <div class="field"><label for="d2">2. Is there an HOA or ARC with a paver palette or a paver tradition?</label><select id="d2"><option value="paver">Yes, pavers are the norm (resort or planned community)</option><option value="none">No HOA, or the street is concrete</option><option value="unsure">Not sure</option></select></div>
  <div class="field"><label for="d3">3. Budget for this surface</label><select id="d3"><option value="low">Lowest total cost matters most</option><option value="mid">Willing to pay more for repairability and look</option><option value="high">Premium finish wanted</option></select></div>
  <div class="field"><label for="d4">4. Will the surface be walked barefoot in summer?</label><select id="d4"><option value="no">Rarely</option><option value="yes">Often (pool, lanai)</option></select></div>
  <div class="field"><label for="d5">5. Do you expect future work through or on the surface (utility lines, widening, a pool later, tree roots nearby)?</label><select id="d5"><option value="no">Unlikely</option><option value="yes">Likely</option></select></div>
  <div class="field"><label for="d6">6. Maintenance you will actually do</label><select id="d6"><option value="min">Minimal; pressure wash now and then</option><option value="ok">Sealing every few years is fine</option></select></div>
  <div class="field"><label for="d7">7. How long will you own the home?</label><select id="d7"><option value="short">Under 5 years</option><option value="long">5 years or more</option></select></div>
  <div class="field"><label for="d8">8. Is it a vacation rental?</label><select id="d8"><option value="no">No</option><option value="yes">Yes</option></select></div>
  <div class="cta-row"><button class="btn btn-primary" id="d-go" type="button">Get a recommendation</button></div>
  <div class="result" id="d-result" hidden></div>
</form>
</div></section>
<script>
(function(){
function q(s){return document.querySelector(s);}
q('#d-go').addEventListener('click',function(){
 var s={concrete:0,pavers:0,stone:0},why=[];
 var d1=q('#d1').value,d2=q('#d2').value,d3=q('#d3').value,d4=q('#d4').value,d5=q('#d5').value,d6=q('#d6').value,d7=q('#d7').value,d8=q('#d8').value;
 if(d1==='pool'){s.pavers+=2;s.stone+=2;why.push('Pool decks favor pavers or stone for coping, drainage and repair.');}
 if(d1==='driveway'){s.concrete+=1;why.push('Driveways are where plain concrete gives the most surface per dollar.');}
 if(d2==='paver'){s.pavers+=3;s.stone+=1;why.push('The community already reviews and prefers pavers; matching it avoids ARC friction and helps resale.');}
 if(d2==='none'){s.concrete+=2;why.push('No paver tradition on the street: concrete matches and costs less.');}
 if(d3==='low'){s.concrete+=3;why.push('Lowest first cost: broom-finish concrete runs 50–70 percent below pavers in the current index.');}
 if(d3==='mid'){s.pavers+=2;}
 if(d3==='high'){s.stone+=3;s.pavers+=1;why.push('A premium budget opens travertine, marble and large-format porcelain.');}
 if(d4==='yes'){s.stone+=3;s.concrete-=1;why.push('Barefoot use in July: light travertine and marble measure coolest in published comparisons.');}
 if(d5==='yes'){s.pavers+=3;s.concrete-=2;why.push('Future cuts or widening: pavers can be lifted and relaid; concrete patches show.');}
 if(d6==='min'){s.concrete+=2;s.pavers-=1;why.push('Minimal maintenance: concrete needs the least; pavers need sanding and sealing every few years.');}
 if(d7==='long'){s.pavers+=1;}
 if(d8==='yes'){s.pavers+=2;s.stone-=1;why.push('Rental traffic and weekly cleaning favor sealed concrete pavers with anti-slip sealer.');}
 var best='concrete',bs=s.concrete;if(s.pavers>bs){best='pavers';bs=s.pavers;}if(s.stone>bs){best='stone';bs=s.stone;}
 var names={concrete:'Poured concrete',pavers:'Concrete pavers',stone:'Travertine or marble'};
 var links={concrete:'<a class="btn btn-primary" href="/concrete/">Concrete services</a> <a class="btn btn-outline" href="/pricing/concrete/">Concrete costs</a>',pavers:'<a class="btn btn-primary" href="/pavers/">Paver services</a> <a class="btn btn-outline" href="/pricing/pavers/">Paver costs</a>',stone:'<a class="btn btn-primary" href="/pavers/travertine/">Travertine</a> <a class="btn btn-outline" href="/pavers/marble-porcelain/">Marble &amp; porcelain</a>'};
 var h='<h3>Recommendation: '+names[best]+'</h3><p>Scores: concrete '+s.concrete+', pavers '+s.pavers+', stone '+s.stone+'.</p><ul>'+why.map(function(w){return '<li>'+w+'</li>';}).join('')+'</ul><p>'+links[best]+'</p><p class="note">Whatever the surface, on Osceola sand it needs a compacted base and water kept off the edges. Compare pages: <a href="/compare/concrete-vs-pavers/">concrete vs. pavers</a>, <a href="/compare/travertine-vs-concrete-pavers/">travertine vs. concrete pavers</a>.</p>';
 var out=q('#d-result');out.innerHTML=h;out.hidden=false;if(window.kcTrack)window.kcTrack('tool_decision',{result:best});
});
})();
</script>'''
    body += sec("Surface temperature, the factor people underweight",
        table(["Surface", "Published midday temperature, Florida sun", "Source type"], [
            ("Light travertine, tumbled", "105–120 °F", "Installer and manufacturer measurements (cited)"),
            ("Marble, light", "Coolest of the group", "Installer reports (cited)"),
            ("Light-colored concrete pavers", "115–130 °F", "Installer measurements (cited)"),
            ("Gray broom concrete", "120–135 °F", "Installer measurements (cited)"),
            ("Dark concrete pavers, dark porcelain", "130–145 °F", "Installer measurements (cited)"),
            ("Artificial turf", "Hotter than pavers", "Manufacturer guidance (cited)"),
        ], caption="Cited figures from published installer and manufacturer comparisons; our own measurement (infrared thermometer, 2 p.m., clear July day, six materials on one deck) is planned and will replace these with method and date. See the surface-temperature guide.") + f"<p>{guide('surface-temperature-pool-decks')}</p>", cls="alt")
    faqs = [
        faq("Is this tool a quote?", "No; it weighs the factors we weigh on a site visit and points you to the right pages. The estimate is in writing after the visit."),
        faq("Why does the HOA question count so much?", "Because in a paver community the ARC, the resale market and the streetscape all push the same way, and fighting it costs time and value."),
        faq("What if concrete and pavers tie?", "Then either works; the cost guides and the comparison page break the tie on money."),
    ]
    return {"route": TOOLS["concrete-vs-pavers"]["route"], "title": "Concrete vs. Pavers Decision Tool – Eight Questions (Kissimmee)", "meta_description": "Answer eight questions about your driveway, patio or pool deck (budget, HOA, barefoot use, future work, maintenance, rental) and get a concrete, paver or stone recommendation with reasons and a surface-heat table.", "h1": "Concrete vs. pavers decision tool", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Decision tool", None)], "body_html": body, "faqs": faqs, "kind": "tool", "nav_active": "/tools/"}


def hoa_checklist():
    body = sec("Build the packet your board will actually accept",
        cap("Pick your community and the type of work; the checklist assembles what the architectural committee asks for, drawn from the criteria we have read (APV, Solivita, Celebration, Bellalago, Solterra) or from the typical management-company form where we have not. Print it, gather the items, and we fill in the technical attachments."),
        eyebrow="HOA / ARC Packet Checklist")
    body += '''
<section><div class="wrap">
<form class="tool" id="hc" onsubmit="return false">
  <div class="row-2">
    <div class="field"><label for="h-comm">Community</label><select id="h-comm">
      <option value="apv">Poinciana (APV Design Control Board)</option><option value="solivita">Solivita</option><option value="celebration">Celebration (CROA ARC)</option><option value="bellalago">Bellalago / Isles of Bellalago</option><option value="solterra">Solterra Resort</option><option value="reunion">Reunion (Artemis / Greystone / Southwest)</option><option value="generic">Other planned or resort community (management ARC form)</option><option value="none">No HOA</option>
    </select></div>
    <div class="field"><label for="h-work">Work</label><select id="h-work">
      <option value="drive">Driveway replacement (same material)</option><option value="drive-change">Driveway change of material or widening</option><option value="patio">Patio or lanai extension</option><option value="pool">Pool deck overlay or rebuild</option><option value="walk">Walkway or steps</option><option value="seal">Sealing (clear)</option><option value="seal-change">Sealing with a finish change (wet look, tint)</option><option value="wall">Seat wall, fire pit, outdoor kitchen</option>
    </select></div>
  </div>
  <div class="cta-row"><button class="btn btn-primary" id="h-go" type="button">Build my checklist</button><button class="btn btn-outline" type="button" id="h-print">Print</button></div>
  <div class="result" id="h-result" hidden></div>
</form>
</div></section>
<script>
(function(){
function q(s){return document.querySelector(s);}
var C={
 apv:{name:'Poinciana (APV DCB)',contact:'401 Walnut Street, Poinciana, FL 34759 · (863) 427-0900',rules:['Prior written DCB approval is required before any driveway, patio, drainage, paved area or wall is commenced (Criteria, Article 6).','Driveway materials: concrete, asphalt or brick pavers (9.1.1). Walks beside the house no wider than 2 ft.','An application not acted on within 30 days of submittal is deemed disapproved (6.1): follow up before day 30.','Application must include a complete set of plans and specifications (6.2).'],county:'Osceola or Polk by village: county driveway permit (Osceola, 24-ft max) or Polk right-of-way rules.'},
 solivita:{name:'Solivita',contact:'Solivita Community Association ARC (Polk County)',rules:['Replacement driveways and walkways must match the original builder\\'s style and materials (6.14); extensions or modifications are reviewed individually.','Pavers, patios, driveway reseal, walkways and screen enclosures are listed on the application form as reviewable items.','Requests for pavers or tile must include a color sample or picture.','Appeals go to the Board in writing within 30 days.'],county:'Polk County: right-of-way and setback portions permitted; Paver Release Form if pavers reach the right-of-way.'},
 celebration:{name:'Celebration (CROA ARC)',contact:'Town Hall, 851 Celebration Ave · 407-566-1200 ext. 2206 · townhall@ciramail.com',rules:['ARC meets the third Monday of each month; submit a complete packet before the agenda deadline.','Current Design Guidelines and applications are on the Front Porch (owner login) or at Town Hall; get the driveway/paver section before selecting material.','Village-specific palettes and accents; joint-sand color has been a reason for rejection (installer reports, not verified by us).','Alleys are private streets maintained by the community; ARC approval doubles as access approval.'],county:'Unincorporated Osceola: county driveway permit for new or widened drives (24-ft max).'},
 bellalago:{name:'Bellalago / Isles of Bellalago',contact:'FirstService Residential · ConnectResident ARC form · resident line (866) 378-1099',rules:['Architectural review is needed prior to any change to the exterior of the home.','Submit through the online ARC Request Form on ConnectResident; the committee meets twice a month.','Written notification of the decision follows; the guidelines PDF (updated for modern materials) is available to residents.'],county:'Unincorporated Osceola: county driveway permit for new or widened drives (24-ft max).'},
 solterra:{name:'Solterra Resort',contact:'Artemis Lifestyles · (407) 705-2190',rules:['Expanded driveways no more than three cars wide; no additional walking area (VIII.J).','No painting or staining of concrete; clear matte sealer allowed with a request to the Reviewer (VIII.J).','Paver or tile requests need a lot survey with a sketch of the area and a sample of the material (II.B).','The Board may require the installer\\'s insurance certificate naming the Association, with GL and WC minimums (III.C).','Incomplete applications: 15 days to complete or a new application is required (III.A).','Rear setback 15 ft (5 ft to a pool deck or screen patio); side 5 ft (VIII.A).'],county:'Unincorporated Polk: right-of-way and setback portions permitted; Paver Release Form if pavers reach the right-of-way.'},
 reunion:{name:'Reunion Resort',contact:'Artemis Lifestyles 407-705-2190 (single-family, most condo sections) · Greystone 407-645-4945 (Villas) · Southwest Property Mgmt 407-656-1081 (Terraces)',rules:['Submit to the management company for your section; written criteria not verified by us, so ask for the current guidelines.','Expect palette matching to the streetscape and review of anything visible.'],county:'Unincorporated Osceola: county driveway permit for new or widened drives (24-ft max).'},
 generic:{name:'Management-company ARC',contact:'Your community manager',rules:['Ask the manager for the current architectural guidelines and the application form; we have not verified this community\\'s written criteria.','Expect review of anything visible from the street or a neighbor; like-for-like maintenance is usually faster.'],county:'Depends on the address: use the permit finder.'},
 none:{name:'No HOA',contact:'',rules:['No association review. County or city permit rules still apply.'],county:'Use the permit finder for the office.'}
};
var W={
 drive:['Site plan or survey with the driveway outlined and dimensions','Material name and color (sample for pavers, chip for colored concrete)','Note that the footprint is unchanged','Drainage note: water leaves the lot as before'],
 'drive-change':['Site plan or survey with existing and proposed footprint and widths','Material, color, pattern and border (physical paver sample)','Drainage note and apron detail (concrete apron at the street)','Photo of the existing driveway and the neighbors\\' for context'],
 patio:['Survey markup with dimensions and setbacks to property lines','Material, finish and color sample','Drainage note showing slope away from the house and where water goes','Statement of whether a roof or screen enclosure is planned (separate permit)'],
 pool:['Survey markup or lanai photo with the deck outlined','Material and color sample (paver, travertine, coping profile)','Drain channel location and where it discharges','Coping detail at the bond beam; cage footer note if the enclosure is being replaced'],
 walk:['Survey markup with the walk route and width','Material, pattern and border sample','Step and landing dimensions if steps are included','Note on tree roots and any root barrier'],
 seal:['Product name and finish (clear, matte); usually maintenance, confirm if a letter is needed'],
 'seal-change':['Product name and a sample or photo of the finish on a similar surface','Note that the color or sheen will change'],
 wall:['Survey markup with location, height and setbacks','Material and cap sample','Height under 4 ft and non-retaining statement (structural walls need engineering)','Gas or electrical: licensed trade permits noted']
};
var ALWAYS=['Owner name, lot address, contact','Contractor name and insurance certificate (naming the association if required)','Start date and expected duration; for rentals, the turnover window','Signature and application fee, if the association charges one'];
q('#h-go').addEventListener('click',function(){
 var c=C[q('#h-comm').value],w=W[q('#h-work').value];
 var h='<h3>'+c.name+'</h3>'+(c.contact?'<p><strong>Where it goes:</strong> '+c.contact+'</p>':'');
 h+='<p><strong>What the board asks for:</strong></p><ul>'+w.concat(ALWAYS).map(function(i){return '<li>☐ '+i+'</li>';}).join('')+'</ul>';
 h+='<p><strong>Rules that apply:</strong></p><ul>'+c.rules.map(function(r){return '<li>'+r+'</li>';}).join('')+'</ul>';
 h+='<p><strong>Permit after approval:</strong> '+c.county+' <a href="/tools/permit-finder/">Permit finder</a>.</p>';
 h+='<p class="note">Since July 1, 2026 (HB 803) an association may not require a building permit as a precondition of architectural review.</p>';
 var out=q('#h-result');out.innerHTML=h;out.hidden=false;if(window.kcTrack)window.kcTrack('tool_hoa_checklist',{community:q('#h-comm').value,work:q('#h-work').value});
});
q('#h-print').addEventListener('click',function(){q('#h-go').click();window.print();});
})();
</script>'''
    body += sec("Sources for the rules", f"<p>{hoa('poinciana-apv')}, {hoa('solivita')}, {hoa('celebration')}, {hoa('bellalago')}, {hoa('solterra')}; the <a href=\"/hoa/\">HOA hub</a> lists which communities we have verified and which we have not.</p>", cls="alt")
    faqs = [
        faq("Do you submit the packet for me?", "We prepare it and submit it where the association allows contractors to; otherwise you submit and we supply the attachments."),
        faq("What if my community isn't listed?", "Choose the management-form option; it lists what boards typically ask for, and we build to the current guidelines you get from your manager."),
        faq("Can the HOA demand a permit first?", "Not since HB 803 took effect on July 1, 2026."),
    ]
    return {"route": TOOLS["hoa-packet-checklist"]["route"], "title": "HOA & ARC Packet Checklist for Paver and Concrete Work", "meta_description": "Build the architectural review packet for pavers, a driveway change, patio, pool deck, walkway or seat wall in Poinciana, Solivita, Celebration, Bellalago, Solterra, Reunion or any management-form community. Printable.", "h1": "HOA / ARC packet checklist", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("HOA packet checklist", None)], "body_html": body, "faqs": faqs, "kind": "tool", "nav_active": "/tools/", "sources": ["apv", "solivita", "celebration", "bellalago", "solterra", "hb803"]}


def pour_calendar():
    months = "".join(
        f'<div class="month {"storm" if d10 >= 9 else ("good" if d10 <= 4.5 else "")}"><b>{m}</b><span class="small">{hi:.0f}° / {lo:.0f}°</span><div class="bar" title="{d01} rain days"><i style="width:{min(100, d01/18*100):.0f}%"></i></div><span class="small">{d01} rain days<br>{p:.1f} in</span></div>'
        for m, hi, lo, p, d01, d10 in NOAA)
    body = sec("When to pour, sand and seal in Kissimmee",
        cap("NOAA's 1991–2020 normals for the Kissimmee 2 station (USC00084625): June averages 15.8 days with measurable rain, July 16.7, August 17.7 and September 14.3, with 12 or 13 of those days over a tenth of an inch. October through April run 6 to 9. Highs peak at 91.5 °F in July. Our rule: months with 12 or more tenth-inch days are storm-season months, pours start at first light and finish before 2 p.m., and polymeric sand and sealers wait for a dry 24-hour window."),
        eyebrow="Pour Calendar · NOAA 1991–2020")
    body += f'''
<section class="alt"><div class="wrap">
<div class="calendar" aria-label="Monthly normals">{months}</div>
<p class="note" style="margin-top:10px">Bars: days with ≥ 0.01 in of rain (scale to 18). Orange border: storm-season month (≥ 9 days over 0.10 in). Green border: driest months. Source: NOAA NCEI U.S. Climate Normals 1991–2020, Kissimmee 2, FL.</p>
<div class="tool" style="margin-top:18px">
  <div class="row-2">
    <div class="field"><label for="pc-m">Month you want the work done</label><select id="pc-m">{''.join(f'<option value="{i}">{m}</option>' for i, (m, *_) in enumerate(NOAA))}</select></div>
    <div class="field"><label for="pc-w">Work</label><select id="pc-w"><option value="pour">Concrete pour</option><option value="stamp">Stamped concrete</option><option value="overlay">Resurfacing / overlay</option><option value="pavers">Paver installation</option><option value="sand">Polymeric sand and sealing</option><option value="coating">Garage floor coating</option></select></div>
  </div>
  <div class="cta-row"><button class="btn btn-primary" id="pc-go" type="button">Show the plan</button></div>
  <div class="result" id="pc-result" hidden></div>
</div>
</div></section>
<script>
(function(){{
var M={json.dumps([[m, hi, lo, p, d01, d10] for m, hi, lo, p, d01, d10 in NOAA])};
function q(s){{return document.querySelector(s);}}
q('#pc-go').addEventListener('click',function(){{
 var i=parseInt(q('#pc-m').value,10),w=q('#pc-w').value,m=M[i];var storm=m[5]>=9,hot=m[1]>=88,cool=m[1]<76;
 var h='<h3>'+m[0]+': high '+m[1]+' °F, low '+m[2]+' °F, '+m[3].toFixed(2)+' in of rain over '+m[4]+' days ('+m[5]+' days over 0.10 in)</h3>';
 var tips=[];
 if(w==='pour'||w==='stamp'){{
  tips.push(storm?'Storm-season month: first truck at daylight, slab finished and covered before 2 p.m.; more than a 60% chance of rain before 2 p.m. moves the pour a day.':'Dry-season month: full-day pours and larger placements are practical; afternoon starts are fine.');
  if(hot)tips.push('Hot: retarder in the mix, slump controlled at the truck, no water added on site, cure compound or wet cover the same day; surface sets fast but strength gain still needs 7 days for cars and 28 for heavy loads.');
  if(cool)tips.push('Cool mornings: slower set, longer finishing window; watch for a cold front the night after the pour.');
  if(w==='stamp')tips.push('Stamping in '+m[0]+': '+(hot?'small sections and an early start; the surface is ready to stamp 20–40 minutes after placement':'a comfortable stamping window; still one section at a time')+'. Seal after 28 days on a dry slab.');
 }}
 if(w==='overlay'){{tips.push(storm?'Overlays are thin: a downpour 30 minutes after placement ruins them. Morning work only, clear radar, no overlay ahead of a storm.':'Good month for overlays; allow 24 hours before sealing.');}}
 if(w==='pavers'){{tips.push('Base and pavers can be laid in rain-season months; the base must be compacted at the right moisture (wet the ridge sand, drain the flatwoods sand).');tips.push('Polymeric sand needs a dry day and a dry night: '+(storm?'book the sanding for a clear morning and expect one lost day in the schedule.':'easy to schedule this month.'));}}
 if(w==='sand'){{tips.push('Polymeric sand: install dry, vibrate, activate with a light mist, 24 hours without rain. Sealer: dry deck, 24 hours without rain, foot traffic in 4 hours. '+(storm?'Storm-season month: one dry morning for sand, another for sealer; we cancel rather than seal ahead of rain.':'Dry-season month: usually done on consecutive days.'));}}
 if(w==='coating'){{tips.push('Garage floors are indoors, but humidity matters: '+(hot?'high dew points slow polyaspartic cure and raise slab moisture; we test moisture and run fans.':'lower humidity, faster cure.'));}}
 h+='<ul>'+tips.map(function(t){{return '<li>'+t+'</li>';}}).join('')+'</ul>';
 h+='<p class="note">Normals describe an average year; the day itself is decided on the morning radar. Hurricane season runs June 1 – November 30; a named storm in the forecast pauses scheduling.</p>';
 var out=q('#pc-result');out.innerHTML=h;out.hidden=false;if(window.kcTrack)window.kcTrack('tool_pour_calendar',{{month:m[0],work:w}});
}});
}})();
</script>'''
    body += sec("The full table", table(["Month", "Avg high °F", "Avg low °F", "Rain (in)", "Days ≥ 0.01 in", "Days ≥ 0.10 in"], [(m, f"{hi:.1f}", f"{lo:.1f}", f"{p:.2f}", f"{d01}", f"{d10}") for m, hi, lo, p, d01, d10 in NOAA], caption="NOAA NCEI U.S. Climate Normals 1991–2020, station USC00084625, Kissimmee 2, FL (28.2764 N, 81.4239 W). Orlando International (USW00012815) is within a day or two of these figures every month.") + f"<p>{guide('rainy-season-concrete-scheduling')}; {guide('concrete-curing-florida-heat')}.</p>")
    faqs = [
        faq("What is the best month to pour a driveway in Kissimmee?", "November through April on rain days alone; May is the busiest month for demand. Summer pours work with first-light starts."),
        faq("Can you pour concrete in the rain?", "Not in it. We pour before the afternoon storms and cover the slab; a wetted surface after finishing is fine, a downpour during finishing is not."),
        faq("Why do polymeric sand and sealer need a dry day?", "Both cure by drying; rain within 24 hours washes sand out of the joints or clouds a film sealer."),
        faq("Where do the numbers come from?", "NOAA's 1991–2020 monthly normals for the Kissimmee 2 station, downloaded September 10, 2026."),
    ]
    return {"route": TOOLS["pour-calendar"]["route"], "title": "Pour Calendar – Rain Days & Temperatures by Month, Kissimmee FL", "meta_description": "NOAA 1991–2020 normals for the Kissimmee 2 station by month (rain days, inches, highs and lows) with our pour, stamp, overlay, paver, sanding and sealing plan for each month and the storm-season rule.", "h1": "Pour Calendar: rain days and temperatures for Kissimmee", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Pour Calendar", None)], "body_html": body, "faqs": faqs, "kind": "tool", "nav_active": "/tools/", "sources": ["noaa"]}


def ask():
    items = "".join(f'<div class="qa-item" id="{e["id"]}"><h3>{esc(e["q"])}</h3>{e["a_html"]}<p><time datetime="{e["date"]}">{e["date"]}</time> · <a href="{e["link"]}">Related page</a></p></div>' for e in ASK_ENTRIES)
    body = sec("Real questions from estimates, answered short",
        cap("A running log of questions homeowners in Kissimmee, St. Cloud, Poinciana, Celebration and the Polk ridge ask on calls and in the form, anonymized (no names, no addresses), answered in a few sentences with a link to the page that goes deeper. New entries are added as they come in; the log is also published as an RSS feed."),
        eyebrow="Ask the Estimator")
    body += f'<section class="alt"><div class="wrap">{items}<p class="note">Feed: <a href="/feed.xml">/feed.xml</a>. Ask your own through the <a href="/contact/">estimate form</a>; if it is new, it goes here.</p></div></section>'
    return {"route": TOOLS["ask-the-estimator"]["route"], "title": "Ask the Estimator – Real Questions From Kissimmee Estimates", "meta_description": "Anonymized real questions from estimating calls and forms in Kissimmee, St. Cloud, Poinciana and the Polk ridge, answered in a few sentences with a link to the full page. Updated as questions come in; RSS feed available.", "h1": "Ask the Estimator", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Ask the Estimator", None)], "body_html": body, "kind": "tool", "nav_active": "/tools/", "changelog": ["2026-09-10 — first six entries"]}


def brief():
    body = sec("Write a one-page brief so three contractors quote the same job",
        cap("Fill in the job; the tool writes a brief with dimensions, current surface, spec we would propose, drainage and access notes, HOA and permit position, and the questions to ask every bidder. Copy it into emails or print it. It makes low quotes explain what they left out and high quotes explain what they added."),
        eyebrow="Project Brief Generator")
    body += '''
<section><div class="wrap">
<form class="tool" id="pb" onsubmit="return false">
  <div class="row-2">
    <div class="field"><label for="b-work">Work</label><select id="b-work"><option>Concrete driveway (new or replacement)</option><option>Paver driveway</option><option>Concrete patio / lanai extension</option><option>Paver patio</option><option>Pool deck (paver or travertine overlay)</option><option>Concrete pad (shed, RV, generator, hot tub)</option><option>Walkway or steps</option><option>Concrete repair</option><option>Paver sealing / repair</option><option>Garage floor coating</option></select></div>
    <div class="field"><label for="b-city">City or community</label><input id="b-city" type="text" placeholder="e.g. Buenaventura Lakes, Kissimmee"></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="b-len">Length (ft)</label><input id="b-len" type="number" min="1" step="0.5" inputmode="decimal"></div>
    <div class="field"><label for="b-wid">Width (ft)</label><input id="b-wid" type="number" min="1" step="0.5" inputmode="decimal"></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="b-cur">Current surface</label><select id="b-cur"><option>Concrete, cracked / settled</option><option>Concrete, sound</option><option>Pavers, settled</option><option>Pavers, sound</option><option>Asphalt</option><option>Grass / dirt (new)</option></select></div>
    <div class="field"><label for="b-load">Loads</label><select id="b-load"><option>Cars and SUVs</option><option>Boat trailer or RV</option><option>Foot traffic only</option><option>Delivery / commercial trucks</option></select></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="b-hoa">HOA / ARC</label><select id="b-hoa"><option>Yes, approval required</option><option>No HOA</option><option>Not sure</option></select></div>
    <div class="field"><label for="b-jur">Jurisdiction (use the permit finder)</label><select id="b-jur"><option>City of Kissimmee</option><option>Unincorporated Osceola County</option><option>City of St. Cloud</option><option>Unincorporated Polk County</option><option>Orange County</option><option>Other / not sure</option></select></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="b-drain">Drainage observed</label><select id="b-drain"><option>Water pools at the garage or house</option><option>Downspout discharges at the slab edge</option><option>Sprinklers hit the surface (rust)</option><option>Drains fine</option><option>Not sure</option></select></div>
    <div class="field"><label for="b-access">Access</label><select id="b-access"><option>Open street access</option><option>Gated community</option><option>Alley-loaded garage</option><option>Rural lot, long driveway</option><option>Rental: turnover windows</option></select></div>
  </div>
  <div class="field"><label for="b-notes">Anything else (trees, septic, pool, timeline)</label><textarea id="b-notes" rows="3"></textarea></div>
  <div class="cta-row"><button class="btn btn-primary" id="b-go" type="button">Generate the brief</button><button class="btn btn-outline" type="button" data-copy-target="#b-out">Copy</button><button class="btn btn-outline" type="button" id="b-print">Print</button></div>
  <div class="result" id="b-result" hidden><pre id="b-out" style="white-space:pre-wrap;font-family:var(--body);margin:0"></pre></div>
</form>
</div></section>
<script>
(function(){
function q(s){return document.querySelector(s);}
function spec(w,load){
 if(w.indexOf('Concrete driveway')===0||w.indexOf('Concrete pad')===0){return (load.indexOf('Boat')===0||load.indexOf('Delivery')===0)?'6 in, 4,000 psi, fiber, #4 rebar grid at 18 in on chairs, 4–6 in compacted limerock base, joints at 12–15 ft cut within 12 h':'4 in, 3,000–3,500 psi, fiber, #4 rebar at edges and re-entrant corners, 4 in compacted limerock base, joints at 10 ft cut within 12 h';}
 if(w.indexOf('Paver driveway')===0){return '80 mm concrete pavers, 6 in compacted limerock base in two lifts, 1 in bedding sand, edge restraint on the base, polymeric sand vibrated in, concrete apron at the street to the jurisdiction detail';}
 if(w.indexOf('Concrete patio')===0){return '4 in, 3,000 psi, fiber, 2–4 in compacted base, slope ≥ 1/8 in per ft away from the house, doweled to existing slab with expansion joint';}
 if(w.indexOf('Paver patio')===0){return '60 mm pavers, 4–5 in compacted base, 1 in bedding sand, edge restraint, polymeric sand, slope away from the house';}
 if(w.indexOf('Pool deck')===0){return '1 in remodel pavers or 1/2 in travertine thin-set over a sound deck (tap and string-line tested), new bullnose coping on the bond beam with expansion joint, channel drain at the screen line, anti-slip penetrating sealer';}
 if(w.indexOf('Walkway')===0){return '4 in concrete or 60 mm pavers, 4 in base, edge restraint both sides, cross-slope 1/8–1/4 in per ft, riser heights within 1/4 in';}
 if(w.indexOf('Concrete repair')===0){return 'Cause identified first (water, roots, base); routed and sealed cracks, or panel removed and replaced on a rebuilt base, doweled, expansion joint at the garage';}
 if(w.indexOf('Paver sealing')===0){return 'Clean at 2,500–3,000 psi with a wide tip, efflorescence/rust treated, 24–48 h dry, polymeric re-sand vibrated in, two thin coats of sealer (penetrating on stone), anti-slip additive on decks';}
 if(w.indexOf('Garage')===0){return 'Moisture test, diamond grind, crack repair, epoxy or polyaspartic base coat, full flake broadcast, polyaspartic top coat with anti-slip';}
 return '';
}
q('#b-go').addEventListener('click',function(){
 var w=q('#b-work').value,c=q('#b-city').value||'(city)',L=q('#b-len').value,W=q('#b-wid').value,cur=q('#b-cur').value,load=q('#b-load').value,hoa=q('#b-hoa').value,jur=q('#b-jur').value,dr=q('#b-drain').value,ac=q('#b-access').value,notes=q('#b-notes').value;
 var area=(L&&W)?(parseFloat(L)*parseFloat(W)).toLocaleString('en-US')+' sq ft ('+L+' × '+W+' ft)':'(dimensions)';
 var t='PROJECT BRIEF — '+w+'\\nLocation: '+c+'\\nGenerated: '+new Date().toISOString().slice(0,10)+' with the Kissimmee Concrete project brief tool\\n\\n'+
 'SIZE: '+area+'\\nCURRENT SURFACE: '+cur+'\\nLOADS: '+load+'\\nDRAINAGE OBSERVED: '+dr+'\\nACCESS: '+ac+'\\nHOA / ARC: '+hoa+'\\nJURISDICTION: '+jur+'\\n'+(notes?'NOTES: '+notes+'\\n':'')+
 '\\nSPECIFICATION TO QUOTE (each bidder to confirm or state their alternative):\\n'+spec(w,load)+'\\n\\n'+
 'EACH QUOTE MUST STATE:\\n1. Thickness, PSI/mix, reinforcement type and how it is held in position\\n2. Base material, depth, compaction method and whether the subgrade is proof-rolled\\n3. Joint layout and when joints are cut\\n4. Drainage: slope direction, drains, downspout handling\\n5. What happens to the existing surface (removal, haul-off, reuse)\\n6. Apron / right-of-way detail and who pulls the permit\\n7. HOA packet: who prepares and submits it\\n8. Sealing: included or later, product type\\n9. Exclusions (fill, roots, pump truck, drains, permit fees)\\n10. Schedule, weather plan, cure time before use\\n11. Written workmanship warranty terms\\n12. Legal entity name, insurance certificate, Sunbiz registration (no state license exists for this work: s. 489.117(4)(a))\\n\\n'+
 'COMPARE ON: same spec, same exclusions, same warranty. A low number that skips base or steel is not the same job.';
 q('#b-out').textContent=t;q('#b-result').hidden=false;if(window.kcTrack)window.kcTrack('tool_project_brief',{work:w});
});
q('#b-print').addEventListener('click',function(){q('#b-go').click();window.print();});
})();
</script>'''
    body += sec("Why a brief", f"<p>Most bad outcomes we get called to fix trace to a quote that was cheaper because it left out base, steel or drainage, and nobody could tell because the quotes described different jobs. A brief that fixes the spec makes the comparison honest. Pair it with the {tool('concrete-paver-calculator')} for a planning range and the {tool('permit-finder')} for the office. How to check a contractor without a license number: {guide('how-to-verify-a-concrete-contractor-florida')}.</p>", cls="alt")
    faqs = [
        faq("Does the brief get sent to you?", "No. It stays in your browser until you copy or print it; send it to whoever you are getting quotes from, including us."),
        faq("Is the spec in the brief the only right one?", "It is the spec we would propose for the loads and surface you chose; another contractor may propose an alternative, and the brief asks them to say so."),
        faq("Can Realtors and property managers use it?", "Yes; it was built for exactly that."),
    ]
    return {"route": TOOLS["project-brief"]["route"], "title": "Project Brief Generator – Get Comparable Concrete & Paver Quotes", "meta_description": "Generate a one-page brief for a driveway, patio, pool deck, pad, walkway, repair, sealing or garage-floor job with dimensions, spec, drainage, access, HOA and permit notes and twelve questions every bidder must answer.", "h1": "Project brief generator", "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Project brief", None)], "body_html": body, "faqs": faqs, "kind": "tool", "nav_active": "/tools/", "sources": ["fs489117"]}


def get_pages():
    return [hub(), permit_finder(), calculator(), decision(), hoa_checklist(), pour_calendar(), ask(), brief()]
