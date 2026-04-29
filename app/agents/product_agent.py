from copy import deepcopy
from pathlib import Path
import os
import re

from llm import call_llm
from readiness import parse_readiness_block


def _load_product_prompt() -> str:
    prompt_version = os.getenv("BLACKBOARD_PROMPT_VERSION", "V2").strip() or "V2"
    prompt_path = Path(__file__).resolve().parent.parent / f"prompts {prompt_version}" / "product_prompt.md"
    return prompt_path.read_text(encoding="utf-8").strip()


def _build_initial_user_prompt(blackboard: dict) -> str:
    return (
        "Mode: initial_draft\n\n"
        f"Project brief:\n{blackboard['project_brief']}"
    )


def _build_source_revision_user_prompt(blackboard: dict) -> str:
    source_artifacts = blackboard["source_artifacts"]
    evaluation = blackboard["executive_evaluation"] or "None"
    return (
        "Mode: revision\n\n"
        f"Source version:\n{blackboard['source_version'] or 'Unknown'}\n\n"
        f"Project brief:\n{source_artifacts['project_brief'] or blackboard['project_brief']}\n\n"
        f"Existing PRD:\n{source_artifacts['prd']}\n\n"
        f"Existing architecture:\n{source_artifacts['architecture']}\n\n"
        f"Existing GTM:\n{source_artifacts['gtm']}\n\n"
        f"CEO evaluation:\n{evaluation}\n\n"
        "Produce the first revised PRD draft for the second pass. "
        "Absorb the executive feedback first, keep the product framing disciplined, "
        "and make only the revisions that materially improve viability, launchability, and clarity."
    )


def _build_locking_user_prompt(blackboard: dict) -> str:
    expert_decisions = blackboard.get("expert_decisions", {})
    return (
        "Mode: final_locking_pass\n\n"
        "This is a final locking pass.\n"
        "Do not redesign the project.\n"
        "Do not add new ideas.\n"
        "Lock the MVP scope only.\n"
        "Keep previously deferred items deferred unless they are proof-critical.\n"
        "Remove or defer accessory features.\n"
        "Prefer narrower scope over broader scope.\n\n"
        f"Current final PRD:\n{blackboard['prd_draft']}\n\n"
        f"Retained decisions:\n{chr(10).join(f'- {item}' for item in blackboard['retained_decisions']) or '- None'}\n\n"
        f"Deferred decisions:\n{chr(10).join(f'- {item}' for item in blackboard['deferred_decisions']) or '- None'}\n\n"
        f"Rejected changes:\n{chr(10).join(f'- {item}' for item in blackboard['rejected_changes']) or '- None'}\n\n"
        f"Tech structural decisions:\n{chr(10).join(f'- {item}' for item in expert_decisions.get('tech', [])) or '- None'}\n\n"
        f"Growth structural decisions:\n{chr(10).join(f'- {item}' for item in expert_decisions.get('growth', [])) or '- None'}\n\n"
        f"Remaining open tensions:\n{chr(10).join(f'- {item}' for item in blackboard['unresolved_tensions']) or '- None'}\n\n"
        "Return the clean final product proposal first, then a separate structured block headed:\n"
        "## Product Locking\n"
        "Use exactly these subsections:\n"
        "- ### Confirmed In Scope\n"
        "- ### Confirmed Deferred\n"
        "- ### Confirmed Out Of Scope\n"
        "- ### Locking Note\n"
        "Keep each subsection short and use - None when empty."
    )


