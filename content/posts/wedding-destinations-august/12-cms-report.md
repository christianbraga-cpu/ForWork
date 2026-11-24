# CMS report: wedding-destinations-august

**Draft URL / ID:** Not uploaded. No browser in this cloud session, and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED` (not CONFIRMED). Nothing was saved, scheduled or published in the CMS. A human saves as Draft; a human clicks Publish.

**After saving the draft, check the URL is exactly https://weddedwonderland.com/destination-weddings/wedding-destinations-august. The category bug has moved earlier posts (for example /wedding-rsvp-website to /expert-advice/..., /22-amazing-table-settings-for-every-wedding-theme to /style-advice/...). If it differs, do not publish; fix the primary category or confirm with the dev team first.**

- Date: 2026-11-24
- Title / H1: Wedding Destinations in August for Summer or Winter Weddings (60 characters)
- Package: `content/posts/wedding-destinations-august/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/wedding-destinations-august/11-body.md`
- Booking checklist: `content/posts/wedding-destinations-august/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/wedding-destinations-august (slug `wedding-destinations-august`)
- Categories: Destination Weddings (primary, = categories[0], set explicitly), Planning Guides
- New article; no redirect.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed, H1 is the title, all `<!-- fact_xx -->` markers removed, 7 image-slot comments kept, prose, links and UTMs unchanged (diff clean)
- [x] No `<!-- CTA: primary -->` marker in `08-final.md`, so nothing was replaced. CTA positions marked per `09-cro.json`: `<!-- CTA BLOCK: primary -->` after the at-a-glance table, `<!-- CTA INLINE: secondary -->`, `<!-- CTA INLINE: closing -->`, `<!-- LEAD MAGNET -->`. Each utm_content appears once in visible links.
- [x] No `[[VERIFY]]` markers in the copy (none in `08-final.md`)
- [x] Key takeaways (4) and FAQ (5) taken verbatim from the body
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title "Wedding Destinations in August for Summer or Winter Vows" (56); meta description from the META comment (133); focus keyword "wedding destinations august"; canonical set
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 7 slots, all `needed`; alt and caption left empty (nothing invented)
- [x] No prices; needs_signoff empty (nothing for Nic)
- [x] draft_note: "DRAFT. Do not publish until checked:" + image slots, Bali caption rule, Lake Como licence flag, URL check, byline
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/wedding-destinations-august`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (it says NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 7)
- [ ] Logged into the CMS in a Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=wedding-destinations-august once the field map is confirmed)

1. Source and upload the 7 images with alt text and captions; set the featured image (see Images below).
2. Title, slug `wedding-destinations-august`, excerpt, author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body from `11-body.md`; fill the Key Takeaways block (4), the CTA block at `<!-- CTA BLOCK: primary -->` if the template uses one (without duplicating the primary link), and the FAQ (5).
4. Categories Destination Weddings and Planning Guides, then **set Destination Weddings as the primary category explicitly**; add tags.
5. SEO: meta title, meta description, focus keyword, canonical, OG image (featured); schema JSON-LD if the CMS has a field.
6. Paste `draft_note` into the internal note field, then **Save Draft**. Never Publish or Schedule.
7. **Check the URL** is exactly https://weddedwonderland.com/destination-weddings/wedding-destinations-august.
8. Preview desktop and mobile: images, links, CTA, breadcrumb (Home > Destination Weddings > post), and the 3-column at-a-glance table on mobile.

## Images (7 slots, all needed)

| Slot | Role | Rule |
|---|---|---|
| featured | featured | European sea-view summer ceremony at a named venue; month taken (July to August) recorded |
| summer-in-europe | inline | Named European venue (Italy or Greece), summer evening reception; month recorded |
| greek-island | inline | Named Greek island venue matching the H3; month recorded |
| lake-como | inline | Named Lake Como villa; see partner flag below |
| dry-season-winter-escapes | inline | Fiji venue (per the slot comment), not Bali; month (June to September) recorded |
| bali | inline | Named Bali venue; **never caption or alt-text Bali as dry season** |
| fiji | inline | Named Fiji resort; month recorded |

- All are real destinations: licensed or owned only, **never AI**, location proven by register row, EXIF or source page.
- The month taken must be recorded for every image so the caption is true.
- People only with written couple and guest consent.
- **Lake Como flag:** the slot comment names Villa Balbiano and Villa Pizzo galleries on our own site. They may be used only if the partner agreements allow blog use. Not confirmed; images not yet viewed or location-verified.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package. Run `/wedded-cms-discovery` first.
- `04-images.json` was written before `02-seo.json` and `03-source-pack.json` existed: it names no venues, and the file names for `bali` (`...bali-clifftop-venue-august.webp`) and `dry-season-winter-escapes` (`...fiji-august-ceremony-setup.webp`) contain "dry-season". The package copies these paths literally; rename the Bali file before upload so the file name does not call Bali dry season. Its verify items also still say "Bali ... dry season"; they are reworded in the package.
- Author: no named author in any input.
- Breadcrumb level 2 uses https://weddedwonderland.com/destination-weddings, which is not a row in `link-map.csv`; confirm the category archive URL.
- The Greek islands source link is `http://oldportal.emy.gr/...` (http, an old portal). Check it still resolves in preview.
- Several lines are dated "As at November 2026" (Smartraveller); recheck if publishing is delayed.
- `09-cro.json` open questions (Concierge fee model, commissions, deposits, private channel) are for /wonderland-concierge, not this post.
- Booking questions for couples are in `booking-checklist.md` and don't block publishing.
