# Cappuccina Country Resort package page: build notes

Page: `/packages/italy/tuscany/cappuccina-country-resort` (this folder's `index.html`)
Status: Draft, vet before publish. The page carries `noindex` until it is cleared.

## What the page combines

1. **Everything on the Easy Weddings package page** (from the 7 Oct screenshot):
   hero with location, Highlights box (5 ticks, 20 to 300 guests, from $38,550,
   exclusive accommodation for 16), Highlights / Images / Inclusions jump links,
   "Rural Resort Luxury" intro, Your Wedding, Your Stay, Resort Highlights with
   Read more, Tuscany map and blurb, "Your wedding package includes" cards for
   Ceremony, Reception and Accommodation (venue lists, inclusion lists, image
   carousels, "Upgrades available" tags), 5-image gallery with "+21 more",
   personal planner panel, enquiry form (first name, last name, email, phone,
   guests, wedding date) with terms line.
2. **Everything in the Wedded Wonderland brief** (WW-Page-Briefs-2026-10-07):
   offers table, why couples choose it, history, spaces comparison, room
   categories, dining, spa and activities, getting there, Tuscany guide,
   stay on after the wedding, Wedded Privileges, 5-step process, nearby
   comparisons, FAQ, Concierge vs Marketplace choice.
3. **Added by this build**: exclusive Villa Cappuccina as its own offer row,
   resort distances on the map card, AUD quoting and fee-in-writing points in
   the advisor panel, "dates flexible" and message fields on the form, chosen
   offer carried into the enquiry, mobile sticky enquire bar, schema.org
   Breadcrumb, Product/Offer and FAQPage markup, merged duplicate FAQ.

## Build rules applied

- The enquiry form posts to Wedded Concierge (`/api/concierge/enquiry`,
  hidden `route_to=wedded-concierge`). No venue contact details appear on the page.
  **Confirm the real endpoint** with the dev team.
- All prices are shown as "From AUD" and need Nic's sign-off.
- No Easy Weddings branding, copy-only claims ("3,500+ weddings planned",
  "Easy Exclusive") or images are reused.

## Still to check before publishing

- [ ] Nic to vet AUD 38,550 (Easy Weddings shows $38,550) and the three comparison prices.
- [ ] Capacity: package says 20 to 300; official site only confirms terraces up to 200.
      La Lista says up to 250 for weddings, auditorium 300, restaurant 180 seated.
- [ ] Ballroom capacity is not stated on the official site.
- [ ] Room count: official site 69 rooms plus tower; Easy Weddings says "up to 70".
      Number of tower rooms not stated (La Lista says 7 or 8 suites).
- [ ] Villa Cappuccina exclusive: 7 rooms and suites, sleeps 16 (from Easy Weddings).
      Confirm with the resort, and price the exclusive villa offer.
- [ ] Airport transfer time: Easy Weddings says Florence Airport 30 to 60 minutes;
      official site gives none, so the page uses distances only.
- [ ] "Vineyard" chip and "Vineyard wedding setting" highlight: confirm the
      resort has its own vines or reword to "vineyard views".
- [ ] Wedded Privileges sub-lines are generic; confirm wording with the programme owner.
- [ ] Nearby package slugs are guessed from names; confirm the URLs exist.
- [ ] Header, footer, fonts and colours are a stand-in: the live
      weddedwonderland.com stylesheet could not be reached from the build
      environment. Swap in the site's shared header, footer and tokens.

## Images to supply

Every image slot is a `<div class="ph" data-img="...">`. Upload the photos and
set `IMG_BASE` in the page script (for example
`/img/packages/cappuccina-country-resort/`), or replace each slot with an `<img>`.

| File | Where |
|---|---|
| hero-01-tower-house.jpg | Hero slide 1 |
| hero-02-villa-terrace-san-gimignano.jpg | Hero slide 2 |
| hero-03-panoramic-pool.jpg | Hero slide 3 |
| hero-04-ballroom.jpg | Hero slide 4 |
| ceremony-villa-terrace.jpg, ceremony-ballroom.jpg | Ceremony carousel |
| reception-torre-luce.jpg, reception-villa-terrace.jpg, reception-ballroom.jpg | Reception carousel |
| room-terrace-suite-gold.jpg, room-tower-suite.jpg, room-deluxe-terrace.jpg | Accommodation carousel |
| gallery-01 to gallery-05 | Gallery |
| space-villa-terraces.jpg, space-ballroom.jpg, space-torre-luce.jpg | Spaces |
| tuscany-chianti-hills.jpg | Tuscany section |
| cmp-*.jpg | Nearby comparison cards |

Use the resort's own media kit (with permission), not images from Easy Weddings.

## Sources

- https://www.easyweddings.com.au/destination-weddings/package/cappuccina-country-resort-italy/ (screenshot, 7 Oct 2026)
- https://www.cappuccinacountryresort.com/en/ and the pages listed in the brief
- https://www.lalista.com/venues/tuscany/cappuccina-country-resort (capacity cross-check only)