def _build_revision_user_prompt(
    blackboard: dict, correction_tasks: list[dict] | None = None
) -> str:
    correction_tasks = correction_tasks or []
    tech_recommendations = _get_recommendations(blackboard, "tech")
    growth_recommendations = _get_recommendations(blackboard, "growth")
    tech_summary = blackboard["expert_contributions"]["tech"]["summary"]
    growth_summary = blackboard["expert_contributions"]["growth"]["summary"]
    tech_decisions = blackboard["expert_decisions"]["tech"]
    growth_decisions = blackboard["expert_decisions"]["growth"]
    unresolved_tensions = blackboard["unresolved_tensions"]
    evaluation = blackboard["executive_evaluation"] or "None"
    known_tags = blackboard["readiness"].get("known_tags", [])
    mode = "Mode: correction" if correction_tasks else "Mode: revision"
    return (
        f"{mode}\n\n"
        f"Project brief:\n{blackboard['project_brief']}\n\n"
        f"Current PRD draft:\n{blackboard['prd_draft']}\n\n"
        f"CEO evaluation:\n{evaluation}\n\n"
        f"Tech summary:\n{tech_summary or 'None'}\n\n"
        f"Tech structural decisions:\n{chr(10).join(f'- {item}' for item in tech_decisions) or '- None'}\n\n"
        f"Tech recommendations:\n{chr(10).join(f'- {item}' for item in tech_recommendations) or '- None'}\n\n"
        f"Growth summary:\n{growth_summary or 'None'}\n\n"
        f"Growth structural decisions:\n{chr(10).join(f'- {item}' for item in growth_decisions) or '- None'}\n\n"
        f"Growth recommendations:\n{chr(10).join(f'- {item}' for item in growth_recommendations) or '- None'}\n\n"
        f"Unresolved tensions:\n{chr(10).join(f'- {item}' for item in unresolved_tensions) or '- None'}\n\n"
        f"{_format_known_tags(known_tags)}\n"
        f"{_format_correction_tasks(correction_tasks)}\n"
        "Revise the PRD by arbitrating between the structured expert recommendations. "
        "Retain only decisions that are necessary for MVP viability, launchability, trust, compliance, "
        "or core usability. Defer useful but non-essential ideas. Leave unresolved clarifications out of "
        "the PRD if they are not yet decided. Keep the result focused, disciplined, and MVP-first.\n\n"
        "After the clean PRD, add a separate system block headed exactly `## Product Arbitration`. "
        "For every Tech and Growth recommendation, choose exactly one bucket: Retained, Deferred, "
        "Rejected, or Open Points. Do not leave a recommendation in a generic 'needs arbitration' state. "
        "Use Open Points only when the project brief does not contain enough information to decide safely. "
        "Use exactly these subsections: `### Retained`, `### Deferred`, `### Rejected`, "
        "`### Open Points`, `### Rationales`."
    )


def run_product_agent(blackboard: dict) -> dict:
    """Generate the PRD draft from the shared blackboard."""
    system_prompt = _load_product_prompt()
    user_prompt = _build_initial_user_prompt(blackboard)

    prd_draft = call_llm(system_prompt, user_prompt)
    blackboard["prd_draft"] = prd_draft
    blackboard["prd_draft_initial"] = prd_draft
    blackboard["readiness"]["product"] = parse_readiness_block(
        prd_draft,
        ["## Product Readiness", "## Investment Readiness"],
        blackboard["readiness"].get("known_tags", []),
    )
    blackboard["readiness"]["known_tags"] = _merge_known_tags(
        blackboard["readiness"].get("known_tags", []),
        blackboard["readiness"]["product"].get("known_tags", []),
    )
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "prd_draft_generated",
            "source": "app/agents/product_agent.py",
        }
    )
    return blackboard


def run_product_second_pass_initial(blackboard: dict) -> dict:
    """Generate the first revised PRD draft from version 13 and CEO feedback."""
    system_prompt = _load_product_prompt()
    user_prompt = _build_source_revision_user_prompt(blackboard)

    prd_draft = call_llm(system_prompt, user_prompt)
    blackboard["prd_draft"] = prd_draft
    blackboard["prd_draft_initial"] = prd_draft
    blackboard["second_pass_draft"] = prd_draft
    blackboard["workflow_stage"] = "second_pass_initial"
    blackboard["second_pass_trace"]["initial_revision_draft"] = prd_draft
    blackboard["readiness"]["product"] = parse_readiness_block(
        prd_draft,
        ["## Product Readiness", "## Investment Readiness"],
        blackboard["readiness"].get("known_tags", []),
    )
    blackboard["readiness"]["known_tags"] = _merge_known_tags(
        blackboard["readiness"].get("known_tags", []),
        blackboard["readiness"]["product"].get("known_tags", []),
    )
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "second_pass_initial_prd_draft_generated",
            "source": "app/agents/product_agent.py",
        }
    )
    return blackboard


