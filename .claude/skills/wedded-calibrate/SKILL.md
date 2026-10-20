---
name: wedded-calibrate
description: Rebuild the ICP persona cards from real CRM and enquiry data, then blind-test the reader panel against old posts with known results. Use when the person types /wedded-calibrate.
---

# /wedded-calibrate

## 1. Gather evidence (aggregates only, no personal details in any file)
- **Zoho CRM:** deals and leads from the last 24 months: budget bands, destinations, guest counts, lead source, time to book, won/lost and lost reasons. Use COQL queries for aggregates.
- **WeddedAdmin:** contacts, forms and studio funnel overviews (aggregates).
- **Enquiry wording:** sample 30 to 50 enquiry messages and call notes. Copy only short anonymised phrases (no names, emails, phones, exact dates or venues tied to a person).
- Anything the person uploads (interview notes, reviews).

## 2. Segment
Cluster booked clients into 3 to 5 segments. For each, compute share of booked revenue → `weight` (weights sum to 1.0).

## 3. Rewrite persona cards
Update `content-system/personas/*.yaml` (add/remove cards to match the segments):
- `status: calibrated`, `evidence_base` with counts and date range
- goals, fears, turn-offs, trust signals from real wording
- `voice_samples`: 3 to 6 anonymised real phrases

## 4. Blind test
1. Ask the person for 5 older posts with known results (enquiries or engagement), or pick them from WeddedAdmin/GSC data.
2. Run the `icp-reader` for every persona on each post, then the `icp-panel-chair`.
3. Compare the panel's ranking of the 5 posts with the real ranking. Report agreement (e.g. Spearman correlation) and where it was wrong.
4. If agreement is poor, adjust cards (or weights) and test once more.

## 5. Report
Write `content-system/personas/CALIBRATION.md` (date, sources, segments, weights, test result). Commit.
