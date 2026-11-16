# Run log: Honeymoon Planner Services Explained

## Inputs (from the user, 16 Nov 2026)
- Title: Honeymoon Planner Services Explained
- Primary keyword: honeymoon planner
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/honeymoon-ideas/honeymoon-planner
- Slug: honeymoon-planner
- Primary CMS category: Honeymoon Ideas (confirmed by the user; added to categories.md)
- Type: Guide. Cluster: Honeymoon Planning Service.
- Language: Australian English, AUD
- Personas: primary `couple`, secondary `paying_parent` (advisory), anti `bargain_hunter`
- Mode: FAST; strategist and one research batch in parallel (reuses the travel-advisor packs)
- Markets: Sydney, Melbourne, Brisbane

## Decisions
- **Decision (default, change if you want):** service explainer: what a honeymoon planner does, what you get, when it is worth it, vs booking direct and vs a general travel agent, what to check. Do not repeat the travel-advisor article (pay, accreditation, room blocks) or the brief article (template); link both conditionally (DRAFT). Explain and link /destination-honeymoon-packages without reproducing its inclusions list. Brand claims only from live pages and existing packs, cautious wording; no prices (live page USD conflicts with brand-profile), no ATIA claim, no "never discount". Consumer facts reused (ACCC, Smartraveller). 1,600 to 2,200 words.

## Stages
- **Stage 0 fast (strategist):** DONE. DataForSEO AU returned no volume for 24 variants (same API gap as 15 Nov; not proof of zero demand). SERPs: no top-10 page explains what a honeymoon planner does (parked domain, holding page, agency homepages, a DIY spreadsheet). PAA: cost, how far ahead, realistic budgets. No cannibalisation; /destination-honeymoon-packages medium overlap (explain and link, never copy its list). Brief: 7 H2s, 1,600 to 2,200 words; travel_benefits CTA, discovery_call soft line.
- **Stage 1 fast (research):** DONE. 42 facts (30 reused, 12 new from the live honeymoon page). Page: "LUXURY DESTINATION HONEYMOON PACKAGES", "Our concierge curates your honeymoon anywhere in the world"; 5 steps (share your vision, meet your specialist, tailored shortlist "with suite categories and inclusions made clear", leave the details to us, arrive and unwind); "a dedicated specialist from enquiry to arrival"; inclusions vary by resort; "One team. Every detail."; enquiry form or call with a specialist. Proof points 10,000+/75+/1,200+ conflict with 800+/54; USD price range and "never discount" on the page; testimonials not to be quoted.
- **Decisions (default, change if you want):** proof points only 800+ and 54 countries (brand-profile) or none; no prices; no testimonials; no "never discount"; do not use "a honeymoon specialist who has stayed at these properties" until confirmed (unverifiable claim about staff); no claim about the 320 "Honeymoon journeys" catalogue; lead time 6 to 9 months attributed to /destination-packages.
- **Stage 2 fast (writer, 4 min):** DONE. 03-draft-v1.md. --check: 2,383 reader words (183 over the 2,200 cap; writer estimated 2,000 to 2,100), 0 dashes, 0 placeholders, 2 domains. YAML valid; 23 claims, 16 links (two travel guides conditional).
- **Stage 3 fast (3 parallel reviews):** accuracy FAIL 3.6 (blocker: no confirm-for-your-own-passport line; major: support "while you are away" implied); SEO changes requested (DRAFT sibling links; 183 over); reader:couple 3/3/3/2 (blocker R-01: steering and pay model unanswered, a user input; fee line x4; brochure steps; four contact routes). User asked 16 Nov for CONCIERGE-PAY, SHORTLIST-SCOPE, MID-TRIP-SUPPORT.
- **Stage 4 fast (one loop, 3 min):** DONE. 03-draft-v2.md. --check: 1,957 reader words (range 1,600 to 2,200), 0 dashes, 0 placeholders, 2 domains. YAML valid; 23 claims, 16 links. FAQs 6 to 4 (removed repeats).
- **Stage 6 fast (copy editor):** DONE. final.md, publish-package.json (image plan included), chrome-upload-prompt.md, article.docx. --check: 1,957 reader words, 0 dashes, 0 placeholders, 2 domains, none blocked. YAML and JSON validated by the orchestrator. Link map: added as DRAFT. Run time: about 35 minutes.

## Must fix before publish
1. **User facts (asked 16 Nov):** CONCIERGE-PAY (how we are paid on honeymoon bookings, any fee), SHORTLIST-SCOPE (partner properties only or any hotel), MID-TRIP-SUPPORT (support during the trip or "enquiry to arrival" only). The reader rated would_enquire 2 and flagged steering as a blocker without them.
2. **Publish order (SIBLING-LINKS):** publish both /travel-guides articles first, or delete each sentence that links to a sibling that is not live.
3. **N-008:** whether Wonderland Benefits apply to honeymoon resorts (the travel_benefits CTA is scoped to /travel partner properties).
4. **Website fixes (marketing):** honeymoon page proof points (10,000+/75+/1,200+) conflict with 800+/54; USD price range; testimonials to verify; "has stayed at these properties" to confirm.
5. **Links:** click through the 3 external links once.
6. **Images:** pick files; credit, licence and consent for 6 slots.
7. **CMS:** author, CMS admin URL, tag check.