def run_product_revision(
    blackboard: dict, correction_tasks: list[dict] | None = None
) -> dict:
    """Revise the PRD draft after tech and growth review."""
    system_prompt = _load_product_prompt()
    _build_unresolved_tensions(blackboard)
    user_prompt = _build_revision_user_prompt(blackboard, correction_tasks)

    revised_output = call_llm(system_prompt, user_prompt)
    revised_prd_draft, arbitration_block = _split_prd_and_arbitration(revised_output)
    revised_prd_draft = _clean_prd_document(revised_prd_draft)
    raw_arbitration = _parse_product_arbitration_block(arbitration_block)
    blackboard["readiness"]["product"] = parse_readiness_block(
        revised_prd_draft,
        ["## Product Readiness", "## Investment Readiness"],
        blackboard["readiness"].get("known_tags", []),
    )
    blackboard["readiness"]["known_tags"] = _merge_known_tags(
        blackboard["readiness"].get("known_tags", []),
        blackboard["readiness"]["product"].get("known_tags", []),
    )
    arbitration = deepcopy(raw_arbitration)
    if not arbitration["parsed"]:
        arbitration_outcomes = _build_arbitration_outcomes(blackboard, revised_prd_draft)
        arbitration.update(
            {
                "retained": arbitration_outcomes["retained"],
                "deferred": arbitration_outcomes["deferred"],
                "rejected": arbitration_outcomes["rejected"],
                "open_points": arbitration_outcomes["open_points"],
                "rationales": [],
                "source": "heuristic_fallback",
                "parsed": False,
            }
        )
        blackboard["activity_log"].append(
            {
                "agent": "product_agent",
                "event": "product_arbitration_fallback_used",
                "source": "app/agents/product_agent.py",
                "details": "Structured Product Arbitration block was missing or malformed; fallback heuristics were used.",
            }
        )
    blackboard["arbitration"] = _build_arbitration_state(
        parsed_arbitration=arbitration,
        raw_parsed=raw_arbitration,
    )
    revision_trace = {
        "initial_prd_draft": blackboard["prd_draft_initial"],
        "tech_input": blackboard["architecture_notes"],
        "growth_input": blackboard["gtm_notes"],
        "revision_summary": (
            "Updated the PRD after tech and growth review to align scope, "
            "technical constraints, and go-to-market guidance."
        ),
    }
    blackboard["revision_trace"] = revision_trace
    if blackboard["workflow_stage"].startswith("second_pass"):
        blackboard["second_pass_trace"]["tech_input"] = blackboard["architecture_notes"]
        blackboard["second_pass_trace"]["growth_input"] = blackboard["gtm_notes"]
        blackboard["second_pass_trace"]["revision_summary"] = revision_trace["revision_summary"]
    blackboard["prd_draft"] = revised_prd_draft
    blackboard["retained_decisions"] = arbitration["retained"]
    blackboard["deferred_decisions"] = arbitration["deferred"]
    blackboard["rejected_changes"] = arbitration["rejected"]
    blackboard["open_points"] = arbitration["open_points"]
    blackboard["applied_changes"] = arbitration["retained"]
    blackboard["decisions"] = arbitration["retained"]
    blackboard["workflow_stage"] = (
        "second_pass_final" if blackboard["source_version"] else "first_pass_final"
    )
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "prd_draft_revised",
            "source": "app/agents/product_agent.py",
        }
    )
    return blackboard


