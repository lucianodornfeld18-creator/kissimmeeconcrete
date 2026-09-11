# -*- coding: utf-8 -*-
"""Shared scaffolding for city×service pages. All prose lives in the content_cityservice_* modules."""
from _data import SERVICES, CITIES, COST_INDEX_RELEASE, city_service_route, drive_estimate
from _helpers import cap, sec, table, svc, city, tool, guide, compare, juris, hoa, faq, cost_rows, cost_range, related, cs, esc


def cs_page(city_key, service_key, title, desc, quick, sections, example, local_q, faqs, sources, related_links=None):
    """quick: capsule text; sections: list of (h2, html); example: (h2, html); local_q: (question_h2, capsule_text)."""
    c, s = CITIES[city_key], SERVICES[service_key]
    body = sec(f"The short version for {c['name']}", cap(quick), eyebrow=f"{c['name']} · {c['county']} County")
    for i, (h2, html) in enumerate(sections):
        body += sec(h2, html, cls="alt" if i % 2 == 0 else "")
    body += sec(example[0], example[1], cls="alt" if len(sections) % 2 == 0 else "", eyebrow="Worked example")
    body += sec(local_q[0], cap(local_q[1]))
    links = [svc(service_key, f"{s['name']} (Kissimmee master page)"), city(city_key, f"{c['name']} area guide")] + (related_links or [])
    body += sec("Related pages", related(links))
    if c["miles"]:
        body += f'<div class="wrap"><p class="note">Straight-line distance from downtown Kissimmee: {c["miles"]} miles; drive estimate about {drive_estimate(c["miles"])} minutes. Source for distance: Census 2024 Gazetteer internal point.</p></div>'
    return {
        "route": city_service_route(city_key, service_key),
        "title": title, "meta_description": desc,
        "h1": f"{s['name']} in {c['name']}, FL",
        "breadcrumbs": [("Home", "/"), ("Concrete" if s["pillar"] == "concrete" else "Pavers", "/concrete/" if s["pillar"] == "concrete" else "/pavers/"), (s["name"], s["route"]), (c["name"], None)],
        "body_html": body, "faqs": faqs, "kind": "cityservice", "service_key": service_key, "city_key": city_key,
        "nav_active": "/concrete/" if s["pillar"] == "concrete" else "/pavers/", "sources": sources,
    }
