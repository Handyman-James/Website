#!/usr/bin/env python3
"""Generate town x service pages for the Handyman James site.

Output is plain static HTML matching the existing hand-written pages -- no
build step is introduced. This script exists so the fifteen pages stay
consistent with each other and can be regenerated if the header, nav or
footer ever changes; it is not required to serve the site.
"""
import json, pathlib

ROOT = pathlib.Path("/home/claude/site/Website-main")
BASE = "https://www.handyman-james.com"

# --------------------------------------------------------------- town data
TOWNS = {
    "newton": dict(
        name="Newton", lat=42.3370, lng=-71.2092,
        areas="Newtonville, West Newton, Auburndale, Waban, Newton Centre, "
              "the Highlands, Nonantum and Chestnut Hill",
        hand_lede="Newton is home base. James lives and works here, which for most "
                  "jobs in town means a shorter wait and a shorter drive.",
        hand_p1="It is also where the client history runs deepest. A lot of Newton work "
                "starts as a single job &mdash; a TV that needs mounting properly, a door "
                "that stops latching through a humid week &mdash; and turns into the "
                "standing arrangement of calling the same person every time something goes.",
        hand_p2="Much of Newton's housing stock is old enough to have opinions. Plaster "
                "and lath, settled frames, sashes painted shut by a previous owner, "
                "additions that meet the original house at an awkward angle. That is "
                "ordinary work here rather than a surprise, and it is the reason a "
                "licensed pair of hands is worth more than a general listing on an app.",
        pm_p="Newton has a high share of two-family and owner-occupied rental setups, "
             "and a lot of houses whose owners travel more than they are home. Both are "
             "situations where the thing that matters is not the hourly rate &mdash; it "
             "is whether anyone picks up.",
        snow_p="Newton driveways tend to be short, steep, and close to the neighbours, "
               "with lawn edges and planting beds right up against the asphalt. That is "
               "exactly the geometry a plow damages and a snowblower does not.",
        snow_p2="Many Newton properties have a public sidewalk to clear as well as a driveway, and front walks that run all the way to the street. Both are worth flagging when you register, because they change how long a property takes and therefore where it sits on the round.",
        pm_p2="Newton is also where a first job most often turns into a standing one. People rarely set out to hire a property manager; they hire someone for a leaking valve, decide they would rather not repeat the search, and take the retainer.",
        quote="James goes above and beyond and keeps everyone in contact. I would "
              "recommend him to anyone.",
        cite="Jay, Newton, MA"),

    "lexington": dict(
        name="Lexington", lat=42.4430, lng=-71.2290,
        areas="Lexington Center, the historic district, and the neighbourhoods off "
              "Massachusetts Avenue and Waltham Street",
        hand_lede="Lexington knows James first for snow. The handyman work followed, and "
                  "a good deal of it started with a driveway.",
        hand_p1="Clearing a property every storm for a winter teaches you the house. "
                "Which gutter overflows, which step ices, which door swells. A fair "
                "number of Lexington handyman jobs began as something noticed during a "
                "January round and mentioned to the owner afterwards.",
        hand_p2="The older colonials here, and the houses around the historic district, "
                "carry the maintenance that age brings: sash windows, exterior trim that "
                "wants repainting before it rots rather than after, interior doors that "
                "move with the seasons. None of it is dramatic. All of it gets worse "
                "if left.",
        pm_p="Lexington has a lot of larger properties and a lot of owners who are away "
             "for stretches of the year. A frozen pipe in an empty house is not an "
             "expensive repair because of the pipe; it is expensive because of how long "
             "it runs before anyone notices.",
        snow_p="Lexington driveways are often long, and frequently edged with lawn, "
               "gravel or planting that a plow blade finds on the first pass of the "
               "season. This is the town where the snowblower-only rule earns its keep, "
               "and where the round has its longest unbroken record.",
        snow_p2="A lot of Lexington houses sit well back from the road, which means the walk from the street to the front door is a clearing job in its own right, on top of the driveway. Deicing matters as much as clearing on those approaches.",
        pm_p2="Second homes and long absences are common here, and an empty house is the expensive case. A frozen pipe does not cost much because of the pipe. It costs because of how many hours it runs before anybody walks in.",
        quote="The best snow clearance team I've known in 50 years of living in "
              "Massachusetts. Never fails and always clears the drive perfectly, no "
              "matter the depth.",
        cite="Jim, Lexington, MA"),

    "arlington": dict(
        name="Arlington", lat=42.4154, lng=-71.1565,
        areas="Arlington Heights, Arlington Center and East Arlington",
        hand_lede="Arlington is where the awkward jobs come from &mdash; the ones other "
                  "contractors would rather not quote.",
        hand_p1="Some of that is scale: a single picture to hang, a cabinet door that "
                "will not sit square, work too small for a firm with a crew to keep busy. "
                "Some of it is stranger than that. One Arlington client called about an "
                "industrial sewing machine.",
        hand_p2="The housing here is tight and close together &mdash; capes, two-families "
                "and older singles on narrow lots, plenty of them built when a utility "
                "room meant the basement. Access is usually the first problem to solve "
                "and the one that decides how long a job takes.",
        pm_p="East Arlington in particular runs heavily to two-families and rented units, "
             "often owned by people who no longer live in them. The retainer exists for "
             "precisely that: one licensed number, reachable at any hour, for a property "
             "you are not standing in front of.",
        snow_p="Arlington's driveways are narrow, frequently shared, and hemmed in by "
               "on-street parking that leaves nowhere for a plow to push snow. A "
               "snowblower can put it where it needs to go instead of piling it against "
               "someone else's car.",
        snow_p2="When a snow emergency puts a parking ban on the street, a driveway stops being the convenient place to leave the car and becomes the only one. Shared and tandem drives need clearing properly rather than approximately, and there is usually nowhere obvious to put the snow.",
        pm_p2="A good deal of Arlington's rented stock is owned by people who moved out years ago and kept the building. The retainer is built for exactly that distance: you are not going to drive over to look at it, so somebody has to.",
        quote="James is prompt with his work and getting back to me. His breadth of "
              "knowledge is amazing &mdash; he was able to fix my industrial sewing "
              "machine and get it running well every time. He's also available for small "
              "jobs and quite pleasant to work with.",
        cite="Katherine, Arlington, MA"),

    "waltham": dict(
        name="Waltham", lat=42.3765, lng=-71.2356,
        areas="the Moody Street area, the Brandeis side of town, and the neighbourhoods "
              "off Trapelo Road",
        hand_lede="Waltham is where word of mouth does most of the work. A job on one "
                  "street has a habit of producing the next one two doors down.",
        hand_p1="That is not a marketing line so much as a description of how this part "
                "of the business actually runs. Neighbours talk, someone gets a "
                "recommendation over a fence, and the second call comes without anyone "
                "having searched for anything.",
        hand_p2="Waltham carries a high share of two- and three-family houses, which "
                "changes the shape of the work. A lot of it is turnover work: patching, "
                "painting, fixing what the last tenant left, on a deadline set by when "
                "the next one moves in.",
        pm_p="If you own units here, this is the page that matters. The retainer is "
             "priced per property, so a three-unit portfolio is $150 a month for "
             "round-the-clock access to a licensed tradesman who already knows all three "
             "buildings &mdash; and no emergency premium when a tenant calls at "
             "midnight rather than at noon.",
        snow_p="Multi-unit properties have a harder snow problem than single homes: "
               "several sets of tenants who all need to get out early, shared walkways "
               "that become a liability the moment they ice over, and often a commercial "
               "frontage as well. All of that is on the same register.",
        snow_p2="Tenants leave earlier and in more directions than a single family does, and shared walkways become a liability the moment they ice over. Commercial frontages have their own early-morning deadline. All of it is on the same register, and all of it is worth describing when you sign up.",
        pm_p2="Turnover here runs to a calendar rather than a convenience. The gap between one tenant leaving and the next arriving is short, fixed, and expensive to overrun, which is a different problem from a homeowner's repair list.",
        quote=None, cite=None),

    "belmont": dict(
        name="Belmont", lat=42.3959, lng=-71.1787,
        areas="Belmont Hill, Waverley and Cushing Square",
        hand_lede="Belmont sits in the middle of the round, between Arlington, Waltham "
                  "and Cambridge &mdash; which makes it one of the easier towns to reach "
                  "quickly.",
        hand_p1="It is a mixed town to work in. Belmont Hill runs to large older houses "
                "with the upkeep that implies, while Waverley and the streets around "
                "Cushing Square are denser and carry more two-families. The work follows "
                "the housing: bigger exterior and carpentry jobs on one side of town, "
                "steady small repairs on the other.",
        hand_p2="Being central to the service area matters more than it sounds. Belmont "
                "usually sits between two other jobs rather than at the end of a long "
                "drive, which is part of why small jobs here are worth taking at all.",
        pm_p="Belmont's larger properties have more that can go wrong out of sight "
             "&mdash; more roof, more gutter, more exterior to weather a winter. "
             "Seasonal walkthroughs are the part of the retainer that pays for itself "
             "here, because they catch things in October that would otherwise be found "
             "in February.",
        snow_p="Belmont Hill is the reason to think about this before December. Steep "
               "driveways ice rather than simply filling with snow, which makes deicing "
               "as important as clearing, and makes a plow's habit of leaving a "
               "compacted layer behind a genuine hazard rather than an annoyance.",
        snow_p2="A plow on a sloped drive tends to leave a compacted layer behind it that then freezes. Clearing to the surface and treating it afterwards is the difference between a driveway you can walk down in January and one you cannot.",
        pm_p2="Larger houses simply have more that fails out of sight &mdash; more roof, more gutter, more exterior to get through a winter. The seasonal walkthrough is the part of the retainer that earns its money here, because October is a much cheaper month to find something than February.",
        quote=None, cite=None),
}

