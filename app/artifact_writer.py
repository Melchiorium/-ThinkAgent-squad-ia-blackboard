from __future__ import annotations

from pathlib import Path
import shutil

if __package__ and __package__.startswith("app"):
    from .architecture_render import render_architecture_diagram
    from .blackboard_items import list_items
    from .run_documents import list_documents, read_named_document
    from .run_store import append_activity_log_entry, write_text_file
    from .v4_parsing import extract_section
    from .readiness import group_tagged_items, render_tagged_item
else:
    from architecture_render import render_architecture_diagram
    from blackboard_items import list_items
    from run_documents import list_documents, read_named_document
    from run_store import append_activity_log_entry, write_text_file
    from v4_parsing import extract_section
    from readiness import group_tagged_items, render_tagged_item


def write_run_artifacts(
    output_dir: Path,
    blackboard: dict,
    project_brief_text: str,
    evaluator_report_text: str = "",
) -> None:
    (output_dir / "project-brief.md").write_text(project_brief_text, encoding="utf-8")
    (output_dir / "prd.md").write_text(blackboard["prd_draft"], encoding="utf-8")
    (output_dir / "architecture.md").write_text(
        blackboard["architecture_notes"], encoding="utf-8"
    )
    artifact_state = render_architecture_diagram(output_dir, blackboard)
    blackboard.setdefault("artifacts", {}).update(artifact_state)
    if artifact_state.get("architecture_visual_warning"):
        blackboard["activity_log"].append(
            {
                "agent": "main",
                "event": "architecture_visual_warning",
                "source": "app/main.py",
                "details": artifact_state["architecture_visual_warning"],
            }
        )
    (output_dir / "gtm.md").write_text(blackboard["gtm_notes"], encoding="utf-8")
    (output_dir / "blackboard.md").write_text(
        _format_blackboard_markdown(blackboard),
        encoding="utf-8",
    )
    activity_log_lines = [_format_activity_log_entry(entry) for entry in blackboard["activity_log"]]
    (output_dir / "activity_log.txt").write_text(
        "\n".join(activity_log_lines) + ("\n" if activity_log_lines else ""),
        encoding="utf-8",
    )
    if evaluator_report_text:
        (output_dir / "evaluator-report.md").write_text(
            evaluator_report_text,
            encoding="utf-8",
        )


def write_v4_run_artifacts(
    run_state: dict,
    output_dir: Path,
    evaluator_report_text: str = "",
) -> None:
    workspace = run_state["workspace"]
    final_output_dir = workspace.final_outputs_dir
    final_output_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    project_brief_text = str(run_state.get("project_brief", "")).strip()
    project_brief_source = str(run_state.get("project_brief_source", "")).strip()
    project_name = str(run_state.get("project_name", "")).strip()

    product_doc = read_named_document(workspace, "product", "PRD_FINAL.md")
    growth_doc = read_named_document(workspace, "growth", "GTM_FINAL.md")
    tech_doc = read_named_document(workspace, "tech", "Architecture_FINAL.md")

    _write_final_text(final_output_dir / "project-brief.md", project_brief_text)
    _write_final_text(final_output_dir / "prd.md", product_doc)
    _write_final_text(final_output_dir / "architecture.md", tech_doc)

    artifact_state = render_architecture_diagram(
        final_output_dir,
        {
            "architecture_notes": tech_doc,
            "mermaid_diagram": "",
        },
    )
    _record_v4_artifact_state(workspace, artifact_state)

    _write_final_text(final_output_dir / "gtm.md", growth_doc)
    _write_final_text(
        final_output_dir / "blackboard.md",
        _format_v4_blackboard_markdown(
            run_state,
            project_name=project_name,
            project_brief_source=project_brief_source,
            product_doc=product_doc,
            growth_doc=growth_doc,
            tech_doc=tech_doc,
            artifact_state=artifact_state,
        ),
    )
    _write_final_text(final_output_dir / "activity_log.txt", _read_activity_log(workspace))
    if evaluator_report_text:
        _write_final_text(final_output_dir / "evaluator-report.md", evaluator_report_text)

    _mirror_directory_contents(final_output_dir, output_dir)


