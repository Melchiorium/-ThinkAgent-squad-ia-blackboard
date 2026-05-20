#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha256
import json
import tempfile
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app import orchestrator
from app import artifact_writer
from app.artifact_writer import write_v4_run_artifacts
from app.blackboard_items import create_item
from app.run_documents import write_document
from app.run_store import create_run_workspace, read_text_file
from app.run_summaries import generate_summary
from app.v4_parsing import (
    parse_v4_agent_response,
    parse_v4_blackboard_operations,
    parse_v4_structured_document,
)


def main() -> None:
    _validate_strict_document_parser()
    _validate_structured_blackboard_operations()
    _validate_structured_summaries()
    _validate_prompt_split_and_v4_flow()
    print("ok")


def _validate_strict_document_parser() -> None:
    product_doc = _build_document("product")
    parsed = parse_v4_agent_response(product_doc, role="product")
    assert parsed["items_to_create"] == []
    assert parsed["items_to_update"] == []
    assert parsed["blackboard_operation_format"] == "separate_json"
    orchestrator.validate_v4_document(
        role="product",
        mode_label="initial_draft",
        parsed_response=parsed,
        raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
    )

    invalid_heading = _build_document("growth").replace(
        "## GTM Readiness",
        "## Pragmatic Next Steps\n- This must be inside an allowed section.\n\n## GTM Readiness",
    )
    invalid_heading_parsed = parse_v4_agent_response(invalid_heading, role="growth")
    _expect_value_error(
        lambda: orchestrator.validate_v4_document(
            role="growth",
            mode_label="review",
            parsed_response=invalid_heading_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/growth_review.raw.md",
        ),
        "unexpected top-level heading",
    )

    _expect_value_error(
        lambda: parse_v4_agent_response(
            product_doc + "\n\nBLACKBOARD_OPERATIONS:\n{}\n",
            role="product",
        ),
        "must not contain blackboard operation protocol",
    )
    _expect_value_error(
        lambda: parse_v4_agent_response(
            product_doc + "\n\n## Blackboard Items To Create\n- None\n",
            role="product",
        ),
        "must not contain blackboard operation protocol",
    )
    _expect_value_error(
        lambda: orchestrator.validate_v4_document(
            role="product",
            mode_label="initial_draft",
            parsed_response=parse_v4_agent_response("# Product Draft\n\n" + product_doc),
            raw_response_trace_path="runs/fake/agent_outputs/product_initial_draft.raw.md",
        ),
        "unsupported heading level",
    )

    product_payload = _document_payload("product")
    structured = parse_v4_structured_document(product_payload, role="product")
    assert "## Core MVP Workflow" in structured["document_text"]
    assert "## Core MVP Workflows" not in structured["document_text"]
    orchestrator.validate_v4_document(
        role="product",
        mode_label="revision",
        parsed_response=structured,
        raw_response_trace_path="runs/fake/agent_outputs/product_revision.raw.md",
    )
    empty_list_payload = _document_payload("product")
    empty_list_payload["Out of Scope"] = []
    empty_list_payload["Product Readiness"] = {
        "status": "READY",
        "blocking_gaps": [],
        "required_improvements": [],
    }
    empty_list_payload["Product Locking"] = {
        "confirmed_in_scope": ["Strict V4 final documents."],
        "confirmed_deferred": [],
        "confirmed_out_of_scope": [],
        "locking_note": ["Product locks the final PRD before downstream finalization."],
    }
    empty_list_structured = parse_v4_structured_document(empty_list_payload, role="product")
    assert "- None" not in empty_list_structured["document_text"]
    assert "No explicit out-of-scope item identified." in empty_list_structured["document_text"]
    assert "No blocking gap identified." in empty_list_structured["document_text"]
    orchestrator.validate_v4_document(
        role="product",
        mode_label="verification",
        parsed_response=empty_list_structured,
        raw_response_trace_path="runs/fake/agent_outputs/product_verification.raw.md",
    )

    plural_payload = dict(product_payload)
    plural_payload["Core MVP Workflows"] = plural_payload.pop("Core MVP Workflow")
    _expect_value_error(
        lambda: parse_v4_structured_document(plural_payload, role="product"),
        "Unexpected V4 document section field: Core MVP Workflows",
    )

    body_heading_payload = dict(product_payload)
    body_heading_payload["Product Problem"] += (
        "\n\n## Core MVP Workflows\n- This injected top-level heading must fail."
    )
    body_heading_parsed = parse_v4_structured_document(body_heading_payload, role="product")
    _expect_value_error(
        lambda: orchestrator.validate_v4_document(
            role="product",
            mode_label="revision",
            parsed_response=body_heading_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/product_revision.raw.md",
        ),
        "unexpected top-level heading",
    )

    _expect_value_error(
        lambda: parse_v4_structured_document(
            {
                **_document_payload("tech"),
                "Architecture Notes": {
                    "mermaid_diagram": "```mermaid\nflowchart LR\n  A --> B\n```",
                    "notes": "The runtime owns Mermaid fences.",
                },
            },
            role="tech",
        ),
        "mermaid_diagram must not include code fences",
    )

    tech_structured = parse_v4_structured_document(_document_payload("tech"), role="tech")
    assert "```mermaid" in tech_structured["sections"]["Architecture Notes"]
    growth_structured = parse_v4_structured_document(_document_payload("growth"), role="growth")
    assert "Blocking Gaps:" in growth_structured["sections"]["GTM Readiness"]
    assert "Required Improvements:" in growth_structured["sections"]["GTM Readiness"]
    assert "No open questions remain." in growth_structured["sections"]["Open Questions"]

    placeholder_array_payload = _document_payload("tech")
    placeholder_array_payload["Open Questions"] = ["None."]
    _expect_value_error(
        lambda: parse_v4_structured_document(placeholder_array_payload, role="tech"),
        "placeholder list item 'None.'",
    )

    missing_readiness_field_payload = _document_payload("growth")
    missing_readiness_field_payload["GTM Readiness"] = dict(
        missing_readiness_field_payload["GTM Readiness"]
    )
    missing_readiness_field_payload["GTM Readiness"].pop("blocking_gaps")
    _expect_value_error(
        lambda: parse_v4_structured_document(missing_readiness_field_payload, role="growth"),
        "Missing V4 document field in section 'GTM Readiness': blocking_gaps",
    )

    blocking_without_improvement = _document_payload("growth")
    blocking_without_improvement["GTM Readiness"] = {
        "status": "LIMITED",
        "blocking_gaps": ["Specific security measures are not defined."],
        "required_improvements": [],
    }
    blocking_without_improvement_parsed = parse_v4_structured_document(
        blocking_without_improvement,
        role="growth",
    )
    _expect_value_error(
        lambda: orchestrator.validate_v4_document(
            role="growth",
            mode_label="finalization",
            parsed_response=blocking_without_improvement_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/growth_finalization.raw.md",
        ),
        "blocking gaps require at least one required improvement",
    )

    ready_with_blocking_gap = _document_payload("tech")
    ready_with_blocking_gap["Technical Readiness"] = {
        "status": "READY",
        "blocking_gaps": ["Architecture diagram is not implementable."],
        "required_improvements": ["Replace the narrative diagram with system components."],
    }
    ready_with_blocking_gap_parsed = parse_v4_structured_document(
        ready_with_blocking_gap,
        role="tech",
    )
    _expect_value_error(
        lambda: orchestrator.validate_v4_document(
            role="tech",
            mode_label="verification",
            parsed_response=ready_with_blocking_gap_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/tech_verification.raw.md",
        ),
        "READY status cannot keep material blocking gaps",
    )

    empty_locking_note = _document_payload("product")
    empty_locking_note["Product Locking"] = dict(empty_locking_note["Product Locking"])
    empty_locking_note["Product Locking"]["locking_note"] = []
    empty_locking_note_parsed = parse_v4_structured_document(empty_locking_note, role="product")
    _expect_value_error(
        lambda: orchestrator.validate_v4_document(
            role="product",
            mode_label="finalization",
            parsed_response=empty_locking_note_parsed,
            raw_response_trace_path="runs/fake/agent_outputs/product_finalization.raw.md",
        ),
        "final Product locking note must contain a concrete locking decision",
    )


