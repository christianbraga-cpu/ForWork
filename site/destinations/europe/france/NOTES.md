# France destination page: FIX build notes

Page: `/destinations/europe/france` (this folder's `index.html`)
Action: FIX, live but broken. Template T2 Country destination, with section 2 run as a
region chooser because France has 0 package pages. Brief: research of 14 Oct 2026.
Live page fetched 19 Oct 2026 for the before state.

## Head and SEO

| Item | Live (before) | Fixed (after) |
|---|---|---|
| Title | France Wedding Venues: Curated Luxury Estates & Châteaux \| Wedded Wonderland (78 chars) | Wedding in France \| Châteaux, Riviera & Paris Venues \| WW (57 chars). Check pixel width; fallback: Wedding in France \| Venues, Regions & Legal Guide |
| Meta | 152 chars, venues only | 150 chars: wedding in France, 5 regions, legal or symbolic, Wedded Advisor, no price |
| H1 | France Wedding Venues | Get married in France, from a Loire château to a Riviera terrace |
| First sentence | No primary keyword | Carries "wedding in France" and "wedding venues in France" |
| Schema | TouristDestination, Service, BreadcrumbList, FAQPage (4), Organization, WebSite | TouristDestination with containedInPlace Country + Place (Europe), ItemList of 6 regions, Service (areaServed France), BreadcrumbList, FAQPage (10, matches visible text), Organization. No Offer, no AggregateRating. Keep the site-wide WebSite node from the template |
| Canonical, robots | Correct, index follow | Unchanged |

## What was broken, and the fix

- Flat-label headings: all H2s rewritten in JJ's voice (section plan in the brief).
- Legacy Marketplace module "Discover France's Finest Venues & Vendors": removed. The 4 venues
  appear once each in one text line under the region chooser.
- "Ready-made packages" H2: removed.
- Copy was about the South of France only: now 6 regions (Riviera, Provence, Paris and
  Île-de-France, Loire, Bordeaux and Dordogne, Champagne and Burgundy), each with best months,
  lead time, arrival and a guests or venue-hire line.
- Cost section had no numbers: Costs tab with named-source EUR ranges by guest band and line items.
- Legal line was imprecise: now the service-public.gouv.fr rule (1 month continuous residence in
  the commune for either partner or a parent, 10 days of banns, 18+, same-sex rule), in 3 routes.
- Unsourced Gulf and Levant claim: removed.
- Em dash in the closing band: band removed; page has 0 em dashes and 0 en dashes.
- "Wonderland Luxury Advisor": now Wedded Advisor throughout.
- "CONTACT US" and "Start Planning With a Specialist" buttons: replaced with the exact button set
  (Find your region in France, Speak with a Wedded Advisor, Check your date, See all real
  weddings in France, Send your enquiry, Start for free in Wonderland Studio).
- No enquiry form, real weddings, B16, How it works, Privileges: all added.
- Compare Destinations linked only Italy and Greece: now Italy, Greece, Portugal, Switzerland,
  Turkey and the Europe hub.

## Blocks used

B8 proof strip (no venue-offer count, it would read 0) · B9 qualifier under the H1 (carries into
the form) · B16 spotlight straight after section 1 · region chooser in place of B15 · B6 real
weddings · B5 celebrations · B11 guest website and Studio · B13 Travel link · B1 How it works ·
B2 Privileges Tier 1 · B3 form (destination France, region, ceremony type, guest band, budget band,
season) · B14 advisor band · B10 FAQ (10) · B7 articles and trending row.

## Still to check before publishing

- [ ] Nic: is any France package page planned? When one ships, the B15 grid replaces the region
      cards in section 2 and the regions move down to section 4.
- [ ] Nic: destination-level "from" figure. Left out (comment in the quick-answer box).
- [ ] TEMPLATES open item 8: OK to show third-party EUR cost ranges with source and year?
- [ ] Child pages: when `/destinations/europe/france/{paris,provence,french-riviera}` return 200,
      point the region buttons at `data-child-url` and switch to "See Paris weddings",
      "Compare Provence venues", "See French Riviera weddings". Then point the ItemList at them.
- [ ] Legal page: `/destinations/legal-requirements/france` 308s here today, so it is not linked.
      Remove the redirect in the same release as the T20b page and add the link (comment in the
      Marrying legally tab).
- [ ] Flight times from Sydney, Melbourne, Brisbane, Perth, Los Angeles, New York, London and Dubai:
      not shown. Add only from airline schedules.
- [ ] ETIAS: start date not stated on purpose. Confirm on travel-europe.europa.eu and add it.
- [ ] Eurostar "about 2 hours 16 minutes": confirm on eurostar.com.
- [ ] Evergreen article slugs guessed (marked `data-verify`): symbolic ceremony (WC3-T147) and how far
      ahead to plan (WC3-T448). Confirm or remove.
- [ ] Real weddings: confirm each is in France and consent for names. Cards use no couple names.
      Hide the section if fewer than 3 verify.
- [ ] Trending links use the `/trending/` slugs (live sitemap), not the donor-sheet root slugs.
- [ ] Privileges: name hotel programs (Four Seasons, Virtuoso, Rosewood Elite, Mandarin Oriental
      Fan Club) only once confirmed for France properties.
- [ ] Advisor phone number for the B14 band.
- [ ] Form endpoint `/api/concierge/enquiry` (same as the Cappuccina draft): confirm with dev.
- [ ] Header, footer, fonts and colours are a stand-in. Use the site's shared components.
- [ ] Staging: fix the double-slash canonical. Live Europe hub: fix the
      `/destinations/europe/amalfi-coast-wedding` link (missing `/italy/`).

## Link donors to update (outside this page)

- `/trending/inside-mario-ho-and-ming-xis-long-awaited-wedding-at-a-historic-french-castle`: add a
  contextual link to this page.
- `/trending/mondo-duplantis-and-desir-inglanders-cte-dazur-wedding`: add a link here (and to the
  Riviera page once live).
- `/a-luxury-4-day-chateau-destination-wedding-in-loire-valley-france`: link here, anchor "wedding in France".
- `/top-10-french-bridal-boutiques`: optional link here.

## Images to supply

Every image slot is a `<div class="ph" data-img="...">` with an aria-label as alt text. Set
`IMG_BASE` in the page script (for example `/img/destinations/france/`) or replace with `<img>`.
The live page has 9 images; this layout uses about 50.

| Files | Where |
|---|---|
| wedding-in-france-loire-chateau-long-table-golden-hour.jpg | Hero (alt carries "wedding in France") |
| france-loire-chambord-golden-hour, france-champagne-reims-chalk-cellar, france-paris-place-vendome-seine-dusk, france-riviera-villa-ephrussi-cap-ferrat, france-provence-lavender-stone-mas, france-bordeaux-vineyard-chateau-harvest, france-croquembouche-chateau-staircase | B16 spotlight |
| france-region-*.jpg (6) | Region cards |
| france-why-*.jpg (5) | Reason cards |
| france-setting-*.jpg (6) | Ceremony settings |
| france-inclusions-croquembouche-closeup.jpg | Inclusions |
| france-guests-chateau-breakfast.jpg | Guests |
| rw-*.jpg (5) | Real wedding covers (from each story) |
| cel-*.jpg (5) | Celebrations |
| france-advisor-planning.jpg | Beside the form |
| art-*.jpg, tr-*.jpg, eu-*.jpg | Article, trending and Europe thumbnails (reuse existing covers) |

## Sources

- https://www.service-public.gouv.fr/particuliers/vosdroits/F930 (re-checked 19 Oct 2026; updated 16 Sep 2026)
- https://weddingsabroadguide.com/wedding-in-france.html
- https://wedding.wayanbarre.com/en/guides/how-to-plan-a-destination-wedding-in-france-the-complete-guide/
- https://www.frenchweddingstyle.com/planning-a-destination-wedding-in-france/
- https://www.frenchweddingvenues.com/
- https://chateaubeeselection.com/top-20-best-wedding-venues-in-france/
- https://www.theknot.com/content/france-marriage-requirements
- https://www.hitchedinfrance.com/venues
- https://mollycarrphotography.com/france-wedding-venues/
- https://www.france.fr/en/destination/ (loire-valley, champagne, paris, cote-dazur, provence, bordeaux)
