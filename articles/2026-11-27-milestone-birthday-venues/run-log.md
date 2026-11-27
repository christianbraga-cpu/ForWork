# Run log: Milestone Birthday Venues for a Party to Remember

## Inputs (from the user, 27 Nov 2026)
- Title: Milestone Birthday Venues for a Party to Remember (49 characters; keyword first; not a question; no colon or dash)
- Primary keyword: milestone birthday venues
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/celebration-ideas/milestone-birthday-venues
- Slug: milestone-birthday-venues
- Primary CMS category: Celebration Ideas. Type: Guide. Cluster: Milestone Birthdays.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent` (hosting a parent's 60th or 70th), anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default):** H1 as given. SEO title from the strategist (50 to 60 characters).
- **Decision (default):** the angle.
  - Milestone birthday venues for this audience: their own 30th or 40th, and a parent's 60th, 70th or 80th.
  - Covers private dining rooms, villas, wineries, yachts, rooftops, and a weekend away or abroad.
  - How to choose: guest count, exclusive use, catering, accommodation, access for older guests, noise and curfew, weather plan.
  - Questions to ask each venue.
- **Decision (default):**
  - Venues named only where we have a live /venue profile (link-map rule 5), with facts as their profile states. No invented capacities or prices.
  - Destination options link our destination hubs.
  - The Milestone Birthdays cluster is new; link-map rule 4 says to link /travel, /destination-packages or /wonderland-concierge for celebrations without a page.
  - Link /celebration-ideas/celebrations-we-plan and /packages where relevant.
  - No Wedded World plug, no DRAFT links.
- **Decision (default):** official sources only where a fact needs one (e.g. state liquor or noise rules, or Smartraveller for a party abroad), linked at the claim; otherwise advice. 1,600 to 2,100 words, 5 FAQs.

## Stages
- Stage 0 and 1 launched in parallel (both save early).
- **01:53 check-in:** both agents are held on MCP permission prompts. Saved: a 00-brief.json stub and 19 facts (our celebration, packages, travel and venue-search pages, plus ACCC). No /venue profiles captured yet. **Decision (default):** the writer waits. A venues guide needs real venue profiles, and starting now would mean a rewrite.
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho WC3-T434 (In Progress).
  - **The cluster is not new:** three milestone birthday pages are live (party ideas, by decade, trip). None targets venues, so the overlap is partial. Link each once with non-exact anchors; do not repeat the ideas list.
  - **Volumes:** the head term has no data. AU: 30th birthday venues 260, 40th 140, 60th party 30, birthday venues sydney 320, melbourne 480. US: 30th 210, 60th 110.
  - **SERP:** marketplaces and single-venue pages; no AU page explains how to choose (the gap).
  - **SEO title:** "Milestone Birthday Venues for 30th, 40th and 60th Parties" (57). Meta 152.
  - Venue profiles were confirmed from the sitemap via Apify but not read (Firecrawl out). The researcher was asked to read each profile before any venue is named.
  - Link map: Milestone Birthdays section added.
- **02:10 check-in:** the research file holds 33 facts incl. 12 live /venue profiles (Aambra, Amarti, Bennys, Crown Sydney, Greyleigh, InterContinental Hayman, Mona Farm, Park Hyatt Sydney, The Valley Estate, W Melbourne, Woodburn Homestead, Yallamundi Rooms). Above the threshold of 5, so the writer started; it re-reads the research before saving.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 2,234 reader words (over the cap); 0 dashes; 0 placeholders. External: accc.gov.au only.
  - YAML valid: 32 claims, 28 links.
  - 11 venue profiles named. The Valley Estate and all venues abroad are left out (thin facts); no yachts; no Smartraveller (no facts in the pack).
  - CTA: Discovery Call.
- Reviews launched (accuracy, SEO, couple reader).
- **Stage 1 fast (research):** DONE (late, after permission holds). 44 facts plus 6 reused ACCC facts, incl. 20 live venue profiles and the three sibling pages.
  - Only Aambra mentions birthdays; Amarti and Crown Sydney say "private celebrations".
  - 6 USD venue prices (unused).
  - **Not found:** no yacht, winery or official page (Smartraveller returned 500).
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.6:** majors on the Aambra superlative, the change-of-mind wording, the unlinked unfair-terms claim, "one set of written terms", and the entry-requirements authority.
  - **SEO 3.8:** majors on the missing demand variants (Sydney, Melbourne, 30th, 40th, 60th), length, and four venue profiles not in link-map (added by the orchestrator).
  - **Reader (couple):** relevance 2, trust 3, clarity 4, would_enquire 2, "save". Fixes: one wedding-profile caveat; cut the Eligible stays perks line; replace the vague fee line.
  - Merged request: 04-reviews/v1/merged.md.
- Stage 4: writer v2 launched.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md.
  - --check: 2,128 reader words (28 over the cap; the copy editor trims); 0 dashes; 0 placeholders. External: accc.gov.au, smartraveller.gov.au.
  - YAML valid: 31 claims, 30 links.
  - All 19 items applied; the Eligible stays line is cut. Dropping "first" in C-03 is correct (N-07 does not rank the question).
- Stage 6: copy editor launched.
- **Stage 6 fast (copy editor):** DONE. final.md 2,081 reader words, 0 dashes, 0 placeholders; YAML 31 claims, 30 links.
  - publish-package.json valid (11 open items; no prices, so no nic_signoff lines).
  - chrome-upload-prompt.md is draft only and creates a new post after a slug check. article.docx built.

## Must-fix before publish
1. NEW-URL: the URL was 404. Create a new post (Zoho WC3-T434).
2. VENUE-RECHECK: the 11 venue profiles were read on 27 Nov via Apify; recheck capacities and spaces before publish.
3. CONF-06: the sibling birthday pages give different lead times (six to nine vs six to twelve months).
4. IMAGE-RIGHTS: venue images only with rights from the venue or our gallery.
5. YACHT-GAP (no yacht partner or facts), CONCIERGE-PAY, WEDDED-WORLD, FIRECRAWL-CREDITS, LINK-CHECK (live checks failed in review), AUTHOR, CMS-URL.
No prices, so nothing for Nic.