RETAINER_QUOTE = dict(
    quote="This man's dedication to his job is outstanding. He's well informed, "
          "professional, and transparent about everything he does.",
    cite="Matthew, Lincoln, MA")

# ------------------------------------------------------------ shared chrome
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Fraunces:ital,wght@0,400;0,500;0,600;1,400;1,500&'
         'family=Archivo:wght@400;500;600;700&display=swap">')

BANNER = ('<div class="season-banner">Limited places on the 2026&ndash;2027 snow '
          'clearance round &mdash; register closes 30 September &mdash; '
          '<a href="snow-register.html">register your property</a></div>')

HEADER = '''<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand">
      <img src="images/logo.png" alt="Handyman James" class="brand-logo">
      <span class="brand-text">Handyman James</span>
    </a>
    <div class="header-right">
      <span class="license-badge">Construction Supervisor License <strong>#120385</strong></span>
      <span class="license-badge">Home Improvement Contractor <strong>#197410</strong></span>
      <a href="tel:+15083061552" class="header-phone">Call or text (508) 306-1552</a>
    </div>
  </div>
  <div class="header-nav-row">
    <div class="container">
    <nav class="site-nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <a href="property-management.html">Property Management</a>
      <a href="snow-register.html">Snow Register</a>
      <a href="locations.html">Locations</a>
      <a href="about.html">About</a>
      <a href="faq.html">FAQ</a>
      <a href="contact.html">Contact</a>
    </nav>
    </div>
  </div>
</header>'''

