# Stage 12 CMS report: average-cost-wedding-photographer

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser was opened and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled in the CMS.

**Status:** Draft only. A human clicks Publish.

## Package
- `content/posts/average-cost-wedding-photographer/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/average-cost-wedding-photographer/11-body.md` (08-final.md wording unchanged; front matter and 21 fact markers removed; 4 IMAGE SLOT comments and the N-508 LINK comment kept; inline links and UTMs kept; no [[VERIFY]] markers)
- `content/posts/average-cost-wedding-photographer/booking-checklist.md` (questions to ask a photographer, side-by-side package comparison)
- Title: Average Wedding Photographer Cost and What Packages Include
- Slug: average-cost-wedding-photographer. URL: https://weddedwonderland.com/expert-advice/average-cost-wedding-photographer
- Type: New (not a refresh, no redirect). Cluster: Average Wedding Cost
- Categories: Expert Advice (primary), Wedding Photography, Wedding Budget, Planning Guides
- Tags: wedding photographer cost, wedding photography packages, wedding budget, wedding suppliers, destination wedding photography, wedding contracts
- Author/byline: Wedded Wonderland
- Meta title: Average Cost Wedding Photographer and What Packages Include (59 chars, exactly as 02-seo.json; no figures, colons or dashes)
- Meta description: What shapes a wedding photographer quote, what a package should include and the questions to ask before you sign, whether you marry at home or abroad. (150 chars, exactly as 02-seo.json)
- Excerpt: What shapes a wedding photographer's quote, what a package should spell out in writing, the extras that sit outside it, questions to settle for a wedding abroad, and your consumer and copyright position in Australia before you sign. (232 chars; no figures, no "usually/most/typically", no promise of an average)
- Key takeaways: 4. FAQ: 5 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline in the body): primary Wedded Concierge link (end of "Photographing a destination wedding"), secondary Wedded Concierge link (end of "How to compare quotes in writing"), closing Wedded Concierge link and magazine link (closing paragraph). All utm_medium=content.

## Checklist (publish-checklist.md)
- [ ] Images uploaded with alt and caption: not done, all 4 slots `needed`
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

## Images
- Place images by the IMAGE SLOT comments in `11-body.md`:
  - `featured`: featured image (comment at the top of the body)
  - `cost-factors`: under the H2 "What shapes a wedding photographer's quote"
  - `package-inclusions`: under the H2 "What wedding photographer packages include"
  - `destination-coverage`: under the H2 "Photographing a destination wedding"
- All 4 slots are still `needed`. Licensed photos only; never AI for real people or places. The package-inclusions still life (no people, no real place) may use AI only if Nic approves, captioned "Illustrative image".
- Do not publish with `[[IMAGE NEEDED]]` captions.

## Links to settle
- **N-508 (destination photographer cost):** no URL yet. The sentence "Our destination photographer cost guide goes further into travel, accommodation and coverage abroad." is plain text followed by `<!-- LINK N-508: destination photographer cost guide, add URL when live -->`. Add the link when N-508 is live.
- **/all-inclusive-wedding-cost:** both it and /destination-weddings/all-inclusive-wedding-cost are in the link map. Confirm the canonical one before publishing and update the link in "Extras that sit outside the headline package" if needed.
- **Italy photographer cost:** confirm /what-does-an-italy-wedding-photographer-cost permanently (301) redirects to /expert-advice/what-does-an-italy-wedding-photographer-cost (the body links the /expert-advice/ URL).

## Before publish
- [[VERIFY]]: none in the body.
- NO FIGURES by the user's choice, so nothing for Nic's price sign-off. Nic to approve the Wedded Concierge lines (primary, secondary, closing) and the magazine link.
- Licensed images for all 4 slots.
- N-508 link, all-inclusive canonical and Italy 301 settled as above.
- Set datePublished at publish.

## Mismatches
- None checked on screen: package-only run, and the CMS field map is still not mapped. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=average-cost-wedding-photographer`.
