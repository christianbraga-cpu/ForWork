# CMS report: albanian-wedding-traditions

**Draft URL/ID:** not uploaded.
**Reason:** package-only run (fast mode, no browser tool used). Also, `content-system/cms/field-map.md` says `Status: NOT YET MAPPED`, so upload would be blocked anyway. Run `/wedded-cms-discovery`, confirm the field map, then `/wedded-blog resume=albanian-wedding-traditions`.

## Package

- `content/posts/albanian-wedding-traditions/11-publish-package.json` (stage 11, status `needs_input`, payload `status: draft`, validate.py: All valid)
- `content/posts/albanian-wedding-traditions/11-body.md`

| Field | Value |
|---|---|
| Title | What Are the Albanian Wedding Traditions You Did Not Know? |
| Slug | albanian-wedding-traditions |
| URL | /expert-advice/albanian-wedding-traditions |
| Primary category | Expert Advice (categories[0]; set explicitly once the field map says how) |
| Other categories | Wedding Traditions, Cultural Weddings, Destination Weddings, Europe |
| Author byline | Wedded Wonderland |
| Meta title | Albanian Wedding Traditions: Customs and Meanings |
| Focus keyword | albanian wedding traditions |
| Primary CTA | Read the free magazine (utm_content=primary), rendered before "Marrying legally in Albania as an Australian" |
| Key takeaways | 4, copied from 08-final.md |
| FAQ | 6 Q&A pairs, also in FAQPage JSON-LD |
| Schema | Article + BreadcrumbList (Home > Expert Advice > post) + FAQPage, datePublished empty |

## Checklist

- [x] Body built from 08-final.md, wording unchanged; fact markers and non-image comments removed; 8 IMAGE SLOT comments kept
- [x] CTA from 09-cro.json rendered at the marker
- [x] No em dashes, no prices, no [[VERIFY]] markers in the body
- [x] Draft note written (Smartraveller publish-day check, images, redirect, no prices)
- [ ] Images uploaded (all 8 slots `needed`, no licensed files)
- [ ] Featured image, title/slug/excerpt/author, body, takeaways, CTA, FAQ, categories, primary category, tags, SEO, schema, draft note entered in CMS
- [ ] Save Draft
- [ ] Preview screenshots (desktop, mobile): none taken

## Before publish (human)

1. Publish-day Smartraveller check of the Albania page (level, 16 October 2026 update date, healthcare, heat and fire, protests, dual nationality, same-sex lines).
2. 301 redirect, recommendation only: `/9-albanian-wedding-traditions-thatll-have-you-partying-all-week` to `/expert-advice/albanian-wedding-traditions`, at publish.
3. Licensed featured image (and inline images or remove their slots).
4. Nic: no prices in the post, so no price sign-off needed.

## Mismatches

None checked against a live CMS (no upload). Field map not yet mapped.