def run_product_locking_pass(blackboard: dict) -> dict:
    """Apply the final Product-only locking pass."""
    system_prompt = _load_product_prompt()
    user_prompt = _build_locking_user_prompt(blackboard)

    locked_output = call_llm(system_prompt, user_prompt)
    locked_prd_draft, locking_block = _split_prd_and_block(locked_output, "product locking")
    locked_prd_draft = _clean_prd_document(locked_prd_draft)
    locking = _parse_product_locking_block(locking_block)
    if not locking["parsed"]:
        locking = _build_fallback_product_locking(blackboard, locked_prd_draft)
        blackboard["activity_log"].append(
            {
                "agent": "product_agent",
                "event": "product_locking_fallback_used",
                "source": "app/agents/product_agent.py",
                "details": "Structured Product Locking block was missing or malformed; fallback scope locking was used.",
            }
        )

    locking["applied"] = True
    blackboard["product_locking"] = locking
    blackboard["prd_draft"] = locked_prd_draft
    blackboard["workflow_stage"] = (
        "second_pass_locked" if blackboard["source_version"] else "first_pass_locked"
    )
    blackboard["readiness"]["product"] = parse_readiness_block(
        locked_prd_draft,
        ["## Product Readiness", "## Investment Readiness"],
        blackboard["readiness"].get("known_tags", []),
    )
    blackboard["readiness"]["known_tags"] = _merge_known_tags(
        blackboard["readiness"].get("known_tags", []),
        blackboard["readiness"]["product"].get("known_tags", []),
    )
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "product_locking_applied",
            "source": "app/agents/product_agent.py",
        }
    )
    blackboard = _reconcile_arbitration_with_deliverables(blackboard)
    return blackboard


def _get_recommendations(blackboard: dict, source: str) -> list[str]:
    recommendations = blackboard["expert_contributions"][source]["recommendations"]
    if recommendations:
        return recommendations
    return blackboard["requested_changes"][source]


def _format_correction_tasks(tasks: list[dict]) -> str:
    if not tasks:
        return "Targeted correction tasks:\n- None"
    lines = [
        "Targeted correction tasks:",
        "Treat each task as a gap-closure assignment owned by Product.",
        "For every task, either resolve it concretely in the PRD or state a credible reduction path.",
    ]
    for index, task in enumerate(tasks, start=1):
        contributors = ", ".join(task.get("contributors", [])) or "None"
        lines.extend(
            [
                f"{index}. Task: {task.get('task', '')}",
                f"   - Source Gap: {task.get('source_gap', '')}",
                f"   - Expected Output: {task.get('expected_output', '')}",
                f"   - Contributors: {contributors}",
            ]
        )
    return "\n".join(lines)


def _format_known_tags(known_tags: list[str]) -> str:
    if not known_tags:
        return "Known reusable tags:\n- None"
    return "Known reusable tags:\n" + "\n".join(f"- {tag}" for tag in known_tags)


def _summarize_text(text: str, max_chars: int = 280) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 3].rstrip() + "..."


def _merge_known_tags(existing: list[str], new: list[str]) -> list[str]:
    merged = []
    seen = set()
    for tag in list(existing) + list(new):
        if not tag or tag in seen:
            continue
        seen.add(tag)
        merged.append(tag)
    return merged


def _record_product_trace_checkpoint(
    blackboard: dict,
    stage: str,
    draft: str,
    note: str = "",
    loop: int | None = None,
    correction_tasks: list[dict] | None = None,
) -> None:
    product_trace = blackboard.setdefault("workflow_trace", {}).setdefault("checkpoints", [])
    excerpt = _draft_excerpt(draft)
    checkpoint = {
        "stage": stage,
        "loop": loop,
        "note": note,
        "excerpt": excerpt,
        "line_count": len([line for line in draft.splitlines() if line.strip()]),
        "char_count": len(draft.strip()),
        "correction_tasks": [
            {
                "owner": task.get("owner", ""),
                "task": task.get("task", ""),
                "source_gap": task.get("source_gap", ""),
                "expected_output": task.get("expected_output", ""),
                "contributors": list(task.get("contributors", [])),
                "tag": task.get("tag", ""),
            }
            for task in (correction_tasks or [])
        ],
    }
    product_trace.append(checkpoint)
    blackboard["product_trace"] = product_trace

    if not blackboard.get("product_initial_draft"):
        blackboard["product_initial_draft"] = draft
    if stage in {"revision", "second_pass_initial"} and not blackboard.get("product_revised_draft"):
        blackboard["product_revised_draft"] = draft
    if stage == "correction":
        blackboard["product_post_correction_drafts"].append(draft)
    if stage == "final_locking_pass":
        blackboard["product_locked_draft"] = draft


