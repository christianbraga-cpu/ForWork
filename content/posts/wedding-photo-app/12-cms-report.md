# Stage 12 CMS report: wedding-photo-app

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser was opened, no login was attempted and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/wedding-photo-app/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-photo-app/11-body.md` (08-final.md wording unchanged; front matter and 21 fact markers removed; 4 IMAGE SLOT comments kept; inline links and UTMs kept; no [[VERIFY]] markers in the body)
- `content/posts/wedding-photo-app/booking-checklist.md` (photo app set-up checklist, questions for the venue and the photographer; names no apps; Wedded Concierge link without UTM parameters)
- Title: Wedding Photo App Guide for Collecting Guest Photos (51 chars; the user's choice, replacing "Best Wedding Photo Sharing Apps for Your Guests")
- Slug: wedding-photo-app. URL: https://weddedwonderland.com/wedding-tools/wedding-photo-app
- Type: New (not a refresh, no redirect). Cluster: Wedding Planning App
- Categories: Wedding Tools (primary, set explicitly), Wedding Photography, Planning Guides
- Tags: wedding photo app, guest photos, wedding photo sharing, QR code wedding, unplugged ceremony, destination wedding planning
- Author/byline: Wedded Wonderland
- Meta title: Wedding Photo App Guide for Collecting Guest Photos (51 chars, same as the title)
- Meta description: How a wedding photo app gathers guest photos in one private album, what to check on privacy and copyright, and how to set it up for a destination wedding. (154 chars, no figures.) The 02-seo.json version was 156 chars, over the 155 limit, so "gallery" became "album" (the body's own word); nothing else changed.
- Excerpt: 226 chars, no figures, drawn from the intro and section headings.
- Focus keyword: wedding photo app. Canonical: the URL above. OG image: featured slot.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Wedding Tools > post, with Wedding Tools pointing to https://weddedwonderland.com/blog/wedding-tools), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body; 08-final.md has no `<!-- CTA: primary -->` marker): secondary Wedded Concierge link (end of the set-up steps), primary Wedded Concierge link (end of "Guest photos at a destination wedding"), closing Wedded Concierge link and magazine link (closing paragraph). All utm_campaign=wedding-photo-app, utm_medium=content.
- No prices anywhere in the post.

## Checklist (publish-checklist.md)
- [ ] Field map CONFIRMED: no (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0] (Wedding Tools)
- [ ] Images prepared with alt and caption: not done, all 4 slots `needed`
- [ ] Logged into CMS: not checked (package-only run)
- [ ] Images uploaded first: not done
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body with inline images: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA blocks: in package (inline), not entered
- [ ] FAQ block: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` holds nothing from this run

## Categories, URL and the CMS category bug
- Primary category Wedding Tools must be set explicitly with the field-map method, not left to list order.
- `/wedding-tools` itself returns 404. The section listing is `/blog/wedding-tools`, so the breadcrumb's Wedding Tools item links there. Check the on-page breadcrumb in preview points to `/blog/wedding-tools`, not `/wedding-tools`.
- Secondary categories Wedding Photography and Planning Guides come from 01-brief.json and are **not confirmed** against the live CMS category list. Neither has a `/blog/` listing in link-map.csv (the nearest live listings are Wedding Planning at `/blog/wedding-planning` and Destination Weddings at `/blog/destination-weddings`). Match them to existing CMS categories; do not create new ones.
- Known CMS bug: recently saved posts have been moved by the category bug. After Save Draft (and again at publish), check the live URL is exactly `/wedding-tools/wedding-photo-app`.

## Images
Place images by the IMAGE SLOT comments in `11-body.md`, not the provisional `after_h2` numbers in `04-images.json`:
- `featured`: featured image and OG image (comment at the top of the body)
- `qr-card`: under the H3 "On the day, QR cards on tables and at the entrance"
- `couple-album`: under the H3 "After the wedding, download, back up and share"
- `destination-dusk`: under the H2 "Guest photos at a destination wedding"

All 4 slots are still `needed`. Licensed images only, with consent for every identifiable person; never AI for real people or places; no third-party app screens, logos or brands. The qr-card still life (no people, no real place, placeholder code) may be AI only if Nic approves in writing, captioned "Illustrative image". destination-dusk is never AI. Alt text is drafted from the shot briefs and must be rewritten to match the final images. Do not publish with `[[IMAGE NEEDED]]` captions.

## Flags for Nic
- **Wonderland Studio pricing is inconsistent across our own pages.** `/wonderland-studio` says free with no trial clock; `/expert-advice/best-wedding-planning-apps` and `/expert-advice/what-is-wonderland-studio` say 7-day trial then subscription. This post states no Studio pricing. Please settle the site wording.
- **Does Wonderland Studio have any guest photo feature?** The post says nothing either way and describes Studio only as our planning app for seating charts and RSVPs.
- No prices in the post, so nothing for price sign-off. Please confirm the Wedded Concierge lines (secondary, primary, closing) and the magazine link.
- Approve or decline in writing an AI illustrative still life for the qr-card slot only.

## Open items before publish
- [[VERIFY licence]] for every image used, and [[VERIFY credit]] for each caption.
- Confirm `/expert-advice/average-cost-wedding-photographer` resolves (linked twice in the body; 02-seo.json recorded it live on 2026-11-23, the editor asked for a recheck).
- booking-checklist.md has no page on the site, so it is not linked from the post (backlog suggestion only).
- Set datePublished at publish.
- Check the live URL is exactly `/wedding-tools/wedding-photo-app` (category bug).

## Legal note
The privacy and copyright points in the post and the checklist (eSafety Commissioner, OAIC and the Privacy Act 1988, Copyright Act 1968 s35) are general information as at November 2026, not legal advice. The body says so at the top of the privacy section and in the copyright FAQ answer, and links the official sources at each claim.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-photo-app`.
