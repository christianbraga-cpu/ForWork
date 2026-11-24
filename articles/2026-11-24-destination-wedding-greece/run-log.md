# Run log: Destination Wedding in Greece Guide for Couples

## Inputs (from the user, 24 Nov 2026)
- Title: Destination Wedding in Greece Guide for Couples (47 characters; leads with a close keyword variant; not a question; no colon or dash)
- Primary keyword: destination wedding greece
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/destination-weddings/destination-wedding-greece
- Slug: destination-wedding-greece
- Primary CMS category: Destination Weddings. Type: Guide. Cluster: Destination Wedding Guide 2026.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, change if you want):** H1 as given ("Destination Wedding in Greece" reads naturally and is accepted as keyword first). SEO title "Destination Wedding in Greece Guide for Australian Couples" (57 characters).
- **Decision (default):** URL status checked first. If live, refresh in place; if not, create a new post after a CMS slug check.
- **Decision (default):** this is the planning overview for Greece (where, when, legal route in brief, budget, guests, timeline). It links out to the hub and every live spoke rather than repeating them. The cannibalisation check is against /destinations/europe/greece, the Greece licence, best time, venues, packages, same-sex, two-day and Santorini cost pages, and the UK guide (DRAFT).
- **Decision (default):** Greek legal facts (Australian route) and Smartraveller Greece facts are reused with their original dates. Santorini figures are quoted as worded in EUR (Nic). Legal confirmation goes to the municipality and the Australian embassy, never the advisor. No Wedded World plug, no DRAFT links.

## Stages
- **Stage 1 fast (research):** DONE. 52 facts: 27 reused with original dates; 12 legal; 7 prices for Nic. The URL is 404, so a new post. All seven of our Greece pages are live and were read today. Smartraveller Greece: "exercise normal safety precautions"; up to 90 days in any 180.
- **SITE-CONFLICTS (for the user and Nic):**
  - Santorini capacity: four different figures across our pages.
  - Season: May to October (hub) vs April to October (best-time page).
  - Document age: three months (packages page, one venue's terms) vs six months (Australian Embassy Athens).
  - The Greece hub's legal section is written for US citizens and says the advisor handles legal matters, which conflicts with our rule that legal confirmation goes to the authority.
- **Decision (default):** none of the conflicting figures is quoted. Season is attributed to each page as worded, or given as "check the best-time guide". Document age comes from the Australian Embassy only.
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho WC3-T688 (WW-281, To-Do).
  - **Volumes (AU / US):** destination wedding greece 30 / 480; santorini wedding 90 / 590; greece wedding cost 10 / 140.
  - **SERP:** hotel pages, pins and hotel lists. No Australian planning overview ranks.
  - **Cannibalisation:**
    - The legacy /how-to-plan-a-destination-wedding-in-greece-if-youre-overseas overlaps totally (LEGACY-301 after publish, user approval).
    - The hub overlaps partly and owns "greece wedding venues", which clashes with /greece-wedding-venues (HUB-KEYWORD).
    - The other spokes are summarised and linked. Do not link 13-reasons or /favorite-destination-weddings-in-greece.
  - **Venue filter:** /search?tab=venues&country=Greece shows only one venue, so the plain venue search is linked.
  - SEO title 58 characters.
- **Stage 2:** writer launched.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 2,597 reader words (over); 0 dashes; 1 visible [[NEEDS]] (flight routes). Seven official domains inline, none blocked.
  - YAML valid: 43 claims, 34 links.
  - Conflicting figures cut (Santorini capacity, document age).
- **Link map (orchestrator, from the brief):**
  - 15 Greece spokes and venue profiles added (Santorini, Mykonos and Crete venues, packages and cost pages; Greek Orthodox; traditions).
  - Greece licence row set to LIVE.
  - Duplicates and older Greece pages marked do not link.
  - The legacy planning page is marked for a 301.
- **Note for the user (UK-GREECE-URL):** the old URL /destination-weddings/if-youre-thinking-of-getting-married-in-greece-you-need-to-know-this now shows the title "Getting Married in Greece from the UK Step by Step". It looks as if the UK refresh was published in place at the old URL, not at /destination-weddings/getting-married-in-greece-from-uk. Please confirm which URL is live.
- Reviews launched.
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.6:** majors on the unsourced Santorini cap line, "walked and confirmed" step-free routes (not a live service), timeline CNI timing, and the flights placeholder.
  - **SEO 4.2:** majors on island cards not linking their spokes, and length with the legal section overlapping the licence spoke.
  - **Reader (couple):** relevance 3, trust 3, clarity 4, would_enquire 2, "save and forward". Majors: the placeholder; the partner-properties Benefits line raising the commission worry.
  - Merged request: 04-reviews/v1/merged.md.
- **Conflict resolved:** the flights paragraph uses the accuracy wording ("check with your airline or travel advisor"), not "the islands add one more leg".
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md: 2,423 reader words, 0 dashes, 0 placeholders. Official domains: mitos.gov.gr, greece.embassy.gov.au, ag.gov.au, heraklion.gr, smartraveller.gov.au. YAML valid: 43 claims (C-07 and C-43 removed from body), 34 links. All 20 items applied; spokes linked with non-exact anchors; flights use the accuracy wording.
- **SITE-CONFLICTS addition:** a Mykonos cost page is live, so "we have not published ranges" was cut from the body and FAQ.
- Copy editor launched.
- **Stage 6 fast (copy editor):** DONE. final.md 2,421 reader words, 0 dashes, 0 placeholders; publish-package.json valid (34 links, 5 FAQs, 7 image slots, 11 open items); chrome-upload-prompt.md draft only, creates a new post after a slug check; article.docx built. The orchestrator replaced "complimentary" in a final-notes line with "banned brand words" and rebuilt the docx.

## Must-fix before publish
1. NEW-URL: the URL was 404. Create a new post (Zoho WC3-T688, WW-281).
2. NIC-SIGNOFF: 8 figures (Santorini in EUR, DFAT fees in AUD), all in original currency. AUD-EXCEPTION: confirm no conversions.
3. SITE-CONFLICTS (for the user and Nic): Santorini capacity; season May vs April; document age 3 vs 6 months; the hub's US-focused legal section naming the advisor; the live Mykonos cost page.
4. UK-GREECE-URL: confirm which URL carries the UK guide.
5. HUB-KEYWORD: the hub owns "greece wedding venues", which clashes with /greece-wedding-venues.
6. LEGACY-301: after publish, 301 /how-to-plan-a-destination-wedding-in-greece-if-youre-overseas here (user approval).
7. FLIGHTS (optional), LINK-CHECK, AUTHOR, IMAGE-RIGHTS, CMS-URL.
