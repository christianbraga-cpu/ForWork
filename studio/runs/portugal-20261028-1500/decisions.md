# Decisions: Portugal run

Project Lead decisions, with reasons. The user can overturn any of them.

## D1. Follow the Portuguese registry (IRN) over the Australian Embassy page
Where IRN and the Australian Embassy Lisbon page differ (6 months vs 3 months to marry
after approval; translation rules), the copy follows IRN, the Portuguese authority
that runs civil marriage. Government source of the country where the marriage happens
outranks a foreign embassy summary. The difference is listed in NOTES.md for the T20
legal page owner.

## D2. Live page: hold changes that depend on unsigned facts, do not add noindex
The repo rule is "noindex until every fact needing sign-off is confirmed". That rule is
for new pages. This page is live and indexed. Adding noindex to a live page to publish
unconfirmed facts would be the wrong trade. Instead:
- Copy that depends on a fact needing sign-off (the EUR 120 registry fee, third-party
  cost ranges, the US notarial fee, the Blue Flag line, the founder quote, the B8 proof
  strip numbers) is marked **"Apply only after sign-off"** in CMS-HANDOFF.md, with a
  fallback line to use until then.
- Everything else can go live as soon as it is applied.
- The automated `noindex_while_unconfirmed` check on the preview is accepted as a known
  failure for this reason.

## D3. Australian CNI: hedge, do not state
No official source says whether Portugal accepts a CNI issued in Australia (F041). The copy
says the Australian Embassy in Lisbon can issue a CNI (F038) and tells couples to confirm
with the Registo Civil or the Embassy of Portugal in Canberra which document they need.
No claim that an Australian-issued CNI is accepted.

## D4. Official fees are not WW prices
The EUR 120 civil registry fee is a government fee, not a Wedded Wonderland price, so the
"From AUD" rule does not apply to it. It still waits for Nic's sign-off (per config) before
it is shown, under D2.

## D5. Primary persona for this page
The CRM has no Australian Portugal enquiries and only 2 to 3 real Portugal enquiries
(US, Canada). US and UK hold about 97% of search demand. Primary persona:
`intl-couple-europe-full-service`. Secondary: `au-couple-marrying-abroad` (home market),
`intimate-destination-elopement`. Always: `discerning-skeptic`.

## D6. Other branches are not used
Per the user, the France and Greece pages and the content system on other branches are
not approved and are not referenced in this run.
