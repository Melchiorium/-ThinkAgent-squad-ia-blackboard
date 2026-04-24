from pathlib import Path

from orchestrator import run_v0_flow


def _load_project_brief() -> tuple[str, str]:
    brief_path = Path(__file__).resolve().parent.parent / "dev-agents" / "architect-context.md"
    if not brief_path.exists():
        raise FileNotFoundError(
            f"Missing project brief file: {brief_path}"
        )

    brief_text = brief_path.read_text(encoding="utf-8").strip()
    if not brief_text:
        raise ValueError(f"Project brief file is empty: {brief_path}")

    return brief_text, "dev-agents/architect-context.md"


def _format_block(title: str, content: str) -> str:
    body = content.strip() or "_Aucun contenu._"
    return f"## {title}\n\n{body}\n"


def _format_blackboard_markdown(blackboard: dict) -> str:
    revision_trace = blackboard["revision_trace"]
    lines = [
        "# Blackboard",
        "",
        _format_block("Project Brief", blackboard["project_brief"]),
        _format_block("Project Brief Source", blackboard["project_brief_source"]),
        _format_block("Initial PRD", revision_trace["initial_prd_draft"]),
        _format_block("Tech Input", blackboard["architecture_notes"]),
        _format_block("Growth Input", blackboard["gtm_notes"]),
        _format_block("Final Revised PRD", blackboard["prd_draft"]),
        _format_block("Revision Summary", revision_trace["revision_summary"]),
        "## Open Questions\n\n"
        + ("\n".join(f"- {item}" for item in blackboard["open_questions"]) or "_Aucune question._")
        + "\n",
        "## Risks\n\n"
        + ("\n".join(f"- {item}" for item in blackboard["risks"]) or "_Aucun risque._")
        + "\n",
        "## Decisions\n\n"
        + ("\n".join(f"- {item}" for item in blackboard["decisions"]) or "_Aucune décision._")
        + "\n",
        "## Conflicts\n\n"
        + ("\n".join(f"- {item}" for item in blackboard["conflicts"]) or "_Aucun conflit._")
        + "\n",
        "## Activity Log\n\n"
        + (
            "\n".join(
                f"- {entry['agent']}: {entry['event']}" for entry in blackboard["activity_log"]
            )
            or "_Aucune activité._"
        )
        + "\n",
    ]
    return "\n".join(lines)


def main() -> None:
    """Run the flow and write the main output files."""
    project_brief, project_brief_source = _load_project_brief()
    blackboard = run_v0_flow(project_brief, project_brief_source)
    outputs_dir = Path(__file__).resolve().parent.parent / "outputs"
    (outputs_dir / "prd.md").write_text(blackboard["prd_draft"], encoding="utf-8")
    (outputs_dir / "architecture.md").write_text(
        blackboard["architecture_notes"], encoding="utf-8"
    )
    (outputs_dir / "gtm.md").write_text(blackboard["gtm_notes"], encoding="utf-8")
    (outputs_dir / "project_brief.md").write_text(project_brief, encoding="utf-8")
    (outputs_dir / "blackboard.md").write_text(
        _format_blackboard_markdown(blackboard),
        encoding="utf-8",
    )
    activity_log_lines = [
        f"{entry['agent']} | {entry['event']} | {entry['source']}"
        for entry in blackboard["activity_log"]
    ]
    (outputs_dir / "activity_log.txt").write_text(
        "\n".join(activity_log_lines) + ("\n" if activity_log_lines else ""),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
