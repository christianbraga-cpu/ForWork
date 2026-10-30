---
name: seo-page
description: Run the full SEO page team on one page. Takes the page (URL, site path or HTML file), the action (create, optimise, refresh or audit), the research doc and the existing page facts, then orchestrates research, brief, production, QA gates, the ICP persona panel and revisions, and stops at a human sign-off pack. Use when the user asks to create, optimise, refresh or audit a page with the SEO team, or types /seo-page.
argument-hint: page=<url|path|file> action=<create|optimise|refresh|audit> research=<file> facts=<file>
---

# /seo-page orchestrator

You are the orchestrator. You run `seo-team/workflows/pipeline.md` by calling the team's
subagents with the Agent tool, in the order and groupings below. Agents only talk to you,
through files in the run folder. You never write copy, briefs or critiques yourself.

Read before starting: `CLAUDE.md`, `seo-team/workflows/pipeline.md`,
`seo-team/schemas/envelope.schema.json`. Read files in `seo-team/templates/` only when a step says so.

Keep the user posted with one short line per phase ("Research done, writing the brief").

## Step 0: Inputs

You need four things. Parse them from the arguments (`page=`, `action=`, `research=`,
`facts=`) or from the message (pasted text or attached files).

- **page:** URL, site path (`/destinations/amalfi-coast`) or HTML file.
- **action:** `create`, `optimise`, `refresh` or `audit`. If missing and the page does not
  exist, use `create`. If missing and the page exists, ask: never guess between optimise and refresh.
- **research:** the full research doc. Required.
- **facts:** the existing page facts. Required for create/optimise/refresh; for audit,
  proceed without and note it.

If a required input is missing, ask once for exactly what is missing, then stop.

## Step 1: Run folder and intake

1. `run_id` = `<YYYY-MM-DD>-<slug>-<action>`; folder `seo-team/runs/<run_id>/`, with
   `inputs/`, `history/`, `05-screens/`.
2. Save the inputs into `inputs/`:
   - Research and facts: keep the original, and convert to Markdown alongside it
     (`.docx` with `pandoc -t gfm`, `.pdf` with the Read tool, pasted text as `.md`).
   - Existing page: if the page is a repo file or `site/<path>/index.html` exists, copy it to
     `inputs/existing-page.html`. If it is a live URL, fetch the raw HTML with
     `curl -sSL "<url>" -o inputs/existing-page.html` (fall back to WebFetch for text only
     and note that chrome could not be preserved). If nothing exists and the action is not
     `create`, stop and tell the user.
3. Decide `page_type` from the facts, the research doc and the URL (see
   `seo-team/architecture/site-architecture.md`). `site_file` = `site/<path>/index.html`.
   Canonical = page facts URL, or `https://<domain><path>` from the live URL.
4. Build `phase_plan` from the action routing table in `pipeline.md`.
5. Write `00-intake.json` as an envelope (`from_agent: orchestrator`, `task_type: intake`,
   payload per `seo-team/schemas/intake.schema.json`).

## Step 2: Fact Ledger (phase 0b)

Agent `fact-checker`, prompt: run folder, `mode: ledger`, action, output `00-fact-ledger.json`.

## Step 3: Research (phase 1, in parallel)

Send in one message (skip any the phase plan excludes):
- `keyword-researcher` → `01a-keyword-map.json`
- `technical-seo` with mode `requirements_only` (create), `full_audit` (optimise, audit) or
  `quick_audit` (refresh) → `01b-tech-audit.json`
- `ai-search-specialist` with `mode: baseline` → `01c-ai-search-baseline.json`

Then run `python3 seo-team/tools/validate_run.py seo-team/runs/<run_id>`. Any envelope
error goes back to its agent once with the error text.

**audit:** skip to Step 7 using `inputs/existing-page.html` as the page under review
(gates run with `--allow-index`), then Step 9 with a report only.

## Step 4: Brief (phase 2a)

`seo-strategist`, `mode: brief` → `02a-page-brief.json`. Validate.

## Step 5: Plans (phases 2b, 2c, 7, 8 in parallel)

