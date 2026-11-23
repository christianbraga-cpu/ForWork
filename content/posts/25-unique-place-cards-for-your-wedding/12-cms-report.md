# CMS report: 25-unique-place-cards-for-your-wedding

**Result: not uploaded. Package only.**

- Draft URL/ID: not uploaded.
- Reason 1: package-only run as instructed (no browser used, no upload or login attempted).
- Reason 2: `content-system/cms/field-map.md` is `Status: NOT YET MAPPED`, not `CONFIRMED`.
- Nothing was saved, published or scheduled in the CMS.

## URL-move warning: primary category (read before saving)

**WARNING: the user set the primary category to Expert Advice. The live page's categories show Style first (Style, Stationery, Planning, Guests, Theming, DIY) and no Expert Advice. Changing the primary category may move the URL: the category bug has moved earlier refreshes (for example /our-favourite-interactive-seating-charts moved to /expert-advice/...).**

**After saving the draft, check the live URL is exactly https://weddedwonderland.com/25-unique-place-cards-for-your-wedding. If it moved, do not publish until a 301 is confirmed.**

## URL, slug and redirect

- URL https://weddedwonderland.com/25-unique-place-cards-for-your-wedding: **KEPT, do not change.**
- Slug `25-unique-place-cards-for-your-wedding`: **KEPT, do not change.** The "25" in the slug is accepted; the post now has 21 ideas.
- Redirect at publish (web team): **301** https://weddedwonderland.com/17-unconventional-yet-stunning-place-cards to https://weddedwonderland.com/25-unique-place-cards-for-your-wedding.

## What changes

| Field | Value |
|---|---|
| Title (old) | 25 Unique Place Cards For Your Wedding |
| Title (new) | Wedding Place Cards Ideas for Every Table (user's choice) |
| Meta title | Wedding Place Cards Ideas for Every Table (41 characters) |
| Meta description | Wedding place cards ideas for every table, from calligraphy and acrylic to keepsake stones and edible names, plus how to word, place and order them. (148 characters, from 02-seo.json, no figures) |
| Focus keyword | wedding place cards |
| Categories (in order) | Expert Advice, Stationery, Style, Planning |
| Primary category | Expert Advice (user's instruction; set explicitly) |
| Tags to add | place cards, wedding stationery, seating plan, escort cards, destination weddings, wedding planning |
| Tags to remove | stationary (misspelt) |
| Canonical | https://weddedwonderland.com/25-unique-place-cards-for-your-wedding |
| Breadcrumb | Home > Expert Advice > Wedding Place Cards Ideas for Every Table |
| Status | Draft only. A human publishes. |

Secondary categories Stationery, Style and Planning come from 01-brief.json and need matching to real CMS categories (live chips /blog/stationery, /blog/style, /blog/planning). The brief proposed Stationery as primary; the user's instruction (Expert Advice) is used.

## Remove from the old post

- All old images: the 25 body images on the 25 post (/api/images/cmii33..., listed in 04-images.json) and the 17 post's featured image (menu.png, 2019 screenshot). No licence on record.
- All image credits: Instagram handles, Etsy shops, photographers, stylists, publications.
- Embedded Instagram posts in the 17 post.
- Every outbound link to other publishers and shops (Camille Styles, Martha Stewart Weddings, Deer Pearl Flowers, Garden Pics and Tips, Something Turquoise, The Wishlist Gifts, Etsy, Instagram and others).
- The "Venues & Vendors to Explore" vendor box, if editable on this post. If it is a site template, leave it and report it.
- Old bylines: Ellen Kirkness, Alessandra Fasanella. The new byline is a human decision.
- Typos: "quests" (gone with the full body replacement) and the "stationary" tag.

The new body (`11-body.md`) replaces the old body in full and contains none of these.

## Steps for the web team

1. Log into the CMS yourself and open the existing post at /25-unique-place-cards-for-your-wedding (edit, do not create a new post).
2. Do not change the slug field.
3. Replace the body with `content/posts/25-unique-place-cards-for-your-wedding/11-body.md`; replace title, excerpt, key takeaways (4), FAQ (6), tags, meta title and description, and schema from `content/posts/25-unique-place-cards-for-your-wedding/11-publish-package.json`. The CTAs are already inline links in the body; do not add copies.
4. Remove the old images, credits, embeds, outbound links, vendor box (if editable), old bylines and the "stationary" tag.
5. Categories in this order: Expert Advice, Stationery, Style, Planning; then set the primary category explicitly to Expert Advice.
6. Paste the `draft_note` from the package into the internal note field.
7. Save Draft only. Never Publish or Schedule.
8. Immediately check the live URL is exactly /25-unique-place-cards-for-your-wedding. If it moved, do not publish until a 301 is confirmed.
9. Preview desktop and mobile: images, links, CTAs, breadcrumb (Home > Expert Advice > post).
10. At publish: add the 301 from /17-unconventional-yet-stunning-place-cards to the kept URL.

## Open items before publishing

- Prices: none in the post, so nothing for Nic's price sign-off.
- [[VERIFY]] markers in the body: none.
- Images: 5 slots needed, none sourced: featured, natural-edible, keepsake, glass-acrylic, destination-table. Licensed images only, no stationer branding. Slots featured, natural-edible, keepsake and glass-acrylic may be AI generic still lifes only if Nic approves, captioned "Illustrative image", with placeholder names. The destination-table slot is never AI. Do not publish with `[[IMAGE NEEDED]]` or `[[VERIFY credit]]` captions.
- Package verify items: licence and credit for every sourced photo; verified venue and town for the destination caption; old images retired; category names matched; live URL checked after save.
- Legal note: the allergen paragraph is general information as at November 2026, not legal advice (body sentence updated to say so).
- `datePublished` in the schema is empty; set at publish.
- Booking checklist (`booking-checklist.md`) is built but has no page on the site; it is not linked from the post.
- Follow-up (not blocking): backlinks to add from four related posts are listed in 02-seo.json `backlinks_to_add`.

## Checklist

- [x] 11-body.md built (front matter and fact markers removed; no CTA marker present; 5 image slot comments kept; allergen legal note dated)
- [x] 11-publish-package.json built and validated (`All valid.`)
- [x] booking-checklist.md built
- [ ] Images uploaded (none sourced)
- [ ] Fields entered in CMS (not uploaded)
- [ ] Primary category set (not uploaded)
- [ ] Save Draft (not done)
- [ ] Live URL checked after save (not done)
- [ ] Preview screenshots (none: no browser)
- [ ] 301 from the 17 post (web team, at publish)

## Mismatches

None observed: CMS not opened.
