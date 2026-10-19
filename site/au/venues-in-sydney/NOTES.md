# Wedding Venues in Sydney: fix notes

Page: `/au/venues-in-sydney` (this folder's `index.html`)
Action: FIX, live but broken (plan row KEEP · P3 Fix live page · pillar 2 Venues · owner Christian · JJ approves)
Template: T5 Vendor category (Wedded Marketplace), city-child variant, adapted for venues
Page type: D, directory listing
Status: Draft for JJ. Keeps `index, follow` and the self canonical, because it replaces the live page at the same URL.

## URL decision (open question 1, JJ to confirm)

- Scope URL `/venues/australia/sydney` is 404 on live and staging. **Do not build it.**
- Fix the live page in place at `/au/venues-in-sydney` (TEMPLATES.md section 5, Still open item 2, option (a)), on the T5 frame (option (b) is viable now: 14 metro venues is above the 3-venue minimum).
- If a move happens later, 301 only after the new URL is indexed.

## Defects on the live page and how this draft fixes them

| # | Live defect | Fix in this draft |
|---|---|---|
| 1 | Greyleigh (Jerrara, near Kiama) and The Jackson Ranch (Bawley Point) are on the grid but are not in Sydney | Removed from the grid, the counter and the ItemList. Linked once in a "Weekends away from Sydney" line under the grid (open question 2) |
| 2 | Intro promises "capacities, packages, and real photography"; cards show type and suburb only | Every card shows suburb and area, type, seated capacity, ceremony on site, rooms on site, price line, 3 photo slots, Enquire and Save |
| 3 | Addresses inconsistent ("The Rocks, The Rocks NSW", "Sydney, Australia", "Belmore, Australia") | One pattern: suburb plus area, for example "The Rocks · Harbour and CBD" |
| 4 | Meta description oversells "beach-front cliffs" and "harbour-side estates", has an em dash, is over 155 characters | New meta (149 characters), no dashes, only claims the list supports |
| 5 | 4 em dashes and 7 en dashes in visible text, including the FAQ H2 | Zero em or en dashes in the draft (ranges written as "to") |
| 6 | FAQ cost figures ($8,000 to $40,000+; $15,000 to $25,000 for 100 guests) have no source | Removed. Cost block and FAQ use sourced ranges only, each named and dated |
| 7 | "Hunter Valley ... a short drive north" is wrong | Removed. No Hunter Valley claim on the page |
| 8 | "explore the listings below" sits under the listings | Removed |
| 9 | "Are the venues verified?" answers with no method | Replaced by a "See how we choose Sydney venues" section with the listing criteria, reviewer and last updated date |
| 10 | Peak season stated as "October to April" | Spring (September to November) and autumn (March to May), matching One Fine Day and DestinationWeddings.com (open question 6) |
| 11 | "Wedding inspiration" block: a podcast and event news, no real weddings | Replaced by 6 Sydney real weddings with venue credits |
| 12 | No filters, counter, area grouping, curation method, cost block, Choose how you plan or Pro band | All added (see section plan) |
| 13 | "Visy Dior Hotels International" reads as a company name; the card name has a trailing space | Card shows the listing name trimmed, flagged for the Marketplace team to confirm the venue's trading name |
| 14 | Generic og:image (site Home.png) | og:image points to a Sydney harbour image slot (upload needed) |
| 15 | Card alts are the venue name only | Alts follow "{Venue} wedding reception, {suburb}, Sydney" |
| 16 | Schema: the brief records CollectionPage, ItemList, BreadcrumbList and FAQPage on the 14 Oct crawl; a Firecrawl pass on 19 Oct returned no JSON-LD in the server HTML | Draft ships all four in the server HTML. Dev to check whether the live JSON-LD is client-injected, and render it server side |

Staging before release (not on this page's HTML, but blocks the release):

- `/venue/southern-highlands-estate` is confirmed test data (location "Jallukur", copy for a different property, "Oceanfront Cliff Lawn" inland, type "Castles", "From USD $1,500"). It must not appear on the Sydney grid. Who deletes it in Marketplace admin? (open question 4)
- `/venue/machine-hall` reads as a real listing (300 seated, external catering only) but its address is only "Sydney, Australia". Get the suburb and consent, then add it to the right area group; the counter and title then read 15.
- Staging canonical points at the staging host. Make sure production renders the production canonical.

## Section plan as built

| # | H2 (JJ voice) | Block | Notes |
|---|---|---|---|
| 1 | H1: Find your Sydney wedding venue, from the harbour to the beaches | B8 | First sentence carries "wedding venues in Sydney". Area plus type search, live counter, proof strip (120,000+ celebrations planned, 17+ years, 14 Sydney venues listed) |
| 1b | See why couples choose Sydney Harbour | B16 | Straight after the intro, as T5 requires for city pages. 6 shots, button "Compare Sydney harbour venues" |
| 2 | Compare 14 wedding venues in Sydney | ItemList | Filters: area, venue type, guests, ceremony on site, rooms on site, cultural expertise, price band (hidden until question 3 is answered). Server HTML groups cards under area H3s (National Trust pattern). Advisor card inline after card 6. "Weekends away from Sydney" line |
| 2b | Find a venue by style | | Anchors #small, #waterfront, #garden, #luxury, #beach, #affordable: one paragraph each. Carries the intent of the 5 dropped style child URLs plus "cheap" |
| 2c | Marry on the harbour, then celebrate at your venue | | Public ceremony sites with published fees and capacities, paired with nearby listed venues |
| 3 | Browse wedding venues in other cities | | Dubai and Ras Al Khaimah only (3+ venues). AU cities hidden until each has 3+. Plus Sydney vendors |
| 4 | See how we choose Sydney venues | | Curation method, reviewer, last updated |
| 5 | Know what a Sydney wedding venue costs | | Sourced ranges in AUD, named and dated. No WW package prices |
| 6 | Ask these 5 questions before you book | | Links "What Should You Do on a Venue Site Visit?" |
| 6b | Marrying in Sydney from overseas | | 3 lines: NOIM timing, symbolic option, link to the destination page (once live) and Concierge |
| 7 | See real weddings at Sydney venues | B6 | 6 covers with venue credits |
| 8 | Build the rest of your Sydney team | | Vendors, planners, DJs |
| 9 | Hand the search to a Wedded Advisor | B4, B11 | Three routes plus Studio band. No B1 or B2 (directory rule) |
| 10 | List your Sydney venue | B12 | "List your venue" |
| 11 | Get answers before you enquire | B10 | 8 FAQs, FAQPage |

## Metadata

- Title: `Wedding Venues Sydney: Compare 14 Venues | Wedded Wonderland` (60 characters). The brief's pattern with a second pipe ran to 61, so the first separator is a colon. Update the number if Machine Hall is added.
- Meta description (149): `Compare 14 Sydney wedding venues by area, guests and setting, from harbour hotels to Mosman and Cronulla. See capacity, then enquire with each venue.`
- H1: `Find your Sydney wedding venue, from the harbour to the beaches`
- Breadcrumb: Home > Venues (`/venue`) > Wedding Venues in Sydney. Keep `/venue` at level 2 until `/vendors` exists.

## Keywords

| Keyword (AU) | Volume | Where it is served |
|---|---|---|
| wedding venues sydney / sydney wedding venues | 6,600 | Title, H1 area, first sentence, grid H2 |
| cheap wedding venues sydney | 590 | #affordable paragraph, cost block, FAQ 2 ("affordable" wording) |
| small wedding venues sydney | 390 | #small paragraph, guests filter "Up to 50" |
| garden wedding venues sydney | 260 | #garden paragraph, ceremony sites block |
| waterfront wedding venues sydney | 170 | #waterfront paragraph, spotlight |
| luxury wedding venues sydney | 110 | #luxury paragraph (WW already has impressions at pos 73) |
| beach wedding venues sydney | 110 | #beach paragraph |
| sydney wedding | 390 | Not targeted. Belongs to `/destinations/oceania/australia/sydney` |

Cannibalisation split: this page targets "wedding venues sydney" and lists venues; the destination page targets couples travelling to Sydney. Each links to the other once (the link here is in the overseas block and is commented out until the destination page returns 200).

## Schema

CollectionPage with an ItemList of 14 EventVenue items (name, url to the profile, PostalAddress, maximumAttendeeCapacity where verified), BreadcrumbList, FAQPage. No AggregateRating (no first-party reviews). No Offer prices. Add `geo` per venue from the Marketplace record when the template renders it.

## Internal links on the page

- Parent: `/venue`. Children: the 14 metro `/venue/{slug}` profiles, plus `/venue/greyleigh` and `/venue/the-jackson-ranch` in the weekends line.
- Siblings: `/au/vendors-in-sydney`, `/au/wedding-planners-in-sydney`, `/au/wedding-djs-in-sydney`, `/ae/venues-in-dubai`, `/ae/venues-in-ras-al-khaimah`.
- Service: `/wonderland-concierge`, `/wonderland-studio`, `/business`.
- Articles: "What Should You Do on a Venue Site Visit?" (WC3-T473), "Who Can Legally Marry You?" (WC3-T175). Slugs are placeholders until the articles publish: search the page for `TODO-slug`.
- Real weddings: 6 of the 10 in brief section 11.

Link donors to update (outside this page): `/a-look-inside-emma-freedmans-chic-sydney-wedding` (one body link "Sydney wedding venues"), `/sydneys-top-20-proposal-locations`, `/sydneys-top-10-luxury-hotels-to-spend-your-wedding-night` (hotel names to their `/venue` profiles), and the old listicles in brief section 11 (open question 9).

## Open questions for JJ

1. URL: confirm fix in place at `/au/venues-in-sydney` (recommended).
2. Out-of-area venues: the draft keeps Greyleigh and The Jackson Ranch as a "Weekends away from Sydney" line only. Drop them entirely instead?
3. Venue-supplied per-head bands on cards: inside the 14 Oct price rule? Until confirmed, every card says "Price on enquiry" and the price filter and "Under $150 per head" preset stay hidden (`hidden` attribute).
4. Staging: who deletes "Southern Highlands Estate"? Machine Hall's suburb and consent?
5. Cost figures: the draft replaces the unsourced live figures with the sourced ranges below. OK?
6. Peak season: draft uses spring and autumn (sourced), not the live "October to April".
7. Cannibalisation split with `/destinations/oceania/australia/sydney`: agree before either ships.
8. Hotel programme marks (for example Four Seasons partner status): not used until permission is confirmed.
9. Old Sydney venue listicles: link here, or consolidate? Needs a GSC check per URL. WW's own "Top 20 Wedding Venues In Sydney" post showed in a US search for the head term on 19 Oct, so it competes with this page.
10. Reviewer for the curation section: draft says "Reviewed by the Wedded Marketplace editors". Name a person for the byline.

## Facts used and their sources

Verify before publish. Market: Sydney, AUD.

| Fact on page | Source |
|---|---|
| Per-head reception ranges AUD 95 to 320 on venue cards, October 2026 | https://www.easyweddings.com.au/WeddingVenues/Sydney/ (figures rotate; cite as "ranges seen on Easy Weddings, October 2026") |
| Reception budget around AUD 150 to 300 or more per person | https://onefinedayweddingexpo.com.au/wedding-hub/wedding-tips/best-wedding-venues-sydney/ |
| Royal Botanic Garden lawns: 3-hour hire AUD 2,000, extra hour AUD 515, parking permit AUD 102, GST inclusive | https://www.botanicgardens.org.au/venues-and-lawns/all-venues-and-lawns/tarpeian-lawn-sydney-harbour |
| Harbour Trust: 2-hour hire from AUD 400 (up to 160 guests) to AUD 1,000 (Harbour View Lawn above Chowder Bay, up to 130) | https://www.harbourtrust.gov.au/venue-hire/wedding-venues/ |
| NSW average venue spend 2026 AUD 18,662; national AUD 17,518 for about 85 guests (replaces the brief's older "about AUD 16,000") | https://www.easyweddings.com.au/articles/wedding-venue-cost/ and https://www.easyweddings.com.au/articles/wedding-cost/ (Easy Weddings 2026 report) |
| Clarence House: about AUD 80 to 130 per head; 150 guests Saturday about AUD 16,500 to 19,500; Friday or Sunday 15 to 20% less | https://www.clarencehouse.com.au/wedding-planning/how-much-does-a-wedding-at-clarence-house-actually-cost/ (Aug 2026). Venue's own published figures used in editorial copy, not on the card (see open question 3) |
| Bradleys Head Amphitheatre AUD 1,210 for 3 hours, up to 120, Monday to Saturday, closed 22 Dec to 1 Feb | https://www.nationalparks.nsw.gov.au/venues/bradleys-head-amphitheatre |
| Shakespeares Point, Nielsen Park AUD 880 for 3 hours, up to 120, closed 25 Dec to 1 Jan | https://www.nationalparks.nsw.gov.au/venues/shakespeares-point |
| City of Sydney parks AUD 880 iconic, AUD 451 neighbourhood, 3 hours, up to 35, apply 4+ weeks ahead (fees from 1 July 2026) | https://www.cityofsydney.nsw.gov.au/lists-maps-inventories/fees-and-charges-for-outdoor-venue-hire |
| Northern Beaches ceremony permit AUD 498 for 3 hours | https://www.northernbeaches.nsw.gov.au/community/weddings-on-northern-beaches |
| Waverley (Bondi, Bronte, Tamarama): up to 50 guests, beaches closed December and January, allow 10 business days, fee not published | https://www.waverley.nsw.gov.au/recreation/use_of_public_spaces/weddings_and_private_ceremonies |
| June is Sydney's wettest month on average (133.1 mm, Observatory Hill) | https://www.bom.gov.au/climate/averages/tables/cw_066062_All.shtml |
| Crown Sydney deposit: 10% of estimated costs or AUD 2,000, whichever is greater, contract within 14 days | https://www.crownsydney.com.au/events-and-conferences/weddings (FAQ) |
| Book 12 to 18 months ahead for peak Saturdays | One Fine Day FAQ; WeddingHero; DestinationWeddings.com |
| Spring (September to November) and autumn (March to May) are the popular seasons | DestinationWeddings.com |
| Harbour events: opera on the harbour in March and April; light festival in May and June | https://www.sydney.com/destinations/sydney/sydney-city/sydney-harbour |
| NOIM at least 1 month and no more than 18 months before; authorised celebrant; two witnesses 18 or over | Verified 19 Oct: https://www.ag.gov.au/families-and-marriage/marriage/get-married and https://www.nsw.gov.au/family-and-relationships/marriages/getting-married-nsw |
| Venue capacities on cards | See the capacity table below |

Corrections to avoid: Sydney is not Australia's capital. Docklands, St Kilda and Yarra Valley are Melbourne.

## Venue data on the cards

Scraped 19 Oct 2026 from each WW profile, cross-checked against the venue's own site. **10 of 16 profiles show a round "300 seated" headline that the venue's own figures contradict.** The cards use the verified figure; the Marketplace team should correct the profiles so card and profile agree. Where only a total guest figure exists (not seated), the card label reads "Guests", not "Seated". Official figures for the big hotels came from search-result snippets of the official pages; confirm each with the venue.

| Venue | Area on card | Card capacity | WW profile says | Source of card figure | Ceremony on site | Rooms |
|---|---|---|---|---|---|---|
| Crown Sydney | Harbour and CBD | Seated up to 320 | 320 | WW (Pearl Ballroom) | Yes (Pavilion, 40 standing) | Yes |
| Four Seasons Hotel Sydney | Harbour and CBD | Seated up to 480 | 300 | fourseasons.com/sydney/weddings/venues (Grand Ballroom banquet) | Ask the venue | Yes |
| Hyatt Regency Sydney | Harbour and CBD | Guests up to 550 | 300 (About says 1,000) | hyatt.com weddings page (per ballroom) | Yes | Yes |
| InterContinental Sydney | Harbour and CBD | Guests up to 400 | 300 | 2022 wedding brochure (Boronia Ballroom); may be dated | Ask the venue | Yes |
| Park Hyatt Sydney | Harbour and CBD | Seated up to 120 | 200 | hyatt.com weddings page (The Gallery) | Ask the venue | Yes |
| The Langham, Sydney | Harbour and CBD | Guests up to 200 | 200 | langhamhotels.com events (Grand Ballroom) | Yes | Yes |
| W Sydney | Harbour and CBD | Guests up to 650 | 300 | marriott.com events (The Great Room) | Yes | Yes |
| Yallamundi Rooms | Harbour and CBD | Seated 150 to 180 | 300 (that is the cocktail figure) | sydneyoperahouse.com venue hire | Ask the venue | No |
| Weddings and Events at Taronga | Lower North Shore and Mosman | Seated up to 450 | 300 (About says Marquee 450) | WW About copy (The Marquee) | Yes (3 outdoor sites) | Yes |
| The Brighton Hotel, MGallery | Southern Sydney and Cronulla | Seated up to 320 | 300 | thebrightonsydney.com.au (Endeavour Ballroom; Brighton Ballroom up to 600 guests) | Yes | Yes |
| Benny's | Southern Sydney and Cronulla | Seated up to 80 | 80 | WW (no official site found; Shire Scout says 16 to 140) | Ask the venue | No |
| Visy Dior Hotels International | Western Sydney and the Hills | Seated up to 300 | 380 (room list says 375 seated, text says 300 seated, 375 cocktail) | WW room text (Giorgia Grand Ballroom) | Yes (garden gazebo) | Yes (132 rooms) |
| The HIGHLINE Venue | Western Sydney and the Hills | Guests 250 to 600 | 300 | highlineevents.com.au (Sapphire Ballroom) | Ask the venue | No |
| Clarence House | Western Sydney and the Hills | Guests up to 580 | 300 (About says 350) | clarencehouse.com.au (The Lemnos 320 to 580+) | Yes | No |
| Greyleigh (weekends line) | Kiama hinterland, about 90 min | not on grid | 300 | Official max 250 (The Gables) | Yes | Yes (sleeps 18) |
| The Jackson Ranch (weekends line) | Bawley Point, about 3.5 h | not on grid | 180 | Official PDF up to 200 (2022) | Yes | Yes (up to 40) |

Area note: Belmore and Bankstown sit in Canterbury-Bankstown (south-west). They are grouped under "Western Sydney and the Hills" per the brief's facet list; the area intro names them as south-west. Rename the facet "Western and South-west Sydney" if JJ prefers.

Profile fixes for the Marketplace team (from the 19 Oct scrape):

- Correct the headline capacities above, and add an Event spaces section (seated, cocktail per room) to every Sydney profile. Only Crown and Visy Dior have one.
- Visy Dior: trailing space in title and og:title; Grand Ballroom "375 seated" is the cocktail figure; Sofia Ballroom "160 seated" is cocktail (120 seated); semicolon typo in the tagline.
- The HIGHLINE Venue: broken video embed ("Sorry. This video does not exist.") that injects a second H1. Benny's and The Jackson Ranch show an empty "Video tour" heading.
- "Australia, Australia" repeated in the location on 8 profiles; Four Seasons and Park Hyatt addresses duplicated.
- Type labels: Benny's tagged "Yachts"; Taronga tagged "Banquet Hall" and "Private Estates"; Crown leads with "Banquet Hall".
- Thin bulk-imported profiles (Four Seasons, Hyatt Regency, InterContinental, Langham, W, Clarence House): templated About copy and 4 to 7 photos. Request galleries.
- Park Hyatt and The Brighton show an unrelated wedding veil article; Sydney profiles show Woodburn Homestead (South Australia) as a "similar venue".
- Greyleigh's hero file is named "JR.WP-41.jpg": confirm it is a Greyleigh photo.
- Hub `/venue`: H1 renders "Where Your WeddingBegins" (missing space); no visible breadcrumb.
- `/destinations/oceania/australia/sydney` (404) carries both `index, follow` and `noindex` robots tags.

## Images to supply

Every image slot is a `<div class="ph" data-img="...">`. Upload and set `IMG_BASE` in the page script, or swap each slot for an `<img>` with the alt shown in its `aria-label`.

| File | Where |
|---|---|
| spot-01-opera-house-bridge-dusk.jpg | Spotlight: landmark, Circular Quay East at dusk |
| spot-02-ballroom-harbour-windows.jpg | Spotlight: ballroom set for a wedding with harbour windows (InterContinental, Four Seasons or Crown gallery) |
| spot-03-botanic-garden-ceremony.jpg | Spotlight: garden lawn aisle with the Opera House behind |
| spot-04-mosman-headland-golden-hour.jpg | Spotlight: couple on a Chowder Bay headland |
| spot-05-ferry-guests.jpg | Spotlight: ferry or water taxi with guests at a wharf |
| spot-06-walsh-bay-night.jpg | Spotlight: wharf under the Bridge at night |
| {slug}-1.jpg to {slug}-3.jpg | 3 per venue card, from each `/venue/{slug}` gallery; first image is the room set for a wedding, not the exterior |
| rw-*.jpg | Real wedding covers (WW library) |
| studio-guest-list.jpg | Studio band |
| pro-venue-team.jpg | Pro band (member supplied, not stock) |
| og-sydney-harbour.jpg | og:image, 1200 x 630 |

## Build notes

- Header, footer, fonts and colours reuse the stand-in from the Cappuccina draft, with nav links pointed at real live URLs. Swap in the site's shared header and footer.
- Filters run client side on the server-rendered cards, so crawlers see every venue and every area H3. Filter state is mirrored to the URL hash (`#area=harbour`), so style anchors and the spotlight button can preset the grid.
- Card "Enquire" opens the venue profile's enquiry form with `?enquire=1&from=au-venues-in-sydney` (hidden fields venue slug and page slug, per the brief). Confirm the param names with dev.
- The inline Advisor card posts to `/api/concierge/enquiry` (same placeholder endpoint as the Cappuccina draft). **Confirm the real endpoint.**
