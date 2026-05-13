#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import tempfile
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app import artifact_writer, orchestrator
from app.artifact_writer import write_v4_run_artifacts
from app.run_store import create_run_workspace, read_text_file
from app.v4_parsing import parse_v4_agent_response


def main() -> None:
    _validate_parser()
    _validate_v4_flow_and_compiler()
    print("ok")


def _validate_parser() -> None:
    sample = """## Product Problem
- Real content.

## Blackboard Items To Create
- QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.

## Blackboard Items To Update
- ITEM-001 | ANSWERED
"""
    parsed = parse_v4_agent_response(sample)
    assert "Blackboard Items To Create" not in parsed["document_text"]
    assert "Blackboard Items To Update" not in parsed["document_text"]
    assert len(parsed["items_to_create"]) == 1
    assert len(parsed["items_to_update"]) == 1


def _validate_v4_flow_and_compiler() -> None:
    with tempfile.TemporaryDirectory(prefix="squad-ia-v4-") as temp_dir:
        temp_root = Path(temp_dir)
        runs_root = temp_root / "runs"
        public_root = temp_root / "public"
        calls: list[dict] = []

        def workspace_factory(project_name: str):
            return create_run_workspace(project_name, base_root=runs_root)

        def summary_runner(workspace, source_document_path):
            source_path = Path(source_document_path)
            if not source_path.is_absolute():
                source_path = workspace.root / source_path
            source_text = read_text_file(source_path)
            relative_source = source_path.relative_to(workspace.root)
            return {
                "source_document": str(relative_source),
                "source_hash": sha256(source_text.encode("utf-8")).hexdigest(),
                "scope": f"Summary for {source_path.name}",
                "key_decisions": [f"Decision captured from {source_path.name}"],
                "unresolved_questions": (
                    [f"Follow-up from {source_path.name}"] if "FINAL" not in source_path.name else []
                ),
                "critical_risks": [],
            }

        def agent_runner(
            *,
            role: str,
            mode_label: str,
            project_brief: str,
            project_brief_source: str,
            workspace,
            state: dict,
            open_items: list[dict],
            summaries: dict[str, dict],
            documents: dict[str, str],
            extra_context: list[str],
        ) -> dict:
            calls.append(
                {
                    "role": role,
                    "mode_label": mode_label,
                    "open_items": [dict(item) for item in open_items],
                    "documents": dict(documents),
                }
            )
            return _fake_v4_agent_output(role, mode_label)

        blackboard = orchestrator.run_v4_flow(
            "Harness Project",
            "Project name: Harness Project\n\nBuild a V4 validation harness.",
            "scripts/check_v4_flow_no_llm.py",
            workspace_factory=workspace_factory,
            summary_runner=summary_runner,
            agent_runner=agent_runner,
        )

        finalization_calls = [call for call in calls if call["mode_label"] == "finalization"]
        assert [call["role"] for call in finalization_calls] == ["product", "growth", "tech"]
        assert "# Final PRD" in finalization_calls[1]["documents"]["product"]
        assert "# Final PRD" in finalization_calls[2]["documents"]["product"]
        assert "# Final GTM" in finalization_calls[2]["documents"]["growth"]

        def bad_growth_update_agent_runner(
            *,
            role: str,
            mode_label: str,
            project_brief: str,
            project_brief_source: str,
            workspace,
            state: dict,
            open_items: list[dict],
            summaries: dict[str, dict],
            documents: dict[str, str],
            extra_context: list[str],
        ) -> dict:
            parsed = _fake_v4_agent_output(role, mode_label)
            if role == "growth" and mode_label == "finalization":
                parsed["items_to_update"] = [{"id": "ITEM-001", "status": "ANSWERED"}]
            return parsed

        try:
            orchestrator.run_v4_flow(
                "Harness Project Bad Finalization",
                "Project name: Harness Project Bad Finalization\n\nBuild a V4 validation harness.",
                "scripts/check_v4_flow_no_llm.py",
                workspace_factory=workspace_factory,
                summary_runner=summary_runner,
                agent_runner=bad_growth_update_agent_runner,
            )
        except ValueError as exc:
            assert "cannot update" in str(exc)
        else:
            raise AssertionError(
                "Growth finalization updates must fail inside run_v4_flow."
            )

        product_final_open_call = [
            call
            for call in calls
            if call["role"] == "product" and call["mode_label"] == "finalization"
        ][0]
        assert any(
            item["id"] == "ITEM-004" and item["status"] == "OPEN"
            for item in product_final_open_call["open_items"]
        )

        original_renderer = artifact_writer.render_architecture_diagram
        artifact_writer.render_architecture_diagram = _fake_render_architecture_diagram
        try:
            output_dir = public_root / "tests" / "Harness Project" / "version 1"
            write_v4_run_artifacts(blackboard, output_dir)
        finally:
            artifact_writer.render_architecture_diagram = original_renderer

        try:
            orchestrator._apply_v4_finalization_item_operations(
                blackboard["workspace"],
                {
                    "items_to_create": [],
                    "items_to_update": [{"id": "ITEM-001", "status": "ANSWERED"}],
                },
                default_author="GROWTH",
            )
        except ValueError as exc:
            assert "cannot update" in str(exc)
        else:
            raise AssertionError("Growth and Tech finalization must not update items.")

        final_outputs = blackboard["workspace"].final_outputs_dir
        public_output_dir = public_root / "tests" / "Harness Project" / "version 1"
        required_files = [
            "project-brief.md",
            "prd.md",
            "architecture.md",
            "gtm.md",
            "blackboard.md",
            "activity_log.txt",
            "architecture-diagram.mmd",
            "architecture-diagram.png",
        ]
        for filename in required_files:
            assert (final_outputs / filename).exists(), filename
            assert (public_output_dir / filename).exists(), filename

        for filename in ("prd.md", "architecture.md", "gtm.md"):
            text = (public_output_dir / filename).read_text(encoding="utf-8")
            assert "Blackboard Items To Create" not in text, filename
            assert "Blackboard Items To Update" not in text, filename

        blackboard_text = (public_output_dir / "blackboard.md").read_text(encoding="utf-8")
        open_items_section = _extract_section(blackboard_text, "Open Items")
        resolved_items_section = _extract_section(blackboard_text, "Resolved Items")
        assert "ITEM-005" in open_items_section
        assert "ITEM-004" in resolved_items_section
        assert "ITEM-001" in resolved_items_section
        assert "ITEM-002" in resolved_items_section
        assert "ITEM-003" in resolved_items_section
        assert "Open Items" in blackboard_text
        assert "Resolved Items" in blackboard_text

        final_prd = (public_output_dir / "prd.md").read_text(encoding="utf-8")
        final_architecture = (public_output_dir / "architecture.md").read_text(
            encoding="utf-8"
        )
        final_gtm = (public_output_dir / "gtm.md").read_text(encoding="utf-8")
        assert "Final PRD" in final_prd
        assert "Final Architecture" in final_architecture
        assert "Final GTM" in final_gtm


