// Cloudflare Pages Function — POST /api/contact (kissimmeeconcrete.com)
// Validates the lead form server-side, checks honeypot + Turnstile + a KV rate
// limit, then hands the lead to the contact-email Worker (service binding).
// No PII is logged. Attribution fields (hub_id, page_url, utm_*, referrer) travel with the lead.

const HUB_ID = "kissimmee";
const MAX_FORM_BYTES = 7_000_000; // allows one photo up to ~6 MB
const MAX_PHOTO_BYTES = 6 * 1024 * 1024;
const LIMITS = { name: 100, phone: 40, email: 254, city: 120, service: 120, property_type: 60, timeline: 60, language: 10, message: 3000, page_url: 300, referrer: 300, utm_source: 120, utm_medium: 120, utm_campaign: 120, utm_term: 120, utm_content: 120, gclid: 200, client_ts: 40 };

function isAllowedOrigin(origin) {
  if (!origin) return true;
  try {
    const { hostname, protocol } = new URL(origin);
    if (protocol !== "https:" && hostname !== "localhost" && hostname !== "127.0.0.1") return false;
    return hostname === "kissimmeeconcrete.com" || hostname === "www.kissimmeeconcrete.com" || hostname === "kissimmeeconcrete.pages.dev" || hostname.endsWith(".kissimmeeconcrete.pages.dev") || hostname === "localhost" || hostname === "127.0.0.1";
  } catch { return false; }
}
function field(form, name) { const v = form.get(name); return typeof v === "string" ? v.trim() : ""; }
function text(message, status) { return new Response(message, { status, headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" } }); }

function validate(p) {
  if (!p.name || p.name.length > LIMITS.name) return "Please enter your name.";
  if (!p.phone || p.phone.length > LIMITS.phone || !/\d{7,}/.test(p.phone.replace(/\D/g, ""))) return "Please enter a phone number we can reach you at.";
  if (!p.email || p.email.length > LIMITS.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(p.email)) return "Please enter a valid email address.";
  for (const k of Object.keys(LIMITS)) if ((p[k] || "").length > LIMITS[k]) return "One of the fields is too long.";
  return null;
}

async function verifyTurnstile(token, secret, ip) {
  if (!secret) return { ok: true, skipped: true };
  if (!token) return { ok: false };
  const body = new URLSearchParams({ secret, response: token });
  if (ip) body.set("remoteip", ip);
  try {
    const r = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" }, body });
    const j = await r.json();
    return { ok: !!j.success };
  } catch { return { ok: false }; }
}

async function rateLimit(env, ip) {
  if (!env.RATE_LIMIT_KV || !ip) return true;
  const key = "rl:" + ip;
  const n = Number((await env.RATE_LIMIT_KV.get(key)) || "0");
  if (n >= 5) return false;
  await env.RATE_LIMIT_KV.put(key, String(n + 1), { expirationTtl: 600 });
  return true;
}

export async function onRequestPost(context) {
  const { request, env } = context;
  if (Number(request.headers.get("content-length") || "0") > MAX_FORM_BYTES) return text("This request is too large. Please attach a smaller photo.", 413);
  if (!isAllowedOrigin(request.headers.get("origin"))) return text("This form submission is not allowed.", 403);
  const ct = request.headers.get("content-type") || "";
  if (!ct.startsWith("application/x-www-form-urlencoded") && !ct.startsWith("multipart/form-data")) return text("Unsupported form format.", 415);

  let form;
  try { form = await request.formData(); } catch { return text("The form could not be read.", 400); }
  if (field(form, "company")) return Response.redirect(new URL("/thank-you/", request.url), 303); // honeypot

  const ip = request.headers.get("cf-connecting-ip") || "";
  if (!(await rateLimit(env, ip))) return text("Too many requests from this connection. Please email hello@kissimmeeconcrete.com instead.", 429);

  const ts = await verifyTurnstile(field(form, "cf-turnstile-response"), env.TURNSTILE_SECRET_KEY, ip);
  if (!ts.ok) return text("We could not verify that you are human. Please reload the page and try again.", 403);

  const payload = { hub_id: HUB_ID };
  for (const k of Object.keys(LIMITS)) payload[k] = field(form, k);
  const err = validate(payload);
  if (err) return text(err, 400);

  let photo = null;
  const file = form.get("photo");
  if (file && typeof file === "object" && file.size) {
    if (file.size > MAX_PHOTO_BYTES) return text("Please attach a photo under 6 MB.", 413);
    if (!/^image\/(jpeg|png|webp|heic|heif)$/.test(file.type)) return text("Please attach a JPG, PNG, WebP or HEIC photo.", 415);
    const buf = await file.arrayBuffer();
    let bin = ""; const bytes = new Uint8Array(buf);
    for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
    photo = { name: (file.name || "photo").slice(0, 80), type: file.type, base64: btoa(bin) };
  }
  payload.server_ts = new Date().toISOString();
  payload.country = request.headers.get("cf-ipcountry") || "";
  payload.photo = photo;

  if (!env.CONTACT_EMAIL) return text("The contact service is not configured yet. Please email hello@kissimmeeconcrete.com.", 503);
  const res = await env.CONTACT_EMAIL.fetch("https://contact-email.internal/send", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
  if (!res.ok) return text("We could not send your request right now. Please email hello@kissimmeeconcrete.com or try again in a few minutes.", 502);
  return Response.redirect(new URL("/thank-you/", request.url), 303);
}

export async function onRequestGet() { return text("Method not allowed", 405); }
