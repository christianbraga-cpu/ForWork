---
name: wedded-cms-discovery
description: One-time mapping of the custom CMS blog editor into content-system/cms/field-map.md so the cms-publisher can upload drafts. Use when the person types /wedded-cms-discovery or the field map is not confirmed.
---

# /wedded-cms-discovery

## Before starting
- A browser tool must be available (Claude in Chrome, or the remote-devices browser). If not, explain the options in `content-system/connectors/README.md` (Claude in Chrome section) and stop.
- Ask the person to **open the CMS and log in themselves** in Chrome, then open the "new blog post" screen. **Never ask for or type credentials.**

## Steps
1. Run the `cms-publisher` agent in **discovery mode**. Tell it the field map path and that it must not save anything in the CMS.
2. It reads every field on the new-post screen and fills `content-system/cms/field-map.md`, including:
   - how the body is edited (blocks, rich text, HTML/markdown)
   - where images go and how alt/caption are set
   - the category control and **exactly how the primary category is chosen**
   - SEO fields, schema field (if any), CTA/takeaways/FAQ blocks, the draft and preview buttons
   - a place for the internal draft note
3. Show the person the filled table and ask them to confirm or correct it. When they confirm, change the status line to `Status: CONFIRMED` and commit.
