# Stage 12 CMS report: wedding-morning-timeline (NEW ARTICLE)

**Draft URL/ID:** not uploaded. This was a package-only run, as instructed. There is no browser tool in this cloud session, no login was attempted and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled.

**Status:** Draft only. A human clicks Publish.

## URL check (read before saving)
- **Target URL: https://weddedwonderland.com/expert-advice/wedding-morning-timeline**, slug `wedding-morning-timeline`.
- Primary category **Expert Advice**. Set it explicitly with the field-map method, not by list order alone.
- The CMS category bug has moved earlier posts.
- **After Save Draft, check the URL is exactly `/expert-advice/wedding-morning-timeline`.** If it differs, fix the category or slug before publish. Check again at publish.

## Package
- `content/posts/wedding-morning-timeline/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-morning-timeline/11-body.md`: 08-final.md wording is unchanged. Front matter, META comments, the H1 and 2 fact markers (fact_01, fact_02) were removed. The 4 IMAGE SLOT comments, the 2 LINK comments, inline links and UTMs were kept. The body has no [[VERIFY]] markers.
- `content/posts/wedding-morning-timeline/booking-checklist.md`: a fill-in getting-ready schedule worked back from the ceremony, a chair-order table, and questions for the stylist and artist, the photographer and the venue.
- H1 and meta title: Wedding Morning Timeline for the Getting Ready Hours (52 chars)
- Meta description (from the 08-final.md META comment, 144 chars): A wedding morning timeline worked back from your ceremony: when hair and makeup start, the chair order, when to dress and where the buffer goes.
- Excerpt: 210 chars.
- Focus keyword: wedding morning timeline. Canonical: the target URL. OG image: featured slot.
- Categories: Expert Advice (primary, set explicitly), Wedding Planning, Destination Weddings. Match them to existing CMS categories and do not create new ones.
- Tags: wedding morning timeline, getting ready, hair and makeup schedule, wedding day timeline, destination wedding planning.
- Key takeaways: 4. FAQ: 5 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice at /blog/expert-advice > post) and FAQPage. datePublished is left empty.
- CTAs from 09-cro.json are already inline (08-final.md has no `<!-- CTA: primary -->` marker):
  - primary Wedded Concierge (end of "Destination wedding mornings")
  - secondary Wedded Concierge and the magazine link (after the template table)
  - closing Wedded Concierge ("Start from the ceremony")
  - All use utm_campaign=wedding-morning-timeline.
- **No prices** anywhere in the post or checklist, so nothing for Nic's price sign-off.

## LINK comments in 11-body.md (keep; must not render as visible text)
1. **WW-127**, section "Why your trial sets the pace", after the beauty prep link: `<!-- LINK: WW-127 beauty prep countdown, add URL when live; if WW-127 is the beauty prep page above, delete this note -->`. Confirm whether WW-127 is /expert-advice/bridal-beauty-prep-what-to-book-test-and-schedule-before-your-wedding. If it is, delete the comment. If not, add the WW-127 URL once live.
2. **4pm page**, section "A sample wedding morning timeline for a 4pm ceremony": `<!-- LINK: /expert-advice/wedding-timeline-4pm-ceremony when live -->`. Link "our full 4pm wedding timeline" once that page is live. It was a draft on 2026-11-24.

## Jump link (web team)
The intro sentence "For the example times, jump to the [sample morning for a 4pm ceremony](#a-sample-wedding-morning-timeline-for-a-4pm-ceremony)" needs the H2 "A sample wedding morning timeline for a 4pm ceremony" to carry the ID `a-sample-wedding-morning-timeline-for-a-4pm-ceremony`. **Web team: check the CMS gives that heading this anchor ID in the saved Draft.** If it does not, use the ID the CMS creates, or drop the jump sentence.

## Redirect recommendation (user's call)
Recommend a **301 from /your-pre-ceremony-wedding-schedule-sorted to https://weddedwonderland.com/expert-advice/wedding-morning-timeline at publish.** The old page was published in 2016, covers the same pre-ceremony intent and ranks for nothing in AU (DataForSEO ranked keywords; GSC not checked). This is your decision. Nothing has been changed on the old page.

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
- [ ] URL exactly /expert-advice/wedding-morning-timeline after save: not checked (nothing saved)
- [ ] Jump-link anchor ID checked in the saved Draft: not checked
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` is empty

## Images (4 slots needed, none sourced)
Place each image at its IMAGE SLOT comment in `11-body.md`:
- `featured`: featured and OG image. Hair or makeup by a window in morning light. **Licensed or owned real photo with written consent. Never AI.**
- `wedding-party-together`: end of "The order of the hair and makeup chairs". **Licensed or owned real photo with written consent from every identifiable adult. Children only with written parental consent. Never AI.**
- `getting-ready-suite`: end of "Setting up the getting ready space". Outfits and breakfast, no identifiable people. **Licensed or owned real photo. Never AI.**
- `printed-schedule`: start of the 4pm sample section. An owned photo or Canva brand asset is preferred. **AI only with Nic's written approval, captioned "Illustrative image"**, with placeholder names only. Any readable times must match the article's 4pm examples.

Record each licence, credit, consent, venue and town in library-index.csv before use. Alt text and captions are drafted; rewrite them to match the final images. Do not publish with `[[IMAGE NEEDED]]` captions.

## Backlinks to add once live (02-seo.json)
- /expert-advice/wedding-day-timeline (required), anchor "wedding morning timeline"
- /expert-advice/wedding-day-timeline-template, anchor "the getting-ready hours, chair by chair"
- /expert-advice/bridal-beauty-prep-what-to-book-test-and-schedule-before-your-wedding, anchor "a timed running order"

## Flags for Nic
- No prices in the post, so nothing for price sign-off.
- Source and approve licensed, consented real-wedding photos for featured, wedding-party-together and getting-ready-suite.
- For printed-schedule, supply an owned or Canva asset, or give written approval for an AI still life captioned "Illustrative image".

## Open items before publish
- Author: not recorded in stages 01 to 10. The team sets the byline and shows a last-updated date.
- URL exactly /expert-advice/wedding-morning-timeline after Save Draft.
- Jump-link anchor ID (above).
- The two LINK comments (above).
- [[VERIFY licence]] and [[VERIFY credit]] for all four images, plus venue and town for the photo captions.
- Set datePublished at publish.
- 301 decision for /your-pre-ceremony-wedding-schedule-sorted.

## Wording checks
- The banned end-of-night dance phrase from the brief appears nowhere in the body, package or checklist.
- Nothing in the post, package or checklist states or implies that the Wedded Advisor runs, coordinates or attends the wedding morning.
- No em dashes. Australian English.

## Mismatches
- None checked on screen, because this was a package-only run and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-morning-timeline`.
