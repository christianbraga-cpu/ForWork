# SERP research: wedding destinations august

Run: 2026-11-24, fast mode. Source: DataForSEO `serp_organic_live_advanced` (desktop, en, depth 10). Pages read with Firecrawl. All competitor pages are reference only.

## Scope of this run (lean, as briefed)
- Keyword "wedding destinations august", 5 locations: Sydney, Melbourne, New York, Dubai, Singapore. All 5 returned results (New York and Dubai needed retries after DataForSEO 40101 "Internal SE Server Error").
- Not run (lean scope set by the caller): the other 5 locations in locations.yaml (Los Angeles, Abu Dhabi, Riyadh, Doha, Hong Kong), the Arabic query in Dubai/Riyadh, and AU secondary-keyword SERPs.
- Organic result URLs came back as `google.com/goto` redirects, so URLs in serp-*.json come from Google's breadcrumbs (some truncated).

## Per region

| Location | AI Overview | PAA | Top 3 organic | Destinations the ranking pages list |
|---|---|---|---|---|
| Sydney | Yes (async, text not returned) | none | Reddit r/weddingplanning "Destination wedding in August, suggestions?"; Great Destination Weddings (AU directory, homepage); Facebook group video "Would we recommend an August destination wedding?" | Northern Italy, southern France, Spain, Netherlands, Switzerland/Ticino (Reddit); Bali, Thailand, Fiji; Cyprus, Greek islands (#5 Perfect Weddings Abroad); Scottish Highlands, Ibiza (#6 CN Traveller); Ko Samui, Riviera Maya (#8 Lonely Planet) |
| Melbourne | Yes (async) | none | Brendan Creaser Photography (Victorian summer, wrong intent); Hello May (ideas); Oliver's Travels (trends) | Mornington Peninsula; Cotswolds to Bahamas (LOVE BRAND); Croatia, Iceland (**our own Pinterest pin, #5**); Gippsland (Easy Weddings forum, 2018); Australia, Bali, Fiji; Santorini, Lake Como (Yahoo, Nov 2026) |
| New York | Yes (async) | Is August a good month to have a wedding? / Which destination is best for a wedding? / How much did Virat Kohli's marriage cost? / Is $10,000 expensive for a wedding venue? | Christa Taylor Photography; forums block (Reddit, Tripadvisor "August destination HELP", The Knot "Outdoor August wedding?"); Events of a Lifetime (US destinations) | Maui, Maldives; Puerto Rico, Costa Rica, Jamaica, Belize, Dominican Republic, Aruba, Greece, Italy, Croatia (Elite Daily 2017); Kiawah Island, Big Sur, Florida Keys, Martha's Vineyard |
| Dubai | Yes (async) | none | IMPACT Collective "Top 10 Summer Wedding Destinations for 2026"; The Romantic Tourist (25 venues, Nov 2026); Pinterest warm-weather venues | Tuscany, Santorini, Amalfi Coast, Napa, Maui, Lake Como, Riviera Maya, Banff, Provence, Hamptons; Berlin, Seychelles, French Riviera, Dubai, Turkey, Abu Dhabi, Austria (Marriott Traveler) |
| Singapore | Yes (async) | none | Pinterest (The Knot flowers, off-topic); Lemon8 x2 (generic) | Dolomites, Grand Tetons, Bali, Maui, St Lucia; French Polynesia, South Africa, Mauritius, Kenya, Zanzibar, Scotland, Bali (Mariee Travel, honeymoon); Puglia, Santorini, Arcangues |

Related searches: "best wedding destinations august", "wedding destinations august europe", "best places to get married in Australia", "best wedding venues Thailand".

## Pages read (top 3, deduped, reference only; saved in 02-research/pages/)

| Page | Words | Headings | Pricing | Real weddings | FAQ/schema | CTA | Images | Strengths | Gaps |
|---|---|---|---|---|---|---|---|---|---|
| perfectweddingsabroad.co.uk/august-weddings (competitor operator, UK) | ~350 own copy | H1, H2 | none on page | none | none seen | phone, Start Planning, sale banner | card images | Only true month page in the SERP; part of a 12-month series; in image pack in all 5 cities | Thin; no reasons per place; UK only; no weather or hemisphere logic |
| impactcollective.com top-10 summer 2026 (competitor planner, US) | ~650 | H1, H5 per item | none | none | none | contact "dream team" | 10 | Clean "Best for / Venue vibe" format; ranks #1 Dubai | Summer, not August; no heat, crowds or Ferragosto; no southern options; no sources |
| cntraveller.com gallery (editorial, 2023) | long gallery | H2 per place | none | none | none | affiliate hotel links | gallery | Gives a "best time" window per place | Its own windows put Lake Como and Santorini outside August; not month-led |

Reddit and Facebook were in Sydney's top 3 but are forum/UGC, not read.

## Cross-region summary
- **Intent:** mixed and under-served. No result in any city answers "where should we marry in August" well; most are generic destination lists or summer lists. Forums rank because people ask the exact question. Informational with commercial investigation.
- **Guest counts / pricing shown:** none of the ranking pages show either.
- **Top concern (real wording):** "Is August a good month to have a wedding?" (PAA, NY); "Would we recommend an August destination wedding?" (FB, AU); "Outdoor August wedding?" (The Knot forum). Heat, crowds and peak pricing are the implied worries.
- **Gap we can own:** (1) a hemisphere split, northern summer vs southern winter/dry season, which no ranking page does; (2) weather stated only as official met services publish it, linked at the claim; (3) honest August caveats on popular places (Ferragosto, heat, peak rates); (4) every pick links to our own guide with legal steps.
- **Our presence:** weddedwonderland.com already appears in image packs in Melbourne, Singapore and Dubai via /expert-advice/where-to-go-on-honeymoon-in-august, plus /expert-advice/best-places-to-travel-in-august (Singapore) and an old Pinterest pin (Melbourne organic #5). No organic web result yet.
- **recommended_scope:** global (single English page; AU-first framing in tone, northern picks serve US/ME/Asia).

## Search volume (DataForSEO Google Ads, AU and US, 2026-11-24)
Google Ads returned **no volume** (null) for every term in both markets: wedding destinations august, best wedding destinations in august, august destination wedding, where to get married in august, destination wedding in august europe, the same five for september, and for june (US; AU response for june omitted the rows). Also null: destination wedding august, august wedding destinations, best places to get married in august (US).
Reading: each month variant is below Google Ads reporting threshold. Series sizing cannot be done from volume; the SERP evidence (forums ranking, a competitor running a 12-month series, Google's own "best wedding destinations august" related search) shows demand exists but is long-tail. Treat the month series as a low-volume, high-intent cluster that links into the destination guides, not a traffic play. No numbers invented.

## Search Console
Not read. `content-system/seo/gsc.md` needs `mcp__Google_Drive__search_files`, which is not available in this session (only read_file_content without a file id). No GSC figures used.

## Our pages (verified 2026-11-24, Firecrawl)
All 21 requested paths return 200. Robots meta read directly as "index, follow" on mykonos-wedding, best-time-to-get-married-in-greece, mauritius-wedding, getting-married-in-seychelles, getting-married-in-hawaii (these had draft/noindex dates in link-map.csv, which is stale for them). Other paths: 200 and no noindex flag in the link map; robots meta not individually read in fast mode.
Target URL /destination-weddings/wedding-destinations-august returns 404 (free).

## Existing month series and cannibalisation
- No "wedding-destinations-<month>" page exists (site map search "august", link map grep).
- Related month pages that exist: /expert-advice/where-to-go-on-honeymoon-in-august (honeymoon intent; link map still lists the old path /expert-advice/a-guide-on-where-to-go-on-honeymoon-in-august), /expert-advice/where-to-go-on-honeymoon-in-june, -july, -september, /expert-advice/best-places-to-travel-in-august, /the-best-honeymoon-destinations-based-on-the-month-of-your-wedding, /7-gorgeous-in-season-wedding-flowers-for-the-august-bride.
- "Best time" pages: /destination-weddings/best-time-to-get-married-in-greece, -bali, -italy. These own "best time to get married in X"; the new page owns "where to marry in August". Low risk if the month page summarises one line per place and links out for the month-by-month detail, and does not reproduce their weather tables.
- Risk to manage: the honeymoon-in-August page already shows for this query in image packs. Keep the new page wedding-led (ceremony, guests, venues) and cross-link both ways with distinct anchors.
