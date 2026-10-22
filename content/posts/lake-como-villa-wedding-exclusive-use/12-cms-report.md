# CMS report: lake-como-villa-wedding-exclusive-use

**Draft URL / ID:** Not uploaded: no browser connection in this cloud session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-10-22 (rebuild for round 5: VERIFY markers 19 to 9 under the new policy in `content-system/rubrics/qa-gates.md`)
- Title: 10 Lake Como Villas You Can Book for an Exclusive-Use Wedding
- Package: `content/posts/lake-como-villa-wedding-exclusive-use/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/lake-como-villa-wedding-exclusive-use/11-body.md`
- Target URL: https://weddedwonderland.com/destination-weddings/lake-como-villa-wedding-exclusive-use
- Primary category: Destination Weddings (= categories[0])

## Package build (Part 1)

- [x] Body rebuilt from round-5 `08-final.md` (10 villas; copy unchanged apart from the round-5 VERIFY rewording, where removed markers became "your Wedded Advisor confirms in writing" lines): primary CTA at the `<!-- CTA: primary -->` marker, secondary CTA and lead magnet at the close, all `<!-- fact_xx -->` markers removed, 9 `[[VERIFY]]` markers and 14 image-slot comments kept
- [x] Inline `/wonderland-concierge` link given `utm_content=inline` UTMs
- [x] Key takeaways (5) and FAQ (6) extracted from `08-final.md`
- [x] Categories: Destination Weddings, Italy, Venues; primary_category = Destination Weddings
- [x] Tags (5), meta title and description (10 villas), focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (all 6 FAQs)
- [x] Images: all 14 slots from `04-images.json` listed, all `needed`
- [x] verify_items = the 9 markers now in the body
- [x] draft_note: 9 VERIFY items, Nic sign-off (Nulla Osta AUD 80 fee), 14 image slots needed, 6 deferred business items, and "Booking checklist (not publishing blockers): see booking-checklist.md"
- [x] `python3 -I content-system/scripts/validate.py content/posts/lake-como-villa-wedding-exclusive-use`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 14 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started (images, featured image, title/slug/excerpt/author, body, Key Takeaways, CTA blocks, FAQ, categories and primary category, tags, SEO fields, schema, draft note, Save Draft).

After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt and caption: none supplied in `04-images.json` (no approved images); left empty, not invented.
- `04-images.json` gives villa-09 (Villa La Felice) and villa-10 (Villino Rubini) bare file names without the `content/posts/.../images/` path; copied as given.
- Two optional editor trims in `06-edit-final.json` (Villa La Felice "a private dock" repeat; Balbiano Milan-centre sentence) were not applied in `08-final.md`, so they stay in the body as written.
- Booking-stage checks dropped from the body under the new marker policy now live in `booking-checklist.md`; they are not publishing blockers.
- `11-body.md` keeps the `08-final.md` front matter; strip it if the CMS body field does not accept it.
- Deferred business items (person's decision): fee model/commissions, deposits/refunds/contracts, From AUD price range, Wedded Privileges explanation, named Advisor/phone line, real wedding at a listed villa.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=lake-como-villa-wedding-exclusive-use`. Nothing was published or scheduled.
