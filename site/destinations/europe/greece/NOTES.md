# Greece destination page: build notes

Page: `/destinations/europe/greece` (this folder's `index.html`)
Action: FIX, live but broken. Pillar 1. Destinations. Template T2 Country destination, adapted (island chooser instead of offer grid).
Brief: research dated 14 and 15 Oct 2026. Built 19 Oct 2026.
Status: ready for JJ and writer review. The page stays `index, follow` because the live page is already indexed; the open questions below should be cleared before it replaces the live page.

## SEO set-up

| Item | Live (15 Oct) | This build |
|---|---|---|
| Title | "Greece Wedding Venues: Curated Island & Mainland Luxury \| Wedded Wonderland" (75 chars) | "Greece Wedding \| Santorini, Crete & Island Venues \| WW" (54 chars). Alternative from the brief: "Wedding in Greece \| Islands, Venues & Legal Guide" (49). |
| Meta | n/a | 151 chars, carries "Greece wedding", the islands, legal by passport, Wedded Advisor. No price promise. |
| H1 | "Greece Wedding Venues" | "Get married in Greece, from a caldera terrace to a Cretan olive estate" |
| Canonical | correct on live, double slash on staging | `https://weddedwonderland.com/destinations/europe/greece` |
| Keywords in intro | n/a | Sentence 1: "Greece wedding" and "wedding in Greece". Sentence 2: "Greece wedding venues". |
| Schema | TouristDestination, Service, BreadcrumbList, FAQPage, Organization, WebSite | Organization, BreadcrumbList, TouristDestination (containedInPlace Country + Place Europe), ItemList (Santorini page + 5 offers, no prices), Service (Wedded Concierge, areaServed Greece), FAQPage (10, text matches the visible FAQ). Keep the site-wide WebSite node from the shared layout. |

H2 order matches the brief's section plan: B16 spotlight, island chooser, why Greece, settings, tabbed guide, inclusions (with traditions strip as H3), guests, real weddings, celebrations, advisor (steps, privileges, form, speak-to-an-advisor band), FAQ, articles plus trending, more of Europe.

## Removed from the live page (per brief and the 14 Oct rules)

- "Discover Greece's Finest Venues & Vendors" Marketplace module
- "Ready-made packages" H2 and the duplicate Rocabella card
- "within one business day" promise (form confirmation now has no time frame)
- Palm Island Suites line
- "Wonderland Luxury Advisor" in the menu (now "Wedded Advisor")
- Unsourced "Gulf and the Levant" claim
- Wendy El-Khoury's culture note (held back pending the decision in open questions)
- Unsourced cost section and the US-only legal section (replaced by sourced tabs)

## Brief rules applied

- No WW price and no competitor offer price anywhere. Costs tab shows only named third-party EUR ranges with guest band and year.
- Santorini offers show "Price on enquiry" and "View offers" only. No "{N} venues with offers" count.
- B8 written exactly as "120,000+ celebrations" and "17+ years".
- Legal answer split AU, US, UK, plus same-sex and Orthodox lines. The 8-day licence wait and 40-day registration are stated for US citizens only. The newspaper notice is left out (applies only with a Greek partner).
- Notice that civil ceremonies cannot be held at archaeological sites is NOT on the page (unverified; confirm with a municipality before adding).
- Real-wedding cards use first names only (consent rule). "Lia Georgantis" shows as "Lia".
- Trending links use the root slugs (the /trending/ paths 308 to them). Traditions link uses the 301 target `/8-greek-wedding-traditions-you-didnt-know-about`.
- Enquiry posts to `/api/concierge/enquiry` with `route_to=wedded-concierge`, `destination=Greece`, island and ceremony type fields. Island card buttons prefill the island. The B9 checker carries season, guest band and celebration into the form. **Confirm the endpoint and field names with dev.**

## Links held back (switch on when the target is live)

- [ ] `/destinations/legal-requirements/greece`: today it 308s to this page, so linking it would loop. The "Check the full rules for Greece" link sits in an HTML comment in the Marrying legally tab. Remove the redirect and uncomment when T20 ships.
- [ ] `/destinations/europe/greece/mykonos` and `/crete`: 404. Mykonos and Crete cards route to the enquiry for now (comments mark where to swap).
- [ ] `/real-weddings/destination/greece`: 404. "See all real weddings in Greece" points to `/real-weddings` until the gallery exists (needs 6+ tagged).
- [ ] `/destinations/europe/spain`: 404. Commented slot in "Explore more of Europe".
- [ ] `/wonderland-studio` (Start for free) and `/honeymoons`, `/travel`, `/concierge`, `/privileges`, `/contact`: guessed paths, confirm.

## Open questions (from the brief, still open)

- [ ] Santorini child page is linked from the chooser. Index it (remove noindex) and add it to the sitemap with this release?
- [ ] OK to run the island chooser with a 5-card Santorini strip instead of the 6-offer grid?
- [ ] AU and UK couples: confirm with a municipality or the Greek Ministry of Interior whether the 8-day licence wait and 40-day registration apply the same way. Until then the copy states them for US citizens only.
- [ ] OK to cite Big Fat Greek Day, Weddings Abroad Guide, Destination Wedding Directory and Johnny Africa by name in the Costs tab?
- [ ] Wendy's culture note: keep a short founder line, or leave it out (current build)?
- [ ] Pyrgos Taverna capacity: card copy avoids a number because the source says both "up to 35" and "garden reception up to 150".
- [ ] The Dunes Carpe: no setting or capacity in the brief. Card says "Ask your Wedded Advisor". Add one fact line.
- [ ] Koufeta source is a Sydney parish Facebook post. Swap for Visit Greece or a museum source if found.
- [ ] Wedded Privileges sub-lines are generic; confirm Tier 1 wording, and name hotel programmes only where WW can confirm them for Greek properties.

## Writer checks (written by this build, not in the brief's sources)

- [ ] Island card guest ranges ("Intimate to 100+", "Caldera venues 2 to 35") and setting-card guest ranges and best times: sense-check with the Concierge team.
- [ ] Month ratings in When to go (Jan to Mar, Nov, Dec rated Low; "many island venues run seasonally").
- [ ] Getting there: route lines are deliberately general (Gulf or Asian hub from Australia; New York and Los Angeles; London). Verify before adding named airlines or nonstops.
- [ ] Planning timeline months are a general guide, not sourced.
- [ ] Heatwave line converts travel.state.gov's "over 100°F" to "can top 38°C (100°F)".

## Dev defects to log (not fixable in this file)

- [ ] Greece, Italy and France return 200 but are missing from the live sitemap.
- [ ] Staging canonical has a double slash.
- [ ] Header, footer, fonts and colours are a stand-in, matching the Cappuccina draft. Swap in the shared site layout and tokens.

## Off-page link work (from link-donors.json)

- [ ] `/love-island-greek-wedding-anna-mcevoy` (34 clicks, pos 8): add a body link to this page, anchor "wedding in Greece".
- [ ] `/8-greek-wedding-traditions-you-didnt-know-about` (54 clicks, pos 9) and `/5-timeless-greek-engagement-traditions` (62 clicks, pos 7): add a link to this page from the intro.
- [ ] Link this page from `/destinations/europe` and from each Santorini package page.

## Images to supply

Every image slot is a `<div class="ph" data-img="...">`. Upload the photos and set `IMG_BASE` in the page script (for example `/img/destinations/greece/`), or replace each slot with an `<img>`. Use descriptive file names and island-specific alt text (image packs show in AU, US and UK). Hotel-supplied photos only for the Santorini offer strip; consented images only for real weddings and the same-sex couple shot.

| Slot | Files |
|---|---|
| Hero | greece-wedding-santorini-caldera-terrace-sunset.jpg (also the og:image) |
| Spotlight (6) | greece-wedding-santorini-caldera-imerovigli.jpg, -mykonos-windmills-little-venice.jpg, -crete-chania-lighthouse-dusk.jpg, -rhodes-lindos-chapel-st-pauls-bay.jpg, -corfu-old-town-lane.jpg, -athens-riviera-acropolis.jpg |
| Island cards (6) | greece-wedding-island-santorini-caldera.jpg, -mykonos-windmills.jpg, -crete-olive-estate.jpg, -athens-riviera-terrace.jpg, -rhodes-lindos-chapel.jpg, -corfu-old-town.jpg |
| Santorini strip (5) | offer-pyrgos-taverna.jpg, offer-rocabella.jpg, offer-santo-winery.jpg, offer-santorini-gem.jpg, offer-the-dunes-carpe.jpg |
| Reasons (5) | why-signing-the-register.jpg, why-island-arrival-ferry.jpg, why-rhodes-medieval-town-wall.jpg, why-caldera-sunset-ceremony.jpg, why-same-sex-couple-terrace.jpg |
| Settings (7) | setting-caldera-terrace.jpg, setting-cycladic-chapel.jpg, setting-cretan-olive-estate.jpg, setting-mykonos-beach-club.jpg, setting-athens-riviera-villa.jpg, setting-lindos-chapel.jpg, setting-orthodox-church-stefana.jpg |
| Inclusions | inclusions-koufeta-tulle.jpg |
| Guests | guests-boat-day.jpg |
| Real weddings (6) | rw-*.jpg (from each real wedding post) |
| Celebrations (6) | celebrate-*.jpg |
| Articles, trending, siblings | art-*.jpg, trend-*.jpg, sib-*.jpg (reuse each page's own feature image) |

## Sources

Official: https://gr.usembassy.gov/getting-married-in-greece/ · https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Greece.html · https://greece.embassy.gov.au/athn/marriages.html · https://www.smartraveller.gov.au/destinations/europe/greece · https://www.gov.uk/foreign-travel-advice/greece/entry-requirements · https://www.gov.uk/marriages-civil-partnerships-abroad/get-documents-for-a-marriage-or-civil-partnership-abroad
Tourism: Visit Greece pages for Santorini, Mykonos, Crete, Rhodes, Corfu, Athens.
Costs and season: bigfatgreekday.com, weddingsabroadguide.com, destinationweddingdirectory.co, johnnyafrica.com, theknot.com (1 to 15 August holiday).
WW offers: staging Santorini page (releasing-weddedwonderland.vercel.app/destinations/europe/greece/santorini).