def _write_final_text(path: Path, content: str) -> None:
    write_text_file(path, content.rstrip("\n") + ("\n" if content else ""))


def _mirror_directory_contents(source_dir: Path, target_dir: Path) -> None:
    for source_path in source_dir.iterdir():
        target_path = target_dir / source_path.name
        if source_path.is_dir():
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
            continue
        shutil.copy2(source_path, target_path)


def _read_activity_log(workspace) -> str:
    activity_log_path = workspace.activity_log_path
    if not activity_log_path.exists():
        return ""
    return activity_log_path.read_text(encoding="utf-8").rstrip()


def _format_v4_blackboard_markdown(
    run_state: dict,
    *,
    project_name: str,
    project_brief_source: str,
    product_doc: str,
    growth_doc: str,
    tech_doc: str,
    artifact_state: dict,
) -> str:
    workspace = run_state["workspace"]
    items = list_items(workspace)
    summary_blocks = run_state.get("summaries", {})
    document_names = {
        "product": ", ".join(list_documents(workspace, "product")) or "None",
        "growth": ", ".join(list_documents(workspace, "growth")) or "None",
        "tech": ", ".join(list_documents(workspace, "tech")) or "None",
    }
    open_items = [item for item in items if item.get("status") == "OPEN"]
    answered_items = [item for item in items if item.get("status") != "OPEN"]

    lines = [
        "# Blackboard",
        "",
        _format_block("Run Id", workspace.run_id),
        _format_block("Project Name", project_name),
        _format_block("Project Brief Source", project_brief_source),
        _format_block("Workspace Root", str(workspace.root)),
        _format_v4_document_index(document_names),
        _format_v4_summary_section(summary_blocks),
        _format_v4_item_section("Open Items", open_items),
        _format_v4_residual_document_gaps_section(
            {
                "product": product_doc,
                "growth": growth_doc,
                "tech": tech_doc,
            }
        ),
        _format_v4_item_section("Resolved Items", answered_items),
        _format_v4_decisions_section(
            {
                "product": product_doc,
                "growth": growth_doc,
                "tech": tech_doc,
            }
        ),
        _format_block(
            "Architecture Markdown Ready",
            str(bool(artifact_state.get("architecture_markdown_ready"))),
        ),
        _format_block(
            "Architecture Visual Ready",
            str(bool(artifact_state.get("architecture_visual_ready"))),
        ),
        _format_block(
            "Architecture Visual Status",
            artifact_state.get("architecture_visual_status", ""),
        ),
        _format_block(
            "Architecture Visual Warning",
            artifact_state.get("architecture_visual_warning", ""),
        ),
        _format_block(
            "Architecture Mermaid Ready",
            str(bool(artifact_state.get("architecture_mermaid_ready"))),
        ),
        _format_block(
            "Architecture Mermaid Source",
            artifact_state.get("architecture_mermaid_source", ""),
        ),
        _format_block(
            "Architecture Image Path",
            artifact_state.get("architecture_image_path", ""),
        ),
        _format_block("Activity Log", _read_activity_log(workspace)),
    ]
    return "\n".join(lines)


def _record_v4_artifact_state(workspace, artifact_state: dict) -> None:
    details = (
        f"markdown_ready={bool(artifact_state.get('architecture_markdown_ready'))}; "
        f"mermaid_source_ready={bool(artifact_state.get('architecture_mermaid_ready'))}; "
        f"png_ready={bool(artifact_state.get('architecture_image_ready'))}; "
        f"visual_status={artifact_state.get('architecture_visual_status', '')}"
    )
    warning = str(artifact_state.get("architecture_visual_warning", "")).strip()
    if warning:
        details = f"{details}; warning={warning}"
    append_activity_log_entry(
        workspace,
        {
            "agent": "artifact_writer",
            "event": "final_artifact_status",
            "source": "app/artifact_writer.py",
            "details": details,
        },
    )


def _format_v4_document_index(document_names: dict[str, str]) -> str:
    lines = ["## Documents", ""]
    for agent, filename in document_names.items():
        lines.append(f"- {agent}: {filename}")
    return "\n".join(lines)