def _fake_v4_agent_output(role: str, mode_label: str) -> dict:
    document_text = _build_document(role, mode_label)
    item_map = {
        ("product", "initial_draft"): (
            [
                {
                    "type": "QUESTION",
                    "author": "PRODUCT",
                    "targets": ["PRODUCT", "TECH"],
                    "priority": "HIGH",
                    "tags": ["scope"],
                    "title": "Clarify core scope",
                    "content": "Need a clear scope anchor.",
                }
            ],
            [],
        ),
        ("growth", "review"): (
            [
                {
                    "type": "RISK",
                    "author": "GROWTH",
                    "targets": ["GROWTH"],
                    "priority": "MEDIUM",
                    "tags": ["launch"],
                    "title": "Launch motion risk",
                    "content": "The launch motion is still broad.",
                }
            ],
            [],
        ),
        ("tech", "review"): (
            [],
            [{"id": "ITEM-001", "status": "ANSWERED"}],
        ),
        ("product", "revision"): ([], []),
        ("growth", "item_resolution"): ([], []),
        ("tech", "item_resolution"): ([], []),
        ("product", "item_resolution"): (
            [],
            [{"id": "ITEM-002", "status": "ANSWERED"}],
        ),
        ("growth", "candidate_rewrite"): (
            [
                {
                    "type": "QUESTION",
                    "author": "GROWTH",
                    "targets": ["GROWTH", "PRODUCT"],
                    "priority": "HIGH",
                    "tags": ["pilot"],
                    "title": "Pilot motion clarity",
                    "content": "Need a narrower pilot motion.",
                }
            ],
            [],
        ),
        ("tech", "candidate_rewrite"): ([], []),
        ("product", "candidate_rewrite"): (
            [],
            [{"id": "ITEM-002", "status": "ANSWERED"}],
        ),
        ("product", "verification"): (
            [
                {
                    "type": "QUESTION",
                    "author": "PRODUCT",
                    "targets": ["PRODUCT"],
                    "priority": "MEDIUM",
                    "tags": ["verification"],
                    "title": "Remaining verification gap",
                    "content": "One open verification item remains.",
                }
            ],
            [{"id": "ITEM-003", "status": "ANSWERED"}],
        ),
        ("growth", "verification"): ([], []),
        ("tech", "verification"): ([], []),
        ("growth", "finalization"): ([], []),
        ("tech", "finalization"): ([], []),
        ("product", "finalization"): (
            [
                {
                    "type": "QUESTION",
                    "author": "PRODUCT",
                    "targets": ["PRODUCT"],
                    "priority": "LOW",
                    "tags": ["followup"],
                    "title": "Follow-up item",
                    "content": "Leave a visible follow-up for the next iteration.",
                }
            ],
            [{"id": "ITEM-004", "status": "ANSWERED"}],
        ),
    }
    items_to_create, items_to_update = item_map.get((role, mode_label), ([], []))
    return {
        "raw_response": document_text,
        "document_text": document_text,
        "sections": {},
        "items_to_create": items_to_create,
        "items_to_update": items_to_update,
        "role": role,
    }


