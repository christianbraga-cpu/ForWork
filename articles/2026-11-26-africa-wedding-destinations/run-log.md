# Run log: Africa Wedding Destinations From Safari to Coast

## Inputs (from the user, 26 Nov 2026)
- Title given: 12 Africa Wedding Destinations From Safari to Coast
- Primary keyword: africa wedding destinations
- URL: https://weddedwonderland.com/destination-weddings/africa-wedding-destinations
- Slug: africa-wedding-destinations
- Primary CMS category: Destination Weddings. Type: Programmatic. Cluster: Destination Wedding Guide 2026. Plan ref: WW-300.
- Audience (standing default): couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- Standing user rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default, TITLE-RULE):** the given title starts with "12", so it is not keyword first.
  - H1: "Africa Wedding Destinations From Safari to Coast" (48 characters).
  - The number moves to the H2 "Our 12 Africa wedding destinations".
  - Revert if you prefer (TITLE-SERIES).
- **Decision (default):** Programmatic reuses the month-destinations card pattern; the copy editor saves blog-team/templates/region-destinations.md.
- **Decision (default):** an editorial ranking with criteria stated: setting, season, legal or symbolic, exact Smartraveller level, guest travel only if officially stated.
  - Legal facts from official pages only; otherwise "confirm with the embassy" plus a FACT-GAP-LEGAL item.
  - No invented prices or weather; no competitor lists.
- **Decision (default):**
  - Never link /destinations/africa (hidden).
  - Check og:url for redirects.
  - No DRAFT links, no Wedded World plug.

## Stages
- Stage 0 and 1 launched in parallel (both save early).
- **Stage 0 fast (strategist):** DONE.
  - **URL:** 404, so a new post. Zoho WC3-T198 (To-Do, WW-300).
  - **Live pages:** the South Africa, Seychelles and Mauritius legal pages; the African honeymoon page (the old expert-advice URL redirects to it).
  - **AFRICA-HUB-404 (for the user):** the four /destinations/africa/* country pages return 404, although Zoho shows them in Review. Not linked.
  - **Volumes:** the head term has no data in AU or US. AU about 10 a month per variant. US: african destination wedding 30, safari wedding 90, wedding in africa 40.
  - **SERP:** weak in all four cities (Pinterest, Instagram, old blogs). The SERP URLs came back as redirect links (null in 01-serp.json).
  - **Gap:** nobody gives legal steps, the advice level or guest logistics per destination.
  - **Titles:** SEO title "Africa Wedding Destinations From Safari Camps to the Coast". Meta 155 characters.
  - Link-map "Africa destinations" section added.
- The researcher is held on an MCP permission prompt.
- **05:50 check-in:** the researcher is intermittently held on MCP permission prompts. 16 facts across 4 countries (Seychelles, Kenya, Tanzania, South Africa). Below the 8-country threshold, so the writer waits.