FOOTER = '''<footer class="site-footer">
  <div class="container">
    <div><strong>Handyman James</strong></div>
    <div>CSL #120385 &amp; HIC #197410, Newton, MA</div>
    <div>&copy; 2026 Handyman James</div>
  </div>
</footer>'''

LICENSE_BLOCK = '''<section>
  <div class="container">
    <h2 class="section-label">Licensed, insured, and accountable</h2>
    <p>James holds an unrestricted Massachusetts Construction Supervisor License
    (CSL #120385) and is a registered Home Improvement Contractor (HIC #197410) &mdash;
    the state registration that gives {town} clients access to the Guaranty Fund and
    the arbitration program if something goes wrong. He carries insurance. If a job
    falls outside his license or his skills, he will say so before starting, not after.</p>
    <a href="contact.html" class="btn">Get a quote</a>
  </div>
</section>'''


def head(title, desc, canon, image="icon-512.png", schema=None):
    blocks = ""
    if schema:
        blocks = ('<script type="application/ld+json">\n'
                  + json.dumps(schema, indent=2, ensure_ascii=False)
                  + '\n</script>\n')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}/{canon}">
<link rel="icon" href="images/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="images/apple-touch-icon.png">
<meta name="theme-color" content="#1B2921">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Handyman James">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/images/{image}">
<meta property="og:url" content="{BASE}/{canon}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{BASE}/images/{image}">
{FONTS}
<link rel="stylesheet" href="style.css">
{blocks}<script src="analytics.js" defer></script>
</head>
<body>