def _format_v4_summary_section(summary_blocks: dict) -> str:
    if not summary_blocks:
        return "## Summaries\n\n- None"
    lines = ["## Summaries", ""]
    for name, summary in summary_blocks.items():
        lines.extend(
            [
                f"### {name}",
                f"- Source document: {summary.get('source_document', '')}",
                f"- Source hash: {summary.get('source_hash', '')}",
                f"- Scope: {summary.get('scope', '')}",
                "- Key decisions:",
            ]
        )
        lines.extend(f"  - {value}" for value in summary.get("key_decisions", []) or ["None"])
        lines.append("- Unresolved questions:")
        lines.extend(f"  - {value}" for value in summary.get("unresolved_questions", []) or ["None"])
        lines.append("- Critical risks:")
        lines.extend(f"  - {value}" for value in summary.get("critical_risks", []) or ["None"])
    return "\n".join(lines)


def _format_v4_item_section(title: str, items: list[dict]) -> str:
    if not items:
        return f"## {title}\n\n- None"
    lines = [f"## {title}", ""]
    for item in items:
        lines.extend(
            [
                f"### {item['id']}",
                f"- Type: {item['type']}",
                f"- Author: {item['author']}",
                f"- Targets: {', '.join(item.get('targets', [])) or 'None'}",
                f"- Priority: {item['priority']}",
                f"- Status: {item['status']}",
                f"- Tags: {', '.join(item.get('tags', [])) or 'None'}",
                f"- Title: {item['title']}",
                f"- Content: {item['content']}",
            ]
        )
    return "\n".join(lines)


def _format_v4_residual_document_gaps_section(latest_documents: dict[str, str]) -> str:
    gaps = _collect_v4_residual_document_gaps(latest_documents)
    if not gaps:
        return "## Residual Document Gaps\n\n- None"
    lines = ["## Residual Document Gaps", ""]
    lines.extend(f"- {gap}" for gap in gaps)
    return "\n".join(lines)


def _collect_v4_residual_document_gaps(latest_documents: dict[str, str]) -> list[str]:
    readiness = {
        "product": _extract_v4_readiness(latest_documents["product"], "Product Readiness"),
        "growth": _extract_v4_readiness(latest_documents["growth"], "GTM Readiness"),
        "tech": _extract_v4_readiness(latest_documents["tech"], "Technical Readiness"),
    }
    gaps: list[str] = []
    product_status = readiness["product"]["status"]
    for role in ("growth", "tech"):
        peer_status = readiness[role]["status"]
        if product_status == "READY" and peer_status and peer_status != "READY":
            gaps.append(
                f"Product readiness is READY while {_role_label(role)} readiness is {peer_status}."
            )

    for role, role_readiness in readiness.items():
        status = role_readiness["status"]
        if status and status != "READY":
            gaps.append(f"{_role_label(role)} readiness is {status}.")
        for gap in role_readiness["blocking_gaps"]:
            gaps.append(f"{_role_label(role)} blocking gap: {gap}")
        for improvement in role_readiness["required_improvements"]:
            gaps.append(f"{_role_label(role)} required improvement: {improvement}")

    product_arbitration = extract_section(latest_documents["product"], "Product Arbitration")
    for open_point in _extract_v4_subsection_items(product_arbitration, "Open Points"):
        gaps.append(f"Product open point: {open_point}")
    for role, section_name in (("growth", "Open Questions"), ("tech", "Open Questions")):
        for question in _extract_v4_section_items(latest_documents[role], section_name):
            gaps.append(f"{_role_label(role)} open question: {question}")
    return _dedupe_preserving_order(gaps)


def _extract_v4_readiness(document_text: str, heading: str) -> dict[str, object]:
    readiness_text = extract_section(document_text, heading)
    return {
        "status": _extract_v4_status(readiness_text),
        "blocking_gaps": _extract_v4_labeled_list(readiness_text, "Blocking Gaps"),
        "required_improvements": _extract_v4_labeled_list(
            readiness_text,
            "Required Improvements",
        ),
    }


def _extract_v4_status(section_text: str) -> str:
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("status:"):
            return stripped.split(":", 1)[1].strip().upper()
    return ""


