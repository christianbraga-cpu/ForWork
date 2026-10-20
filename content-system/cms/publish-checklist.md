# CMS publish checklist (cms-publisher, every run)

Before upload
- [ ] `cms/field-map.md` status is CONFIRMED
- [ ] `11-publish-package.json` validates; `primary_category == categories[0]`
- [ ] All approved images prepared (WebP, size limits, alt, caption)
- [ ] The person is logged into the CMS in the Chrome tab (never ask for a password)

Upload
- [ ] Images uploaded first; media IDs recorded
- [ ] Featured image set
- [ ] Title, slug, excerpt, author
- [ ] Body with inline images in the right slots
- [ ] Key Takeaways block at the top (after intro)
- [ ] CTA block(s) at the agreed placement, UTM links
- [ ] FAQ block
- [ ] Categories assigned, then **primary category set explicitly** to categories[0]
- [ ] Tags
- [ ] SEO fields: meta title, description, focus keyword, canonical, OG image
- [ ] Schema JSON-LD (if the CMS has a field)
- [ ] Internal draft note: [[VERIFY]] list + Nic sign-off list + `[[IMAGE NEEDED]]` slots
- [ ] **Save Draft** (never Publish / Schedule)

After save
- [ ] Open preview; screenshot desktop and mobile into `screenshots/`
- [ ] Check: every image loads, every link resolves, CTA visible, breadcrumb shows the primary category
- [ ] Record the draft URL/ID in `12-cms-report.md`
