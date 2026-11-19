# Stage 12 CMS report: short-wedding-vows

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser was opened and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/short-wedding-vows/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/short-wedding-vows/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; 4 IMAGE SLOT comments kept; inline links and UTMs kept; no [[VERIFY]] markers)
- `content/posts/short-wedding-vows/booking-checklist.md` (vow-writing checklist, celebrant or registrar questions, venue questions)
- Title: Short Wedding Vows Examples Under One Minute
- Slug: short-wedding-vows. URL: https://weddedwonderland.com/expert-advice/short-wedding-vows
- Type: New (not a refresh, no redirect). Cluster: Wedding Vows
- Categories: Expert Advice (primary), Wedding Vows, Ceremony, Planning Guides
- Author/byline: Wedded Wonderland
- Meta title: Short Wedding Vows Examples You Can Say in Under a Minute (57 chars, from 02-seo.json)
- Meta description: Short wedding vows by style, from romantic to funny, with a one-minute template, the legal words you say in Australia and tips for saying them aloud. (149 chars; 02-seo.json's "the legal words Australia requires" changed to match the body, which says the s45(2) words are sufficient "or words to that effect")
- Key takeaways: 4. FAQ: 5 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body): secondary Wedded Concierge link (destination examples intro), primary Wedded Concierge link (end of the "Marrying overseas" note), closing Wedded Concierge link and magazine link (closing paragraph). All utm_medium=content.

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
- Place images by the IMAGE SLOT comments in `11-body.md`, not the numbered `after_h2` placements in `04-images.json` (the legal section moved below the examples, so those numbers are out of date):
  - `featured`: featured image (comment at the top of the body)
  - `vow-cards`: under the H2 "How long should short wedding vows be?"
  - `destination-ceremony`: under the H2 "What are some good short wedding vows?"
  - `renewal`: under the H3 "Renewal"
- All 4 slots are still `needed`. Licensed photos only; never AI for real people or places. The vow-cards still life (no people, no real place) may use AI only if Nic approves, captioned "Illustrative image".
- Do not publish with `[[IMAGE NEEDED]]` captions.

## Publish order: sister drafts
Four internal links go to sister drafts that are not yet live:
- /expert-advice/who-can-perform-a-marriage
- /expert-advice/notice-of-intended-marriage
- /destination-weddings/get-married-in-new-zealand
- /expert-advice/wedding-processional-songs

Publish those first or with this post, or remove the links before publishing.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so nothing for Nic's price sign-off. Nic to approve the Wedded Concierge lines (primary, secondary, closing) and the magazine link.
- Licensed images for all 4 slots.
- Sister drafts live, or their links removed.
- Set datePublished at publish.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=short-wedding-vows`.
