# Handyman James — new site

Plain HTML and CSS, no build tools, no frameworks. Every page is a real file you can open and read. This is step one of the migration: home page, contact page, and the deployment pipeline, all working end to end. The other eight pages (Services hub, four pillar pages, Locations, FAQ, About) come next — once this pipeline is live, adding them is just "drop in a file, push."

## What's in this folder

- `index.html` — home page, with the LocalBusiness schema built directly into the page (no more pasting into a Custom Code panel — it's just part of the file now)
- `contact.html` — contact page with a working form
- `style.css` — everything's styling, shared by every page
- `render.yaml` — tells Render how to deploy this, automatically
- `README.md` — this file

## Before you go live: two things need your input

**1. Images.** I couldn't pull your actual photo files from Wix, so the pages reference images that don't exist yet. Create an `images` folder next to these files and add:
- `images/hero.jpg` — a good photo of your work (referenced by the schema too)
- `images/james-portrait.jpg` — a photo of you, for the About section

Easiest path: open your current site, right-click the images you like, "Save image as," and drop them in with those exact filenames.

**2. The contact form.** Sign up free at [formspree.io](https://formspree.io) (email only, no card needed), create a form, and they'll give you an endpoint that looks like `https://formspree.io/f/abc123xy`. Open `contact.html`, find the line that says `YOUR_FORM_ID`, and replace it with your real ID.

## Getting this online (do this part first, before touching your domain)

1. **Create a GitHub account** at github.com, if you don't have one.
2. **Create a new repository** — call it something like `handyman-james-site`. Keep it public (Render's free tier needs that).
3. **Upload the files** — on the new repo's page, click "Add file" → "Upload files," and drag in everything from this folder (including the `images` folder once you've added your photos).
4. **Create a Render account** at render.com and connect your GitHub account.
5. **New → Blueprint**, point it at your repo. Render reads `render.yaml` automatically and sets everything up — you shouldn't need to configure anything by hand.
6. Render gives you a temporary address like `handyman-james-site.onrender.com`. **Open it and check everything** — click around, submit the contact form, check it on your phone.

## Only after that works: moving your domain over

This is the one genuinely risky step, so it's worth doing carefully rather than fast. `www.handyman-james.com` currently points at Wix. Moving it to Render means changing DNS records — and if `info@handyman-james.com` runs through Wix's own email hosting, those same DNS records may be carrying your email too. Change the wrong thing and you can take your inbox down along with the site.

When you're ready for this step, let's do it together rather than you doing it solo from a support article — I'll walk you through exactly which records to change and which to leave alone.

## What's next

The remaining pages — Services hub, the four service pillar pages, Locations, FAQ, About — get built the same way: a new `.html` file, styled by the same `style.css`, pushed to the same repo. Once pushed, Render redeploys automatically. No new setup needed after today.
