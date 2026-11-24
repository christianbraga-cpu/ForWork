# Run log: Wedding Venue Comparison Spreadsheet and What to Compare

## Inputs (from the user, 24 Nov 2026)
- Title: Wedding Venue Comparison Spreadsheet and What to Compare (56 characters; keyword first; not a question; no colon or dash)
- Primary keyword: wedding venue comparison spreadsheet
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/expert-advice/wedding-venue-comparison-spreadsheet (type "new")
- Slug: wedding-venue-comparison-spreadsheet
- Primary CMS category: Expert Advice. Cluster: wedding planning spreadsheet.
- Brief (user): the venue shortlist tab as its own page, with strong internal links to the Marketplace venue search (/search?tab=vendors) and destination venue pages.
- Rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default):** H1 and SEO title as given (56 characters; passes the rule and the meta range).
- **Decision (default):** URL status checked first. If live, refresh in place; if not, create a new post after a CMS slug check.
- **Decision (default):** /search?tab=vendors is checked first (link-map marks /marketplace NOT LIVE). If it loads, it becomes the main venue-search link and is added to link-map. If not, fall back to /venue and the city venue pages, and log it.
- **Decision (default):** the comparison table is our own template, with no invented prices or venue facts. Official sources (ACCC deposits and refunds) are used only where a fact needs one, reused with original dates. No Wedded World plug, no DRAFT links.

## Stages
- **00:37 check-in:** no hand-back from the strategist or the researcher after 15 minutes (likely held on permission prompts). The research pack has 10 reused facts (saved 00:22). **Decision (default):** the writer started on the saved facts with an inline 7-H2 brief. /search?tab=vendors is linked once, pending MARKETPLACE-SEARCH-CHECK (must be confirmed live before publish).
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md (the research pack had grown to 21 facts).
  - --check: 2,342 reader words (over); 0 dashes; 3 visible [[NEEDS: AUD approximation]] placeholders (against the no-conversion rule; removed in v2). Official domains: ACCC, Energy Safe Victoria, Smartraveller.
  - YAML: one unquoted value fixed by the orchestrator; now valid, 26 claims, 25 links.
  - /search?tab=vendors lists vendors by category (F-19), so the anchor became "search planners, caterers and stylists in our Marketplace". The SEO review checks for a venue filter.
  - Reviews launched. The strategist and researcher are still held on permission prompts.
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.6:** two blockers, both ACL overstatements (deposit FAQ and takeaway). Majors: AUD placeholders; Dubai wording; "who shares the pool"; package inclusions caveat; "Marketplace" misnaming.
  - **SEO 3.8:** majors on /search?tab=vendors (not in link-map, not a venue search); 2,342 words; the spreadsheet intent (competitors offer a copyable Sheet).
  - **Reader (couple):** relevance 3, trust 3, clarity 4, would_enquire 2, "save and forward". Bali-heavy examples; visible placeholders; product names unclear. The planner-vetting blocker is downgraded as out of scope.
  - Merged request: 04-reviews/v1/merged.md.
- **Decision (default):**
  - /venue (filters by city and guest count) is the primary venue-search link.
  - /search?tab=vendors is kept once, as the user asked, with the anchor "search planners, caterers and stylists among our trusted vendors", and added to link-map.
  - DESIGN-SHEET (a copyable Google Sheet or .xlsx) is logged for before publish.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md: 2,006 reader words, 0 dashes, 0 placeholders, ACCC and Smartraveller inline (the generator line was dropped). YAML valid: 26 claims, 20 links. All 20 items applied. ACL wording fixed; /venue is the primary venue search; vendor search linked once as "trusted vendors". The orchestrator moved the /search?tab=vendors link-map row out of "Do not link" into section 4.
- **Stage 0 fast (strategist, late, after the permission hold):** DONE.
  - **URL:** 404, so a new post. Zoho WC3-T1016 (To-Do, TK-106).
  - **Marketplace venue search:** found at /search?tab=venues ("Exceptional Venues", 78 venues; filters by location, capacity and type; 200, noindex). Added to link-map. The copy editor was told to make it the primary venue-search link; /search?tab=vendors stays once.
  - **Volumes (AU / US):** keyword 30 / 320; questions to ask a venue 90 / 2,400; planning spreadsheet 390 / 2,400.
  - **SERP:** paid templates and pin boards; nobody offers a free table, column weighting or venue-abroad columns. The draft already covers these.
  - **Cannibalisation:** go.
  - **Note:** the site header still links /marketplace, which link-map marks NOT LIVE (MARKETPLACE-HEADER, for the user).
