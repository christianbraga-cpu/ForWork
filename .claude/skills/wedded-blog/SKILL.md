---
name: wedded-blog
description: Run the full Wedded Wonderland blog pipeline from a title, keyword and target audience to a CMS Draft. Use when the person types /wedded-blog title="..." keyword="..." audience="..." (or resume=<slug>), or asks to write a blog post for Wedded Wonderland.
---

# /wedded-blog: orchestrator

You are the **managing editor**. You don't write the post yourself: you run each specialist subagent (Agent tool, `subagent_type` = the agent name), check their envelopes, route questions, enforce gates and keep the run moving. The run is **fully automatic to Draft**: don't pause to ask the person anything unless a stop condition is hit.

## 0. Start
1. Parse `title`, `keyword`, `audience` from the arguments. If one is missing, ask for it once (that's the only question allowed).
   - `resume=<slug>`: read `run-log.md` in that folder and continue from the first stage whose file is missing or not `complete`.
2. Slug: lowercase keyword, hyphens, `a-z0-9-` only (e.g. `amalfi-coast-villa-wedding`). If the folder exists and isn't a resume, add `-2`.
3. Create `content/posts/<slug>/` with `02-research/pages/`, `07-icp/`, `images/src/`, `reference-only/`, `screenshots/`.
4. Write `00-input.json`: `{title, keyword, audience, slug, started: <ISO date>}`.
5. Check freshness: if `content-system/seo/link-map.csv` rows have `last_seen` older than 7 days, or fewer than 100 rows, run the `/wedded-linkmap` steps first (read `.claude/skills/wedded-linkmap/SKILL.md`).
6. Start `run-log.md` with a line per event: `HH:MM stage agent status note`.

## 1. Run the stages

For every subagent call, the prompt must include: the slug, the post folder path, the files to read, the file to write, and "Follow your agent instructions and CLAUDE.md". After each call, **read the output file** and check:
- File exists and `python3 -I content-system/scripts/validate.py content/posts/<slug>` reports no problems for it
- `status` is `complete` (handle others below)
- `self_qa.confidence` (log anything < 0.7 for the report)
- `open_questions`: send each to the agent named in `to` (one extra call), then rerun the asking agent if the question was `blocking`

| Step | Agent | Writes | Gate (see `content-system/rubrics/qa-gates.md`) |
|---|---|---|---|
| 1 | `content-strategist` | `01-brief.json` | G1 |
| 2 | `seo-researcher` | `02-research/*`, `02-seo.json` | G2 |
| 2b | `content-strategist` (second pass) **only if** `02-seo.json` `recommended_scope` differs from the brief's `regional_scope` or there's cannibalisation | updated `01-brief.json` | G1 |
| 3+4 | `planner-sme` **and** `visual-curator` **in parallel** (two Agent calls in one message). **List articles (5+ venues):** instead run `planner-sme` as up to 3 parallel batches (general facts → `03-source-pack.json` with fact_01 to fact_099; venue batch n → `03-source-pack-part-<n>.json` with fact_<n>00 to fact_<n>99), then `python3 -I content-system/scripts/merge_source_packs.py content/posts/<slug>` | `03-source-pack.json`, `04-images.json` | G3, G4 |
| 5 | `luxury-writer` | `05-draft.md` | **Send the first draft to the person straight away** (SendUserFile, render) with a 3-line note; the rest carries on |
| 6 | `editor` on the latest draft | `06-edit.json` | G5 |
| 7 | `icp-reader` × 5 **in parallel**, one per `content-system/personas/*.yaml`; arrival context = "a Google search for '<keyword>'" (search_visitor, planner_couple, sceptic), "a link your daughter sent you" (funding_parent), "a link your assistant shortlisted" (uhnw) | `07-icp/<persona_id>.json` | – |
| 7b | `icp-panel-chair` | `07-panel.json` | G6 |
| 8 | `luxury-writer` → `08-final.md` (with panel fixes if `revise`) | `08-final.md` | – |
| 8b | `editor` blocking-issue check on `08-final.md` (only if the panel said `revise`) | `06-edit-final.json` | blocking issues = 0 |
| 9 | `cro-specialist` | `09-cro.json` | – |
| 10 | `distribution` | `10-distribution.json` | – |
| 11 | `cms-publisher` | `11-publish-package.json`, `12-cms-report.md` | G7, G8 |

### Loops
- **Editor (G5):** `revise` → writer applies `edits` to make `05-draft-r2.md` → editor round 2 (rename previous `06-edit.json` to `06-edit-r1.json`). Still failing after round 2 → **stop**. `pass_with_edits` → writer applies edits once, no re-score.
- **Panel (G6):** `revise` → writer makes `08-final.md` with must_fix + should_fix → editor blocking-issue check. No second panel round. If must_fix items need facts, run `planner-sme` once for just those items first.
- If `planner-sme` or `visual-curator` returns `needs_input`, rerun once with the missing input; then continue with `[[VERIFY]]` / `needed` placeholders rather than stopping (the run is automatic).

### Fast mode (default; target about 45 minutes)
Measured on the ring-settings run: about 25 minutes to a finished package. Use it unless the person asks for a full run.
- **After the brief, run 02, 03 and 04 in parallel.** The brief must name the list items or must-includes so `planner-sme` can start without the outline; the writer merges both.
- **Lean SERP:** 5 cities, one per region (Sydney, Melbourne, New York, Dubai, Singapore). Read the Sydney top 3 plus any page in the top 3 of 2+ cities. No Arabic queries, ranked keywords or GSC unless the topic needs them.
- **Time budgets in every prompt:** brief 5 min, SEO 10, facts 15 (save as you go), images 8, draft 8, final 7, each check 5. Over budget → save and finish; gaps become "not published" or `[[VERIFY]]`, never more searching.
- **Editor and the 5 readers run in parallel** on the first draft. The orchestrator applies the editor's exact `old`/`new` edits itself (`05-draft-r2.md`), then the panel chair merges the reader feedback, noting what the editor already fixed.
- **One combined final pass** by the writer, then the blocking check, CRO and distribution **in parallel**. The orchestrator applies CRO's exact copy changes and any one-sentence blocking fixes itself.
- Legal or venue-list articles may still need the full planner budget (about 25 to 35 min); give the planner the sister post's source pack to re-check when one exists.

### Keep it moving
- Run every stage in the background and check in when it reports. If a stage hasn't reported within 20 minutes of its usual time, check whether it's waiting on a permission prompt or stuck, and tell the person in one line.
- Business answers the person has confirmed live in `content-system/brand/brand-facts.md` under "Confirmed business answers". Tell the panel chair that anything listed there or listed as "deferred" is not a must-fix.

### Stop conditions (write the report, then end)
- A gate fails after its allowed retries
- `seo-researcher` returns `blocked` (no SERP source at all)
- Any agent returns `blocked`
- `cms-publisher` reports a login screen or a field-map mismatch (the package is still saved)

## 2. Finish
1. Update `content-system/seo/link-map.csv`: add the new post (`path` from `02-seo.json` `url_path` or `/<slug>`, type, title, `primary_keyword`, `noindex` = `draft`, notes "Draft <date>").
2. Write `backlinks-todo.md` from `02-seo.json` `backlinks_to_add` using `content-system/templates/backlinks-todo.md`.
3. Write `13-run-report.md` from `content-system/templates/run-report.md`: gates and rounds, the booking checklist (from `BOOKING CHECKLIST:` assumptions), every `[[VERIFY]]` (collect from all envelopes' `verify_items` + scan `08-final.md`), Nic sign-off prices, images needed, low-confidence stages, panel highlights, research summary, tools used, draft link.
4. Add a row to `content/calendar.csv` (status `draft`, slug, date).
4b. Make the Word version for human review: `node content-system/scripts/md_to_docx.js content/posts/<slug>/11-body.md content/posts/<slug>/<slug>-draft.docx content/posts/<slug>/11-publish-package.json`, and send it to the person as a download along with the run report.
5. Run the validator one last time and include its result in the report.
6. Commit the post folder and link map on the current branch with a message like `Add draft: <title>` and push (follow the session's git instructions).
7. Reply to the person in under 15 lines: status, draft link or package location, the top `[[VERIFY]]` items, prices to sign off, images needed, and the path to `13-run-report.md`.
