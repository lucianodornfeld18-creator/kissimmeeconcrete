# -*- coding: utf-8 -*-
"""HTML helpers shared by the content modules."""
from _data import (SERVICES, CITIES, TOOLS, GUIDES, COMPARISONS, JURISDICTIONS, HOAS, CONCRETE_SERVICES, PAVER_SERVICES, COATING_SERVICES,
                   PHONE_E164, PHONE_DISPLAY, BUSINESS, TURNSTILE_SITE_KEY, COST_INDEX, COST_INDEX_RELEASE, drive_estimate, city_service_route, CITY_SERVICES, src)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def cap(*paras):
    """Answer capsule: 40-70 words, self-contained, placed right under a question H2."""
    return '<div class="capsule">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def sec(h2, inner, cls="", eyebrow=None, hid=None):
    eb = f'<span class="eyebrow">{esc(eyebrow)}</span>' if eyebrow else ""
    idattr = f' id="{hid}"' if hid else ""
    return f'<section class="{cls}"{idattr}><div class="wrap">{eb}<h2>{h2}</h2>{inner}</div></section>'


def table(headers, rows, caption=None):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    cap_html = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="table-wrap"><table>{cap_html}<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def cards(items, cols=3):
    """items: list of (title, text_html, href, link_label)"""
    out = []
    for title, text, href, label in items:
        out.append(f'<article class="card"><h3><a href="{href}" style="text-decoration:none;color:inherit">{esc(title)}</a></h3><p>{text}</p><a class="card-link" href="{href}">{esc(label)} &rarr;</a></article>')
    return f'<div class="grid grid-{cols}">{"".join(out)}</div>'


def steps(items):
    return '<ol class="steps">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def callout(html, kind=""):
    return f'<div class="callout {kind}">{html}</div>'


def svc(key, label=None):
    s = SERVICES[key]
    return f'<a href="{s["route"]}">{esc(label or s["name"])}</a>'


def city(key, label=None):
    c = CITIES[key]
    return f'<a href="{c["route"]}">{esc(label or c["name"])}</a>'


def tool(key, label=None):
    t = TOOLS[key]
    return f'<a href="{t["route"]}">{esc(label or t["name"])}</a>'


def guide(key, label=None):
    g = GUIDES[key]
    return f'<a href="{g["route"]}">{esc(label or g["name"])}</a>'


def compare(key, label=None):
    c = COMPARISONS[key]
    return f'<a href="{c["route"]}">{esc(label or c["name"])}</a>'


def juris(key, label=None):
    j = JURISDICTIONS[key]
    return f'<a href="{j["route"]}">{esc(label or j["name"])}</a>'


def hoa(key, label=None):
    h = HOAS[key]
    return f'<a href="{h["route"]}">{esc(label or h["name"])}</a>'


def cs(city_key, service_key, label=None):
    return f'<a href="{city_service_route(city_key, service_key)}">{esc(label or (SERVICES[service_key]["name"] + " in " + CITIES[city_key]["name"]))}</a>'


def city_services_for(city_key):
    return [s for c, s in CITY_SERVICES if c == city_key]


def cities_for_service(service_key):
    return [c for c, s in CITY_SERVICES if s == service_key]


def cost_rows(keys):
    rows = []
    for k, name, unit, lo, hi, note in COST_INDEX:
        if k in keys:
            rows.append((name, unit, f"${lo:,.2f}" if lo < 100 else f"${lo:,.0f}", f"${hi:,.2f}" if hi < 100 else f"${hi:,.0f}", note or "&nbsp;"))
    return table(["Item", "Unit", "Low", "High", "Notes"], rows, caption=f"Kissimmee Concrete Cost Index, {COST_INDEX_RELEASE['label']} release ({COST_INDEX_RELEASE['date']}). Installed planning ranges for the Kissimmee/Osceola market, not quotes. Method: <a href='/data-and-methods/'>Data &amp; methods</a>.")


def cost_range(key):
    for k, name, unit, lo, hi, note in COST_INDEX:
        if k == key:
            f = (lambda v: f"${v:,.2f}") if lo < 100 else (lambda v: f"${v:,.0f}")
            return f"{f(lo)}–{f(hi)} per {unit}"
    return ""


