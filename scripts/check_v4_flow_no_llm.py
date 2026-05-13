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
    assert parsed["items_to_create"][0]["raw_line"] == (
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision."
    )
    assert parsed["items_to_update"][0]["raw_line"] == "ITEM-001 | ANSWERED"


def _validate_v4_flow_and_compiler() -> None:
    with tempfile.TemporaryDirectory(prefix="squad-ia-v4-") as temp_dir:
        temp_root = Path(temp_dir)
        runs_root = temp_root / "runs"
        public_root = temp_root / "public"
        valid_calls: list[dict] = []
        valid_workspaces: list = []
        summary_calls: list[str] = []

        def workspace_factory(project_name: str):
            workspace = create_run_workspace(project_name, base_root=runs_root)
            valid_workspaces.append(workspace)
            return workspace

        def summary_runner(workspace, source_document_path):
            source_path = Path(source_document_path)
            if not source_path.is_absolute():
                source_path = workspace.root / source_path
            source_text = read_text_file(source_path)
            relative_source = source_path.relative_to(workspace.root)
            summary_calls.append(source_path.name)
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
            valid_calls.append(
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

        finalization_calls = [call for call in valid_calls if call["mode_label"] == "finalization"]
        assert [call["role"] for call in finalization_calls] == ["product", "growth", "tech"]
        assert summary_calls.count("PRD_FINAL.md") == 1
        assert summary_calls.count("GTM_FINAL.md") == 1
        assert summary_calls.count("Architecture_FINAL.md") == 1
        assert summary_calls.index("PRD_FINAL.md") < summary_calls.index("GTM_FINAL.md")
        assert summary_calls.index("GTM_FINAL.md") < summary_calls.index(
            "Architecture_FINAL.md"
        )

        valid_workspace = valid_workspaces[0]
        assert (valid_workspace.root / "agent_outputs" / "product_initial_draft.raw.md").exists()
        assert (valid_workspace.root / "agent_outputs" / "growth_review.raw.md").exists()
        assert (valid_workspace.root / "agent_outputs" / "tech_review.raw.md").exists()

        repeated_trace_state: dict = {}
        repeated_trace_first = orchestrator._run_v4_agent(
            role="growth",
            mode_label="item_resolution",
            project_brief="Project name: Harness Project\n\nBuild a V4 validation harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=valid_workspace,
            state=repeated_trace_state,
            open_items=[],
            summaries={},
            documents={"growth": _build_document("growth", "item_resolution")},
            extra_context=[],
            agent_runner=lambda **kwargs: _fake_v4_agent_output(kwargs["role"], kwargs["mode_label"]),
        )
        repeated_trace_second = orchestrator._run_v4_agent(
            role="growth",
            mode_label="item_resolution",
            project_brief="Project name: Harness Project\n\nBuild a V4 validation harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=valid_workspace,
            state=repeated_trace_state,
            open_items=[],
            summaries={},
            documents={"growth": _build_document("growth", "item_resolution")},
            extra_context=[],
            agent_runner=lambda **kwargs: _fake_v4_agent_output(kwargs["role"], kwargs["mode_label"]),
        )
        first_trace_path = Path(repeated_trace_first["raw_response_trace_path"])
        second_trace_path = Path(repeated_trace_second["raw_response_trace_path"])
        assert first_trace_path.exists()
        assert second_trace_path.exists()
        assert first_trace_path != second_trace_path
        assert first_trace_path.name == "growth_item_resolution.raw.md"
        assert second_trace_path.name == "growth_item_resolution_02.raw.md"

        def bad_create_workspace_factory(project_name: str):
            workspace = create_run_workspace(project_name, base_root=runs_root)
            invalid_create_workspaces.append(workspace)
            return workspace

        invalid_create_workspaces: list = []

        def bad_create_type_agent_runner(
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
            if role == "product" and mode_label == "initial_draft":
                parsed["items_to_create"] = [
                    {
                        "type": "BROKEN",
                        "author": "PRODUCT",
                        "targets": ["PRODUCT"],
                        "priority": "HIGH",
                        "tags": ["scope"],
                        "title": "Broken type",
                        "content": "This type should be rejected.",
                        "raw_line": "- BROKEN | PRODUCT | PRODUCT | HIGH | scope | Broken type | This type should be rejected.",
                    }
                ]
            return parsed

        original_create_item = orchestrator.create_item
        original_update_item_status = orchestrator.update_item_status
        orchestrator.create_item = lambda *args, **kwargs: (_ for _ in ()).throw(
            AssertionError("create_item should not be called for invalid V4 item types")
        )
        try:
            try:
                orchestrator.run_v4_flow(
                    "Harness Project Bad Create Type",
                    "Project name: Harness Project Bad Create Type\n\nBuild a V4 validation harness.",
                    "scripts/check_v4_flow_no_llm.py",
                    workspace_factory=bad_create_workspace_factory,
                    summary_runner=summary_runner,
                    agent_runner=bad_create_type_agent_runner,
                )
            except ValueError as exc:
                assert "invalid value 'BROKEN'" in str(exc)
                assert "field 'type'" in str(exc)
            else:
                raise AssertionError("Invalid V4 item types must fail before persistence.")

            create_trace_path = (
                invalid_create_workspaces[0].root / "agent_outputs" / "product_initial_draft.raw.md"
            )
            assert create_trace_path.exists()

            invalid_priority_workspaces: list = []

            def bad_priority_workspace_factory(project_name: str):
                workspace = create_run_workspace(project_name, base_root=runs_root)
                invalid_priority_workspaces.append(workspace)
                return workspace

            def bad_priority_agent_runner(
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
                if role == "product" and mode_label == "initial_draft":
                    parsed["items_to_create"] = [
                        {
                            "type": "QUESTION",
                            "author": "PRODUCT",
                            "targets": ["PRODUCT"],
                            "priority": "BROKEN",
                            "tags": ["scope"],
                            "title": "Broken priority",
                            "content": "This priority should be rejected.",
                            "raw_line": "- QUESTION | PRODUCT | PRODUCT | BROKEN | scope | Broken priority | This priority should be rejected.",
                        }
                    ]
                return parsed

            try:
                orchestrator.run_v4_flow(
                    "Harness Project Bad Create Priority",
                    "Project name: Harness Project Bad Create Priority\n\nBuild a V4 validation harness.",
                    "scripts/check_v4_flow_no_llm.py",
                    workspace_factory=bad_priority_workspace_factory,
                    summary_runner=summary_runner,
                    agent_runner=bad_priority_agent_runner,
                )
            except ValueError as exc:
                assert "invalid value 'BROKEN'" in str(exc)
                assert "field 'priority'" in str(exc)
            else:
                raise AssertionError("Invalid V4 item priorities must fail before persistence.")

            priority_trace_path = (
                invalid_priority_workspaces[0].root / "agent_outputs" / "product_initial_draft.raw.md"
            )
            assert priority_trace_path.exists()

            orchestrator.create_item = original_create_item
            invalid_update_workspaces: list = []

            def bad_update_workspace_factory(project_name: str):
                workspace = create_run_workspace(project_name, base_root=runs_root)
                invalid_update_workspaces.append(workspace)
                return workspace

            def bad_update_agent_runner(
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
                if role == "tech" and mode_label == "review":
                    parsed["items_to_update"] = [
                        {
                            "id": "ITEM-001",
                            "status": "BROKEN",
                            "raw_line": "- ITEM-001 | BROKEN",
                        }
                    ]
                return parsed

            orchestrator.update_item_status = lambda *args, **kwargs: (_ for _ in ()).throw(
                AssertionError("update_item_status should not be called for invalid V4 item statuses")
            )
            try:
                orchestrator.run_v4_flow(
                    "Harness Project Bad Update",
                    "Project name: Harness Project Bad Update\n\nBuild a V4 validation harness.",
                    "scripts/check_v4_flow_no_llm.py",
                    workspace_factory=bad_update_workspace_factory,
                    summary_runner=summary_runner,
                    agent_runner=bad_update_agent_runner,
                )
            except ValueError as exc:
                assert "invalid value 'BROKEN'" in str(exc)
                assert "field 'status'" in str(exc)
            else:
                raise AssertionError("Invalid V4 item statuses must fail before persistence.")

            update_trace_path = (
                invalid_update_workspaces[0].root / "agent_outputs" / "tech_review.raw.md"
            )
            assert update_trace_path.exists()

            output_dir = public_root / "tests" / "Harness Project" / "version 1"
            original_renderer = artifact_writer.render_architecture_diagram
            artifact_writer.render_architecture_diagram = _fake_render_architecture_diagram
            try:
                write_v4_run_artifacts(blackboard, output_dir)
            finally:
                artifact_writer.render_architecture_diagram = original_renderer

            final_outputs = valid_workspace.final_outputs_dir
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

            assert not (public_output_dir / "agent_outputs").exists()
            assert not any(path.name.endswith(".raw.md") for path in public_output_dir.rglob("*"))

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
            assert "Product Problem" in final_prd
            assert "Architecture Notes" in final_architecture
            assert "Go-To-Market Notes" in final_gtm

            direct_placeholder_cases = {
                "product": "Product Problem",
                "growth": "Go-To-Market Notes",
                "tech": "Architecture Notes",
            }
            for role, section_name in direct_placeholder_cases.items():
                parsed = parse_v4_agent_response(_build_document(role, "review"))
                parsed["sections"][section_name] = "- See above"
                try:
                    orchestrator.validate_v4_document(
                        role=role,
                        mode_label="review",
                        parsed_response=parsed,
                        raw_response_trace_path=f"runs/fake/agent_outputs/{role}_review.raw.md",
                    )
                except ValueError as exc:
                    assert section_name in str(exc)
                    assert "See above" in str(exc)
                else:
                    raise AssertionError(f"{role} placeholder-only sections must fail validation.")

            none_placeholder_cases = {
                "product": "Product Problem",
                "growth": "Go-To-Market Notes",
                "tech": "Architecture Notes",
            }
            for role, section_name in none_placeholder_cases.items():
                parsed = parse_v4_agent_response(_build_document(role, "review"))
                parsed["sections"][section_name] = "- None"
                try:
                    orchestrator.validate_v4_document(
                        role=role,
                        mode_label="review",
                        parsed_response=parsed,
                        raw_response_trace_path=f"runs/fake/agent_outputs/{role}_review.raw.md",
                    )
                except ValueError as exc:
                    assert section_name in str(exc)
                    assert "None" in str(exc)
                else:
                    raise AssertionError(f"{role} - None sections must fail validation.")
        finally:
            orchestrator.create_item = original_create_item
            orchestrator.update_item_status = original_update_item_status


def _fake_v4_agent_output(role: str, mode_label: str) -> dict:
    document_text = _build_document(role, mode_label)
    parsed = parse_v4_agent_response(document_text)
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
    parsed["items_to_create"] = items_to_create
    parsed["items_to_update"] = items_to_update
    parsed["raw_response"] = document_text
    parsed["role"] = role
    parsed["mode_label"] = mode_label
    return parsed


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
                "## Initial Wedge",
                "- A run-local blackboard dossier for one brief.",
                "",
                "## First Target User",
                "- Internal evaluator or architect reading the dossier.",
                "",
                "## Existing Alternatives And Switching Trigger",
                "- Existing ad hoc run notes; switch when traceability matters.",
                "",
                "## Core MVP Workflow",
                "- Brief in, Product/Growth/Tech review, final locking out.",
                "",
                "## In Scope",
                "- Explicit V4 sections, blackboard items, run-local traces.",
                "",
                "## Out of Scope",
                "- Generic orchestration graphs and broad retry frameworks.",
                "",
                "## MVP Build Vs Pilot Operations",
                "- Build the explicit flow; keep validation tooling operational.",
                "",
                "## Business Model Hypothesis",
                "- The value comes from auditable multi-agent dossier generation.",
                "",
                "## Critical Assumptions",
                "- The brief is enough to start, and the validation path is inspectable.",
                "",
                "## How To Test Quickly",
                "- Run the no-LLM harness and inspect the run-local trace paths.",
                "",
                "## Acceptance Criteria",
                "- Valid runs create the final documents and public artifacts.",
                "",
                "## Risks And Failure Modes",
                "- Invalid item operations or placeholder-only sections must fail fast.",
                "",
                "## Product Readiness",
                "",
                "Status: READY",
                "",
                "Blocking Gaps:",
                "- None",
                "",
                "Required Improvements:",
                "- None",
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
                "",
                "## Blackboard Items To Create",
                "",
                "- None",
                "",
                "## Blackboard Items To Update",
                "",
                "- None",
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
                "- A concrete pilot launch motion and observability.",
                "",
                "### Can Stay Manual Or Operational During Pilot",
                "- Manual onboarding and launch support.",
                "",
                "### Deferred Until After Proof",
                "- Broader automation and scaling polish.",
                "",
                "## Critical Assumptions",
                "- The pilot can be launched with the current scope.",
                "",
                "## Requested Changes",
                "- Narrow the launch motion and keep it testable.",
                "",
                "## Risks",
                "- Launch motion is too vague or too broad.",
                "",
                "## Open Questions",
                "- Which primary launch motion is best to test first?",
                "",
                "## Why This Could Fail Even With Good Execution",
                "- If the motion is too broad, users never convert.",
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
                "",
                "## Blackboard Items To Create",
                "",
                "- None",
                "",
                "## Blackboard Items To Update",
                "",
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
            "  Brief[Brief] --> Product[Product]",
            "  Product --> Growth[Growth]",
            "  Growth --> Tech[Tech]",
            "  Tech --> Blackboard[Blackboard]",
            "```",
            "",
            "## Review Summary",
            "- Feasibility stays bounded.",
            "",
            "## Critical Assumptions",
            "- The runtime stays file-system first and inspectable.",
            "",
            "## Requested Changes",
            "- Keep the architecture simple and explicit.",
            "",
            "## Risks",
            "- Mermaid rendering can fail if the browser is missing.",
            "",
                "## Open Questions",
                "- What browser/runtime configuration is required for Mermaid PNG generation?",
                "",
                "## Why This Could Fail Even With Good Execution",
                "- A missing renderer or malformed Mermaid source stops the PNG.",
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
            "",
            "## Blackboard Items To Create",
            "",
            "- None",
            "",
            "## Blackboard Items To Update",
            "",
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
