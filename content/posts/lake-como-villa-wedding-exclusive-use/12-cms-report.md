# CMS report: lake-como-villa-wedding-exclusive-use

**Draft URL / ID:** Not uploaded: no browser connection in this cloud session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-10-21
- Package: `content/posts/lake-como-villa-wedding-exclusive-use/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/lake-como-villa-wedding-exclusive-use/11-body.md`
- Target URL: https://weddedwonderland.com/destination-weddings/lake-como-villa-wedding-exclusive-use
- Primary category: Destination Weddings (= categories[0])

## Package build (Part 1)

- [x] Body built from `08-final.md`: primary CTA at the `<!-- CTA: primary -->` marker, secondary CTA and lead magnet at the close, all `<!-- fact_xx -->` markers removed, 17 `[[VERIFY]]` markers and 12 image-slot comments kept
- [x] Inline `/wonderland-concierge` link given `utm_content=inline` UTMs
- [x] Key takeaways (5) and FAQ (6) extracted
- [x] Categories: Destination Weddings, Italy, Venues; primary_category = Destination Weddings
- [x] Tags (5), meta title, meta description, focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage
- [x] draft_note: 17 VERIFY items, Nic sign-off (Nulla Osta AUD 80 fee), 12 image slots needed, 6 deferred business items
- [x] `python3 -I content-system/scripts/validate.py content/posts/lake-como-villa-wedding-exclusive-use`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 12 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started (images, featured image, title/slug/excerpt/author, body, Key Takeaways, CTA blocks, FAQ, categories and primary category, tags, SEO fields, schema, draft note, Save Draft).

After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt and caption: none supplied in `04-images.json` (no approved images); left empty, not invented.
- `11-body.md` keeps the `08-final.md` front matter; strip it if the CMS body field does not accept it.
- Deferred business items (person's decision): fee model/commissions, deposits/refunds/contracts, From AUD price range, Wedded Privileges explanation, named Advisor/phone line, real wedding at a listed villa.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=lake-como-villa-wedding-exclusive-use`. Nothing was published or scheduled.
