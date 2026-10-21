# SERP research: lake como villa wedding exclusive use (2026-10-21)
Source: DataForSEO serp_organic_live_advanced (Google, en, desktop, depth 10). Pages read with Firecrawl (Apify web-fetch fallback). Raw SERPs: 02-research/serp-<location_id>.json (+ serp-sydney-head-term.json, serp-new_york-head-term.json). Page text: 02-research/pages/*.md (unreadable URLs in pages/_not-scraped.md).

## Run notes
- 10/10 locations returned results. New York gave DataForSEO 40101 twice and succeeded on the 3rd try; Sydney gave 40101 once.
- Doha: 'Doha,Qatar' was rejected (40501). serp_locations(QA) gives 'Doha,Doha Municipality,Qatar' (code 1011785), which worked. Update locations.yaml.
- Arabic queries were not run (Dubai/Riyadh): the English SERPs are populated, arabiaweddings.com ranks in English, and there is no natural established Arabic query.
- AI Overview at position 1 in all 10 locations (asynchronous; text only captured for the NY head term).
- DataForSEO cost was not returned in responses; check the dashboard.
- GSC: the only Drive export is dated 2025-05-14 (525 days old), so it was not used; gsc-exports/ is empty.

## Demand (Google Ads monthly, AU / US)
Primary and 'exclusive use villa lake como': no data in either. lake como villa wedding 10/70; lake como wedding villa(s) 10/90; villa wedding lake como 10/10; lake como wedding venues 210/2,900; villa balbiano wedding 20/170; villa pizzo wedding 10/110. KD (AU): lake como wedding venues 0, others no data. Related searches in all 10 locations: 'lake como villa wedding exclusive use cost/price/packages/reviews'. Labs related: 'lake como wedding venues with accommodation'.

## Where weddedwonderland.com ranks
No WW URL in any top 10 checked. AU: /best-lake-como-wedding-venues at 73 to 89 for the 'lake como wedding venues' family. US: /lake-como-wedding-guide (now /trending/...) #1 for 'getting married in lake como'; /best-lake-como-wedding-venues 69 to 94; Indian real wedding #19; Villa d'Este page #43.

## Top 3 by location
Sydney: boutique-weddings, villinorubini (all-inclusive), Facebook group. Melbourne: theheritage-collection (Balbiano owner), villinorubini, kissfromfleur. New York and LA: exclusiveitalyweddings, reddit r/BigBudgetBrides, italianvenues. Dubai: exclusiveitalyweddings, infinity-weddingsandevents, victoriavanderberg. Abu Dhabi: kaipoweddings.de, italianlakeswedding (d'Este 2015), Facebook. Riyadh: kaipo, villinorubini (romantic), Facebook. Doha: Facebook, idoinlakecomo, weddingitaly (d'Este). Singapore: paulinayehevents (2020), khalabuzar, Facebook video. Hong Kong: kaipo, villinorubini, Facebook.
PAA: How much does it cost to have a wedding at villa Como? / What are some luxury lake villas suitable for weddings in Lake Como, Italy? / Can you get married at a villa? / Can you legally get married in Lake Como? / How much does a wedding cost in Lake Como?

## Page analysis (14 readable, 7 not)
- exclusiveitalyweddings (~860 words): 15 venue cards across 4 lakes; one line on hotels vs one-day exclusive rental; no rules, prices or FAQ.
- italianvenues (~1,460 words, Jul 2026): best quality. Splits sleep-on-site from event-only and FAI day-use; Balbiano 'from €50,000'; no table, no minimum nights; meta noindex at scrape.
- kaipoweddings (3,200+ words, Jan 2025): 22 venues with unlabelled stat blocks (guests, sleeps, jetty, music times); unsourced.
- villinorubini x2 (~950 / ~1,230 words): self-promoting listicles with factual errors (says Balbiano has no rooms); table and FAQ.
- boutique-weddings (900+ words): cards with a capacity/boat/accommodation flag.
- kissfromfleur (~2,270 words, 2023): first-person tour; hotels and villas mixed.
- infinity (~1,830 words): romantic copy, no rules.
- victoriavanderberg (~1,250 words, Aug 2026): villas vs hotels tiers; 'questions to ask any venue' (exclusive vs shared with day visitors, wet weather, curfew, boat-only); unsourced € ranges; FAQ.
- idoinlakecomo (~1,580 words): 6 venues with capacity, ceremony type, accommodation and access fields.
- paulinayeh (~2,000 words, 2020): insider tips.
- weddingitaly / italianlakeswedding: single Villa d'Este (hotel) pages.
Not readable: Reddit (bot wall), khalabuzar (body not exposed), 5 Facebook items (login-gated). Images were not counted (excluded at scrape) and schema was not inspected.

## Cross-region summary
- Guest counts conflict across sources (Balbiano 100 to 600; rooms none/12/~30).
- Pricing is rare, € only, unsourced; there is no AUD anywhere.
- Top concern: exclusive-use cost, sleeping on site, legal ceremony, finding a villa that is truly private.
- Gap: no page limits itself to whole-property exclusive-use villas, answers the same rule fields per villa from official sources, or addresses long-haul Australian guests.
- Regional differences are small: US has planners/Reddit/PAA; AU has the owner site and Facebook; Gulf/Asia have kaipo, arabiaweddings and older posts.
- recommended_scope: au_focus.

## Link verification 2026-10-21
- Live and indexable: hub /destinations/europe/italy/lake-como-wedding; /destinations/europe/italy; /expert-advice/how-much-does-a-lake-como-wedding-cost (root 301s here); /expert-advice/how-do-you-get-a-lake-como-wedding (root 301s here); /expert-advice/what-is-included-in-lake-como-wedding-packages; /expert-advice/getting-married-in-italy-...; /trending/lake-como-wedding-guide (old path 301s here); /best-lake-como-wedding-venues (not in the link map: add it); /venue/villa-balbiano; /venue/villa-pizzo; /wonderland-concierge; /wonderland-studio; /travel.
- /privileges: 404, noindex.
- External, all 200: Smartraveller getting-married-overseas (new path); Smartraveller Italy; theheritage-collection.com/villa-balbiano/; villapizzo.eu; fondoambiente.it Balbianello.

## Cannibalisation
LOW for the target keyword, MODERATE for the villa/venue cluster (/best-lake-como-wedding-venues and the hub). Do not target 'lake como wedding venues'; link up to the hub; get a backlink from /best-lake-como-wedding-venues; consider refreshing that listicle later.
