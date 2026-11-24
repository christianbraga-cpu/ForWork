# Stage 12 CMS report: wedding-guest-list-template (REFRESH)

**Draft URL/ID:** not uploaded. Package only, as instructed: no browser tool in this cloud session, no login was attempted and the CMS was not touched. `content-system/cms/field-map.md` also says `Status: NOT YET MAPPED` (not confirmed). Nothing was saved, published or scheduled.

**Status:** Draft only. A human clicks Publish.

## URL WARNING (read before saving)
- **Keep URL https://weddedwonderland.com/wedding-guest-list-template and slug `wedding-guest-list-template`. Do not change them. No redirect is planned.**
- The CMS category bug has moved earlier refreshes, including **/wedding-rsvp-website to /expert-advice/wedding-rsvp-website**.
- Primary category stays **Expert Advice**, the live page's category. Set it explicitly with the field-map method, not by list order alone.
- **After Save Draft, check the URL is still exactly `/wedding-guest-list-template`.** If it has moved (for example to `/expert-advice/wedding-guest-list-template`), **do not publish until a 301 from `/wedding-guest-list-template` to the new path is confirmed.** Check again at publish.

## Upload the spreadsheet (web team, before publish)
1. Upload `content/posts/wedding-guest-list-template/download/wedding-guest-list-template.xlsx` as a **public, no-sign-up file** (no email gate, no UTM on the file link).
2. Confirm the final URL and replace the placeholder `/downloads/wedding-guest-list-template.xlsx` in the body. It is the bold link straight after the intro, marked by the `<!-- DOWNLOAD: ... -->` comment in `11-body.md`.
3. Add a **download analytics event** on the link (for example `file_download` with the file name and page slug) and check it fires.
4. Test the download logged out on desktop and mobile; check the file opens in Excel and imports into Google Sheets (File, then Import, Create new spreadsheet).

Do not publish with the placeholder URL.

## Package
- `content/posts/wedding-guest-list-template/11-publish-package.json` (stage 11, status draft, validates)
- `content/posts/wedding-guest-list-template/11-body.md` (08-final.md wording unchanged; front matter, META comments, H1 and 8 fact markers removed; 4 IMAGE SLOT comments and the DOWNLOAD comment kept; inline links and UTMs kept; no [[VERIFY]] markers in the body)
- `content/posts/wedding-guest-list-template/booking-checklist.md` (guest list set-up, destination travel and privacy checklists; column names match the .xlsx; no Advisor role in the guest list, guest travel or visas)
- H1 and meta title: Wedding Guest List Template for Google Sheets and Excel (55 chars)
- Meta description (from the 08-final.md META comment, 152 chars): Download our wedding guest list template for Google Sheets or Excel with no sign-up. Every column explained, including flights, hotels and visa letters.
- Excerpt: 246 chars, no figures, no "free".
- Focus keyword: wedding guest list template. Canonical: https://weddedwonderland.com/wedding-guest-list-template. OG image: featured slot.
- Categories: Expert Advice (primary, set explicitly), Planning Guides. Tags: wedding planning, templates, wonderland studio, guest list, destination weddings.
- Key takeaways: 4. FAQ: 6 pairs. Schema: Article, BreadcrumbList (Home > Expert Advice at /blog/expert-advice > post), FAQPage; datePublished left empty.
- CTAs (from 09-cro.json, already inline; 08-final.md has no `<!-- CTA: primary -->` marker): primary Wedded Concierge (end of "Destination wedding columns"), secondary and magazine link ("When a spreadsheet stops being enough"), closing ("Planning the weekend around your guests"). All utm_campaign=wedding-guest-list-template.
- No prices anywhere in the post or checklist, so nothing for Nic's price sign-off.

## Remove from the old post
None of these may survive in the CMS entry (body, old blocks, excerpt, SEO fields, image alt text):
- The copy-and-paste table used as the "template"
- The sample rows with names, street addresses and email addresses
- Decline percentages (10% to 20%) and thresholds ("six weeks", "roughly 100 guests")
- The A/B/C tier rules and "invite A and B first"
- The old Wonderland Studio feature claims (city and country fields, arrival and leaving times, import, seating and menu sync, "all eleven planning tools")
- The "Join Wedded Concierge" button wording and the three-bullet Concierge box
- "Free" in the H1 and intro, and the old title "Wedding Guest List Template: Free Sheets, Excel, PDF"

