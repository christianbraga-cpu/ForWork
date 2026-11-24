# Run log: Wedding Venue Comparison Spreadsheet and What to Compare

## Inputs (from the user, 24 Nov 2026)
- Title: Wedding Venue Comparison Spreadsheet and What to Compare (56 characters; keyword first; not a question; no colon or dash)
- Primary keyword: wedding venue comparison spreadsheet
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/expert-advice/wedding-venue-comparison-spreadsheet (type "new")
- Slug: wedding-venue-comparison-spreadsheet
- Primary CMS category: Expert Advice. Cluster: wedding planning spreadsheet.
- Brief (user): the venue shortlist tab as its own page, with strong internal links to the Marketplace venue search (/search?tab=vendors) and destination venue pages.
- Rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default):** H1 and SEO title as given (56 characters; passes the rule and the meta range).
- **Decision (default):** URL status checked first. If live, refresh in place; if not, create a new post after a CMS slug check.
- **Decision (default):** /search?tab=vendors is checked first (link-map marks /marketplace NOT LIVE). If it loads, it becomes the main venue-search link and is added to link-map. If not, fall back to /venue and the city venue pages, and log it.
- **Decision (default):** the comparison table is our own template, with no invented prices or venue facts. Official sources (ACCC deposits and refunds) are used only where a fact needs one, reused with original dates. No Wedded World plug, no DRAFT links.

## Stages
