/* Google Analytics (GA4) for handyman-james.com
 *
 * The measurement ID lives here and nowhere else. The usual Google snippet repeats
 * it twice on every page, which on an 11-page site means 22 copies to keep in step -
 * and one missed page is a gap in the data that's invisible until you go looking for
 * it. Each page loads this file instead, so changing the ID is a one-line edit.
 *
 * ---------------------------------------------------------------------------
 * SET THIS. Find it in Google Analytics under Admin > Data Streams > your web
 * stream. It looks like G-ABC1234XYZ (not "UA-" - that's the old Universal
 * Analytics, switched off in 2023, and its tags no longer collect anything).
 * ---------------------------------------------------------------------------
 */
var GA_MEASUREMENT_ID = "G-RWV9HVGWHS";

(function () {
  // Deliberately does nothing until a real ID is set, so the site can ship before
  // the Analytics account is ready without firing requests at a bad property or
  // throwing errors in the console.
  if (!GA_MEASUREMENT_ID || GA_MEASUREMENT_ID.indexOf("G-") !== 0) {
    return;
  }

  // Don't count local testing as real traffic.
  var host = window.location.hostname;
  if (host === "localhost" || host === "127.0.0.1" || host === "" || host.indexOf(".local") > -1) {
    return;
  }

  // Nor the Render preview domain. The site gets tested there before every DNS
  // change and before each season's register goes live; without this, that
  // testing lands in the same property as real visitors.
  if (host.indexOf(".onrender.com") > -1) {
    return;
  }

  // Nor James's own visits. Opening the site once with ?notrack
  // (www.handyman-james.com/?notrack) stops that browser being counted; ?track turns
  // it back on. It's remembered per browser, so Chrome and Safari on the same phone
  // each need it, and clearing the site's data undoes it. Without this, every check
  // of the live site after a change lands in "Direct" looking like a customer.
  var NOTRACK_KEY = "hj-notrack";
  var query = window.location.search;
  var wantsOff = /[?&]notrack\b/.test(query);
  var wantsOn = /[?&]track\b/.test(query);
  var off = wantsOff;
  var stored = true;
  try {
    if (wantsOff) localStorage.setItem(NOTRACK_KEY, "1");
    if (wantsOn) localStorage.removeItem(NOTRACK_KEY);
    off = localStorage.getItem(NOTRACK_KEY) === "1";
  } catch (e) {
    // Storage blocked (private window, strict settings): this page load still
    // honours ?notrack, but there's nowhere to remember it.
    stored = false;
  }
  if (wantsOff) {
    showNote(stored
      ? "This browser is no longer counted in Google Analytics. Open the site with ?track to undo."
      : "This browser blocks site storage, so ?notrack only applies to this one page.");
  } else if (wantsOn) {
    showNote("This browser is counted in Google Analytics again.");
  }
  if (off) {
    return;
  }

  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_MEASUREMENT_ID);
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("js", new Date());

  // anonymize_ip is on by default in GA4 and can't be turned off, so there's nothing
  // to set for it here. This just names the property being reported to.
  gtag("config", GA_MEASUREMENT_ID);

  // A lead. Every form on the site - contact, Property Care and the snow register -
  // sends people to thank-you.html, and the server only redirects there once the
  // enquiry is saved, so landing here means a real enquiry came in. Marked as a key
  // event in Analytics. history.state survives a refresh and Back/Forward, so
  // reloading the page doesn't count the same enquiry twice; a new submission is a
  // new history entry and counts again.
  if (/\/thank-you(\.html)?$/.test(window.location.pathname)) {
    var counted = false;
    try { counted = !!(history.state && history.state.hjLeadCounted); } catch (e) {}
    if (!counted) {
      gtag("event", "generate_lead");
      try { history.replaceState({ hjLeadCounted: true }, ""); } catch (e) {}
    }
  }

  // Taps on the phone number or email address, from any page. Most people call
  // or text rather than fill in a form, and without this those leads never show up.
  // One listener on the document covers every link, including ones added later.
  document.addEventListener("click", function (e) {
    var link = e.target && e.target.closest ? e.target.closest("a[href]") : null;
    if (!link) return;
    var href = link.getAttribute("href") || "";
    if (href.indexOf("tel:") === 0 || href.indexOf("sms:") === 0) {
      gtag("event", "phone_click");
    } else if (href.indexOf("mailto:") === 0) {
      gtag("event", "email_click");
    }
  });

  // The ?notrack / ?track confirmation. A plain bar at the foot of the page, since
  // without it there's no way to tell the switch did anything.
  function showNote(text) {
    var note = document.createElement("div");
    note.textContent = text;
    note.setAttribute("role", "status");
    note.style.cssText = "position:fixed;left:16px;right:16px;bottom:16px;z-index:1000;" +
      "padding:12px 16px;border-radius:8px;background:#1B2921;color:#fff;" +
      "font:500 15px/1.4 Archivo,system-ui,sans-serif;box-shadow:0 4px 16px rgba(0,0,0,.25);";
    document.body.appendChild(note);
    setTimeout(function () { note.remove(); }, 8000);
  }
})();