def _draft_excerpt(draft: str, max_lines: int = 4, max_chars: int = 280) -> str:
    lines = [line.strip() for line in draft.splitlines() if line.strip()]
    if not lines:
        return ""
    excerpt = " | ".join(lines[:max_lines])
    if len(excerpt) > max_chars:
        return excerpt[: max_chars - 3].rstrip() + "..."
    return excerpt


def _build_arbitration_outcomes(blackboard: dict, revised_prd_draft: str) -> dict[str, list[str]]:
    tech_recommendations = _get_recommendations(blackboard, "tech")
    growth_recommendations = _get_recommendations(blackboard, "growth")
    retained = []
    deferred = []
    rejected = []
    open_points = []

    for source, recommendations in (
        ("tech", tech_recommendations),
        ("growth", growth_recommendations),
    ):
        for recommendation in recommendations:
            normalized_source = source.capitalize()
            if _recommendation_is_retained(recommendation, revised_prd_draft):
                retained.append(f"{normalized_source}: {recommendation}")
            elif _recommendation_is_open_clarification(recommendation):
                open_points.append(f"{normalized_source}: {recommendation}")
            elif _recommendation_is_mvp_later(recommendation):
                deferred.append(f"{normalized_source}: {recommendation}")
            else:
                open_points.append(f"{normalized_source}: {recommendation}")

    open_points.extend(
        f"Tech: {item}" for item in blackboard["expert_contributions"]["tech"]["open_questions"]
    )
    open_points.extend(
        f"Growth: {item}" for item in blackboard["expert_contributions"]["growth"]["open_questions"]
    )
    open_points.extend(blackboard["unresolved_tensions"])

    return {
        "retained": retained,
        "deferred": deferred,
        "rejected": rejected,
        "open_points": open_points,
    }


def _build_fallback_product_locking(blackboard: dict, locked_prd_draft: str) -> dict:
    confirmed_in_scope = _dedupe_strings(blackboard["retained_decisions"] or [])
    confirmed_deferred = _dedupe_strings(blackboard["deferred_decisions"] or [])
    confirmed_out_of_scope = _dedupe_strings(blackboard["rejected_changes"] or [])
    locking_note = "Final MVP narrowed after Product closing pass."
    if blackboard["open_points"]:
        locking_note = (
            "Final MVP narrowed after Product closing pass with unresolved points intentionally deferred."
        )
    return {
        "applied": True,
        "confirmed_in_scope": confirmed_in_scope,
        "confirmed_deferred": confirmed_deferred,
        "confirmed_out_of_scope": confirmed_out_of_scope,
        "locking_note": locking_note,
        "raw": locked_prd_draft,
        "source": "heuristic_fallback",
        "parsed": False,
    }


def _build_arbitration_state(
    parsed_arbitration: dict,
    raw_parsed: dict | None = None,
    reconciled: dict | None = None,
    reconciliation_notes: list[str] | None = None,
) -> dict:
    state = deepcopy(parsed_arbitration)
    state["raw_parsed"] = deepcopy(raw_parsed or parsed_arbitration)
    state["reconciled"] = deepcopy(reconciled or parsed_arbitration)
    state["reconciliation_notes"] = list(reconciliation_notes or [])
    state.setdefault("warnings", [])
    return state