def phone_cta(text="Call"):
    if PHONE_E164:
        return f'<a class="btn btn-outline" href="tel:{PHONE_E164}">{text} {esc(PHONE_DISPLAY)}</a>'
    return ""


def lead_form(heading="Request a free on-site estimate", service_default=None, compact=False):
    def opts(keys):
        return "".join(f'<option value="{esc(SERVICES[k]["name"])}"{" selected" if k == service_default else ""}>{esc(SERVICES[k]["name"])}</option>' for k in keys)
    service_opts = (f'<option value="">Select a service</option><optgroup label="Concrete">{opts(CONCRETE_SERVICES)}</optgroup>'
                    f'<optgroup label="Pavers &amp; hardscape">{opts(PAVER_SERVICES)}</optgroup><optgroup label="Coatings">{opts(COATING_SERVICES)}</optgroup>'
                    '<option value="Not sure yet">Not sure yet</option>')
    turnstile = (f'<div class="cf-turnstile" data-sitekey="{esc(TURNSTILE_SITE_KEY)}"></div><script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>') if TURNSTILE_SITE_KEY else ""
    hidden = "".join(f'<input type="hidden" name="{n}" value="">' for n in ["hub_id", "page_url", "referrer", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "client_ts"])
    extra = "" if compact else f'''
      <div class="row-2">
        <div class="field"><label for="f-prop">Property type</label><select id="f-prop" name="property_type"><option value="">Select</option><option>Primary home</option><option>Vacation rental / second home</option><option>Rental I manage</option><option>Commercial / HOA / business</option><option>New construction</option></select></div>
        <div class="field"><label for="f-time">Timeline</label><select id="f-time" name="timeline"><option value="">Select</option><option>As soon as possible</option><option>Within 1–3 months</option><option>3–6 months</option><option>Planning ahead / just pricing</option></select></div>
      </div>
      <div class="field"><label for="f-photo">Photo of the area (optional, under 6 MB)</label><input id="f-photo" type="file" name="photo" accept="image/*"></div>'''
    return f'''
<form class="lead" method="post" action="/api/contact" enctype="multipart/form-data" novalidate>
  <h2 style="margin-top:0;font-size:1.25rem">{esc(heading)}</h2>
  <div class="row-2">
    <div class="field"><label for="f-name">Name</label><input id="f-name" type="text" name="name" autocomplete="name" required maxlength="100"></div>
    <div class="field"><label for="f-phone">Phone</label><input id="f-phone" type="tel" name="phone" autocomplete="tel" required maxlength="40" inputmode="tel"></div>
  </div>
  <div class="row-2">
    <div class="field"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" type="email" name="email" autocomplete="email" maxlength="254"></div>
    <div class="field"><label for="f-zip">ZIP code of the project</label><input id="f-zip" type="text" name="zip" autocomplete="postal-code" inputmode="numeric" pattern="[0-9]{{5}}" maxlength="5" placeholder="34741" required></div>
  </div>
  <div class="field"><label for="f-service">Service</label><select id="f-service" name="service">{service_opts}</select></div>{extra}
  <div class="field"><label for="f-msg">Project notes (size, current surface, HOA, anything else)</label><textarea id="f-msg" name="message" maxlength="3000"></textarea></div>
  <div class="hp" aria-hidden="true"><label for="f-company">Company</label><input id="f-company" type="text" name="company" tabindex="-1" autocomplete="off"></div>
  {hidden}
  {turnstile}
  <button class="btn btn-primary" type="submit">Send my request</button>
  <p class="note" style="margin:10px 0 0">We reply during business hours, {esc(BUSINESS["hours"])}. Estimates are free and in writing.</p>
</form>'''


def faq(q, a_html):
    return {"q": q, "a": a_html if a_html.strip().startswith("<") else f"<p>{a_html}</p>"}


def drive(city_key):
    return f"about {drive_estimate(CITIES[city_key]['miles'])} minutes"


def related(links):
    """links: list of html anchors -> pill nav"""
    return '<ul class="pill-nav">' + "".join(f"<li>{l}</li>" for l in links) + "</ul>"