{BANNER}
{HEADER}
'''


def service_schema(name, stype, desc, town, d, canon, offer=None):
    s = {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": f"{BASE}/{canon}#service",
        "name": name,
        "serviceType": stype,
        "description": desc,
        "provider": {
            "@id": f"{BASE}/#business",
            "@type": "HomeAndConstructionBusiness",
            "name": "Handyman James",
            "url": BASE,
            "telephone": "+1-508-306-1552",
        },
        "areaServed": {
            "@type": "City",
            "name": f"{town}, Massachusetts",
            "geo": {"@type": "GeoCoordinates",
                    "latitude": d["lat"], "longitude": d["lng"]},
        },
    }
    if offer:
        s["offers"] = offer
    return s


def testimonial(quote, cite):
    if not quote:
        return ""
    return f'''    <div class="testimonial">
      <p>&ldquo;{quote}&rdquo;</p>
      <cite>&mdash; {cite}</cite>
    </div>
'''


def crosslinks(slug, town, current):
    rows = []
    if current != "hand":
        rows.append((f"handyman-work-{slug}.html", f"Handyman work in {town}",
                     "Repairs, fixtures, drywall, painting and the everyday jobs."))
    if current != "pm":
        rows.append((f"property-management-{slug}.html",
                     f"Property management in {town}",
                     "$50 a month, per property. 24/7 access, no emergency callout fees."))
    if current != "snow":
        rows.append((f"snow-removal-{slug}.html", f"Snow clearance in {town}",
                     "Snowblowers only, never a plow. Register closes 30 September."))
    body = "\n".join(
        f'''    <div class="service-row">
      <h3><a href="{u}">{t}</a></h3>
      <p>{p}</p>
    </div>''' for u, t, p in rows)
    return f'''<section class="alt">
  <div class="container">
    <h2 class="section-label">Also in {town}</h2>
{body}
    <p style="margin-top:20px;"><a href="locations.html">All service areas &rarr;</a></p>
  </div>
</section>'''


# ----------------------------------------------------------- retainer block
def retainer_block(town, d, alt=True):
    """The retainer, given its own section on every page in the set."""
    cls = ' class="alt"' if alt else ""
    return f'''<section{cls}>
  <div class="container">
    <h2 class="section-label">The {town} retainer &mdash; $50 a month</h2>
    <p>Most people meet James through a single job. A fair number then move onto the
    monthly retainer, which is less a service than an arrangement: <strong>$50 per month,
    per property</strong>, and from then on there is one licensed number to call at any
    hour, with no emergency premium attached to calling it at the wrong one.</p>
    <div class="value-grid">
      <div>
        <h3>No emergency premium</h3>
        <p>A 3am callout is billed at the same hourly rate as a Tuesday afternoon.</p>
      </div>
      <div>
        <h3>Reach him directly</h3>
        <p>Phone, text or email, 24 hours a day. Not a call centre or a ticket queue.</p>
      </div>
      <div>
        <h3>Seasonal walkthroughs</h3>
        <p>Gutters, exterior and weatherproofing checked before the season that causes
        the damage, not after it.</p>
      </div>
      <div>
        <h3>Someone who knows the property</h3>
        <p>The same licensed tradesman every time, who already knows where your shutoff
        valve is.</p>
      </div>
    </div>
    <p style="margin-top:24px;">{d["pm_p"]}</p>
    <a href="property-management-{d["slug"]}.html" class="btn">The {town} retainer in
    full</a>
  </div>
