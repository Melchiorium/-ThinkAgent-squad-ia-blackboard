from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


DEFAULT_PROGRESS_TIMEOUT_SECONDS = 600
MAX_PROGRESS_EVENTS = 100
ALLOWED_PROGRESS_BLOCK_STATUSES = {
    "pending",
    "active",
    "done",
    "skipped",
    "failed",
}

PROGRESS_BLOCK_DEFINITIONS: list[dict[str, str]] = [
    {"id": "brief_received", "group": "Brief", "label": "Brief reçu"},
    {"id": "product_brief_analysis", "group": "Product", "label": "Analyse du brief"},
    {"id": "product_problem", "group": "Product", "label": "Problème cible"},
    {"id": "product_users_goals", "group": "Product", "label": "Utilisateurs et objectifs"},
    {"id": "product_user_stories", "group": "Product", "label": "User stories"},
    {"id": "growth_segments", "group": "Growth / GTM", "label": "Segments"},
    {"id": "growth_positioning", "group": "Growth / GTM", "label": "Positionnement"},
    {"id": "growth_channels", "group": "Growth / GTM", "label": "Canaux GTM"},
    {"id": "growth_objections", "group": "Growth / GTM", "label": "Objections et risques"},
    {"id": "tech_constraints", "group": "Tech", "label": "Contraintes"},
    {"id": "tech_components", "group": "Tech", "label": "Composants"},
    {"id": "tech_mermaid", "group": "Tech", "label": "Diagramme Mermaid"},
    {"id": "tech_risks", "group": "Tech", "label": "Risques techniques"},
    {"id": "product_revision", "group": "Finalisation", "label": "Consolidation PRD"},
    {"id": "readiness_check", "group": "Finalisation", "label": "Readiness"},
    {"id": "correction_loop", "group": "Finalisation", "label": "Correction ciblée"},
    {"id": "product_locking", "group": "Finalisation", "label": "Verrouillage produit"},
    {"id": "artifacts_persistence", "group": "Finalisation", "label": "Persistance des artefacts"},
    {"id": "done", "group": "Finalisation", "label": "Terminé"},
]

GRAPH_NODE_DEFINITIONS: list[dict[str, str]] = [
    {"id": "system", "label": "Système / Artefacts"},
    {"id": "product", "label": "Product"},
    {"id": "growth", "label": "Growth"},
    {"id": "tech", "label": "Tech"},
    {"id": "blackboard", "label": "Blackboard"},
]

GRAPH_FLOW_DEFINITIONS: list[dict[str, str]] = [
    {"id": "system_to_product", "from": "system", "to": "product", "label": "System → Product"},
    {"id": "product_to_blackboard", "from": "product", "to": "blackboard", "label": "Product → Blackboard"},
    {"id": "blackboard_to_growth", "from": "blackboard", "to": "growth", "label": "Blackboard → Growth"},
    {"id": "growth_to_blackboard", "from": "growth", "to": "blackboard", "label": "Growth → Blackboard"},
    {"id": "blackboard_to_tech", "from": "blackboard", "to": "tech", "label": "Blackboard → Tech"},
    {"id": "tech_to_blackboard", "from": "tech", "to": "blackboard", "label": "Tech → Blackboard"},
    {"id": "blackboard_to_product", "from": "blackboard", "to": "product", "label": "Blackboard → Product"},
    {"id": "blackboard_to_system", "from": "blackboard", "to": "system", "label": "Blackboard → System"},
]

_BLOCK_ORDER = {definition["id"]: index + 1 for index, definition in enumerate(PROGRESS_BLOCK_DEFINITIONS)}
_BLOCK_DEFINITION_BY_ID = {definition["id"]: definition for definition in PROGRESS_BLOCK_DEFINITIONS}
_GRAPH_FLOW_BY_ID = {definition["id"]: definition for definition in GRAPH_FLOW_DEFINITIONS}
_GRAPH_FLOW_BY_PAIR = {
    (definition["from"], definition["to"]): definition["id"] for definition in GRAPH_FLOW_DEFINITIONS
}


def build_empty_progress_state(timeout_seconds: int = DEFAULT_PROGRESS_TIMEOUT_SECONDS) -> dict:
    return {
        "progress_stage": "",
        "progress_label": "",
        "progress_detail": "",
        "progress_order": 0,
        "progress_total": 0,
        "progress_blocks": [],
        "progress_events": [],
        "progress_started_at": "",
        "progress_last_event_at": "",
        "progress_timeout_seconds": int(timeout_seconds),
        "progress_error_type": "",
        "progress_error_message": "",
    }


def build_default_progress_blocks() -> list[dict]:
    return [
        {
            "id": definition["id"],
            "group": definition["group"],
            "label": definition["label"],
            "status": "pending",
        }
        for definition in PROGRESS_BLOCK_DEFINITIONS
    ]


