(function () {
  "use strict";
  var d = document;
  function q(s, r) { return (r || d).querySelector(s); }
  function qa(s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); }
  function track(name, params) {
    try {
      if (window.gtag) { window.gtag("event", name, params || {}); }
      if (window.clarity) { window.clarity("event", name); }
      if (window.__kcEvents) { window.__kcEvents.push([name, params || {}]); }
    } catch (e) {}
  }
  window.kcTrack = track;

  // mobile nav
  var t = q("#navToggle"), n = q("#primaryNav");
  if (t && n) {
    t.addEventListener("click", function () {
      var open = n.classList.toggle("open");
      t.setAttribute("aria-expanded", open ? "true" : "false");
      t.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape" && n.classList.contains("open")) { n.classList.remove("open"); t.setAttribute("aria-expanded", "false"); t.focus(); } });
  }

  // tel / sms click tracking
  qa('a[href^="tel:"]').forEach(function (a) { a.addEventListener("click", function () { track("tel_click", { page: location.pathname }); }); });
  qa('a[href^="sms:"]').forEach(function (a) { a.addEventListener("click", function () { track("sms_click", { page: location.pathname }); }); });

  // lead forms: attribution fields, start/submit/error events
  qa("form.lead").forEach(function (f) {
    var started = false;
    function set(name, val) { var el = f.querySelector('[name="' + name + '"]'); if (el && !el.value) el.value = val || ""; }
    try {
      var p = new URLSearchParams(location.search);
      set("page_url", location.href.split("#")[0].slice(0, 300));
      set("referrer", (d.referrer || "").slice(0, 300));
      ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid"].forEach(function (k) { set(k, (p.get(k) || "").slice(0, 120)); });
      set("client_ts", new Date().toISOString());
      set("hub_id", "kissimmee");
    } catch (e) {}
    f.addEventListener("focusin", function () { if (!started) { started = true; track("form_start", { page: location.pathname }); } });
    f.addEventListener("submit", function (e) {
      var file = f.querySelector('input[type="file"]');
      if (file && file.files && file.files[0] && file.files[0].size > 6 * 1024 * 1024) { e.preventDefault(); alert("Please attach a photo under 6 MB."); track("form_error", { reason: "file_size" }); return; }
      try {
        var v = function (n) { var e = f.querySelector('[name="' + n + '"]'); return (e && e.value) || ""; };
        var subj = f.querySelector('[name="subject"]');
        if (subj) subj.value = "[Kissimmee Concrete] " + (v("service") || "Estimate request") + " — " + (v("zip") || "no ZIP") + " — " + v("name");
      } catch (e) {}
      track("form_submit", { page: location.pathname, service: (f.querySelector('[name="service"]') || {}).value || "", zip: (f.querySelector('[name="zip"]') || {}).value || "" });
      var b = f.querySelector('button[type="submit"]'); if (b) { b.disabled = true; b.textContent = "Sending…"; }
    });
  });

  // copy buttons (project brief etc.)
  qa("[data-copy-target]").forEach(function (b) {
    b.addEventListener("click", function () {
      var el = q(b.getAttribute("data-copy-target")); if (!el) return;
      var txt = el.innerText || el.textContent;
      if (navigator.clipboard) { navigator.clipboard.writeText(txt).then(function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1500); }); }
    });
  });
})();
