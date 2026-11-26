# Run log: AI Wedding Vows and How to Make Them Sound Like You

## Inputs (from the user, 26 Nov 2026)
- Title: AI Wedding Vows and How to Make Them Sound Like You (51 characters; keyword first; not a question; no colon or dash)
- Primary keyword: AI wedding vows
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/wedding-tools/ai-wedding-vows (type "new")
- Slug: ai-wedding-vows
- Primary CMS category: Wedding Tools. Cluster: AI wedding planner.
- Brief (user): an AI use case people search for; links to the vows cluster and to Studio AI chat. Small.
- Rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default):**
  - H1 as given; SEO title the same, or the strategist's version within 50 to 60 characters.
  - Small: 1,200 to 1,600 words, 4 FAQs.
- **Decision (default):** the angle is AI as a drafting partner, not a ghostwriter. It covers:
  - a prompt framework built from your own stories
  - editing out generic phrasing
  - a read-aloud length check (our how-to-write page wording)
  - a before and after example written by us
  - privacy advice
- **Decision (default):** Studio AI chat is linked only as its live pages describe it; if there is no live page, link /wonderland-studio and log STUDIO-AI-URL.
- **Decision (default):** official sources at the claim.
  - The Attorney-General's Department on the Marriage Act words required in a legal Australian ceremony.
  - Abroad, the local registrar or embassy decides.
  - Privacy is advice only unless OAIC speaks to individuals.
  - No third-party AI tool rankings.
- **Decision (default):** no DRAFT links (the funny and bible vows pages are DRAFT); no Wedded World plug.

## Stages
- Stage 0 and 1 launched in parallel (both save early).
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho WC3-T1003 (In Progress).
  - **Studio AI:** /wonderland-studio/ai-chat is live but login-gated. Live wording: "Ask your AI Planning Assistant. Timing, budgets, destinations, etiquette. Ask anything, any hour." Our comparison page says Studio is "not a writing studio" for vows. **Decision (default):** link /wonderland-studio in the body and the ai-chat page only as a secondary "try it" link. Do not claim it writes vows.
  - **STUDIO-AI-PRICE conflict:** "free with a message allowance" vs "7-day trial, then paid". No price is stated.
  - **Volumes (AU / US):** ai wedding vows 20 / 140; chatgpt wedding vows 40 / 260.
  - **SERP:** expects named tools. **Decision (default):** name tools only as examples (no ranking), with facts only from their own pages.
- **Orchestrator Firecrawl check (26 Nov):** the funny vows URL redirects to /planning/how-to-write-wedding-vows, and the bible verses URL redirects to /expert-advice/traditional-wedding-vows; link-map rows updated.
  - The how-to-write page now says "about 150 words, a minute out loud" and "300 words is the most we would suggest" (quote this, not 250 to 300).
  - That page cites s45(2) of the Marriage Act on legislation.gov.au and the AG's Department.
  - **Web team:** the page's Concierge box uses "complimentary".
  - **VOWS-URL (for the user):** /how-to-write-wedding-vows vs /planning/how-to-write-wedding-vows. The /planning/ URL is canonical and used here.
- **03:03 check-in:** the researcher is held on an MCP permission prompt; 22 facts saved: the Marriage Act s45 and s46 (legislation.gov.au), the AG's Department get-married page, our how-to-write page, and the Studio and ChatGPT-vs pages. No OAIC fact and no third-party tool facts yet. **Decision (10-minute rule):** the writer started on the saved facts with an inline brief. Privacy is advice only; no third-party AI tools are named unless facts land.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 1,653 reader words (slightly over); 0 dashes; 0 placeholders. Official domains: legislation.gov.au, ag.gov.au.
  - YAML valid: 24 claims, 14 links.
  - No AI tools named. The vows parent is /planning/how-to-write-wedding-vows.
  - The Concierge line uses brand-profile wording (CONCIERGE-CEREMONY). Studio is called "our free planning hub" (STUDIO-AI-PRICE pending).
- Reviews launched (accuracy, SEO, couple reader).
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 4:** majors on the s45(2) wording (it applies to civil celebrants only) and the "no credit card" and "free" price terms (STUDIO-AI-PRICE). Judged on the pack, because live fetches failed.
  - **SEO 4.0:** majors on too many related links, and "chatgpt wedding vows" and "ai vow generator" are missing.
  - **Reader (couple):** relevance 2, trust 3, clarity 4, would_enquire 2, "save". Adds an Italy legal link and a plainer Concierge line.
  - Merged request: 04-reviews/v1/merged.md.
- **Decision (default, AI-TOOL-NAMES):** ChatGPT is named only through our own comparison page's wording (S-06), with no ranking. "Free" stays for Studio (the primary live page), with Nic's sign-off.
- Stage 4: writer v2 launched. The researcher is still held on a permission prompt.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md.
  - --check: 1,524 reader words; 0 dashes; 0 placeholders. Official: legislation.gov.au, ag.gov.au.
  - YAML valid: 24 claims, 12 links.
  - All 13 items applied. The Concierge line uses brand-profile wording. The login-gated ai-chat link was dropped. OAIC is not linked (advice only).
- Stage 6: copy editor launched.
- **Stage 6 fast (copy editor):** DONE. final.md 1,524 reader words, 0 dashes, 0 placeholders; YAML 24 claims, 12 links.
  - publish-package.json valid (13 open items). chrome-upload-prompt.md is draft only and creates a new post after a slug check. article.docx built.
- The researcher was still held on a permission prompt at the end; the article did not need its remaining work.

## Must-fix before publish
1. NEW-URL: the URL was 404. Create a new post (Zoho WC3-T1003).
2. NIC-SIGNOFF (STUDIO-AI-PRICE): "free" for Studio (the primary live page says free; another page says a 7-day trial, then paid). Fallback: "our planning hub" and "Start planning".
3. VOWS-URL (for the user): /how-to-write-wedding-vows vs /planning/how-to-write-wedding-vows. The /planning/ URL is canonical and linked.
4. LINK-CHECK: live checks failed in review. Re-check legislation.gov.au, ag.gov.au and our quoted vows and Studio pages on publish day.
5. WEB-TEAM: the how-to-write page's Concierge box uses a banned brand word.
6. STUDIO-AI-LOGIN (ai-chat is login-gated, not linked), CATEGORY-CHECK (Wedding Tools), CONCIERGE-PAY, AUTHOR, IMAGE-RIGHTS, CMS-URL.
- **Stage 1 fast (research):** DONE after delivery. 29 facts (12 legal).
  - The AGD Guidelines v6.0 para 4.24 say the s45(2) words "are the minimum words", which fits the article.
  - OAIC AI guidance covers organisations only, so privacy stays advice only.
  - The for-her, for-him and elopement vows URLs redirect to the parent.
- **Post-delivery link fix (orchestrator):**
  - /expert-advice/short-wedding-vows redirects to the parent, so that sentence and link (L-03) were removed.
  - /expert-advice/wedding-ceremony-script-australia redirects, so it was repointed to /expert-advice/wedding-ceremony-script.
  - Link-map rows marked REDIRECT, and a ceremony-script row added.
  - final.md is now 1,513 reader words, 11 links, 0 dashes; docx rebuilt and re-sent.
