# Merged revision request: v1 to v2 (married-in-italy)

From the Editorial Director (orchestrator), merging voice, accuracy, SEO and
the reader panel (us_couple, paying_parent, bargain_hunter).

## Gate result

| Dimension | Result | Why |
|---|---|---|
| voice | FAIL | 4 majors; two_readers, brief_fidelity, brand_accuracy at 3 |
| accuracy | FAIL | 2 blockers, 4 majors |
| seo | FAIL | 3 majors (meta length, YAML, UK cross-link) |
| reader:us_couple (primary) | FAIL | trust 4 (pass), would_enquire 3 (needs 4); fears 3 and 4 touched |
| reader:paying_parent (advisory) | advisory | clarity 3 |
| reader:bargain_hunter (anti) | PASS | would_enquire 2 |

This is a strong first draft. Fix the items below without restructuring, and
keep the passages listed at the end.

## Orchestrator decisions (resolve reviewer conflicts)

- **Who "confirms".** The editor is right: the concierge is not a legal
  authority. Send every "confirm" to the body that decides (the comune, the
  Italian consulate for your state, the US post, or a lawyer licensed in
  Italy). Keep one caveat that rules change and requirements must be confirmed
  for your own passports and comune. This overrides the fact-checker's
  "(your post or advisor will confirm which)": use "your US post confirms
  which".
- **"Ask how the service is paid".** Cut it. Every reader read it as hidden
  commissions and the user has not supplied the answer. Do not replace it with
  a claim. Keep the honest line that the concierge is a paid advisory service
  that starts with a free, no-obligation Discovery Call.
- **Travel times (N-03).** Brief amended by the orchestrator: no travel-time
  column (nothing is sourced). Instead add one sentence under the region table:
  the consulate and Prefettura are in the regional capital, so check rail or
  road times from your venue when you plan the week, and allow for the trip on
  the day you book. No numbers.

## Blockers (accuracy)

1. C-47: "the Los Angeles table does not say whether the Atto Notorio fee is
   charged per couple or per partner, so ask your consulate."
2. C-52 (body and FAQ): "The US Embassy describes no step to register the
   marriage in the US: your apostilled Italian certificate is the proof."

## Majors

3. **Concierge as legal confirmer** (voice): apply the decision above in the
   intro, under the region table, in "After the wedding" and in the same-sex
   FAQ. Move the concierge mention out of intro paragraph 2 (us_couple: the
   pitch arrives before any value); the first brand mention should be in the
   help section.
4. **Prefettura rule** (accuracy): restore "generally in the same consular
   district" in the takeaway and the wedding-week section; "your US post
   confirms which".
5. **Witnesses** (accuracy): credit each condition to its source, as in
   accuracy.json; keep "plan on four unless your consulate says otherwise".
6. **Court fallback** (accuracy): booking with the Ufficio Atti Notori,
   witnesses attend with you, everyone shows proof of being in Italy,
   interpreter only if someone does not speak Italian.
7. **SEO title year**: "(2026)" or no year. Use: "How to Get Married in Italy
   as an American: US Steps" if it fits 50 to 60 characters, otherwise
   "(2026)".
8. **Meta description** to 140 to 155 characters: "How to get married in
   Italy as an American: US documents and apostilles, the Atto Notorio,
   wedding-week appointments, official fees and steps at home."
9. **YAML defect**: put `changes_from_previous:` on its own line.
10. **UK cross-link**: in the "for other passports" sentence add "or, for
    British couples, [the UK passport version of this guide](/expert-advice/how-do-british-citizens-get-married-in-italy)".
11. **Parent sentence** (voice and parent reader): replace it with one sentence
    on who is physically present (you two, your interpreter and witnesses, and
    a local planner if you hire one) and how money moves (USD at the US post,
    EUR stamps from a tabacchi, EUR hire to the comune, with your concierge
    coordinating deposits and currency if you use the service). Drop "small".
12. **Older guests** (parent reader): one sentence in the wedding-week section:
    while you are at the consulate city, someone needs to look after arriving
    guests, and historic town halls can mean stairs, so ask the comune about
    step-free access. No claims beyond that.
13. **Who the concierge suits** (bargain hunter): in the help section, use the
    live-site description: "a luxury wedding advisory and matchmaking service
    for modern couples" (brand-profile.md).

## Minors

14. "US post" on first use: "the US Embassy or consulate (the 'US post')";
    make "New York requires it" read "the Italian consulate in New York
    requires it".
15. Define "Letter of Exemplification" and "notary seal" in a clause each.
16. 2013 district list: add what to rely on: "the Embassy's district pages
    match it; your US post confirms".
17. Bring the Amalfi Coast Atto Notorio exception forward into step 4's lead
    as a clear conditional ("If you marry on the Amalfi Coast, the Naples
    consulate says you generally do not need it; check with your comune").
18. Add FAQ "Do Americans need a Nulla Osta to marry in Italy?" (2 sentences).
19. Lake Como table cell links `/destinations/europe/italy/lake-como-wedding`;
    move the Lake Como legal guide to a descriptive anchor under the table.
20. Venice row: "Venice if sworn at the Venice agency; any in Milan's district
    if sworn in Milan."
21. Fee table header "About USD"; rate, dates and "the consulates charge the
    USD figures directly" in a note under the table.
22. Step 1 timing as "we suggest"; "With 60 to 90 guests" to "With a full
    guest list"; taxes "generally follows"; C-38 to F-05; second fam.state.gov
    link as plain text.
23. Remove the overlap between the concierge quote and the soft CTA.
24. Step 4: "it is your last US step" as its own sentence.
25. **Length:** land at 2,300 to 2,400 reader words (run `--check`
    mentally: the tool count for v1 was 2,413). Pay for the new FAQ, the UK
    link and the parent and older-guest lines by cutting the old parent
    sentence, the "Ask how the service is paid" line, overlap in the help
    section and long table headers.

## Keep verbatim

- "You have found the villa, your guests are asking about flights, and
  someone now has to own the paperwork."
- "Your guests never see this part. It shapes the days before the welcome
  dinner..."
- "Budgets slip around the fees: extra nights in the consulate city,
  transfers, rush translations and documents re-ordered after they expire."
- "Any earlier and they expire."
- The NYC birth certificate three-stop line; the Nulla Osta explanation; the
  witness conflict honesty; "money orders only"; "You can handle the US side
  yourselves. Local help earns its fee in Italy."
