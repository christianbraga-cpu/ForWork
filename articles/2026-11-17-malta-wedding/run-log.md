# Run log: Malta Wedding Legal Requirements and Paperwork

## Inputs (from the user, 17 Nov 2026)
- Title: Malta Wedding Legal Requirements and Paperwork
- Primary keyword: malta wedding
- Audience: couples in their 30s, interested in destination weddings and luxury experiences, budget AUD 150K+
- URL: https://weddedwonderland.com/destination-weddings/malta-wedding
- Slug: malta-wedding
- Primary CMS category: Destination Weddings (confirmed)
- Type: Template. Cluster: Getting Married in {Country}.
- Language: Australian English, AUD (EUR where sourced)
- Personas: primary `couple`, secondary `paying_parent` (advisory), anti `bargain_hunter`
- Mode: FAST; strategist and two research batches in parallel

## Decisions
- **Decision (default, change if you want):** third article built from blog-team/templates/country-legal-guide.md, including the Vietnam lessons.
- **Decision (default):** "malta wedding" is broad; the article stays a legal guide, with a short sourced "why Malta" note only.
- **Decision (default):** no Malta destination page in link-map; link /destinations/europe and log MALTA-PAGE.
- Legal sources: Malta Public Registry / Identity Malta, gov.mt and servizz.gov.mt, Maltese High Commission in Canberra, Australian High Commission in Malta, Smartraveller, DFAT.

## Stages
- **Stage 0 fast (strategist):** DONE. Volumes AU: malta wedding 50, malta wedding venues 70; UK 480 and 720; "malta wedding legal requirements" no data. AI overview gives the rules (no residency requirement, RZ1/RZ2 forms 6 weeks to 3 months ahead, two witnesses) but cites UK operators and blogs; nobody covers the Australian side. Brief: template's 11 H2s, one venue-selection H3 in the wedding-week section, 2,300 words, 5 FAQs, SEO title "Malta Wedding: Legal Requirements and Paperwork". No cannibalisation. Brisbane SERP not run; competitor pages not read (snippets only).
- **Decision (default, change if you want):** Malta URLs added to link-map (Delta Goodrem story, /venue/the-phoenicia-malta; venue profiles are linkable per link-map rule 5). MALTA-PAGE open item.
- **Stage 1 fast research B:** DONE. 22 facts (F-100 to F-121; F-100 to F-114 reused from France and Vietnam packs). Malta in the Apostille Convention since 3 Mar 1968 (HCCH); Smartraveller: Schengen 90 in 180, EES, ETIAS not yet open. Australian High Commission Malta shows no CNI service: apply through DFAT in Australia (N-100). Fees AUD 181 CNI and AUD 105 apostille (2026, Nic). Gaps: climate, DFAT processing times, certificate language. highcommission.gov.au added to domains.md.
- **Stage 1 fast research A:** DONE. 19 legal facts (identita.gov.mt, legislation.mt Cap. 255, humanrights.gov.mt). Non-resident foreigners CAN marry civilly; no residency rule. Australian documents need an apostille; non-EU translations too. Contact Registry 3+ months ahead, file no later than 6 weeks before; documents valid 3 months; venue must be public and Registrar-approved. Age 18; same-sex marriage since 2017. Registry fees EUR 76.95, 102.60, 51.30 (PDF uploaded Feb 2024, no year printed; Nic). Gaps N-001 to N-009 (CNI vs affidavit, RZ2 apostille, Gozo office, church rules, certificate after). One Firecrawl extraction discarded for invented Act text. "Maltese government" row added to domains.md.
- **Decision (default, change if you want):** Registry fees written as "(fee schedule published 2024)"; the marry-in-Australia H2 kept but short, since Malta is open to non-residents.
- **Stage 2 fast (writer):** DONE. 03-draft-v1.md. --check: 2,440 reader words (under the 2,500 cap), 0 dashes, 0 placeholders, 6 domains, none blocked. YAML valid; 39 claims, 24 links. Open: CNI vs affidavit, RZ2 apostille, Gozo office, church rules, climate, venue link (editorial), pillar and witnesses links conditional.
- **Stage 3 fast (3 reviews):** DONE. Accuracy 3.8 (majors: "sets no residency rule" overstates the guideline; unsourced apostille definition; Phoenicia "in Valletta" unsourced). SEO 4.6, approved (minors: title 56 chars for Australians, H2 rename, FAQ repeats, Wedded World plug to delete). Reader (couple) relevance 2, trust 3, clarity 3, would_enquire 2 (Italy-led persona; H2 3 heading contradicts body; repeated "ask the Registry"; jargon; concierge brochure language). Merged request: 04-reviews/v1/merged.md.
- **Decision (default, change if you want):** H2 3 adapted for an open country ("Prefer to marry in Australia?"); Delta Goodrem link kept as inspiration; Wedded World sentence removed (house rule). Template updated with these lessons.
- **Stage 4 fast (writer v2):** DONE. 03-draft-v2.md. --check: 2,238 reader words, 0 dashes, 0 placeholders, 7 domains, none blocked. YAML valid; 40 claims, 23 links. All 27 merged items applied; overstated residency, apostille definition, Valletta, Wedded World plug and the contradicting H2 all gone.
- **Stage 6 fast (copy editor):** DONE. final.md 2,237 reader words, 0 dashes, 0 placeholders, none blocked; publish-package.json valid (SEO title "Malta Wedding: Legal Requirements for Australian Couples", 12 open items); chrome-upload-prompt.md (draft only); article.docx built. Light edits only; research gaps folded into REGISTRY-QUESTIONS. Image file names are placeholders.

## Must-fix before publish
1. REGISTRY-QUESTIONS: ask the Public Registry (Identita) whether Australians bring a DFAT CNI or an affidavit, whether the notarised RZ2 needs an apostille, certificate copies after the wedding, the Gozo office, church rules.
2. Nic signs off the Registry fees (EUR 76.95, 102.60, 51.30; schedule published 2024, no year printed) and DFAT fees (AUD 181, AUD 105; 2026).
3. LINK-CHECK: open every external link in a browser (session network blocks them), especially the Smartraveller notarial URL and the 2024 fee PDF.
4. Publish after /expert-advice/marriage-licence-requirements and /expert-advice/wedding-witnesses, or apply the PILLAR-LINK and WITNESS-LINK fallbacks.
5. VENUE-LINK (confirm The Phoenicia profile may be linked editorially), MALTA-PAGE, CONCIERGE-PAY, IMAGE-RIGHTS, AUTHOR, CMS-URL.
6. Research hygiene: 02-research-B.json reused facts carry 17 Nov checked dates and "Wedded Advisor confirms" summary lines; clean before reuse.
