---
name: page-studio
description: Run the Wedded Wonderland page team on one page. Use when the user gives a page (URL, repo path or new path), an action (create, optimise, refresh, audit), a research doc and existing page facts, or says "run page studio", "optimise this page", "build this package page". Orchestrates the specialist agents in .claude/agents through brief, research, architecture, content, design, build, QA and publish-package stages.
---

# Page Studio (Project Lead)

You are the Project Lead. You do not write copy, design or code yourself. You
brief the specialist agents, route their handoffs, enforce the QA gates, and
assemble the final package. Read `studio/README.md` once if you have not this
session, then follow this file.

## 0. Intake

The user gives four inputs. Collect them before anything else.

| Input | Accept | If missing |
|---|---|---|
| Page | Live URL, repo path, or new URL path | Ask |
| Action | `create`, `optimise`, `refresh`, `audit` | Ask |
| Research doc | Drive link or name (Google Drive connector), Notion link (Notion connector), repo path, pasted text | Ask |
| Existing page facts | Table, sheet, pasted list | Ask. For `create` with no facts yet, the user may say "none"; every fact is then `unconfirmed` |

Optional: `mode` (`fast` or `full`) and `scope` (`copy` or `full`). If not given, use
`config.default_mode` and `config.default_scope` for the action. Do not ask anything else unless a stage is blocked. Defaults live in
`studio/config.json`.

Then:
1. Derive `slug` from the page path (last segment) and `run_id` = `<slug>-<YYYYMMDD-HHMM>`.
2. Create `studio/runs/<run_id>/` and write `00-intake.md` with the four inputs
   verbatim (fetch the research doc and save it as `research-doc.md` in the run folder).
3. Write `facts.json` from the existing page facts using
   `studio/schemas/payloads/fact_ledger.schema.json`. Every fact gets an id (`F001`...).
4. For `optimise`, `refresh` and `audit`: capture the current page. Live URL:
   fetch the HTML (WebFetch, or Firecrawl scrape through the Lead_MCP connector) into
   `current.html`. Repo path: copy it to `current.html`.

## Stage plan by action

| Stage | create | optimise | refresh | audit |
|---|---|---|---|---|
| 1 Research | full | full | facts + SERP only | full |
| 2 Architecture | full | full (diff against current) | skip unless facts change structure | full, report only |
| 2b Persona review of brief | yes | yes | no | no |
| 3 Content + visuals | full | changed sections | changed facts only | no |
| 3b Persona review of copy | yes | yes | no | no |
| 4 UX / design | full | changed sections | no | review current only |
| 5 Build | full | full | patch | no |
| 6 QA gate | full | full | automated + fact check | automated on current |
| 7 Publish package | yes | yes | yes | audit report only |
| 8 Amplify plan | yes | yes | no | recommendations only |
| 9 Measurement plan | yes | yes | no | baseline only |

## Mode: `fast` (the default for `optimise`, `refresh` and `audit`)

Target: the final copy and the Word handoff within **60 minutes** of intake. The mode
comes from `config.default_mode`; the user can say "full mode" to get the full pipeline
below instead (the default for `create`). Fast mode always uses `scope: copy`.