def _validate_structured_blackboard_operations() -> None:
    parsed = parse_v4_blackboard_operations(
        {
            "create": [
                {
                    "type": "QUESTION",
                    "targets": ["TECH"],
                    "priority": "HIGH",
                    "tags": ["architecture"],
                    "title": "Confirm integration boundary",
                    "content": "The architecture must confirm where the integration boundary sits.",
                }
            ],
            "update": [],
        }
    )
    assert parsed["items_to_create"][0]["type"] == "QUESTION"
    assert parsed["items_to_create"][0]["targets"] == ["TECH"]

    _expect_value_error(
        lambda: parse_v4_blackboard_operations(
            [
                {
                    "type": "QUESTION",
                    "targets": ["TECH"],
                    "priority": "HIGH",
                    "tags": [],
                    "title": "Bare array",
                    "content": "Bare arrays are no longer accepted.",
                }
            ]
        ),
        "must be a JSON object",
    )
    _expect_value_error(
        lambda: parse_v4_blackboard_operations(
            {
                "create": [
                    {
                        "type": "QUESTION",
                        "targets": ["TECH"],
                        "priority": "HIGH",
                        "tags": [],
                        "title": "Unexpected author",
                        "content": "Author is assigned by runtime.",
                        "author": "PRODUCT",
                    }
                ],
                "update": [],
            }
        ),
        "Unexpected create operation field: author",
    )

    with tempfile.TemporaryDirectory(prefix="squad-ia-v4-items-") as temp_dir:
        workspace = create_run_workspace("Item Harness", base_root=Path(temp_dir))
        external_item = create_item(
            workspace,
            type="QUESTION",
            author="PRODUCT",
            targets=["EXTERNAL"],
            priority="HIGH",
            tags=["pricing"],
            title="Confirm external price",
            content="The brief does not contain a price.",
        )
        tech_item = create_item(
            workspace,
            type="QUESTION",
            author="PRODUCT",
            targets=["TECH"],
            priority="HIGH",
            tags=["architecture"],
            title="Confirm data store",
            content="The data store choice is unresolved.",
        )
        existing_items = {item["id"]: item for item in [external_item, tech_item]}

        _expect_value_error(
            lambda: create_item(
                workspace,
                type="QUESTION",
                author="PRODUCT",
                targets=["EXTERNAL"],
                priority="HIGH",
                tags=["pricing"],
                title="Lock external price",
                content="The current brief still does not contain a price.",
            ),
            "Duplicate open blackboard item",
        )
        reuse_result = orchestrator._apply_v4_item_operations(
            workspace,
            {
                "role": "growth",
                "mode_label": "verification",
                "items_to_create": [
                    {
                        "type": "QUESTION",
                        "targets": ["EXTERNAL"],
                        "priority": "HIGH",
                        "tags": ["pricing"],
                        "title": "Lock external price",
                        "content": "The current brief still does not contain a price.",
                        "raw_line": "{}",
                    }
                ],
                "items_to_update": [],
                "blackboard_operations_trace_path": (
                    "runs/fake/agent_outputs/growth_verification_blackboard.json"
                ),
            },
            default_author="GROWTH",
        )
        assert reuse_result["reused"] == 1

        launch_item = create_item(
            workspace,
            type="QUESTION",
            author="PRODUCT",
            targets=["EXTERNAL"],
            priority="HIGH",
            tags=["launch-market", "compliance", "data-handling"],
            title="Define first launch geography and minimum health-data compliance requirements",
            content=(
                "The brief flags sensitive medical information and country-specific "
                "legal/compliance issues, but does not specify the first launch market."
            ),
        )
        _expect_value_error(
            lambda: create_item(
                workspace,
                type="QUESTION",
                author="GROWTH",
                targets=["EXTERNAL"],
                priority="HIGH",
                tags=["launch-market", "compliance", "health-data"],
                title="Define the first launch geography and compliance regime",
                content=(
                    "The GTM plan depends on a concrete launch market because "
                    "storage and sharing of health-related information varies by country."
                ),
            ),
            "Duplicate open blackboard item",
        )
        external_reuse_result = orchestrator._apply_v4_item_operations(
            workspace,
            {
                "role": "product",
                "mode_label": "verification",
                "items_to_create": [
                    {
                        "type": "QUESTION",
                        "targets": ["EXTERNAL"],
                        "priority": "HIGH",
                        "tags": ["launch-market", "compliance", "data-handling"],
                        "title": (
                            "Confirm first launch geography and minimum health-data "
                            "compliance requirements"
                        ),
                        "content": (
                            "The revised PRD still depends on a concrete launch market "
                            "or compliance regime before sensitive care data handling "
                            "can be treated as launch-ready."
                        ),
                        "raw_line": "{}",
                    }
                ],
                "items_to_update": [],
                "blackboard_operations_trace_path": (
                    "runs/fake/agent_outputs/product_verification_blackboard.json"
                ),
            },
            default_author="PRODUCT",
        )
        assert external_reuse_result["reused"] == 1
        assert launch_item["id"]

        _expect_value_error(
            lambda: orchestrator.validate_v4_item_operations(
                role="product",
                mode_label="initial_draft",
                parsed_response={
                    "items_to_create": [
                        {
                            "type": "BROKEN",
                            "targets": ["TECH"],
                            "priority": "HIGH",
                            "tags": [],
                            "title": "Broken",
                            "content": "Invalid type.",
                            "raw_line": "{}",
                        }
                    ],
                    "items_to_update": [],
                },
                existing_item_ids=set(existing_items),
                existing_items_by_id=existing_items,
            ),
            "field 'type'",
        )
        _expect_value_error(
            lambda: orchestrator.validate_v4_item_operations(
                role="growth",
                mode_label="review",
                parsed_response={
                    "items_to_create": [
                        {
                            "type": "QUESTION",
                            "targets": ["GROWTH"],
                            "priority": "HIGH",
                            "tags": [],
                            "title": "Self target",
                            "content": "This should be resolved by Growth directly.",
                            "raw_line": "{}",
                        }
                    ],
                    "items_to_update": [],
                },
                existing_item_ids=set(existing_items),
                existing_items_by_id=existing_items,
            ),
            "field 'targets'",
        )
        _expect_value_error(
            lambda: orchestrator.validate_v4_item_operations(
                role="product",
                mode_label="revision",
                parsed_response={
                    "items_to_create": [],
                    "items_to_update": [
                        {"id": external_item["id"], "status": "ANSWERED", "raw_line": "{}"}
                    ],
                },
                existing_item_ids=set(existing_items),
                existing_items_by_id=existing_items,
            ),
            "non-EXTERNAL item id",
        )
        orchestrator.validate_v4_item_operations(
            role="product",
            mode_label="revision",
            parsed_response={
                "items_to_create": [],
                "items_to_update": [
                    {"id": tech_item["id"], "status": "ANSWERED", "raw_line": "{}"}
                ],
            },
            existing_item_ids=set(existing_items),
            existing_items_by_id=existing_items,
        )
        for role in ("PRODUCT", "GROWTH", "TECH"):
            _expect_value_error(
                lambda role=role: orchestrator._apply_v4_finalization_item_operations(
                    workspace,
                    {
                        "mode_label": "finalization",
                        "blackboard_operations_trace_path": (
                            "runs/fake/agent_outputs/"
                            f"{role.lower()}_finalization_blackboard.json"
                        ),
                        "items_to_create": [
                            {
                                "type": "DECISION",
                                "targets": ["ALL"],
                                "priority": "HIGH",
                                "tags": ["finalization"],
                                "title": "Late finalization decision",
                                "content": "Finalization must not create new work.",
                                "raw_line": (
                                    '{"type": "DECISION", "targets": ["ALL"], '
                                    '"title": "Late finalization decision"}'
                                ),
                            }
                        ],
                        "items_to_update": [],
                    },
                    default_author=role,
                ),
                "field 'create'",
            )

        external_market_item = create_item(
            workspace,
            type="QUESTION",
            author="TECH",
            targets=["PRODUCT"],
            priority="HIGH",
            tags=["market", "compliance"],
            title="Confirm pilot market",
            content="The brief does not define the first pilot market.",
        )
        _expect_value_error(
            lambda: orchestrator._validate_v4_external_decision_guardrails(
                role="product",
                mode_label="item_resolution",
                project_brief="Project name: External Guardrail\n\nNo country is specified.",
                open_items=[external_market_item],
                summaries={},
                documents={"product": _build_document("product")},
                parsed_response={
                    "document_text": _build_document("product").replace(
                        "one project brief",
                        "one United States pilot",
                    )
                },
                raw_response_trace_path=(
                    "runs/fake/agent_outputs/product_item_resolution.raw.md"
                ),
            ),
            "unsupported external decision term",
        )
        orchestrator._validate_v4_external_decision_guardrails(
            role="product",
            mode_label="item_resolution",
            project_brief=(
                "Project name: External Guardrail\n\n"
                "The first pilot market is the United States."
            ),
            open_items=[external_market_item],
            summaries={},
            documents={"product": _build_document("product")},
            parsed_response={
                "document_text": _build_document("product").replace(
                    "one project brief",
                    "one United States pilot",
                )
            },
            raw_response_trace_path="runs/fake/agent_outputs/product_item_resolution.raw.md",
        )


