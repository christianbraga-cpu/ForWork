# CMS report: 5-tips-to-creating-a-personalised-wedding-hashtag

## URL-move warning (read first)

**Changing the primary category from Style to Wedding Tools has moved earlier posts. After Save Draft, check the saved URL is exactly https://weddedwonderland.com/5-tips-to-creating-a-personalised-wedding-hashtag. If it moved, do not publish.**

The slug `5-tips-to-creating-a-personalised-wedding-hashtag` is **do not change**. Refresh in place: URL kept, no redirect.

## Result: not uploaded, package only

- Draft URL/ID: not uploaded.
- Reason 1: package-only run as instructed. The person uploads via the Word doc. No browser was used and no login was attempted.
- Reason 2: `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`, not `CONFIRMED`.
- Nothing was saved, published or scheduled in the CMS. Status: Draft only. A human clicks Publish.

## What changes

| Field | Value |
|---|---|
| Title (old, for the record) | 5 Tips to Creating a Personalised Wedding Hashtag |
| Title and H1 (new) | Wedding Hashtag Generator Ideas and How to Make Your Own (56 characters) |
| Meta title | Wedding Hashtag Generator Ideas and How to Make Your Own |
| Meta description | Wedding hashtag generator ideas by style, plus how to make your own from your names, date and destination, test it, and share it with your guests. (146 characters, from 02-seo.json) |
| URL | https://weddedwonderland.com/5-tips-to-creating-a-personalised-wedding-hashtag (kept) |
| Slug | 5-tips-to-creating-a-personalised-wedding-hashtag (do not change; no redirect) |
| Canonical | https://weddedwonderland.com/5-tips-to-creating-a-personalised-wedding-hashtag |
| Focus keyword | wedding hashtag generator |
| Categories (in order) | Wedding Tools, Planning, Style |
| Primary category | Wedding Tools, set explicitly (the live post is currently under Style) |
| Categories to remove | Stationery, Theming |
| Tags | wedding hashtag, wedding hashtag ideas, personalised wedding, wedding weekend, guest photos, wedding planning |
| Tags to remove | couples, hashtag, MODERN WEDDING |
| Author/byline | Wedded Wonderland |
| Status | Draft only |

## Remove from the old post

The new body (`11-body.md`) replaces all old content. Remove:
- The two embedded third-party Instagram posts.
- The photo booth supplier link.
- The celebrity couple reference and the celebrity hashtag anecdote.
- Every old example tag.
- The old "You may also like" links to 2017 era posts.
- Any old images, including the old featured image, unless their licence is confirmed.

## Steps for the web team

1. Log into the CMS yourself and open the existing post (edit it, do not create a new one).
2. Do not touch the slug field.
3. Replace the body with `content/posts/5-tips-to-creating-a-personalised-wedding-hashtag/11-body.md` (or the Word doc). The title field supplies the H1, so the body has no H1. Replace title, excerpt, key takeaways (4), FAQ (7), tags, meta title, meta description and schema from `11-publish-package.json`.
4. The CTAs and the magazine link are already inline links in the body with their UTMs. Do not add CTA copies or marker comments, and do not change any link.
5. Remove the old embeds, supplier link, old tags and old images listed above.
6. Categories in this order: Wedding Tools, Planning, Style. Then set the primary category explicitly to Wedding Tools. Remove Stationery and Theming.
7. Paste the `draft_note` from the package into the internal note field.
8. Save Draft only. Never Publish or Schedule.
9. **Check the saved URL is exactly https://weddedwonderland.com/5-tips-to-creating-a-personalised-wedding-hashtag. If it moved, do not publish.**
10. Preview on desktop and mobile: images, links, CTAs, and the breadcrumb (Home > Wedding Tools > post, with Wedding Tools linking to /blog/wedding-tools; /wedding-tools itself is 404).

## Checklist (publish-checklist.md)

- [ ] Field map CONFIRMED: no (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0] (Wedding Tools)
- [ ] Images prepared with alt and caption: not done, all 4 slots `needed`
- [ ] Logged into CMS: not checked (package-only run)
- [ ] Images uploaded first: not done
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body with inline images: in package, not entered
- [ ] Key Takeaways block: in package (4), not entered
- [ ] CTA blocks: inline in the body (primary, secondary, closing, magnet), not entered
- [ ] FAQ block: in package (7), not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` is empty

## Package files

- `content/posts/5-tips-to-creating-a-personalised-wedding-hashtag/11-body.md`: 08-final.md wording unchanged. Removed only the front matter, the two META comments, the H1 and the fact markers. 4 IMAGE SLOT comments kept. All 12 links and UTMs identical to 08-final.md; internal links relative. No [[VERIFY]] markers in the body. No CTA marker comments.
- `content/posts/5-tips-to-creating-a-personalised-wedding-hashtag/11-publish-package.json`: stage 11, status draft, validates.
- `content/posts/5-tips-to-creating-a-personalised-wedding-hashtag/booking-checklist.md`: hashtag worksheet, questions and blanks only. Not linked from the post (no page on the site).

## Images

All 4 slots are `needed`. Place them by the IMAGE SLOT comments in `11-body.md`:
- `featured`: featured image and OG image (top of the body).
- `stationery-flatlay`: under the H2 "How to make your own wedding hashtag".
- `guests-phones`: under the H3 "Hashtags for a wedding weekend".
- `welcome-sign`: under the H2 "Using your wedding hashtag well".

Licensed photos only. No AI for real weddings. Placeholder hashtag only, no app screens, logos or brands. The stationery flat lay may be AI only with Nic's written approval, captioned "Illustrative image". guests-phones and welcome-sign are never AI. Alt text is drafted from the shot briefs; rewrite it to match the final images. Do not publish with `[[IMAGE NEEDED]]` or `[[VERIFY credit]]` captions.

## Open items before publish

- [[VERIFY licence]] every image used, with consent for identifiable people; [[VERIFY credit]] credit and place for each caption.
- [[VERIFY: search the placeholder hashtag #SamAndAlexRivera2027 before it is printed or edited into any image, so it is not a real couple's tag.]]
- [[VERIFY licence]] any old images on the live post; retire them unless confirmed.
- /expert-advice/chatgpt-vs-ai-wedding-planner is linked with a neutral anchor. Its own copy mentions a Wonderland Studio AI assistant; this post makes no such claim.
- Set datePublished at publish (empty in the schema).
- Distribution (10-distribution.json): social assets are on hold until images are licensed, and the caption's live example tags should be searched before posting.

## Flags for Nic

- No prices in the post, so nothing for price sign-off. Please confirm the Wedded Concierge lines (primary, secondary, closing) and the magazine link.
- Approve or decline in writing an AI illustrative image for the stationery-flatlay slot only.
- Product decision, not blocking: whether to build a real on-site hashtag generator. The post makes no tool claim.

## Legal note

The privacy points (eSafety Commissioner, OAIC and the Privacy Act 1988) and the Instagram hashtag rules are general information as at November 2026, not legal advice. The body says so and links the official sources at each claim.

## Mismatches

None checked on screen: package-only run, and the field map is not confirmed.
