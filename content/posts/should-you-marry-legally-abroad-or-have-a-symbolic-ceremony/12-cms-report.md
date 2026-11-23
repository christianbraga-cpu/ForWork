# CMS report: should-you-marry-legally-abroad-or-have-a-symbolic-ceremony

**Result: not uploaded. Package only.**

- Draft URL/ID: not uploaded.
- Reason 1: package-only run as instructed (no browser used, no upload or login attempted).
- Reason 2: `content-system/cms/field-map.md` is `Status: NOT YET MAPPED`, not `CONFIRMED`.
- Nothing was saved, published or scheduled in the CMS. Draft only: a human clicks Publish.

## Legal note (read before saving)

**Every legal point in this post is general information as at November 2026, not legal advice.**

Each legal claim links at the claim to an official source:

- Attorney-General's Department: [Get married](https://www.ag.gov.au/families-and-marriage/marriage/get-married) and [Notice of intended marriage](https://www.ag.gov.au/families-and-marriage/publications/notice-intended-marriage)
- Smartraveller: [Getting married overseas](https://www.smartraveller.gov.au/planning-trip/advice-your-planned-activities/getting-married-overseas) (including certificates of no impediment)
- Federal Register of Legislation: [Marriage Act 1961](https://www.legislation.gov.au/C1961A00012/latest/text)
- AustLII: Marriage Act [s45](https://classic.austlii.edu.au/au/legis/cth/consol_act/ma196185/s45.html) and [s46](https://classic.austlii.edu.au/au/legis/cth/consol_act/ma196185/s46.html)

The line "General information as at November 2026, not legal advice." appears under the comparison table, in "How to Marry Legally and Still Have a Symbolic Ceremony" and in two FAQ answers. Nothing in the post says Wedded Wonderland, Wedded Concierge or a Wedded Advisor handles the legal marriage or paperwork. Recheck that each official link still resolves and says the same at publish.

## URL, slug and redirect

- URL https://weddedwonderland.com/expert-advice/should-you-marry-legally-abroad-or-have-a-symbolic-ceremony: **KEPT, do not change.**
- Slug `should-you-marry-legally-abroad-or-have-a-symbolic-ceremony`: **KEPT, do not change.**
- Redirect: **none.**
- https://weddedwonderland.com/expert-advice/symbolic-ceremony was requested but **not created** (15 Oct audit merge, user's choice). Do not create it. It was confirmed not live (404) on 2026-11-23, so no redirect is needed.
- Primary category Expert Advice is unchanged from the live page, so the URL should not move. **Still check the live URL after saving the draft.** If it moved, do not publish until it is fixed or a 301 is confirmed.

## What changes

| Field | Value |
|---|---|
| Title | What Is a Symbolic Ceremony? (user's choice) |
| Meta title | Symbolic Ceremony Meaning and How to Marry Legally Too (54 characters) |
| Meta description | What a symbolic ceremony is, how it differs from a legal wedding, and how Australian couples marry legally at home and celebrate anywhere in the world. (151 characters, from 02-seo.json, no figures) |
| Focus keyword | symbolic ceremony |
| Categories (in order) | Expert Advice, Destination Weddings, Planning Guides |
| Primary category | Expert Advice (unchanged; set explicitly) |
| Tags | Wedding Paperwork, Symbolic Ceremony, Legal Requirements, Wedding Ceremony, Destination Weddings |
| Canonical | https://weddedwonderland.com/expert-advice/should-you-marry-legally-abroad-or-have-a-symbolic-ceremony |
| Breadcrumb | Home > Expert Advice > What Is a Symbolic Ceremony? |
| Key takeaways | 4 |
| FAQ | 7 pairs, FAQPage schema included |
| Prices | None |
| Status | Draft only. A human publishes. |

"Planning Guides" has no hub in link-map.csv (nearest: /blog/wedding-planning); confirm it is a real CMS category or drop it.

## Remove from the old post

- Every /vendor link (including "local professionals") and the "Venues & Vendors to Explore" vendor card module. If the module is a site template and not editable, leave it and report it.
- All cost and budget claims: "one set of costs", "cheaper abroad", "Budget for both sides", the "Are symbolic ceremonies cheaper?" FAQ and the budget question in "Questions to ask yourselves".
- The guarantee wording in the old closing box CTA, "Your Choice of Ceremony is Never Meaningless", and any CTA line tying Concierge to the legal route or legal ceremony.
- The broken celebrant link (missing /expert-advice/) and the broken vow renewal link (pointed to /destination-packages). The new body links /expert-advice/what-does-a-celebrant-do-and-do-you-need-one-abroad and /expert-advice/vow-renewal-ideas.
- The Wonderland Studio budget-tool claim.
- Filler links named in the brief (/venue, /destination-packages, honeymoon packages, /destination-wedding-guide, /wedding-planning-tools, /plan-your-destination-wedding) and the Greek island link in the intro.
- The old unsourced legal list and claims.

The new body (`11-body.md`) replaces the old body in full and contains none of these.

## Steps for the web team

1. Log into the CMS yourself and open the existing post at /expert-advice/should-you-marry-legally-abroad-or-have-a-symbolic-ceremony (edit, do not create a new post).
2. Do not change the slug field.
3. Replace the body with `11-body.md`; replace title, excerpt, key takeaways, FAQ, tags, meta title and description, and schema from `11-publish-package.json`. The four Wedded Concierge and magazine links are already inline in the body; do not add copies.
4. Remove the items listed above, including the vendor card module if editable.
5. Categories in this order: Expert Advice, Destination Weddings, Planning Guides; then set the primary category explicitly to Expert Advice.
6. Paste the `draft_note` from the package into the internal note field.
7. Save Draft only. Never Publish or Schedule.
8. Immediately check the live URL is exactly /expert-advice/should-you-marry-legally-abroad-or-have-a-symbolic-ceremony.
9. Preview desktop and mobile: images, links, CTAs, breadcrumb (Home > Expert Advice > post).

## Open items before publishing

- **Images: 4 slots needed, none sourced:** featured, legal-signing-australia, ritual-moment, guests-destination. Licensed real photography only, consent for identifiable people, location provable. Never AI for real people or places. Do not publish with `[[IMAGE NEEDED]]` captions. Images on the live page have no licence on record; do not keep them unless the register confirms one.
- **Internal links to draft pages:** /expert-advice/who-can-perform-a-marriage, /destination-weddings/get-married-in-new-zealand and /expert-advice/short-wedding-vows are drafts in the link map. Publish them first, or unlink the anchor text.
- Prices: none in the post, so nothing for Nic's price sign-off.
- `[[VERIFY]]` markers in the body: none. Package verify items: live URL after save, draft-page links, Planning Guides category, official links at publish, image licences, vendor module.
- `datePublished` in the schema is empty; set at publish.
- Booking checklist (`booking-checklist.md`) is built but has no page on the site; it is not linked from the post.
- Follow-up (not blocking): backlinks to add from four related posts are listed in 02-seo.json `backlinks_to_add`.

## Checklist

- [x] 11-body.md built (front matter and fact markers removed; no CTA marker present; 4 image slot comments kept)
- [x] 11-publish-package.json built and validated (`All valid.`)
- [x] booking-checklist.md built
- [ ] Images uploaded (none sourced)
- [ ] Fields entered in CMS (not uploaded)
- [ ] Primary category set (not uploaded)
- [ ] Save Draft (not done)
- [ ] Live URL checked after save (not done)
- [ ] Preview screenshots (none: no browser)

## Mismatches

None observed: CMS not opened.