def normalize_progress_state(job: dict[str, Any] | None) -> dict:
    state = build_empty_progress_state()
    if not job:
        return state

    state["progress_stage"] = _clean_text(job.get("progress_stage", ""))
    state["progress_label"] = _clean_text(job.get("progress_label", ""))
    state["progress_detail"] = _clean_text(job.get("progress_detail", ""))
    state["progress_order"] = _coerce_int(job.get("progress_order", 0))
    state["progress_total"] = _coerce_int(job.get("progress_total", 0))
    state["progress_blocks"] = normalize_progress_blocks(job.get("progress_blocks", []))
    state["progress_events"] = normalize_progress_events(job.get("progress_events", []))
    state["progress_started_at"] = _clean_text(job.get("progress_started_at", ""))
    state["progress_last_event_at"] = _clean_text(job.get("progress_last_event_at", ""))
    state["progress_timeout_seconds"] = _coerce_timeout_seconds(
        job.get("progress_timeout_seconds", DEFAULT_PROGRESS_TIMEOUT_SECONDS)
    )
    state["progress_error_type"] = _clean_text(job.get("progress_error_type", ""))
    state["progress_error_message"] = _clean_text(job.get("progress_error_message", ""))

    if state["progress_blocks"] and state["progress_total"] <= 0:
        state["progress_total"] = len(state["progress_blocks"])
    if state["progress_blocks"] and state["progress_order"] <= 0:
        state["progress_order"] = _infer_progress_order(state["progress_blocks"])
    return state


def normalize_progress_blocks(blocks: Any) -> list[dict]:
    if not isinstance(blocks, list):
        return []

    normalized: list[dict] = []
    seen: set[str] = set()
    extra_blocks: list[dict] = []
    for block in blocks:
        if not isinstance(block, dict):
            continue
        block_id = _clean_text(block.get("id", ""))
        if not block_id:
            continue
        if block_id in _BLOCK_DEFINITION_BY_ID:
            definition = _BLOCK_DEFINITION_BY_ID[block_id]
            normalized.append(
                {
                    "id": block_id,
                    "group": _clean_text(block.get("group", definition["group"])) or definition["group"],
                    "label": _clean_text(block.get("label", definition["label"])) or definition["label"],
                    "status": _normalize_block_status(block.get("status", "pending")),
                }
            )
            seen.add(block_id)
        else:
            extra_blocks.append(
                {
                    "id": block_id,
                    "group": _clean_text(block.get("group", "Other")) or "Other",
                    "label": _clean_text(block.get("label", block_id)) or block_id,
                    "status": _normalize_block_status(block.get("status", "pending")),
                }
            )

    for definition in PROGRESS_BLOCK_DEFINITIONS:
        block_id = definition["id"]
        if block_id in seen:
            continue
        normalized.append(
            {
                "id": block_id,
                "group": definition["group"],
                "label": definition["label"],
                "status": "pending",
            }
        )
    normalized.extend(extra_blocks)
    return normalized


def normalize_progress_events(events: Any) -> list[dict]:
    if not isinstance(events, list):
        return []

    normalized: list[dict] = []
    for event in events[-MAX_PROGRESS_EVENTS:]:
        if not isinstance(event, dict):
            continue
        normalized.append(_clean_event_payload(event))
    return normalized[-MAX_PROGRESS_EVENTS:]


def build_progress_graph(job: dict | None) -> dict:
    state = normalize_progress_state(job or {})
    job_status = _clean_text((job or {}).get("status", ""))
    nodes = [
        {
            "id": definition["id"],
            "label": definition["label"],
            "status": "idle",
        }
        for definition in GRAPH_NODE_DEFINITIONS
    ]
    flows = [
        {
            "id": definition["id"],
            "from": definition["from"],
            "to": definition["to"],
            "label": definition["label"],
            "status": "idle",
        }
        for definition in GRAPH_FLOW_DEFINITIONS
    ]
    node_map = {node["id"]: node for node in nodes}
    flow_map = {flow["id"]: flow for flow in flows}
    seen_nodes: set[str] = set()
    seen_flows: set[str] = set()

    active_event = _find_latest_exchange_event(state["progress_events"])
    for event in state["progress_events"]:
        actor = _clean_text(event.get("actor", ""))
        target = _clean_text(event.get("target", ""))
        flow_id = _resolve_flow_id(actor, target, event.get("flow", ""))
        if actor in node_map:
            seen_nodes.add(actor)
        if target in node_map:
            seen_nodes.add(target)
        if flow_id in flow_map:
            seen_flows.add(flow_id)

    for node_id in seen_nodes:
        node_map[node_id]["status"] = "done"
    for flow_id in seen_flows:
        flow_map[flow_id]["status"] = "done"

    active_actor = ""
    active_target = ""
    active_flow = ""
    current_task = state["progress_label"] or state["progress_stage"]
    loop_value = None

    if active_event is not None:
        active_actor = _clean_text(active_event.get("actor", ""))
        active_target = _clean_text(active_event.get("target", ""))
        active_flow = _resolve_flow_id(active_actor, active_target, active_event.get("flow", ""))
        current_task = _clean_text(active_event.get("task", "")) or current_task
        loop_value = _coerce_positive_int(active_event.get("loop"))

        if active_actor in node_map:
            node_map[active_actor]["status"] = "active" if job_status != "failed" else "failed"
        if active_target in node_map:
            node_map[active_target]["status"] = "active" if job_status != "failed" else "failed"
        if active_flow in flow_map:
            flow_map[active_flow]["status"] = "active" if job_status != "failed" else "failed"

        if job_status == "done":
            if active_actor in node_map:
                node_map[active_actor]["status"] = "done"
            if active_target in node_map:
                node_map[active_target]["status"] = "done"
            if active_flow in flow_map:
                flow_map[active_flow]["status"] = "done"

    if job_status == "failed" and active_event is None:
        current_task = state["progress_label"] or state["progress_stage"] or "Échec"

    return {
        "nodes": nodes,
        "flows": flows,
        "active_actor": active_actor,
        "active_target": active_target,
        "active_flow": active_flow,
        "current_task": current_task,
        "loop": loop_value,
    }


