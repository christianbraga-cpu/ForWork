# Payload specs

Every run file is an envelope (`envelope.schema.json`). This file defines the
`payload` for each `task_type`. Intake, fact ledger and page brief have full JSON
Schemas; the rest are specified here. Keep keys exactly as written so the
validator and downstream agents can rely on them.

## keyword_map (01a, keyword-researcher)

```json
{
  "market": "AU",
  "primary_keyword": {"term": "", "volume": 0, "kd": 0, "intent": "commercial", "cpc_aud": 0, "serp_url_count_checked": 10},
  "secondary_keywords": [{"term": "", "volume": 0, "intent": "", "assign_to_section": ""}],
  "questions": [{"question": "", "volume": 0, "source": "paa|semrush|research_doc"}],
  "excluded_keywords": [{"term": "", "reason": "brand_misfit|low_intent|owned_by_other_page|competitor_brand"}],
  "serp": {"features": ["ai_overview", "people_also_ask", "image_pack", "local_pack", "video"], "top_results": [{"position": 1, "url": "", "type": "venue|aggregator|planner|editorial"}]},
  "competitor_gaps": [{"competitor": "", "ranks_for": "", "position": 0, "we_rank": null}],
  "cannibalisation": {"conflicts": [{"term": "", "owned_by": "", "recommendation": ""}]},
  "current_rankings": [{"term": "", "position": 0}],
  "data_freshness": "YYYY-MM-DD"
}
```

## tech_audit (01b, technical-seo)

```json
{
  "mode": "requirements_only|full_audit|quick_audit",
  "findings": [{"id": "T-001", "area": "performance|indexing|schema|links|images|mobile|accessibility|markup", "severity": "blocker|high|medium|low", "issue": "", "evidence": "", "fix": ""}],
  "requirements": {
    "template": "package",
    "performance_budget": {"lcp_s": 2.5, "cls": 0.1, "hero_kb_mobile": 200, "gallery_kb": 120, "total_js_kb": 100},
    "schema_types": ["BreadcrumbList", "Product", "FAQPage"],
    "indexing": {"robots": "noindex until signoff", "canonical": ""},
    "markup_rules": ["one h1", "section ids match brief", "real <img> with width/height", "hero eager + fetchpriority=high, rest lazy"]
  },
  "existing_metrics": {"lighthouse": {}, "word_count": 0, "h1": "", "title": "", "meta_description": ""}
}
```

## ai_search_baseline (01c) and entity_plan (07b), ai-search-specialist

```json
{
  "queries_tested": [{"query": "", "engine": "chatgpt|google_ai_overview|perplexity|claude", "brand_mentioned": false, "competitors_mentioned": [], "cited_urls": []}],
  "entity_facts": [{"fact": "", "consistent_across": ["site", "gbp", "directories"], "inconsistencies": []}],
  "content_requirements": ["Direct-answer sentence for cost question in first 2 lines of #offers"],
  "actions": [{"action": "", "owner": "", "priority": "high|medium|low"}]
}
```

## link_plan (02b, linking-specialist)

```json
{
  "links_out_internal": [{"target": "", "anchor": "", "section_id": "", "target_status": "live|unverified", "reason": ""}],
  "links_out_external": [{"url": "", "anchor": "", "section_id": "", "rel": "|nofollow|sponsored", "reason": "official_source|press|vendor_credit"}],
  "backlink_tasks": [{"source": "", "anchor": "", "placement": "", "source_in_repo": false}],
  "registry_update": {"url": "", "page_type": "", "status": "draft", "primary_keyword": "", "approved_anchors": []},
  "registry_checks": {"anchor_conflicts": [], "click_depth": 0, "orphan_risk": false, "planned_urls_avoided": []}
}
```

## conversion_spec (02c, cro-specialist)