The new body contains none of these (checked by scan; "%" appears only inside IMAGE SLOT comments as zoom levels).

## Checklist (publish-checklist.md)
- [ ] Field map CONFIRMED: no (NOT YET MAPPED)
- [x] 11-publish-package.json validates; primary_category == categories[0] (Expert Advice)
- [ ] Images prepared with alt and caption: not done, all 4 slots `needed`
- [ ] Logged into CMS: not checked (package-only run, no browser)
- [ ] Spreadsheet uploaded as public no-sign-up file, URL replaced, download event added: not done (web team)
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
- [ ] URL still /wedding-guest-list-template after save: not checked (nothing saved)
- [ ] Preview screenshots (desktop, mobile): none taken; `screenshots/` is empty

## Categories
- Primary Expert Advice, set explicitly, not left to list order.
- Secondary Planning Guides comes from 01-brief.json and is **not confirmed** against the CMS (no /blog/planning-guides in link-map.csv; nearest is Wedding Planning at /blog/wedding-planning). Match it to a real CMS category; do not create a new one.
- The live breadcrumb reads Home > Blog > Expert Advice; the schema breadcrumb is Home > Expert Advice > post. Match the template if it adds the Blog level.

## Images (4 slots needed)
Place by the IMAGE SLOT comments in `11-body.md`:
- `featured`: featured and OG image. **Team** screenshot of the .xlsx with placeholder names only.
- `destination-columns`: under "Destination wedding columns". **Team** crop of the eight Destination travel columns with placeholder names.
- `couple-planning`: in "Filling it in by household". **Licensed real photo with a signed model release for both people; never AI.** Licence and credit recorded in library-index.csv before use.
- `studio-guest-list`: in "When a spreadsheet stops being enough". **Team** Wonderland Studio screenshot with sample names only.

No third-party logos, no real guest data. Alt text and captions are drafted; rewrite to match the final images. Do not publish with `[[IMAGE NEEDED]]` captions.

## Flags for Nic
- No prices in the post, so nothing for price sign-off. Please confirm the Wedded Concierge lines and the magazine link.
- Source and approve the licensed couple-planning photo.

## Open items before publish
- Author: not recorded in stages 01 to 10; team to confirm the byline and make the author meta tag match.
- URL still /wedding-guest-list-template after Save Draft; if moved, 301 confirmed before publish.
- Spreadsheet uploaded, final URL in the body, download event live.
- [[VERIFY licence]] and [[VERIFY credit]] for the couple photo; the three team screenshots supplied.
- Planning Guides matched to a real CMS category.
- The Studio sentence "Replies, plus-ones and dietary notes arrive straight into Wonderland Studio's guest list" was accepted at final check as the /wonderland-studio page's own wording; confirm it still matches that page at publish (09-cro raised it).
- Show the updated date on the page; set datePublished/dateModified at publish.

## Legal note
Privacy points (OAIC) are general information as at November 2026, not legal advice; the body says so in the privacy section. Visa letters: each guest checks with the destination's embassy or consulate (Smartraveller). Nothing in the post, package or checklist says or implies that the Wedded Advisor manages the guest list, guest travel or visas.

## Mismatches
- None checked on screen: package-only run, and the field map is not confirmed. To upload, run `/wedded-cms-discovery` in a logged-in Chrome tab, then `/wedded-blog resume=wedding-guest-list-template`.


## Update 2026-11-24: download hosted on Google Drive
The web team could not host the file in time, so the author put it on Google Drive (work account, Anyone with the link, Viewer). The body now links https://drive.google.com/uc?export=download&id=1sFcupK6ddDkXDAMxbIwqRG-vsYahUO2z and the DOWNLOAD comment is removed. Earlier upload steps above are superseded. Test the link in a private window before publishing.
