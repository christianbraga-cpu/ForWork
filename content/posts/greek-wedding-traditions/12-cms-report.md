# CMS report: greek-wedding-traditions

**Draft URL / ID:** not uploaded. Reason: this was a package-only run in fast mode with no Chrome, as the orchestrator asked. Also, `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`, so the publisher could not upload even with a browser. Nothing was published or scheduled.

**Target:** https://weddedwonderland.com/expert-advice/greek-wedding-traditions (primary category Expert Advice, CMS slug `greek-wedding-traditions`). This is a refresh of `/8-greek-wedding-traditions-you-didnt-know-about`.

## Package

- `content/posts/greek-wedding-traditions/11-publish-package.json` (stage 11, status draft; passes `validate.py` with "All valid")
- `content/posts/greek-wedding-traditions/11-body.md` (byline Wedded Wonderland; fact markers and CTA comment markers removed; CTA block appears once; 7 IMAGE SLOT comments kept; 08-final.md wording unchanged)

## Checklist

- [x] Body built from 08-final.md, with no wording changes
- [x] Key takeaways: 4, copied word for word from 08-final.md
- [x] FAQ: 8 Q&A pairs, plus FAQPage schema
- [x] Categories from the brief; primary_category = Expert Advice = categories[0]
- [x] Tags, meta title ("Greek Wedding Traditions: 12 Customs, From Church to Dance"), meta description, focus keyword and canonical
- [x] schema_jsonld: Article (publisher Wedded Wonderland, datePublished left empty), BreadcrumbList (Home > Expert Advice > post) and FAQPage
- [x] Primary CTA (magazine) and secondary CTA (Wedded Advisor, inline after the legal section)
- [x] Draft note written
- [x] No em dashes, and no "from first idea to the last dance"
- [ ] Images: all 7 slots are still needed (none approved, so alt text and captions are not written yet)
- [ ] CMS upload, Save Draft, preview and screenshots: not done (no browser; field map not confirmed)

## Screenshots

None, because nothing was uploaded.

## Redirects (human action)

1. **Required:** update `/8-greek-wedding-traditions-you-didnt-know-about` in place. Change its slug and path to `/expert-advice/greek-wedding-traditions`, and replace the old body, categories and unlicensed images. Then confirm the old URL returns a **301** (not 302 or 404).
2. **Recommendation only:** at publish, 301 `/greek-wedding-traditions-we-love` and `/10-charming-and-timeless-wedding-traditions-in-greece-2` to the new URL.
3. **On publish day:** check Smartraveller Greece (advice level, and the "last updated 30 September 2026" date) and the Australian Embassy Athens notarial page.

## Open items before Publish

- The body has no [[VERIFY]] markers. Other items still to check: the exact goarch.org marriage URL, and whether the internal link targets (German and Turkish pages, the pillar page, the Greece hub) are live.
- Nic: the body states no prices. Image licences still need Nic: the 3 old-page images, the AI fallback for koufeta, and consented real Greek wedding photos.

## Mismatches

There are no on-screen mismatches because the CMS was not opened. The field map has not been confirmed: run `/wedded-cms-discovery`.