def _reconcile_arbitration_with_deliverables(blackboard: dict) -> dict:
    arbitration = blackboard.get("arbitration", {})
    raw_parsed = arbitration.get("raw_parsed") or arbitration
    if raw_parsed.get("source") != "heuristic_fallback":
        reconciliation_notes = [
            "Parsed Product Arbitration supplied by Product; heuristic reconciliation was not needed."
        ]
        blackboard["arbitration"] = _build_arbitration_state(
            parsed_arbitration=arbitration,
            raw_parsed=raw_parsed,
            reconciled=raw_parsed,
            reconciliation_notes=reconciliation_notes,
        )
        blackboard["retained_decisions"] = list(raw_parsed.get("retained", []))
        blackboard["deferred_decisions"] = list(raw_parsed.get("deferred", []))
        blackboard["rejected_changes"] = list(raw_parsed.get("rejected", []))
        blackboard["open_points"] = list(raw_parsed.get("open_points", []))
        blackboard["applied_changes"] = list(raw_parsed.get("retained", []))
        blackboard["decisions"] = list(raw_parsed.get("retained", []))
        blackboard["activity_log"].append(
            {
                "agent": "product_agent",
                "event": "arbitration_reconciled",
                "source": "app/agents/product_agent.py",
                "details": reconciliation_notes[0],
            }
        )
        return blackboard

    deliverable_text = "\n\n".join(
        [
            blackboard.get("prd_draft", ""),
            blackboard.get("architecture_notes", ""),
            blackboard.get("gtm_notes", ""),
        ]
    ).lower()

    reconciled = deepcopy(raw_parsed)
    reconciled["source"] = "reconciled"
    reconciled["warnings"] = []
    reconciliation_notes = []

    for bucket in ("deferred", "rejected", "open_points"):
        for item in raw_parsed.get(bucket, []):
            if _item_appears_in_deliverables(item, deliverable_text):
                note = (
                    f"Potential contradiction: {bucket} item appears in the final deliverables: {item}"
                )
                if note not in reconciliation_notes:
                    reconciliation_notes.append(note)
                if note not in reconciled["warnings"]:
                    reconciled["warnings"].append(note)

    locking_note = blackboard.get("product_locking", {}).get("locking_note")
    if locking_note:
        reconciled["rationales"] = _dedupe_strings(
            list(raw_parsed.get("rationales", [])) + [locking_note]
        )
    else:
        reconciled["rationales"] = _dedupe_strings(list(raw_parsed.get("rationales", [])))

    if not reconciliation_notes:
        reconciliation_notes.append(
            "No obvious contradictions found between arbitration and the final deliverables."
        )

    blackboard["arbitration"] = _build_arbitration_state(
        parsed_arbitration=arbitration,
        raw_parsed=raw_parsed,
        reconciled=reconciled,
        reconciliation_notes=reconciliation_notes,
    )
    blackboard["retained_decisions"] = list(raw_parsed.get("retained", []))
    blackboard["deferred_decisions"] = list(raw_parsed.get("deferred", []))
    blackboard["rejected_changes"] = list(raw_parsed.get("rejected", []))
    blackboard["open_points"] = list(raw_parsed.get("open_points", []))
    blackboard["applied_changes"] = list(raw_parsed.get("retained", []))
    blackboard["decisions"] = list(raw_parsed.get("retained", []))
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "arbitration_reconciled",
            "source": "app/agents/product_agent.py",
            "details": "; ".join(reconciliation_notes),
        }
    )
    return blackboard


def _item_appears_in_deliverables(item: str, deliverable_text: str) -> bool:
    if not item or not deliverable_text:
        return False
    normalized_deliverables = _normalize_match_text(deliverable_text)
    normalized_item = _normalize_match_text(item)
    if normalized_item and normalized_item in normalized_deliverables:
        return True
    for phrase in _recommendation_phrases(item):
        if _normalize_match_text(phrase) in normalized_deliverables:
            return True
    return _has_strong_token_overlap(item, deliverable_text)


def _recommendation_is_retained(recommendation: str, revised_prd_draft: str) -> bool:
    text = _normalize_match_text(revised_prd_draft)
    phrases = _recommendation_phrases(recommendation)
    if any(_normalize_match_text(phrase) in text for phrase in phrases):
        return True
    return _has_strong_token_overlap(recommendation, revised_prd_draft)


def _recommendation_phrases(recommendation: str) -> list[str]:
    normalized = recommendation.lower().replace("**", "")
    fragments = []
    if ":" in normalized:
        title, detail = normalized.split(":", 1)
        title = title.strip(" -")
        detail = detail.strip(" -.")
        if title:
            fragments.append(title)
        if detail:
            fragments.extend(_long_phrases(detail))
    else:
        fragments.extend(_long_phrases(normalized))
    return [fragment for fragment in fragments if len(fragment) >= 12]


def _recommendation_is_open_clarification(recommendation: str) -> bool:
    normalized = recommendation.lower().lstrip("*- ").strip()
    return normalized.startswith(
        ("clarify ", "specify ", "define ", "detail ", "outline ", "confirm ")
    )


