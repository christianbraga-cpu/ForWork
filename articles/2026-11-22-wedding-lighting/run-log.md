# Run log: Wedding Lighting Ideas for a Glowing Reception (refresh)

## Inputs (from the user, 22 Nov 2026)
- Title: Wedding Lighting Ideas for a Glowing Reception (46 characters; keyword first; not a question; no colon or dash)
- Primary keyword: wedding lighting
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL to refresh (same URL): https://weddedwonderland.com/style-advice/wedding-lighting
- Slug: wedding-lighting
- Primary CMS category: Style Advice
- Type: Guide. Cluster: Decor and Florals.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, change if you want):** the H1 is as given. SEO title "Wedding Lighting Ideas for a Glowing Reception Abroad" (53 characters, in the 50 to 60 meta range), unless the strategist finds it weakens intent.
- **Decision (default):** refresh in place.
  - Read the live page, keep what still holds and rewrite the rest.
  - Same URL, so no redirect.
  - The CMS updates the existing post as a draft revision.
- **Decision (default):** style ideas are practical advice, with no invented statistics or prices. Safety points come only from official sources at the claim: state fire services on candles, open flame and total fire ban days; electrical regulators. Otherwise "check with your venue". No competitor brands, images or supplier names.
- **Decision (default):** a Decor and Florals section is added to link-map from the Firecrawl map. No Wedded World plug, no DRAFT links. 6 to 8 image slots with tight briefs.

## Stages
- **Stage 0 fast (strategist):** DONE.
  - **Finding:** /style-advice/wedding-lighting returns 404 (noindex), and no map found it, so there is no live page to refresh at that URL. The real incumbent is /14-creative-ways-to-use-lighting-in-your-wedding ("14 Creative Ways to Use Lighting in Your Wedding").
  - **Decision (default, change if you want):** publish as a new page at the user's URL /style-advice/wedding-lighting (slug wedding-lighting). Treat the 14-ways page, plus /planning-tips-for-candlelit-wedding-reception for its candle content, as the refresh source. LEGACY-301: 301 the 14-ways page to the new URL after publish, with user approval. The candlelit page stays and gets a non-exact anchor.
  - **Volumes (AU, per month):** wedding lighting 140; fairy lights wedding 90; candle wedding decor 50; outdoor wedding lighting 40; reception lighting 20; ideas 10. Mostly high competition.
  - **SERP:** local hire pages, Amazon, Pinterest and directories. No editorial guide in the top 3 and no PAA. Nobody covers lighting abroad. SEO title "Wedding Lighting Ideas for a Glowing Reception Abroad" (53 characters) kept.
  - **Cluster:** no Decor and Florals hub. /style-advice/wedding-table-decor is the proposed head (DECOR-HUB, FLORALS-PAGE open items). The Decor and Florals section is added to link-map.
  - **Domains:** official fire-service and electrical-regulator domains approved (government); the researcher adds them.
  - **Brief:** 8 H2s.
- **Stage 1 fast (research):** DONE. 32 facts: 18 from our pages, 14 official; 5 legal; no prices.
  - **Old pages:** the 2017 14-ways post is a thin listicle with third-party images (full rewrite). The 2024 candlelit post has a truncated item and promises safety without a source.
  - **Confirmed:** NSW RFS fire ban rules; CFA (tents count as open air; fire pits banned on ban days); Queensland Fire Department; ACCC national sky lantern ban; SafeWork NSW fireworks licence; Energy Safe Victoria on decorative lights and generators. Six domains added.
  - **Gaps:** whether candles count as "fire in the open"; sparklers; destination rules; other states; event electrical rules.
- **Stage 2:** writer launched.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 2,704 reader words (over the brief; v2 trims), 0 dashes, 0 placeholders. Official domains inline: RFS, CFA, QFD, Product Safety, SafeWork NSW, Energy Safe Victoria. None blocked.
  - YAML valid; 33 claims, 21 links (over the 14 to 18 target).
  - Front matter CTA body says "complimentary"; v2 removes it.
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.6:** blocker on the Dubai Civil Defence claim (own page only). Majors: Queensland fireworks wording; "venue's insurance decide"; the concierge outcome promise. Minors: state-rule precision, a recheck-in-the-wedding-week line, hedges.
  - **SEO 4.0:** title rule passes. Majors: 2,704 words (cut about 520); 22 links (drop 4); the fireworks claim not linked at the claim.
  - **Reader (couple):** relevance 3, trust 3, clarity 4, would_enquire 2, "save". Majors: Australian fire-ban detail outweighs the overseas line; the unproven concierge paragraph.
  - Merged request: 04-reviews/v1/merged.md. Conflict on fireworks resolved by deleting the sentence (off-topic).
- **Decision (default):** blog-team/brand/cta-library.md discovery_call body changed from "A complimentary, no-obligation call" to "A free, no-obligation call", in line with the standing never-"complimentary" rule. This affects future articles only.
