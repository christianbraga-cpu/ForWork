# Stage 12 CMS report: serbian-wedding-traditions

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/serbian-wedding-traditions/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/serbian-wedding-traditions/11-body.md` (08-final.md wording unchanged; fact markers, front matter and CTA wrapper comments removed; CTA rendered once after section 11; 7 IMAGE SLOT comments kept)
- Title: What Are the Serbian Wedding Traditions You Did Not Know?
- Slug: serbian-wedding-traditions. Path: /expert-advice/serbian-wedding-traditions
- Categories: Expert Advice (primary), Wedding Traditions, Cultural Weddings, Europe
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 7 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.

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

## Refresh and redirects (recommendations; do at publish)
1. Update `/6-quirky-serbian-wedding-traditions-2` in place: change its slug and path to `/expert-advice/serbian-wedding-traditions`, replace the old body, categories and unlicensed images, then confirm the old URL returns a 301 (not 302 or 404).
2. 301 `/how-to-plan-a-serbian-wedding` (live, same customs) and `/6-quirky-serbian-wedding-traditions` (currently 404; catches old links) to the new URL. Recommendation only.
3. Publish-day check: Smartraveller Serbia (level and update date) and the Australian Embassy Belgrade notarial page.

## Before publish
- No [[VERIFY]] markers remain. No prices, so no price sign-off; Nic to approve the Advisor lines and CTA.
- Licensed images for all 7 slots.

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=serbian-wedding-traditions`.