def _recommendation_is_mvp_later(recommendation: str) -> bool:
    normalized = recommendation.lower()
    later_markers = (
        "admin tool",
        "dashboard",
        "incentive system",
        "referral",
        "dynamic pricing",
        "weekly or monthly",
        "package pricing",
        "chat feature",
        "messaging feature",
        "advanced",
        "optimization",
    )
    return any(marker in normalized for marker in later_markers)


def _long_phrases(text: str) -> list[str]:
    cleaned = " ".join(text.split())
    if not cleaned:
        return []
    parts = [part.strip(" -.,()") for part in cleaned.split(",")]
    candidates = [cleaned]
    candidates.extend(parts)
    return [candidate for candidate in candidates if len(candidate) >= 12]


def _normalize_match_text(value: str) -> str:
    normalized = value.lower().replace("`", "").replace("**", "")
    normalized = re.sub(r"[_/-]+", " ", normalized)
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def _has_strong_token_overlap(needle: str, haystack: str) -> bool:
    needle_tokens = _content_tokens(needle)
    if len(needle_tokens) < 3:
        return False
    haystack_tokens = set(_content_tokens(haystack))
    overlap = [token for token in needle_tokens if token in haystack_tokens]
    return len(overlap) >= min(4, len(needle_tokens)) and len(overlap) / len(needle_tokens) >= 0.55


def _content_tokens(value: str) -> list[str]:
    stopwords = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "be",
        "before",
        "by",
        "for",
        "from",
        "in",
        "into",
        "is",
        "it",
        "make",
        "must",
        "of",
        "or",
        "pass",
        "should",
        "the",
        "through",
        "to",
        "with",
    }
    normalized = _normalize_match_text(value)
    return [
        token
        for token in normalized.split()
        if len(token) >= 4 and token not in stopwords
    ]


def _extract_inline_value(line: str) -> str:
    if ":" not in line:
        return ""
    value = line.split(":", 1)[1].strip()
    return value if value else ""


def _extract_list_item(line: str) -> str:
    if line.startswith("- "):
        return line[2:].strip()
    if line.startswith("* "):
        return line[2:].strip()
    if ". " in line:
        prefix, value = line.split(". ", 1)
        if prefix.isdigit():
            return value.strip()
    return ""