</section>'''


# --------------------------------------------------------------- page types
def handyman_page(slug, d):
    town = d["name"]
    canon = f"handyman-work-{slug}.html"
    title = f"Handyman in {town}, MA | Licensed &amp; Insured | Handyman James"
    desc = (f"Licensed, insured handyman work in {town}, Massachusetts &mdash; repairs, "
            f"fixtures, drywall, painting and general fixes. One accountable "
            f"professional, no job too small.")
    schema = service_schema(
        f"Handyman work in {town}, MA", "Handyman and home repair services",
        f"General handyman work in {town}, Massachusetts: repairs, fixtures, furniture, "
        f"drywall, painting and outdoor upkeep, by a licensed and insured professional.",
        town, d, canon)
    return head(title, desc, canon, schema=schema) + f'''
<section class="hero" style="padding-bottom:40px;">
  <div class="container">
    <h1>Handyman in {town}, Massachusetts</h1>
    <p class="lede">{d["hand_lede"]}</p>
    <a href="contact.html" class="btn">Get a quote</a>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-label">Working in {town}</h2>
    <p>{d["hand_p1"]}</p>
    <p>{d["hand_p2"]}</p>
    <p>Covering {d["areas"]}.</p>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-label">What's included</h2>
    <div class="value-grid">
      <div>
        <h3>Furniture &amp; fixtures</h3>
        <p>Hanging blinds, TVs, artwork and shelving. Furniture assembly and fitting out
        a room from scratch.</p>
      </div>
      <div>
        <h3>Drywall &amp; painting</h3>
        <p>Patching, repairs, and full painting and decorating jobs, interior or
        exterior.</p>
      </div>
      <div>
        <h3>Outdoor upkeep</h3>
        <p>Deck cleaning and repainting, leaf clearance, lawn mowing and hedge
        trimming.</p>
      </div>
      <div>
        <h3>General fixes</h3>
        <p>If it's broken and it's in your house, there's a good chance James has fixed
        one like it before &mdash; from a sticking door to an industrial sewing
        machine.</p>
      </div>
    </div>
    <p style="margin-top:24px;"><a href="handyman-work.html">Full handyman work
    page &rarr;</a></p>
  </div>
</section>

{retainer_block(town, d, alt=False)}

<section class="alt">
  <div class="container">
    <h2 class="section-label">{"What " + town + " clients say" if d["quote"] else "What clients say"}</h2>
{testimonial(d["quote"], d["cite"]) or testimonial(RETAINER_QUOTE["quote"], RETAINER_QUOTE["cite"])}    <div class="review-links">
      <a class="review-link" href="https://maps.app.goo.gl/h1HN2yAFXUMvTpWw7" target="_blank" rel="noopener">
        <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> Read our Google reviews
      </a>
      <a class="review-link" href="https://www.yelp.com/biz/handyman-james-newton" target="_blank" rel="noopener">
        Find us on Yelp
      </a>
    </div>
  </div>
</section>

{LICENSE_BLOCK.format(town=town)}

{crosslinks(slug, town, "hand")}

{FOOTER}

</body>
</html>
'''


def pm_page(slug, d):
    town = d["name"]
    canon = f"property-management-{slug}.html"
    title = (f"Property Management in {town}, MA | $50/month Retainer | Handyman James")
    desc = (f"Property management and 24/7 on-call handyman service in {town}, MA for "
            f"$50 per month, per property. Seasonal walkthroughs, same-day response, no "
            f"emergency callout fees.")
    schema = service_schema(
        f"Property management & 24/7 on-call in {town}, MA",
        "Property management and 24/7 on-call handyman service",
        f"Monthly retainer giving {town} property owners 24-hour access to a licensed "
        f"handyman by phone, text and email, with same-day response, no emergency "
        f"callout fees, seasonal walkthroughs and rental turnover support.",
        town, d, canon,
        offer={"@type": "Offer", "price": "50.00", "priceCurrency": "USD",
               "priceSpecification": {
                   "@type": "UnitPriceSpecification", "price": "50.00",
                   "priceCurrency": "USD", "unitText": "per property per month"}})
    return head(title, desc, canon, schema=schema) + f'''