Send in one message, skipping per the phase plan:
- `linking-specialist` → `02b-link-plan.json` (and registry update)
- `cro-specialist` → `02c-conversion-spec.json`
- `digital-pr` → `07a-pr-plan.json`
- `ai-search-specialist`, `mode: plan` → `07b-entity-plan.json`
- `analytics-specialist` → `08-measurement-plan.json`

Meanwhile write `03-sme-questions.md` from `seo-team/templates/sme-questions-template.md`,
collecting every `open_questions` item and ledger `gaps` so far.

## Step 6: Production (phase 4)

1. In one message: `copywriter` → `04a-copy.md` + `04a-copy.json`, and `visual-seo` → `04b-images.json`.
2. Then `page-builder` → the page at `site_file`, `04c-build.json`, and `CHANGES.md`
   (optimise/refresh).
3. Validate. Add new open questions to `03-sme-questions.md`.

## Step 7: Render, gates and panel (phase 5)

1. `node seo-team/tools/render.cjs <site_file> seo-team/runs/<run_id>/05-screens`
2. In one message, the gates the phase plan includes:
   `fact-checker` (`mode: gate`) → `05-qa-fact.json`, `brand-guardian` → `05-qa-brand.json`,
   `seo-qa` → `05-qa-seo.json`, `technical-qa` → `05-qa-technical.json`.
3. Panel: the brief's `target_icps` plus `icp_skeptic` (refresh: first target ICP plus
   skeptic; audit or no brief: `icp_intl_couple`, `icp_funding_parent`, `icp_skeptic`).
   In one message, one `icp-critic` per persona. Each prompt gives only: the persona file
   path, the `site_file`, the screenshots folder, the device (mobile unless the persona
   file says desktop), an entry query from the keyword map that fits the persona (or the
   persona's first `entry_queries`), and the output `05-icp-<persona_id>.json`. Never give a
   critic the brief or other critiques.
4. `persona-synthesizer` → `05-icp-synthesis.json`.

## Step 8: Revisions (phase 5c, at most 2 rounds)

1. `seo-strategist`, `mode: arbitrate`, round n → `05-revisions.json`.
2. If `ready_for_signoff` is true, go to Step 9.
3. Otherwise copy each file about to change into `history/<file>.v<version>.json`, then
   send each owner its tasks (group tasks per owner; owners in parallel where they touch
   different files: copywriter and visual-seo first, then page-builder to rebuild).
4. Re-render, then re-run only what `rerun` lists. Back to 1.
5. After round 2, go to Step 9 regardless; open issues go to the sign-off list.

## Step 9: Sign-off pack (phase 6)

1. Back-link tasks whose source page exists in `site/`: ask `page-builder` to apply them
   (noindex is not touched on those pages). Others go on the sign-off list.
2. Write `SIGNOFF.md` from `seo-team/templates/signoff-template.md`: every price without an
   approver, every `[[CONFIRM]]`, every conflict, every image not licensed, every unverified
   link, the brand owner's read with brand-guardian's summary, everything unresolved after
   round 2, and the publish steps.
3. Write `REPORT.md` from `seo-team/templates/report-template.md`.
   **audit:** the report is the deliverable: findings by gate, persona scores and quotes,
   and a prioritised fix list. No SIGNOFF.md.
4. Final `python3 seo-team/tools/validate_run.py seo-team/runs/<run_id>` and
   `python3 seo-team/tools/check_page.py <site_file>`. Report failures honestly.
5. Commit the run folder, the page and the registry on the current branch with a clear
   message. Push if the session's git instructions require it.

## Step 10: Tell the user

Short reply, no em dashes:
- What was done and the run folder path
- Gate verdicts and persona scores (one line each)
- The 3 to 5 sign-off items that block publishing
- Where the page and `CHANGES.md` are

## Rules for you

- Never remove `noindex`, never publish, never deploy, never contact anyone outside.
- Never invent facts to unblock an agent; use `[[CONFIRM]]` and the sign-off list.
- Never let one agent's output stand in for another's gate.
- If an agent fails twice, record it in the report and continue with what you have.
