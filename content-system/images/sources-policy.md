# Image sources policy

Work through these in order. Stop at the first source with a correct, licensed image for the slot.

| # | Source | How | Publishable? |
|---|---|---|---|
| 1 | **Image library** (Google Drive `Wedded Image Library/<destination>/<venue>/`, registered in `library-index.csv`) | Google Drive connector: search, download original | ✅ If the register shows licence + consent |
| 2 | **weddedwonderland.com pages** (venue/package images supplied by partners) | Firecrawl scrape → image URLs → download | ✅ Only if the supply agreement covers blog use; otherwise `[[VERIFY licence]]` |
| 3 | **Canva brand kit / uploads** | Canva `get-assets` | ✅ |
| 4 | **Venue media kit / press page** | Firecrawl finds it; Gmail **draft** permission request (never sent by the agent) | ⏳ After written permission. Slot stays `pending_permission` |
| 5 | **Competitor / search result pages** | Firecrawl image URLs → `reference-only/` | ❌ Never. Mood and shot briefs only |
| 6 | **AI-generated (Higgsfield)** | Only textures, abstract headers, flat-lays; labelled illustrative | ⚠️ Never for a real venue, destination or wedding |
| – | **Premium stock (Stocksy, Getty, Offset)** | Human purchases, adds to Drive library + register | ✅ After purchase |

## Verifying location and content
- Location: register row, EXIF GPS/date (`scripts/prepare_images.py` prints it), photographer gallery name, or the source page. **Never from appearance alone.**
- Content: Claude views the image (Read tool) and checks it against the paragraph and shot brief (setting, season, subject). Record `fit_reason`.
- Uniqueness and ownership: Google Lens via Apify (actor chosen below). The image must be at a public URL.

## Google Lens actor
- Preferred: `s-r/google-lens` (pay per image with matches). Fallback: `gio21/google-lens-scraper`.
- Confirm the input schema with `apify_get_actor_input_schema` before the first run, then update this line with the tested choice.