Before starting, read `studio/brand-answers.md` (approved business answers; use only rows
with Status `approved`) and the facts library (`studio/facts-library/general.json` and the
destination's file, if any).

| Step | Budget | What runs |
|---|---|---|
| F0 Intake | 5 min | The 4 inputs. Save the research doc and the live copy (DataForSEO `on_page_content_parsing` if the site is blocked). Build `facts.json`: the user's page facts, plus every library fact whose `reverify_after` is in the future (keep its status), plus the research doc's sourced facts as `unconfirmed`. |
| F1 Fact delta | 10 min | One `fact-checker` call, checking only: legal and visa lines, prices and fees, capacities, and expired library facts. Everything else from the research doc stays `unconfirmed` and is hedged or held. No SEO or GEO refresh if the research doc is under `config.fast.research_refresh_if_doc_older_than_days` old. No separate brief: the research doc's section plan is the brief. |
| F2 Copy | 15 min | One `copywriter` call writing straight from the research doc's section plan, with `studio/standards/copy-limits.json`, the standing button and form rules in this file, `brand-answers.md`, and the decisions template below. Same `page_copy` format and sign-off pairs. |
| F3 Parallel review | 10 min | All at once: `fact-checker` on the copy, `qa-reviewer` with the SEO lens, `qa-reviewer` with the brand-voice lens, and `persona-reader` once for each of up to 4 personas (primary, AU home market, one more by fit, and the skeptic). Also run `python3 studio/tools/check_copy.py`. Personas do not raise items listed as pending in `brand-answers.md`; those go straight to the user's question list. |
| F4 One revision | 10 min | One combined fix list (fact blockers, then copy-check failures, persona issues, SEO, brand) and one `copywriter` revision. Re-run `check_copy.py` and a quick `fact-checker` pass only if there was a fact blocker. No second round: what remains goes to the user. |
| F5 Handoff | 5 min | `node studio/tools/handoff_docx.js <run> <run>/<Page>-CMS-Handoff.docx`, plus `CMS-HANDOFF.md`, NOTES.md and SUMMARY.md. Add newly verified facts to the facts library. |

Not in fast mode: the persona review of a brief, screenshots and the preview page, the UX
consult (its rules are now in `copy-limits.json` and below), more than one persona run, and
stages 8 and 9 (the amplify and measurement plans can be asked for separately).

Fast-mode standing rules (from the Portugal run):
- Hero: H1, a quick answer of 3 lines, then the buttons, then the one brand sentence (F088 wording).
- Buttons and form: the research doc's exact button labels; the B9 bar fills in the form; hidden
  fields route_to, destination, page_slug, offer, entry_point and the five UTM fields.
- Passport order: the markets with the most demand first (usually US, UK, then AU).
- "Wedded Advisor" about 15 times per page, never in two consecutive sentences.
- Repeat a rule (for example legal steps or beach permits) once in full, then link to it.
- Live pages keep index, follow; lines that need sign-off are held with a fallback (D2 pattern).

If a step goes over budget, carry on but say so in SUMMARY.md, with the reason.

### Scope: `copy` (the default for `optimise`)

Most optimise runs change copy only: headings, body text, meta, FAQ, captions, CTAs
and anchor text. Use `scope: full` only when the user asks for layout, image, form or
code changes. The default comes from `config.default_scope.optimise`.

With `scope: copy`:

| Stage | What runs |
|---|---|
| 1 Research | full (keywords, AI search, fact audit, baseline) |
| 2 Architecture | brief maps the outline onto the **existing** sections. New sections only if research shows a clear gap, each marked `new_section` so the user can decide |
| 2b, 3b Persona reviews | yes |
| 3 Content | copywriter only. Visual lead is skipped, but the copywriter still revises alt text and captions where they are copy |
| 3 Peer reviews | SEO lens and fact-checker on copy. No image review |
| 4 UX / design | skipped. UX gives one consult on copy length and CTA wording only (`review` payload) |
| 5 Build | technical-seo applies the approved copy to a copy of `current.html` as `preview.html` in the run folder. No structural, image or code changes. This exists only so the gate can check and screenshot the result |
| 6 QA gate | `check_page.py` on `preview.html`, brand voice review, final fact pass, persona page review on preview screenshots |
| 7 Package | `CMS-HANDOFF.md` with copy and meta changes only, `CHANGELOG.md`, NOTES.md. No new `index.html` in `site/` |
| 8 Amplify | GEO plan only (it is copy-driven). PR and local are skipped unless asked |
| 9 Measurement | yes |

If research or a review finds a non-copy issue (broken schema, a missing alt
attribute, a form problem), do not fix it. List it in `CMS-HANDOFF.md` under
"Outside this run's scope" with the finding and a suggested fix.

## How to call an agent

Use the Agent tool with `subagent_type` set to the agent name. Every prompt you
send contains:
- `run_dir`: `studio/runs/<run_id>`
- `action` and `page`
- The exact files the agent should read (never paste whole files into the prompt)
- The output file name it must write
- Any review findings it must address (for revisions)

Every agent writes one envelope JSON file (`studio/schemas/envelope.schema.json`)
to the run folder and returns a short summary. After each agent returns, run:

```bash
python3 studio/tools/validate_envelope.py studio/runs/<run_id>/<file>.json
```

An invalid envelope goes straight back to the same agent with the validator
output. It does not go to a reviewer.

Run agents in parallel wherever the table below shows no dependency.

## Stages

### 1. Research (parallel)

| Agent | Writes | Notes |
|---|---|---|
| `seo-strategist` | `10-keyword-research.json` | Semrush + DataForSEO, all markets in config |
| `geo-specialist` | `11-ai-search.json` | DataForSEO AI optimisation tools |
| `fact-checker` | `12-fact-audit.json` | Checks research doc and current page claims against `facts.json` and official sources; adds new facts as `unconfirmed` |
| `analytics-lead` | `13-baseline.json` | Current performance if the page is live, CRM enquiry signals for the destination |

When the fact-checker returns, merge its additions into `facts.json` (you own that file).

### 2. Architecture

`seo-strategist` writes `20-content-brief.json` (payload `content_brief`, with
`link_plan` and `section_outline`). Give it 10 to 13 plus `research-doc.md`.
Then `ux-conversion` consults on the outline (one round), writing
`21-ux-consult.json`. If UX raises blockers, send them back to the strategist once.

### 2b. Persona review of the brief

Pick the personas: the user's choice if given, else every persona in
`studio/personas/` whose `fit.page_types` matches this page, plus `discerning-skeptic`
always. For each persona, call `persona-reader` with the brief only, giving it the
output path `persona/brief-<persona_id>-r<n>.json`. Run each persona
`qa.persona_runs_per_review` times (config), in parallel. Weight personas with
`status: assumption` lower; they never block the gate on their own. Then:

```bash
python3 studio/tools/aggregate_personas.py studio/runs/<run_id> brief
```

That writes `22-persona-brief-summary.json`. Send blocker objections back to the
strategist (one round).

### 3. Content (parallel)

| Agent | Writes |
|---|---|
| `copywriter` | `30-page-copy.json` (payload `page_copy`) |
| `visual-lead` | `31-image-set.json` (payload `image_set`) |

The copywriter reads the brief, `facts.json`, `studio/standards/brand-voice.md`,
`studio/standards/linking.md`. The visual lead reads the brief, `facts.json`,
`studio/standards/images.md`, and any media folder the user gave.

Then peer review in parallel (`qa-reviewer` agent, one call each):
- Copy reviewed by the `seo-strategist` checklist lens → `32-review-copy-seo.json`
- Copy reviewed against facts by `fact-checker` → `33-review-copy-facts.json`
- Images reviewed by the `technical-seo` checklist lens → `34-review-images.json`

### 3b. Persona review of copy

Same as 2b, but with the copy (text only). Then run `aggregate_personas.py <run> copy`.

Send the copywriter one combined fix list: fact blockers first, then persona blockers,
then SEO findings. At most `qa.max_revision_rounds` rounds. After that, you decide
and record the decision in `decisions.md`.

### 4. UX / design

`ux-conversion` writes `40-design.json` (payload `design_spec`): section order,
components, CTA placement, enquiry form spec, mobile behaviour. For pages that
follow an existing template (for example package pages), it must reuse that
template's components (see the reference page in `studio/README.md`).

### 5. Build

`technical-seo` builds the page to `site/<page path>/index.html`, following the
reference page's structure and conventions, and writes `50-build-report.json`.
`analytics-lead` then adds the tracking spec to the page and writes `51-tracking.json`.

### 6. QA gate

Run the automated checks:

```bash
python3 studio/tools/check_page.py site/<page path>/index.html --facts studio/runs/<run_id>/facts.json --brief studio/runs/<run_id>/20-content-brief.json --out studio/runs/<run_id>/60-automated-qa.json
```

Then, in parallel:
- `persona-reader` on screenshots of the built page (mobile and desktop; the
  technical-seo build report lists their paths). Aggregate with `aggregate_personas.py <run> page`.
- `qa-reviewer` with the brand voice rubric → `61-review-brand.json`
- `fact-checker` final pass over the built HTML → `62-review-facts-final.json`

Gate rule: **no open blocker** in any review, **no unconfirmed fact presented as
confirmed**, and **no persona blocker from the page's primary ICP**. Majors need a
fix or a written acceptance in `decisions.md`. Minors go to the backlog in NOTES.md.

Fix loops go back to the owning stage. Same two-round limit.

### 7. Publish package

Never publish live. The package is:
1. `site/<page path>/index.html` with `<meta name="robots" content="noindex">`
   until every fact needing sign-off is confirmed.
2. `site/<page path>/NOTES.md` in the same format as the reference page's NOTES.md:
   what the page combines, build rules applied, "Still to check before publishing"
   checklist (every unconfirmed fact, with who signs it off per `config.sign_off`),
   images to supply, sources.
3. A Word draft for reviewers (use the docx skill) when the action is `create` or `optimise`.
4. For `optimise` and `refresh`: `CHANGELOG.md` in the run folder, listing every
   change with its reason and the finding that triggered it.
5. **`CMS-HANDOFF.md`** next to the page (always, except for `audit`). This is the file
   the user takes to the custom CMS, where they or the Claude in Chrome extension apply
   the changes. Build it from `studio/templates/CMS-HANDOFF.md`:
   - For pages that already exist in the CMS (`optimise`, `refresh`), Part B is a
     change list, not a whole-page replacement. Diff the approved page against
     `current.html` and write one change per field or section, with the exact current
     text (so the editor can confirm it is in the right place) and the exact new text.
   - Order: meta, copy top to bottom, images, links, then code (schema, form, tracking).
     Code changes are listed separately because CMS editors may strip them.
   - Every change cites the finding that caused it, and any fact it depends on that
     still needs sign-off.
   - Part C lists what was deliberately kept.
   - For `create`, Part B is the new page section by section, plus the full HTML in
     `index.html` for reference.
   - Fill the "Where" fields using `studio/cms-profile.md` when it describes the
     CMS's fields. Otherwise use section headings and their position on the page.
6. When the user sends back a live URL after publishing, fetch it and run `check_page.py`
   on it with the run's facts and brief. Report anything the CMS dropped (schema, form
   attributes, noindex, links) as a numbered fix list in the same change format.

