from pathlib import Path
import os

from llm import call_llm
from readiness import parse_readiness_block


def _load_tech_prompt() -> str:
    prompt_version = os.getenv("BLACKBOARD_PROMPT_VERSION", "V2").strip() or "V2"
    prompt_path = Path(__file__).resolve().parent.parent / f"prompts {prompt_version}" / "tech_prompt.md"
    return prompt_path.read_text(encoding="utf-8").strip()


def run_tech_agent(blackboard: dict, correction_tasks: list[dict] | None = None) -> dict:
    """Generate architecture notes from the shared blackboard."""
    system_prompt = _load_tech_prompt()
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

    architecture_notes = call_llm(system_prompt, user_prompt)
    blackboard["architecture_notes"] = architecture_notes
    blackboard["diagram_blueprint"] = _extract_diagram_blueprint(architecture_notes)
    tech_summary = _extract_section(
        architecture_notes, "## Review Summary"
    )
    tech_decisions = _extract_structural_decisions(
        architecture_notes,
        "### Structural Technical Decisions",
        limit=4,
    )
    tech_recommendations = _extract_bullet_list(
        architecture_notes, "## Requested Changes", limit=5
    )
    if not tech_decisions:
        tech_decisions = tech_recommendations[:2]
    tech_risks = _extract_bullet_list(architecture_notes, "## Risks", limit=3)
    tech_open_questions = _extract_bullet_list(architecture_notes, "## Open Questions", limit=3)
    blackboard["review_summaries"]["tech"] = tech_summary
    blackboard["requested_changes"]["tech"] = tech_recommendations
    blackboard["expert_contributions"]["tech"]["summary"] = tech_summary
    blackboard["expert_contributions"]["tech"]["decisions"] = tech_decisions
    blackboard["expert_contributions"]["tech"]["recommendations"] = tech_recommendations
    blackboard["expert_contributions"]["tech"]["risks"] = tech_risks
    blackboard["expert_contributions"]["tech"]["open_questions"] = tech_open_questions
    blackboard["expert_decisions"]["tech"] = tech_decisions
    blackboard["readiness"]["tech"] = parse_readiness_block(
        architecture_notes,
        "## Technical Readiness",
        blackboard["readiness"].get("known_tags", []),
    )
    if blackboard["readiness"]["tech"].get("parse_warning"):
        blackboard["activity_log"].append(
            {
                "agent": "tech_agent",
                "event": "technical_readiness_parse_warning",
                "source": "app/agents/tech_agent.py",
                "details": blackboard["readiness"]["tech"]["parse_warning"],
            }
        )
    blackboard["readiness"]["known_tags"] = _merge_known_tags(
        blackboard["readiness"].get("known_tags", []),
        blackboard["readiness"]["tech"].get("known_tags", []),
    )
    blackboard["risks"].extend(tech_risks)
    blackboard["open_questions"].extend(tech_open_questions)
    blackboard["activity_log"].append(
        {
            "agent": "tech_agent",
            "event": "architecture_notes_generated",
            "source": "app/agents/tech_agent.py",
        }
    )
    return blackboard


def _extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    capture = False
    collected = []
    target = _normalize_heading(heading)
    for line in lines:
        stripped = line.strip()
        if _normalize_heading(stripped) == target:
            capture = True
            continue
        if capture and stripped.startswith("## "):
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


def _extract_diagram_blueprint(text: str) -> str:
    section = _extract_section(text, "Diagram Blueprint")
    if section:
        return section
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


def _normalize_heading(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.lstrip("#").strip()
    return normalized


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