def _extract_v4_labeled_list(section_text: str, label: str) -> list[str]:
    target = _normalize_v4_gap_text(label)
    current = ""
    items: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current = _normalize_v4_gap_text(stripped[:-1])
            continue
        if current != target:
            continue
        text = _clean_v4_list_item(stripped)
        if text and not _is_v4_absence_text(text):
            items.append(text)
    return items


def _extract_v4_section_items(document_text: str, heading: str) -> list[str]:
    return _material_v4_lines(extract_section(document_text, heading))


def _extract_v4_subsection_items(section_text: str, subsection_heading: str) -> list[str]:
    target = _normalize_v4_gap_text(subsection_heading)
    capture = False
    lines: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("### "):
            if capture:
                break
            capture = _normalize_v4_gap_text(stripped[4:]) == target
            continue
        if capture:
            lines.append(line)
    return _material_v4_lines("\n".join(lines))


def _material_v4_lines(text: str) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("### "):
            continue
        cleaned = _clean_v4_list_item(stripped)
        if cleaned and not _is_v4_absence_text(cleaned):
            items.append(cleaned)
    return items


def _clean_v4_list_item(text: str) -> str:
    return text.strip().lstrip("-*").strip()


def _is_v4_absence_text(text: str) -> bool:
    normalized = _normalize_v4_gap_text(text)
    return (
        normalized in {"none", "n/a"}
        or normalized.startswith("no ")
        and any(
            marker in normalized
            for marker in (
                "identified",
                "remain",
                "recorded",
                "required",
                "open question",
                "blocking gap",
            )
        )
    )


def _normalize_v4_gap_text(text: str) -> str:
    normalized = str(text).strip().lower()
    normalized = normalized.lstrip("-*").strip()
    return normalized.rstrip(".?!").strip()


def _dedupe_preserving_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        key = _normalize_v4_gap_text(value)
        if key in seen:
            continue
        seen.add(key)
        result.append(value)
    return result


def _role_label(role: str) -> str:
    return {"product": "Product", "growth": "Growth", "tech": "Tech"}.get(role, role)


def _format_v4_decisions_section(latest_documents: dict[str, str]) -> str:
    product_arbitration = extract_section(latest_documents["product"], "Product Arbitration")
    product_locking = extract_section(latest_documents["product"], "Product Locking")
    growth_notes = extract_section(latest_documents["growth"], "Go-To-Market Notes")
    tech_notes = extract_section(latest_documents["tech"], "Architecture Notes")
    sections = [
        _format_block("Product Arbitration", product_arbitration),
        _format_block("Product Locking", product_locking),
        _format_block("Growth Notes", growth_notes),
        _format_block("Tech Notes", tech_notes),
    ]
    return "\n\n".join(["## Decisions Snapshot", *sections])


def _format_block(title: str, content: str) -> str:
    body = content.strip() or "_Aucun contenu._"
    return f"## {title}\n\n{body}\n"


def _format_activity_log_entry(entry: dict) -> str:
    parts = [
        str(entry.get("agent", "")),
        str(entry.get("event", "")),
        str(entry.get("source", "")),
    ]
    details = str(entry.get("details", "")).strip()
    if details:
        parts.append(details)
    return " | ".join(parts)


def _format_list_block(title: str, items: list[str], empty_label: str) -> str:
    body = "\n".join(f"- {item}" for item in items) or empty_label
    return f"## {title}\n\n{body}\n"


def _format_expert_contribution(title: str, contribution: dict) -> str:
    parts = [
        f"### {title} Summary\n\n{contribution['summary'].strip() or '_Aucun contenu._'}",
        _format_list_block(
            f"{title} Structural Decisions",
            contribution.get("decisions", []),
            "_Aucune décision structurante._",
        ),
        _format_list_block(
            f"{title} Recommendations",
            contribution["recommendations"],
            "_Aucune recommandation._",
        ),
        _format_list_block(f"{title} Risks", contribution["risks"], "_Aucun risque._"),
        _format_list_block(
            f"{title} Open Questions",
            contribution["open_questions"],
            "_Aucune question._",
        ),
    ]
    return "\n\n".join(parts)