def _build_document(role: str, mode_label: str) -> str:
    if role == "product":
        title = "Final PRD" if mode_label == "finalization" else f"Product {mode_label.title()}"
        return "\n".join(
            [
                f"# {title}",
                "",
                "## Product Problem",
                "- Deliver a deterministic V4 workflow.",
                "",
                "## Product Arbitration",
                "",
                "### Retained",
                "- Keep explicit final documents.",
                "",
                "### Deferred",
                "- None",
                "",
                "### Rejected",
                "- None",
                "",
                "### Open Points",
                "- None",
                "",
                "### Rationales",
                "- Explicit final filenames prevent version ambiguity.",
                "",
                "## Product Locking",
                "",
                "### Confirmed In Scope",
                "- Final documents",
                "",
                "### Confirmed Deferred",
                "- None",
                "",
                "### Confirmed Out Of Scope",
                "- None",
                "",
                "### Locking Note",
                f"- Product {mode_label} notes.",
            ]
        )
    if role == "growth":
        title = "Final GTM" if mode_label == "finalization" else f"Growth {mode_label.title()}"
        return "\n".join(
            [
                f"# {title}",
                "",
                "## Go-To-Market Notes",
                "- Keep launch motion concrete.",
                "",
                "## Review Summary",
                "- Launch motion remains inspectable.",
                "",
                "## Build Vs Pilot Operations",
                "",
                "### Must Be Productized Now",
                "- None",
                "",
                "### Can Stay Manual Or Operational During Pilot",
                "- None",
                "",
                "### Deferred Until After Proof",
                "- None",
                "",
                "## GTM Readiness",
                "",
                "Status: READY",
                "",
                "Blocking Gaps:",
                "- None",
                "",
                "Required Improvements:",
                "- None",
            ]
        )
    title = "Final Architecture" if mode_label == "finalization" else f"Architecture {mode_label.title()}"
    return "\n".join(
        [
            f"# {title}",
            "",
            "## Architecture Notes",
            "- Keep the architecture inspectable.",
            "",
            "### Mermaid Diagram",
            "```mermaid",
            "graph TD",
            "  A-->B",
            "```",
            "",
            "## Review Summary",
            "- Feasibility stays bounded.",
            "",
            "## Technical Readiness",
            "",
            "Status: READY",
            "",
            "Blocking Gaps:",
            "- None",
            "",
            "Required Improvements:",
            "- None",
        ]
    )


def _fake_render_architecture_diagram(output_dir: Path, blackboard: dict) -> dict:
    mermaid_source = "graph TD\n  A-->B\n"
    mmd_path = output_dir / "architecture-diagram.mmd"
    png_path = output_dir / "architecture-diagram.png"
    mmd_path.write_text(mermaid_source, encoding="utf-8")
    png_path.write_bytes(b"PNG")
    return {
        "architecture_markdown_ready": True,
        "architecture_visual_ready": True,
        "architecture_visual_warning": "",
        "architecture_mermaid_ready": True,
        "architecture_mermaid_source": mermaid_source,
        "architecture_image_ready": True,
        "architecture_image_path": str(png_path),
    }


def _extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    section_lines: list[str] = []
    capture = False
    marker = f"## {heading}"
    for line in lines:
        if line.strip() == marker:
            capture = True
            continue
        if capture and line.startswith("## "):
            break
        if capture:
            section_lines.append(line)
    return "\n".join(section_lines).strip()


if __name__ == "__main__":
    main()
