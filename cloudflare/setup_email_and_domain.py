# -*- coding: utf-8 -*-
"""Finish the Cloudflare side for kissimmeeconcrete.com.

Three steps, safe to re-run:

  1. Clear what the registrar's parking service left in the zone: the A records
     on the apex, www and the wildcard that point at the Afternic lander, the
     null MX records (`0 .`) that block Email Routing, the `v=spf1 -all` TXT
     records, and the NS records that delegate a long list of subdomains back
     to ns1/ns2.afternic.com.
  2. Point the apex and www at the Pages project and wait for the certificates.
  3. Enable Email Routing, forward hello@kissimmeeconcrete.com to the marketing
     inbox and turn on the catch-all, matching windermereconcrete.com.

Tokens: DNS work needs a token with Zone.DNS:Edit, passed as CF_API_TOKEN.
Pages and Email Routing work with the wrangler OAuth session. Each call tries
CF_API_TOKEN first and falls back to the wrangler token on an auth error, so
either a single broad token or the two together will do.
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
PARKING_IPS = {"13.248.169.48", "76.223.54.146", "172.67.147.196", "104.21.28.230"}
API = "https://api.cloudflare.com/client/v4"


def _wrangler_token():
    cfg = pathlib.Path(os.path.expanduser("~/.wrangler/config/default.toml"))
    if not cfg.exists():
        return None
    for line in cfg.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("oauth_token"):
            return line.split("=", 1)[1].strip().strip('"')
    return None


TOKENS = [t for t in (os.environ.get("CF_API_TOKEN") or os.environ.get("CLOUDFLARE_API_TOKEN"), _wrangler_token()) if t]
if not TOKENS:
    raise SystemExit("no Cloudflare token: set CF_API_TOKEN or log in with wrangler")


def call(method, path, body=None):
    """Try each token in turn; an auth error falls through to the next one."""
    url = path if path.startswith("http") else API + path
    last = None
    for tok in TOKENS:
        r = urllib.request.Request(
            url, data=json.dumps(body).encode() if body is not None else None,
            method=method, headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
        try:
            return json.loads(urllib.request.urlopen(r, timeout=90).read())
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            try:
                last = json.loads(raw or "{}")
            except Exception:
                last = {"success": False, "errors": [{"code": e.code, "message": raw[:200]}]}
            codes = {str(x.get("code")) for x in (last.get("errors") or [])}
            if not ({"10000", "9109", "1000"} & codes):
                return last
    return last


def errs(r):
    return json.dumps((r or {}).get("errors"))[:220]


ACCOUNT_ID = "21cabe20549f2f63baa4d3fd781abe74"


def account_id():
    """The DNS-scoped token cannot list accounts, so prefer the known id."""
    if ACCOUNT_ID:
        return ACCOUNT_ID
    res = (call("GET", "/accounts") or {}).get("result") or []
    if not res:
        raise SystemExit("no account visible to these tokens; set ACCOUNT_ID")
    return res[0]["id"]


def is_parking(rec):
    typ, name, content = rec["type"], rec["name"], (rec.get("content") or "").strip().strip('"')
    if typ in ("A", "AAAA") and content in PARKING_IPS:
        return True
    if typ == "MX" and content in (".", ""):
        return True
    if typ == "TXT" and content.startswith("v=spf1") and "cloudflare" not in content:
        return True
    if typ == "NS" and content.rstrip(".").endswith("afternic.com") and name != ZONE:
        return True
    if typ == "CNAME" and name in (ZONE, "www." + ZONE) and PAGES_HOST not in content:
        return True
    return False


def step1_clear_parking_dns():
    print("1. clearing the registrar parking DNS")
    r = call("GET", f"/zones/{ZID}/dns_records?per_page=500")
    if not r.get("success"):
        print("   cannot read DNS: %s" % errs(r))
        print("   -> set CF_API_TOKEN to a token with Zone.DNS:Edit on " + ZONE)
        return False
    targets = [x for x in r["result"] if is_parking(x)]
    print("   %d of %d records look like parking leftovers" % (len(targets), len(r["result"])))
    by_type = {}
    removed = failed = 0
    for rec in targets:
        d = call("DELETE", f"/zones/{ZID}/dns_records/{rec['id']}")
        if d.get("success"):
            removed += 1
            by_type[rec["type"]] = by_type.get(rec["type"], 0) + 1
        else:
            failed += 1
            print("   FAILED %-5s %-34s %s" % (rec["type"], rec["name"], errs(d)))
    print("   removed %d (%s)%s" % (removed, ", ".join("%s x%d" % (k, v) for k, v in sorted(by_type.items())),
                                    ", %d failed" % failed if failed else ""))
    left = call("GET", f"/zones/{ZID}/dns_records?per_page=500").get("result") or []
    print("   %d record(s) remain: %s" % (len(left), ", ".join(sorted({x["type"] for x in left})) or "none"))
    return True


def step2_point_at_pages():
    print("2. pointing the apex and www at Pages")
    acc = account_id()
    for host in (ZONE, "www." + ZONE):
        r = call("POST", f"/accounts/{acc}/pages/projects/{PROJECT}/domains", {"name": host})
        print("   attach %-30s %s" % (host, "ok" if r.get("success") else errs(r)[:90]))

    cur = call("GET", f"/zones/{ZID}/dns_records?per_page=500").get("result") or []
    have = {(x["type"], x["name"]): x for x in cur}
    for host in (ZONE, "www." + ZONE):
        existing = have.get(("CNAME", host))
        if existing and PAGES_HOST in (existing.get("content") or ""):
            print("   CNAME already set for", host); continue
        c = call("POST", f"/zones/{ZID}/dns_records",
                 {"type": "CNAME", "name": host, "content": PAGES_HOST, "proxied": True, "ttl": 1})
        print("   CNAME %-30s -> %-32s %s" % (host, PAGES_HOST, "ok" if c.get("success") else errs(c)[:90]))

    print("   waiting for the certificates")
    for _ in range(24):
        time.sleep(15)
        d = call("GET", f"/accounts/{acc}/pages/projects/{PROJECT}/domains")
        rows = [(x["name"], x.get("status")) for x in (d.get("result") or [])]
        print("     " + " | ".join("%s=%s" % r for r in rows))
        if rows and all(s == "active" for _, s in rows):
            print("   both domains active")
            return True
    print("   still provisioning; certificates can take a few more minutes")
    return True


def step3_email_routing():
    print("3. enabling Email Routing")
    r = call("POST", f"/zones/{ZID}/email/routing/enable", {})
    if r.get("success"):
        print("   routing enabled")
    elif "already" in errs(r).lower() or "enabled" in errs(r).lower():
        print("   routing already enabled")
    else:
        print("   enable ->", errs(r))
        if "MX" in errs(r):
            return False

    addr = f"{LOCAL_PART}@{ZONE}"
    rules = call("GET", f"/zones/{ZID}/email/routing/rules?per_page=50").get("result") or []
    if any(any(m.get("value") == addr for m in (x.get("matchers") or [])) for x in rules):
        print("   rule for %s already exists" % addr)
    else:
        c = call("POST", f"/zones/{ZID}/email/routing/rules", {
            "name": "Forward %s" % addr, "enabled": True,
            "matchers": [{"type": "literal", "field": "to", "value": addr}],
            "actions": [{"type": "forward", "value": [DESTINATION]}]})
        print("   rule %s -> %s  %s" % (addr, DESTINATION, "ok" if c.get("success") else errs(c)))

    ca = call("PUT", f"/zones/{ZID}/email/routing/rules/catch_all", {
        "name": "Forward all Kissimmee Concrete email", "enabled": True,
        "matchers": [{"type": "all"}],
        "actions": [{"type": "forward", "value": [DESTINATION]}]})
    print("   catch-all -> %s  %s" % (DESTINATION, "ok" if ca.get("success") else errs(ca)))

    s = call("GET", f"/zones/{ZID}/email/routing")
    res = s.get("result") or {}
    print("   status: enabled=%s state=%s" % (res.get("enabled"), res.get("status")))
    return True


def main():
    print("tokens available: %d\n" % len(TOKENS))
    if not step1_clear_parking_dns():
        return 1
    step2_point_at_pages()
    step3_email_routing()
    print("\nDone. Check https://%s/ and send a test message to %s@%s" % (ZONE, LOCAL_PART, ZONE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
