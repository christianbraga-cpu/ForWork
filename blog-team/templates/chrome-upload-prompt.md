# Claude in Chrome: CMS upload prompt (template)

The copy-editor fills every `{{...}}` from `publish-package.json` and saves the
result as `articles/<slug>/chrome-upload-prompt.md`. Paste it into the Claude
side panel in Chrome while logged in to the CMS. Upload the images to the media
library first if direct uploads are unreliable.

---

Open {{CMS_URL}} in a new tab. Create a new post with the details below.
Work carefully and do not click Publish.

1. **Title:** {{title}}
2. **Slug / permalink:** {{slug}}
3. **Body:** paste the article below. Convert headings to Heading blocks (H2,
   H3), bullet lists to List blocks, and FAQ to the FAQ block if the site has
   one. Replace each `[IMAGE: slot]` line with that image (see step 6).
4. **Key Takeaways:** insert the reusable "Key Takeaways" block right after the
   intro paragraph, with these bullets:
{{key_takeaways_bullets}}
5. **CTA:** insert the reusable CTA block "{{cta.id}}" at the end of the
   article. Heading: "{{cta.heading}}". Body: "{{cta.body}}". Button:
   "{{cta.button}}" linking to {{cta.url}}.
6. **Images:** from the media library, insert these files where their slot
   marker is. Set alt text and caption exactly as given. Set
   {{featured_image}} as the featured image.
{{images_table}}
7. **Categories:** tick {{categories_list}}. Then set **{{primary_category}}**
   as the primary category using the "Make primary" control (Yoast or
   RankMath). Ticking order does not set the primary.
8. **Tags:** {{tags}}
9. **Excerpt:** {{excerpt}}
10. **SEO fields:** SEO title "{{seo_title}}". Meta description "{{meta_description}}".
11. **Author:** {{author}}
12. **Save as draft. Do not publish.**

Then open the preview and check: every image loaded and has alt text; every
link works; the Key Takeaways and CTA blocks are present; the breadcrumb shows
{{primary_category}}; the SEO fields are filled. Take a desktop and a mobile
screenshot. List anything that did not work.

---

## Article body

{{body_markdown}}
