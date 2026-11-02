# Run report: What Are the Filipino Wedding Traditions You Did Not Know?

- **Slug:** filipino-wedding-traditions (CMS slug as given)  ·  **Run date:** 2026-11-01 to 02  ·  **Status:** Package ready (no Chrome)
- **Mode:** fast mode, refresh. Started 23:57 UTC, first draft 00:41, package 00:48. About 51 minutes in total; the research stages ran about 35 minutes each (page readers very slow, several government pages returned errors).
- **Draft:** not uploaded (no Chrome in the cloud session; CMS field map not yet confirmed)
- **Word file:** `filipino-wedding-traditions-draft.docx`

## Inputs
- Title: What Are the Filipino Wedding Traditions You Did Not Know? (kept as given)
- Keyword: filipino wedding traditions
- Audience: couples in their 30s interested in destination weddings and luxury experiences, AUD 150k+
- URL: /expert-advice/filipino-wedding-traditions · Type: Listicle · Cluster: Wedding Traditions · Primary category: Expert Advice
- Refresh of: /15-filipino-wedding-traditions-you-wont-believe

## The page being refreshed
- Live (HTTP 200, 1,773 words, 2016). Ranks for 17 keywords in AU (best: "traditional wedding philippines" #4; the primary keyword #9) and 28 in the US (primary #22); cited in the Dubai AI overview; #7 in Singapore.
- Errors dropped: Spanish colonisation dated to the 18th century (it began in the 16th); a blood-drawing rite and a three-day wedding presented as current norms; death-themed superstitions; unsourced FAQ claims about who pays and which attendants are required.
- /best-wedding-dress-designers-philippines ranks for "filipino wedding dress" (AU #6): different intent, so this post does not target that term in a heading.

### At publish (recommendation; nothing changed on the live site)
- 301 /15-filipino-wedding-traditions-you-wont-believe to /expert-advice/filipino-wedding-traditions
- Publish the wedding traditions pillar (/expert-advice/wedding-traditions) with or before this post
- Re-check Smartraveller on publish day: Level 2 overall (updated 24 September 2026); Level 4 central and western Mindanao, the Zamboanga Peninsula, the Sulu Archipelago and southern Sulu Sea; Level 3 eastern Mindanao except Camiguin, Dinagat and Siargao

## How the topic is handled
- The source pack is thin (20 facts). Customs are described plainly as things couples often choose, with no origin stories, dates or "always" claims; meanings appear only as "often told". The article says plainly that customs vary by family, faith and region, and does not present every custom as Catholic.
- Legal facts used: Family Code Arts 3 and 6 (two witnesses of legal age; no religious rite required) and Smartraveller's marriage page. Everything else is "check with the local civil registrar and the Australian Embassy in Manila, including any fees".

## Time per stage (fast mode)
| Stage | Time |
|---|---|
| Brief (incl. old page and Smartraveller) | 5 min |
| Images (parallel) | 1 min |
| SEO research and fact-check, 2 batches (parallel) | about 35 min (15 min budget; slow page readers) |
| Orchestrator fixes to 02-seo.json schema | 3 min |
| First draft | 2 min |
| Editor and 5 readers (in parallel) | 2 min |
| Panel chair | 1 min |
| Final copy | 1 min |
| Final check, CTA, social (in parallel) | 2 min |
| Package and finish | about 4 min |

## Gates
| Gate | Result | Rounds | Notes |
|---|---|---|---|
| G1 Brief | Pass | 1 | 12 customs plus a legal section; old page errors listed |
| G2 Research | Pass (after schema fixes) | 1 | 5 cities; 260/mo AU, difficulty 26; page one is retailers and social posts |
| G3 Sources | Pass (thin) | 1 | 20 facts; embassy marriage page HTTP 500, Family Code on lawphil 404, PSA timed out, Britannica 404 |
| G4 Images | Needs input | 1 | 7 slots, all placeholders |
| G5 Edit (avg score) | Pass with edits (4.0) | 1 | 29 edits, mostly toning unsourced certainty down to "often" or "some" |
| G6 Reader panel (weighted) | Revise (enquire 2.5), 1 must-fix | 1 | Slogan replaced from brand facts; takeaways rebalanced to the traditions |
| G6b Final blocking check | 1 one-sentence fix, then 0 blocking | 1 | Unsourced "A fee applies" reworded |
| G7 Package | Pass | 1 | validate.py: all valid |
| G8 CMS | Not run | | No browser connection |

## Before you publish: human checks
### [[VERIFY]] items (2)
- The principal sponsors' role (ninong and ninang as witnesses and mentors): needs a church, cultural or academic source
- The Australian Embassy Manila steps: the certificate of legal capacity or CNI, the marriage licence and any waiting period (the embassy page returned an error today)

### Weaker sources to spot-check
- Pamamanhikan, harana and faith or regional variation rest on a Wikipedia page flagged for unreliable sources; written as "often described"
- The cord, the veil and the money dance rest on search summaries only; written as "often told"

### Prices needing Nic's sign-off
- None. No prices printed.

### Images needed (7 slots, all placeholders)
- Licensed photos for people, attire and ceremonies; coins and veil-cord still lifes may use an approved "Illustrative image"
- Do not reuse the old page's images (licences unknown)

### Questions for you
- Pinterest board names in 10-distribution.json need confirming
- Who applies the 301?
- The search, fact-check and package stages ran about twice as long tonight as on earlier runs; if this repeats, a Firecrawl top-up would help

### Deferred by you (business confirmation needed)
- Fee model and commissions; deposits and who holds supplier contracts; a phone call with a named Advisor; scale; a real Filipino wedding to link

## What the reader panel said
- Applied: slogan replaced; takeaways rebalanced towards the traditions; questions to ask when holding the rites outside the Philippines; older-guest questions for the venue
- Kept because it worked: dated Smartraveller advice, honesty about folklore versus fact, the at-a-glance table, the FAQ
- Not changed: the title (your choice)

## Links
- Internal: /magazine (primary CTA), /wonderland-concierge (secondary, after the legal section), wedding traditions pillar (draft), /destinations/asia, the Tuscany Filipino couple story, registering an overseas marriage at home, the destination wedding checklist
- External: Smartraveller Philippines, Australian Embassy in Manila (homepage)
- Backlinks and redirect: see `backlinks-todo.md`

## Distribution assets
- See `10-distribution.json`: 3 Pinterest pins, 8-slide carousel, newsletter section
