# CMS report: is-marriage-in-italy-recognised-in-australia

**Draft URL/ID: not uploaded.**

Why it was not uploaded:
1. No browser tool in this session. Claude in Chrome (`mcp__claude-in-chrome__*`) and the remote-devices browser are both unavailable.
2. `content-system/cms/field-map.md` reads `Status: NOT YET MAPPED`, not `CONFIRMED`.

Nothing was entered, saved, published or scheduled in the CMS. Only the package (Part 1) was built.

Next step: run `/wedded-cms-discovery` in a Chrome tab where you are logged into the CMS, confirm the field map, then run `/wedded-blog resume=is-marriage-in-italy-recognised-in-australia`.

## Package

- `content/posts/is-marriage-in-italy-recognised-in-australia/11-publish-package.json`: stage 11 envelope, `status: "draft"`. Validates with `python3 -I content-system/scripts/validate.py content/posts/is-marriage-in-italy-recognised-in-australia` (all 14 stage files valid).
- `content/posts/is-marriage-in-italy-recognised-in-australia/11-body.md`: no front matter and no fact markers. It keeps 6 image-slot comments and 1 `[[VERIFY]]` marker. The primary CTA block from 09-cro.json is in place of the CTA marker.

| Field | Value |
|---|---|
| Title | Italian Marriage Recognition in Australia Explained |
| Slug / URL | is-marriage-in-italy-recognised-in-australia / /destination-weddings/is-marriage-in-italy-recognised-in-australia |
| Categories | Destination Weddings (primary), Italy, Expert Advice |
| Author | Wedded Wonderland (organisation; byline unconfirmed) |
| Key takeaways | 4, exactly as in 08-final.md |
| FAQ | 5 Q&A pairs (also in FAQPage JSON-LD) |
| Primary CTA | Speak with a Wedded Advisor, `utm_content=primary`, placed after "The trade-offs if Italy should be 'the' wedding" |
| Secondary CTA | Closing in-copy link, `utm_content=secondary` (already in the copy) |
| Lead magnet | Not placed (optional; add only if the person wants it) |
| Meta title | Is Marriage in Italy Recognised in Australia? What to Know |
| Focus keyword | is marriage in italy recognised in australia |
| Canonical | https://weddedwonderland.com/destination-weddings/is-marriage-in-italy-recognised-in-australia |
| Schema | @graph: Article (datePublished empty), BreadcrumbList (Home > Destination Weddings > post), FAQPage |
| needs_signoff | empty (no prices printed) |

## Publish checklist

Before upload
- [ ] Field map status is CONFIRMED: **no** (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0]
- [ ] Approved images prepared: **no**, all 6 slots are `needed`
- [ ] Person logged into CMS in Chrome: not checked, because no browser tool is available

Upload: not started. Images, featured image, title/slug/excerpt/author, body, Key Takeaways, CTA, FAQ, categories plus primary category, tags, SEO, schema, draft note and Save Draft were all skipped.

After save: not applicable. No preview and no screenshots (`screenshots/` is empty).

## Mismatches

None checked on screen, because the CMS was not opened. The field map is still blank, so there is nothing to compare against yet.

## Draft note (for the CMS internal note field)

The full text is in `payload.draft_note`. In summary:
1. VERIFY (1): how Australia treats an Italian unione civile. AGD, Smartraveller, NSW and Victorian pages are silent as at October 2026.
2. Nic sign-off on prices: none (no prices printed).
3. Image slots needed (6): featured, home-again, proof-documents, passport-name, symbolic-ceremony, australian-celebration.
4. Deferred business items (6): Concierge fee model and commissions, deposits/refunds/contracts, From AUD ranges, named Advisor or phone or referral line, real wedding, Wedded Privileges.
5. Questions for the person:
   - Should the official fees be printed?
   - What does Wedded Concierge handle: the Prefettura apostille appointment, NAATI translation, comune follow-up, the Australian legal ceremony?
   - Who is the confirmed byline?
6. Publish together with /destination-weddings/getting-married-in-italy. This post links to it and it is still a draft.
7. Suggest a family lawyer reviews the civil union passage and the s 113 passages before publishing.
