# CMS report: paros-wedding-venues

**Draft URL / ID:** Not uploaded: no browser connection in this session and the CMS field map is not yet confirmed (run /wedded-cms-discovery locally)

- Date: 2026-11-11
- Title: Paros Wedding Venues and How to Get Married There
- Package: `content/posts/paros-wedding-venues/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/paros-wedding-venues/11-body.md`
- Booking checklist: `content/posts/paros-wedding-venues/booking-checklist.md`
- Target URL: https://weddedwonderland.com/destination-weddings/paros-wedding-venues (CMS slug `paros-wedding-venues`)
- Primary category: Destination Weddings (= categories[0]); type Guide; cluster Getting Married in Greece
- New article, no redirect

## Package build (Part 1)

- [x] Confirmed `08-final.md` already carries the `09-cro.json` copy change (primary marker filled after the table) and the 8b edits; secondary, closing and magnet links were already in place
- [x] Body built from `08-final.md`: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 8 image-slot comments kept, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA block (Speak with a Wedded Advisor, subtext "The fee is agreed in writing before any work begins.") at the `<!-- CTA: primary -->` marker; the inline sentence after it retagged `utm_content=inline` (as the Mykonos model); secondary, closing and lead magnet links marked with comments; each `utm_content` link appears once
- [x] Key takeaways: exactly the 4 in the body, copied verbatim; FAQ (6) extracted
- [x] Categories: Destination Weddings, Greece, Venues; primary_category = Destination Weddings; tags (7) from the brief, unchanged
- [x] Meta title "Paros Wedding Venues and How to Get Married There" (from `02-seo.json`, matches the H1); meta description kept from `02-seo.json` because Naoussa, Parikia, Kolymbithres and Golden Beach all have a venue in the body (151 characters); focus keyword, canonical, OG image slot (featured)
- [x] schema_jsonld: Article (datePublished empty) + BreadcrumbList (Home > Destination Weddings > post) + ItemList (8 venues, official URLs) + FAQPage (6)
- [x] Images: 8 slots in the body (featured, 3 areas, 3 venues, legal still life), all `needed`
- [x] verify_items: image credits and licences only (8); needs_signoff empty (no prices)
- [x] draft_note: linked drafts to publish together, mobile table scroll, jump list, image slots, deferred business items
- [x] redirects_recommended: none (new article)
- [x] `python3 -I content-system/scripts/scan_copy.py content/posts/paros-wedding-venues/11-body.md`: no banned words, 0 dashes, no overlaps; flagged "exclusive" 13 (expected in a venue guide comparing exclusive use); no change made
- [x] `python3 -I content-system/scripts/validate.py content/posts/paros-wedding-venues`: All valid

## CMS checklist (Part 2: not run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED (currently "NOT YET MAPPED")
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (0 of 8 approved; all `needed`)
- [ ] The person is logged into the CMS in the Chrome tab (no browser connection in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## Publish together

The body links four drafts: /destination-weddings/greece-wedding-venues (three times, one with the #getting-legally-married-in-greece-as-australians-in-brief anchor), /destination-weddings/greece-wedding-packages (once), /destination-weddings/mykonos-wedding-venues (once) and /expert-advice/greek-wedding-traditions (once). Publish the Greece venues guide, the Greece packages guide, Mykonos wedding venues and Greek wedding traditions together with this post, or hold this post until they are live. The Greece venues and packages guides and the Mykonos guide should link down to this post where they mention Paros.

## Mismatches and open points

- Field map not confirmed, so no CMS labels could be checked against the package.
- No `[[VERIFY]]` markers in the copy. Publishing blockers are image credits and licences (8 slots) only.
- Author: no named author in the inputs; package uses "Wedded Wonderland" pending confirmation.
- Image alt, caption, credit and licence: none supplied in `04-images.json` apart from the legal-still-life caption ("Illustrative image"); left empty, not invented.
- `04-images.json` still uses generic file names: featured (`paros-wedding-venues-featured-venue-ceremony-hero.webp`; the body brief names Petra Farm or Astir of Paros), venue-01 (`paros-wedding-venues-venue-01-naoussa-north-ceremony-setting.webp`) is Monastiri, venue-02 (`paros-wedding-venues-venue-02-west-or-inland-ceremony-setting.webp`) is Villa Mira Paros, venue-03 (`paros-wedding-venues-venue-03-east-south-ceremony-setting.webp`) is The Secret View. area-inland-villages is planned in `04-images.json` but has no slot in the body. The package uses the `04-images.json` file names as they stand. Normalise `04-images.json`.
- No image slot for Astir of Paros, Anemoi, Petra Farm, Pyrgaki or Poseidon in the body (none planned in `04-images.json`).
- The legal-still-life slot: AI only with the person's approval, and then captioned "Illustrative image".
- The at-a-glance table has four columns with long cells and must scroll sideways on mobile; check in the mobile preview.
- Jump list anchors (#naoussa-and-the-north, #parikia-and-the-west, #golden-beach-and-the-east-coast, #how-to-get-married-on-paros) depend on the CMS generating heading IDs; check in preview.
- Booking checklist items flagged for confirmation before quoting: Astir current wedding terms (page from 2018) and chapel ceremonies; Pyrgaki current terms (2020) and the Hundred Doors church option; The Secret View Terrace 110/120 vs 250 conflict; Monastiri wedding capacity (800 is the corporate amphitheatre); Petra Farm guest accommodation and overall maximum; Villa Mira capacity; Anemoi chapel ceremony types; Poseidon capacity and rooms; civil marriage steps with the Municipality of Paros; whether Greece needs a CNI; Orthodox and symbolic requirements; plus step-free access, transfers and drive times, and where guests stay at every venue.
- Deferred business items (person's decision): a real Paros or Greece wedding, fee model and commissions, an Advisor who calls first, referral or assistant contact, mobility checks by venue, proof of 200 to 400 guest scale.

## Next step

Source and license the 8 images, then run `/wedded-cms-discovery` locally in a Chrome tab where you are logged into the CMS, confirm the field map, then `/wedded-blog resume=paros-wedding-venues`. Nothing was published or scheduled.