```json
{
  "primary_cta": {"label": "", "target": "#enquire"},
  "secondary_ctas": [{"label": "", "target": ""}],
  "cta_placements": [{"section_id": "", "cta": "", "reason": ""}],
  "form": {"endpoint": "<from page facts or existing page>", "hidden": {}, "fields": [{"name": "", "type": "", "required": true}], "carry_offer": true, "success_message": ""},
  "trust_placements": [{"section_id": "", "signal": "", "fact_id": ""}],
  "objection_handling": [{"persona_fear": "", "answer_location": "", "fact_ids": []}],
  "mobile": {"sticky_cta": true, "notes": ""},
  "tests_to_run_post_launch": [{"hypothesis": "", "metric": ""}]
}
```

## copy (04a, copywriter)

The page copy itself lives in `04a-copy.md` (one `## <section id>` per brief section,
with HTML-ready Markdown). The envelope payload:

```json
{
  "copy_file": "04a-copy.md",
  "title_tag": "",
  "meta_description": "",
  "og_title": "",
  "og_description": "",
  "h1": "",
  "sections": [{"id": "", "heading": "", "word_count": 0, "fact_ids_used": [], "keywords_used": [], "links_placed": [], "decision": "new|keep|change"}],
  "faqs": [{"question": "", "answer": "", "fact_ids": []}],
  "claims": [{"text": "", "fact_id": "", "risk": "high|medium|low"}],
  "placeholders": [{"text": "[[CONFIRM: ...]]", "section_id": "", "ask": ""}],
  "keyword_coverage": {"primary_in_title": true, "primary_in_h1": true, "primary_in_first_100_words": true, "secondaries_covered": 0, "secondaries_total": 0},
  "total_word_count": 0,
  "forbidden_terms_found": []
}
```

## image_plan (04b, visual-seo)

```json
{
  "images": [{
    "slot": "hero-01", "section_id": "", "role": "hero|carousel|gallery|space|room|region|compare|portrait",
    "filename": "", "asset_source": "venue_media_kit|own_shoot|photographer|placeholder",
    "alt": "", "caption": "", "credit": {"text": "", "url": ""},
    "licence": {"status": "confirmed|requested|unknown", "scope": ["web", "social", "editorial", "paid_ads"], "expiry": ""},
    "consent": "full|anonymised|none|not_applicable", "identifiable_minors": false, "ai_edited": false,
    "loading": "eager|lazy", "fetchpriority": "high|auto",
    "widths": [480, 768, 1200, 1600, 2400], "aspect_ratio": "3:2", "max_kb": 0
  }],
  "pinterest_variants": [{"slot": "", "ratio": "2:3"}],
  "video": [{"idea": "", "schema": "VideoObject"}],
  "shot_list_requests": ["Shots the page needs that we do not have"],
  "image_schema": "ImageObject with creator, creditText, copyrightNotice, license"
}
```

## build (04c, page-builder)

```json
{
  "site_file": "site/<path>/index.html",
  "notes_file": "site/<path>/NOTES.md",
  "implemented": {"sections": [], "schema_types": [], "links": 0, "images": 0, "form_endpoint": ""},
  "deviations": [{"from": "brief|copy|link_plan|conversion_spec|tech_requirements", "what": "", "why": ""}],
  "robots": "noindex",
  "checker_output": "Summary of tools/check_page.py run"
}
```

## qa_gate (05, fact-checker / brand-guardian / seo-qa / technical-qa)

```json
{
  "gate": "fact_gate|brand_gate|seo_gate|technical_gate",
  "verdict": "pass|pass_with_notes|fail",
  "checks": [{"id": "", "result": "pass|fail|n/a", "note": ""}],
  "issues": [{"id": "", "severity": "blocker|high|medium|low", "location": "section:<id> | selector | file:line", "quote": "", "issue": "", "fix_owner": "copywriter|visual-seo|page-builder|linking-specialist|cro-specialist|technical-seo|seo-strategist", "suggested_fix": ""}],
  "human_signoff_items": [{"item": "", "who": "price_approver|brand_owner|sme_planner|venue|dev_team"}],
  "attempt": 1
}
```

