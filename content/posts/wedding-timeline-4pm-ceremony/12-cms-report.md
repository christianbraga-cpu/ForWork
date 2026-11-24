# Stage 12 CMS report: wedding-timeline-4pm-ceremony (NEW ARTICLE)

**Draft URL/ID:** not uploaded. This was a package-only run, as instructed. There is no browser tool in this cloud session, no login was attempted and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled.

**Status:** Draft only. A human clicks Publish.

## URL check (read before saving)
- **Target URL: https://weddedwonderland.com/expert-advice/wedding-timeline-4pm-ceremony**, slug `wedding-timeline-4pm-ceremony`.
- Primary category **Expert Advice**. Set it explicitly with the field-map method, not by list order alone.
- The CMS category bug has moved earlier posts (for example /wedding-rsvp-website to /expert-advice/wedding-rsvp-website).
- **After Save Draft, check the URL is exactly `/expert-advice/wedding-timeline-4pm-ceremony`.** If it differs, fix the category or slug before publish. Check again at publish.

## Package
- `content/posts/wedding-timeline-4pm-ceremony/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-timeline-4pm-ceremony/11-body.md`: 08-final.md wording is unchanged. Front matter, META comments, the H1 and 6 fact markers were removed. The 4 IMAGE SLOT comments, inline links and UTMs were kept. The body has no [[VERIFY]] markers.
- `content/posts/wedding-timeline-4pm-ceremony/booking-checklist.md`: a fill-in day timeline built from the reader's own sunset (Geoscience Australia, no stated times) and venue questions.
- H1: Wedding Timeline for a 4pm Ceremony With 2pm to 5pm Options (59 chars)
- Meta title: Wedding Timeline 4pm Ceremony With 2pm to 5pm Options (53 chars)
- Meta description (from the 08-final.md META comment, 142 chars): A wedding timeline for a 4pm ceremony, with and without a first look, set by your sunset, plus how the day shifts for a 2pm, 3pm or 5pm start.
- Excerpt: 164 chars, no figures.
- Focus keyword: wedding timeline 4pm ceremony. Canonical: the target URL. OG image: featured slot.
- Categories: Expert Advice (primary, set explicitly), Wedding Planning, Destination Weddings. All three exist as category listings in link-map.csv. Match them to existing CMS categories and do not create new ones.
- Tags: wedding timeline, wedding day schedule, ceremony time, destination wedding planning, timeline template.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice at /blog/expert-advice > post) and FAQPage. datePublished is left empty.
- CTAs from 09-cro.json are already inline (08-final.md has no `<!-- CTA: primary -->` marker):
  - primary Wedded Concierge (end of "Planning a 4pm ceremony at a destination wedding")
  - secondary Wedded Concierge and the magazine link (after the template table)
  - closing Wedded Concierge ("Plan the day around your light")
  - All use utm_campaign=wedding-timeline-4pm-ceremony.
- **No prices** anywhere in the post or checklist, so nothing for Nic's price sign-off.

## Checklist (publish-checklist.md)
- [ ] Field map CONFIRMED: no (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0] (Expert Advice)
- [ ] Images prepared with alt and caption: not done, all 4 slots `needed`
- [ ] Logged into CMS: not checked (package-only run, no browser)
- [ ] Images uploaded first: not done
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package but not entered (author to confirm)
- [ ] Body with inline images: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA blocks: in package (inline), not entered
- [ ] FAQ block: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; the method is unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] URL exactly /expert-advice/wedding-timeline-4pm-ceremony after save: not checked (nothing saved)
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` is empty

## Images (4 slots needed, none sourced)
Place each image at its IMAGE SLOT comment in `11-body.md`:
- `featured`: featured and OG image. An outdoor ceremony in late-afternoon light, with the couple and celebrant. **Licensed or owned real photo with written consent. Never AI.**
- `golden-hour-portraits`: end of "How sunset shapes a 4pm wedding day". **Licensed or owned real photo with written consent. Never AI.**
- `dusk-drinks`: end of "Where the buffer belongs in a 4pm day". **Licensed or owned real photo.** Consent is needed for any identifiable guest, and identifiable children need consent too. **Never AI.**
- `run-sheet`: after the template table. An owned photo or Canva brand asset is preferred. **AI only with Nic's written approval, captioned "Illustrative image"**, with placeholder names only. Any readable times must match the article's example timeline.

Record each licence, credit, venue and town in library-index.csv before use. Alt text and captions are drafted; rewrite them to match the final images. Do not publish with `[[IMAGE NEEDED]]` captions.

## Overlap with the template page
The live /expert-advice/wedding-day-timeline-template (published 2026-10-21) has a full 4pm sheet with and without a first look. It ranks #5 in Singapore for "wedding timeline 4pm ceremony". The user chose to publish this page anyway on 2026-11-24, and this post links to that page. **Recommendation:** trim the template page's 4pm sheet to a two-line summary plus a link here (anchor "wedding timeline for a 4pm ceremony"). This is not a publish blocker.

Backlinks to add once this post is live (02-seo.json `backlinks_to_add`):
- /expert-advice/wedding-day-timeline (required)
- /your-pre-ceremony-wedding-schedule-sorted
- /expert-advice/how-long-is-a-wedding-ceremony
- /expert-advice/wedding-day-timeline-template (the trim above)

## Flags for Nic
- No prices in the post, so nothing for price sign-off.
- Source and approve licensed, consented real-wedding photos for featured, golden-hour-portraits and dusk-drinks.
- For run-sheet, supply an owned or Canva asset, or give written approval for an AI still life captioned "Illustrative image".

## Open items before publish
- Author: not recorded in stages 01 to 10. The team sets the byline and shows a last-updated date (search_visitor asked for both).
- URL exactly /expert-advice/wedding-timeline-4pm-ceremony after Save Draft.
- [[VERIFY licence]] and [[VERIFY credit]] for all four images, plus venue and town for the photo captions.
- Set datePublished at publish.
- Optional: 09-cro's secondary CTA wording suggestion was not applied, and the current line is compliant.

## Wording checks
- The banned end-of-night dance phrase from the brief appears nowhere in the body, package or checklist; the day ends with "the final song" and "the send-off".
- Nothing in the post, package or checklist states or implies that the Wedded Advisor runs, coordinates or attends the day.
- No em dashes. Australian English.

## Mismatches
- None checked on screen, because this was a package-only run and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-timeline-4pm-ceremony`.
