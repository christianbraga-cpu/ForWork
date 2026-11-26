# Run log: Destination Wedding Cost per Guest Explained

## Inputs (from the user, 26 Nov 2026)
- Title: Destination Wedding Cost per Guest Explained (44 characters; keyword first; not a question; no colon or dash)
- Primary keyword: destination wedding cost per guest
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/destination-weddings/destination-wedding-cost-per-guest
- Slug: destination-wedding-cost-per-guest
- Primary CMS category (as given): Real Weddings. Type: Pillar. Cluster: Destination Wedding Costs.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **CATEGORY-MISMATCH (for the user):** categories.md limits Real Weddings to client case studies with consent. This is a cost pillar under /destination-weddings/.
  - **Decision (default):** keep Real Weddings as given, and recommend Destination Weddings as primary, with Real Weddings secondary only if real wedding cost breakdowns are featured.
  - The upload prompt uses whatever you confirm.
- **Decision (default):** H1 as given; SEO title the same or the strategist's version within 50 to 60 characters.
- **Decision (default):** the pillar for the Destination Wedding Costs cluster.
  - **What makes up a per-guest cost:** venue hire vs per-head catering, minimum spends, accommodation, transfers, welcome and farewell events, and who pays what for guests.
  - **Per-guest figures** only where our own live cost pages or real wedding cost breakdowns state them, quoted as worded with currency, year and guest count. No computing per-guest numbers from totals, no conversions, no cross-currency comparison. Nic signs off every figure.
  - Links out to the cost spokes (by region, hidden costs, all-inclusive, Lake Como, Amalfi, Santorini, Maldives, Fiji, Dubai, Bali).
- **Decision (default):** cannibalisation check against /expert-advice/average-destination-wedding-cost-by-region, the hidden costs page and the all-inclusive page.
  - /expert-advice/wedding-cost-per-guest is live, but link-map says do not link or quote it (an A$38,252 figure from a blocked source; SITE-CONFLICTS), so it is not linked.
  - DUP-PAGE pages are not linked. No DRAFT links, no Wedded World plug.
- **Decision (default):** official sources only where needed (e.g. Smartraveller on travel insurance for guests; ACCC on deposits, reused from earlier packs with original dates). 2,200 to 2,800 words, 5 FAQs.

## Stages
- Stage 0 and 1 launched in parallel (both save early).
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho WC3-T324 (In Progress) sets the primary category to Destination Weddings.
  - **SERP:** no result gives per-guest costs for a wedding abroad (domestic venue pages and old US content). That gap is the angle.
  - **Volumes:** "cost per person" and "who pays for guests" 10 AU and 10 US; the head term has no data in DataForSEO. Zoho claims 2,800 (VOLUME-CONFLICT).
  - **SEO title:** "Destination Wedding Cost per Guest and Who Pays for What" (56 characters). Meta 150 characters.
  - **Cannibalisation:** partial overlap with the by-region, hidden costs, all-inclusive and who-pays-guest-travel pages; all linked with descriptive anchors. /expert-advice/wedding-cost-per-guest stays unlinked.
  - **Redirects:** /real-weddings/lake-como-wedding-cost redirects to the expert-advice Lake Como page. The all-inclusive canonical is /destination-weddings/all-inclusive-wedding-cost.
  - **SITE-CONFLICTS:** the Maldives green tax is "per night" on one page and "per day" on another.
  - Firecrawl credits ran out (FIRECRAWL-CREDITS); Apify used instead.
- **Decision (default, changed):** the primary category is Destination Weddings, because Zoho WC3-T324 and categories.md both say so. Real Weddings is dropped as primary (CATEGORY-SWITCH: revert if you want Real Weddings).
- **23:23 check-in:** the researcher is held on an MCP permission prompt. 67 facts saved (23:20) across 14 of our cost pages, plus ACCC and Smartraveller. Above the threshold of 4 pages, so the writer started on the saved facts with an inline brief.
- **Stage 1 fast (research):** DONE. 76 facts (28 reused, 8 official, 0 legal); 17 price lines for Nic.
  - **Per-guest figures found:** Dubai AED 200 to 595 pp; Maldives US$250+; Fiji FJD 130 to 180+ per extra guest; Phuket US$70 to 160; Italy EUR 110 to 300+ catering; Amalfi EUR 180 to 310+; Santorini EUR 75 to 160+; Mykonos EUR 80 to 300+; Le Ciel EUR 190 per missing guest.
  - **SITE-CONFLICTS:**
    - The Lake Como page was rewritten on 25 Nov (now EUR 120k to 200k for 60 guests), so older packs are stale.
    - Maldives green tax: per night vs per day.
    - Bali: three different figures.
    - Dubai: the minimum spend low end differs.
    - Mykonos: the page arithmetic does not add up.
  - **Gaps:** no real client breakdown; no welcome dinner price; mira.gov.mv blocked.
  - The conflicts were sent to the writer (no conflicting figure stated as fact).
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 3,069 reader words (over the 2,800 cap); 0 dashes; 0 visible placeholders. External: accc.gov.au, smartraveller.gov.au.
  - YAML valid: 46 claims, 29 links. The front matter author field is a [[NEEDS]] (AUTHOR).
  - All figures are in nic_signoff. Conflicts are kept out of the copy. Both Santorini drinks rates were cut (EUR 20 vs EUR 25 low end).
  - The Phuket figure is unlinked (the page is not in link-map).
- Reviews launched (accuracy, SEO, couple reader).
