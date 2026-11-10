# CMS report: crete-wedding-venues

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-10
- Title: 15 Best Crete Wedding Venues
- Package: `content/posts/crete-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/crete-wedding-venues/11-body.md`
- Booking checklist: `content/posts/crete-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/crete-wedding-venues (CMS slug `crete-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` copy changes (primary marker filled after the table, secondary inline link on the house-rules sentence, closing brand-facts lines)
- [x] Body built from `08-final.md`: front matter removed, all `<!-- fact_xx -->` markers removed, 11 image-slot comments kept, no `[[VERIFY]]` markers
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline` (as the Greece model); secondary, closing and lead magnet links marked with comments; each `utm_content` appears once
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (6) extracted
- [x] Categories: Destination Weddings, Greece, Venues; primary_category = Destination Weddings; tags (7) from the brief
- [x] Meta title and description, focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (15 venues, official URLs) + FAQPage (6)
- [x] Images: 11 slots in the body (featured, 4 areas, 6 venues), all `needed`
- [x] verify_items: image credits and licences (11) and jump list anchors (1) only; needs_signoff empty (no prices)
- [x] draft_note: linked drafts to publish together, mobile table scroll, jump list, image slots, deferred business items
- [x] redirects_recommended: none (new article)
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/crete-wedding-venues/11-body.md`: no banned words, 0 dashes, no overlaps; "exclusive" flagged 22 times (expected in a venue guide comparing exclusive use; no change made)
- [x] `python3 -I content-system/scripts/validate.py content/posts/crete-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 11 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Publish together

The body links two drafts: /destination-weddings/greece-wedding-venues (twice) and /expert-advice/greek-wedding-traditions (once). Publish them with this post, or hold this post until they are live. The Greece guide's Crete section should link down to this post.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt, caption, credit and licence: none supplied in `04-images.json`; left empty, not invented.
- `04-images.json` still holds slots for venues not in the final article (venue-02 Daios Cove, venue-11 Kapsaliana, venue-12 Domes Zeen, venue-13 Talos Villas, venue-15 Manousakis Winery) and slots for listed venues with no body placement (venue-03, venue-05, venue-08, venue-09). The package carries only the 11 body slots. Normalise `04-images.json`.
- The at-a-glance table has six columns and must scroll sideways on mobile; check in the mobile preview.
- Jump list anchors (#elounda-and-agios-nikolaos, #hersonissos-and-the-heraklion-coast, #rethymno, #chania-and-the-west) depend on the CMS generating heading IDs; check in preview.
- Title follows the person's title and the 08-final.md front matter ("15 Best Crete Wedding Venues"); the brief's working title differs. Meta title is the SEO stage's "Crete Wedding Venues: 15 From Elounda to Chania".
- Booking checklist items flagged for confirmation before quoting: Minos Beach wedding services conflict (hotel page vs Marriott events page), Abaton 2027 terms, Caramel ceremony type, Porto Elounda 2026 works, Minos Palace adults-only, Sea View locality and ceremony type, plus access and level paths for older guests at every venue.
- Deferred business items (person's decision): a real Crete or Greece wedding, fee model and commissions, an Advisor who calls first, referral or assistant contact.

## Next step

Run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=crete-wedding-venues`. Nothing was published or scheduled.
