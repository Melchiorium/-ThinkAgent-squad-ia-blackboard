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
from app.run_summaries import generate_summary
from app.run_store import create_run_workspace, read_text_file
from app.run_store import write_text_file
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

    colon_fallback_sample = sample.replace(
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope: Need a decision.",
    )
    colon_fallback_parsed = parse_v4_agent_response(colon_fallback_sample)
    assert colon_fallback_parsed["items_to_create"][0]["title"] == "Clarify scope"
    assert colon_fallback_parsed["items_to_create"][0]["content"] == "Need a decision."
    assert colon_fallback_parsed["items_to_create"][0]["raw_line"] == (
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope: Need a decision."
    )

    mixed_target_sample = sample.replace(
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
        "QUESTION | PRODUCT | PRODUCT,UX | HIGH | scope | Clarify scope | Need a decision.",
    )
    mixed_target_parsed = parse_v4_agent_response(mixed_target_sample)
    assert mixed_target_parsed["items_to_create"][0]["targets"] == ["PRODUCT"]
    assert mixed_target_parsed["items_to_create"][0]["tags"] == ["scope", "UX"]

    custom_code_type_sample = sample.replace(
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
        "DATA-GOV-01 | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
    )
    custom_code_type_parsed = parse_v4_agent_response(custom_code_type_sample)
    assert custom_code_type_parsed["items_to_create"][0]["type"] == "QUESTION"
    assert custom_code_type_parsed["items_to_create"][0]["tags"] == ["scope", "DATA-GOV-01"]

    embedded_type_sample = sample.replace(
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
        "DATA-MODEL_QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
    )
    embedded_type_parsed = parse_v4_agent_response(embedded_type_sample)
    assert embedded_type_parsed["items_to_create"][0]["type"] == "QUESTION"
    assert embedded_type_parsed["items_to_create"][0]["tags"] == [
        "scope",
        "DATA-MODEL_QUESTION",
    ]

    missing_author_sample = sample.replace(
        "QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.",
        "QUESTION | TECH | HIGH | scope | Clarify scope | Need a decision.",
    )
    missing_author_parsed = parse_v4_agent_response(missing_author_sample)
    assert missing_author_parsed["items_to_create"][0]["author"] == ""
    assert missing_author_parsed["items_to_create"][0]["targets"] == ["TECH"]
    assert missing_author_parsed["items_to_create"][0]["priority"] == "HIGH"
    assert missing_author_parsed["items_to_create"][0]["title"] == "Clarify scope"

    case_variant_sample = _build_document("product", "review").replace(
        "## Blackboard Items To Create",
        "## BlackBoard Items To Create",
    ).replace(
        "- None\n\n## Blackboard Items To Update\n\n- None",
        "- QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.\n\n## BlackBoard Items To Update\n\n- ITEM-001 | ANSWERED",
        1,
    )
    case_variant_parsed = parse_v4_agent_response(case_variant_sample)
    assert "BlackBoard Items To Create" not in case_variant_parsed["document_text"]
    assert "BlackBoard Items To Update" not in case_variant_parsed["document_text"]
    assert len(case_variant_parsed["items_to_create"]) == 1
    assert len(case_variant_parsed["items_to_update"]) == 1
    orchestrator.validate_v4_document(
        role="product",
        mode_label="review",
        parsed_response=case_variant_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_review.raw.md",
    )

    duplicate_heading_sample = """## Product Problem
- Real content.

## product problem
- Duplicate content.
"""
    try:
        parse_v4_agent_response(duplicate_heading_sample)
    except ValueError as exc:
        assert "Duplicate top-level heading after normalization" in str(exc)
    else:
        raise AssertionError("Duplicate normalized headings must fail parsing.")

    growth_preamble_sample = "\n".join(
        [
            "## Role (GTM Context for Review)",
            "- This is non-deliverable role context.",
            "",
            _build_document("growth", "review"),
        ]
    )
    growth_preamble_parsed = parse_v4_agent_response(growth_preamble_sample, role="growth")
    assert "Role (GTM Context for Review)" not in growth_preamble_parsed["document_text"]
    orchestrator.validate_v4_document(
        role="growth",
        mode_label="review",
        parsed_response=growth_preamble_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/growth_review.raw.md",
    )

    product_duplicate_tail_sample = "\n".join(
        [
            _build_document("product", "initial_draft"),
            "",
            "## Product Locking",
            "- See Product Locking section above for current locking status and next steps.",
        ]
    )
    product_duplicate_tail_parsed = parse_v4_agent_response(
        product_duplicate_tail_sample,
        role="product",
    )
    assert product_duplicate_tail_parsed["document_text"].count("## Product Locking") == 1
    orchestrator.validate_v4_document(
        role="product",
        mode_label="initial_draft",
        parsed_response=product_duplicate_tail_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
    )

    product_locking_block = "\n".join(
        [
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
            "- Product initial_draft notes.",
        ]
    )
    product_late_locking_sample = _build_document("product", "initial_draft").replace(
        product_locking_block + "\n\n",
        "",
        1,
    )
    product_late_locking_sample = product_late_locking_sample + "\n\n" + product_locking_block
    product_late_locking_parsed = parse_v4_agent_response(
        product_late_locking_sample,
        role="product",
    )
    assert product_late_locking_parsed["document_text"].count("## Product Locking") == 1
    orchestrator.validate_v4_document(
        role="product",
        mode_label="initial_draft",
        parsed_response=product_late_locking_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
    )

    product_bare_heading_sample = _build_document("product", "initial_draft").replace(
        "## Product Arbitration",
        "Product Arbitration",
        1,
    )
    product_bare_heading_parsed = parse_v4_agent_response(
        product_bare_heading_sample,
        role="product",
    )
    assert "Product Arbitration" in product_bare_heading_parsed["sections"]
    orchestrator.validate_v4_document(
        role="product",
        mode_label="initial_draft",
        parsed_response=product_bare_heading_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
    )

    product_missing_arbitration_parent_sample = _build_document(
        "product",
        "initial_draft",
    ).replace(
        "## Product Arbitration\n\n",
        "",
        1,
    )
    product_missing_arbitration_parent_parsed = parse_v4_agent_response(
        product_missing_arbitration_parent_sample,
        role="product",
    )
    assert "Product Arbitration" in product_missing_arbitration_parent_parsed["sections"]
    assert "### Retained" in product_missing_arbitration_parent_parsed["sections"]["Product Arbitration"]
    orchestrator.validate_v4_document(
        role="product",
        mode_label="initial_draft",
        parsed_response=product_missing_arbitration_parent_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
    )

    product_trailing_sections_sample = "\n".join(
        [
            _build_document("product", "revision"),
            "",
            "## Product Readying",
            "Status: LIMITED",
            "",
            "## Product Readiness",
            "Status: LIMITED",
            "",
            "Blocking Gaps:",
            "- [scope] duplicated tail",
            "",
            "Required Improvements:",
            "- [scope] duplicated tail",
            "",
            "## Product Locking",
            "### Confirmed In Scope",
            "- duplicated tail",
        ]
    )
    product_trailing_sections_parsed = parse_v4_agent_response(
        product_trailing_sections_sample,
        role="product",
    )
    assert "Product Readying" not in product_trailing_sections_parsed["document_text"]
    assert product_trailing_sections_parsed["document_text"].count("## Product Readiness") == 1
    assert product_trailing_sections_parsed["document_text"].count("## Product Locking") == 1
    orchestrator.validate_v4_document(
        role="product",
        mode_label="revision",
        parsed_response=product_trailing_sections_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_revision.raw.md",
    )

    canonical_mermaid_block = "\n".join(
        [
            "### Mermaid Diagram",
            "```mermaid",
            "graph TD",
            "  Brief[Brief] --> Product[Product]",
            "  Product --> Growth[Growth]",
            "  Growth --> Tech[Tech]",
            "  Tech --> Blackboard[Blackboard]",
            "```",
        ]
    )
    bullet_mermaid_block = "\n".join(
        [
            "- Mermaid Diagram",
            "  Mermaid Diagram",
            "  graph TD",
            "    Brief[Brief] --> Product[Product]",
            "    Product --> Tech[Tech]",
            "- Notes",
            "  - Keep privacy controls explicit.",
        ]
    )
    tech_bullet_mermaid_sample = _build_document("tech", "review").replace(
        canonical_mermaid_block,
        bullet_mermaid_block,
    )
    tech_bullet_mermaid_parsed = parse_v4_agent_response(
        tech_bullet_mermaid_sample,
        role="tech",
    )
    architecture_notes = tech_bullet_mermaid_parsed["sections"]["Architecture Notes"]
    assert "### Mermaid Diagram" in architecture_notes
    assert "```mermaid" in architecture_notes
    assert "graph TD" in architecture_notes
    orchestrator.validate_v4_document(
        role="tech",
        mode_label="review",
        parsed_response=tech_bullet_mermaid_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/tech_review.raw.md",
    )

    tech_absence_placeholder_sample = _build_document("tech", "verification").replace(
        "## Open Questions\n- What browser/runtime configuration is required for Mermaid PNG generation?",
        "## Open Questions\n- None",
        1,
    )
    tech_absence_placeholder_parsed = parse_v4_agent_response(
        tech_absence_placeholder_sample,
        role="tech",
    )
    assert "No open questions remain" in tech_absence_placeholder_parsed["sections"]["Open Questions"]
    orchestrator.validate_v4_document(
        role="tech",
        mode_label="verification",
        parsed_response=tech_absence_placeholder_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/tech_verification.raw.md",
    )

    tech_interleaved_internal_sample = _build_document("tech", "finalization").replace(
        "## Blackboard Items To Update",
        "\n".join(
            [
                "## Open Questions",
                "- See Open Questions section above.",
                "",
                "## Technical Readiness",
                "Status: LIMITED",
                "",
                "Blocking Gaps:",
                "- [risk] duplicated tail",
                "",
                "Required Improvements:",
                "- [risk] duplicated tail",
                "",
                "## Blackboard Items To Update",
            ]
        ),
        1,
    )
    tech_interleaved_internal_parsed = parse_v4_agent_response(
        tech_interleaved_internal_sample,
        role="tech",
    )
    assert tech_interleaved_internal_parsed["document_text"].count("## Technical Readiness") == 1
    assert tech_interleaved_internal_parsed["items_to_update"] == []
    orchestrator.validate_v4_document(
        role="tech",
        mode_label="finalization",
        parsed_response=tech_interleaved_internal_parsed,
        raw_response_trace_path="runs/fake/agent_outputs/tech_finalization.raw.md",
    )


