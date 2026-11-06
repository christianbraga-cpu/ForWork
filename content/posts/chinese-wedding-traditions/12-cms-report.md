# Stage 12 CMS report: chinese-wedding-traditions

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/chinese-wedding-traditions/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/chinese-wedding-traditions/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; primary CTA block, 1 [[VERIFY]] marker and 7 IMAGE SLOT comments kept)
- Title: What Are the Chinese Wedding Traditions You Did Not Know?
- Slug: chinese-wedding-traditions. Path: /expert-advice/chinese-wedding-traditions
- Type: Listicle. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Cultural Weddings, Asia
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 7 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Read the free magazine" (CTA block after the return visit, utm_content=primary); secondary "Speak with a Wedded Advisor" (inline, end of 'Chinese weddings for Australians', utm_content=secondary). Both utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 7 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA block (magazine, utm_content=primary): in package, not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken

## Refresh and redirects (do at publish)
1. Update `/6-weird-and-wonderful-chinese-wedding-traditions` in place: change its slug and path to `/expert-advice/chinese-wedding-traditions`, replace the old body, categories and unlicensed images, then load the old URL and confirm a 301 (not 302 or 404).
2. Keep `/why-chinese-brides-wear-red-dresses` live and cross-link it with the new post both ways. No 301.
3. Publish-day check: Smartraveller China (level, update date, visa waiver end date) and the Beijing embassy and consulate pages.

## Before publish
- [[VERIFY]] (1): Embassy and Consulates-General notarial/CNI pages not read; confirm CNI service for a marriage in China and re-read consulate URLs before linking them.
- No prices, so no price sign-off; Nic to approve the Advisor lines and both CTAs.
- Licensed images for all 7 slots (AI fallback only for tea-ceremony and red-double-happiness, with Nic's approval, captioned 'Illustrative image').

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=chinese-wedding-traditions`.
