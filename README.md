# Handyman James — website

Plain HTML and CSS. No build tools, no frameworks, no external dependencies. Every page is a real file you can open and read.

## What's in this folder

**Pages**
- `index.html` — home page, with LocalBusiness schema
- `services.html` — services hub
- `property-management.html` — property management & 24/7 on-call ($50/month), with sign-up form
- `snow-register.html` — 2026–2027 snow clearance register, with sign-up form
- `handyman-work.html` — general handyman work
- `snow-removal.html` — snow clearance & deicing
- `locations.html` — service areas, with the area map
- `about.html`, `faq.html`, `contact.html`

**Assets**
- `style.css` — all styling, shared by every page
- `images/logo.png`, `images/snow-clearing.jpg`, `images/cleared-driveway.jpg`, `images/icon-512.png`
- `images/favicon.ico`, `images/apple-touch-icon.png`

**Analytics**
- `analytics.js` — Google Analytics (GA4), loaded by every page

The measurement ID is set in one place, at the top of `analytics.js`. The standard
Google snippet repeats the ID twice per page; across 11 pages that's 22 copies to keep
in step, and a page that gets missed is a hole in the data you only find by going
looking for it. Each page loads the shared file instead.

Until a real `G-` ID is filled in, the file deliberately does nothing — so the site can
deploy before the Analytics account is ready. It also skips localhost, so testing
doesn't show up as real traffic.

**Config**
- `render.yaml` — Render deployment config
- `sitemap.xml` — page index for search engines
- `robots.txt` — crawler permissions, points to the sitemap

---

## Forms

Three pages have working forms, all posting to the backend's public enquiry endpoint
(`https://handyman-s4l1.onrender.com/api/public/enquiry`):

- `contact.html`
- `property-management.html`
- `snow-register.html`

Each carries three hidden fields:

- `_subject` — labels the message by which page it came from (contact enquiry,
  property management sign-up, or snow register request)
- `_redirect` — sends the visitor to `thank-you.html` after a successful submit
- `_gotcha` — a hidden honeypot field; bots fill it in, real people don't

These previously went to Formspree (form ID `meaqakbz`). That free tier capped at 50
submissions a month, which was a real risk during the September snow register rush —
once full, submissions stopped rather than queued. The backend has no such cap.

**Test each one after deploying.** Submissions only work from the live domain, not from
a file opened locally.

---

## Deploying to Render

1. Create a GitHub account and a public repository
2. Upload everything in this folder, keeping the `images/` folder structure
3. Create a Render account, connect GitHub
4. **New → Blueprint**, point it at your repo — Render reads `render.yaml` automatically
5. Render gives you a temporary address like `handyman-james-site.onrender.com`. Test everything there first — click every link, submit each form, check it on your phone.

### Then, and only then: the domain

`www.handyman-james.com` currently points at Wix. Moving it means changing DNS records — and if `info@handyman-james.com` runs through Wix's email, those records may carry your email too. Change the wrong one and the inbox goes down with the site. Worth doing carefully, together, rather than from a support article.

---

## Seasonal maintenance

**After 30 September 2026:** remove the red snow register banner from every page. Search for `season-banner` — it's one `<div>` at the top of each HTML file, directly above `<header class="site-header">`.

**Each new snow season:** update the dates in `snow-register.html` (title, banner, deadline text, and the `availabilityEnds` date in the schema block).
