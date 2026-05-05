from pathlib import Path
import os

if __package__ and __package__.startswith("app"):
    from ..llm import call_llm
    from ..readiness import parse_readiness_block
else:
    from llm import call_llm
    from readiness import parse_readiness_block


def _load_growth_prompt() -> str:
    prompt_version = os.getenv("BLACKBOARD_PROMPT_VERSION", "V2").strip() or "V2"
    prompt_path = Path(__file__).resolve().parent.parent / f"prompts {prompt_version}" / "growth_prompt.md"
    return prompt_path.read_text(encoding="utf-8").strip()


def run_growth_agent(
    blackboard: dict, correction_tasks: list[dict] | None = None
) -> dict:
    """Generate GTM notes from the shared blackboard."""
    system_prompt = _load_growth_prompt()
    correction_tasks = correction_tasks or []
    known_tags = blackboard["readiness"].get("known_tags", [])
    mode = "Mode: correction" if correction_tasks else "Mode: review"
    user_prompt = (
        f"{mode}\n\n"
        f"Project brief:\n{blackboard['project_brief']}\n\n"
        f"PRD draft:\n{blackboard['prd_draft']}\n\n"
        f"{_format_known_tags(known_tags)}\n\n"
        f"{_format_correction_tasks(correction_tasks)}"
    )

    gtm_notes = call_llm(system_prompt, user_prompt)
    blackboard["gtm_notes"] = gtm_notes
    growth_summary = _extract_section(
        gtm_notes, "## Review Summary"
    )
    growth_decisions = _extract_structural_decisions(
        gtm_notes,
        "### 2 to 3 Structural GTM Decisions",
        limit=4,
    )
    growth_recommendations = _extract_bullet_list(
        gtm_notes, "## Requested Changes", limit=5
    )
    if not growth_decisions:
        growth_decisions = growth_recommendations[:2]
    growth_risks = _extract_bullet_list(gtm_notes, "## Risks", limit=3)
    growth_open_questions = _extract_bullet_list(gtm_notes, "## Open Questions", limit=3)
    blackboard["review_summaries"]["growth"] = growth_summary
    blackboard["requested_changes"]["growth"] = growth_recommendations
    blackboard["expert_contributions"]["growth"]["summary"] = growth_summary
    blackboard["expert_contributions"]["growth"]["decisions"] = growth_decisions
    blackboard["expert_contributions"]["growth"]["recommendations"] = growth_recommendations
    blackboard["expert_contributions"]["growth"]["risks"] = growth_risks
    blackboard["expert_contributions"]["growth"]["open_questions"] = growth_open_questions
    blackboard["expert_decisions"]["growth"] = growth_decisions
    blackboard["readiness"]["growth"] = parse_readiness_block(
        gtm_notes,
        "## GTM Readiness",
        blackboard["readiness"].get("known_tags", []),
    )
    blackboard["readiness"]["known_tags"] = _merge_known_tags(
        blackboard["readiness"].get("known_tags", []),
        blackboard["readiness"]["growth"].get("known_tags", []),
    )
    blackboard["risks"].extend(growth_risks)
    blackboard["open_questions"].extend(growth_open_questions)
    blackboard["activity_log"].append(
        {
            "agent": "growth_agent",
            "event": "gtm_notes_generated",
            "source": "app/agents/growth_agent.py",
        }
    )
    return blackboard


def _extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    capture = False
    collected = []
    for line in lines:
        if line.strip() == heading:
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            collected.append(line)
    return "\n".join(collected).strip()


def _extract_bullet_list(text: str, heading: str, limit: int) -> list[str]:
    section = _extract_section(text, heading)
    if not section:
        return []
    items = []
    for line in section.splitlines():
        stripped = line.strip()
        value = _extract_list_value(stripped)
        if value:
            items.append(value)
        if len(items) >= limit:
            break
    return items


def _extract_list_value(line: str) -> str:
    if line.startswith("- "):
        value = line[2:].strip()
    elif line.startswith("* "):
        value = line[2:].strip()
    else:
        parts = line.split(". ", 1)
        if len(parts) == 2 and parts[0].isdigit():
            value = parts[1].strip()
        else:
            return ""
    if value and value != "None":
        return value
    return ""


def _extract_structural_decisions(text: str, heading: str, limit: int) -> list[str]:
    section = _extract_section(text, heading)
    if not section:
        return []
    items = []
    for line in section.splitlines():
        stripped = line.strip()
        value = _extract_list_value(stripped)
        if value:
            items.append(value)
        if len(items) >= limit:
            break
    return items


def _format_correction_tasks(tasks: list[dict]) -> str:
    if not tasks:
        return "Targeted correction tasks:\n- None"
    lines = [
        "Targeted correction tasks:",
        "Treat each task as a gap-closure assignment, not a generic suggestion list.",
        "For each task, either resolve the blocker concretely or propose the smallest credible reduction path.",
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


def _merge_known_tags(existing: list[str], new: list[str]) -> list[str]:
    merged = []
    seen = set()
    for tag in list(existing) + list(new):
        if not tag or tag in seen:
            continue
        seen.add(tag)
        merged.append(tag)
    return merged


def _summarize_text(text: str, max_chars: int = 280) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[: max_chars - 3].rstrip() + "..."
