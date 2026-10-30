# Site pages and SEO team

This repo holds page builds (`site/`) and the SEO agent team that produces them
(`seo-team/`, `.claude/agents/`, `.claude/skills/seo-page/`).

## Running the team

Everything starts from four inputs: **the page**, **the action**, **the research doc**
and **the existing page facts**. Run:

```
/seo-page page=<url, site path or html file> action=<create|optimise|refresh|audit> research=<file> facts=<file>
```

Inputs can also be pasted into the chat; the orchestrator saves them into the run folder first.
See `seo-team/README.md` for the full guide and `seo-team/workflows/pipeline.md` for the phases.

Pages differ in type and structure. Do not copy the structure of any existing build in
`site/`; each page's structure comes from its own research doc, page facts and existing page.

## Rules every agent follows

- **Facts come from the Fact Ledger only.** Page facts outrank the research doc;
  anything else is unverified. Never invent prices, capacities, distances, legal steps or
  inclusions. Unknowns become `[[CONFIRM: ...]]` placeholders and go on the sign-off list.
- **Never publish.** Pages keep `<meta name="robots" content="noindex">` until a human
  signs off. The pipeline stops at `awaiting_signoff`.
- **House rules** are in `seo-team/brand/site-rules.md`; **voice** in `seo-team/brand/brand-voice.md`.
  No em dashes in any copy or report.
- **Every agent output** uses the envelope in `seo-team/schemas/envelope.schema.json`
  and is saved in the run folder, never only in chat.
