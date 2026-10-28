#!/usr/bin/env python3
"""Combine persona_review envelopes for one stage into a panel summary.

Usage:
  python3 studio/tools/aggregate_personas.py <run_dir> <brief|copy|page>

Reads every persona review envelope in <run_dir>/persona/ whose payload.stage
matches, applies the noise filter from studio/config.json (an issue must appear
in at least qa.persona_issue_min_runs runs of the same persona), and writes:
  brief -> 22-persona-brief-summary.json
  copy  -> 35-persona-copy-summary.json
  page  -> 63-persona-page-summary.json

Issues raised by two or more personas are ranked first as likely real problems.
An issue raised only by personas with status "assumption" never counts as a gate
blocker; it is reported as advisory.
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = {"brief": "22-persona-brief-summary.json", "copy": "35-persona-copy-summary.json", "page": "63-persona-page-summary.json"}


def norm(text):
    return " ".join(text.lower().split())[:120]


def persona_status(pid):
    path = ROOT / "personas" / f"{pid}.json"
    return json.loads(path.read_text()).get("status", "unknown") if path.exists() else "unknown"


def main(run_dir, stage):
    config = json.loads((ROOT / "config.json").read_text())
    min_runs = config["qa"]["persona_issue_min_runs"]
    run_dir = Path(run_dir)
    reviews = []
    for path in sorted((run_dir / "persona").glob("*.json")):
        env = json.loads(path.read_text())
        if env.get("payload_type") == "persona_review" and env["payload"].get("stage") == stage:
            reviews.append(env["payload"])
    if not reviews:
        print(f"no persona reviews for stage {stage} in {run_dir}/persona")
        return 1

    by_persona = defaultdict(list)
    for r in reviews:
        by_persona[r["persona_id"]].append(r)

    personas = {}
    issue_personas = defaultdict(set)
    issue_detail = {}
    for pid, runs in by_persona.items():
        decisions = Counter(r["decision"] for r in runs)
        unanswered = Counter(q["question"] for r in runs for q in r["questions_answered"] if q["answered"] != "yes")
        objections = Counter()
        severity = {}
        for r in runs:
            for o in r["objections_triggered"]:
                key = norm(o["objection"])
                objections[key] += 1
                severity[key] = max(severity.get(key, "minor"), o["severity"], key=["minor", "major", "blocker"].index)
                issue_detail.setdefault(key, o)
        kept = {k: n for k, n in objections.items() if n >= min(min_runs, len(runs))}
        for k in kept:
            issue_personas[k].add(pid)
        personas[pid] = {
            "status": persona_status(pid),
            "runs": len(runs),
            "decisions": dict(decisions),
            "majority_decision": decisions.most_common(1)[0][0],
            "unanswered_questions": [q for q, n in unanswered.items() if n >= min(min_runs, len(runs))],
            "objections": [{"objection": issue_detail[k]["objection"], "severity": severity[k], "runs": n} for k, n in kept.items()],
            "verbatims": [r["verbatim_reaction"] for r in runs],
        }

    ranked = sorted(issue_personas.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    issues = []
    for key, pids in ranked:
        sev = max((o["severity"] for p in pids for o in personas[p]["objections"] if norm(o["objection"]) == key), key=["minor", "major", "blocker"].index)
        issues.append({
            "objection": issue_detail[key]["objection"],
            "personas": sorted(pids),
            "scope": "cross_persona" if len(pids) > 1 else f"segment:{next(iter(pids))}",
            "severity": sev,
            "advisory_only": all(personas[p]["status"] == "assumption" for p in pids),
        })

    summary = {"stage": stage, "personas": personas, "issues": issues,
               "blockers": [i for i in issues if i["severity"] == "blocker" and not i["advisory_only"]]}
    out = run_dir / OUT[stage]
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"wrote {out}: {len(personas)} personas, {len(issues)} issues, {len(summary['blockers'])} blockers")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[2] not in OUT:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
