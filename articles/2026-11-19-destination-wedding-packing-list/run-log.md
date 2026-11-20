# Run log: Destination Wedding Packing List for Couples and Guests

## Inputs (from the user, 19 Nov 2026)
- Title: Destination Wedding Packing List for Couples and Guests (55 characters; keyword first; not a question; no colon or dash)
- Primary keyword: destination wedding packing list
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/expert-advice/destination-wedding-packing-list
- Slug: destination-wedding-packing-list
- Primary CMS category: Expert Advice
- Type: New. Cluster: wedding planning checklist.
- Brief (user): the destination variant, which is WW's edge and which no live or planned page covers. WW-202 is honeymoon packing. Link the head's destination track to /destination-wedding-checklist.
- User rules: title not a question, keyword first, 60 chars max, no colons or dashes; official sources linked at the claim; internal links per link-map.
- Personas: primary `couple`, secondary `paying_parent`, anti `bargain_hunter`
- Mode: FAST

## Decisions
- **Decision (default):** H1 and SEO title are both "Destination Wedding Packing List for Couples and Guests" (55 characters; passes the user rule and the 50 to 60 meta range).
- **Cannibalisation flag:** link-map lists a live page, /how-to-pack-for-a-destination-wedding (owns "pack for a destination wedding"), although the brief says no live page covers this. The strategist confirms. **Decision (default, change if you want):** this piece is the printable list, split into a couple's list and a guest list, while the existing page stays the how-to advice. It links to that page with a non-exact anchor. WW-202 (honeymoon packing) is linked only if live, otherwise it becomes a RETRO-LINK.
- **Decision (default):** packing and travel rules come only from official sources, linked at the claim:
  - Smartraveller: essentials checklist, insurance, passports.
  - Australian Border Force: what you can take and bring back, duty-free, cash.
  - Department of Agriculture: biosecurity, declaring flowers, food and natural items.
  - TGA and Smartraveller: travelling with medicines.
  - CASA: batteries and dangerous goods.
  Airline baggage rules are not quoted (they vary by carrier); readers are told to check their airline.
- **Decision (default):** no brand claims beyond live wording; no Wedded World plug; no DRAFT links.

## Stages
- **Stage 0 fast (strategist):** DONE.
  - **Volumes (AU, per month):** keyword 10; guests variant 10; what to pack 10; wedding packing list 40.
  - **SERP:** weak (Pinterest, Etsy, Facebook, a 2020 brand blog). Our /expert-advice/destination-wedding-checklist already ranks #3 in all three Australian cities.
  - **Overlap:** /how-to-pack-for-a-destination-wedding is live (styling advice; partial overlap; non-exact anchor). Two more live generic lists overlap most, /what-to-pack-for-a-destination-wedding and /pack-for-your-destination-wedding: not linked; 301 decision for the user.
  - **Live checks:** the destination checklist lives at /expert-advice/destination-wedding-checklist. The cluster head /expert-advice/wedding-planning-checklist is live. WW-202 is not live, so /honeymoon-essentials-checklist is linked and WW-202 becomes a RETRO-LINK.
  - **Link map:** new section added.
- **Decision (default):** H2 2 loses its colon (house style). H2 7 (what the Wedded Advisor arranges) must use only live brand wording, or be cut back to the Concierge's sourced travel wording.
- **Stage 1 fast (research):** PARTIAL at 23:58. The agent is waiting on an MCP permission prompt; 28 official facts are saved (Smartraveller, ABF duty free and cash, CASA batteries, TGA medicines, passports). Not yet in: biosecurity, our own pages. **Decision (default):** the writer started at 23:58 on the saved facts and re-reads the pack before writing.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md.
  - --check: 2,995 reader words, over the brief, so v2 trims to about 2,300.
  - 0 dashes, 0 placeholders. Official domains inline: ABF, CASA, Passports, Smartraveller, TGA. None blocked.
  - YAML valid; 33 claims, 20 links.
  - BIOSECURITY: a fallback line with no link.
  - The last H2 was renamed by the writer to "What your planning team arranges"; the reviewers check its service claims.
- **Decision (default):** tga.gov.au, casa.gov.au and agriculture.gov.au are approved in domains.md (official government). The dress, guest guide and what-not-to-wear pages from the brief are added to link-map (live per the Firecrawl map).
- **Stage 3 fast (3 reviews):** DONE.
  - **Accuracy 3.4:** blockers on invented on-site services and an outcome promise in the last H2, and on the PBS rule overstated twice. Majors: the 50,000-vendors count, and the advisor image slot and takeaway.
  - **SEO 3.9:** title rule passes. Majors: 36% over length, three brief pages not linked, biosecurity unlinked, and several official claims not linked at the claim.
  - **Reader (couple):** relevance 2, trust 3, clarity 3, would_enquire 2, "save". The partnered-network funnel line, the unsupported "answer to planning from afar", and too many brand names.
  - Merged request: 04-reviews/v1/merged.md.
- **Decision (default):** the last H2 becomes questions to ask the planner and venue (no implied services). Biosecurity stays unlinked until the research agent, still waiting on its permission prompt, supplies a Department of Agriculture fact.
- **Research:** COMPLETE (38 facts: Agriculture biosecurity F-31 to F-35, ABF, TGA, CASA, Smartraveller). Biosecurity penalty figures conflict ($7,280 vs $6,600), so none is quoted. Writer v2 told to link biosecurity at the claim.