def _validate_structured_summaries() -> None:
    with tempfile.TemporaryDirectory(prefix="squad-ia-v4-summary-") as temp_dir:
        workspace = create_run_workspace("Summary Harness", base_root=Path(temp_dir))
        document_path = write_document(workspace, "product", "PRD_V0.md", _build_document("product"))
        source_text = read_text_file(document_path)
        expected_source = str(document_path.relative_to(workspace.root))
        expected_hash = sha256(source_text.encode("utf-8")).hexdigest()

        def fake_summary_llm(system_prompt: str, user_prompt: str, schema: dict, *, schema_name: str):
            assert "Return one JSON object" in system_prompt
            assert "Source document path to copy exactly into source_document" in user_prompt
            assert schema["properties"]["source_document"]["enum"] == [expected_source]
            assert schema["properties"]["source_hash"]["enum"] == [expected_hash]
            assert schema_name == "v4_summary"
            return {
                "source_document": expected_source,
                "source_hash": expected_hash,
                "scope": "Grounded PRD summary.",
                "key_decisions": ["The MVP wedge is explicit."],
                "unresolved_questions": [],
                "critical_risks": [],
            }

        summary = generate_summary(workspace, document_path, llm_call=fake_summary_llm)
        assert summary["source_hash"] == expected_hash
        raw_trace = workspace.root / "summary_outputs" / "product-PRD_V0.summary.raw.json"
        rendered_summary = workspace.summaries_dir / "product-PRD_V0.summary.yaml"
        assert raw_trace.exists()
        assert rendered_summary.exists()
        assert "summary:" in read_text_file(rendered_summary)

        def bad_summary_llm(system_prompt: str, user_prompt: str, schema: dict, *, schema_name: str):
            assert schema["properties"]["source_document"]["enum"] == [expected_source]
            assert schema["properties"]["source_hash"]["enum"] == [expected_hash]
            return {
                "source_document": source_text,
                "source_hash": expected_hash,
                "scope": "Grounded PRD summary.",
                "key_decisions": [],
                "unresolved_questions": [],
                "critical_risks": [],
            }

        _expect_value_error(
            lambda: generate_summary(workspace, document_path, llm_call=bad_summary_llm),
            "Summary source_document does not match the source path",
        )

        duplicate_path = write_document(workspace, "product", "PRD_DUPLICATE.md", source_text)
        cache_metrics: list[dict] = []

        def should_not_call_summary_llm(system_prompt: str, user_prompt: str, schema: dict, *, schema_name: str):
            raise AssertionError("Identical source document should reuse cached summary")

        cached_summary = generate_summary(
            workspace,
            duplicate_path,
            llm_call=should_not_call_summary_llm,
            metric_recorder=lambda run, metric: cache_metrics.append(metric),
        )
        assert cached_summary["source_document"].endswith("PRD_DUPLICATE.md")
        assert cached_summary["source_hash"] == expected_hash
        assert cache_metrics and cache_metrics[0]["status"] == "skipped"
        assert cache_metrics[0]["skip_reason"] == "summary_cache_hit"


