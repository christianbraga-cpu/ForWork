# CMS report: wedding-destinations-november

**Draft URL / ID:** Not uploaded. Package-only mode: the person uploads the post from the Word doc. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/destination-weddings/wedding-destinations-november (path `/destination-weddings/wedding-destinations-november`). The category bug has moved earlier posts. If it differs, do not publish; fix the primary category or confirm with the dev team first.**

**Anchor check:** the H2 "Wedding destinations in November at a glance" must produce the anchor `#wedding-destinations-in-november-at-a-glance`, because the intro links to it ("table at the end of the list"). Check it in preview. If the CMS gives the heading a different ID (or none), remove that link from the intro rather than leaving a dead jump link.

- Date: 2026-11-26
- Plan ref: WW-296
- Title / H1: Wedding Destinations in November for Autumn or Spring (53 characters)
- Meta title: Wedding Destinations in November for Autumn or Spring (53)
- Meta description: Wedding destinations in November, from autumn on the Greek islands and in Portugal to spring in New Zealand, plus Bali, Fiji and Hawaii. (136, from `02-seo.json`)
- Focus keyword: wedding destinations november
- Package: `content/posts/wedding-destinations-november/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/wedding-destinations-november/11-body.md`
- Booking checklist: `content/posts/wedding-destinations-november/booking-checklist.md`
- Target URL: /destination-weddings/wedding-destinations-november (slug `wedding-destinations-november`); canonical https://weddedwonderland.com/destination-weddings/wedding-destinations-november
- Categories: Destination Weddings (primary, = categories[0], set explicitly), Planning Guides. No "Latin America & Caribbean" or "Africa" category.
- Status: Draft only. Never Publish or Schedule.
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, prose unchanged
- [x] All 41 links and the 4 UTM links kept exactly as in `08-final.md`, same order; internal links relative
- [x] Three LINK comments kept in "How we chose these ten November destinations": August, March and Punta Cana (`<!-- LINK: /destination-weddings/punta-cana-destination-wedding when live; add as an entry ... fact_117) -->`; the `fact_117` text is inside the LINK comment and was kept). Add each link when the page is live.
- [x] No `<!-- CTA: primary -->` marker in `08-final.md`, so nothing replaced; no CTA marker comments added. CTA links in place per `09-cro.json`: primary (after the at-a-glance table), secondary, magnet, closing; each utm_content appears once
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (5) taken verbatim from the body
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 7 slots, all `needed`; alt and caption left empty (nothing invented); no AI images
- [x] No prices; needs_signoff empty (nothing for Nic)
- [x] draft_note: "DRAFT. Do not publish until checked:" + image slots, european slot mismatch, licence question, anchor check, LINK comments, URL check, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/wedding-destinations-november`: All valid (14 stage files)

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
2. Title, slug `wedding-destinations-november`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md` (or the Word doc); fill the Key Takeaways block (4) and the FAQ (5). Use the CTA links as they are in the body; don't add a second primary CTA link.
4. Categories Destination Weddings and Planning Guides, then **set Destination Weddings as the primary category explicitly**; add tags.
5. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
6. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
7. **Check the URL** is exactly /destination-weddings/wedding-destinations-november.
8. Preview desktop and mobile: images, links, CTA, breadcrumb (Home > Destination Weddings > post), the intro jump link to `#wedding-destinations-in-november-at-a-glance`, and the 3-column at-a-glance table (10 rows) on mobile.

## Images (7 slots, all needed)

| Slot | Role | Sits in | Rule |
|---|---|---|---|
| featured | featured | Under the H1 | Outdoor ceremony at a listed destination; month taken recorded before any "autumn" or "spring" caption |
| northern-autumn | inline | Opening "Autumn in the northern hemisphere" | Northern hemisphere terrace or garden; no people; never imply venues are open in November |
| european | inline | Amalfi Coast entry | **Mismatch:** filename `wedding-destinations-november-europe-villa-lakefront-terrace.webp` and the only own-site candidates (Villa Balbiano, Villa Pizzo) are Lake Como, a reserve that is not in the list. Use a named Amalfi Coast image and rename the file, or move the slot to the entry the image shows |
| southern-spring | inline | Opening "Spring and early summer in the southern hemisphere" | Southern hemisphere beachfront, garden or lodge lawn; "spring" only where sourced |
| new-zealand | inline | New Zealand entry | Named New Zealand lodge, vineyard or lakeside lawn; month taken (October to December) recorded; weather stays in the copy |
| tropical | inline | Bali entry | Use a named Bali venue, or move the slot to the entry the image shows. Never caption November weather, wet season or cyclone season |
| planning | inline | "What to plan for a November wedding abroad" | Flat-lay, no real place; owned, licensed or Canva brand asset. Not generated; AI illustrative only with orchestrator approval and an "illustrative" label |

- Every place image shows a real destination: licensed or owned only, **never AI**, location proven by register row, EXIF or source page.
- The month taken must be recorded for every place image so the caption is true.
- People only with written couple and guest consent.
- **Own-site gallery licence (open question):** venue galleries on weddedwonderland.com may be used only if the partner agreements allow blog use. Not confirmed; images not viewed or location-verified.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` before any automated upload.
- `04-images.json` is still `needs_input` and its european slot targets Lake Como (see Images). Re-run stage 04 once photos exist.
- `09-cro.json` lists the CTA links as absolute URLs; the body keeps them relative exactly as in `08-final.md` (same paths and UTMs).
- The New Zealand source link in `08-final.md` is `https://niwa.co.nz/climate-and-weather/monthly/climate-summary-november-2025`, while `02-seo.json` lists Earth Sciences New Zealand at `https://earthsciences.nz/`. Kept as written; check it resolves in preview.
- The Greek islands source link is `http://oldportal.emy.gr/...` (http, an old portal). Check it still resolves in preview.
- Backlinks to add (from `02-seo.json`): the August and March drafts should link to this page ("wedding destinations in November"), plus `/expert-advice/best-honeymoon-destinations-by-month` and `/destination-weddings/best-time-to-get-married-in-bali` (the Bali one carries its own VERIFY on the live wording).
- `link-map.csv` is stale (honeymoon in November redirects, how-to-plan redirect); suggest `/wedded-linkmap` refresh.
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/destination-weddings, which is not a row in `link-map.csv`; confirm the category archive URL.
- Several lines are dated "As at November 2026" (Smartraveller); recheck if publishing is delayed.
- `10-distribution.json`: pins and carousel are on hold until the images are licensed and approved.
- `09-cro.json` open questions (fee model, deposits, on-the-day contact and so on) are for /wonderland-concierge, not this post.
- Questions for couples are in `booking-checklist.md` and don't block publishing.
