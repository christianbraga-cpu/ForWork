# Run log: Getting Married in Greece from the UK (refresh)

## Inputs (from the user, 20 Nov 2026)
- Given title: "How Do UK Couples Get Married in Greece?" (a question)
- Primary keyword: getting married in greece from uk
- Audience line given: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- Article to refresh: https://weddedwonderland.com/if-youre-thinking-of-getting-married-in-greece-you-need-to-know-this
- Intended URL: https://weddedwonderland.com/destination-weddings/getting-married-in-greece-from-uk
- Slug: getting-married-in-greece-from-uk
- Primary CMS category: Destination Weddings
- Type: legal. Cluster: Getting Married in Greece.
- User rule: keep this one UK-specific and link to it.
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Mode: FAST

## Decisions
- **Decision (default, change if you want):** the given title is a question, which breaks the standing title rule. H1 and SEO title: "Getting Married in Greece from the UK Step by Step" (50 characters; keyword first with "the" for grammar). The original question becomes an FAQ.
- **Decision (default):** UK-specific throughout. Readers are British couples in their 30s with British passports, planning a luxury wedding. Figures in GBP or EUR as sourced, with no conversions and no AUD. No Australian steps. A new persona, blog-team/personas/uk-couple.md, is drafted for CRM calibration. Panel: primary uk_couple, secondary paying_parent, anti bargain_hunter.
- **Decision (default):** refresh method.
  - Read the old article.
  - Keep only what official sources still support.
  - Rewrite to the country-legal-guide template, with H2 3 as "Prefer to marry in the UK?".
  - The 301 from the old URL to the new URL is an open item (REDIRECT-301).
- **Decision (default):** official sources only, linked at the claim.
  - UK: gov.uk, FCDO, British Embassy Athens, GRO, NRS, GRO NI, FCDO legalisation.
  - Greece: gov.gr, municipalities, Greek Embassy London.
  - The Greek-side facts are reused from the 12 Nov Greece licence pack, keeping their original dates.
- **Decision (default):** "link to it". A link-map row marks this page as the UK route in the Greece cluster. One sentence is added to the Greece licence article (DRAFT) sending UK readers here, and its docx is rebuilt.

## Stages
- **Stage 0 fast (strategist):** DONE.
  - **UK volumes per month:** keyword 70 (high competition); "getting married in greece" 260; "uk citizens getting married abroad" 50.
  - **SERP:** no top-3 page in London or Manchester is written for British couples (local planners, a US-citizen guide, Viator). Edinburgh's leader is a 2017 budget page. The gap is a current, sourced UK step by step that includes recognition at home.
  - **Old URL:** live (200), titled "If You're Thinking of Getting Married in Greece You Need to Know This". It dates from 2020, is written for Australians, and its same-sex claim is outdated. 301 to the new URL after publish.
  - **Cannibalisation:** none apart from the old page.
  - **Brief:** 9 H2s and 5 FAQs.
- **Flag for the user:** the site map lists /destination-weddings/greece-marriage-licence with a live-looking title, although link-map says DRAFT. **Decision (default):** link it conditionally, and the user confirms whether it is published (GREECE-LICENCE-LIVE).
- **Decision (default):** H2 1 loses its colon (house style). It becomes "Can British couples marry legally in Greece".
- **Stage 1 fast (research):** DONE. 32 facts: 19 Greek-side reused from the 12 Nov pack, 13 new UK facts. 7 legal; 6 prices for Nic.
  - **Old article:** outdated. 6 of 20 claims still hold. Errors corrected in the rewrite:
    - same-sex marriage (legal in Greece since 2024)
    - civil ceremony by the mayor or town hall, not a celebrant
    - the translation office replaced in 2021
    - the newspaper notice and 40-day registration fine are unsourced
    - fees are unsourced
  - **UK steps confirmed on gov.uk:**
    - online CNI or equivalent, £50
    - paper apostille £45, up to 25 working days
    - a marriage abroad is recognised but not registered in the UK
    - passport name change £102 online
    - Greece entry passport rules
  - **Gaps:** the Greece-specific document details are visible only inside the gov.uk application; Santorini and Mykonos town halls; Scotland and NI records pages; church conditions; the apostille on the Greek certificate.
- **Stage 2:** writer launched.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 3,209 reader words (over the brief; v2 trims), 0 dashes, 3 visible [[NEEDS]] markers for UK nation pages (to resolve in v2).
  - 8 official domains inline (gov.uk, mfa.gr, ypes.gr, mitos.gov.gr, municipality sites); none blocked.
  - YAML valid; 49 claims (45 sourced), 24 links.
  - Link map: Santorini cost breakdown row and this page's DRAFT row (the UK route) added.
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.4:** blocker on FAQ 5's unsourced UK-nation issuers and its visible [[NEEDS]]. Majors: two more [[NEEDS]]; the licence rule's wording; the visa-free qualifier; the unsourced Greek apostille step; the hand-decoded 2019 circular (CIRCULAR-READ).
  - **SEO 4.0:** title rule passes. Majors: meta 161 characters; 3,209 words, with a cut plan to about 2,300.
  - **Reader (uk_couple):** relevance 5, trust 4, clarity 3, would_enquire 3, "save and forward". Majors: the placeholders; nothing on Santorini or Mykonos; the venue question left open.
  - Merged request: 04-reviews/v1/merged.md.
- **Link map:** six Greece pages from the strategist's map added to the Greece section: best time, packages, same-sex, venues, the CNI explainer, and an older Greece planning page marked do-not-link.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md: 2,376 reader words, 0 dashes, 0 placeholders, 7 official domains inline, none blocked. YAML valid: 42 claims, 30 links. All 28 merged items applied. No [[NEEDS]] in the body. Santorini and Mykonos are covered honestly (no published requirements found), and the venue question goes into the municipality question list.
- **Stage 6 fast (copy editor):** DONE. final.md 2,376 reader words, 0 dashes, 0 placeholders, 7 official domains inline; publish-package.json valid; chrome-upload-prompt.md is draft only and never touches the old URL; article.docx built. Template lessons added to country-legal-guide.md. The Greece licence article's retro-link sentence is in, and its docx rebuilt.

## Must-fix before publish
1. CIRCULAR-READ: a Greek reader confirms the 2019 Interior Ministry circular (a free-to-marry document naming the partner counts as the licence). This is the article's central legal point.
2. REDIRECT-301: after publish, 301 /if-youre-thinking-of-getting-married-in-greece-you-need-to-know-this to the new URL (user approval).
3. GREECE-LICENCE-LIVE: confirm whether /destination-weddings/greece-marriage-licence is published (link-map says DRAFT; the site map shows it). It now links here, so publish the UK guide first or together.
4. NIC-SIGNOFF: GBP 50, 45, 102, 115.50; EUR 10, 10, 100, 150 (official fees).
5. LINK-CHECK (gov.uk and Greek hosts not reachable in the session), CONCIERGE-PAY, AUTHOR, IMAGE-RIGHTS, CMS-URL.
