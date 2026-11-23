# Run log: Bridal Shower Guest List Etiquette and Who to Invite

## Inputs (from the user, 23 Nov 2026)
- Title: Bridal Shower Guest List Etiquette and Who to Invite (52 characters; keyword first; not a question; no colon or dash)
- Primary keyword: bridal shower guest list
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/expert-advice/bridal-shower-guest-list (type given as "new")
- Slug: bridal-shower-guest-list
- Primary CMS category: Expert Advice. Cluster: wedding guest list template.
- Brief (user): KD 2. Sits next to /should-men-be-invited-to-the-bridal-shower, which already ranks top 5 for a large query set, so it inherits internal links fast.
- Rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default):** H1 and SEO title are both "Bridal Shower Guest List Etiquette and Who to Invite" (52 characters; passes the title rule and the 50 to 60 meta range).
- **Decision (default):** the URL status is checked first. If it is live, refresh in place; if not, create a new post after a CMS slug check.
- **Decision (default):** etiquette is advice, not fact.
  - Conventions are framed as conventions, in our voice: "a long-standing convention is...".
  - Anything stated as a rule must come from our own live pages, quoted as worded, or be framed as advice. No competitor etiquette sources.
  - Official sources only if a factual claim needs one (unlikely).
- **Decision (default):** destination edge. Covers:
  - who to invite when the wedding is abroad and the guest list is small
  - inviting people who cannot travel
  - a shower at home vs a shower near the wedding
  - virtual guests
- **Decision (default):** links.
  - /should-men-be-invited-to-the-bridal-shower as a close sibling, with a non-exact anchor.
  - The guest list template cluster pages found by the strategist.
  - Wonderland Studio guest list tools, if in link-map.
  - Etiquette and destination guest pages.
  - No Wedded World plug, no DRAFT links.
  - A link back from the sibling page is logged as RETRO-LINK.

## Stages
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho task WC3-T983 (To-Do, TK-068, due 24 Nov).
  - **Volumes (AU / US per month):** bridal shower guest list 10 / 140; who to invite to bridal shower 30 / 1,600; bridal shower etiquette 20 / 720.
  - **SERP:** weak (forums, Facebook, Pinterest, a 2012 column, an AU directory). Nobody covers the destination wedding, guests who cannot travel, virtual guests, a printable checklist or kitchen tea terms.
  - **Cannibalisation:** partial only with the men, bridal shower planning, destination bridal shower and who-hosts pages (short sections with links).
  - **Cluster:** head /wedding-guest-list-template. Primary CTA studio_free plus a soft Discovery Call.
  - **Link map:** new "Bridal shower and guest list" section added.
- **Decision for the user (SIBLING-SOFTEN):** the men sibling's FAQ calls "shower guests must be wedding guests" "the one firm rule"; this piece calls it a convention. Soften the sibling after publish?
- **LINK-CHECK:** /wedding-tools/online-wedding-shower-invitations (Zoho says published; not in the site map).
- **Stage 1 fast (research):** DONE. 36 facts, all from our live pages and the brand profile; no legal facts, no prices. Third-party sources our pages mention (Vogue, The Knot, a US planner) are flagged so they are not cited.
  - **Wonderland Studio:** free, with a guest list, RSVPs (plus-ones, dietary) and guest grouping.
  - **Conflicts:** "one firm rule" vs a softer line for small faraway weddings; our pages disagree on shower timing (TIMING-CONFLICT; no timing rule stated).
- **Stage 2:** writer launched.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md. --check: 2,143 reader words (over), 0 dashes, 1 visible placeholder (move to open_items), no external domains. YAML valid: 29 claims, 33 link instances to 17 URLs (too many). No guest numbers or timing rules stated. Reviews launched.
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.8:** majors on plus-ones stated as fact, an implied Studio shower-list feature, and three URLs (all are in link-map; hens switched to the AU page).
  - **SEO 4.0:** majors on length (2,143 words), 33 link instances, meta 138 characters.
  - **Reader (couple):** relevance 3, trust 3, clarity 4, would_enquire 2, "forward". The visible placeholder; the deflected answer on people not invited abroad; the bolted-on Concierge line. The planner-vetting blocker is downgraded as out of scope.
  - Merged request: 04-reviews/v1/merged.md. Duplicate link-map row removed.
- **Decision (default):** people at home not invited abroad get concrete options framed as our suggestions (a relaxed gathering after you are home, no gifts expected) plus "talk it through with your host". "Sources current as at" is dropped (no official sources on etiquette).
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md: 1,914 reader words, 0 dashes, 0 placeholders. YAML valid: 32 claims (24 sourced, 8 advice), 16 links across 15 URLs. All 19 items applied. Options for people at home not invited abroad added as advice; plus-ones as advice; Studio wording matches live copy.
- **Stage 6 fast (copy editor):** DONE. final.md 1,914 reader words, 0 dashes, 0 placeholders; publish-package.json valid (17 links incl. CTA); chrome-upload-prompt.md is draft only and creates a new post after a slug check; article.docx built.

## Must-fix before publish
1. NEW-URL: the URL was 404. Create a new post (Zoho WC3-T983, TK-068, due 24 Nov).
2. RETRO-LINK: add a link from /should-men-be-invited-to-the-bridal-shower to this page.
3. Decisions for the user:
   - SIBLING-SOFTEN: the sibling calls "shower guests are wedding guests" "the one firm rule".
   - SIBLING-FAQ: consider removing that question from the sibling's FAQ schema.
4. DESIGN-PDF: printable checklist.
5. TIMING-CONFLICT: our pages disagree on shower timing.
6. LINK-CHECK (incl. /wedding-tools/online-wedding-shower-invitations, not linked), AUTHOR, IMAGE-RIGHTS, CMS-URL.
No prices, so nothing for Nic.