def _validate_v4_flow_and_compiler() -> None:
    with tempfile.TemporaryDirectory(prefix="squad-ia-v4-") as temp_dir:
        temp_root = Path(temp_dir)
        runs_root = temp_root / "runs"
        public_root = temp_root / "public"
        prompt_workspace = create_run_workspace("Prompt Harness", base_root=runs_root)
        valid_calls: list[dict] = []
        valid_workspaces: list = []
        summary_calls: list[str] = []
        summary_validation_workspace = create_run_workspace(
            "Summary Harness", base_root=runs_root
        )
        contextual_instruction = "\n".join(
            [
                "Contextual step instruction:",
                "- This is the first Product draft for this run.",
                "- No blackboard item exists yet unless it is shown in Open items context.",
                "- In Blackboard Items To Update, write `- None`.",
                "- In Blackboard Items To Create, create only real unresolved questions, risks, decisions, proposals, constraints, warnings, or feedback.",
                "- Do not output template rows, field names, or placeholder values as items.",
            ]
        )
        operation_reminder = "\n".join(
            [
                "Blackboard operation reminder:",
                "- In create items, ROUTING_TARGETS must contain only PRODUCT, GROWTH, TECH, or ALL.",
                "- Put topic labels such as pricing, privacy, onboarding, data-model, or compliance in TAGS, not in ROUTING_TARGETS.",
                "- Do not output TYPE, AUTHOR, TARGET1, TARGET2, PRIORITY, TAGS, TITLE, or CONTENT as literal item values.",
                "- In Blackboard Items To Create, the first field must be a valid item type, never an ITEM-### id.",
                "- In Blackboard Items To Create, title and content are separate fields; use `|` between them, not `:`.",
                "- Existing ITEM-### ids are read-only references unless they are used in Blackboard Items To Update.",
                "- In Blackboard Items To Update, output only item id and status, with no targets, priority, tags, title, or content.",
                "- Use one bullet marker only for each blackboard operation; do not write nested bullets like `- - ITEM-001 | ANSWERED`.",
                "- Do not copy Open items context rows into Blackboard Items To Create.",
                "- Every required top-level section heading must start with `##`.",
                "- Do not repeat any required document section after the Blackboard Items sections.",
                "- Keep Blackboard Items To Create and Blackboard Items To Update consecutive; do not insert document sections between them.",
                "- Do not write any content after Blackboard Items To Update.",
                "- Update only item IDs that appear in Open items context or Resolved items context for this step.",
                "- If there is no valid operation, write `- None`.",
            ]
        )

        def _summary_prompt_context(user_prompt: str) -> dict[str, str]:
            context: dict[str, str] = {}
            lines = user_prompt.splitlines()
            for index, line in enumerate(lines):
                stripped = line.strip()
                if stripped == "Source document:" and index + 1 < len(lines):
                    context["source_document"] = lines[index + 1].strip()
                elif stripped == "Source hash:" and index + 1 < len(lines):
                    context["source_hash"] = lines[index + 1].strip()
            if "source_document" not in context or "source_hash" not in context:
                raise AssertionError("Summary prompt did not expose source document and hash.")
            return context

        def _summary_response(
            *,
            context: dict[str, str],
            scope: str,
            scope_block: bool = False,
            fenced: bool = False,
            key_decisions: list[str] | None = None,
            unresolved_questions: list[str] | None = None,
            critical_risks: list[str] | None = None,
            none_marker: str = "none",
        ) -> str:
            def render_list(name: str, values: list[str] | None) -> list[str]:
                lines = [f"  {name}:"]
                if values:
                    lines.extend([f"    - {value}" for value in values])
                else:
                    lines.append(f"    - {none_marker}")
                return lines

            lines = [
                "summary:",
                f"  source_document: {context['source_document']}",
                f"  source_hash: {context['source_hash']}",
            ]
            if scope_block:
                lines.append("  scope: |")
                lines.extend(
                    [
                        f"    {line}" if line else "    "
                        for line in scope.splitlines() or [""]
                    ]
                )
            else:
                lines.append(f"  scope: {scope}")
            lines.extend(render_list("key_decisions", key_decisions))
            lines.extend(render_list("unresolved_questions", unresolved_questions))
            lines.extend(render_list("critical_risks", critical_risks))
            rendered = "\n".join(lines)
            if fenced:
                return f"```yaml\n{rendered}\n```"
            return rendered

        def probe_summary_runner(workspace, source_document_path):
            source_path = Path(source_document_path)
            if not source_path.is_absolute():
                source_path = workspace.root / source_path
            source_text = read_text_file(source_path)
            return {
                "source_document": str(source_path.relative_to(workspace.root)),
                "source_hash": sha256(source_text.encode("utf-8")).hexdigest(),
                "scope": f"Summary for {source_path.name}",
                "key_decisions": [f"Decision captured from {source_path.name}"],
                "unresolved_questions": [],
                "critical_risks": [],
            }

        def summary_runner(workspace, source_document_path):
            source_path = Path(source_document_path)
            if not source_path.is_absolute():
                source_path = workspace.root / source_path
            summary_calls.append(source_path.name)

            def summary_llm(system_prompt: str, user_prompt: str) -> str:
                context = _summary_prompt_context(user_prompt)
                source_name = Path(context["source_document"]).name
                if source_name == "PRD_V0.md":
                    return _summary_response(
                        context=context,
                        scope="Grounded scope for PRD_V0.md",
                        scope_block=True,
                        fenced=True,
                        key_decisions=["Decision captured from PRD_V0.md"],
                        unresolved_questions=[],
                        critical_risks=[],
                    )
                return _summary_response(
                    context=context,
                    scope=f"Grounded scope for {source_name}",
                    key_decisions=[f"Decision captured from {source_name}"],
                    unresolved_questions=[f"Follow-up from {source_name}"],
                    critical_risks=[],
                )

            return generate_summary(workspace, source_path, llm_call=summary_llm)

        prompt_root = REPO_ROOT / "app" / "prompts V4"
        for prompt_path in sorted(prompt_root.glob("*_prompt.md")):
            prompt_text = prompt_path.read_text(encoding="utf-8")
            assert "TARGET1" not in prompt_text, prompt_path.name
            assert "- TYPE | AUTHOR |" not in prompt_text, prompt_path.name
            if prompt_path.name != "summary_prompt.md":
                assert "Every required top-level section heading must start with `##`." in prompt_text
                assert "title and content are separate create-item fields" in prompt_text
                assert "use one bullet marker only" in prompt_text
                assert "never write only `- None`" in prompt_text
                assert "Blackboard Items To Create` and `## Blackboard Items To Update` consecutive" in prompt_text
                assert "Blackboard Items To Update`; it is the final section" in prompt_text
            if prompt_path.name == "product_prompt.md":
                assert "Always include the parent heading `## Product Arbitration`" in prompt_text
            if prompt_path.name == "tech_prompt.md":
                assert "### Mermaid Diagram" in prompt_text
                assert "Do not copy a generic sample diagram" in prompt_text
                assert "App[App]" not in prompt_text

        for mode_label in (
            "initial_draft",
            "review",
            "revision",
            "item_resolution",
            "candidate_rewrite",
            "verification",
            "finalization",
        ):
            built_prompt = orchestrator._build_v4_user_prompt(
                role="product",
                mode_label=mode_label,
                project_brief="Project name: Prompt Harness\n\nBuild a V4 validation harness.",
                project_brief_source="scripts/check_v4_flow_no_llm.py",
                workspace=prompt_workspace,
                open_items=[],
                summaries={},
                documents={},
                extra_context=[],
            )
            assert operation_reminder in built_prompt
            if mode_label == "initial_draft":
                assert contextual_instruction in built_prompt
            else:
                assert "Contextual step instruction:" not in built_prompt

        growth_finalization_prompt = orchestrator._build_v4_user_prompt(
            role="growth",
            mode_label="finalization",
            project_brief="Project name: Prompt Harness\n\nBuild a V4 validation harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=prompt_workspace,
            open_items=[],
            summaries={},
            documents={},
            extra_context=[],
        )
        assert "Contextual finalization instruction:" in growth_finalization_prompt
        assert "create only a RISK or WARNING item" in growth_finalization_prompt
        product_finalization_prompt = orchestrator._build_v4_user_prompt(
            role="product",
            mode_label="finalization",
            project_brief="Project name: Prompt Harness\n\nBuild a V4 validation harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=prompt_workspace,
            open_items=[],
            summaries={},
            documents={},
            extra_context=[],
        )
        assert "Contextual finalization instruction:" not in product_finalization_prompt

        valid_initial_draft_sample = _build_document("product", "initial_draft")
        valid_initial_draft_parsed = parse_v4_agent_response(valid_initial_draft_sample)
        orchestrator.validate_v4_document(
            role="product",
            mode_label="initial_draft",
            parsed_response=valid_initial_draft_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
        )
        orchestrator.validate_v4_item_operations(
            role="product",
            mode_label="initial_draft",
            parsed_response=valid_initial_draft_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
            existing_item_ids=set(),
        )
        nested_none_initial_draft = parse_v4_agent_response(
            valid_initial_draft_sample.replace(
                "## Blackboard Items To Update\n\n- None",
                "## Blackboard Items To Update\n\n- - None",
            )
        )
        orchestrator.validate_v4_document(
            role="product",
            mode_label="initial_draft",
            parsed_response=nested_none_initial_draft,
            raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
        )
        orchestrator.validate_v4_item_operations(
            role="product",
            mode_label="initial_draft",
            parsed_response=nested_none_initial_draft,
            raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
            existing_item_ids=set(),
        )

        def _copyable_template_product_initial_draft() -> dict:
            raw_response = "\n".join(
                [
                    "# Product initial draft",
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
                    "- Product initial draft notes.",
                    "",
                    "## Blackboard Items To Create",
                    "",
                    "- TYPE | AUTHOR | TARGET1, TARGET2 | PRIORITY | tag1, tag2 | Title | Content",
                    "",
                    "## Blackboard Items To Update",
                    "",
                    "- None",
                ]
            )
            parsed = parse_v4_agent_response(raw_response)
            parsed["raw_response"] = raw_response
            parsed["mode_label"] = "initial_draft"
            parsed["role"] = "product"
            return parsed

        def _update_only_initial_draft() -> dict:
            raw_response = "\n".join(
                [
                    "# Product initial draft",
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
                    "- Product initial draft notes.",
                    "",
                    "## Blackboard Items To Create",
                    "",
                    "- QUESTION | PRODUCT | PRODUCT | HIGH | scope | Clarify scope | Need a decision.",
                    "",
                    "## Blackboard Items To Update",
                    "",
                    "- ITEM-001 | ANSWERED",
                ]
            )
            parsed = parse_v4_agent_response(raw_response)
            parsed["raw_response"] = raw_response
            parsed["mode_label"] = "initial_draft"
            parsed["role"] = "product"
            return parsed

        invalid_template_workspaces: list = []

        def invalid_template_workspace_factory(project_name: str):
            workspace = create_run_workspace(project_name, base_root=runs_root)
            invalid_template_workspaces.append(workspace)
            return workspace

        try:
            orchestrator.run_v4_flow(
                "Harness Template Failure",
                "Project name: Harness Template Failure\n\nBuild a V4 validation harness.",
                "scripts/check_v4_flow_no_llm.py",
                workspace_factory=invalid_template_workspace_factory,
                summary_runner=probe_summary_runner,
                agent_runner=lambda **kwargs: _copyable_template_product_initial_draft()
                if kwargs["role"] == "product" and kwargs["mode_label"] == "initial_draft"
                else _fake_v4_agent_output(kwargs["role"], kwargs["mode_label"]),
            )
        except ValueError as exc:
            assert "field 'targets'" in str(exc)
            assert "TARGET1, TARGET2" in str(exc)
            assert invalid_template_workspaces
            template_trace_path = (
                invalid_template_workspaces[0].root
                / "agent_outputs"
                / "product_initial_draft.raw.md"
            )
            assert template_trace_path.exists()
            assert str(template_trace_path) in str(exc)
        else:
            raise AssertionError("Template item rows must fail before persistence.")

        invalid_update_workspaces: list = []

        def invalid_update_workspace_factory(project_name: str):
            workspace = create_run_workspace(project_name, base_root=runs_root)
            invalid_update_workspaces.append(workspace)
            return workspace

        try:
            orchestrator.run_v4_flow(
                "Harness Update Failure",
                "Project name: Harness Update Failure\n\nBuild a V4 validation harness.",
                "scripts/check_v4_flow_no_llm.py",
                workspace_factory=invalid_update_workspace_factory,
                summary_runner=probe_summary_runner,
                agent_runner=lambda **kwargs: _update_only_initial_draft()
                if kwargs["role"] == "product" and kwargs["mode_label"] == "initial_draft"
                else _fake_v4_agent_output(kwargs["role"], kwargs["mode_label"]),
            )
        except ValueError as exc:
            assert "field 'id'" in str(exc)
            assert "ITEM-001" in str(exc)
            assert invalid_update_workspaces
            update_trace_path = (
                invalid_update_workspaces[0].root
                / "agent_outputs"
                / "product_initial_draft.raw.md"
            )
            assert update_trace_path.exists()
            assert str(update_trace_path) in str(exc)
        else:
            raise AssertionError("Updating an item created in the same response must fail.")

        def workspace_factory(project_name: str):
            workspace = create_run_workspace(project_name, base_root=runs_root)
            valid_workspaces.append(workspace)
            return workspace

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
                    "extra_context": list(extra_context),
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
        assert all(
            not context.lstrip().startswith("##")
            for call in valid_calls
            for context in call["extra_context"]
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

            prd_v0_trace_path = (
                valid_workspace.root / "summary_outputs" / "product-PRD_V0.summary.raw.yaml"
            )
            assert prd_v0_trace_path.exists()
            assert prd_v0_trace_path.read_text(encoding="utf-8").startswith("```yaml")
            assert not (public_output_dir / "summary_outputs").exists()
            assert not any(
                path.name.endswith(".summary.raw.yaml") for path in public_output_dir.rglob("*")
            )

            def summary_source(filename: str, body: str) -> Path:
                path = summary_validation_workspace.product_documents_dir / filename
                write_text_file(path, body)
                return path

            def expect_summary_failure(
                *,
                filename: str,
                response_text: str,
                expected_substrings: tuple[str, ...],
            ) -> None:
                source_path = summary_source(
                    filename, f"Summary validation source for {filename}."
                )
                raw_trace_path = (
                    summary_validation_workspace.root
                    / "summary_outputs"
                    / f"product-{Path(filename).stem}.summary.raw.yaml"
                )

                def failing_llm(system_prompt: str, user_prompt: str) -> str:
                    return response_text.format(**_summary_prompt_context(user_prompt))

                try:
                    generate_summary(summary_validation_workspace, source_path, llm_call=failing_llm)
                except ValueError as exc:
                    error_text = str(exc)
                    assert str(raw_trace_path) in error_text
                    for substring in expected_substrings:
                        assert substring in error_text
                    assert raw_trace_path.exists()
                    assert raw_trace_path.read_text(encoding="utf-8").strip()
                else:
                    raise AssertionError(f"Summary case '{filename}' must fail.")

            scalar_summary_source = summary_source(
                "PRD_scalar.md", "Scalar summary validation source."
            )

            def scalar_summary_llm(system_prompt: str, user_prompt: str) -> str:
                context = _summary_prompt_context(user_prompt)
                return _summary_response(
                    context=context,
                    scope="Scalar scope for PRD_scalar.md",
                    key_decisions=["Decision A"],
                    unresolved_questions=["Question A"],
                    critical_risks=["Risk A"],
                )

            scalar_summary = generate_summary(
                summary_validation_workspace,
                scalar_summary_source,
                llm_call=scalar_summary_llm,
            )
            assert scalar_summary["scope"] == "Scalar scope for PRD_scalar.md"
            assert scalar_summary["key_decisions"] == ["Decision A"]
            assert scalar_summary["source_document"] == str(
                scalar_summary_source.relative_to(summary_validation_workspace.root)
            )
            assert scalar_summary["source_hash"] == sha256(
                scalar_summary_source.read_text(encoding="utf-8").encode("utf-8")
            ).hexdigest()
            assert (
                summary_validation_workspace.root
                / "summary_outputs"
                / "product-PRD_scalar.summary.raw.yaml"
            ).exists()

            block_summary_source = summary_source(
                "PRD_block.md", "Block summary validation source."
            )

            def block_summary_llm(system_prompt: str, user_prompt: str) -> str:
                context = _summary_prompt_context(user_prompt)
                return _summary_response(
                    context=context,
                    scope="Block scope line 1\nBlock scope line 2",
                    scope_block=True,
                    key_decisions=["Decision B"],
                    unresolved_questions=["Question B"],
                    critical_risks=["Risk B"],
                )

            block_summary = generate_summary(
                summary_validation_workspace,
                block_summary_source,
                llm_call=block_summary_llm,
            )
            assert block_summary["scope"] == "Block scope line 1\nBlock scope line 2"

            fenced_summary_source = summary_source(
                "PRD_fenced.md", "Fenced summary validation source."
            )

            def fenced_summary_llm(system_prompt: str, user_prompt: str) -> str:
                context = _summary_prompt_context(user_prompt)
                return _summary_response(
                    context=context,
                    scope="Fenced scope for PRD_fenced.md",
                    fenced=True,
                    key_decisions=["Decision C"],
                    unresolved_questions=["Question C"],
                    critical_risks=["Risk C"],
                )

            fenced_summary = generate_summary(
                summary_validation_workspace,
                fenced_summary_source,
                llm_call=fenced_summary_llm,
            )
            assert fenced_summary["scope"] == "Fenced scope for PRD_fenced.md"

            none_summary_source = summary_source("PRD_none.md", "None summary validation source.")

            def none_summary_llm(system_prompt: str, user_prompt: str) -> str:
                context = _summary_prompt_context(user_prompt)
                return _summary_response(
                    context=context,
                    scope="None marker scope for PRD_none.md",
                    key_decisions=[],
                    unresolved_questions=[],
                    critical_risks=[],
                )

            none_summary = generate_summary(
                summary_validation_workspace,
                none_summary_source,
                llm_call=none_summary_llm,
            )
            assert none_summary["key_decisions"] == []
            assert none_summary["unresolved_questions"] == []
            assert none_summary["critical_risks"] == []

            repeat_summary_source = summary_source(
                "PRD_repeat.md", "Repeat summary validation source."
            )
            repeat_summary_first = generate_summary(
                summary_validation_workspace,
                repeat_summary_source,
                llm_call=scalar_summary_llm,
            )
            repeat_summary_second = generate_summary(
                summary_validation_workspace,
                repeat_summary_source,
                llm_call=scalar_summary_llm,
            )
            assert repeat_summary_first["source_document"] == repeat_summary_second[
                "source_document"
            ]
            repeat_trace_first = (
                summary_validation_workspace.root
                / "summary_outputs"
                / "product-PRD_repeat.summary.raw.yaml"
            )
            repeat_trace_second = (
                summary_validation_workspace.root
                / "summary_outputs"
                / "product-PRD_repeat_02.summary.raw.yaml"
            )
            assert repeat_trace_first.exists()
            assert repeat_trace_second.exists()

            expect_summary_failure(
                filename="PRD_root_bullet.md",
                response_text="\n".join(
                    [
                        "summary:",
                        "  source_document: {source_document}",
                        "  source_hash: {source_hash}",
                        "  scope: Root bullet scope",
                        "- See above",
                    ]
                ),
                expected_substrings=(
                    "Summary parsing failed",
                    "raw trace",
                    "Summary list items must be nested under a summary field",
                ),
            )

            expect_summary_failure(
                filename="PRD_malformed_bullet.md",
                response_text="\n".join(
                    [
                        "summary:",
                        "  source_document: {source_document}",
                        "  source_hash: {source_hash}",
                        "  scope: Malformed bullet scope",
                        "  - MVP core features defined",
                    ]
                ),
                expected_substrings=(
                    "Summary parsing failed",
                    "raw trace",
                    "Summary list items must be nested under a summary field",
                ),
            )

            expect_summary_failure(
                filename="PRD_unknown_field.md",
                response_text="\n".join(
                    [
                        "summary:",
                        "  source_document: {source_document}",
                        "  source_hash: {source_hash}",
                        "  scope: Unknown field scope",
                        "  mystery_field: nope",
                        "  key_decisions:",
                        "    - Decision X",
                        "  unresolved_questions:",
                        "    - none",
                        "  critical_risks:",
                        "    - none",
                    ]
                ),
                expected_substrings=(
                    "Summary parsing failed",
                    "raw trace",
                    "Unexpected summary field: mystery_field",
                ),
            )

            expect_summary_failure(
                filename="PRD_duplicate_field.md",
                response_text="\n".join(
                    [
                        "summary:",
                        "  source_document: {source_document}",
                        "  source_hash: {source_hash}",
                        "  scope: Duplicate field scope",
                        "  key_decisions:",
                        "    - Decision X",
                        "  key_decisions:",
                        "    - Decision Y",
                        "  unresolved_questions:",
                        "    - none",
                        "  critical_risks:",
                        "    - none",
                    ]
                ),
                expected_substrings=(
                    "Summary parsing failed",
                    "raw trace",
                    "Duplicate summary field: key_decisions",
                ),
            )

            expect_summary_failure(
                filename="PRD_wrong_source_document.md",
                response_text="\n".join(
                    [
                        "summary:",
                        "  source_document: wrong/path/PRD_wrong_source_document.md",
                        "  source_hash: {source_hash}",
                        "  scope: Wrong source document scope",
                        "  key_decisions:",
                        "    - Decision X",
                        "  unresolved_questions:",
                        "    - none",
                        "  critical_risks:",
                        "    - none",
                    ]
                ),
                expected_substrings=(
                    "Summary validation failed",
                    "raw trace",
                    "Summary source_document does not match the source path",
                ),
            )

            expect_summary_failure(
                filename="PRD_wrong_source_hash.md",
                response_text="\n".join(
                    [
                        "summary:",
                        "  source_document: {source_document}",
                        "  source_hash: deadbeef",
                        "  scope: Wrong hash scope",
                        "  key_decisions:",
                        "    - Decision X",
                        "  unresolved_questions:",
                        "    - none",
                        "  critical_risks:",
                        "    - none",
                    ]
                ),
                expected_substrings=(
                    "Summary validation failed",
                    "raw trace",
                    "Summary source_hash does not match the source document",
                ),
            )

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

            boundary_cases = [
                ("product", "GTM_V0.md"),
                ("product", "Go-To-Market Notes"),
                ("product", "Technical Readiness"),
                ("growth", "Technical Readiness"),
                ("tech", "Go-To-Market Notes"),
            ]
            for role, forbidden_heading in boundary_cases:
                parsed = parse_v4_agent_response(_build_document(role, "review"))
                parsed["sections"][forbidden_heading] = "- Copied content."
                try:
                    orchestrator.validate_v4_document(
                        role=role,
                        mode_label="review",
                        parsed_response=parsed,
                        raw_response_trace_path=f"runs/fake/agent_outputs/{role}_review.raw.md",
                    )
                except ValueError as exc:
                    assert forbidden_heading in str(exc)
                    assert "unexpected top-level heading" in str(exc)
                else:
                    raise AssertionError(
                        f"{role} forbidden heading '{forbidden_heading}' must fail."
                    )

            readiness_cases = {
                "product": ("Product Readiness", "READY"),
                "growth": ("GTM Readiness", "LIMITED"),
                "tech": ("Technical Readiness", "INSUFFICIENT"),
            }
            for role, (section_name, status_value) in readiness_cases.items():
                parsed = parse_v4_agent_response(_build_document(role, "review"))
                parsed["sections"][section_name] = "\n".join(
                    [
                        f"Status: {status_value}",
                        "",
                        "Blocking Gaps:",
                        "- None",
                        "",
                        "Required Improvements:",
                        "- None",
                    ]
                )
                orchestrator.validate_v4_document(
                    role=role,
                    mode_label="review",
                    parsed_response=parsed,
                    raw_response_trace_path=f"runs/fake/agent_outputs/{role}_review.raw.md",
                )

            placeholder_readiness_cases = {
                "product": "Product Readiness",
                "growth": "GTM Readiness",
                "tech": "Technical Readiness",
            }
            for role, section_name in placeholder_readiness_cases.items():
                parsed = parse_v4_agent_response(_build_document(role, "review"))
                parsed["sections"][section_name] = "\n".join(
                    [
                        "Status: READY / LIMITED / INSUFFICIENT",
                        "",
                        "Blocking Gaps:",
                        "- None",
                        "",
                        "Required Improvements:",
                        "- None",
                    ]
                )
                try:
                    orchestrator.validate_v4_document(
                        role=role,
                        mode_label="review",
                        parsed_response=parsed,
                        raw_response_trace_path=f"runs/fake/agent_outputs/{role}_review.raw.md",
                    )
                except ValueError as exc:
                    assert section_name in str(exc)
                    assert "READY / LIMITED / INSUFFICIENT" in str(exc)
                    assert "invalid status" in str(exc)
                else:
                    raise AssertionError(
                        f"{role} placeholder readiness must fail validation."
                    )

            topic_only_parse = {
                "items_to_create": [
                    {
                        "type": "QUESTION",
                        "author": "PRODUCT",
                        "targets": ["PRICING_MODEL"],
                        "priority": "HIGH",
                        "tags": ["pricing"],
                        "title": "Topic only",
                        "content": "This target should be rejected.",
                        "raw_line": "- QUESTION | PRODUCT | PRICING_MODEL | HIGH | pricing | Topic only | This target should be rejected.",
                    }
                ],
                "items_to_update": [],
            }
            try:
                orchestrator.validate_v4_item_operations(
                    role="product",
                    mode_label="verification",
                    parsed_response=topic_only_parse,
                    raw_response_trace_path="runs/fake/agent_outputs/product_verification.raw.md",
                    existing_item_ids={"ITEM-001"},
                )
            except ValueError as exc:
                assert "field 'targets'" in str(exc)
                assert "PRICING_MODEL" in str(exc)
            else:
                raise AssertionError("Topic-only targets must fail before persistence.")

            assert orchestrator._owners_for_targets(["ALL"]) == ["product", "growth", "tech"]
            assert orchestrator._owners_for_targets(["PRICING_MODEL"]) == []

            all_target_workspace = create_run_workspace("Harness All Target", base_root=runs_root)
            all_target_item = orchestrator.create_item(
                all_target_workspace,
                type="QUESTION",
                author="PRODUCT",
                targets=["ALL"],
                priority="HIGH",
                tags=["routing"],
                title="Route to everyone",
                content="This should reach every role owner.",
            )
            assert all_target_item["targets"] == ["PRODUCT", "GROWTH", "TECH"]
            assert orchestrator._owners_for_targets(all_target_item["targets"]) == [
                "product",
                "growth",
                "tech",
            ]

            open_items_context = orchestrator._format_open_items_context(
                all_target_workspace,
                [all_target_item],
            )
            assert "Item id: ITEM-001" in open_items_context
            assert "Read-only blackboard item:" in open_items_context
            assert not any(
                line.startswith("- ITEM-") and " | " in line
                for line in open_items_context.splitlines()
            )

            resolved_items_context = orchestrator._format_items_context(
                "Resolved Items",
                [all_target_item],
            )
            assert "Item id: ITEM-001" in resolved_items_context
            assert not any(
                line.startswith("- ITEM-") and " | " in line
                for line in resolved_items_context.splitlines()
            )

            growth_create_update_confusion = _build_document("growth", "review").replace(
                "- None\n\n## Blackboard Items To Update\n\n- None",
                (
                    "- ITEM-005 | OPEN | ALL | HIGH | data-model, privacy | "
                    "Data ownership and consent model | Define who owns data.\n\n"
                    "## Blackboard Items To Update\n\n- None"
                ),
                1,
            )
            growth_confusion_parsed = parse_v4_agent_response(growth_create_update_confusion)
            try:
                orchestrator.validate_v4_item_operations(
                    role="growth",
                    mode_label="review",
                    parsed_response=growth_confusion_parsed,
                    raw_response_trace_path="runs/fake/agent_outputs/growth_review.raw.md",
                    existing_item_ids={"ITEM-005"},
                )
            except ValueError as exc:
                assert "Blackboard Items To Create" in str(exc)
                assert "Blackboard Items To Update" in str(exc)
                assert "ITEM-005" in str(exc)
                assert "growth_review.raw.md" in str(exc)
            else:
                raise AssertionError("Create rows starting with ITEM ids must fail clearly.")

            malformed_update_doc = _build_document("growth", "review").replace(
                "## Blackboard Items To Update\n\n- None",
                "## Blackboard Items To Update\n\n- ITEM-005 | OPEN | ALL | HIGH | data-model | Bad | Bad",
                1,
            )
            try:
                parse_v4_agent_response(malformed_update_doc)
            except ValueError as exc:
                assert "Blackboard Items To Update" in str(exc)
                assert "exactly" in str(exc)
                assert "ITEM-005 | OPEN | ALL | HIGH" in str(exc)
            else:
                raise AssertionError("Update rows with extra fields must fail parsing.")

            valid_update_doc = _build_document("growth", "review").replace(
                "## Blackboard Items To Update\n\n- None",
                "## Blackboard Items To Update\n\n- ITEM-005 | ANSWERED",
                1,
            )
            valid_update_parsed = parse_v4_agent_response(valid_update_doc)
            orchestrator.validate_v4_item_operations(
                role="growth",
                mode_label="review",
                parsed_response=valid_update_parsed,
                raw_response_trace_path="runs/fake/agent_outputs/growth_review.raw.md",
                existing_item_ids={"ITEM-005"},
            )

            nested_update_doc = _build_document("growth", "review").replace(
                "## Blackboard Items To Update\n\n- None",
                "## Blackboard Items To Update\n\n- - ITEM-005 | ANSWERED",
                1,
            )
            nested_update_parsed = parse_v4_agent_response(nested_update_doc)
            assert nested_update_parsed["items_to_update"][0]["raw_line"] == (
                "ITEM-005 | ANSWERED"
            )
            orchestrator.validate_v4_item_operations(
                role="growth",
                mode_label="review",
                parsed_response=nested_update_parsed,
                raw_response_trace_path="runs/fake/agent_outputs/growth_review.raw.md",
                existing_item_ids={"ITEM-005"},
            )

            missing_update_parse = {
                "items_to_create": [],
                "items_to_update": [
                    {
                        "id": "ITEM-404",
                        "status": "ANSWERED",
                        "raw_line": "ITEM-404 | ANSWERED",
                    }
                ],
            }
            try:
                orchestrator.validate_v4_item_operations(
                    role="product",
                    mode_label="verification",
                    parsed_response=missing_update_parse,
                    raw_response_trace_path="runs/fake/agent_outputs/product_verification.raw.md",
                    existing_item_ids={"ITEM-001"},
                )
            except ValueError as exc:
                assert "ITEM-404" in str(exc)
                assert "field 'id'" in str(exc)
            else:
                raise AssertionError("Updates for missing items must fail before persistence.")

            same_response_update_parse = {
                "items_to_create": [
                    {
                        "type": "QUESTION",
                        "author": "PRODUCT",
                        "targets": ["PRODUCT"],
                        "priority": "HIGH",
                        "tags": ["followup"],
                        "title": "Follow-up item",
                        "content": "This item should not be updated in the same response.",
                        "raw_line": "- QUESTION | PRODUCT | PRODUCT | HIGH | followup | Follow-up item | This item should not be updated in the same response.",
                    }
                ],
                "items_to_update": [
                    {
                        "id": "ITEM-001",
                        "status": "ANSWERED",
                        "raw_line": "ITEM-001 | ANSWERED",
                    }
                ],
            }
            try:
                orchestrator.validate_v4_item_operations(
                    role="product",
                    mode_label="verification",
                    parsed_response=same_response_update_parse,
                    raw_response_trace_path="runs/fake/agent_outputs/product_verification.raw.md",
                    existing_item_ids=set(),
                )
            except ValueError as exc:
                assert "ITEM-001" in str(exc)
                assert "field 'id'" in str(exc)
            else:
                raise AssertionError(
                    "Items created in the same response must not be updated."
                )

            finalization_followup_parse = {
                "items_to_create": [
                    {
                        "type": "PROPOSAL",
                        "author": "GROWTH",
                        "targets": ["ALL"],
                        "priority": "HIGH",
                        "tags": ["compliance"],
                        "title": "Regional compliance plan",
                        "content": "Draft a region-specific compliance plan.",
                        "raw_line": "PROPOSAL | GROWTH | ALL | HIGH | compliance | Regional compliance plan | Draft a region-specific compliance plan.",
                    }
                ],
                "items_to_update": [
                    {
                        "id": "ITEM-001",
                        "status": "ACCEPTED",
                        "raw_line": "ITEM-001 | ACCEPTED",
                    }
                ],
            }
            orchestrator._normalize_v4_finalization_create_types(finalization_followup_parse)
            orchestrator._drop_v4_finalization_updates(finalization_followup_parse)
            normalized_followup = finalization_followup_parse["items_to_create"][0]
            assert normalized_followup["type"] == "WARNING"
            assert "finalization-followup" in normalized_followup["tags"]
            assert "Originally emitted as PROPOSAL during finalization." in normalized_followup["content"]
            assert finalization_followup_parse["items_to_update"] == []
            assert finalization_followup_parse["ignored_finalization_updates"][0]["id"] == "ITEM-001"
            orchestrator.validate_v4_item_operations(
                role="growth",
                mode_label="finalization",
                parsed_response=finalization_followup_parse,
                raw_response_trace_path="runs/fake/agent_outputs/growth_finalization.raw.md",
                allowed_create_types={"RISK", "WARNING"},
                allow_updates=False,
                existing_item_ids={"ITEM-001"},
            )
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
