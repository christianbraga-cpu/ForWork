# CMS handoff: {page title}

Page: {live URL}
Action: {optimise | refresh | create}
Run: {run_id}
Prepared: {date}
Gate result: {passed | passed with accepted majors (see decisions.md)}

This file is what you take to the CMS. Apply the changes yourself, or paste the
prompt in Part A into the Claude in Chrome extension with the CMS editor open
for this page. Part B is the full change list the prompt refers to.

---

## Part A: prompt for Claude in Chrome

Copy everything between the lines into the extension.

---------------------------------------------------------------------------

You are editing one page in our custom CMS, in the tab I have open. Apply the
changes listed in the CMS handoff file below, exactly as written.

Rules:
1. Before changing anything, copy the current content of every field or
   section you will edit and show it to me, so I have a backup.
2. Make the changes in the order listed. For each change, find the field or
   section by the "Where" description, check that the "Current" text matches
   what is there now, then replace it with the "New" text. If the current text
   does not match, stop and tell me. Do not guess.
3. Do not change anything that is not on the list.
4. Keep the page as a draft or unpublished. Do NOT click publish, update live,
   or save to the live page. When all changes are in, stop and tell me they are
   ready for my review.
5. If the editor removes or rewrites code (scripts, schema markup, form
   attributes, meta tags), stop and tell me which change it affected.
6. When finished, list each change number with "done", "skipped" or "problem",
   plus a reason for anything not done.

{paste Part B here, or attach this file}

---------------------------------------------------------------------------

## After publishing (you or the extension)

1. Open the live page and check that every change in Part B appears.
2. Confirm the robots setting: {keep noindex | remove noindex (all facts signed off)}.
3. Send the live URL back to Page Studio. It runs `check_page.py` on the live page to
   confirm the schema, the form routing, links and meta all survived the CMS.
4. If anything is broken, restore from the backup from step 1 of the prompt.

---

## Part B: change list

Summary: {n} changes ({n} meta, {n} copy, {n} structure, {n} images, {n} code).
Still blocked on sign-off: {list of fact ids and owners, or "nothing"}

Each change uses this format:

### Change {n}: {short name}
- **Type:** meta | copy | structure | image | link | code (schema, form, tracking)
- **Where:** {CMS field name, or section heading and position on the page}
- **Current:** {exact current text or code, or "none (new)"}
- **New:** {exact new text or code}
- **Why:** {finding id and one-line reason, e.g. "SEO-R1-F3: primary keyword missing from H1"}
- **Depends on sign-off:** {fact id and owner, or "no"}
- **Check after:** {what to look for on the live page}

{repeat for every change, ordered: meta first, then copy top to bottom, then
images, then links, then code}

---

## Outside this run's scope

Issues found that are not copy (copy-scope runs only). Nothing here was changed:
- {finding id, issue, suggested fix}

---

## Part C: do not change

Things on the current page that Page Studio reviewed and decided to keep, so
nobody "fixes" them by accident:
- {item and reason}