## icp_critique (05a, icp-critic)

```json
{
  "persona_id": "",
  "entry_query": "",
  "device": "mobile|desktop",
  "first_impression": {"stay_or_bounce": "stay|bounce", "reason": "", "quote": ""},
  "sections_read": [""],
  "sections_skipped": [{"section": "", "reason": ""}],
  "reactions": [{"quote": "", "section_id": "", "sentiment": "positive|negative|neutral", "impact": "high|medium|low", "comment": ""}],
  "unaddressed_fears": [""],
  "trust_signals_noticed": [""],
  "deal_breakers_triggered": [""],
  "images": {"feel_real": true, "comment": ""},
  "next_action": "enquire_now|save_and_compare|send_to_partner|back_to_google",
  "next_action_reason": "",
  "scores": {"relevance": 0, "trust": 0, "clarity": 0, "fear_resolution": 0, "brand_feel": 0, "enquiry_intent": 0},
  "score_reasons": {"relevance": "", "trust": "", "clarity": "", "fear_resolution": "", "brand_feel": "", "enquiry_intent": ""},
  "assumptions_used": [""]
}
```

## icp_synthesis (05b, persona-synthesizer)

```json
{
  "panel": [""],
  "score_table": [{"persona_id": "", "relevance": 0, "trust": 0, "clarity": 0, "fear_resolution": 0, "brand_feel": 0, "enquiry_intent": 0, "next_action": ""}],
  "consensus_issues": [{"issue": "", "personas": [], "quotes": [], "section_id": "", "priority": "fix_before_signoff"}],
  "segment_issues": [{"issue": "", "persona": "", "recommendation": "fix_here|serve_on_other_page|ignore", "reason": ""}],
  "conflicts": [{"between": [], "issue": "", "recommendation": ""}],
  "what_works": [{"quote": "", "personas": []}],
  "verdict": "ready|revise"
}
```

## revisions (05c, seo-strategist in arbitrate mode)

```json
{
  "round": 1,
  "tasks": [{"id": "R-001", "owner": "", "priority": "blocker|high|medium|low", "issue": "", "evidence": [""], "from": ["05-qa-fact"], "instruction": ""}],
  "decisions": [{"topic": "", "options": [], "chosen": "", "reason": ""}],
  "waived": [{"issue_id": "", "reason": ""}],
  "rerun": ["seo_gate", "icp_intl_couple"],
  "ready_for_signoff": false
}
```

## pr_plan (07a, digital-pr)

```json
{
  "link_gap": [{"domain": "", "links_to_competitors": [], "links_to_us": false, "type": "publication|venue|tourism_board|directory|blog"}],
  "prospects": [{"prospect": "", "type": "real_wedding_feature|vendor_credit|data_pr|expert_quote|unlinked_mention|award|podcast", "target_url_for_link": "", "relevance_score": 0, "audience_overlap": [], "consents_needed": [], "risk_flags": [], "requires_human_review": true}],
  "assets_needed": [""],
  "do_not_pursue": [{"prospect": "", "reason": ""}]
}
```

## measurement_plan (08, analytics-specialist)

```json
{
  "events": [{"name": "generate_lead", "trigger": "", "params": ["page_path", "offer", "guest_count"]}],
  "crm_mapping": {"system": "Zoho CRM", "lead_source_fields": {"page_path": "", "offer": "", "utm": ""}, "test_lead_required": true},
  "baseline": [{"metric": "", "value": "", "source": ""}],
  "checks": [{"day": 14, "metrics": ["indexed", "impressions", "primary_keyword_position"]}, {"day": 30, "metrics": []}, {"day": 90, "metrics": ["enquiries", "signed_contracts"]}],
  "kpis": [{"metric": "", "target": "", "by_day": 0}],
  "rank_tracking": {"tool": "semrush_position_tracking", "keywords": []}
}
```
