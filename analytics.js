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
var GA_MEASUREMENT_ID = "";

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
})();
