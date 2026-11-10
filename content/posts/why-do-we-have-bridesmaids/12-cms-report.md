# Stage 12 CMS report: why-do-we-have-bridesmaids

**Draft URL/ID:** not uploaded. Reason: this was a package-only run (no browser in this session), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

## Package
- `content/posts/why-do-we-have-bridesmaids/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/why-do-we-have-bridesmaids/11-body.md` (08-final.md wording unchanged, with the 09-cro edits already applied; fact markers and front matter removed; primary CTA block and 6 IMAGE SLOT comments kept; scan_copy.py clean, 0 dashes)
- Title: Bridesmaids Tradition and Where It Comes From
- Slug: why-do-we-have-bridesmaids. Path: /expert-advice/why-do-we-have-bridesmaids
- Type: Guide. Cluster: Wedding Traditions
- Categories: Expert Advice (primary), Wedding Traditions, Planning Guides
- Author/byline: Wedded Wonderland
- Key takeaways: 4. FAQ: 5 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs: primary "Read the free magazine" (CTA block at the end of section 6, how many bridesmaids, utm_content=primary); secondary Wedded Advisor link closing section 9, destination weddings (utm_content=secondary); closing Advisor link (utm_content=closing); magazine link in the closing section (utm_content=magnet). All utm_medium=content.

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
- The pillar `/expert-advice/wedding-traditions`, `/expert-advice/why-do-brides-wear-veils`, `/expert-advice/something-old-something-new` and `/expert-advice/what-do-bridesmaids-wear`, all linked from this post, are drafts. Publish them together with this post. Add links from each back to this post at publish.
- Live listicle pages linked from the body: `/how-many-is-too-many-9-weddings-with-the-most-bridesmaids` (section 6) and `/5-types-of-bridesmaids-every-bride-needs` (section 7). Confirm both still resolve at publish.

## Before publish
- [[VERIFY]]: image credits only. All 6 captions read "Photo: [[VERIFY credit]]" (featured, maid-of-honour-dress, getting-ready, bridesman-mixed-party, destination-wedding-party, thank-you-gift).
- No prices, so no price sign-off. Nic approves the Advisor lines and the CTAs.
- Licensed images for all 6 slots. AI fallback only for thank-you-gift, with Nic's approval, as a neutral still life captioned 'Illustrative image'. Never AI for the hero or any slot with people or place. The destination-wedding-party caption names the place and town only once verified.
- "In this guide" anchors (`#4-maid-of-honour-or-matron-of-honour-what-is-the-difference`, `#6-how-many-bridesmaids-should-you-have`, `#9-bridesmaids-at-a-destination-wedding`, `#frequently-asked-questions`): confirm they match the heading IDs the CMS builds, and fix in preview if not.
- Publish day: recheck the travel insurance wording in section 9 against Smartraveller and update 'As at November 2026' if anything changed.

## Mismatches
- Field map not mapped: run `/wedded-cms-discovery` in a logged-in Chrome tab, confirm the map, then `/wedded-blog resume=why-do-we-have-bridesmaids`.
