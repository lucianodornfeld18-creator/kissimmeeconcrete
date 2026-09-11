// kissimmeeconcrete-contact — Worker that turns a validated lead into an email.
// Bound to the Pages project as service binding CONTACT_EMAIL. Only accepts
// internal service-binding calls (no public route). Secrets: CONTACT_DESTINATION
// (verified Email Routing destination), optional RESEND_API_KEY for the
// homeowner auto-reply (Cloudflare Email Workers can only send to verified
// destinations, so the auto-reply needs a transactional provider).
import { EmailMessage } from "cloudflare:email";
import { createMimeMessage } from "mimetext";

const FROM = "hello@kissimmeeconcrete.com";
const FROM_NAME = "Kissimmee Concrete";

function line(k, v) { return v ? `${k}: ${v}\n` : ""; }

export default {
  async fetch(request, env) {
    if (request.method !== "POST") return new Response("Method not allowed", { status: 405 });
    let p;
    try { p = await request.json(); } catch { return new Response("Bad JSON", { status: 400 }); }
    if (!env.CONTACT_DESTINATION) return new Response("CONTACT_DESTINATION not set", { status: 503 });

    const subject = `[Kissimmee Concrete] ${p.service || "Estimate request"} — ${p.city || "city not given"} — ${p.name}`;
    const body =
      `New estimate request from kissimmeeconcrete.com (hub_id=${p.hub_id})\n\n` +
      line("Name", p.name) + line("Phone", p.phone) + line("Email", p.email) + line("Preferred language", p.language) +
      line("City / community", p.city) + line("Service", p.service) + line("Property type", p.property_type) + line("Timeline", p.timeline) +
      `\nProject notes:\n${p.message || "(none)"}\n\n` +
      `--- attribution ---\n` + line("Page", p.page_url) + line("Referrer", p.referrer) + line("utm_source", p.utm_source) + line("utm_medium", p.utm_medium) +
      line("utm_campaign", p.utm_campaign) + line("utm_term", p.utm_term) + line("utm_content", p.utm_content) + line("gclid", p.gclid) +
      line("Submitted (client)", p.client_ts) + line("Submitted (server)", p.server_ts) + line("Country", p.country);

    const msg = createMimeMessage();
    msg.setSender({ name: FROM_NAME, addr: FROM });
    msg.setRecipient(env.CONTACT_DESTINATION);
    msg.setSubject(subject);
    if (p.email) msg.setHeader("Reply-To", p.email);
    msg.addMessage({ contentType: "text/plain", data: body });
    if (p.photo && p.photo.base64) {
      msg.addAttachment({ filename: p.photo.name, contentType: p.photo.type, data: p.photo.base64, encoding: "base64" });
    }
    try {
      await env.SEND_EMAIL.send(new EmailMessage(FROM, env.CONTACT_DESTINATION, msg.asRaw()));
    } catch (e) {
      return new Response("send failed", { status: 502 });
    }

    // Optional auto-reply to the homeowner (needs RESEND_API_KEY + verified domain at Resend)
    if (env.RESEND_API_KEY && p.email) {
      try {
        await fetch("https://api.resend.com/emails", {
          method: "POST",
          headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, "content-type": "application/json" },
          body: JSON.stringify({
            from: `${FROM_NAME} <${FROM}>`, to: [p.email], reply_to: env.CONTACT_DESTINATION,
            subject: "We received your estimate request — Kissimmee Concrete",
            text: `Hi ${p.name},\n\nThanks for reaching out to Kissimmee Concrete about ${p.service || "your project"}${p.city ? " in " + p.city : ""}. We'll call or text you during business hours (Mon–Fri 7:30–6, Sat 8–1) to set up a site visit and a written estimate.\n\nIf you'd like to add photos or measurements, just reply to this email.\n\nKissimmee Concrete\n${FROM}\n`,
          }),
        });
      } catch (e) { /* auto-reply is best effort */ }
    }
    return new Response("ok", { status: 200 });
  },
};
