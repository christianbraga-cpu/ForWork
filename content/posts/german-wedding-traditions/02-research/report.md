# SEO research: german-wedding-traditions (stage 02, fast mode, 2026-11-01)

Source: DataForSEO (SERP, Labs, Ads volume, instant pages); Apify web-fetch for page reads. GSC export not read (Google Drive connector disconnected): positions below are DataForSEO, not Search Console.

## Refresh findings
| Page | HTTP | Ranked kw AU / US | 'german wedding traditions' | Verdict |
|---|---|---|---|---|
| /7-german-wedding-traditions-you-didnt-know-about | 200 | 13 / 74 | AU rank 2 (abs 4, vol 70); US rank 5 (vol 880) | 301 to new URL at publish (confirmed) |
| /8-greek-wedding-traditions-you-didnt-know-about | 200 | 7 / 35 | Not ranked; 0 German keywords in AU or US | Brief diagnosis corrected |

- Greek page: every ranked keyword is Greek. The shared title template is not causing German rankings in DataForSEO data. Keep the anchor fix (exact-match "German wedding traditions" anchor becomes descriptive and points to the new URL). Drop the title/H1 change for German reasons. No redirect.
- The old German page also ranks in the US for "wedding traditions in germany" (880, pos 4), "german marriage customs" (880, pos 4) and "german wedding dress traditions" (260, pos 3). Keep the dress and gifts sections so the 301 carries them.
- Regional scope: confirmed **au_focus**. AU volume is small (70/mo, KD 0), but the US volume is larger (880) and the content is global. Write for AU (Standesamt from Australia) and keep the traditions sections usable worldwide.

## SERP by region (top 3 organic)
| City | 1 | 2 | 3 | PAA highlights |
|---|---|---|---|---|
| Sydney | The Knot | Wedded Wonderland (old page) | hamburg.com | dress colour, gift money, ring finger, marrying a German citizen |
| Melbourne | Wikipedia | Facebook post | Reddit r/AskGermany | culture traditions, who pays |
| New York | Oahu Officiant | Discover Germany | Reddit r/AskGermany | who pays, 30-5 rule |
| Dubai | German Marylanders | Angara | Facebook DW | what to wear as a guest |
| Singapore | German Marylanders | Love Bird Ceremonies | Scribd | cost of a wedding in Germany |

AI overviews (AU, US) group customs as pre-wedding / ceremony / reception, which matches the brief's timeline grouping.

## Pages read (Apify web-fetch, 2026-11-01)
- **The Knot** (reference only, competitor, not linked): about 1,600 words; H2s History / Prewedding / Attire / Ceremony / Reception / Food / Postwedding; no prices; one German-born officiant quoted; no sources. Gap: no Standesamt guidance for foreign couples.
- **hamburg.com** (official city portal, usable as authority): about 600 words; 8 customs; states Polterabend "probably" pre-Christian, that glass is never broken, and the North German midnight burning ritual; bride kidnapping "more common in villages" today.
- **German Marylanders** (heritage society, top 3 in Dubai and Singapore): about 1,500 words; personal anecdotes; gives gift amounts (we will not); Standesamt-first rule; regional notes ("not throughout Germany").
- **Reddit r/AskGermany** (top 3 in Melbourne and NY): blocked by a captcha, not read.
- Page texts were not saved to 02-research/pages/ (fast-mode budget). Apify dataset IDs are XORzfKGDcAn4l8q4j (The Knot), DsYPLugCCIhD3bhCi (hamburg.com) and zsuPTVrZW963GQ22r (German Marylanders), for the originality check.

## Cross-region summary
- Guest counts: no result states guest counts reliably; only "smaller wedding parties" (The Knot, quoted officiant).
- Pricing shown: none, apart from gift amounts on German Marylanders. We publish no amounts.
- Top concern: what actually happens on the night, and whether customs are still practised.
- Gap we can own: official sourcing, plus the Standesamt step explained for Australians.

## Not done (fast mode)
- Los Angeles, Abu Dhabi, Riyadh, Doha and Hong Kong were not run. The Arabic query was not run.
- /magazine and /wonderland-concierge were not live-checked. Backlink sentences for the two traditions pages were not confirmed.

recommended_scope: au_focus
