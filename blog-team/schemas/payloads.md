# Payload schemas

Every agent output is JSON (except the draft and final article, which are
Markdown with YAML front matter). The orchestrator saves each output in the
article folder under the file name shown.

## Envelope (wraps every JSON output)

```json
{
  "task_id": "<slug>",
  "stage": "serp|brief|research|review|assets|publish",
  "agent": "<agent name>",
  "version": 1,
  "status": "draft|ready_for_review|changes_requested|approved|blocked|escalated",
  "inputs_used": ["00-brief.json", "02-research.json"],
  "payload": {},
  "self_qa": { "checks": [{ "id": "...", "result": "pass|fail", "note": "..." }], "score": 4.5 },
  "open_questions": [],
  "handoff_to": "<next stage>"
}
```

## `01-serp.json` (content-strategist)

```json
"payload": {
  "keyword": "...",
  "method": "dataforseo|websearch_fallback",
  "method_note": "If websearch_fallback: results are not localised per country.",
  "markets": [{
    "location": "Sydney,New South Wales,Australia",
    "keyword_used": "...",
    "checked": "YYYY-MM-DD",
    "top3": [{
      "rank": 1, "url": "...", "title": "...", "domain_type": "planner|directory|publisher|venue|tourism",
      "word_count": 0, "h2s": [], "angle": "...", "intent": "informational|commercial|transactional",
      "faqs": [], "cta_type": "...", "trust_signals": [], "gaps": [],
      "images": { "count": 0, "style": "..." }, "schema": [], "updated": "..."
    }]
  }],
  "cross_market_insights": [],
  "recommended_angle": "...",
  "reference_only_images": [{ "url": "...", "page": "...", "note": "style reference only, licence: none" }]
}
```

## `00-brief.json` (content-strategist)

```json
"payload": {
  "title": "...", "title_options": [],
  "primary_keyword": "...", "secondary_keywords": [],
  "audience": { "primary_persona": "...", "secondary_persona": "...", "anti_persona": "bargain_hunter", "notes": "..." },
  "funnel_stage": "awareness|consideration|decision",
  "search_intent": "...",
  "angle": "...",
  "serp_gaps_to_win": [],
  "outline": [{ "h2": "...", "answers": "...", "must_include": [] }],
  "must_include": [], "must_avoid": [],
  "word_count": [1600, 2200],
  "cta": { "primary": "<cta id>", "soft": "<line or null>" },
  "internal_links_planned": [{ "url": "...", "role": "hub|service|related|package" }],
  "categories": ["<primary>", "<secondary>"], "tags": [],
  "image_count": 6
}
```

## `02-research.json` (researcher)

```json
"payload": {
  "facts": [{ "id": "F-01", "claim": "...", "source_url": "...", "source_name": "...",
              "source_type": "official|venue|tourism|publisher|aggregator",
              "source_date": "YYYY-MM", "checked": "YYYY-MM-DD", "confidence": "high|medium|low",
              "use_note": "..." }],
  "legal": [{ "id": "F-..", "country": "...", "summary": "...", "source_url": "...", "checked": "..." }],
  "prices": [{ "id": "F-..", "item": "...", "amount": "From AUD ...", "source": "...", "needs_nic_signoff": true }],
  "brand_facts_used": [],
  "needs": [{ "id": "N-01", "what": "e.g. a real Tuscany wedding with consent", "who": "planning team" }]
}
```

## `03-draft-vN.md` (writer)

Markdown with YAML front matter:

```yaml
---
title: "..."
slug: "..."
seo_title: "..."
meta_description: "..."
excerpt: "..."
primary_keyword: "..."
categories: ["<primary>", "..."]
tags: []
cta: { primary: "<cta id>", soft: "..." }
key_takeaways: ["...", "..."]
image_slots:
  - { slot: hero, after: "H1", place: "...", season_time: "...", moment: "...", culture: "...", scale: "...", mood: "...", must_not_show: "..." }
claims_register:
  - { id: C-01, text: "...", fact_ref: F-01, status: sourced|needs }
links_register:
  - { id: L-01, type: internal, anchor: "...", url: "/concierge", role: service }
  - { id: L-02, type: external, anchor: "...", url: "https://...", purpose: "source for F-03", rel: "noopener" }
faq:
  - { q: "...", a: "..." }
changes_from_previous: []
---
# H1
...
```

Image slots appear in the body as `[IMAGE: <slot>]` on their own line.
Placeholders: `[[NEEDS: ...]]`, `[[LINK NEEDED: ...]]`.

## `04-reviews/vN/<dimension>.json` (reviewers and readers)

```json
"payload": {
  "dimension": "voice|accuracy|seo|reader:<persona_id>",
  "rubric": [{ "line": "...", "score": 4, "note": "..." }],
  "findings": [{ "severity": "blocker|major|minor", "location": "H2 'Getting there' / C-04 / L-02",
                 "quote": "exact text", "issue": "...", "required_fix": "..." }],
  "verdict": "approved|changes_requested"
}
```

ICP readers add:

```json
  "first_impression": { "keep_reading": true, "why": "..." },
  "reactions": [{ "quote": "...", "reaction": "interested|trust_up|trust_down|confused|bored|skeptical", "comment": "..." }],
  "fears_coverage": [{ "fear": "...", "status": "addressed|touched|ignored", "quote": "..." }],
  "unanswered_questions": [],
  "scores": { "relevance": 0, "trust": 0, "clarity": 0, "would_enquire": 0 },
  "decision": "enquire|save|forward|leave",
  "in_their_words": "..."
```

## `05-assets.json` (photo-curator)

```json
"payload": {
  "assets": [{
    "slot": "hero", "brief": { "place": "...", "season_time": "...", "moment": "...", "culture": "...", "scale": "...", "mood": "...", "must_not_show": "..." },
    "source_plan": "own_gallery|partner_kit|licensed_stock|ai_mood_only",
    "search_terms": [], "drive_candidates": [],
    "file_name": "tuscany-villa-ceremony-01.webp",
    "alt_text": "...", "caption": "...", "credit": "[[NEEDS: photographer]]",
    "licence_type": "[[NEEDS]]", "licence_expiry": null, "client_consent": null,
    "context_checks": ["landmarks match", "season matches", "no competitor branding", "reverse image search before use"]
  }],
  "pinterest_variants": true
}
```

## `publish-package.json` (copy-editor)

```json
"payload": {
  "title": "...", "slug": "...", "url": "/blog/<slug>",
  "seo_title": "...", "meta_description": "...", "excerpt": "...",
  "categories": ["<PRIMARY FIRST>", "..."], "primary_category": "...", "tags": [],
  "author": "[[NEEDS: named author]]",
  "key_takeaways": [], "cta": { "id": "...", "heading": "...", "body": "...", "button": "...", "url": "..." },
  "images": [{ "slot": "...", "file_name": "...", "alt_text": "...", "caption": "...", "credit": "...", "featured": true }],
  "links": [], "retro_links": [{ "from": "...", "anchor": "..." }],
  "faq": [], "schema_jsonld": {},
  "needs": [], "nic_signoff": [],
  "status": "draft"
}
```
