# -*- coding: utf-8 -*-
"""Per-route extra sections and FAQs, merged into pages by templates.render_page.

Keeping these out of the page builders lets a page's local depth grow without
touching the module that defines its route, title and schema. Keys are routes.
Every block here is written for that one route; nothing is generated from a
template with a city name substituted.

Several modules may contribute to the same route, so blocks are concatenated in
module order rather than overwriting one another.
"""
EXTRA_SECTIONS = {}
EXTRA_FAQS = {}

_MODULES = (
    "extra_cityservice_a", "extra_cityservice_b", "extra_cityservice_c", "extra_cityservice_d",
    "extra_services", "extra_areas", "extra_misc", "extra_topups", "extra_final", "extra_final2",
)

for _mod in _MODULES:
    try:
        _m = __import__(_mod)
    except ImportError:
        continue
    for _route, _html in getattr(_m, "SECTIONS", {}).items():
        EXTRA_SECTIONS[_route] = EXTRA_SECTIONS.get(_route, "") + _html
    for _route, _faqs in getattr(_m, "FAQS", {}).items():
        EXTRA_FAQS[_route] = EXTRA_FAQS.get(_route, []) + list(_faqs)
