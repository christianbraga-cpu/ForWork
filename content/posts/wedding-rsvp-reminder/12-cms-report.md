# Stage 12 CMS report: wedding-rsvp-reminder

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser tool in this cloud session, so the CMS was not opened. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/wedding-rsvp-reminder/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-rsvp-reminder/11-body.md` (08-final.md wording unchanged, checked by diff; front matter, META comments, H1 and 5 fact markers removed; 4 IMAGE SLOT comments kept; 4 UTM links kept; no `[[VERIFY]]` markers; no `<!-- CTA: primary -->` marker existed, the CTAs are already inline)
- `content/posts/wedding-rsvp-reminder/booking-checklist.md` (reminder schedule template relative to the reply date and the venue and caterer final-numbers date, channel checklist per guest, privacy checklist)
- H1/title: Wedding RSVP Reminder Wording and When to Send It (49 chars)
- Slug: wedding-rsvp-reminder
- URL: https://weddedwonderland.com/expert-advice/wedding-rsvp-reminder
- Type: New (not a refresh, no redirect). Cluster: Wedding RSVP Website
- Categories: Expert Advice (primary, set explicitly), Planning Guides, Destination Weddings. Confirm "Planning Guides" and "Destination Weddings" exist as CMS categories.
- Tags: RSVP, wedding invitations, guest list, wedding wording, destination wedding planning
- Author/byline: Wedded Wonderland
- Meta title: Wedding RSVP Reminder Wording and When to Send It (49 chars)
- Meta description (verbatim from 02-seo.json, 150 chars): How and when to send a wedding RSVP reminder, with polite wording for texts, emails, cards and calls, and what to say once your reply date has passed.
- Focus keyword: wedding rsvp reminder. Canonical: the URL above. OG image: featured slot.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs (09-cro.json, already inline): Wedded Concierge primary (H2 "Who to remind and how to reach them"), secondary (H2 "Reminding guests for a destination wedding"), closing (final H2); magazine link (H2 "Keep one list so you only remind the right guests"). All utm_medium=content.
- Privacy line: "General information as at November 2026, not legal advice" sits in the H2 "Who to remind and how to reach them" with the OAIC links at the claim; keep it in place.

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
- [ ] After save, URL is exactly https://weddedwonderland.com/expert-advice/wedding-rsvp-reminder: not checked. The category bug has moved earlier posts, including /wedding-rsvp-website, so check this and the breadcrumb (Home > Expert Advice > post) after saving.
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` is empty

## Images
All 4 slots are `needed`. Place them by the IMAGE SLOT comments in `11-body.md`, not the provisional `after_h2` numbers in `04-images.json`:
- `featured`: featured and OG image (comment after the intro). Still life, placeholder names only. Licensed or own shoot; AI only with Nic's written approval, captioned "Illustrative image".
- `phone-reminder-message`: end of the H2 "Wedding RSVP reminder text message wording". Licensed phone photo with a plain, unbranded message and sample names; not presented as a Wonderland Studio screen. No third-party app screens. Never AI.
- `destination-welcome`: end of the H2 "Reminding guests for a destination wedding". Real partner venue, verified and named in the caption. Never AI.
- `couple-guest-list`: end of the H2 "Keep one list so you only remind the right guests". Licensed or own shoot with model release or consent; no third-party app screens. Never AI.

Do not publish with `[[IMAGE NEEDED]]` captions. Pinterest pins and the carousel in 10-distribution.json are on hold until these are approved.

## Before publish
- [[VERIFY]] in the body: none.
- [[VERIFY]] image licences and credits for all 4 slots.
- [[VERIFY]] The body links the RSVP website guide at /expert-advice/wedding-rsvp-website (200 on 2026-11-24). That path exists because the category bug moved the post from /wedding-rsvp-website. Confirm the URL the team keeps and update that one link, or confirm a 301, before publish.
- No prices, so nothing for Nic's price sign-off. Nic to confirm the three Wedded Concierge lines and the magazine link, and to decide on the featured image (licensed, or AI with written approval).
- Nothing implies the Wedded Advisor chases guests, sends reminders or handles RSVPs (checked in body, package and booking checklist).
- Set datePublished at publish.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-rsvp-reminder`.
- Phone slot brief: `04-images.json` asks for a Wonderland Studio screenshot; the newer body IMAGE SLOT comment (after the editor round) asks for a plain unbranded message, not presented as a Studio screen. The package follows the body. The planned file name in 04-images still contains "studio"; rename when the image is sourced.
- `02-seo.json` lists the anchor "Wonderland Studio's free RSVP and guest list tools"; the body uses "Wonderland Studio is our planning app for seating charts and RSVPs" (no "free"), which matches the brief. No change needed.
