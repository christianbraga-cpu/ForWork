# Stage 12 CMS report: wedding-rsvp-website (REFRESH)

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser was opened, no login was attempted and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled.

**Status:** Draft only. A human clicks Publish.

## URL WARNING (read before saving)
- **Keep URL https://weddedwonderland.com/wedding-rsvp-website and slug `wedding-rsvp-website`. Do not change them. No redirect is planned.**
- The CMS category bug has moved **three recently saved refreshes** into category paths.
- Primary category stays **Expert Advice**, the live page's category, so the URL does not move. Do not switch it to Wedding Tools.
- **After Save Draft, check the live URL is still exactly `/wedding-rsvp-website`.** If it has moved (for example to `/expert-advice/wedding-rsvp-website` or `/wedding-tools/wedding-rsvp-website`), **do not publish until a 301 from `/wedding-rsvp-website` to the new path is confirmed.** Check again at publish.

## Package
- `content/posts/wedding-rsvp-website/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-rsvp-website/11-body.md` (08-final.md wording unchanged; front matter, H1 and 10 fact markers removed; 4 IMAGE SLOT comments kept; inline links and UTMs kept; no [[VERIFY]] markers in the body)
- `content/posts/wedding-rsvp-website/booking-checklist.md` (questions to ask any RSVP website plus a destination RSVP question set; names no platforms; Wedded Concierge link without UTM parameters)
- Title and meta title: Wedding RSVP Website Guide to Collect Every Reply (49 chars; the user's choice, replacing "Wedding RSVP Websites: Collect Every Reply, Chase None")
- Meta description (from 02-seo.json, unchanged, 153 chars, no figures, "free" or "best"): How to choose a wedding RSVP website that collects every reply: the main types compared, what to ask guests, QR codes and RSVPs for destination weddings.
- Excerpt: 223 chars, no figures, drawn from the intro and section headings.
- Focus keyword: wedding rsvp website. Canonical: https://weddedwonderland.com/wedding-rsvp-website. OG image: featured slot.
- Categories: Expert Advice (primary, set explicitly), Wedding Tools, Planning Guides. Tags: rsvp, wedding websites, wonderland studio, destination weddings, guest list.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice at /blog/expert-advice > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline; 08-final.md has no `<!-- CTA: primary -->` marker): primary Wedded Concierge (end of "Exporting numbers for your venue and caterer"), secondary (end of "Getting every reply in"), closing (last section), magazine link (end of "Where Wonderland Studio fits"). All utm_campaign=wedding-rsvp-website.
- No prices anywhere in the post or checklist.

## Author (to confirm)
The live page shows one author on the byline (Mark Tuason) but its article:author meta tag shows another (Yash). **Team to confirm which name the refresh carries** and make the byline and meta tag match. The package author field is marked `[[VERIFY: author]]`; schema author is Organization Wedded Wonderland until confirmed.

## Remove from the old post
When the refresh replaces the live content, none of these may survive in the CMS entry (body, old blocks, excerpt, SEO fields, image alt text):
- Every platform name: Zola, The Knot, Joy, Minted, RSVPify, Riley & Grey (and any other)
- All "free" wording
- All prices
- The dated "Feature claims verified 27 Aug 2026" line
- The old meta description that names platforms
- The old inline platform screenshot (never reuse)

The new body contains none of these (checked by scan).

## Checklist (publish-checklist.md)
- [ ] Field map CONFIRMED: no (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0] (Expert Advice)
- [ ] Images prepared with alt and caption: not done, all 4 slots `needed`
- [ ] Logged into CMS: not checked (package-only run)
- [ ] Images uploaded first: not done
- [ ] Featured image: not done (slot `featured` needed)
- [ ] Title, slug, excerpt, author: in package, not entered (author to confirm)
- [ ] Body with inline images: in package, not entered
- [ ] Key Takeaways block: in package, not entered
- [ ] CTA blocks: in package (inline), not entered
- [ ] FAQ block: in package, not entered
- [ ] Categories, then primary category set explicitly: in package; method unknown until the field map is confirmed
- [ ] Tags, SEO fields, schema, internal draft note: in package, not entered
- [ ] Save Draft: not done
- [ ] Live URL still /wedding-rsvp-website after save: not checked (nothing saved)
- [ ] Preview screenshots (desktop, mobile): none taken

## Categories
- Primary Expert Advice, set explicitly with the field-map method, not left to list order.
- Secondaries Wedding Tools (listing /blog/wedding-tools exists) and Planning Guides (no /blog/ listing in link-map.csv; nearest is Wedding Planning at /blog/wedding-planning) come from 01-brief.json and are **not confirmed** against the live CMS category list. Match them to real CMS categories; do not create new ones.
- The live on-page breadcrumb reads Home > Blog > Expert Advice; the schema breadcrumb is Home > Expert Advice > post. Match the template if it adds the Blog level.

## Images (4 slots needed, licensed only)
Place by the IMAGE SLOT comments in `11-body.md`:
- `featured`: featured and OG image; couple reviewing replies, screen not legible, model release.
- `welcome-dinner`: under "Separate RSVPs for each event"; licensed real photo, venue and town recorded, consent; never AI.
- `qr-invitation`: end of the QR code section; owned or licensed photo preferred. AI still life only if Nic approves, placeholder code, captioned "Illustrative image".
- `studio-rsvp-screen`: under "Where Wonderland Studio fits"; **the team needs to supply a Wonderland Studio RSVP screenshot with sample names only.**

No third-party platform screens or logos in any slot. Alt text is drafted from the shot briefs; rewrite to match the final images. Do not publish with `[[IMAGE NEEDED]]` captions.

## Flags for Nic
- No prices in the post, so nothing for price sign-off. Please confirm the Wedded Concierge lines and the magazine link.
- Approve or decline an AI illustrative still life for qr-invitation only.

## Open items before publish
- Author: Mark Tuason or Yash.
- Live URL still /wedding-rsvp-website after Save Draft; if moved, 301 confirmed before publish.
- [[VERIFY licence]] and [[VERIFY credit]] for every image.
- Confirm `/expert-advice/wedding-rsvp-wording` resolves (linked in the body; seen only via a site map, not in link-map.csv).
- Confirm `/how-to-manage-wedding-rsvps` 301s to `/expert-advice/wedding-rsvp` (the body links the final URL).
- Show the updated date on the page (search_visitor noted none is shown); set datePublished/dateModified at publish.
- booking-checklist.md has no page on the site, so it is not linked from the post (backlog suggestion only).

## Legal note
The privacy points (OAIC) and QR code points (Australian Cyber Security Centre) in the post and the checklist are general information as at November 2026, not legal advice. The body says so at the top of the privacy section and links the official sources at each claim.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-rsvp-website`.
