# Stage 12 CMS report: baltic-wedding-traditions

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/baltic-wedding-traditions/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/baltic-wedding-traditions/11-body.md` (08-final.md wording unchanged; fact markers, front matter and the empty `<!-- CTA: primary -->` marker removed; 2 [[VERIFY]] markers and 7 IMAGE SLOT comments kept)
- Title: What Are the Baltic Wedding Traditions You Did Not Know?
- Slug: baltic-wedding-traditions. Path: /expert-advice/baltic-wedding-traditions
- Type: Listicle. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Cultural Weddings, Europe
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Speak with a Wedded Advisor" (inline, 'at home' section, utm_content=primary); secondary "Tell a Wedded Advisor" (closing section, utm_content=secondary).

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 7 slots `needed`
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered
- [ ] Body: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA block (Wedded Advisor, utm_content=primary): in package, not entered
- [ ] FAQ: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Preview screenshots (desktop, mobile): none taken

## Refresh and redirects (do at publish)
1. Update `/10-baltic-wedding-traditions-you-never-knew` in place: change its slug and path to `/expert-advice/baltic-wedding-traditions`, replace the old body, categories and unlicensed images, then load the old URL and confirm a 301 (not 302 or 404).
2. No other Baltic pages exist, so no further redirects.
3. Publish-day check: Smartraveller Estonia, Latvia and Lithuania (levels and update dates) and the Stockholm and Warsaw embassy pages.

## Before publish
- [[VERIFY]] (2): Stockholm embassy CNI for weddings in Estonia and Latvia; Warsaw embassy CNI for a wedding in Lithuania.
- No prices, so no price sign-off; Nic to approve the Advisor lines and both CTAs.
- Licensed images for all 7 slots (AI fallback only for lt-wreath and bread-salt still lifes, with Nic's approval).

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=baltic-wedding-traditions`.
