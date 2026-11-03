# CMS report: lebanese-wedding-traditions

**Draft URL/ID:** not uploaded. This was a package-only run (fast mode, no browser), and `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`. Nothing was saved, published or scheduled in the CMS.

**Target:** /expert-advice/lebanese-wedding-traditions (CMS slug `lebanese-wedding-traditions`, primary category Expert Advice). This is a refresh of /7-big-and-electrifying-lebanese-wedding-traditions.

## Package
- `11-publish-package.json`: stage 11, status `needs_input`, payload status `draft`. `validate.py` passes ("All valid").
- `11-body.md`: the wording is identical to `08-final.md`. The primary CTA ("Read the free magazine", utm_content=primary) is rendered once at the marker. Fact markers are removed. All 7 IMAGE SLOT comments are kept.

## Checklist (package)
- [x] Title, slug, URL path and excerpt
- [x] Byline: Wedded Wonderland
- [x] Categories: Expert Advice (primary, categories[0]), Wedding Traditions, Cultural Weddings, Destination Weddings, Middle East
- [x] Tags from the brief
- [x] Key takeaways: exactly 4, matching 08-final.md
- [x] FAQ: 6 Q&A pairs, plus FAQPage schema
- [x] Primary CTA block. The secondary Advisor CTA stays as the existing inline link, with no extra block
- [x] SEO: meta title, meta description, focus keyword, canonical
- [x] Schema JSON-LD: Article (datePublished empty), BreadcrumbList (Home > Expert Advice > post), FAQPage
- [x] Internal draft note
- [x] No prices, so no Nic price sign-off is needed. No em dashes. No [[VERIFY]] markers in the body
- [ ] Images: all 7 slots are `needed` (featured, henna-night, ceremony, zaffeh, dabke, sugared-almonds, abroad-italy). None are licensed yet
- [ ] CMS upload, preview and screenshots: not done (no field map, no browser)

## Before publish (human)
1. Re-check Smartraveller Lebanon on publish day. Confirm it still says "Do not travel" (updated 24 September 2026), and that the religious-law and dual nationality lines and Key takeaway 4 still match.
2. 301 redirects (recommendation only): /7-big-and-electrifying-lebanese-wedding-traditions and /how-to-plan-a-lebanese-wedding-2-2, both to /expert-advice/lebanese-wedding-traditions.
3. Check that /guides/arab-levantine-weddings, /expert-advice/wedding-traditions and /expert-advice/palestinian-wedding-traditions are live, or remove those links.
4. Featured image licensed and uploaded.

## Mismatches
- The field map is not confirmed. Run `/wedded-cms-discovery`, then `/wedded-blog resume=lebanese-wedding-traditions`.

## Screenshots
None (no CMS session).