<section class="hero" style="padding-bottom:40px;">
  <div class="container">
    <h1>Property management &amp; 24/7 on-call in {town}</h1>
    <p class="lede">$50 per month, per property. Reach a licensed handyman at any hour
    by phone, text or email &mdash; and when something goes wrong at 3am in {town},
    there's no emergency callout fee waiting for you.</p>
    <a href="#signup" class="btn">Sign up</a>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-label">Why {town} owners take the retainer</h2>
    <p>{d["pm_p"]}</p>
    <p>{d["pm_p2"]}</p>
    <p>{d["hand_p2"]}</p>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-label">What you're paying for</h2>
    <div class="value-grid">
      <div>
        <h3>No emergency premium</h3>
        <p>A 3am callout is billed at the same hourly rate as a Tuesday afternoon. No
        several-hundred-dollar surcharge for bad timing.</p>
      </div>
      <div>
        <h3>Reach him any hour</h3>
        <p>Phone, text or email, 24 hours a day. Not a call centre or a ticket queue
        &mdash; James directly.</p>
      </div>
      <div>
        <h3>Same-day response</h3>
        <p>Normal callouts often within hours. Emergencies, as soon as he can physically
        get there.</p>
      </div>
      <div>
        <h3>Someone who knows the property</h3>
        <p>The same licensed tradesman every time, who already knows where your shutoff
        valve is.</p>
      </div>
      <div>
        <h3>Seasonal walkthroughs</h3>
        <p>Gutters, exterior and weatherproofing checked ahead of the seasons that cause
        the damage &mdash; not after.</p>
      </div>
      <div>
        <h3>Rental turnover support</h3>
        <p>Repairs and touch-ups handled between tenants, on your schedule, for owners
        who aren't local.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-label">What it costs</h2>
    <div class="service-row">
      <h3>The retainer</h3>
      <p><strong>$50 per month, per property.</strong> This covers 24-hour access,
      seasonal walkthroughs, and removes emergency callout fees. Landlords with several
      units in {town} pay per property.</p>
    </div>
    <div class="service-row">
      <h3>The work itself</h3>
      <p>Billed at James's standard hourly rate, plus materials and any other costs
      incurred. The retainer isn't a labour plan &mdash; it's what makes sure someone
      answers, and that calling at midnight doesn't cost more than calling at noon.</p>
    </div>
    <div class="service-row">
      <h3>The maths</h3>
      <p>A single after-hours emergency callout from a contractor typically carries a
      premium of several hundred dollars before anyone picks up a tool. At $50 a month,
      one 3am call in a year and the retainer has more than paid for itself &mdash; and
      most properties have more than one.</p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-label">What clients say</h2>
{testimonial(d["quote"], d["cite"])}{testimonial(RETAINER_QUOTE["quote"], RETAINER_QUOTE["cite"])}  </div>
</section>

<section id="signup">
  <div class="container">
    <h2 class="section-label">Sign up in {town}</h2>
    <p>Fill this in and James will call you to confirm the details and set up billing.
    No payment is taken through this form.</p>

    <div class="contact-block">
      <div>
        <form action="https://handyman-s4l1.onrender.com/api/public/enquiry" method="POST">
          <input type="hidden" name="_subject" value="Property Management sign-up &mdash; {town}">
          <input type="hidden" name="_redirect" value="{BASE}/thank-you.html">
          <input type="hidden" name="town" value="{town}">
          <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="form-field">
            <label for="name">Your name</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-field">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-field">
            <label for="phone">Phone</label>
            <input type="tel" id="phone" name="phone" required>
          </div>
          <div class="form-field">
            <label for="properties">Property address(es)</label>
            <textarea id="properties" name="properties" required placeholder="One per line if you have several"></textarea>
          </div>
          <div class="form-field">
            <label for="count">How many properties?</label>
            <input type="number" id="count" name="property_count" min="1" value="1" required>
          </div>
          <div class="form-field">
            <label for="notes">Anything else worth knowing?</label>
            <textarea id="notes" name="notes" placeholder="Tenanted, vacant, recurring issues, access arrangements..."></textarea>
          </div>
          <button type="submit" class="btn">Request sign-up</button>
        </form>
      </div>

      <div>
        <div class="contact-item">
          <span class="label">Rather just call or text?</span>
          <a href="tel:+15083061552">(508) 306-1552</a>
        </div>
        <div class="contact-item">
          <span class="label">Or email</span>
          <a href="mailto:info@handyman-james.com">info@handyman-james.com</a>
        </div>
        <div class="contact-item">
          <span class="label">Covering</span>
          <span>{d["areas"]}</span>
        </div>
      </div>
    </div>
  </div>
