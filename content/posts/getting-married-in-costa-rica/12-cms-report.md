# CMS report: getting-married-in-costa-rica

**Draft URL / ID:** Package ready, not uploaded: no browser in this session and the CMS field map is not confirmed; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-17
- Title: How to Get Married in Costa Rica Step by Step
- Series: fourth post in the "Getting Married in {Country}" series (after Hawaii, Mauritius and the Seychelles); template `content-system/templates/getting-married-in-country.md`
- Package: `content/posts/getting-married-in-costa-rica/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/getting-married-in-costa-rica/11-body.md`
- Booking checklist: `content/posts/getting-married-in-costa-rica/booking-checklist.md` (Costa Rica civil marriage checklist: both routes, documents and steps in order, questions for the Registro Civil, the notary and the resort)
- Target URL: https://weddedwonderland.com/destination-weddings/getting-married-in-costa-rica (CMS slug `getting-married-in-costa-rica`)
- Primary category: Destination Weddings (= categories[0]); then Costa Rica, Latin America & Caribbean, Planning Guides; type planning_guide
- Tags: from the brief, as given
- New article, no redirect.
- **CMS setup needed first:** the `/destination-weddings` folder (URL path) and the **Destination Weddings** category must exist in the CMS before the draft is saved.
- **Seychelles, Mauritius and Hawaii sister links are drafts:** "Venues and planning" links to `/destination-weddings/getting-married-in-seychelles`, `/destination-weddings/mauritius-wedding` and `/destination-weddings/getting-married-in-hawaii`, none live yet. Publish the posts together, or remove that sentence before publishing.
- **Do not link `/destinations/latin-america-caribbean`:** it is not linked in the body; keep it that way in the CMS.

## Package build (Part 1)

- [x] `08-final.md` checked stable before building (modification time 03:22, size 28398 bytes unchanged across checks); it already includes the final-check fixes, so it was built from as is
- [x] Body: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, all links and the 4 UTM links unchanged (link list identical to `08-final.md`), no CTA marker comments, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing "speak with Wedded Concierge" link (utm_content=primary) in "Venues and planning" is the CTA, unchanged (no `<!-- CTA: primary -->` marker in 08-final.md)
- [x] Secondary, closing and magnet links unchanged; each utm_content appears exactly once in the body
- [x] No em dashes; Australian English; `scan_copy.py` on `11-body.md`: 0 banned, 0 flagged, 0 dashes, no overlaps
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (5) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title "How to Get Married in Costa Rica, Step by Step" (46 characters) and meta description (149 characters) from `02-seo.json`; no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty, author and publisher Wedded Wonderland) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 6 slots (featured, documents, civil-ceremony, certificate-australia, when-to-marry, choose-your-region), all `needed`
- [x] verify_items and needs_signoff empty: no `[[VERIFY]]` markers, no price or fee amounts, nothing for Nic to sign off
- [x] Byline Wedded Wonderland
- [x] `python3 -I content-system/scripts/validate.py content/posts/getting-married-in-costa-rica`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not confirmed)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] `/destination-weddings` folder and Destination Weddings category exist in the CMS (not checked; no browser)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=getting-married-in-costa-rica once the field map is confirmed)

1. Create the `/destination-weddings` folder and the Destination Weddings category if they do not exist yet.
2. Source and upload the 6 images with alt text and captions; set the featured image. featured and civil-ceremony come from a licensed real wedding with written consent, never AI (officiant identifiable only with written consent); when-to-marry and choose-your-region are real places proven by media kit, register or EXIF, never AI (record the month taken for when-to-marry); documents and certificate-australia are still lifes (Canva, licensed stock or own shoot; AI only with Wedded Wonderland approval, captioned "Illustrative image"). Instituto Costarricense de Turismo (ICT) media only if its licence covers third-party commercial blog use.
3. Enter title, slug `getting-married-in-costa-rica`, excerpt and author ("Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block if the template uses one (text "Speak with Wedded Concierge", subtext "One Wedded Advisor confirms the inclusions in writing before you commit.", primary UTM link), and the FAQ (5 pairs).
5. Categories Destination Weddings, Costa Rica, Latin America & Caribbean, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
6. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
7. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
8. Preview desktop and mobile; check links, the CTA and the breadcrumb (Home > Destination Weddings > post).
9. After publishing: add links to this post from the Seychelles, Mauritius and Hawaii posts' "Venues and planning" once all are live.

## Mismatches and open points

- Field map not confirmed and no browser, so no CMS labels could be compared with the package.
- `/destination-weddings` and Destination Weddings must exist in the CMS; confirm before saving.
- The Seychelles (`/destination-weddings/getting-married-in-seychelles`), Mauritius (`/destination-weddings/mauritius-wedding`) and Hawaii (`/destination-weddings/getting-married-in-hawaii`) sister links are drafts, not live: publish together or remove.
- `/destinations/latin-america-caribbean` is on the do-not-link list and is not linked here.
- Brief tag `Getting Married in {Country}` kept as given; rename in the CMS if a literal `{Country}` tag is not wanted.
- Planner SME to reconfirm the TSE (Registro Civil and online marriage declaration) pages, the Ministry of Foreign Affairs authentications service and Smartraveller live before publishing.
