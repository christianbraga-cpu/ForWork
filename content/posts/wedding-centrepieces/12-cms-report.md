# CMS report: wedding-centrepieces

**Result: not uploaded. Package only.**

- Draft URL/ID: not uploaded.
- Reason 1: package-only run as instructed (no browser used, no upload or login attempted).
- Reason 2: `content-system/cms/field-map.md` is `Status: NOT YET MAPPED`, not `CONFIRMED`.
- Nothing was saved, published or scheduled in the CMS.

## URL check (read before and after saving)

**The category bug has recently moved three saved posts (table settings, flowers hub, seating charts) into category paths. This is a new post and its intended URL already includes /style-advice/. After saving the draft, check the URL is exactly https://weddedwonderland.com/style-advice/wedding-centrepieces (slug `wedding-centrepieces`, no doubled or different category segment). If it differs, do not publish; report it to the web team.**

## Anchor check

The intro link "Skip to the 30 ideas" points to `#30-centrepiece-ideas-by-style`. The CMS must generate the id `30-centrepiece-ideas-by-style` on the H2 "30 centrepiece ideas by style". Check in preview that the link jumps there. If the CMS does not generate heading anchors, or generates a different id, remove the "Skip to the 30 ideas" link (or add the id by hand if the editor allows it).

## Fields

| Field | Value |
|---|---|
| Post type | New post |
| Title | 30 Wedding Centrepieces That Make the Table (43 characters) |
| Slug | wedding-centrepieces |
| URL / canonical | https://weddedwonderland.com/style-advice/wedding-centrepieces |
| Meta title | Wedding Centrepieces, 30 Ideas That Make the Table (50 characters, keyword first) |
| Meta description | Wedding centrepieces by style, from low garden runs and tall statement pieces to candlelit and non floral tables, plus how to choose for your room. (147 characters, from 02-seo.json, no figures) |
| Focus keyword | wedding centrepieces |
| Categories (in order) | Style Advice, Wedding Table Decor, Wedding Flowers, Destination Weddings |
| Primary category | Style Advice (set explicitly) |
| Tags | wedding centrepieces, wedding table decor, wedding flowers, reception styling, destination weddings, candles, table styling |
| Author | Wedded Wonderland |
| OG image | featured slot |
| Schema | Article (datePublished empty), BreadcrumbList (Home > Style Advice > post), FAQPage (6 questions) |
| Status | Draft only. A human publishes. |

The three secondary category names come from `01-brief.json` and are assumed; match them to real CMS categories before saving.

## Steps for the web team

1. Log into the CMS yourself and create a new post.
2. Upload images only once licensed photos are supplied (none yet; see below). Alt text is in the package.
3. Title, slug `wedding-centrepieces`, excerpt and author from `content/posts/wedding-centrepieces/11-publish-package.json`.
4. Body from `content/posts/wedding-centrepieces/11-body.md`. The CTAs (primary, secondary, closing) and the magazine link are already inline links in the body; do not add copies.
5. Key Takeaways (4) and FAQ (6) from the package.
6. Categories in this order: Style Advice, Wedding Table Decor, Wedding Flowers, Destination Weddings; then set the primary category explicitly to Style Advice.
7. Tags, SEO fields, schema (if the CMS has a field).
8. Paste the `draft_note` from the package into the internal note field.
9. Save Draft only. Never Publish or Schedule.
10. Immediately check the URL is exactly https://weddedwonderland.com/style-advice/wedding-centrepieces.
11. Preview desktop and mobile: images, links, CTAs, the skip-link anchor, breadcrumb (Home > Style Advice > post).

## Open items before publishing

- Prices: none in the post, so nothing for Nic's price sign-off.
- [[VERIFY]] markers in the body: none.
- Images: 5 slots needed, none sourced: featured, low-florals, tall-centrepiece, candlelit-long-table, non-floral-destination. Licensed images only; never AI for real people, venues, destinations or weddings. No alt text or caption may claim a flower is in season (current alt texts do not). Do not publish with `[[IMAGE NEEDED]]` or `[[VERIFY credit]]` captions.
- Image checks: licence scope and releases, credit wording (no vendor names), verified venue and town in each caption.
- Internal links to the flowers hub and seating charts post use the paths they moved to after the category bug (/style-advice/fashionable-flowers-opt-for-in-season-or-order-imported and /expert-advice/our-favourite-interactive-seating-charts). Check in preview that every internal link resolves without a redirect chain, and recheck if the dev fix moves them back.
- `datePublished` in the schema is empty; set at publish.
- Booking checklist (`booking-checklist.md`) is built but has no page on the site yet; it is not linked from the post. Its "Full guide" link only works once this post is published.

## Checklist

- [x] 11-body.md built (front matter and fact markers removed; no CTA marker present; 5 image slot comments kept)
- [x] 11-publish-package.json built and validated
- [x] booking-checklist.md built
- [ ] Images uploaded (none sourced)
- [ ] Fields entered in CMS (not uploaded)
- [ ] Primary category set (not uploaded)
- [ ] Save Draft (not done)
- [ ] URL checked after save (not done)
- [ ] Anchor checked in preview (not done)
- [ ] Preview screenshots (none: no browser)

## Mismatches

None observed: CMS not opened.
