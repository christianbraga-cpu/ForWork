# Stage 12 CMS report: wedding-processional-songs

**Draft URL/ID:** not uploaded. Stopped before the CMS: no Chrome or browser tool in this session, and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/wedding-processional-songs/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-processional-songs/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; 5 IMAGE SLOT comments kept; no [[VERIFY]] markers)
- `content/posts/wedding-processional-songs/booking-checklist.md` (processional music checklist)
- Title: 40 Wedding Processional Songs to Walk Down the Aisle To
- Slug: wedding-processional-songs. Path: /expert-advice/wedding-processional-songs
- Refresh of: /top-24-wedding-processional-songs-in-2024 (update in place, 301)
- Categories: Expert Advice (primary), Wedding Music, Planning Guides
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage, ItemList (40 songs); datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body): primary and secondary Wedded Concierge links, closing Wedded Concierge link, magazine link. All utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 5 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA block: in package, not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken

## In-place update and 301 (for the web team, at publish)
1. Open the existing page `/top-24-wedding-processional-songs-in-2024` in the CMS. Do not create a new post.
2. Change its title to "40 Wedding Processional Songs to Walk Down the Aisle To", its slug to `wedding-processional-songs` and its path to `/expert-advice/wedding-processional-songs`.
3. Replace the old body, excerpt, categories (Expert Advice primary), tags, meta title, meta description, canonical and schema with the package values. Remove old images unless their licence is confirmed.
4. Save as Draft only. A human clicks Publish.
5. After publish, load `/top-24-wedding-processional-songs-in-2024` and confirm it returns a 301 (not 302 or 404) to `/expert-advice/wedding-processional-songs`. Update any internal links that still point to the old URL.
6. Set datePublished at publish.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so no price sign-off; Nic to approve the Wedded Concierge lines and the magazine link.
- Licensed images for all 5 slots (AI fallback only for the instrumental slot, with Nic's approval, captioned 'Illustrative image').

## Mismatches
- Field map not confirmed, so no on-screen comparison was possible. Run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-processional-songs`.