def _format_readiness_block(title: str, readiness: dict) -> str:
    sections = [_format_block(f"{title} Status", readiness["status"])]
    parse_warning = readiness.get("parse_warning", "")
    if parse_warning:
        sections.append(_format_block(f"{title} Parse Warning", parse_warning))
    sections.extend(
        [
            _format_tagged_items_block(
                f"{title} Blocking Gaps",
                readiness["blocking_gaps"],
                "_Aucun blocage identifié._",
            ),
            _format_tagged_items_block(
                f"{title} Required Improvements",
                readiness["required_improvements"],
                "_Aucune amélioration requise._",
            ),
        ]
    )
    return "\n\n".join(sections)


def _format_readiness_section(blackboard: dict) -> str:
    readiness = blackboard["readiness"]
    return (
        "## Readiness\n\n"
        + "\n\n".join(
            [
                _format_readiness_block("Product", readiness["product"]),
                _format_readiness_block("Tech", readiness["tech"]),
                _format_readiness_block("Growth", readiness["growth"]),
                _format_readiness_block("Global", readiness["global"]),
                _format_list_block(
                    "Known Tags",
                    readiness.get("known_tags", []),
                    "_Aucun tag connu._",
                ),
            ]
        )
        + "\n"
    )


def _format_expert_decisions_section(blackboard: dict) -> str:
    expert_decisions = blackboard.get("expert_decisions", {})
    return (
        "## Expert Decisions\n\n"
        + "\n\n".join(
            [
                _format_tagged_items_block(
                    "Tech Structural Decisions",
                    _tag_decision_items(expert_decisions.get("tech", []), "tech"),
                    "_Aucune décision structurante tech._",
                ),
                _format_tagged_items_block(
                    "Growth Structural Decisions",
                    _tag_decision_items(expert_decisions.get("growth", []), "growth"),
                    "_Aucune décision structurante growth._",
                ),
            ]
        )
        + "\n"
    )


def _format_artifacts_section(blackboard: dict) -> str:
    artifacts = blackboard.get("artifacts", {})
    return (
        "## Artifacts\n\n"
        + "\n\n".join(
            [
                _format_block(
                    "Architecture Markdown Ready",
                    str(bool(artifacts.get("architecture_markdown_ready"))),
                ),
                _format_block(
                    "Architecture Visual Ready",
                    str(bool(artifacts.get("architecture_visual_ready"))),
                ),
                _format_block(
                    "Architecture Visual Warning",
                    artifacts.get("architecture_visual_warning", ""),
                ),
                _format_block(
                    "Architecture Mermaid Ready",
                    str(bool(artifacts.get("architecture_mermaid_ready"))),
                ),
                _format_block(
                    "Architecture Mermaid Source",
                    artifacts.get("architecture_mermaid_source", ""),
                ),
                _format_block(
                    "Architecture Image Ready",
                    str(bool(artifacts.get("architecture_image_ready"))),
                ),
                _format_block(
                    "Architecture Image Path",
                    artifacts.get("architecture_image_path", ""),
                ),
            ]
        )
        + "\n"
    )


def _format_product_locking_section(blackboard: dict) -> str:
    locking = blackboard.get("product_locking", {})
    if not locking.get("applied"):
        return "## Product Locking\n\n_Aucun verrouillage produit appliqué._\n"
    return (
        "## Product Locking\n\n"
        + "\n\n".join(
            [
                _format_block("Applied", str(bool(locking.get("applied")))),
                _format_list_block(
                    "Confirmed In Scope",
                    locking.get("confirmed_in_scope", []),
                    "_Aucun élément confirmé en scope._",
                ),
                _format_list_block(
                    "Confirmed Deferred",
                    locking.get("confirmed_deferred", []),
                    "_Aucun élément différé._",
                ),
                _format_list_block(
                    "Confirmed Out Of Scope",
                    locking.get("confirmed_out_of_scope", []),
                    "_Aucun élément hors scope._",
                ),
                _format_block("Locking Note", locking.get("locking_note", "")),
            ]
        )
        + "\n"
    )