def _normalize_heading(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.lstrip("#").strip()
    return normalized


def _split_prd_and_block(text: str, heading: str) -> tuple[str, str]:
    lines = text.splitlines()
    target = _normalize_heading(heading)
    block_index = None
    for index, line in enumerate(lines):
        if _normalize_heading(line) == target:
            block_index = index
            break
    if block_index is None:
        return text, ""
    return "\n".join(lines[:block_index]).strip(), "\n".join(lines[block_index:]).strip()


def _parse_product_locking_block(text: str) -> dict:
    locking = {
        "applied": False,
        "confirmed_in_scope": [],
        "confirmed_deferred": [],
        "confirmed_out_of_scope": [],
        "locking_note": "",
        "raw": text.strip(),
        "source": "parsed",
        "parsed": False,
    }
    if not text.strip():
        return locking

    current_bucket = ""
    seen_sections = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        normalized = _normalize_heading(line)
        if normalized == "product locking":
            continue
        if normalized == "confirmed in scope":
            current_bucket = "confirmed_in_scope"
            seen_sections.add(current_bucket)
            continue
        if normalized == "confirmed deferred":
            current_bucket = "confirmed_deferred"
            seen_sections.add(current_bucket)
            continue
        if normalized == "confirmed out of scope":
            current_bucket = "confirmed_out_of_scope"
            seen_sections.add(current_bucket)
            continue
        if normalized == "locking note":
            current_bucket = "locking_note"
            seen_sections.add(current_bucket)
            continue

        item = _extract_list_item(line)
        if item and current_bucket and current_bucket != "locking_note":
            if item.lower() != "none":
                locking[current_bucket].append(item)
            continue

        if current_bucket == "locking_note" and line.lower() != "none":
            locking["locking_note"] = (
                f"{locking['locking_note']} {line}".strip() if locking["locking_note"] else line
            )

    locking["parsed"] = bool(seen_sections)
    return locking


def _dedupe_strings(values: list[str]) -> list[str]:
    result = []
    seen = set()
    for value in values:
        cleaned = " ".join(value.split())
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        result.append(cleaned)
    return result


def _build_unresolved_tensions(blackboard: dict) -> list[str]:
    tensions = []
    tech_recommendations = _get_recommendations(blackboard, "tech")
    growth_recommendations = _get_recommendations(blackboard, "growth")
    tech_opens = blackboard["expert_contributions"]["tech"]["open_questions"]
    growth_opens = blackboard["expert_contributions"]["growth"]["open_questions"]

    for item in tech_recommendations[1:]:
        tensions.append(f"Tech recommendation needing arbitration: {item}")
    for item in growth_recommendations[1:]:
        tensions.append(f"Growth recommendation needing arbitration: {item}")
    for item in tech_opens:
        tensions.append(f"Tech open question: {item}")
    for item in growth_opens:
        tensions.append(f"Growth open question: {item}")

    blackboard["unresolved_tensions"] = tensions
    return tensions


def _split_prd_and_arbitration(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    arbitration_index = None
    for index, line in enumerate(lines):
        if _normalize_heading(line) == "product arbitration":
            arbitration_index = index
            break
    if arbitration_index is None:
        return text, ""
    return "\n".join(lines[:arbitration_index]).strip(), "\n".join(lines[arbitration_index:]).strip()


def _parse_product_arbitration_block(text: str) -> dict:
    arbitration = {
        "retained": [],
        "deferred": [],
        "rejected": [],
        "open_points": [],
        "rationales": [],
        "raw": text.strip(),
        "source": "parsed",
        "parsed": False,
    }
    if not text.strip():
        return arbitration

    current_bucket = ""
    seen_sections = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        normalized = _normalize_heading(line)
        if normalized == "product arbitration":
            continue
        if normalized == "retained":
            current_bucket = "retained"
            seen_sections.add(current_bucket)
            inline = _extract_inline_value(line)
            if inline and inline.lower() != "none":
                arbitration[current_bucket].append(inline)
            continue
        if normalized == "deferred":
            current_bucket = "deferred"
            seen_sections.add(current_bucket)
            inline = _extract_inline_value(line)
            if inline and inline.lower() != "none":
                arbitration[current_bucket].append(inline)
            continue
        if normalized == "rejected":
            current_bucket = "rejected"
            seen_sections.add(current_bucket)
            inline = _extract_inline_value(line)
            if inline and inline.lower() != "none":
                arbitration[current_bucket].append(inline)
            continue
        if normalized == "open points":
            current_bucket = "open_points"
            seen_sections.add(current_bucket)
            inline = _extract_inline_value(line)
            if inline and inline.lower() != "none":
                arbitration[current_bucket].append(inline)
            continue
        if normalized == "rationales":
            current_bucket = "rationales"
            seen_sections.add(current_bucket)
            inline = _extract_inline_value(line)
            if inline and inline.lower() != "none":
                arbitration[current_bucket].append(inline)
            continue

        item = _extract_list_item(line)
        if item and current_bucket:
            if item.lower() != "none":
                arbitration[current_bucket].append(item)
            continue

        if current_bucket and line.lower() != "none":
            arbitration[current_bucket].append(line)

    arbitration["parsed"] = bool(seen_sections)
    return arbitration


def _clean_prd_document(text: str) -> str:
    forbidden_headings = (
        "[please note",
        "## architecture notes",
        "## go-to-market notes",
        "## Architecture Notes",
        "## Review Summary",
        "## Requested Changes",
        "## Product Arbitration",
        "## Risks",
        "## Growth Review Notes",
        "## Tech Review Notes",
        "**Review Summary**",
        "**Requested Changes:**",
        "**Risks:**",
        "**Tech Review Notes**",
        "**Growth Review Notes**",
        "### Retained",
        "### Deferred",
        "### Rejected",
        "### Open Points",
        "### Rationales",
    )
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if not cleaned_lines and stripped.lower().startswith("[please note"):
            continue
        if stripped in forbidden_headings:
            break
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines).strip()
