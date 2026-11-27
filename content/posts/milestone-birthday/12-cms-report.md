# Stage 12 CMS report: milestone-birthday

**Draft URL/ID:** not uploaded. Package only, as instructed: this cloud session has no browser, so no browser was opened and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. Never publish; a human clicks Publish.

## Package
- `content/posts/milestone-birthday/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/milestone-birthday/11-body.md` (08-final.md wording unchanged; front matter and 15 fact markers removed; H1, the 2 META comments and 5 IMAGE SLOT comments kept; no CTA marker comments added; all links exactly as in 08-final.md, including the 4 UTM links; internal links relative; no [[VERIFY]] markers)
- `content/posts/milestone-birthday/booking-checklist.md` (celebration planning checklist, questions only: guest of honour, guest list, home or destination, venue, local council, accommodation, guest travel, hosting for someone else; no claims, no prices)
- H1 and title: Milestone Birthday Celebration Ideas and How to Plan One
- Slug: milestone-birthday. URL: /celebration-ideas/milestone-birthday (canonical https://weddedwonderland.com/celebration-ideas/milestone-birthday)
- Type: New (not a refresh, no redirect). Cluster: Milestone Celebrations
- Categories: Celebration Ideas (primary), Planning Guides
- Tags: Milestone Birthdays, Birthday Celebration Ideas, 30th Birthday, 40th Birthday, 50th Birthday, 60th Birthday, Destination Celebrations, Wedded Concierge
- Author/byline: Wedded Wonderland
- Meta title: Milestone Birthday Celebration Ideas and How to Plan One (same as the title)
- Meta description: Milestone birthday celebration ideas and planning advice for a party at home or a destination weekend, from the guest list to the timeline. (the 08-final.md version, without "budget"; 02-seo.json still carries the older wording with "budget")
- Focus keyword: milestone birthday. OG image: featured slot.
- Excerpt: Milestone birthday celebration ideas by style and by decade, a party at home weighed against a destination weekend, and a step by step plan and timeline, from the guest list and venue questions to looking after travelling guests and hosting for someone else. (258 chars, no figures)
- Key takeaways: 4. FAQ: 5 pairs. Schema: Article, BreadcrumbList (Home > Celebration Ideas > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body, once each, relative links):
  - primary: Wedded Concierge, end of "Hand over the logistics" (`utm_content=primary`)
  - lead magnet: destination magazines, "Choosing a place guests can reach" (`utm_content=magnet`)
  - secondary: Wedded Concierge, end of "Where everyone stays and one hosted dinner" (`utm_content=secondary`)
  - closing: Wedded Concierge, final paragraph (`utm_content=closing`)
  - All `utm_source=blog&utm_medium=content&utm_campaign=milestone-birthday`.
- Prices or figures: none, so nothing needs Nic's price sign-off.

## Checklist (publish-checklist.md)
- [x] `11-publish-package.json` validates; primary_category equals categories[0]
- [ ] field-map.md CONFIRMED: no (NOT YET MAPPED); not needed for a package-only run
- [ ] Images uploaded with alt and caption: not done, all 5 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA blocks: in package (already inline in the body), not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly to Celebration Ideas: in package; method unknown until the field map is confirmed, and the category itself is not yet confirmed to exist in the CMS
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done (no browser in this session)
- [ ] Preview screenshots (desktop, mobile): none taken

## Images
- Place images by the IMAGE SLOT comments in `11-body.md`; each slot's shot brief is in the comment and in the package `images` list:
  - `featured`: featured image (comment under the H1)
  - `toast-moment`: under the H2 "Milestone birthday celebration ideas by style"
  - `dessert-table`: under the H2 "Matching the celebration to the milestone"
  - `planning-flat-lay`: under the H2 "How to plan a milestone birthday step by step"
  - `destination-weekend`: under the H2 "Planning a destination birthday weekend"
- All 5 slots are `needed`; no files exist yet. Licensed photos only; never AI for a real place or real people (featured, toast-moment, destination-weekend). The two still lifes (dessert-table, planning-flat-lay; no people, no real place) may use AI only with approval, captioned "Illustrative image".
- Do not publish with `[[IMAGE NEEDED]]` captions or `[[VERIFY credit]]` credits. Social visuals in 10-distribution.json are on hold until these are licensed for social use too.

## Before publish
- **Confirm the "Celebration Ideas" category exists in the CMS** and set it as the primary category explicitly, so the URL and breadcrumb read Celebration Ideas.
- **URL-move warning: after saving, check the URL is exactly /celebration-ideas/milestone-birthday** (category path and slug). If the CMS has moved it (a default path, another category, or a slug with a suffix such as `-2`), do not publish; fix it first.
- **[[VERIFY]]: none in the body.** Responsible service of alcohol and council permits for a park or beach could not be sourced, so the post states no rule: both appear only as questions (to the venue and the local council) in the body and in `booking-checklist.md`.
- Nic to approve the Wedded Concierge lines (primary, secondary, closing) and the magazine link. No price sign-off needed.
- Licensed images for all 5 slots.
- The body starts with the two META comments and the H1. If the CMS renders the title field as the H1, delete the body H1 line so the page has one H1; the META comments are reference only (the values go in the SEO fields).
- Travel and safety lines (Smartraveller, travel insurance, Cancer Council SunSmart, SA MFS candles, US Department of State checklist) are general information as at November 2026. Recheck if the post is published much later.
- Set datePublished at publish.

## After publish
- **Cannibalisation:** `/celebration-ideas/milestone-birthday-by-decade` is live and owns the decade idea lists (HIGH in 02-seo.json). This post links to it once. Add the backlinks in 02-seo.json `backlinks_to_add` (from milestone-birthday-by-decade, `/travel-guides/experiences-by-occasion` and `/trending/inside-bella-hadids-30th-birthday-weekend-at-blackberry-farm`) and watch both milestone URLs in GSC.

## Mismatches
- None checked on screen: package-only run, and the CMS field map is still not mapped. To upload through the browser later, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=milestone-birthday`.
