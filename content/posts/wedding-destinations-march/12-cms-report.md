# CMS report: wedding-destinations-march

**Draft URL / ID:** Not uploaded. Package-only mode: the person uploads the post from the Word doc. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/destination-weddings/wedding-destinations-march. The category bug has moved earlier posts. If it differs, do not publish; fix the primary category or confirm with the dev team first.**

**Anchor check:** the H2 "Wedding destinations in March at a glance" must produce the anchor `#wedding-destinations-in-march-at-a-glance`, because the intro links to it ("table at a glance"). Check it in preview. If the CMS gives the heading a different ID (or none), remove that link from the intro rather than leaving a dead jump link.

- Date: 2026-11-25
- Title / H1: Wedding Destinations in March for Spring or Autumn Weddings (59 characters)
- Meta title: Wedding Destinations in March for Spring or Autumn Weddings (59)
- Meta description: Ten wedding destinations for March, from spring on the Greek islands and in Portugal to autumn in New Zealand, plus Bali, Fiji and Mauritius. (141)
- Focus keyword: wedding destinations march
- Package: `content/posts/wedding-destinations-march/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/wedding-destinations-march/11-body.md`
- Booking checklist: `content/posts/wedding-destinations-march/booking-checklist.md`
- Target URL: /destination-weddings/wedding-destinations-march (slug `wedding-destinations-march`); canonical https://weddedwonderland.com/destination-weddings/wedding-destinations-march
- Categories: Destination Weddings (primary, = categories[0], set explicitly), Planning Guides. No "Latin America & Caribbean" or "Africa" category.
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, prose unchanged
- [x] All 42 links and the 4 UTM links kept exactly as in `08-final.md`, same order; internal links relative
- [x] August LINK comment kept: `<!-- LINK: /destination-weddings/wedding-destinations-august when live -->` in "How we chose these ten March destinations". Add the link when the August page is live.
- [x] No `<!-- CTA: primary -->` marker in `08-final.md`, so nothing replaced; no CTA marker comments added. CTA links in place per `09-cro.json`: primary (after the at-a-glance table), magnet, secondary, closing; each utm_content appears once
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (5) taken verbatim from the body
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 7 slots, all `needed`; alt and caption left empty (nothing invented); no AI images
- [x] No prices; needs_signoff empty (nothing for Nic)
- [x] draft_note: "DRAFT. Do not publish until checked:" + image slots, Lake Como licence question, anchor check, LINK comment, URL check, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/wedding-destinations-march`: All valid (14 stage files)

## CMS checklist (Part 2: not run, package-only mode)

- [ ] `cms/field-map.md` status is CONFIRMED (it says NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 7)
- [ ] Upload: not started (the person uploads via the Word doc)
- [ ] After save: not started

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person)

1. Source and upload the 7 images with alt text and captions; set the featured image (see Images below).
2. Title, slug `wedding-destinations-march`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md` (or the Word doc); fill the Key Takeaways block (4) and the FAQ (5). Use the CTA links as they are in the body; don't add a second primary CTA link.
4. Categories Destination Weddings and Planning Guides, then **set Destination Weddings as the primary category explicitly**; add tags.
5. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
6. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
7. **Check the URL** is exactly https://weddedwonderland.com/destination-weddings/wedding-destinations-march.
8. Preview desktop and mobile: images, links, CTA, breadcrumb (Home > Destination Weddings > post), the intro jump link to `#wedding-destinations-in-march-at-a-glance`, and the 3-column at-a-glance table on mobile.

## Images (7 slots, all needed)

| Slot | Role | Rule |
|---|---|---|
| featured | featured | European spring ceremony at a named venue we cover (Italy or Greece); month taken recorded before any "spring" caption |
| northern-spring | inline | Named northern hemisphere venue, early spring planting; no identifiable people |
| greek-island | inline | Named Greek island venue matching the H3; month taken (March to May) recorded |
| lake-como | inline | Lake Como villa; caption and alt name Lake Como only, no venue name; **licence open question** (below) |
| southern-autumn | inline | Named southern hemisphere venue (New Zealand preferred); "autumn" only where sources state it |
| new-zealand | inline | Named New Zealand venue (Queenstown or Central Otago); month taken recorded |
| tropical | inline | Sits in the Bali entry: use a named Bali venue, or move the slot to Fiji if the image is Fiji. Never caption March as dry or wet season |

- All are real destinations: licensed or owned only, **never AI**, location proven by register row, EXIF or source page.
- The month taken must be recorded for every image so the caption is true.
- People only with written couple and guest consent.
- **Lake Como licence (open question):** `04-images.json` names the Villa Balbiano and Villa Pizzo galleries on our own site as candidates. They may be used only if the partner agreements allow blog use. Not confirmed; images not yet viewed or location-verified.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` before any automated upload.
- Two links in `08-final.md` differ from `02-seo.json`: `/expert-advice/symbolic-ceremony` (02-seo: `/expert-advice/should-you-marry-legally-abroad-or-have-a-symbolic-ceremony`) and `/expert-advice/how-to-plan-a-destination-wedding` (02-seo: `/destination-weddings/...`). `link-map.csv` lists both 08-final targets as live redirect targets, so they were kept as written.
- Backlink to add: the August page (draft) should link to this page ("wedding destinations in March"), per `02-seo.json` backlinks_to_add, alongside the other three backlinks listed there.
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/destination-weddings, which is not a row in `link-map.csv`; confirm the category archive URL.
- The Greek islands source link is `http://oldportal.emy.gr/...` (http, an old portal). Check it still resolves in preview.
- Several lines are dated "As at November 2026" (Smartraveller); recheck if publishing is delayed.
- `10-distribution.json`: pins and carousel are on hold until the images are licensed and approved.
- `09-cro.json` open questions (Concierge fee and on-the-day contact) are for /wonderland-concierge, not this post.
- Questions for couples are in `booking-checklist.md` and don't block publishing.
