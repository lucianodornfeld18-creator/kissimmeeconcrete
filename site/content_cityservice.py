# -*- coding: utf-8 -*-
"""Aggregates the 44 city×service pages and checks them against _data.CITY_SERVICES."""
from _data import CITY_SERVICES, city_service_route
import content_cityservice_a
import content_cityservice_b
import content_cityservice_c


def get_pages():
    pages = content_cityservice_a.get_pages() + content_cityservice_b.get_pages() + content_cityservice_c.get_pages()
    expected = {city_service_route(c, s) for c, s in CITY_SERVICES}
    got = {p["route"] for p in pages}
    missing = expected - got
    extra = got - expected
    if missing or extra:
        raise SystemExit(f"[cityservice] missing={sorted(missing)} extra={sorted(extra)}")
    return pages
