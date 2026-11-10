# CMS report: greece-wedding-venues

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-10
- Title: 20 Greece Wedding Venues From the Islands to Athens
- Package: `content/posts/greece-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/greece-wedding-venues/11-body.md`
- Booking checklist: `content/posts/greece-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/greece-wedding-venues
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries all 6 `06-edit-final.json` edits and both `09-cro.json` copy changes
- [x] Body built from `08-final.md`: primary CTA block at the `<!-- CTA: primary -->` marker, secondary CTA block and lead magnet marked at the close, all `<!-- fact_xx -->` markers removed, 28 image-slot comments kept, no `[[VERIFY]]` markers
- [x] Inline `/wonderland-concierge` link after the table retagged `utm_content=inline` (as the Lake Como model); all UTMs use `utm_medium=content`
- [x] Key takeaways (exactly the 4 in the body) and FAQ (6) extracted
- [x] Categories: Destination Weddings, Greece, Venues; primary_category = Destination Weddings; tags (6) from the brief
- [x] Meta title and description, focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (20 venues, official URLs) + FAQPage (6)
- [x] Images: 28 slots (featured, 7 regions, 20 venues), all `needed`
- [x] verify_items empty; draft_note lists image slots, deferred business items and the hub recommendation
- [x] redirects_recommended: none
- [x] `python3 -I content-system/scripts/validate.py content/posts/greece-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 28 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Hub recommendation (recommendation only; nothing on the live site changes)

Retitle the hub /destinations/europe/greece to target "greece weddings" and "destination wedding greece" with a packages angle, leaving "greece wedding venues" to this guide. Link the two both ways: this guide already links the hub twice; the hub should add a link to this guide.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt and caption: none supplied in `04-images.json`; left empty, not invented.
- `04-images.json` defines a `venue-<nn>` pattern, not 20 concrete slots, and has no `region-halkidiki` slot (the body does); those 21 file names were derived from the pattern and its slug map. Normalise in `04-images.json` if needed.
- One&Only Aesthesis Agora Veranda capacity (250 vs 300 on the resort's own pages) is on the booking checklist, not a marker.
- The transfers-section Wedded Concierge link keeps `utm_content=secondary` as in `08-final.md`.
- `11-body.md` keeps the `08-final.md` front matter; strip it if the CMS body field does not accept it.
- Deferred business items (person's decision): fee model/commissions, deposits/refunds/contracts, From AUD price range, Wedded Privileges explanation, named Advisor/phone line, real Greek wedding, large-event credentials.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=greece-wedding-venues`. Nothing was published or scheduled.