</section>

{crosslinks(slug, town, "pm")}

{FOOTER}

</body>
</html>
'''


def snow_page(slug, d):
    town = d["name"]
    canon = f"snow-removal-{slug}.html"
    title = f"Snow Removal in {town}, MA | Snowblowers Only | Handyman James"
    desc = (f"Snow clearance and deicing in {town}, Massachusetts &mdash; snowblowers "
            f"only, never a plow, so driveways and lawn edges come through winter "
            f"intact. Register closes 30 September.")
    schema = service_schema(
        f"Snow clearance & deicing in {town}, MA",
        "Snow removal and deicing",
        f"Snowblower-only snow clearance and deicing for residential and commercial "
        f"properties in {town}, Massachusetts. Places on the seasonal round are limited.",
        town, d, canon)
    return head(title, desc, canon, image="snow-clearing.jpg", schema=schema) + f'''
<section class="hero" style="padding-bottom:40px;">
  <div class="container">
    <p class="deadline-flag">Limited places &middot; Registration closes 30 September 2026</p>
    <h1>Snow clearance &amp; deicing in {town}</h1>
    <p class="lede">Snowblowers only &mdash; never a plow &mdash; so your driveway, lawn
    edges and landscaping come through winter the way they went into it. Residential and
    commercial. Places on the {town} round are limited.</p>
    <a href="snow-register.html" class="btn">Join the 2026&ndash;2027 register</a>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-label">Snow in {town}</h2>
    <p>{d["snow_p"]}</p>
    <p>{d["snow_p2"]}</p>
    <p>Plows are quick, and they are also what scrapes up driveway surfaces, tears lawn
    edges and buries mailboxes. Every property on this register is cleared with
    snowblowers. It takes longer. Nothing underneath gets wrecked.</p>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-label">What's covered</h2>
    <div class="value-grid">
      <div>
        <h3>Snow clearance</h3>
        <p>Driveways, paths and access areas cleared with snowblowers, no matter the
        depth.</p>
      </div>
      <div>
        <h3>Deicing</h3>
        <p>Treatment to keep cleared surfaces safe once the snow is off them.</p>
      </div>
      <div>
        <h3>Residential &amp; commercial</h3>
        <p>Both, on the same register. Commercial properties with early-morning access
        needs are worth flagging when you sign up.</p>
      </div>
      <div>
        <h3>Pricing</h3>
        <p>Charged per cubic foot, per snow event &mdash; so you pay for the snow that
        actually falls, not a flat fee for a winter that might be mild.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 class="section-label">Why places are limited</h2>
    <p>The round is worked by one person, and a storm only gives so many hours before
    people need to get out. Once the season starts, the properties on the list are the
    properties that get cleared &mdash; there is no adding a driveway mid-storm.
    Registering before 30 September is what secures a place in {town} for the winter.
    <a href="snow-removal.html">More on how the round works &rarr;</a></p>
    <picture><source srcset="images/cleared-driveway.webp" type="image/webp"><img src="images/cleared-driveway.jpg" alt="A residential driveway cut clean through deep snow by snowblower, with the snow banked to the side" class="photo" loading="lazy" decoding="async" width="1200" height="800"></picture>
    <a href="snow-register.html" class="btn">Register your {town} property</a>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-label">What clients say</h2>
{testimonial(TOWNS["lexington"]["quote"], TOWNS["lexington"]["cite"])}  </div>
</section>

{retainer_block(town, d, alt=False)}

{crosslinks(slug, town, "snow")}

{FOOTER}

</body>
</html>
'''


# ------------------------------------------------------------------- build
written = []
for slug, d in TOWNS.items():
    d["slug"] = slug
    for fn, builder in (("handyman-work", handyman_page),
                        ("property-management", pm_page),
                        ("snow-removal", snow_page)):
        path = ROOT / f"{fn}-{slug}.html"
        path.write_text(builder(slug, d), encoding="utf-8")
        written.append(path.name)

print(f"Wrote {len(written)} pages:")
for w in sorted(written):
    print("  ", w)
