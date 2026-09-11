# -*- coding: utf-8 -*-
"""Finish the Cloudflare side for kissimmeeconcrete.com.

Does three things, in order, and is safe to re-run:

  1. Clears the DNS left over from the registrar parking page: the apex A
     records pointing at the lander, the www record, the null MX (`0 .`) and
     the `v=spf1 -all` TXT. The null MX is what blocks Email Routing.
  2. Points the apex and www at the Pages project, then waits for the two
     custom domains to go active.
  3. Enables Email Routing, forwards hello@kissimmeeconcrete.com to
     opusdigitalmarketingflorida@gmail.com and turns on the catch-all, which is
     how windermereconcrete.com is set up.

Needs a token with Zone.DNS:Edit on this zone, plus the account-level Pages and
Email Routing permissions the wrangler session already has:

  CF_API_TOKEN=...  python cloudflare/setup_email_and_domain.py

Without CF_API_TOKEN it falls back to the wrangler OAuth token, which can do
everything here except edit DNS, and will stop at step 1 with a clear message.
"""
import json
import os
import pathlib
import sys
import time
import urllib.request

ZONE = "kissimmeeconcrete.com"
ZID = "119c4f7fd17ba423f83520196bdacd8d"
PROJECT = "kissimmeeconcrete"
PAGES_HOST = "kissimmeeconcrete.pages.dev"
DESTINATION = "opusdigitalmarketingflorida@gmail.com"
LOCAL_PART = "hello"

API = "https://api.cloudflare.com/client/v4"


def token():
    t = os.environ.get("CF_API_TOKEN") or os.environ.get("CLOUDFLARE_API_TOKEN")
    if t:
        return t.strip(), "CF_API_TOKEN"
    cfg = pathlib.Path(os.path.expanduser("~/.wrangler/config/default.toml"))
    for line in cfg.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("oauth_token"):
            return line.split("=", 1)[1].strip().strip('"'), "wrangler OAuth"
    raise SystemExit("no Cloudflare token available")


TOK, TOK_SRC = token()
H = {"Authorization": "Bearer " + TOK, "Content-Type": "application/json"}


def call(method, path, body=None):
    url = path if path.startswith("http") else API + path
    r = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                               method=method, headers=H)
    try:
        return json.loads(urllib.request.urlopen(r, timeout=90).read())
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        try:
            return json.loads(raw or "{}")
        except Exception:
            return {"success": False, "errors": [{"code": e.code, "message": raw[:200]}]}


def errs(r):
    return json.dumps(r.get("errors"))[:220]


def account_id():
    r = call("GET", "/accounts")
    return r["result"][0]["id"]


def step1_clear_parking_dns():
    print("1. clearing the registrar parking DNS")
    r = call("GET", f"/zones/{ZID}/dns_records?per_page=200")
    if not r.get("success"):
        print("   cannot read DNS with the %s token: %s" % (TOK_SRC, errs(r)))
        print("   -> re-run with CF_API_TOKEN set to a token that has Zone.DNS:Edit on " + ZONE)
        return False
    removed = 0
    for rec in r["result"]:
        name, typ, content = rec["name"], rec["type"], (rec.get("content") or "")
        drop = (
            (typ in ("A", "AAAA") and name in (ZONE, "www." + ZONE))
            or (typ == "CNAME" and name in (ZONE, "www." + ZONE) and PAGES_HOST not in content)
            or (typ == "MX")
            or (typ == "TXT" and name == ZONE and content.strip('"').startswith("v=spf1") and "cloudflare" not in content)
        )
        if drop:
            d = call("DELETE", f"/zones/{ZID}/dns_records/{rec['id']}")
            print("   %s %-6s %-30s %s" % ("removed" if d.get("success") else "FAILED ", typ, name, content[:40]))
            removed += bool(d.get("success"))
    print("   %d record(s) removed" % removed)
    return True


def step2_point_at_pages():
    print("2. pointing the apex and www at Pages")
    acc = account_id()
    for host in (ZONE, "www." + ZONE):
        r = call("POST", f"/accounts/{acc}/pages/projects/{PROJECT}/domains", {"name": host})
        if r.get("success"):
            print("   attached", host)
        else:
            msg = errs(r)
            print("   %s already attached or: %s" % (host, msg) if "already" in msg.lower() else "   %s -> %s" % (host, msg))
    # a CNAME to the pages.dev host is what actually routes traffic
    cur = call("GET", f"/zones/{ZID}/dns_records?per_page=200")
    have = {(x["type"], x["name"]) for x in (cur.get("result") or [])}
    for host in (ZONE, "www." + ZONE):
        if ("CNAME", host) in have:
            print("   CNAME already present for", host); continue
        c = call("POST", f"/zones/{ZID}/dns_records",
                 {"type": "CNAME", "name": host, "content": PAGES_HOST, "proxied": True, "ttl": 1})
        print("   CNAME %-30s -> %s  %s" % (host, PAGES_HOST, "ok" if c.get("success") else errs(c)))

    print("   waiting for the certificates")
    for i in range(20):
        time.sleep(15)
        d = call("GET", f"/accounts/{acc}/pages/projects/{PROJECT}/domains")
        rows = [(x["name"], x.get("status")) for x in (d.get("result") or [])]
        print("     " + " | ".join("%s=%s" % r for r in rows))
        if rows and all(s == "active" for _, s in rows):
            print("   both domains active"); return True
    print("   still provisioning; certificates can take a few more minutes")
    return True


def step3_email_routing():
    print("3. enabling Email Routing")
    r = call("POST", f"/zones/{ZID}/email/routing/enable", {})
    if not r.get("success") and "already" not in errs(r).lower():
        print("   enable ->", errs(r))
        if "MX" in errs(r):
            print("   -> a non-Cloudflare MX record is still present; step 1 must run first")
            return False
    else:
        print("   routing enabled")

    addr = f"{LOCAL_PART}@{ZONE}"
    rules = call("GET", f"/zones/{ZID}/email/routing/rules?per_page=50").get("result") or []
    if any(any(m.get("value") == addr for m in (x.get("matchers") or [])) for x in rules):
        print("   rule for %s already exists" % addr)
    else:
        c = call("POST", f"/zones/{ZID}/email/routing/rules", {
            "name": "Forward %s" % addr,
            "enabled": True,
            "matchers": [{"type": "literal", "field": "to", "value": addr}],
            "actions": [{"type": "forward", "value": [DESTINATION]}],
        })
        print("   rule %s -> %s  %s" % (addr, DESTINATION, "ok" if c.get("success") else errs(c)))

    ca = call("PUT", f"/zones/{ZID}/email/routing/rules/catch_all", {
        "name": "Forward all Kissimmee Concrete email",
        "enabled": True,
        "matchers": [{"type": "all"}],
        "actions": [{"type": "forward", "value": [DESTINATION]}],
    })
    print("   catch-all -> %s  %s" % (DESTINATION, "ok" if ca.get("success") else errs(ca)))
    return True


def main():
    print("token source: %s\n" % TOK_SRC)
    ok = step1_clear_parking_dns()
    if not ok:
        print("\nstopping: DNS edit permission is required before the rest can run.")
        return 1
    step2_point_at_pages()
    step3_email_routing()
    print("\nDone. Verify: https://%s/ and send a test message to %s@%s" % (ZONE, LOCAL_PART, ZONE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