def _format_product_arbitration_section(blackboard: dict) -> str:
    arbitration = blackboard["arbitration"]
    if not arbitration.get("source") and not any(
        arbitration[key] for key in ("retained", "deferred", "rejected", "open_points", "rationales")
    ):
        return "## Product Arbitration\n\n_Aucun arbitrage produit pour ce run._\n"
    reconciled = arbitration.get("reconciled", {})
    return (
        "## Product Arbitration\n\n"
        + "\n\n".join(
            [
                _format_block("Source", arbitration.get("source", "")),
                _format_list_block(
                    "Retained",
                    arbitration["retained"],
                    "_Aucun élément retenu._",
                ),
                _format_list_block(
                    "Deferred",
                    arbitration["deferred"],
                    "_Aucun élément différé._",
                ),
                _format_list_block(
                    "Rejected",
                    arbitration["rejected"],
                    "_Aucun élément rejeté._",
                ),
                _format_list_block(
                    "Open Points",
                    arbitration["open_points"],
                    "_Aucun point ouvert._",
                ),
                _format_list_block(
                    "Rationales",
                    arbitration["rationales"],
                    "_Aucune rationale._",
                ),
                _format_list_block(
                    "Reconciliation Notes",
                    arbitration.get("reconciliation_notes", []),
                    "_Aucune note de réconciliation._",
                ),
                _format_list_block(
                    "Reconciliation Warnings",
                    reconciled.get("warnings", []),
                    "_Aucune contradiction détectée._",
                ),
            ]
        )
        + "\n"
    )


def _format_tagged_items_block(title: str, items: list[dict], empty_label: str) -> str:
    grouped = group_tagged_items(items)
    if not grouped:
        return f"## {title}\n\n{empty_label}"

    rendered_groups = []
    for group in grouped:
        tag = group["tag"]
        lines = [f"### {tag}"]
        for item in group["items"]:
            lines.append(f"- {render_tagged_item(item)}")
        rendered_groups.append("\n".join(lines))
    return f"## {title}\n\n" + "\n\n".join(rendered_groups)


def _format_correction_loop_section(blackboard: dict) -> str:
    readiness = blackboard["readiness"]
    sections = [
        _format_block("Triggered", "Yes" if readiness["loop_triggered"] else "No"),
        _format_block("Current Loop Count", str(readiness["loop_count"])),
        _format_block("Max Loops", str(readiness["max_loops"])),
        _format_block(
            "Initial Global Status",
            readiness["history"][0]["global_status"] if readiness["history"] else readiness["global_status"],
        ),
        _format_block("Final Outcome", readiness["final_outcome"] or readiness["global_status"]),
        _format_correction_tasks_section(readiness["correction_tasks"]),
        _format_readiness_history_section(readiness["history"]),
    ]
    return "## Correction Loop\n\n" + "\n\n".join(sections) + "\n"


def _format_correction_tasks_section(correction_tasks: list[dict]) -> str:
    if not correction_tasks:
        return "## Correction Tasks\n\n_Aucune boucle de correction déclenchée._"

    grouped = {}
    for entry in correction_tasks:
        grouped.setdefault(entry["loop"], []).append(entry)

    rendered = []
    for loop_number in sorted(grouped):
        loop_entries = grouped[loop_number]
        rendered_items = []
        for item in loop_entries:
            rendered_items.append(
                "\n\n".join(
                    [
                        f"#### {item['owner'].capitalize()} Task",
                        _format_block("Task", item["task"]),
                        _format_block("Source Gap", item["source_gap"]),
                        _format_block("Expected Output", item["expected_output"]),
                        _format_list_block(
                            "Contributors",
                            item.get("contributors", []),
                            "_Aucun contributeur._",
                        ),
                    ]
                )
            )
        rendered.append(
            "\n\n".join(
                [
                    f"### Loop {loop_number}",
                    "\n\n".join(rendered_items),
                ]
            )
        )
    return "## Correction Tasks\n\n" + "\n\n".join(rendered)


