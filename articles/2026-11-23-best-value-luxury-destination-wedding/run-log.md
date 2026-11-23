# Run log: Best Value Luxury Destination Weddings Ranked

## Inputs (from the user, 23 Nov 2026)
- Title: Best Value Luxury Destination Weddings Ranked (45 characters; keyword first; not a question; no colon or dash)
- Primary keyword: best value luxury
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/destination-weddings/best-value-luxury-destination-wedding
- Primary CMS category: Destination Weddings. Type: guide. Cluster: average wedding cost.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, change if you want):** the H1 is as given. SEO title "Best Value Luxury Destination Weddings Ranked by Region" (54 characters).
- **Decision (default):** the URL status is checked first. If it is live, refresh in place; if not, create a new post after checking the CMS for the slug.
- **Decision (default):** the ranking is our editorial judgement, with transparent criteria.
  - Figures come only from our live cost guides (Italy, Lake Como, Amalfi, Santorini, Maldives, Fiji), quoted as worded with currency, year and guest count.
  - No conversions, no computed per-guest figures, no cross-currency arithmetic. Nic signs off every figure.
  - Bali is not ranked on cost (SITE-CONFLICTS).
  - No competitor rankings or figures.
- **Decision (default):** this page answers "where is luxury best value". It links to the live /expert-advice/average-destination-wedding-cost-by-region and the cost guides for averages. "Value" means quality per dollar at the luxury end, not cheap.

## Stages
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho: WC3-T567, plan ref WW-269, In Progress. Zoho files it under the "Destination Wedding Guide 2026" cluster. **Decision (default):** keep the user's "average wedding cost" cluster and flag the mismatch (CLUSTER-CHECK).
  - **Volumes (AU):** "best destination wedding locations" 30; the other four none (Zoho plan says US 450).
  - **SERP:** a directory, an old US video, Pinterest, a quote form and old roundups. Nobody ranks by luxury value with a stated method.
  - **Cannibalisation:** partial only. Found live and not in link-map: /destination-weddings/how-much-is-a-destination-wedding, which duplicates the by-region page (DUP-PAGE, user decision; not linked). Added to link-map.
  - **New site conflict:** our two Lake Como pages give different 60-guest figures (Nic to pick).
  - **Brief:** 8 H2s, 7 destination cards.
- **Stage 1:** the researcher is held on an MCP permission prompt.
- **Stage 1 fast (research):** DONE. 37 facts: 17 reused, 20 new; all 22 prices flagged for Nic.
  - **Current figures:** Italy, small Italy weddings, Lake Como, Amalfi, Santorini, Maldives, Fiji, Bali, Dubai (per person).
  - **Unchanged:** no reused figure has changed since 19 Nov.
  - **New conflicts (pages published 17 Nov):**
    - Lake Como: EUR 45,000 to 90,000 vs EUR 80,000 to 150,000 for 60 guests.
    - Bali: a third range, US$20,000 to 60,000 for 80 guests.
  - **Gaps:** no published totals for Thailand, Mexico, France, Portugal, Crete or Puglia.
- **Decision (default):**
  - Lake Como and Bali are quoted with no figure (Lake Como ranked on other criteria; Bali outside the ranking).
  - Destinations without totals are not ranked.
  - The ranking is presented as our editorial judgement with stated criteria. Nic approves the method (RANKING-METHOD).
- **Stage 2:** writer launched.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md. --check: 2,792 reader words (over), 0 dashes, 0 placeholders, Smartraveller inline. YAML valid: 33 claims, 24 links. Ranking: 1 Santorini, 2 Fiji, 3 Dubai (per person), 4 Maldives, 5 Amalfi, 6 Lake Como (no figure); Bali outside; Italy overall not ranked. Reviews launched.
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.6:** blocker on Dubai figures resting on an unnamed 2026 round-up. Majors: ranking framed as calculated ("per dollar", "more room than anywhere"); several unsourced phrases; concierge wording beyond live copy.
  - **SEO 3.7:** majors on meta length; three URLs not in link-map; cards reproducing spoke breakdowns; 2,792 words; Italy intent (link the Italy hub and Puglia).
  - **Reader (couple):** relevance 2, trust 3, clarity 3, would_enquire 2, "save". Santorini #1 "because its table is clear" undermines the ranking; Italy at 5 and 6; Puglia excluded for an internal reason.
  - Merged request: 04-reviews/v1/merged.md.
- **Decision (default):**
  - Dubai is removed from the ranking (one unranked line, no figures; DUBAI-SOURCE). The ranking is now five.
  - Each card is ranked on destination merits "in our view", with one headline figure.
  - SEO title "Best Value Luxury Destination Weddings Ranked With Costs" (56 characters; "by Region" was inaccurate).
  - The Fiji cost, Dubai cost and hidden-costs URLs are added to link-map (live per Firecrawl).
