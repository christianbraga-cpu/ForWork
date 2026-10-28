# Portugal destination page: FIX notes

Page: `/destinations/europe/portugal` (live). Action: FIX, live but broken, run as optimise, copy scope.
Run: `studio/runs/portugal-20261028-1500`. Final copy: `30-page-copy.json` revision 4. Handoff: `Portugal-CMS-Handoff.docx` and `CMS-HANDOFF.md`.

## What changed

- All headings rewritten in the section plan's voice; H1 "Get Married in Portugal, from a Sintra Palace to an Algarve Cliff"; title "Wedding in Portugal | Venues by Region | Wedded Wonderland".
- Em dashes removed; "Wonderland Luxury Advisor" replaced by Wedded Advisor.
- Unsourced cost and planner-fee figures removed; a named, dated third-party cost range is held for Nic's sign-off.
- Legal paragraph replaced with the official rules (IRN, justica.gov.pt) and the route by passport (US, UK, AU) with official sources.
- Founder quote and byline removed unless Wendy signs off.
- US-only comparisons removed. Spain H2 removed; Spain appears in Explore More of Europe only when live.
- Added: B9 qualifier, B8 proof strip (fallback line), B16 spotlight, region chooser (5 regions, 4 airports), palace booking rules, beach line, venue contract checks, step-by-step tabs, weekend, guests, celebrations, How it works with one Wedded Advisor, enquiry form, 10 FAQs, articles, Europe links, mobile sticky bar.
- Real weddings section hidden at launch (2 of the 3 needed).
- Schema: TouristDestination, ItemList, Service, BreadcrumbList, FAQPage (10), Organization. Article and Person removed. See `schema.jsonld`.

## Still to check before publishing

### Sign-offs (lines are held with a fallback until signed off)

- [ ] F019 B8 proof strip wording: signs off **Project Lead (human)**
- [ ] F020 Founder quote: signs off **Wendy**
- [ ] F024 Civil registry fee (EUR 120, or EUR 200 outside the registry or out of hours; official, shown only after sign-off, D4): signs off **Nic**
- [ ] F043 US: statement of eligibility and fee: signs off **Nic**
- [ ] F066 Algarve Blue Flag beaches: signs off **Project Lead (human)**
- [ ] F069 Cost ranges, Rita Plácido Photography: signs off **Nic**
- [ ] F076 Ponta da Piedade, Lagos: signs off **Project Lead (human)**
- [ ] F077 Douro tourism-board description: signs off **Project Lead (human)**
- [ ] (D16: F082 to F086 are already used with light hedging; confirm in a browser)
- [ ] F082 Madeira: signs off **Project Lead (human)**
- [ ] F083 Cascais: signs off **Project Lead (human)**
- [ ] F084 Comporta: signs off **Project Lead (human)**
- [ ] F085 Fado: signs off **Project Lead (human)**
- [ ] F086 Azulejo tiles: signs off **Project Lead (human)**

### Browser checks (official pages blocked from the build environment)

- [ ] F024 Civil registry fee (EUR 120, or EUR 200 outside the registry or out of hours; official, shown only after sign-off, D4): signs off **Nic**
- [ ] F043 US: statement of eligibility and fee: https://pt.usembassy.gov/marriage-in-portugal/
- [ ] F044 US: timeline and residence: https://pt.usembassy.gov/marriage-in-portugal/ ; https://irn.justica.gov.pt/Servicos/Cidadao/Casamento/Organizar-o-casam
- [ ] F076 Ponta da Piedade, Lagos: https://visitalgarve.pt/en/3640/ponta-da-piedade.aspx
- [ ] F077 Douro tourism-board description: https://www.visitportoandnorth.travel/onde-ir/douro
- [ ] (D16: F082 to F086 are already used with light hedging; confirm in a browser)
- [ ] F082 Madeira: https://visitmadeira.com/en/travel-info/about-us-and-where-we-are/ ; https://visitmadeira.com/en/where-to-go/madeira/sou
- [ ] F083 Cascais: https://jmj2023.cascais.pt/en/geral/about-cascais ; https://www.visitlisboa.com/en/regions/cascais
- [ ] F084 Comporta: https://cm-alcacerdosal.pt/municipio/concelho/freguesias/freguesia-da-comporta/?lang=en ; http://www.portalautarquico.dg
- [ ] F085 Fado: https://ich.unesco.org/en/RL/fado-urban-popular-song-of-portugal-00563/
- [ ] F086 Azulejo tiles: https://www.visitportugal.com/en/node/73867

### Dev

 - [ ] Confirm the enquiry endpoint `/api/concierge/enquiry` and that the CMS keeps hidden form fields.
- [ ] Confirm URLs for Wonderland Studio "Start for free" and the Privacy Policy (marked `[URL to confirm]`).
- [ ] Confirm the CMS keeps the JSON-LD block; paste `schema.jsonld`.
- [ ] Staging is indexable with a staging canonical: noindex staging.
- [ ] Add /destinations/europe/italy, /greece, /france and /7-ancient-and-romantic-portuguese-wedding-traditions to the live sitemap.
- [ ] Sticky bar button "Speak with a Wedded Advisor" wraps at 390px: tighten the button style or choose a shorter label.
- [ ] Check that the linked honeymoon article covers Madeira, the Azores and the Algarve.

