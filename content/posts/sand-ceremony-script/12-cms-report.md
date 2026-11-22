# Stage 12 CMS report: sand-ceremony-script

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser was opened, no login was attempted and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/sand-ceremony-script/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/sand-ceremony-script/11-body.md` (08-final.md wording unchanged; front matter and 6 fact markers removed; 4 IMAGE SLOT comments and the LINK WW-051 comment kept; inline links and UTMs kept; no [[VERIFY]] markers in the body)
- `content/posts/sand-ceremony-script/booking-checklist.md` (sand ceremony planning checklist, celebrant questions, venue or council questions including access and privacy)
- Title: Sand Ceremony Script With Sample Wording (39 chars)
- Slug: sand-ceremony-script. URL: https://weddedwonderland.com/expert-advice/sand-ceremony-script
- Type: New (not a refresh, no redirect)
- Categories: Expert Advice (primary, set explicitly), Ceremony, Planning Guides
- Author/byline: Wedded Wonderland
- Meta title: Sand Ceremony Script With Sample Wording for Your Wedding (57 chars, keyword first, no colon or dash, from 02-seo.json)
- Meta description: A sand ceremony script to read word for word, with sample wording for couples, children and blended families, plus where it fits and what you need. (147 chars, no figures, from 02-seo.json unchanged)
- Focus keyword: sand ceremony script. Canonical: the URL above. OG image: featured slot.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body; 08-final.md has no `<!-- CTA: primary -->` marker): secondary Wedded Concierge link (end of the template section), primary Wedded Concierge link (end of the beach and destination section), magazine link (unity ritual section), closing Wedded Concierge link (close). All utm_campaign=sand-ceremony-script.

## Checklist (publish-checklist.md)
- [ ] Field map CONFIRMED: no (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0] (Expert Advice)
- [ ] Images prepared with alt and caption: not done, all 4 slots `needed`
- [ ] Logged into CMS: not checked (package-only run)
- [ ] Images uploaded first: not done
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body with inline images: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA blocks: in package (inline), not entered
- [ ] FAQ block: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` holds nothing from this run

## Categories and the CMS category bug
- Primary category Expert Advice must be set explicitly with the field-map method, not left to list order.
- Secondary categories Ceremony and Planning Guides come from 01-brief.json and are not confirmed against the live CMS category list. Match them to existing CMS categories; do not create new ones.
- Known CMS bug: recently saved posts have been moved into category paths. After Save Draft (and again at publish), check the URL is exactly `/expert-advice/sand-ceremony-script`.

## Images
Place images by the IMAGE SLOT comments in `11-body.md`, not the provisional `after_h2` numbers in `04-images.json`:
- `featured`: featured image and OG image (comment at the top of the body)
- `family-pour`: under the H3 "With children or a blended family"
- `vessels-still-life`: under the H2 "What you need for a sand ceremony"
- `beach-destination`: under the H2 "A sand ceremony at a beach or destination wedding"

All 4 slots are still `needed`. Licensed images only; never AI for real people or places. Children only with written parental or guardian consent recorded in the register; otherwise hands-only or faces not visible. The vessels still life (no people, no real place) may be AI only if Nic approves, captioned "Illustrative image". The beach slot is never AI. Do not publish with `[[IMAGE NEEDED]]` captions.

## Open items before publish
- **LINK WW-051:** the unity ceremony ideas sentence in "Sand ceremony or another unity ritual" carries `<!-- LINK WW-051: unity ceremony ideas article, add URL when live -->`. Add the URL when WW-051 is live, or leave the sentence as plain text and delete the comment.
- [[VERIFY licence]] for every image used, and [[VERIFY credit]] for each caption.
- No prices in the post, so nothing for Nic's price sign-off. Nic to confirm the Wedded Concierge lines (secondary, primary, closing with the fee line) and the magazine link, and approve or decline the AI still life.
- From 09-cro.json: Nic to confirm whether "Start the conversation" leads to a call or a form (not added to copy).
- Set datePublished at publish.
- Check the live URL is exactly `/expert-advice/sand-ceremony-script` (category bug).

## Legal note
The Marriage Act 1961 (sections 45 and 46) and Smartraveller points in the post are general information as at November 2026, not legal advice. The body quotes the Act and links the official sources at each claim, and tells overseas couples to talk to a lawyer.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=sand-ceremony-script`.
