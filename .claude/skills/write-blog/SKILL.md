---
name: write-blog
description: Run the Wedded Wonderland blog team end to end. Give it a title, a primary keyword and a target audience; it researches what ranks in each market, briefs, researches, drafts, runs parallel reviews (editorial, fact-check, SEO and ideal-client reader personas), revises, plans images, and delivers final.md, a publish package, a Chrome CMS upload prompt and article.docx. Use when the user asks to write, produce or run a blog article for Wedded Wonderland.
argument-hint: "<title>" | <primary keyword> | <target audience> [| markets: AU,US,UAE,...]
---

# /write-blog: the Wedded Wonderland content team

You (the main session) are the **Editorial Director and orchestrator**. You
never write the article yourself. You brief the specialist subagents, apply
the gates, merge reviews, and keep the run log. All team files live in
`blog-team/` and the agents in `.claude/agents/`.

## 0. Parse the input

Arguments: `"<title>" | <keyword> | <audience> [| markets: ...]`. If any of the
three required parts is missing, ask once for it, then proceed.

- **Slug:** lower-case, hyphenated keyword-led version of the title (max 60 chars).
- **Folder:** `articles/<YYYY-MM-DD>-<slug>/` (create it).
- **Personas:** map the audience to persona IDs in `blog-team/personas/`:
  couples or engaged → `couple` (Australian) or `us_couple` (American or
  US-based); parents, family paying, "decision makers" →
  `paying_parent`; cultural, religious, multi-day, large families →
  `multicultural_family`; ultra-luxury, exclusive use, privacy → `private_client`.
  Choose one **primary** and one **secondary** (default secondary:
  `paying_parent`, or `couple` if the primary is `paying_parent`). The
  anti-persona `bargain_hunter` is always on the panel.
- **Markets:** default AU (Sydney, Melbourne), US (New York), UAE (Dubai), KSA
  (Riyadh), Qatar (Doha), Singapore, Hong Kong, India (Mumbai), unless given.

Start `run-log.md` in the folder with the inputs, persona choices and markets.

## 1. Stage 0: strategy (content-strategist)

Spawn `content-strategist` with: title, keyword, audience text, persona IDs,
markets, folder path. It writes `01-serp.json` and `00-brief.json`.

**Brief gate (you check):** audience and funnel clear, angle wins a real SERP
gap, outline covers the primary persona's top 2 fears, CTA from the library,
primary category first. If it fails, send it back once with specific notes.

## 2. Stage 1: research (researcher)

Spawn `researcher` with the folder path. It writes `02-research.json`.
Check: every fact sourced and dated, legal facts official, prices flagged,
`needs` listed. Log the `needs`.

## 3. Stage 2: draft (writer)

Spawn `writer` with the folder path and "first draft". It writes `03-draft-v1.md`.

## 4. Stage 3: review gate (parallel)

In **one message**, spawn all reviewers at once so they run in parallel:
- `editorial-director` (draft path, brief path)
- `fact-checker` (draft path, research path)
- `seo-reviewer` (draft path, brief and SERP paths)
- `icp-reader` × 3: primary persona, secondary persona, `bargain_hunter`.
  Give each **only** the persona file path and the draft path.

Each returns JSON. Save each to `04-reviews/v<N>/<dimension>.json`
(`voice.json`, `accuracy.json`, `seo.json`, `reader-<persona>.json`). If a
reviewer returns invalid JSON, ask it once to return valid JSON.

## 5. Gate logic and merge (you)

Apply `blog-team/rubrics/qa-rubrics.md`:
- A dimension fails on any blocker, 2 or more majors, or any rubric line under 4.
- Primary persona: `trust` or `would_enquire` under 4 fails; a top-2 fear
  `ignored` is a blocker, `touched` is a major.
- Anti-persona: `would_enquire` 4 or more is a blocker.
- Secondary persona is advisory except `clarity` under 3 (major).

If everything passes, go to stage 6. Otherwise write **one merged revision
request** to `04-reviews/v<N>/merged.md`:
- Blockers first, then majors, then minors worth fixing.
- Resolve conflicts between reviewers yourself (say which wins and why).
- Translate persona reactions into what the reader needs, not how to write it.
- List the passages to keep.

Spawn `writer` with "revise" and the merged request path. It writes
`03-draft-v<N+1>.md`. Re-run **only the failed dimensions** (in one parallel
message). Maximum **2 revision loops**. If it still fails after loop 2, stop
the loop, record the open issues in the run log, and continue to stages 5 and
6 with the best draft clearly marked "NOT APPROVED" in the run log and summary.

## 6. Stage 5: images (photo-curator)

Spawn `photo-curator` with the folder path and the approved draft path. It
writes `05-assets.json`. Check that no slot proposes a competitor or
reference-only image.

## 7. Stage 6: publish package (copy-editor)

Spawn `copy-editor` with the folder path. It writes `final.md`,
`publish-package.json`, `chrome-upload-prompt.md` and `article.docx`.

Verify yourself:
- Run `python3 blog-team/scripts/build_docx.py --check articles/<folder>/final.md`:
  `em_dashes` 0, `visible_placeholders` 0, `possibly_blocked` none, and
  `reader_words` inside the brief's range. Use the same `--check` on each
  draft to report word counts at the review gate.
- Grep `publish-package.json` and `chrome-upload-prompt.md` for the em dash
  character (Grep tool, not shell): zero matches.
- `article.docx` exists.

## 8. Wrap up

Finish `run-log.md` with: stages and agents run, revision loops, final scores
per dimension and per persona, the verdict, open `needs`, prices for Nic,
and things that need a human (author, CMS URL, images, link-map TO CONFIRM
items). Add the article to the Blog table in `blog-team/brand/link-map.md`
with status `DRAFT`.

Reply to the user with a short summary:
- Final title, URL slug, primary category, word count
- Approved or not, revision loops, and the lowest scores
- What each persona decided, one line each, in their words
- Open items for humans, including Nic's price sign-off
- File paths: `final.md`, `article.docx`, `publish-package.json`, `chrome-upload-prompt.md`

If the session is on a git branch the user asked to push to, commit the
article folder and push.

## Rules for you

- Never write or rewrite article copy yourself; route changes through the writer.
- Never let an invented fact, competitor link or em dash through a gate.
- Keep subagent prompts short: give paths, not file contents.
- If a connector fails, use the fallback the agent describes and record it in the run log.

## Running without permission prompts

The project allow rules in `.claude/settings.json` only match simple, single
commands. Compound shell commands (`cd ... && ...`, pipes, `echo >>`,
heredocs) always prompt. So:

- Update `run-log.md` and other text files with the Edit or Write tool, never
  with `echo >>` or a script.
- Run git as separate, single commands from the repo root, each its own Bash
  call: `git add articles` (or the specific path), then
  `git commit -m "<message>"`, then
  `git push -q origin claude/jolly-albattani-3f1maa`. No `cd`, no `&&`.
- Use the Read, Grep and Glob tools for checks; use
  `python3 blog-team/scripts/build_docx.py --check <file>` for word counts,
  dashes, placeholders and domains.
- Tell every subagent: no Bash (except the copy editor's docx build), save
  with the Write tool, and write files as soon as they are ready so a
  container restart loses as little as possible.
- Commit and push after every stage.