### Business answers that would lift conversion (see studio/brand-answers.md)

Fee model and currency, a named Wedded Advisor, what happens on the day, why an Australian firm, approved B8 proof numbers or a third Portugal real wedding, what Wedded Privileges gives couples, any Portugal From price.

## Link donors to update (outside this page)

- `/trending/cristiano-ronaldo-georgina-rodriguez-wedding`: one body link to this page, anchor "wedding in Portugal".
- `/7-ancient-and-romantic-portuguese-wedding-traditions`: a contextual link to this page.

## Images to supply

Each slot needs a rights-cleared image (venue media kit with permission, or a real wedding with consent). Never competitor or marketplace images.

| File name | Alt text |
|---|---|
| pena-palace-sintra-hills-wedding-in-portugal.jpg | Pena Palace on its wooded hilltop above Sintra, a palace setting for a wedding in Portugal |
| pena-palace-above-trees-sintra.jpg | Pena Palace rising above the wooded park in the Sintra hills, wrapped in light mist |
| monserrate-palace-arches-lawns-sintra.jpg | Monserrate Palace arches above the lawns of its Romantic park in Sintra |
| queluz-national-palace-facade-dusk.jpg | Facade of the National Palace of Queluz near Lisbon at dusk |
| douro-valley-terraced-vineyards.jpg | Steep terraced vineyards in the Alto Douro Wine Region |
| algarve-coast-clifftops-atlantic.jpg | Golden clifftops above the Atlantic on the Algarve coast |
| azulejo-tile-wall-detail-portugal.jpg | Close-up of blue and white azulejo tiles on a Portuguese wall |
| fado-guitar-portugal.jpg | A Portuguese guitar used to play fado |
| quinta-stone-staircase-couple-portugal.jpg | Couple on the stone staircase of a Portuguese quinta before dinner |
| lisbon-sintra-cascais-pena-palace-forest.jpg | Pena Palace above the forest in Sintra, in the Lisbon, Sintra and Cascais region |
| algarve-clifftops-beach-sea-stacks.jpg | Sea stacks and a sandy beach below the Algarve clifftops |
| porto-douro-terraced-vineyards-river.jpg | Terraced vineyards above the Douro river in the Alto Douro Wine Region |
| comporta-alentejo-coast-dunes-dusk.jpg | Dunes on the Alentejo coast at Comporta at dusk |
| madeira-atlantic-cliffs-green-hills.jpg | Green cliffs above the Atlantic on the island of Madeira |
| registry-table-signing-portugal.jpg | Couple signing the marriage register at a civil registry table in Portugal |
| monserrate-gardens-sintra.jpg | Gardens of the Park and Palace of Monserrate in Sintra |
| douro-slate-terraces-vineyards.jpg | Slate terraces lined with vines in the Douro Valley |
| algarve-beach-low-sun.jpg | Algarve beach and clifftops in low evening sun |
| lisbon-arrival-couple-city-street.jpg | Couple arriving in Lisbon, walking a city street with their luggage |
| quinta-courtyard-dinner-table-portugal.jpg | Quinta courtyard laid with a long table for a wedding dinner |
| pousada-historic-castle-cloister.jpg | Stone cloister of a pousada in a historic Portuguese castle |
| algarve-clifftop-ceremony-aisle.jpg | Ceremony aisle set on an Algarve clifftop above the Atlantic |
| douro-wine-quinta-vineyard-terrace.jpg | Vineyard terrace at a wine quinta in the Douro Valley |
| lisbon-civil-ceremony-salon.jpg | Civil wedding ceremony in an ornate salon in Lisbon |
| portugal-church-doorway-ceremony.jpg | Couple at the doorway of a church in Portugal after a Catholic ceremony |
| quinta-long-dinner-table-portuguese-wine.jpg | Long dinner table with Portuguese wine at a quinta after the ceremony |
| quinta-terrace-guests-morning-after.jpg | Wedding guests at breakfast on a quinta terrace the morning after |
| madeira-funchal-south-coast.jpg | Funchal on the south coast of Madeira, seen from above the bay |
| douro-anniversary-wine-tasting-terraces.jpg | Couple at a wine tasting above the Douro Valley terraces |
| sintra-pena-park-proposal.jpg | Proposal in the wooded park below Pena Palace, Sintra |
| algarve-clifftop-vow-renewal.jpg | Couple renewing their vows on an Algarve clifftop above the Atlantic |
| douro-quinta-birthday-lunch.jpg | Family birthday lunch at a long table at a Douro wine quinta |
| wedded-advisor-planning-with-couple.jpg | Wedded Advisor planning with a couple at a table, laptop and notes open |

## Sources

Official: justica.gov.pt, irn.justica.gov.pt, cig.gov.pt, smartraveller.gov.au, portugal.embassy.gov.au, pt.usembassy.gov, travel.state.gov, gov.uk, parquesdesintra.pt, pousadas.pt, amn.pt, whc.unesco.org. Third party (held for sign-off): ritaplacidophotography.com (Feb 2025). Full list with fact ids: `facts.json`.
