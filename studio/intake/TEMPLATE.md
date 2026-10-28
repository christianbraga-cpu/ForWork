# Page Studio intake

Copy this file into your message (or attach it) to start a run. Only the four
inputs are required. Everything else is optional.

## 1. Page (required)

The page this run is about. One of:
- Live URL: `https://weddedwonderland.com/packages/italy/tuscany/<venue>`
- Repo path: `site/packages/italy/tuscany/<venue>/index.html`
- New page: the intended URL path, e.g. `/packages/greece/santorini/<venue>`

## 2. Action (required)

Pick one:

| Action | Use when | Output |
|---|---|---|
| `create` | The page does not exist yet | New page, NOTES.md, Word draft, amplify and tracking plans |
| `optimise` | The page exists and should rank and convert better | Revised page, change log, NOTES.md, plans |
| `refresh` | Facts, prices, seasons or offers changed; structure is fine | Updated page, fact diff, NOTES.md |
| `audit` | You want a report only, no rebuild | Audit report with prioritised fixes |

## 3. Research doc (required)

The starting point for the run: the page brief, destination and venue research,
keyword ideas, competitor notes. Give one of:
- A Google Drive link or file name
- A Notion page link
- A file path in this repo
- Pasted text

## 4. Existing page facts (required)

Facts that are already verified and signed off. These outrank every other source.
Use the table below, a sheet, or a pasted list. Mark anything not yet confirmed
as `unconfirmed`.

| Fact | Value | Source | Status (confirmed / unconfirmed) | Signed off by |
|---|---|---|---|---|
| From price | AUD 38,550 | Supplier rate card 2026 | confirmed | Nic |
| Guest capacity | 20 to 300 | Package listing | unconfirmed | |
| Rooms on site | 69 plus tower | Official site | confirmed | |

## Optional

- Target ICPs for this page (default: the panel chooses from `studio/personas/`)
- Priority markets (default: `studio/config.json`)
- Deadline
- Anything that must or must not appear on the page
- Image folder or media kit link
