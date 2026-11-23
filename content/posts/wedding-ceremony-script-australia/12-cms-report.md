# Stage 12 CMS report: wedding-ceremony-script-australia

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser tool in this cloud session, so the CMS was not opened. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/wedding-ceremony-script-australia/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-ceremony-script-australia/11-body.md` (08-final.md wording unchanged, checked by diff; front matter, META TITLE comment and fact markers removed; 4 IMAGE SLOT comments kept; 4 UTM links kept; no `[[VERIFY]]` markers; no `<!-- CTA: primary -->` marker existed, the CTAs are already inline)
- `content/posts/wedding-ceremony-script-australia/booking-checklist.md` (legal steps on the day, questions to ask your celebrant)
- H1/title: Australian Wedding Ceremony Script With the Legal Wording
- Slug: wedding-ceremony-script-australia
- URL: https://weddedwonderland.com/expert-advice/wedding-ceremony-script-australia
- Type: New (not a refresh, no redirect). Cluster: Wedding Ceremony Script
- Categories: Expert Advice (primary, set explicitly), Ceremony, Planning. Confirm "Ceremony" and "Planning" exist as CMS categories.
- Author/byline: Wedded Wonderland
- Meta title: Wedding Ceremony Script Australia With the Legal Wording (56 chars)
- Meta description (verbatim from 02-seo.json, 153 chars): Read an Australian wedding ceremony script with the exact monitum and legal vow wording from the Marriage Act, and what your celebrant must say and sign.
- Focus keyword: wedding ceremony script australia. Canonical: the URL above. OG image: featured slot.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs (09-cro.json, already inline): Wedded Concierge primary (after "A short legal script"), secondary (overseas H2), closing (final H2); magazine link (vows H2). All utm_medium=content.
- Legal disclaimer: "General information as at November 2026, not legal advice." sits under each legal H2 and the FAQ in the body; keep it in place.

## Checklist (publish-checklist.md)
- [ ] Field map CONFIRMED: no, NOT YET MAPPED
- [x] 11-publish-package.json validates; primary_category == categories[0] (Expert Advice)
- [ ] Images prepared: no, all 4 slots `needed`
- [ ] Logged into the CMS: not applicable, no browser this session
- [ ] Images uploaded with alt and caption: not done
- [ ] Featured image: not done
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA block: in package, not entered (already inline; do not add a second copy)
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly to Expert Advice: in package, not entered; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] After save, URL is exactly https://weddedwonderland.com/expert-advice/wedding-ceremony-script-australia: not checked. The category bug has moved earlier posts, so check this and the breadcrumb (Home > Expert Advice > post) after saving.
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` is empty

## Images
All 4 slots are `needed`: licensed photos of real Australian ceremonies with signed releases for every identifiable person (celebrant, couple, witnesses). Never AI. Place them by the IMAGE SLOT comments in `11-body.md`, not the provisional `after_h2` numbers in `04-images.json`:
- `featured`: featured and OG image (comment at the top of the body)
- `script-folder`: under the H2 "What the law requires in an Australian wedding ceremony"
- `ring-exchange`: under the H2 "What the celebrant has to say legally, and what they can change"
- `signing`: under the H2 "Witnesses, the signing and the paperwork on the day" (no legible documents, crests or certificate numbers)

Do not publish with `[[IMAGE NEEDED]]` captions. Pinterest pins in 10-distribution.json are on hold until these are approved.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so nothing for Nic's price sign-off. Nic to confirm the three Wedded Concierge lines and the magazine link.
- Licensed images with releases for all 4 slots.
- Nothing implies the Wedded Advisor handles legal paperwork (checked).
- Set datePublished at publish.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-ceremony-script-australia`.
