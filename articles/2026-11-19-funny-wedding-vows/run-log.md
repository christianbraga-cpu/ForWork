# Run log: Funny Wedding Vows That Still Mean Something

## Inputs (from the user, 19 Nov 2026)
- Title: Funny Wedding Vows That Still Mean Something (44 characters; keyword first; no colon or dash)
- Primary keyword: funny wedding vows
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/expert-advice/funny-wedding-vows
- Slug: funny-wedding-vows
- Primary CMS category: Expert Advice (confirmed)
- Type: New. Cluster: wedding vows.
- Personas: primary `couple`, secondary `paying_parent` (advisory), anti `bargain_hunter`
- Mode: FAST; strategist and one research batch in parallel

## New user rules (19 Nov 2026; added to SKILL.md, writer, seo-reviewer, copy-editor)
1. Title (H1 and SEO title): not a question, keyword first, 60 characters max, no colons or dashes.
2. Link official sources at the claim (blog SOP section 4).
3. Follow the internal linking plan (link-map.md): most relevant pages on our site where the topic comes up.

## Decisions
- **Decision (default, change if you want):** no blog SOP file is in the repo; rule 2 is read as "inline link at the claim". Share the SOP if section 4 says more.
- **Decision (default):** a writing guide to funny but sincere vows with an Australian legal anchor: the Marriage Act 1961 s 45 words and the celebrant's monitum must still be said at a legal Australian ceremony; personal vows sit alongside. Symbolic overseas ceremonies allow any words.
- **Decision (default):** example lines are our own original illustrations; no vows attributed to real couples; no humour at a partner's expense (tone guidance).
- **Decision (default):** /expert-advice/traditional-wedding-vows owns "traditional wedding vows": linked with a descriptive anchor only.

## Stages
- **Stage 0 fast (strategist):** DONE. AU volumes: funny wedding vows 70/month, personal wedding vows 70. Page one is Pinterest, Facebook, Reddit and joke lists; none mentions the Marriage Act s 45 words or the monitum. Brief: writing guide (not a joke list), about 1,900 words, 5 FAQs, H1 and SEO title "Funny Wedding Vows That Still Mean Something" (44), Expert Advice only, discovery_call CTA, about 16 internal links plus official links at the claim.
- **Decision (default, change if you want):** five live vow and ceremony pages added to link-map (traditional vows, vows for her, vows for him, humorous ceremony script, simple ceremony script); they partly overlap but none targets "funny wedding vows", so the new page stands.
- **Stage 1 fast (research):** BLOCKED on a user permission prompt since about 00:40; nothing saved by 00:49. **Decision (default):** writer builds 02-research.json from facts already verified in earlier packs (s 45(2) vows and s 46(1) monitum from the 13 Nov licence and witnesses packs; commitment ceremonies; overseas celebrant rule and NOIM timing from the 18 Nov Bali religion pack), then drafts. If the research agent finishes, its facts feed the revision.
- **Stage 2 fast (writer):** DONE. 02-research.json (6 reused verified facts) and 03-draft-v1.md. --check: 2,057 reader words, 0 dashes, 0 placeholders, 2 official domains (legislation.gov.au, ag.gov.au) linked inline at the claim, none blocked. YAML valid; 11 claims, 16 links. H1 and SEO title "Funny Wedding Vows That Still Mean Something". Open: re-check the Marriage Act wording against a compilation later than 9 July 2024 (N-001); vow-renewal pages not in link-map.
- **Stage 3 fast (3 reviews):** DONE. Accuracy 3.5 (blocker: unsourced "personal vows can come before or after the legal words"; majors: no confirm-with-the-destination-authority line, NOIM timing not linked at the claim, vow-renewal FAQ misstates the Guidelines). SEO 4.0 (title rule pass; majors: keyword in no H2, NOIM link). Reader (couple) relevance 3, trust 3, clarity 4, would_enquire 2: would save and forward; two back-to-back Concierge paragraphs felt bolted on. Merged request: 04-reviews/v1/merged.md.
- **Decision (default, change if you want):** SEO title stays the user's 44-character title (rubric prefers 50 to 60; user rule is 60 max). Vow-renewal pages added to link-map and linked in the FAQ. CMS-TITLE open item: the SEO plugin must not add " - Wedded Wonderland" (dash) to the title tag.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md. --check: 1,992 reader words, 0 dashes, 0 placeholders, 2 official domains inline, none blocked. YAML valid; 11 claims, 16 links. Keyword now in H2 "How to write funny wedding vows in four parts"; NOIM timing linked at the claim; Concierge paragraphs merged; vow-renewal guide linked ("guide to writing vows for a renewal").
- **Stage 6 fast (copy editor):** DONE. final.md 1,992 reader words, 0 dashes, 0 placeholders, official sources inline; publish-package.json valid (10 open items); chrome-upload-prompt.md (draft only; title-tag dash check); article.docx built. The copy editor ran one extra ls before its two commands (no harm). The research agent never got past its permission prompt; the article uses facts verified on 13 and 16 Nov.

- **Late research (research agent finished after its permission prompt cleared):** 15 facts in 02-research-late.json (kept separate; it had overwritten the pack the draft cites, which was restored). Marriage Act ss 45(1), 45(2), 46(1) re-read in compilation C2026C00129 (28 Mar 2026): wording matches. Our /how-to-write-wedding-vows guide says 250 to 300 words, about two minutes, which conflicted with the draft's "one minute, 120 to 180 words".
- **v3 fix pass (copy editor):** DONE. Act links swapped to the latest compilation (N-001 closed); vow length now quotes our guide; /how-to-write-wedding-vows linked in the structure H2 (one added sentence); C-01 fact_ref fixed; chrome-upload-prompt.md matched. --check 2,010 words, 0 dashes; JSON and YAML valid; 17 links.

## Must-fix before publish
1. (Closed) N-001.
2. N-002: confirm the vow-renewal FAQ against the 2021 celebrant Guidelines and swap the PDF link.
3. CMS-TITLE: the SEO plugin must not add " - Wedded Wonderland" to the title tag (no-dash rule).
4. LINK-CHECK, CONCIERGE-PAY, RETRO-LINKS (from traditional vows, humorous script, vows for her and him), IMAGE-RIGHTS, AUTHOR, CMS-URL.
No publish-order dependency.
