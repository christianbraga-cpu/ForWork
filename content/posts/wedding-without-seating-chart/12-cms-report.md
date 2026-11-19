# Stage 12 CMS report: wedding-without-seating-chart

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser was opened and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/wedding-without-seating-chart/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-without-seating-chart/11-body.md` (08-final.md wording unchanged; front matter and 5 fact markers removed; 4 IMAGE SLOT comments kept; no other HTML comments; inline links and UTMs kept; no [[VERIFY]] markers)
- `content/posts/wedding-without-seating-chart/booking-checklist.md` (open seating planning checklist, questions for the venue and caterer)
- Title: Wedding Without a Seating Chart and How to Make It Work
- Slug: wedding-without-seating-chart. URL: https://weddedwonderland.com/expert-advice/wedding-without-seating-chart
- Type: New (not a refresh, no redirect). Cluster: Wedding Seating Chart
- Categories: Expert Advice (primary), Wedding Seating Chart, Wedding Reception, Planning Guides
- Tags: wedding seating chart, open seating, wedding reception, wedding guest list, destination wedding planning, micro wedding
- Author/byline: Wedded Wonderland
- Meta title: Wedding Without a Seating Chart and How to Make It Work (55 chars, exactly as 02-seo.json)
- Meta description: Thinking of skipping the seating chart? When open seating works, when it backfires, and the simple alternatives that keep guests and your caterer happy. (152 chars, exactly as 02-seo.json)
- Excerpt: When open seating suits your wedding and when it backfires, the middle ground between a full chart and free seating, and how to brief your venue, MC and caterer so every guest is looked after, at home or abroad. (211 chars; no figures, no "most/usually/typically")
- Key takeaways: 4. FAQ: 5 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- Links: taken from the body in 08-final.md, not from 02-seo.json (out of date). Internal: /expert-advice/wedding-seating-chart, /expert-advice/wedding-menu, /what-is-a-micro-wedding, /expert-advice/11-interactive-wedding-ideas-your-guests-will-love, /expert-advice/wedding-day-timeline, /expert-advice/how-to-make-a-wedding-guest-list, /wedding-guest-list-template, /plan-your-destination-wedding (all in the link map). External: Food Standards Australia New Zealand allergen labelling page, Queensland Government accessible events guide (PDF).
- CTAs (from 09-cro.json, already inline in the body): secondary Wedded Concierge link (end of "Give your caterer a plan for dietary meals"), primary Wedded Concierge link (end of "Open seating at a destination wedding across several days"), closing Wedded Concierge link and magazine link (closing paragraph). All utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 4 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA block: in package, not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken

## Images
- Place images by the IMAGE SLOT comments in `11-body.md` (not by the after_h2 numbers in 04-images.json):
  - `featured`: featured image (comment at the top of the body)
  - `cocktail-reception`: under the H2 "When a wedding without a seating chart works"
  - `reserved-family-table`: under the H2 "What to do instead of a seating chart"
  - `destination-welcome-dinner`: under the H2 "Open seating at a destination wedding across several days" (location must be verified)
- All 4 slots are still `needed`. Licensed photos only, with signed consent from the couple, family and identifiable guests. Never AI for real people or places.
- Settle the photo credit wording with Nic (open question in 04-images.json).
- Do not publish with `[[IMAGE NEEDED]]` captions.

## Links to settle
- **/expert-advice/how-to-make-a-wedding-seating-chart:** confirm it is a permanent 301 redirect to /expert-advice/wedding-seating-chart (the body links /expert-advice/wedding-seating-chart). Add one if it is a 302, a rewrite or a live duplicate, and mark it as a redirect in the link map.

## Template
- Show a published or last-updated date on the post in the CMS template if available (a reader asked).

## Before publish
- [[VERIFY]]: none in the body.
- No prices in the post, so nothing for Nic's price sign-off. Nic to approve the Wedded Concierge lines (primary, secondary, closing) and the magazine link.
- Licensed images for all 4 slots.
- Seating chart 301 confirmed as above.
- Set datePublished at publish.

## Mismatches
- None checked on screen: package-only run, and the CMS field map is still not mapped. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-without-seating-chart`.
