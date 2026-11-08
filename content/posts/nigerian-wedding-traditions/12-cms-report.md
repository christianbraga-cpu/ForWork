# Stage 12 CMS report: nigerian-wedding-traditions

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/nigerian-wedding-traditions/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/nigerian-wedding-traditions/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; primary CTA block and 7 IMAGE SLOT comments kept; no [[VERIFY]] markers)
- Title: What Are the Nigerian Wedding Traditions You Did Not Know?
- Slug: nigerian-wedding-traditions. Path: /expert-advice/nigerian-wedding-traditions
- Type: Listicle. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Cultural Weddings, Africa
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 7 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Read the free magazine" (CTA block after section 11, the white wedding, utm_content=primary); secondary "Speak with a Wedded Advisor" (inline link closing the Advisor paragraph in 'Music, the alaga or MC and room for spraying', utm_content=secondary); closing Advisor link (utm_content=closing); African wedding website template link (utm_content=magnet). All utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 7 slots `needed`
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
1. Update `/10-nigerian-wedding-customs-that-prove-these-brides-know-how-to-party` in place: change its slug and path to `/expert-advice/nigerian-wedding-traditions`, replace the old body, categories and unlicensed images, then load the old URL and confirm a 301 (not 302 or 404).
2. No duplicate Nigerian pages found, so no other 301s.
3. Publish-day check: Smartraveller Nigeria (overall 'Reconsider your need to travel', including Abuja, and the 26 states and Federal Capital Territory at 'Do not travel'), Australian High Commission Abuja services and the overseas marriage recognition wording.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so no price sign-off; Nic to approve the Advisor lines and the CTAs.
- Licensed images for all 7 slots (featured, yoruba-introduction, gele-aso-oke, hausa-fulani, igba-nkwu, aso-ebi, spraying-reception). AI fallback only for gele-aso-oke, with Nic's approval, as a neutral still life of folded aso oke captioned 'Illustrative image'.

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=nigerian-wedding-traditions`.
