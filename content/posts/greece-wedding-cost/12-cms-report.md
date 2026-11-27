# Stage 12 CMS report: greece-wedding-cost

**Draft URL/ID:** not uploaded. Package only, as instructed: the person uploads via the Word doc. No browser was opened and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. Never publish; a human clicks Publish.

## Package
- `content/posts/greece-wedding-cost/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/greece-wedding-cost/11-body.md` (08-final.md wording unchanged; front matter and 33 fact markers removed; H1, the 2 META comments and 5 IMAGE SLOT comments kept; no CTA marker comments added; all 20 links and UTMs exactly as in 08-final.md, internal links relative; no [[VERIFY]] markers)
- `content/posts/greece-wedding-cost/booking-checklist.md` (Greece budget checklist: every cost component with a blank, payment schedule, then questions for the venue, planner, municipality, parish and the Australian side; no figures, no claims)
- H1 and title: Greece Wedding Cost and What It Includes
- Slug: greece-wedding-cost. URL: /destination-weddings/greece-wedding-cost (canonical https://weddedwonderland.com/destination-weddings/greece-wedding-cost)
- Type: New (not a refresh, no redirect). Cluster: Destination Wedding Costs
- Categories: Destination Weddings (primary), Greece, Wedding Budget, Planning Guides
- Tags: greece wedding cost, greece weddings, destination wedding budget, wedding packages, santorini wedding, mykonos wedding, crete wedding
- Author/byline: Wedded Wonderland
- Meta title: Greece Wedding Cost and What It Includes (same as the title)
- Meta description: Greece wedding cost explained for Australian couples. What shapes the total, what venue packages include, what sits outside them and what to ask. (exactly as 02-seo.json)
- Focus keyword: greece wedding cost. OG image: featured slot.
- Excerpt: What shapes the cost of a wedding in Greece for Australian couples, from island, venue, season and guest travel to what venue packages include, what sits outside them, paying in euro from Australia and the questions to ask before you request a quote. (250 chars, no figures)
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Destination Weddings > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body, once each): primary Wedded Concierge (end of "Written quotes"), secondary Wedded Concierge (end of "Questions for the planner"), closing Wedded Concierge and the magazine link (final paragraph). All utm_medium=content.
- Prices or figures: none, so nothing needs Nic's price sign-off.

## Checklist (publish-checklist.md)
- [x] `11-publish-package.json` validates; primary_category equals categories[0]
- [ ] field-map.md CONFIRMED: no (NOT YET MAPPED); not needed for a package-only run
- [ ] Images uploaded with alt and caption: not done, all 5 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA blocks: in package (already inline in the body), not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly to Destination Weddings: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done (person uploads)
- [ ] Preview screenshots (desktop, mobile): none taken

## Images
- Place images by the IMAGE SLOT comments in `11-body.md`:
  - `featured`: featured image (comment under the H1)
  - `guest-travel`: under the H2 "What shapes the cost of a wedding in Greece"
  - `welcome-dinner`: under the H2 "What packages include and what sits outside them"
  - `quotes-still-life`: under the H2 "Paying for a wedding in Greece from Australia"
  - `planning-flat-lay`: under the H2 "How to plan the spend for a Greece wedding"
- All 5 slots are `needed`. Licensed photos only; never AI for a real place. The two still lifes (quotes-still-life, planning-flat-lay; no people, no real place) may use AI only with approval, captioned "Illustrative image".
- Do not publish with `[[IMAGE NEEDED]]` captions or `[[VERIFY credit]]` credits.

## Before publish
- **Check the saved URL is exactly /destination-weddings/greece-wedding-cost** (category path and slug), not a CMS default path or a slug with a suffix.
- **Legal content is general information as at November 2026**, not legal advice: the Rhodes civil route, Embassy Athens, DFAT, Archdiocese, ACCC and Smartraveller lines. Recheck if the post is published much later.
- **[[VERIFY]]: none in the body.** The two items moved at the edit stage (the civil document list, notice period and ceremony days with the municipality where the couple marries; documents, dates and fees for a Greek Orthodox wedding with the parish in Greece) are questions in `booking-checklist.md`, not claims in the post.
- Nic to approve the Wedded Concierge lines (primary, secondary, closing) and the magazine link. No price sign-off needed.
- Licensed images for all 5 slots.
- Confirm the legal anchor link `/destination-weddings/greece-wedding-venues#getting-legally-married-in-greece-as-australians-in-brief` still lands on that section.
- The body starts with the H1 and two META comments. If the CMS renders the title field as the H1, delete the body H1 line so the page has one H1; the META comments are reference only (the values go in the SEO fields).
- Set datePublished at publish.

## After publish
- **The live Greece packages page ranks for cost terms** (`/destination-weddings/greece-wedding-packages`, position 2 for "greece wedding cost" in Sydney per 02-seo.json). After publishing, add a link from it to this page, and **keep "cost" out of its meta** so this page owns "cost". Watch both URLs in GSC.

## Search expectation
- **Searchers expect a figure and this page deliberately gives none** (the person's choice). Every SERP checked leads with figures. The page competes on what shapes the cost and what to ask; expect lower click through from figure seekers.

## Mismatches
- None checked on screen: package-only run, and the CMS field map is still not mapped. To upload through the browser later, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=greece-wedding-cost`.
