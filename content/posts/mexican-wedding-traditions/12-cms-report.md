# Stage 12 CMS report: mexican-wedding-traditions

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/mexican-wedding-traditions/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/mexican-wedding-traditions/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; primary CTA block and 8 IMAGE SLOT comments kept; no [[VERIFY]] markers)
- Title: What Are the Mexican Wedding Traditions You Did Not Know?
- Slug: mexican-wedding-traditions. Path: /expert-advice/mexican-wedding-traditions
- Type: Listicle. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Cultural Weddings, Americas
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 7 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Read the free magazine" (CTA block after section 12, la tornaboda, utm_content=primary); secondary "Speak with a Wedded Advisor" (inline link, end of 'Bringing Mexican traditions home', utm_content=secondary). Both utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 8 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA block (magazine, utm_content=primary): in package, not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken

## Refresh and redirects (do at publish)
1. Update `/10-of-the-most-fascinating-wedding-traditions-in-mexico` in place: change its slug and path to `/expert-advice/mexican-wedding-traditions`, replace the old body, categories and unlicensed images, then load the old URL and confirm a 301 (not 302 or 404).
2. No duplicate Mexican traditions pages found, so no other 301s.
3. Keep `/destinations/latin-america-caribbean/mexico` and `/10-tips-for-planning-a-destination-wedding-in-mexico` live and cross-link them with the new post both ways. No 301.
4. Publish-day check: Smartraveller Mexico (overall level and the 'Reconsider your need to travel' state list), entry conditions and the Embassy CNI process.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so no price sign-off; Nic to approve the Advisor lines and both CTAs.
- Licensed images for all 8 slots (AI fallback only for arras, with Nic's approval, as a neutral coin still life captioned 'Illustrative image').

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=mexican-wedding-traditions`.
