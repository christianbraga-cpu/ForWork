# CMS report: engagement-ring-insurance (WW-049)

**Draft URL / ID:** not uploaded.

**Why:** there is no browser tool in this cloud session, and `content-system/cms/field-map.md` says "Status: NOT YET MAPPED" (it must say CONFIRMED). Nothing was saved, published or scheduled in the CMS. No credentials were requested or entered.

**Next step:** run `/wedded-cms-discovery` in a Chrome tab where you are logged into the CMS, confirm the field map, then run `/wedded-blog resume=engagement-ring-insurance`.

## Package (ready for upload)

- `content/posts/engagement-ring-insurance/11-publish-package.json`: stage 11 envelope, `status: "draft"`, plan_ref WW-049. Validator: all valid.
- `content/posts/engagement-ring-insurance/11-body.md`: the 08-final.md wording, unchanged apart from these edits:
  - the CTA block rendered at the former `<!-- CTA: primary -->` marker
  - fact markers and other non-image comments removed
  - the frontmatter dropped
  - 7 `<!-- IMAGE SLOT ... -->` comments kept in place
  - 1 `[[VERIFY]]` (TMD) left visible for the reviewer

| Field | Value |
|---|---|
| Title | Engagement Ring Insurance and How to Get It |
| Slug / URL | engagement-ring-insurance / /style-advice/engagement-ring-insurance |
| Primary category | Style Advice (set explicitly; categories: Style Advice, Rings and Jewellery, Proposals & Rings) |
| Author | Wedded Wonderland |
| Meta title | Engagement Ring Insurance: How to Get Covered in Australia |
| Focus keyword | engagement ring insurance |
| Canonical | https://weddedwonderland.com/style-advice/engagement-ring-insurance |
| Key takeaways | 4 |
| FAQ | 6 Q&A pairs, mirrored in FAQPage schema |
| Primary CTA | Speak with a Wedded Advisor, /wonderland-concierge (utm_content=primary), subtext "Fee agreed in writing before any work begins" |
| Secondary CTA | inline /destinations link in the close (utm_content=secondary) |
| Schema | @graph: Article (datePublished empty), BreadcrumbList Home > Style Advice > post, FAQPage |

## Checklist (publish-checklist.md)

- [ ] Images uploaded with alt and caption: not done (all 7 slots "needed")
- [ ] Featured image: not done (slot "featured" needed)
- [ ] Title, slug, excerpt, author: not done (in package)
- [ ] Body: not done (11-body.md ready)
- [ ] Key Takeaways block: not done (4 items in package)
- [ ] CTA block: not done (in package; subtext support unconfirmed)
- [ ] FAQ: not done (6 items in package)
- [ ] Categories, then primary category set explicitly: not done (method unknown until field map is confirmed)
- [ ] Tags: not done (10 in package)
- [ ] SEO fields: not done (in package)
- [ ] Schema: not done (in package; field availability unknown)
- [ ] Internal draft note: not done (`draft_note` in package)
- [ ] Save Draft: not done
- [ ] Preview screenshots, desktop and mobile: none taken

## Screenshots

None (no upload).

## Mismatches with the field map

The field map is not filled in, so nothing could be compared. Open items for discovery:
- Can the CTA block render subtext?
- How is the primary category set?
- Is there a schema field?
- Is there an internal note field?
- Is there an end-of-post module that could hold the /magazine lead magnet?

## Before publish (from draft_note)

1. Resolve `[[VERIFY: ASIC or Moneysmart plain-English definition of a Target Market Determination (TMD)]]`. The ASIC and Moneysmart pages returned 404 on 29 Oct 2026.
2. Nic sign-off on prices: none needed (no prices printed).
3. Source all 7 images: featured, three_ways, policy_checks, paperwork, proposal_abroad, travel_wedding, claims_checklist.
4. Confirm the primary CTA is Concierge, as CRO chose, rather than the brief's /destinations. Swap the two if needed.
5. After publish, add backlinks from the insurance sections of the settings and styles posts.
6. Set the last-updated date in the CMS at publish.