def _format_readiness_history_section(history: list[dict]) -> str:
    if not history:
        return "## Readiness History\n\n_Aucun historique de correction._"

    rendered = []
    for entry in history:
        task_lines = []
        for task in entry["tasks"]:
            task_lines.append(
                "\n\n".join(
                    [
                        f"##### {task['owner'].capitalize()}",
                        _format_block("Task", task["task"]),
                        _format_block("Source Gap", task["source_gap"]),
                        _format_block("Expected Output", task["expected_output"]),
                    ]
                )
            )
        loop_tasks_section = (
            "## Loop Tasks\n\n" + "\n\n".join(task_lines)
            if task_lines
            else "## Loop Tasks\n\n_Aucune tâche._"
        )
        rendered.append(
            "\n\n".join(
                [
                    f"### Loop {entry['loop']} {entry['phase']}",
                    _format_block("Global Status", entry["global_status"]),
                    _format_block("Product Status", entry["product"]),
                    _format_block("Tech Status", entry["tech"]),
                    _format_block("Growth Status", entry["growth"]),
                    _format_tagged_items_block(
                        "Global Blocking Gaps",
                        entry["global_blocking_gaps"],
                        "_Aucun blocage global._",
                    ),
                    _format_tagged_items_block(
                        "Global Required Improvements",
                        entry["global_required_improvements"],
                        "_Aucune amélioration globale._",
                    ),
                    loop_tasks_section,
                ]
            )
        )
    return "## Readiness History\n\n" + "\n\n".join(rendered)


def _format_revision_block(title: str, trace: dict) -> str:
    return "\n\n".join(
        [
            _format_block(
                f"{title} Initial Draft",
                trace["initial_prd_draft"] or trace.get("initial_revision_draft", ""),
            ),
            _format_block(f"{title} Tech Input", trace["tech_input"]),
            _format_block(f"{title} Growth Input", trace["growth_input"]),
            _format_block(f"{title} Summary", trace["revision_summary"]),
        ]
    )


def _format_second_pass_block(blackboard: dict) -> str:
    source_artifacts = blackboard["source_artifacts"]
    return "\n\n".join(
        [
            _format_block("Source Version", blackboard["source_version"]),
            _format_block("CEO Evaluation", blackboard["executive_evaluation"]),
            _format_block("Source PRD", source_artifacts["prd"]),
            _format_block("Source Architecture", source_artifacts["architecture"]),
            _format_block("Source GTM", source_artifacts["gtm"]),
            _format_block(
                "First Revised Draft",
                blackboard["second_pass_trace"]["initial_revision_draft"],
            ),
            _format_revision_block("Second Pass", blackboard["second_pass_trace"]),
        ]
    )


def _format_blackboard_markdown(blackboard: dict) -> str:
    revision_trace = blackboard["revision_trace"]
    lines = [
        "# Blackboard",
        "",
        _format_block("Project Brief", blackboard["project_brief"]),
        _format_block("Project Brief Source", blackboard["project_brief_source"]),
        _format_block("Workflow Stage", blackboard["workflow_stage"]),
        _format_block("Source Version", blackboard["source_version"]),
        _format_block("CEO Evaluation", blackboard["executive_evaluation"]),
        _format_artifacts_section(blackboard),
        _format_readiness_section(blackboard),
        _format_correction_loop_section(blackboard),
        _format_expert_decisions_section(blackboard),
        _format_product_locking_section(blackboard),
        "## Expert Contributions\n\n"
        + "\n\n".join(
            [
                _format_expert_contribution(
                    "Tech", blackboard["expert_contributions"]["tech"]
                ),
                _format_expert_contribution(
                    "Growth", blackboard["expert_contributions"]["growth"]
                ),
            ]
        )
        + "\n",
        _format_product_arbitration_section(blackboard),
        _format_block("Source PRD", blackboard["source_artifacts"]["prd"]),
        _format_block("Initial PRD", revision_trace["initial_prd_draft"]),
        _format_list_block(
            "Retained Decisions",
            blackboard["retained_decisions"],
            "_Aucune décision retenue._",
        ),
        _format_list_block(
            "Deferred Decisions",
            blackboard["deferred_decisions"],
            "_Aucune décision différée._",
        ),
        _format_list_block(
            "Rejected Recommendations",
            blackboard["rejected_changes"],
            "_Aucune recommandation rejetée._",
        ),
        _format_list_block(
            "Unresolved Tensions",
            blackboard["unresolved_tensions"],
            "_Aucune tension non résolue._",
        ),
        _format_list_block(
            "Applied Changes",
            blackboard["applied_changes"],
            "_Aucun changement appliqué._",
        ),
        _format_list_block(
            "Remaining Open Points",
            blackboard["open_points"],
            "_Aucun point restant._",
        ),
        _format_list_block("Risks", blackboard["risks"], "_Aucun risque._"),
        _format_list_block("Open Questions", blackboard["open_questions"], "_Aucune question._"),
        _format_block("Final Revised PRD", blackboard["prd_draft"]),
        _format_block("Revision Summary", revision_trace["revision_summary"]),
        _format_list_block("Decisions", blackboard["decisions"], "_Aucune décision._"),
        _format_list_block("Conflicts", blackboard["conflicts"], "_Aucun conflit._"),
        _format_list_block(
            "Activity Log",
            [f"{entry['agent']}: {entry['event']}" for entry in blackboard["activity_log"]],
            "_Aucune activité._",
        ),
    ]
    return "\n".join(lines)