def build_progress_event(
    *,
    stage: str,
    label: str,
    detail: str = "",
    timestamp: str | None = None,
    kind: str = "event",
) -> dict:
    event = {
        "timestamp": timestamp or _utc_now(),
        "stage": _clean_text(stage),
        "label": _clean_text(label),
        "detail": _clean_text(detail),
    }
    if kind:
        event["kind"] = _clean_text(kind)
    return event


def build_agent_exchange_event(
    *,
    stage: str,
    label: str,
    detail: str = "",
    actor: str = "",
    target: str = "",
    flow: str = "",
    task: str = "",
    loop: int | None = None,
    timestamp: str | None = None,
    kind: str = "agent_exchange",
) -> dict:
    event = build_progress_event(
        stage=stage,
        label=label,
        detail=detail,
        timestamp=timestamp,
        kind=kind,
    )
    actor = _clean_text(actor)
    target = _clean_text(target)
    flow = _clean_text(flow)
    task = _clean_text(task)
    if actor:
        event["actor"] = actor
    if target:
        event["target"] = target
    if flow:
        event["flow"] = flow
    if task:
        event["task"] = task
    loop_value = _coerce_positive_int(loop)
    if loop_value is not None:
        event["loop"] = loop_value
    return event


def apply_progress_update(
    job: dict[str, Any] | None,
    *,
    stage: str,
    label: str,
    detail: str = "",
    active_blocks: list[str] | tuple[str, ...] | None = None,
    done_blocks: list[str] | tuple[str, ...] | None = None,
    skipped_blocks: list[str] | tuple[str, ...] | None = None,
    failed_blocks: list[str] | tuple[str, ...] | None = None,
    event: dict[str, Any] | None = None,
    kind: str = "event",
    set_started: bool = False,
    timeout_seconds: int | None = None,
    error_type: str = "",
    error_message: str = "",
) -> dict:
    state = normalize_progress_state(job or {})
    blocks = state["progress_blocks"] or build_default_progress_blocks()
    block_map = {block["id"]: dict(block) for block in blocks}

    for block_id in _iter_block_ids(done_blocks):
        _set_block_status(block_map, block_id, "done")
    for block_id in _iter_block_ids(skipped_blocks):
        _set_block_status(block_map, block_id, "skipped")
    for block_id in _iter_block_ids(failed_blocks):
        _set_block_status(block_map, block_id, "failed")
    for block_id in _iter_block_ids(active_blocks):
        if block_map.get(block_id, {}).get("status") != "failed":
            _set_block_status(block_map, block_id, "active")

    state["progress_blocks"] = _blocks_in_definition_order(block_map)
    state["progress_total"] = len(state["progress_blocks"])
    state["progress_stage"] = _clean_text(stage)
    state["progress_label"] = _clean_text(label)
    state["progress_detail"] = _clean_text(detail)
    state["progress_order"] = _progress_order_from_blocks(state["progress_blocks"], active_blocks, done_blocks, failed_blocks)

    event_payload = event or build_progress_event(stage=stage, label=label, detail=detail, kind=kind)
    if event_payload:
        state["progress_events"].append(_clean_event_payload(event_payload))
        state["progress_events"] = state["progress_events"][-MAX_PROGRESS_EVENTS:]
        state["progress_last_event_at"] = _clean_text(event_payload.get("timestamp", ""))
        if not state["progress_started_at"] or set_started:
            state["progress_started_at"] = state["progress_last_event_at"]

    if timeout_seconds is not None:
        state["progress_timeout_seconds"] = _coerce_timeout_seconds(timeout_seconds)

    if error_type:
        state["progress_error_type"] = _clean_text(error_type)
    if error_message:
        state["progress_error_message"] = _clean_text(error_message)

    if set_started and not state["progress_started_at"]:
        state["progress_started_at"] = _utc_now()
    return state


