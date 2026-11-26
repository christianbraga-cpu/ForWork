# CMS report: marriage-licence

**Draft URL / ID:** Not uploaded. Package-only mode: the person uploads via the Word doc, and `content-system/cms/field-map.md` is still NOT YET MAPPED. Nothing was saved, scheduled or published in the CMS. Status is Draft only; a human clicks Publish.

- Date: 2026-11-26
- Title and H1: How Do You Get a Marriage Licence?
- Meta title: Marriage Licence in Australia and How It Works Overseas (55 characters)
- Meta description (from `02-seo.json`, 146 characters): Marriage licence rules for Australian couples, why a notice of intended marriage takes its place, and how licences work in New Zealand and Hawaii.
- Focus keyword: marriage licence
- Target URL: https://weddedwonderland.com/expert-advice/marriage-licence (slug `marriage-licence`; canonical set to this URL)
- Primary category: Expert Advice (= categories[0]); then Destination Weddings, Planning Guides
- Tags: Wedding Paperwork, Marriage Licence, Notice of Intended Marriage, Legal Requirements, Marrying Overseas
- Package: `content/posts/marriage-licence/11-publish-package.json` (status `draft`, validates clean)
- Body: `content/posts/marriage-licence/11-body.md`
- Booking checklist: `content/posts/marriage-licence/booking-checklist.md`
- Redirect: none (new article)

## Before publishing (a person)

1. **Re-read the govt.nz marriage licence page and the Hawaii State Department of Health marriage licence page** (last read 17 and 16 November 2026) and confirm the New Zealand and Hawaii paragraphs still match.
2. **Check the saved URL is exactly `/expert-advice/marriage-licence`** (slug `marriage-licence`, under Expert Advice).
3. **Legal content is general information as at November 2026**, not legal advice. The post says so in the intro; keep that line.
4. Source and approve all 4 images (none approved yet) and clear every item in the draft note.

## Package build (Part 1)

- [x] Body built from `08-final.md`: front matter and META comments removed (they live in the SEO fields), H1 is the title, all `<!-- fact_xx -->` markers removed, 4 image-slot comments kept, no `[[VERIFY]]` markers in the copy
- [x] **No CTA marker comments added.** 08-final.md has no `<!-- CTA: primary -->` marker, so nothing was replaced; the primary, secondary, closing and magnet links stay as the existing inline links per `09-cro.json`
- [x] Every link and UTM identical to 08-final.md (33 links, same order, checked by script); internal links relative
- [x] Key takeaways: the 4 bullets in the body, verbatim; FAQ: 6 pairs from the body
- [x] Categories and tags from the brief; primary_category = Expert Advice
- [x] schema_jsonld: Article (headline, description, author and publisher Wedded Wonderland, datePublished empty) + BreadcrumbList (Home > Expert Advice > post) + FAQPage (6; links stripped to plain text in JSON-LD only)
- [x] No prices or fees; `needs_signoff` empty, nothing for Nic to sign off
- [x] Images: 4 slots, all `needed`
- [x] draft_note: "DRAFT. Do not publish until checked:" + govt.nz and Hawaii DOH recheck, image licence and consent checks, no Nic sign-off, the 4 needed slots, URL check, general information as at November 2026, "A human clicks Publish"
- [x] No em dashes; Australian English
- [x] `python3 -I content-system/scripts/validate.py content/posts/marriage-licence`: All valid

## CTAs (unchanged, from 09-cro.json)

| Role | Button text | Link | Where |
|---|---|---|---|
| Primary | Begin with Wedded Concierge | `/wonderland-concierge?utm_source=blog&utm_medium=content&utm_campaign=marriage-licence&utm_content=primary` | End of "Marry at home and celebrate abroad" |
| Secondary | Plan with Wedded Concierge | `...&utm_content=secondary` | End of "Marry legally in your destination" |
| Closing | Tell Wedded Concierge your date | `...&utm_content=closing` | Final paragraph |
| Magnet | Get Wedded destination wedding magazines | `/magazine?...&utm_content=magnet` | End of "Recognition back in Australia" |

## Images (all needed, none approved)

| Slot | Role | AI allowed? |
|---|---|---|
| featured | featured, OG image | Only if the person approves; caption "Illustrative image" |
| signing-register-celebrant | inline | Never: real couple and celebrant, written consent |
| certificate-still-life | inline | Only if the person approves; caption "Illustrative image" |
| destination-ceremony | inline | Never: real New Zealand or Hawaii ceremony, licensed, location proven |

No legible certificate, register, crest, passport data page or personal details in any image. No alt text or captions exist in `04-images.json`; they were left empty, not invented.

## CMS checklist (Part 2: not run)

- [ ] `cms/field-map.md` status is CONFIRMED (it is NOT YET MAPPED)
- [x] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] Approved images prepared (0 of 4)
- [ ] The person is logged into the CMS (not applicable: package-only mode)

Upload: not started. After save: not started.

## Screenshots

None. Nothing was uploaded, so there is no preview to capture.

## What to do in the CMS (the person)

1. Upload the approved images with alt text and captions; set the featured image.
2. Title and H1 "How Do You Get a Marriage Licence?", slug `marriage-licence`, excerpt from the package, author (byline to confirm; package uses "Wedded Wonderland").
3. Paste the body; fill the Key Takeaways block (4 bullets) and FAQ (6 pairs). Keep links and UTMs as they are.
4. Categories Expert Advice, Destination Weddings, Planning Guides, then **set Expert Advice as the primary category explicitly**; add tags.
5. SEO fields: meta title, meta description, focus keyword, canonical; schema JSON-LD if the CMS has a field.
6. Paste the draft note into the internal note field, then **Save Draft**. Never Publish or Schedule from the pipeline.
7. Preview desktop and mobile; check the URL is `/expert-advice/marriage-licence`, every link resolves, CTAs show and the breadcrumb reads Home > Expert Advice.

## Internal links

All 8 internal targets are live per the link map (checked 2026-11-16 to 2026-11-26): the Notice of Intended Marriage step by step guide, who can perform a marriage, name change after marriage, get married in New Zealand, getting married in Hawaii, symbolic ceremony, where you can legally get married abroad, plus /magazine and /wonderland-concierge.

## Mismatches and open points

- Field map not mapped, so no CMS labels could be compared with the package.
- `10-distribution.json` (Pinterest pin 1 and two Instagram carousel slides) says the celebrant submits to the registry in "your state or territory"; the final article was corrected to "the state or territory where you married". Align the social copy before posting. Not changed here.
- Author: no named author in the inputs.
- Content type "Guide (legal)" is not a schema value; `planning_guide` from the brief used.
- AI still lifes for featured and certificate-still-life await the person's approval.
