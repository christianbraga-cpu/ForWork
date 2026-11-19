# Run log: Average Destination Wedding Cost by Region

## Inputs (from the user, 19 Nov 2026)
- Title (H1): Average Destination Wedding Cost by Region (42 characters; not a question; no colon or dash)
- Primary keyword: average cost of destination wedding. Secondary: cost destination wedding (720), how much does destination wedding cost (480).
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/expert-advice/average-cost-of-destination-wedding
- Slug: average-cost-of-destination-wedding
- Primary CMS category: Expert Advice
- Type: New. Cluster: average wedding cost (new cluster).
- Brief (user): WW's edge is comparing destination costs against home averages. Must not target "destination wedding" itself. Links to /packages and planned WW-322, WW-335, N-107.
- User rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, change if you want):** the H1 is kept as given. It leads with a close variant of the keyword ("Average Destination Wedding Cost"), not the exact phrase. SEO title: "Average Cost of a Destination Wedding by Region" (47 characters, keyword first, no colon or dash).
- **Decision (default):** every figure carries its source, date and original currency, with no conversions. Home averages come only from authoritative sources (government, ASIC Moneysmart, or an independent national survey); competitor surveys are blocked. If no authoritative home average exists, the article says so and compares cost categories instead of totals.
- **Decision (default):** destination figures come only from our own cost guides, quoted as worded and linked at the claim, and are flagged for Nic. SITE-CONFLICTS carries over: the Bali cost guide's USD range conflicts with the Bali hub's AUD range.
- **Decision (default):** WW-322, WW-335 and N-107 are planned and not live. They are not linked; they are recorded as RETRO-LINKS.

## Stages
- **Stage 0 fast (strategist):** DONE. Australian volumes per month: primary 10; "cost destination wedding" 20 (the user gave 720); "how much does destination wedding cost" 10 (the user gave 480); "destination wedding cost" 20; "average wedding cost australia" 1,300.
  - The SERP top results are forums and blocked marketplaces, all at budget tier. None compares costs by region for Australians or covers the luxury band.
  - The brief has 7 H2s and 5 FAQs.
- **Cannibalisation:** the live page /destination-weddings/destination-wedding-vs-home-cost already covers the destination vs home comparison, leading with US figures.
- **Decision (default, change if you want):** keep this article, since the user requested it. It is the regional average piece. The comparison with home is one short section that links to the vs-home page. Updating that page with Australian figures is offered to the user as a follow-up.
- **Other findings:**
  - /expert-advice/how-much-does-the-average-wedding-cost may already head the "average wedding cost" cluster. Linked as the hub.
  - /expert-advice/wedding-cost-per-guest quotes A$38,252, likely from Easy Weddings, a blocked source. Added to SITE-CONFLICTS for the user; this article will not quote it.
- **Stage 1 fast (research):** PARTIAL. The research agent was held on an MCP permission prompt; 10 facts were saved by 22:56 (our Italy, Lake Como and Bali guides). No home average yet.
- **Decision (default):** the writer started at 23:12 on the saved facts. Late facts, such as a home average or the Zoho titles, go into v2. Neither Bali range is quoted (F-08 USD vs F-09 AUD, SITE-CONFLICTS).
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 2,228 reader words, 0 dashes, 0 placeholders, 0 external domains.
  - YAML valid: 16 claims, 19 links (all internal).
  - Figures: EUR only, from the Italy and Lake Como guides. No Bali range. No home average ([[NEEDS]] in front matter).
  - Link map: new "Average wedding cost cluster" section added, covering the hub, the vs-home page, the cost-per-guest conflict and planned retro-links.
