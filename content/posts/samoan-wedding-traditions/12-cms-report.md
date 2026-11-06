# Stage 12 CMS report: samoan-wedding-traditions

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/samoan-wedding-traditions/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/samoan-wedding-traditions/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; primary CTA block and 8 IMAGE SLOT comments kept; no [[VERIFY]] markers)
- Title: What Are the Samoan Wedding Traditions You Did Not Know?
- Slug: samoan-wedding-traditions. Path: /expert-advice/samoan-wedding-traditions
- Type: Listicle. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Cultural Weddings, Australia & Pacific
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 7 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Read the free magazine" (CTA block after the wedding feast, utm_content=primary); secondary "Speak with a Wedded Advisor" (inline Wedded Concierge link, end of 'Bringing Samoan traditions home', utm_content=secondary). Both utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 8 slots `needed`
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
1. Update `/5-samoan-wedding-traditions-that-will-leave-you-shocked-and-excited` in place: change its slug and path to `/expert-advice/samoan-wedding-traditions`, replace the old body, categories and unlicensed images, then load the old URL and confirm a 301 (not 302 or 404).
2. 301 `/5-samoan-traditions` (duplicate, ranks AU) to `/expert-advice/samoan-wedding-traditions`, then load it and confirm the 301.
3. Keep `/a-traditional-samoan-wedding-celebration` live and cross-link it with the new post both ways. No 301.
4. Publish-day check: Smartraveller Samoa (level, 5 August 2026 update, dengue and cyclone notes) and the Visitor Permit conditions.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so no price sign-off; Nic to approve the Advisor lines and both CTAs.
- Licensed images for all 8 slots (AI fallback only for fine-mats, with Nic's approval, as a neutral woven mat still life captioned 'Illustrative image').

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=samoan-wedding-traditions`.