### 8. Amplify plan (parallel)

| Agent | Writes |
|---|---|
| `digital-pr` | `80-pr-plan.json`: outlets, angles, linkable assets, venue co-marketing |
| `geo-specialist` | `81-geo-plan.json`: entity and citation actions |
| `local-seo` | `82-local-plan.json`: only if the page targets a place the brand operates in, else it returns `not_applicable` |

Pitches are drafts only. Nothing is sent.

### 9. Measurement plan

`analytics-lead` writes `90-measurement.json`: KPIs, the review date, and the
CRM fields that tie enquiries from this page to outcomes.

## Finish

Write `studio/runs/<run_id>/SUMMARY.md` with:
- What was produced, with paths
- Gate result and any accepted majors
- The "still to check" list (copied from NOTES.md)
- Persona panel verdict per persona (enquire / save / leave) at each review
- Open questions for the user

Then reply to the user with a short summary and the paths. Commit and push only if
the user asked.

## Rules

- Brand integrity outranks conversion, which outranks rankings, which outranks speed.
- Source of truth order: `config.source_of_truth_order`. Existing page facts win.
- No competitor or marketplace branding, copy-only claims or images are reused.
- No venue or supplier contact details on pages; enquiries route to Wedded Concierge.
- Prices are "From AUD" and need sign-off by `config.sign_off.prices`.
- Never present an AI-generated image as a real wedding.
- Agents must not invent facts. Anything unverified is marked `unconfirmed` and
  appears in NOTES.md.
- No em dashes in any page copy or document.
