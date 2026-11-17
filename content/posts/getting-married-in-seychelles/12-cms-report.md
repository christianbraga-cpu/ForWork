# CMS report: getting-married-in-seychelles

**Draft URL / ID:** Package ready, not uploaded: no browser in this session and the CMS field map is not confirmed; a human saves as Draft and clicks Publish. Nothing was saved, scheduled or published in the CMS.

- Date: 2026-11-17
- Title: How to Get Married in the Seychelles
- Series: third post in the "Getting Married in {Country}" series (after Hawaii and Mauritius); template `content-system/templates/getting-married-in-country.md`
- Package: `content/posts/getting-married-in-seychelles/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/getting-married-in-seychelles/11-body.md`
- Booking checklist: `content/posts/getting-married-in-seychelles/booking-checklist.md` (Seychelles civil marriage checklist: documents and steps in order, questions for the Civil Status office and the resort)
- Target URL: https://weddedwonderland.com/destination-weddings/getting-married-in-seychelles (CMS slug `getting-married-in-seychelles`)
- Primary category: Destination Weddings (= categories[0]); then Seychelles, Africa, Planning Guides; type planning_guide
- Tags: from the brief, as given
- New article, no redirect.
- **CMS setup needed first:** the `/destination-weddings` folder (URL path) and the **Destination Weddings** category must exist in the CMS before the draft is saved.
- **Mauritius and Hawaii sister links are drafts:** "Venues and planning for getting married in Seychelles" links to `/destination-weddings/mauritius-wedding` and `/destination-weddings/getting-married-in-hawaii`, neither live yet. Publish the posts together, or remove that sentence before publishing.

## Package build (Part 1)

- [x] `08-final.md` checked stable before building (modification time 02:39, size unchanged across checks); it already includes the final-check fixes, so it was built from as is
- [x] Body: front matter removed, H1 set to the title, all `<!-- fact_xx -->` markers removed, 6 image-slot comments kept, all links and the 4 UTM links unchanged (link list identical to `08-final.md`), no CTA marker comments, no `[[VERIFY]]` markers in the copy
- [x] Primary CTA: per 09-cro.json the existing "Speak with Wedded Concierge" link (utm_content=primary) in "Venues and planning for getting married in Seychelles" is the CTA, unchanged (no `<!-- CTA: primary -->` marker in 08-final.md)
- [x] Secondary, closing and magnet links unchanged; each utm_content appears exactly once in the body
- [x] No em dashes; Australian English; `scan_copy.py` on `11-body.md`: 0 banned, 0 flagged, 0 dashes, no overlaps
- [x] Key takeaways: exactly the 4 in the body, verbatim; FAQ (5) extracted from the body only
- [x] Categories and tags from the brief; primary_category = Destination Weddings
- [x] Meta title "How to Get Married in the Seychelles, Step by Step" (50 characters) and meta description (150 characters) from `02-seo.json`; no prices, no em dashes
- [x] schema_jsonld: Article (datePublished empty, author and publisher Wedded Wonderland) + BreadcrumbList (Home > Destination Weddings > post) + FAQPage (5)
- [x] Images: 6 slots (featured, documents, civil-ceremony, certificate-australia, when-to-marry, choose-your-island), all `needed`
- [x] verify_items and needs_signoff empty: no `[[VERIFY]]` markers, no price or fee amounts, nothing for Nic to sign off
- [x] Byline Wedded Wonderland
- [x] `python3 -I content-system/scripts/validate.py content/posts/getting-married-in-seychelles`: All valid

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (not confirmed)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 6; all `needed`)
- [ ] `/destination-weddings` folder and Destination Weddings category exist in the CMS (not checked; no browser)
- [ ] The person is logged into the CMS in the Chrome tab (no browser in this session)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (a person, or /wedded-blog resume=getting-married-in-seychelles once the field map is confirmed)

1. Create the `/destination-weddings` folder and the Destination Weddings category if they do not exist yet.
2. Source and upload the 6 images with alt text and captions; set the featured image. featured and civil-ceremony come from a licensed real wedding with written consent, never AI (Civil Status Officer identifiable only with written consent); when-to-marry and choose-your-island are real, named venues proven by media kit, register or EXIF, never AI; documents and certificate-australia are still lifes (Canva, licensed stock or own shoot; AI only with Wedded Wonderland approval, captioned "Illustrative image"). Seychelles Tourism Board media only if its licence covers third-party commercial blog use.
3. Enter title, slug `getting-married-in-seychelles`, excerpt and author ("Wedded Wonderland").
4. Paste the body from `11-body.md`; fill the Key Takeaways block (4 bullets), the CTA block if the template uses one (text "Speak with Wedded Concierge", subtext "One Wedded Advisor confirms the inclusions in writing before you commit.", primary UTM link), and the FAQ (5 pairs).
5. Categories Destination Weddings, Seychelles, Africa, Planning Guides, then set Destination Weddings as the primary category explicitly; add tags.
6. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
7. Paste the draft note into the internal note field, then **Save Draft**. Do not Publish or Schedule; a human clicks Publish.
8. Preview desktop and mobile; check links, the CTA and the breadcrumb (Home > Destination Weddings > post).
9. After publishing: add a link to this post from `/honeymoon-ideas/african-honeymoon` ("The Indian Ocean Islands"), and from the Mauritius and Hawaii posts' "Venues and planning" once all are live (from 02-seo.json).

## Mismatches and open points

- Field map not confirmed and no browser, so no CMS labels could be compared with the package.
- `/destination-weddings` and Destination Weddings must exist in the CMS; confirm before saving.
- The Mauritius (`/destination-weddings/mauritius-wedding`) and Hawaii (`/destination-weddings/getting-married-in-hawaii`) sister links are drafts, not live: publish together or remove.
- Brief tag `Getting Married in {Country}` kept as given; rename in the CMS if a literal `{Country}` tag is not wanted.
- `/destinations/africa` is on the do-not-link list and is not linked here (the Mauritius draft links it; flagged in its run report by SEO).
- Planner SME to reconfirm the Immigration and Civil Status Seychelles pages, the Australian High Commission (Port Louis) page and Smartraveller live before publishing; where ICS and the High Commission differ, ICS governs.
