# Run log: Couples Experiences Worth Travelling For

## Inputs (from the user, 27 Nov 2026)
- Title given: 20 Couples Experiences Worth Travelling For
- Primary keyword: couples experiences
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/travel-guides/couples-experiences
- Slug: couples-experiences
- Primary CMS category: Travel Guides. Type: Guide. Cluster: Tours and Experiences.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, TITLE-RULE):** the given title starts with "20", so it is not keyword first.
  - H1: "Couples Experiences Worth Travelling For" (40 characters). The number moves to the H2 "Our 20 couples experiences".
  - SEO title from the strategist (50 to 60 characters). Revert if you prefer the original; same pattern as the Africa and February pages (TITLE-SERIES).
- **Decision (default):** an editorial list of 20 experiences, grouped by type: food and wine, water and islands, wildlife, wellness, culture and art, adventure, slow travel.
  - **Each experience:** where (only destinations with our live pages), why it suits a couple, best season only as an official source or our page words it, and one honest caveat. A safety or permit line is linked at the claim to the official source (e.g. national park permits, marine park rules, Smartraveller for activities).
  - No named operators unless our /vendor profiles cover them; no invented prices, perks or durations; figures in original currency (Nic).
- **Decision (default):**
  - Links: our destination hubs, the honeymoon pages (/honeymoon-ideas/*; the African honeymoon target URL), /travel, /destination-packages, /packages, /wonderland-concierge.
  - The honeymoon itinerary hub is DRAFT, so not linked (RETRO-LINK).
  - Check redirects (og:url). No Wedded World plug.
- **Decision (default):** 2,000 to 2,600 words (20 short cards), 5 FAQs. The copy editor saves blog-team/templates/experiences-list.md if the pattern is reusable.

## Stages
- Stage 0 and 1 launched in parallel (both save early).

## 02:52 check-in and stage 1 hand-back
- Strategist done: URL 404 (new post), Zoho WC3-T441 (WW-343). SEO title "Couples Experiences Worth Travelling For Around the World" (57). Volumes AU 590, US 880. SERP is local date ideas and vouchers. Sibling overlap with /travel-guides/private-tours and /travel-guides/experiences-by-occasion (link both; RETRO-LINK from them). /wedded-wonderland-experiences is do-not-link. 7 safety domains need approval (DOMAINS-ADD).
- Research at 49 facts, threshold met. Writer v1 started with an inline brief; shortlist items without facts get swapped for researched ones (SHORTLIST-SWAP).
- Researcher still running, held on an MCP permission prompt.

## Writer v1 (done) and reviews started
- 03-draft-v1.md: 2,548 reader words, 0 dashes, 0 placeholders, YAML ok (56 claims, 53 links). External domains: smartraveller.gov.au, gbrmpa.gov.au, webstatic.niwa.co.nz.
- 13 shortlist swaps and 7 reframes (SHORTLIST-SWAP). Meta rewritten to match the cards (META-CHANGE, 137 characters).
- Decisions for the user: VENUE-NAMING (/venue profiles treated as allowed), ORIENT-EXPRESS (named operator with no /vendor profile), LINK-MAP-ADD /honeymoon-ideas/oceania-honeymoon, DOMAINS-ADD gbrmpa.gov.au and NIWA.
- Fact-checker, SEO reviewer and couple reader started in parallel.
