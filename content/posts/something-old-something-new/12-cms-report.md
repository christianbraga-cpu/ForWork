# Stage 12 CMS report: something-old-something-new

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/something-old-something-new/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/something-old-something-new/11-body.md` (08-final.md wording unchanged; fact markers and front matter removed; primary CTA block and 6 IMAGE SLOT comments kept; no [[VERIFY]] markers)
- Title: Something Old Something New Meaning and Origins
- Slug: something-old-something-new. Path: /expert-advice/something-old-something-new
- Type: Listicle. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Planning Guides
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Read the free magazine" (CTA block after section 6, something blue, utm_content=primary); secondary Wedded Advisor link closing section 9, carrying heirlooms (utm_content=secondary); closing Advisor link (utm_content=closing); magazine link in the closing section (utm_content=magnet). All utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 6 slots `needed`
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

## Redirects and publish order
- Redirects: none. This is a new article with no old page.
- The pillar `/expert-advice/wedding-traditions` and the `/style-advice/engagement-ring-insurance` and `/style-advice/lab-grown-diamonds` articles this post links to are drafts. Publish them first or together with this post. Add a link from the pillar to this post at publish.

## Before publish
- [[VERIFY]]: none in the body.
- No prices, so no price sign-off. Nic approves the Advisor lines and the CTAs.
- Licensed images for all 6 slots (featured, something-old, something-new, something-borrowed, something-blue, sixpence). AI fallback only for something-old, something-new, something-blue and sixpence, with Nic's approval, as neutral still lifes captioned 'Illustrative image'. Never AI for the hero or for something-borrowed.
- Publish day: recheck the travel insurance wording in section 9 against Moneysmart, and confirm `/style-advice/engagement-ring-styles` and `/plan-your-destination-wedding` are live.

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=something-old-something-new`.
