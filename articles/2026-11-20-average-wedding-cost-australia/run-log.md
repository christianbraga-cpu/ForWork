# Run log: Average Wedding Cost in Australia (merge)

## Inputs (from the user, 20 Nov 2026)
- Given title: "This is how much an average wedding costs in Australia"
- Primary keyword: average wedding cost australia
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- Primary CMS category: Expert Advice. Cluster: average wedding cost.
- Kept URL (update): https://weddedwonderland.com/this-is-how-much-an-average-wedding-costs-in-australia
- Merged in:
  - https://weddedwonderland.com/the-average-cost-of-an-australian-wedding-in-2020
  - https://weddedwonderland.com/the-cost-of-a-wedding-in-australia-2019
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **User decision (20 Nov 2026):** no headline figure.
  - No average dollar figure appears, including our 2017 survey and any competitor survey.
  - The piece explains why averages mislead.
  - It states, with sources, that no current government average exists.
  - It compares costs by category.
- **Decision (default, change if you want):** H1 and SEO title "Average Wedding Cost in Australia and What Drives It" (52 characters; keyword first; no colon or dash). The given title does not lead with the keyword.
- **Decision (default):** merge method.
  - Grade every claim on the three old pages.
  - Keep only what official sources or our live guides support. Drop all old dollar averages.
  - MERGE-301: 301 the 2020 and 2019 URLs to the kept URL at publish, with user approval.
  - The kept URL stays as is.
- **Decision (default):** official sources inline: ABS, Moneysmart, ACCC. Our own cost guides for the destination comparison. Competitor surveys blocked.
- **Decision (default):**
  - Link the cluster hub /expert-advice/how-much-does-the-average-wedding-cost with a non-exact anchor and flag the overlap.
  - Link the vs-home page.
  - Do not link /expert-advice/wedding-cost-per-guest (SITE-CONFLICTS) or the 19 Nov destination cost DRAFT (retro-link later).

## Stages
- **Stage 0 fast (strategist):** DONE.
  - **Volumes (AU, per month):** average wedding cost australia 1,300; average cost of a wedding in australia 1,300; how much does a wedding cost australia 390; average wedding cost 480.
  - **SERP:** the AI Overview and top results rest on the $38,252 industry survey (Easy Weddings, blocked), unsourced vendor numbers and second-hand Moneysmart claims. None links ABS. Our 2020 page ranks #2 in Sydney and Brisbane.
  - **URLs:** all three are live.
  - **Cannibalisation:** partial with the hub /expert-advice/how-much-does-the-average-wedding-cost, which is US-led. **Decision (default):** do not merge the hub; suggest the user cut its Australia paragraph to a pointer here (HUB-POINTER).
  - **Brief:** 7 H2s and 5 FAQs.
- **Flag for the user:** a live page, /expert-advice/average-destination-wedding-cost-by-region, matches the topic of the 19 Nov draft. Was that draft published at this URL? Added to link-map.
