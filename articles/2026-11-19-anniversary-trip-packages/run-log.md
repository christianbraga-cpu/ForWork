# Run log: Anniversary Trip Packages for Couples Worth Booking

## Inputs (from the user, 19 Nov 2026; title and keyword corrected by the user)
- Title: Anniversary Trip Packages for Couples Worth Booking (51 characters; keyword first; no colon or dash)
- Primary keyword: anniversary trip packages. Secondary: packages for couples (320).
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/celebration-ideas/anniversary-trip-packages
- Slug: anniversary-trip-packages
- Primary CMS category: Celebration Ideas (confirmed; added to categories.md)
- Type: New. Cluster: wedding anniversary gifts.
- Brief (user): commercial intent that fits WW's packages and travel advisors; links from the head's trip column to /packages and /travel.
- User rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple` (read as married couples planning an anniversary), secondary `private_client`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, change if you want):** /packages is listed as NOT LIVE in link-map (draft structure). The strategist checks it; if not live, link /destination-packages and /travel and log PACKAGES-PAGE.
- **Decision (default):** brand claims only from our live pages (/travel, /destination-packages, /destination-honeymoon-packages, /wonderland-concierge, any anniversary pages), quoted as worded; SITE-CONFLICTS carries over (no package or Concierge prices without Nic, never "complimentary"); travel-advisor and honeymoon-planner facts reused with original dates.
- **Decision (default):** secondary persona private_client instead of paying_parent (anniversary trips are for established couples).

## Stages
- **Stage 0 fast (strategist):** DONE. AU volumes small: packages for couples 70/month (not 320), romantic getaway packages 50, anniversary trip packages 10. Sydney and Melbourne show retailer catalogues; Brisbane and Perth weak (Facebook thread, budget blog, a for-sale domain at #1). Gap: what an anniversary package includes, package vs DIY vs advisor, booking checklist. Brief: title as given, 7 H2s, 5 FAQs, about 1,900 words, 18 links, discovery_call CTA plus /destination-packages.
- **/packages is not live** (two Firecrawl maps): linking /destination-packages; PACKAGES-PAGE logged for the user.
- **Decision (default):** three live anniversary pages added to link-map (anniversary trip ideas, marking a big anniversary, anniversary party venues); this piece stays commercial and never uses "anniversary trip ideas" as an anchor.
- **Note:** the map shows the two Bali packages articles as live although link-map lists them as DRAFT (held for SITE-CONFLICTS). Flagged to the user.
- **Stage 1 fast (research):** DONE. 50 facts (23 reused, 25 our live pages, 2 official). **/packages loads (HTTP 200)** with an Anniversaries tile, although the Firecrawl map missed it: linked as the user asked; link-map updated. No page publishes an anniversary package or AUD price; no authoritative list of gift themes by year. New site conflicts: "ATAS and IATA accredited, A19892" (unverified; ATIA retired the ATAS name in 2024), proof points 17+ years / 120,000+ / 10,000+ / 800+, "complimentary night", "guaranteed late checkout", Wedded Privileges vs Wonderland Benefits naming; concierge US$ tiers (Nic).
- **Decision (default, change if you want):** none of the conflicting claims, counts, accreditation or prices appear in the copy; Wedded Privileges quoted with "Benefits vary by property and booking."
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md. --check: 2,028 reader words, 0 dashes, 0 placeholders, 3 official domains (ACCC, Smartraveller, Governor-General) inline, none blocked. YAML valid; 30 claims, 17 links; /packages Anniversaries tile quoted and used as the second CTA; no prices, counts, accreditation or banned claims. Five pages from the brief (incl. the cluster head /celebration-ideas/wedding-anniversary-gifts) were not in link-map; now added for the revision.
- **Decision (default, change if you want):** reader review uses the private_client persona (anniversary trips are for established couples; the couple persona is Italy-wedding-led).
- **Stage 3 fast (3 reviews):** DONE. Accuracy 3.8 (majors: "sold at a premium", "five time zones", unsourced inclusions as what we "usually" do, no own-passports caveat, "room and view settled" promise). SEO 4.0 (title rule pass; majors: cluster head not linked, gg.gov.au unlisted). Reader (private client) relevance 2, trust 3, clarity 4, would_enquire 2: "competent mid-market packages, no discretion offering"; privacy blocker overruled as a claim and turned into checklist questions. Merged request: 04-reviews/v1/merged.md.
- **Decision (default, change if you want):** gg.gov.au approved in domains.md (official Governor-General site); cluster head, 25th, 50th and itinerary pages linked; /destination-packages and the honeymoon link dropped to stay at 18 links.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md. --check: 2,038 reader words, 0 dashes, 0 placeholders, 3 official domains, none blocked. YAML valid; 29 claims, 18 links (cluster head, 25th, 50th and itinerary template added; /destination-packages and the honeymoon link dropped). All 17 merged items applied; "A free Discovery Call" kept (CTA library wording).
- **Stage 6 fast (copy editor):** running.