def _format_second_pass_blackboard_markdown(blackboard: dict) -> str:
    revision_trace = blackboard["revision_trace"]
    lines = [
        "# Blackboard V2",
        "",
        _format_block("Project Brief", blackboard["project_brief"]),
        _format_block("Project Brief Source", blackboard["project_brief_source"]),
        _format_block("Workflow Stage", blackboard["workflow_stage"]),
        _format_block("Source Version", blackboard["source_version"]),
        _format_block("CEO Evaluation", blackboard["executive_evaluation"]),
        _format_artifacts_section(blackboard),
        _format_readiness_section(blackboard),
        _format_correction_loop_section(blackboard),
        _format_expert_decisions_section(blackboard),
        _format_product_locking_section(blackboard),
        _format_block("Source Project Brief", blackboard["source_artifacts"]["project_brief"]),
        _format_block("Source PRD", blackboard["source_artifacts"]["prd"]),
        _format_block("Source Architecture", blackboard["source_artifacts"]["architecture"]),
        _format_block("Source GTM", blackboard["source_artifacts"]["gtm"]),
        _format_block("First Revised Draft", blackboard["second_pass_trace"]["initial_revision_draft"]),
        "## Expert Contributions\n\n"
        + "\n\n".join(
            [
                _format_expert_contribution(
                    "Tech", blackboard["expert_contributions"]["tech"]
                ),
                _format_expert_contribution(
                    "Growth", blackboard["expert_contributions"]["growth"]
                ),
            ]
        )
        + "\n",
        _format_product_arbitration_section(blackboard),
        _format_list_block(
            "Retained Decisions",
            blackboard["retained_decisions"],
            "_Aucune décision retenue._",
        ),
        _format_list_block(
            "Deferred Decisions",
            blackboard["deferred_decisions"],
            "_Aucune décision différée._",
        ),
        _format_list_block(
            "Rejected Recommendations",
            blackboard["rejected_changes"],
            "_Aucune recommandation rejetée._",
        ),
        _format_list_block(
            "Unresolved Tensions",
            blackboard["unresolved_tensions"],
            "_Aucune tension non résolue._",
        ),
        _format_list_block(
            "Applied Changes",
            blackboard["applied_changes"],
            "_Aucun changement appliqué._",
        ),
        _format_list_block(
            "Remaining Open Points",
            blackboard["open_points"],
            "_Aucun point restant._",
        ),
        _format_list_block("Risks", blackboard["risks"], "_Aucun risque._"),
        _format_list_block("Open Questions", blackboard["open_questions"], "_Aucune question._"),
        _format_block("Final Revised PRD", blackboard["prd_draft"]),
        _format_block("Second Pass Summary", blackboard["second_pass_trace"]["revision_summary"]),
        _format_block("Final Revision Summary", revision_trace["revision_summary"]),
        _format_list_block("Decisions", blackboard["decisions"], "_Aucune décision._"),
        _format_list_block("Conflicts", blackboard["conflicts"], "_Aucun conflit._"),
        _format_list_block(
            "Activity Log",
            [f"{entry['agent']}: {entry['event']}" for entry in blackboard["activity_log"]],
            "_Aucune activité._",
        ),
    ]
    return "\n".join(lines)


def _tag_decision_items(items: list[str], source_tag: str) -> list[dict]:
    return [{"tag": source_tag, "text": item} for item in items if item]