def _validate_prompt_split_and_v4_flow() -> None:
    with tempfile.TemporaryDirectory(prefix="squad-ia-v4-flow-") as temp_dir:
        temp_root = Path(temp_dir)
        prompt_workspace = create_run_workspace("Prompt Harness", base_root=temp_root / "prompts")
        document_prompt = orchestrator._build_v4_user_prompt(
            role="product",
            mode_label="initial_draft",
            project_brief="Project name: Prompt Harness\n\nBuild a strict V4 harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=prompt_workspace,
            open_items=[],
            summaries={},
            documents={},
            extra_context=[],
        )
        assert "BLACKBOARD_OPERATIONS" not in document_prompt
        assert "Return only one JSON object matching the document schema" in document_prompt
        product_document_schema = orchestrator._build_v4_document_schema("product")
        assert "Core MVP Workflow" in product_document_schema["properties"]
        assert "Core MVP Workflows" not in product_document_schema["properties"]
        assert product_document_schema["properties"]["Product Readiness"]["type"] == "object"
        tech_document_schema = orchestrator._build_v4_document_schema("tech")
        architecture_schema = tech_document_schema["properties"]["Architecture Notes"]
        assert architecture_schema["type"] == "object"
        assert "mermaid_diagram" in architecture_schema["properties"]
        assert tech_document_schema["properties"]["Open Questions"]["type"] == "array"

        blackboard_prompt = orchestrator._build_v4_blackboard_prompt(
            role="product",
            mode_label="initial_draft",
            project_brief="Project name: Prompt Harness\n\nBuild a strict V4 harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=prompt_workspace,
            open_items=[],
            summaries={},
            documents={},
            produced_document=_build_document("product"),
            extra_context=[],
        )
        assert "Blackboard operations contract" in blackboard_prompt
        assert "Return only one JSON object" in blackboard_prompt
        finalization_prompt = orchestrator._build_v4_blackboard_prompt(
            role="growth",
            mode_label="finalization",
            project_brief="Project name: Prompt Harness\n\nBuild a strict V4 harness.",
            project_brief_source="scripts/check_v4_flow_no_llm.py",
            workspace=prompt_workspace,
            open_items=[],
            summaries={},
            documents={},
            produced_document=_build_document("growth"),
            extra_context=[],
        )
        finalization_schema = orchestrator._build_v4_blackboard_schema(
            role="growth",
            mode_label="finalization",
            updateable_items=[
                {
                    "id": "ITEM-010",
                    "status": "OPEN",
                    "targets": ["GROWTH"],
                }
            ],
        )
        assert "`create` must be empty" in finalization_prompt
        assert finalization_schema["properties"]["create"]["maxItems"] == 0
        assert "GROWTH" not in _target_schema_enums(finalization_schema)
        assert finalization_schema["properties"]["update"]["items"]["properties"]["id"]["enum"] == [
            "ITEM-010"
        ]
        product_blackboard_schema = orchestrator._build_v4_blackboard_schema(
            role="product",
            mode_label="initial_draft",
            updateable_items=[],
        )
        assert "PRODUCT" not in _target_schema_enums(product_blackboard_schema)
        assert _target_schema_allows_external_only(product_blackboard_schema)
        assert product_blackboard_schema["properties"]["update"]["maxItems"] == 0
        candidate_schema = orchestrator._build_v4_blackboard_schema(
            role="growth",
            mode_label="candidate_rewrite",
            updateable_items=[],
        )
        assert candidate_schema["properties"]["create"]["maxItems"] == 0

        original_call_llm_json = orchestrator.call_llm_json
        captured_document_prompts: list[str] = []
        captured_json_prompts: list[str] = []

        def fake_call_llm_json(
            system_prompt: str,
            user_prompt: str,
            schema: dict,
            *,
            schema_name: str,
        ) -> dict:
            if schema_name.endswith("_document"):
                captured_document_prompts.append(user_prompt)
                assert "Return only one JSON object matching the document schema" in user_prompt
                assert schema["additionalProperties"] is False
                return _document_payload(_role_from_document_schema(schema))
            captured_json_prompts.append(user_prompt)
            assert schema_name == "v4_blackboard_operations"
            if "Mode: finalization" in user_prompt:
                assert "`create` must be empty" in user_prompt
                assert schema["properties"]["create"]["maxItems"] == 0
            return {"create": [], "update": []}

        orchestrator.call_llm_json = fake_call_llm_json
        try:
            parsed = orchestrator._run_v4_agent(
                role="product",
                mode_label="initial_draft",
                project_brief="Project name: Prompt Harness\n\nBuild a strict V4 harness.",
                project_brief_source="scripts/check_v4_flow_no_llm.py",
                workspace=prompt_workspace,
                state={},
                open_items=[],
                summaries={},
                documents={},
                extra_context=[],
                agent_runner=None,
            )
            finalization_parsed = orchestrator._run_v4_agent(
                role="product",
                mode_label="finalization",
                project_brief="Project name: Prompt Harness\n\nBuild a strict V4 harness.",
                project_brief_source="scripts/check_v4_flow_no_llm.py",
                workspace=prompt_workspace,
                state={},
                open_items=[],
                summaries={},
                documents={},
                extra_context=[],
                agent_runner=None,
            )
            duplicate_summary = {
                "source_document": "documents/product/PRD_V0.md",
                "source_hash": sha256(_build_document("product").encode("utf-8")).hexdigest(),
                "scope": "Duplicate context test.",
                "key_decisions": ["Keep the context packet compact."],
                "unresolved_questions": [],
                "critical_risks": [],
            }
            orchestrator._run_v4_agent(
                role="growth",
                mode_label="review",
                project_brief="Project name: Prompt Harness\n\nBuild a strict V4 harness.",
                project_brief_source="scripts/check_v4_flow_no_llm.py",
                workspace=prompt_workspace,
                state={},
                open_items=[],
                summaries={"product": duplicate_summary},
                documents={"product": _build_document("product")},
                extra_context=[
                    orchestrator._format_summary_context("Product summary", duplicate_summary),
                    orchestrator._format_document_context("PRD_V0.md", _build_document("product")),
                ],
                agent_runner=None,
            )
        finally:
            orchestrator.call_llm_json = original_call_llm_json

        assert parsed["items_to_create"] == []
        assert finalization_parsed["items_to_create"] == []
        assert captured_document_prompts and captured_json_prompts
        assert "BLACKBOARD_OPERATIONS" not in captured_document_prompts[0]
        assert (
            prompt_workspace.root
            / "agent_outputs"
            / "product_initial_draft_document.json"
        ).exists()
        assert (prompt_workspace.root / "agent_outputs" / "product_initial_draft.raw.md").exists()
        assert (
            prompt_workspace.root
            / "agent_outputs"
            / "product_initial_draft_blackboard.json"
        ).exists()
        assert (
            prompt_workspace.root
            / "agent_outputs"
            / "product_finalization_blackboard.json"
        ).exists()
        review_prompt = next(prompt for prompt in captured_document_prompts if "Mode: review" in prompt)
        assert "Context document: PRODUCT document" in review_prompt
        assert "Context document: PRD_V0.md" not in review_prompt
        assert "Summary context: Product summary" not in review_prompt
        prompt_metrics = [
            json.loads(line)
            for line in read_text_file(prompt_workspace.root / "prompt_metrics.jsonl").splitlines()
        ]
        assert any(metric["call_type"] == "document" and metric["status"] == "ok" for metric in prompt_metrics)
        assert any(metric["call_type"] == "blackboard" and metric["status"] == "ok" for metric in prompt_metrics)
        assert any(
            metric["call_type"] == "blackboard" and metric["status"] == "skipped"
            for metric in prompt_metrics
        )

        valid_workspaces = []
        summary_calls: list[str] = []

        def workspace_factory(project_name: str):
            workspace = create_run_workspace(project_name, base_root=temp_root / "runs")
            valid_workspaces.append(workspace)
            return workspace

        def summary_runner(workspace, source_document_path):
            source_path = Path(source_document_path)
            if not source_path.is_absolute():
                source_path = workspace.root / source_path
            source_text = read_text_file(source_path)
            summary_calls.append(source_path.name)
            return {
                "source_document": str(source_path.relative_to(workspace.root)),
                "source_hash": sha256(source_text.encode("utf-8")).hexdigest(),
                "scope": f"Summary for {source_path.name}",
                "key_decisions": [f"Decision captured from {source_path.name}"],
                "unresolved_questions": [],
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
            if role == "product" and mode_label == "finalization":
                assert summaries["product"]["source_document"].endswith(
                    "PRD_POST_VERIFICATION_RESOLUTION_1.md"
                )
                parsed = parse_v4_agent_response(documents["product"], role="product")
                parsed["raw_response"] = documents["product"]
                parsed["role"] = role
                parsed["mode_label"] = mode_label
                parsed["items_to_create"] = []
                parsed["items_to_update"] = []
                parsed["blackboard_operation_format"] = "separate_json"
                return parsed
            return _fake_v4_agent_output(role, mode_label, open_items=open_items)

        state = orchestrator.run_v4_flow(
            "Harness Project",
            "Project name: Harness Project\n\nBuild a strict V4 harness.",
            "scripts/check_v4_flow_no_llm.py",
            workspace_factory=workspace_factory,
            summary_runner=summary_runner,
            agent_runner=agent_runner,
        )

        assert summary_calls.count("PRD_FINAL.md") == 1
        assert summary_calls.count("GTM_FINAL.md") == 1
        assert summary_calls.count("Architecture_FINAL.md") == 1
        assert state["post_verification_resolution_log"]
        assert "PRD_POST_VERIFICATION_RESOLUTION_1.md" in summary_calls
        output_dir = temp_root / "public"
        original_render = artifact_writer.render_architecture_diagram

        def fake_render_architecture_diagram(output_dir, blackboard):
            mmd_path = output_dir / "architecture-diagram.mmd"
            mmd_path.write_text("flowchart LR\n  A --> B\n", encoding="utf-8")
            return {
                "architecture_markdown_ready": True,
                "architecture_mermaid_ready": True,
                "architecture_mermaid_source": str(mmd_path),
                "architecture_visual_ready": False,
                "architecture_visual_status": "png_failed",
                "architecture_visual_warning": (
                    "Mermaid PNG generation failed because the Puppeteer Chrome "
                    "cache is missing. Run `PUPPETEER_CACHE_DIR=.cache/puppeteer "
                    "npx puppeteer browsers install chrome-headless-shell`."
                ),
                "architecture_image_ready": False,
                "architecture_image_path": "",
            }

        artifact_writer.render_architecture_diagram = fake_render_architecture_diagram
        try:
            write_v4_run_artifacts(state, output_dir)
        finally:
            artifact_writer.render_architecture_diagram = original_render
        assert (output_dir / "prd.md").exists()
        assert (output_dir / "gtm.md").exists()
        assert (output_dir / "architecture.md").exists()
        prd_output = read_text_file(output_dir / "prd.md")
        blackboard_output = read_text_file(output_dir / "blackboard.md")
        activity_log_output = read_text_file(output_dir / "activity_log.txt")
        assert "BLACKBOARD_OPERATIONS" not in prd_output
        assert "Product post-verification resolution marker" in prd_output
        assert "Architecture Visual Status" in blackboard_output
        assert "png_failed" in blackboard_output
        assert "Puppeteer Chrome cache is missing" in blackboard_output
        residual_gaps_output = artifact_writer._format_v4_residual_document_gaps_section(
            {
                "product": _product_document(),
                "growth": _growth_document().replace(
                    "Status: READY",
                    "Status: LIMITED",
                ).replace(
                    "- No blocking GTM gap remains for this harness.",
                    "- Specific security measures are not defined.",
                ),
                "tech": _tech_document().replace(
                    "- No technical open question remains for this harness.",
                    "- What specific security controls will be implemented?",
                ),
            }
        )
        assert "Residual Document Gaps" in residual_gaps_output
        assert "Product readiness is READY while Growth readiness is LIMITED." in residual_gaps_output
        assert "Growth blocking gap: Specific security measures are not defined." in residual_gaps_output
        assert "Tech open question: What specific security controls will be implemented?" in residual_gaps_output
        assert "final_artifact_status" in activity_log_output
        assert "png_ready=False" in activity_log_output


def _fake_v4_agent_output(role: str, mode_label: str, *, open_items: list[dict] | None = None) -> dict:
    raw_response = _build_document(role)
    if role == "product" and mode_label == "item_resolution" and open_items:
        raw_response = raw_response.replace(
            "## Product Locking",
            "- Product post-verification resolution marker is now part of the current PRD.\n\n## Product Locking",
        )
    parsed = parse_v4_agent_response(raw_response, role=role)
    parsed["raw_response"] = raw_response
    parsed["role"] = role
    parsed["mode_label"] = mode_label
    parsed["items_to_create"] = []
    parsed["items_to_update"] = []
    parsed["blackboard_operation_format"] = "separate_json"
    open_items = open_items or []
    if role == "product" and mode_label == "verification":
        parsed["items_to_create"] = [
            {
                "type": "QUESTION",
                "targets": ["GROWTH"],
                "priority": "HIGH",
                "tags": ["verification"],
                "title": "Resolve verification GTM gap",
                "content": "Growth must resolve this before finalization.",
                "raw_line": "{}",
            }
        ]
    if role == "growth" and mode_label == "item_resolution" and open_items:
        parsed["items_to_update"] = [
            {
                "id": open_items[0]["id"],
                "status": "ANSWERED",
                "raw_line": "{}",
            }
        ]
    if role == "tech" and mode_label == "verification":
        parsed["items_to_create"] = [
            {
                "type": "QUESTION",
                "targets": ["PRODUCT"],
                "priority": "HIGH",
                "tags": ["verification"],
                "title": "Resolve verification Product gap",
                "content": "Product must resolve this before finalization.",
                "raw_line": "{}",
            }
        ]
    if role == "product" and mode_label == "item_resolution" and open_items:
        parsed["items_to_update"] = [
            {
                "id": open_items[0]["id"],
                "status": "ANSWERED",
                "raw_line": "{}",
            }
        ]
    return parsed


def _document_payload(role: str) -> dict:
    sections = parse_v4_agent_response(_build_document(role), role=role)["sections"]
    if role == "product":
        sections["In Scope"] = ["Strict V4 final documents."]
        sections["Out of Scope"] = ["A fourth blackboard compiler agent."]
        sections["Critical Assumptions"] = [
            "A strict document contract and separate JSON operation contract reduce run failures."
        ]
        sections["How To Test Quickly"] = [
            "Run the no-LLM harness and inspect generated final artifacts."
        ]
        sections["Acceptance Criteria"] = [
            "The run creates final documents with no machine protocol in public outputs."
        ]
        sections["Risks And Failure Modes"] = [
            "Invalid structured outputs must fail before blackboard persistence."
        ]
        sections["Product Readiness"] = _readiness_payload()
        sections["Product Arbitration"] = {
            "retained": ["Keep Product as final arbiter."],
            "deferred": ["Defer generic orchestration abstractions."],
            "rejected": ["Reject permissive parsing as the normal path."],
            "open_points": [],
            "rationales": ["Separate structured outputs are easier to validate."],
        }
        sections["Product Locking"] = {
            "confirmed_in_scope": ["Strict V4 final documents."],
            "confirmed_deferred": ["Provider-specific advanced retry policies."],
            "confirmed_out_of_scope": ["A fourth blackboard compiler agent."],
            "locking_note": ["Product locks the final PRD before downstream finalization."],
        }
    if role == "growth":
        sections["Build Vs Pilot Operations"] = {
            "must_be_productized_now": ["Strict output validation and clear final artifacts."],
            "can_stay_manual_or_operational_during_pilot": [
                "Manual review after each live failure."
            ],
            "deferred_until_after_proof": ["Scaling beyond local runs."],
        }
        sections["Critical Assumptions"] = [
            "Reviewers value traceability more than flexible free-form generation."
        ]
        sections["Requested Changes"] = [
            "Keep public artifacts focused on final reader value."
        ]
        sections["Risks"] = ["A loose prompt contract would reintroduce output drift."]
        sections["Open Questions"] = []
        sections["Why This Could Fail Even With Good Execution"] = [
            "Users may still need live examples before trusting the workflow."
        ]
        sections["GTM Readiness"] = _readiness_payload()
    if role == "tech":
        sections["Architecture Notes"] = {
            "mermaid_diagram": "\n".join(
                [
                    "flowchart LR",
                    "    Brief[Project Brief] --> Product[Product]",
                    "    Product --> Growth[Growth]",
                    "    Product --> Tech[Tech]",
                    "    Growth --> Final[Final Outputs]",
                    "    Tech --> Final",
                ]
            ),
            "notes": "- The workflow stays local, explicit, and file-system first.",
        }
        sections["Critical Assumptions"] = [
            "The configured model can return JSON through the structured output path or strict fallback."
        ]
        sections["Requested Changes"] = ["Keep validation failures explicit and traceable."]
        sections["Risks"] = ["Provider-specific JSON support can vary and must fail clearly."]
        sections["Open Questions"] = []
        sections["Why This Could Fail Even With Good Execution"] = [
            "A provider that ignores JSON-only fallback can still cause a structured failure."
        ]
        sections["Technical Readiness"] = _readiness_payload()
    return sections


def _readiness_payload() -> dict:
    return {
        "status": "READY",
        "blocking_gaps": [],
        "required_improvements": ["Keep the static harness as the first validation gate."],
    }


def _role_from_document_schema(schema: dict) -> str:
    properties = schema.get("properties", {})
    if "Product Problem" in properties:
        return "product"
    if "Go-To-Market Notes" in properties:
        return "growth"
    if "Architecture Notes" in properties:
        return "tech"
    raise AssertionError("Unknown V4 document schema")


def _target_schema_enums(schema: dict) -> set[str]:
    target_schema = schema["properties"]["create"]["items"]["properties"]["targets"]
    values: set[str] = set()
    for option in target_schema.get("anyOf", []):
        values.update(option.get("items", {}).get("enum", []))
    return values


def _target_schema_allows_external_only(schema: dict) -> bool:
    target_schema = schema["properties"]["create"]["items"]["properties"]["targets"]
    return any(
        option.get("maxItems") == 1
        and option.get("items", {}).get("enum") == ["EXTERNAL"]
        for option in target_schema.get("anyOf", [])
    )


def _build_document(role: str) -> str:
    if role == "product":
        return _product_document()
    if role == "growth":
        return _growth_document()
    if role == "tech":
        return _tech_document()
    raise AssertionError(f"Unknown role: {role}")


def _product_document() -> str:
    return """## Product Problem
- Teams need a strict V4 workflow that produces inspectable dossiers.

## Initial Wedge
- Start with one project brief and one local run workspace.

## First Target User
- A product or architecture reviewer validating generated startup dossiers.

## Existing Alternatives And Switching Trigger
- Current ad hoc prompts are hard to audit when outputs drift.

## Core MVP Workflow
- Brief in, Product draft, Growth and Tech review, Product arbitration, final documents out.

## In Scope
- PRD, GTM, architecture, summaries, blackboard items, and activity log.

## Out of Scope
- Generic graph engines and distributed queues.

## MVP Build Vs Pilot Operations
- Build the deterministic local workflow and keep pilot operations manual where possible.

## Business Model Hypothesis
- The workflow creates value by making multi-agent dossier generation auditable.

## Critical Assumptions
- A strict document contract and separate JSON operation contract reduce run failures.

## How To Test Quickly
- Run the no-LLM harness and inspect generated final artifacts.

## Acceptance Criteria
- The run creates final documents with no machine protocol in public outputs.

## Risks And Failure Modes
- Invalid structured outputs must fail before blackboard persistence.

## Product Readiness
Status: READY

Blocking Gaps:
- No blocking product gap remains for this harness.

Required Improvements:
- Keep validating strict contracts before live runs.

## Product Arbitration
### Retained
- Keep Product as final arbiter.

### Deferred
- Defer generic orchestration abstractions.

### Rejected
- Reject permissive parsing as the normal path.

### Open Points
- No product open point remains for this harness.

### Rationales
- Separate structured outputs are easier to validate.

## Product Locking
### Confirmed In Scope
- Strict V4 final documents.

### Confirmed Deferred
- Provider-specific advanced retry policies.

### Confirmed Out Of Scope
- A fourth blackboard compiler agent.

### Locking Note
- Product locks the final PRD before downstream finalization."""


def _growth_document() -> str:
    return """## Go-To-Market Notes
- The initial market is internal teams that need auditable generated dossiers.

## Review Summary
- GTM viability depends on trust in deterministic contracts and readable outputs.

## Build Vs Pilot Operations
### Must Be Productized Now
- Strict output validation and clear final artifacts.

### Can Stay Manual Or Operational During Pilot
- Manual review after each live failure.

### Deferred Until After Proof
- Scaling beyond local runs.

## Critical Assumptions
- Reviewers value traceability more than flexible free-form generation.

## Requested Changes
- Keep public artifacts focused on final reader value.

## Risks
- A loose prompt contract would reintroduce output drift.

## Open Questions
- No GTM open question remains for this harness.

## Why This Could Fail Even With Good Execution
- Users may still need live examples before trusting the workflow.

## GTM Readiness
Status: READY

Blocking Gaps:
- No blocking GTM gap remains for this harness.

Required Improvements:
- Keep launch claims tied to generated evidence."""


def _tech_document() -> str:
    return """## Architecture Notes
- The workflow stays local, explicit, and file-system first.

### Mermaid Diagram
```mermaid
flowchart LR
    Brief[Project Brief] --> Product[Product]
    Product --> Growth[Growth]
    Product --> Tech[Tech]
    Growth --> Final[Final Outputs]
    Tech --> Final
```

## Review Summary
- The architecture is viable when machine contracts are separated from Markdown documents.

## Critical Assumptions
- The configured model can return JSON through the structured output path or strict fallback.

## Requested Changes
- Keep validation failures explicit and traceable.

## Risks
- Provider-specific JSON support can vary and must fail clearly.

## Open Questions
- No technical open question remains for this harness.

## Why This Could Fail Even With Good Execution
- A provider that ignores JSON-only fallback can still cause a structured failure.

## Technical Readiness
Status: READY

Blocking Gaps:
- No blocking technical gap remains for this harness.

Required Improvements:
- Keep the static harness as the first validation gate."""


def _expect_value_error(callable_obj, expected_text: str) -> None:
    try:
        callable_obj()
    except ValueError as exc:
        assert expected_text in str(exc), str(exc)
    else:
        raise AssertionError(f"Expected ValueError containing: {expected_text}")


if __name__ == "__main__":
    main()