def progress_block_labels(blocks: list[dict] | None) -> dict[str, str]:
    labels: dict[str, str] = {}
    for block in blocks or []:
        if not isinstance(block, dict):
            continue
        block_id = _clean_text(block.get("id", ""))
        if not block_id:
            continue
        labels[block_id] = _clean_text(block.get("label", block_id)) or block_id
    return labels


def _blocks_in_definition_order(block_map: dict[str, dict]) -> list[dict]:
    ordered_blocks = []
    for definition in PROGRESS_BLOCK_DEFINITIONS:
        block_id = definition["id"]
        block = block_map.get(block_id)
        if block is None:
            block = {
                "id": block_id,
                "group": definition["group"],
                "label": definition["label"],
                "status": "pending",
            }
        ordered_blocks.append(block)
    for block_id, block in block_map.items():
        if block_id in _BLOCK_DEFINITION_BY_ID:
            continue
        ordered_blocks.append(block)
    return ordered_blocks


def _set_block_status(block_map: dict[str, dict], block_id: str, status: str) -> None:
    if block_id not in block_map:
        definition = _BLOCK_DEFINITION_BY_ID.get(block_id)
        if definition is None:
            return
        block_map[block_id] = {
            "id": definition["id"],
            "group": definition["group"],
            "label": definition["label"],
            "status": "pending",
        }
    block_map[block_id]["status"] = _normalize_block_status(status)


def _iter_block_ids(values: list[str] | tuple[str, ...] | None) -> list[str]:
    if not values:
        return []
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        block_id = _clean_text(value)
        if not block_id or block_id in seen:
            continue
        seen.add(block_id)
        ordered.append(block_id)
    return ordered


def _progress_order_from_blocks(
    blocks: list[dict],
    active_blocks: list[str] | tuple[str, ...] | None,
    done_blocks: list[str] | tuple[str, ...] | None,
    failed_blocks: list[str] | tuple[str, ...] | None,
) -> int:
    return _infer_progress_order(blocks)


def _infer_progress_order(blocks: list[dict]) -> int:
    return sum(1 for block in blocks if block.get("status") != "pending")


def _clean_event_payload(event: dict[str, Any]) -> dict:
    cleaned = dict(event)
    cleaned["timestamp"] = _clean_text(cleaned.get("timestamp", ""))
    cleaned["stage"] = _clean_text(cleaned.get("stage", ""))
    cleaned["label"] = _clean_text(cleaned.get("label", ""))
    cleaned["detail"] = _clean_text(cleaned.get("detail", ""))
    for key in ("actor", "target", "flow", "task"):
        if key not in cleaned:
            continue
        value = _clean_text(cleaned.get(key, ""))
        if value:
            cleaned[key] = value
        else:
            cleaned.pop(key, None)
    if "loop" in cleaned:
        loop_value = _coerce_positive_int(cleaned.get("loop"))
        if loop_value is None:
            cleaned.pop("loop", None)
        else:
            cleaned["loop"] = loop_value
    if "kind" in cleaned:
        kind_value = _clean_text(cleaned.get("kind", ""))
        if kind_value:
            cleaned["kind"] = kind_value
        else:
            cleaned.pop("kind", None)
    return cleaned


def _normalize_block_status(status: Any) -> str:
    value = _clean_text(status)
    if value in ALLOWED_PROGRESS_BLOCK_STATUSES:
        return value
    return "pending"


def _coerce_timeout_seconds(value: Any) -> int:
    try:
        timeout = int(value)
    except (TypeError, ValueError):
        timeout = DEFAULT_PROGRESS_TIMEOUT_SECONDS
    return timeout if timeout > 0 else DEFAULT_PROGRESS_TIMEOUT_SECONDS


def _coerce_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _coerce_positive_int(value: Any) -> int | None:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None
    if number <= 0:
        return None
    return number


def _resolve_flow_id(actor: str, target: str, flow: Any) -> str:
    cleaned_flow = _clean_text(flow)
    if cleaned_flow in _GRAPH_FLOW_BY_ID:
        return cleaned_flow
    if actor and target:
        return _GRAPH_FLOW_BY_PAIR.get((actor, target), "")
    return ""


def _find_latest_exchange_event(events: list[dict]) -> dict | None:
    for event in reversed(events):
        if _clean_text(event.get("actor", "")) or _clean_text(event.get("target", "")) or _clean_text(event.get("flow", "")):
            return event
    return None


def _clean_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
