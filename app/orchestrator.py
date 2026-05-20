import json
import os
import re
from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path

if __package__ and __package__.startswith("app"):
    from .blackboard import create_blackboard
    from .agents.product_agent import (
        run_product_agent,
        run_product_locking_pass,
        run_product_revision,
        run_product_second_pass_initial,
    )
    from .agents.tech_agent import run_tech_agent
    from .agents.growth_agent import run_growth_agent
    from .blackboard_items import create_item, list_items, list_open_items, update_item_status
    from .llm import call_llm_json
    from .run_documents import write_document
    from .run_store import append_activity_log_entry, create_run_workspace, write_text_file
    from .run_summaries import generate_summary
    from .readiness import aggregate_global_readiness
    from .v4_parsing import (
        build_v4_document_schema,
        parse_v4_agent_response,
        parse_v4_blackboard_operations,
        parse_v4_structured_document,
        validate_v4_document,
        validate_v4_item_operations,
    )
    from .web_progress import build_agent_exchange_event
else:
    from blackboard import create_blackboard
    from agents.product_agent import (
        run_product_agent,
        run_product_locking_pass,
        run_product_revision,
        run_product_second_pass_initial,
    )
    from agents.tech_agent import run_tech_agent
    from agents.growth_agent import run_growth_agent
    from blackboard_items import create_item, list_items, list_open_items, update_item_status
    from llm import call_llm_json
    from run_documents import write_document
    from run_store import append_activity_log_entry, create_run_workspace, write_text_file
    from run_summaries import generate_summary
    from readiness import aggregate_global_readiness
    from v4_parsing import (
        build_v4_document_schema,
        parse_v4_agent_response,
        parse_v4_blackboard_operations,
        parse_v4_structured_document,
        validate_v4_document,
        validate_v4_item_operations,
    )
    from web_progress import build_agent_exchange_event


def run_v0_flow(
    project_brief: str,
    project_brief_source: str,
    progress_callback=None,
    step_timeout_seconds: int | None = None,
) -> dict:
    """Run the staged collaboration flow and return the updated blackboard."""
    blackboard = create_blackboard(project_brief, project_brief_source)
    _emit_agent_exchange(
        progress_callback,
        stage="product_initial",
        label="Brief transmis à Product",
        detail="Le brief est remis à Product pour cadrer le MVP.",
        actor="system",
        target="product",
        flow="system_to_product",
        task="Analyse du brief",
    )
    blackboard = _run_stage(
        blackboard,
        progress_callback,
        step_timeout_seconds,
        stage="product_initial",
        label="Product structure le PRD initial",
        detail="Analyse du brief, problème cible, utilisateurs et objectifs MVP.",
        active_blocks=[
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
        ],
        done_blocks=["brief_received"],
        runner=lambda current_blackboard: run_product_agent(current_blackboard),
        timeout_message="Product initial a dépassé 10 minutes.",
        success_label="Product a terminé le cadrage initial",
        success_detail="Le PRD initial est prêt pour Growth.",
        success_done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
        ],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="product_initial",
        label="PRD initial écrit",
        detail="Product a écrit le premier PRD dans le blackboard.",
        actor="product",
        target="blackboard",
        flow="product_to_blackboard",
        task="PRD initial",
    )
    _emit_agent_exchange(
        progress_callback,
        stage="growth_review",
        label="PRD transmis à Growth",
        detail="Growth lit le PRD initial avant de proposer le GTM.",
        actor="blackboard",
        target="growth",
        flow="blackboard_to_growth",
        task="Relecture GTM",
    )
    blackboard = _run_stage(
        blackboard,
        progress_callback,
        step_timeout_seconds,
        stage="growth_review",
        label="Growth travaille le GTM initial",
        detail="Analyse des segments, du positionnement, des canaux et des objections.",
        active_blocks=[
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
        ],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
        ],
        runner=lambda current_blackboard: run_growth_agent(current_blackboard),
        timeout_message="Growth a dépassé 10 minutes.",
        success_label="Growth a terminé le GTM initial",
        success_detail="Les signaux marché ont été arbitréés pour le PRD.",
        success_done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
        ],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="growth_review",
        label="GTM écrit",
        detail="Growth a écrit les signaux marché dans le blackboard.",
        actor="growth",
        target="blackboard",
        flow="growth_to_blackboard",
        task="GTM initial",
    )
    _emit_agent_exchange(
        progress_callback,
        stage="tech_review",
        label="PRD transmis à Tech",
        detail="Tech lit le PRD avant de produire l'architecture.",
        actor="blackboard",
        target="tech",
        flow="blackboard_to_tech",
        task="Relecture architecture",
    )
    blackboard = _run_stage(
        blackboard,
        progress_callback,
        step_timeout_seconds,
        stage="tech_review",
        label="Tech prépare l'architecture initiale",
        detail="Analyse des contraintes, composants, diagramme Mermaid et risques.",
        active_blocks=[
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
        ],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
        ],
        runner=lambda current_blackboard: run_tech_agent(current_blackboard),
        timeout_message="Tech a dépassé 10 minutes.",
        success_label="Tech a terminé l'architecture initiale",
        success_detail="Les contraintes techniques et le diagramme sont prêts.",
        success_done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
        ],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="tech_review",
        label="Architecture écrite",
        detail="Tech a écrit l'architecture dans le blackboard.",
        actor="tech",
        target="blackboard",
        flow="tech_to_blackboard",
        task="Architecture initiale",
    )
    _emit_agent_exchange(
        progress_callback,
        stage="product_revision",
        label="Product consolide les retours",
        detail="Product reprend les retours Growth et Tech.",
        actor="blackboard",
        target="product",
        flow="blackboard_to_product",
        task="Consolidation PRD",
    )
    blackboard = _run_stage(
        blackboard,
        progress_callback,
        step_timeout_seconds,
        stage="product_revision",
        label="Product consolide le PRD",
        detail="Arbitrage final entre les retours Growth et Tech.",
        active_blocks=["product_revision"],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
        ],
        runner=lambda current_blackboard: run_product_revision(current_blackboard),
        timeout_message="Product revision a dépassé 10 minutes.",
        success_label="Product a consolidé le PRD",
        success_detail="Le PRD est prêt pour la vérification readiness.",
        success_done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
            "product_revision",
        ],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="product_revision",
        label="PRD révisé écrit",
        detail="Product a écrit la version consolidée du PRD.",
        actor="product",
        target="blackboard",
        flow="product_to_blackboard",
        task="PRD révisé",
    )
    blackboard = _finalize_readiness(blackboard)
    _emit_progress(
        progress_callback,
        stage="readiness_check",
        label="Vérification readiness",
        detail=f"Statut global: {blackboard['readiness'].get('global_status') or 'inconnu'}.",
        active_blocks=["readiness_check"],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
            "product_revision",
        ],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="readiness_check",
        label="Readiness vérifiée",
        detail=f"Statut global: {blackboard['readiness'].get('global_status') or 'inconnu'}.",
        actor="blackboard",
        target="system",
        flow="blackboard_to_system",
        task="Readiness",
    )
    blackboard = _run_targeted_correction_loop(
        blackboard,
        progress_callback=progress_callback,
        step_timeout_seconds=step_timeout_seconds,
    )
    _emit_progress(
        progress_callback,
        stage="correction_loop",
        label="Boucle de correction ciblée",
        detail=(
            "Boucle déclenchée."
            if blackboard["readiness"].get("loop_triggered")
            else "Aucune boucle de correction nécessaire."
        ),
        done_blocks=["correction_loop"],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="product_locking",
        label="Product verrouille la version finale",
        detail="Product verrouille la version finale avant la persistance.",
        actor="blackboard",
        target="product",
        flow="blackboard_to_product",
        task="Verrouillage produit",
    )
    blackboard = _run_stage(
        blackboard,
        progress_callback,
        step_timeout_seconds,
        stage="product_locking",
        label="Product verrouille la version finale",
        detail="Verrouillage du scope MVP avant la persistance des artefacts.",
        active_blocks=["product_locking"],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
            "product_revision",
            "readiness_check",
            "correction_loop",
        ],
        runner=lambda current_blackboard: run_product_locking_pass(current_blackboard),
        timeout_message="Product locking a dépassé 10 minutes.",
        success_label="Product a verrouillé la version finale",
        success_detail="La version finale du PRD est figée.",
        success_done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
            "product_revision",
            "readiness_check",
            "correction_loop",
            "product_locking",
        ],
    )
    _emit_agent_exchange(
        progress_callback,
        stage="product_locking",
        label="PRD final verrouillé",
        detail="Product a figé la version finale dans le blackboard.",
        actor="product",
        target="blackboard",
        flow="product_to_blackboard",
        task="PRD final verrouillé",
    )
    blackboard = _finalize_readiness(blackboard)
    _emit_agent_exchange(
        progress_callback,
        stage="readiness_check",
        label="Artefacts prêts à persister",
        detail="Le run est prêt à persister ses artefacts.",
        actor="blackboard",
        target="system",
        flow="blackboard_to_system",
        task="Persistance des artefacts",
    )
    _emit_progress(
        progress_callback,
        stage="readiness_check",
        label="Vérification readiness finale",
        detail=f"Statut global: {blackboard['readiness'].get('global_status') or 'inconnu'}.",
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
            "product_revision",
            "readiness_check",
            "correction_loop",
            "product_locking",
        ],
    )
    return blackboard


def run_v2_flow(version_dir: Path, evaluation_text: str) -> dict:
    """Run the second-pass revision flow from a versioned source bundle."""
    source_project_brief = _read_text(version_dir / "project-brief.md")
    source_prd = _read_text(version_dir / "prd.md")
    source_architecture = _read_text(version_dir / "architecture.md")
    source_gtm = _read_text(version_dir / "gtm.md")
    source_blackboard = _read_text(version_dir / "blackboard.md")
    source_activity_log = _read_text(version_dir / "activity_log.txt")

    blackboard = create_blackboard(
        project_brief=source_project_brief,
        project_brief_source=str(version_dir / "project-brief.md"),
        source_version=version_dir.name,
        source_artifacts={
            "project_brief": source_project_brief,
            "prd": source_prd,
            "architecture": source_architecture,
            "gtm": source_gtm,
            "blackboard": source_blackboard,
            "activity_log": source_activity_log,
        },
        executive_evaluation=evaluation_text,
    )
    blackboard["workflow_stage"] = "second_pass_initial"
    blackboard["prd_draft_initial"] = source_prd
    blackboard["second_pass_trace"]["initial_revision_draft"] = source_prd
    blackboard["revision_trace"]["initial_prd_draft"] = source_prd

    blackboard = run_product_second_pass_initial(blackboard)
    blackboard = run_growth_agent(blackboard)
    blackboard = run_tech_agent(blackboard)
    blackboard = run_product_revision(blackboard)
    blackboard = _finalize_readiness(blackboard)
    blackboard = _run_targeted_correction_loop(blackboard)
    blackboard = run_product_locking_pass(blackboard)
    blackboard = _finalize_readiness(blackboard)
    return blackboard


def _read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Missing source file for second pass: {path}")
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        raise ValueError(f"Source file is empty for second pass: {path}")
    return content


def _finalize_readiness(blackboard: dict) -> dict:
    readiness = blackboard["readiness"]
    readiness["global"] = aggregate_global_readiness(readiness)
    readiness["global_status"] = readiness["global"]["status"]
    readiness["known_tags"] = readiness["global"].get("known_tags", readiness.get("known_tags", []))
    return blackboard


def _run_targeted_correction_loop(
    blackboard: dict,
    progress_callback=None,
    step_timeout_seconds: int | None = None,
) -> dict:
    readiness = blackboard["readiness"]
    readiness["loop_triggered"] = readiness["global_status"] == "LIMITED"
    readiness["final_outcome"] = readiness["global_status"]

    if readiness["global_status"] != "LIMITED":
        return blackboard

    _emit_progress(
        progress_callback,
        stage="correction_loop",
        label="Boucle de correction ciblée",
        detail="La readiness globale nécessite des corrections ciblées.",
        active_blocks=["correction_loop"],
    )

    while readiness["loop_count"] < readiness["max_loops"]:
        correction_tasks = _build_correction_plan(blackboard)
        if not correction_tasks:
            break

        loop_number = readiness["loop_count"] + 1
        readiness["correction_tasks"].extend(
            {
                "loop": loop_number,
                **task,
            }
            for task in correction_tasks
        )
        readiness["history"].append(
            _snapshot_readiness(blackboard, loop_number, "before", correction_tasks)
        )

        tasks_by_owner = _group_correction_tasks_by_owner(correction_tasks)
        _record_workflow_checkpoint(
            blackboard,
            stage=f"correction_loop_{loop_number}_input",
            note="Correction loop triggered by the current readiness gaps.",
            correction_tasks=correction_tasks,
            tasks_by_owner=tasks_by_owner,
        )

        if tasks_by_owner["tech"]:
            _emit_agent_exchange(
                progress_callback,
                stage=f"correction_loop_{loop_number}_tech",
                label="Correction ciblée Tech",
                detail=f"{len(tasks_by_owner['tech'])} tâche(s) tech à traiter.",
                actor="blackboard",
                target="tech",
                flow="blackboard_to_tech",
                task="Correction ciblée Tech",
                loop=loop_number,
            )
            blackboard = _run_stage(
                blackboard,
                progress_callback,
                step_timeout_seconds,
                stage=f"correction_loop_{loop_number}_tech",
                label="Tech applique les corrections ciblées",
                detail=f"{len(tasks_by_owner['tech'])} tâche(s) tech à traiter.",
                active_blocks=["correction_loop", "tech_constraints", "tech_components", "tech_mermaid", "tech_risks"],
                done_blocks=["readiness_check"],
                runner=lambda current_blackboard: run_tech_agent(
                    current_blackboard, tasks_by_owner["tech"]
                ),
                timeout_message="Tech a dépassé 10 minutes pendant la boucle de correction.",
                success_label="Tech a appliqué les corrections ciblées",
                success_detail="Les corrections tech ciblées sont intégrées.",
                success_done_blocks=[
                    "tech_constraints",
                    "tech_components",
                    "tech_mermaid",
                    "tech_risks",
                ],
            )
            _emit_agent_exchange(
                progress_callback,
                stage=f"correction_loop_{loop_number}_tech",
                label="Architecture corrigée",
                detail="Tech a réécrit les éléments techniques dans le blackboard.",
                actor="tech",
                target="blackboard",
                flow="tech_to_blackboard",
                task="Architecture corrigée",
                loop=loop_number,
            )
        if tasks_by_owner["growth"]:
            _emit_agent_exchange(
                progress_callback,
                stage=f"correction_loop_{loop_number}_growth",
                label="Relecture GTM",
                detail=f"{len(tasks_by_owner['growth'])} tâche(s) growth à traiter.",
                actor="blackboard",
                target="growth",
                flow="blackboard_to_growth",
                task="Relecture GTM",
                loop=loop_number,
            )
            blackboard = _run_stage(
                blackboard,
                progress_callback,
                step_timeout_seconds,
                stage=f"correction_loop_{loop_number}_growth",
                label="Growth applique les corrections ciblées",
                detail=f"{len(tasks_by_owner['growth'])} tâche(s) growth à traiter.",
                active_blocks=["correction_loop", "growth_segments", "growth_positioning", "growth_channels", "growth_objections"],
                done_blocks=["readiness_check"],
                runner=lambda current_blackboard: run_growth_agent(
                    current_blackboard, tasks_by_owner["growth"]
                ),
                timeout_message="Growth a dépassé 10 minutes pendant la boucle de correction.",
                success_label="Growth a appliqué les corrections ciblées",
                success_detail="Les corrections growth ciblées sont intégrées.",
                success_done_blocks=[
                    "growth_segments",
                    "growth_positioning",
                    "growth_channels",
                    "growth_objections",
                ],
            )
            _emit_agent_exchange(
                progress_callback,
                stage=f"correction_loop_{loop_number}_growth",
                label="GTM corrigé",
                detail="Growth a réécrit les éléments marché dans le blackboard.",
                actor="growth",
                target="blackboard",
                flow="growth_to_blackboard",
                task="GTM corrigé",
                loop=loop_number,
            )
        if correction_tasks:
            _emit_agent_exchange(
                progress_callback,
                stage=f"correction_loop_{loop_number}_product",
                label="Correction ciblée Product",
                detail=f"{len(tasks_by_owner['product'])} tâche(s) product à traiter.",
                actor="blackboard",
                target="product",
                flow="blackboard_to_product",
                task="Correction ciblée Product",
                loop=loop_number,
            )
            blackboard = _run_stage(
                blackboard,
                progress_callback,
                step_timeout_seconds,
                stage=f"correction_loop_{loop_number}_product",
                label="Product arbitre les corrections ciblées",
                detail=f"{len(tasks_by_owner['product'])} tâche(s) product à traiter.",
                active_blocks=["correction_loop", "product_revision"],
                done_blocks=["readiness_check"],
                runner=lambda current_blackboard: run_product_revision(
                    current_blackboard, tasks_by_owner["product"]
                ),
                timeout_message="Product revision a dépassé 10 minutes pendant la boucle de correction.",
                success_label="Product a arbitré les corrections ciblées",
                success_detail="La boucle de correction produit est intégrée.",
                success_done_blocks=["product_revision"],
            )
            _emit_agent_exchange(
                progress_callback,
                stage=f"correction_loop_{loop_number}_product",
                label="PRD corrigé",
                detail="Product a réécrit les éléments produits dans le blackboard.",
                actor="product",
                target="blackboard",
                flow="product_to_blackboard",
                task="PRD corrigé",
                loop=loop_number,
            )

        blackboard = _finalize_readiness(blackboard)
        readiness = blackboard["readiness"]
        readiness["loop_count"] += 1
        readiness["history"].append(
            _snapshot_readiness(blackboard, loop_number, "after", correction_tasks)
        )
        readiness["final_outcome"] = readiness["global_status"]

        if readiness["global_status"] in {"READY", "INSUFFICIENT"}:
            break

    readiness["final_outcome"] = readiness["global_status"]
    return blackboard


def _run_stage(
    blackboard: dict,
    progress_callback,
    step_timeout_seconds: int | None,
    *,
    stage: str,
    label: str,
    detail: str,
    active_blocks: list[str] | None,
    done_blocks: list[str] | None,
    runner,
    timeout_message: str,
    success_label: str | None = None,
    success_detail: str | None = None,
    success_active_blocks: list[str] | None = None,
    success_done_blocks: list[str] | None = None,
) -> dict:
    _emit_progress(
        progress_callback,
        stage=stage,
        label=label,
        detail=detail,
        active_blocks=active_blocks,
        done_blocks=done_blocks,
    )
    result = _run_agent_step_with_timeout(
        runner,
        blackboard,
        timeout_seconds=step_timeout_seconds,
        timeout_message=timeout_message,
    )
    _emit_progress(
        progress_callback,
        stage=stage,
        label=success_label or label,
        detail=success_detail or detail,
        active_blocks=success_active_blocks,
        done_blocks=success_done_blocks,
    )
    return result


def _run_agent_step_with_timeout(
    runner,
    blackboard: dict,
    *,
    timeout_seconds: int | None,
    timeout_message: str,
):
    # WEB_AGENT_STEP_TIMEOUT_SECONDS is a stale-step alert threshold in the web UI.
    # Run the agent inline so the generation lock stays held until the step returns.
    return runner(blackboard)


def _emit_progress(
    progress_callback,
    *,
    stage: str,
    label: str,
    detail: str = "",
    active_blocks: list[str] | None = None,
    done_blocks: list[str] | None = None,
    skipped_blocks: list[str] | None = None,
    failed_blocks: list[str] | None = None,
    event: dict | None = None,
) -> None:
    if progress_callback is None:
        return
    progress_callback(
        stage=stage,
        label=label,
        detail=detail,
        active_blocks=active_blocks or [],
        done_blocks=done_blocks or [],
        skipped_blocks=skipped_blocks or [],
        failed_blocks=failed_blocks or [],
        event=event,
    )


def _emit_agent_exchange(
    progress_callback,
    *,
    stage: str,
    label: str,
    detail: str = "",
    actor: str = "",
    target: str = "",
    flow: str = "",
    task: str = "",
    loop: int | None = None,
) -> None:
    _emit_progress(
        progress_callback,
        stage=stage,
        label=label,
        detail=detail,
        event=build_agent_exchange_event(
            stage=stage,
            label=label,
            detail=detail,
            actor=actor,
            target=target,
            flow=flow,
            task=task,
            loop=loop,
        ),
    )


def _build_correction_plan(blackboard: dict) -> list[dict]:
    readiness = blackboard["readiness"]
    raw_gaps = _collect_readiness_gaps(readiness)
    normalized_gaps = _dedupe_and_rank_gaps(raw_gaps)
    priority_gaps = normalized_gaps[:3]
    correction_tasks = []

    for gap in priority_gaps:
        owner = _assign_correction_owner(gap["theme_key"], gap["source_role"])
        correction_tasks.append(
            {
                "owner": owner,
                "task": _build_actionable_task(owner, gap["theme_key"], gap["text"]),
                "source_gap": _format_tagged_gap(gap),
                "expected_output": _build_expected_output(owner, gap["theme_key"]),
                "contributors": _build_contributors(owner, gap["source_roles"]),
                "tag": gap.get("tag", gap["theme_key"]),
            }
        )

    return correction_tasks


def _record_workflow_checkpoint(
    blackboard: dict,
    stage: str,
    note: str = "",
    correction_tasks: list[dict] | None = None,
    tasks_by_owner: dict[str, list[dict]] | None = None,
) -> None:
    checkpoints = blackboard.setdefault("workflow_trace", {}).setdefault("checkpoints", [])
    tasks_by_owner = tasks_by_owner or {}
    checkpoint = {
        "stage": stage,
        "note": note,
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
        "tasks_by_owner": {
            owner: len(tasks)
            for owner, tasks in tasks_by_owner.items()
        },
    }
    checkpoints.append(checkpoint)


def _collect_readiness_gaps(readiness: dict) -> list[dict]:
    items = []
    for role in ("product", "tech", "growth"):
        readiness_block = readiness.get(role, {})
        for gap in readiness_block.get("blocking_gaps", []):
            items.append(
                {
                    "source_role": role,
                    "kind": "blocking_gap",
                    "tag": gap.get("tag", "untagged") if isinstance(gap, dict) else "untagged",
                    "text": gap.get("text", "") if isinstance(gap, dict) else str(gap),
                }
            )
        for improvement in readiness_block.get("required_improvements", []):
            items.append(
                {
                    "source_role": role,
                    "kind": "required_improvement",
                    "tag": improvement.get("tag", "untagged") if isinstance(improvement, dict) else "untagged",
                    "text": improvement.get("text", "") if isinstance(improvement, dict) else str(improvement),
                }
            )
    return [item for item in items if item["text"]]


def _dedupe_and_rank_gaps(gaps: list[dict]) -> list[dict]:
    grouped: dict[str, dict] = {}
    for item in gaps:
        normalized = _normalize_gap_text(item["text"])
        theme_key = _normalize_gap_tag(item.get("tag", "")) or _classify_gap_theme(normalized)
        bucket = grouped.setdefault(
            theme_key,
            {
                "theme_key": theme_key,
                "source_roles": [],
                "texts": [],
                "tags": [],
                "priority": _theme_priority(theme_key),
            },
        )
        if item["source_role"] not in bucket["source_roles"]:
            bucket["source_roles"].append(item["source_role"])
        if item["text"] not in bucket["texts"]:
            bucket["texts"].append(item["text"])
        tag = _normalize_gap_tag(item.get("tag", ""))
        if tag and tag not in bucket["tags"]:
            bucket["tags"].append(tag)

    ranked = []
    for bucket in grouped.values():
        source_roles = bucket["source_roles"]
        primary_tag = bucket["tags"][0] if bucket["tags"] else bucket["theme_key"]
        ranked.append(
            {
                "theme_key": bucket["theme_key"],
                "tag": primary_tag,
                "source_role": source_roles[0] if source_roles else "product",
                "source_roles": source_roles,
                "text": bucket["texts"][0] if bucket["texts"] else "",
                "merged_text": " ".join(bucket["texts"]),
                "priority": bucket["priority"],
            }
        )

    ranked.sort(key=lambda item: (item["priority"], item["source_role"], item["text"]))
    return ranked


def _normalize_gap_text(text: str) -> str:
    normalized = text.lower().strip()
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def _normalize_gap_tag(value: str) -> str:
    normalized = value.lower().strip()
    normalized = re.sub(r"[^a-z0-9_]+", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized


def _classify_gap_theme(normalized_gap: str) -> str:
    theme_keywords = [
        ("legal_compliance", ("legal", "compliance", "regulatory", "privacy", "permission", "data protection", "trust")),
        ("adoption_validation", ("willingness", "adopt", "engagement", "traction", "interest", "users")),
        ("quality_assurance", ("quality", "vetting", "moderation", "submission", "project quality", "abuse")),
        ("market_motion", ("acquisition", "market", "bottleneck", "pilot", "activation", "repeatability", "supply", "demand")),
        ("metrics_validation", ("metric", "metrics", "success", "measurement", "kpi", "engagement metrics")),
        ("onboarding", ("onboarding", "usability", "digital literacy", "training", "education")),
        ("scope", ("scope", "wedge", "segment", "mvp", "business model", "recommendation")),
    ]
    for theme_key, keywords in theme_keywords:
        if any(keyword in normalized_gap for keyword in keywords):
            return theme_key
    return "general"


def _theme_priority(theme_key: str) -> int:
    priorities = {
        "legal_compliance": 0,
        "adoption_validation": 1,
        "quality_assurance": 2,
        "market_motion": 3,
        "metrics_validation": 4,
        "onboarding": 5,
        "scope": 6,
        "general": 7,
    }
    return priorities.get(theme_key, 7)


def _assign_correction_owner(theme_key: str, source_role: str) -> str:
    if theme_key in {"legal_compliance", "quality_assurance", "compliance", "privacy_trust", "data_access"}:
        return "tech"
    if theme_key in {"adoption_validation", "market_motion", "demand_validation"}:
        return "growth"
    if theme_key in {"metrics_validation", "onboarding", "scope", "operations"}:
        return "product"
    return source_role


def _build_actionable_task(owner: str, theme_key: str, source_gap: str) -> str:
    templates = {
        "tech": {
            "legal_compliance": "Define the smallest legal, compliance, and permissions baseline required before launch.",
            "privacy_trust": "Define the smallest privacy and trust control needed before launch.",
            "data_access": "Clarify the minimum access, storage, and permission model needed for MVP data flows.",
            "quality_assurance": "Clarify the smallest quality-control mechanism needed for MVP submissions or supply.",
            "compliance": "Clarify the smallest compliance-safe operating model needed for MVP.",
            "default": "Clarify the smallest technical control needed to close the feasibility risk.",
        },
        "growth": {
            "adoption_validation": "Clarify the smallest credible pilot motion that can validate adoption.",
            "demand_validation": "Clarify the clearest early demand signal and how it will be observed.",
            "market_motion": "Clarify the narrowest credible launch audience and first market motion.",
            "default": "Clarify the most focused acquisition or activation path that closes the market concern.",
        },
        "product": {
            "metrics_validation": "Define the smallest useful success metrics that make the MVP decision explicit.",
            "onboarding": "Clarify the smallest onboarding flow that still proves value.",
            "scope": "Clarify the narrowest credible wedge and remove anything not needed for proof.",
            "operations": "Clarify what must be built versus what can stay manual during MVP.",
            "default": "Clarify the narrowest credible product decision needed to close the concern.",
        },
    }
    owner_templates = templates.get(owner, {})
    if theme_key in owner_templates:
        return owner_templates[theme_key]
    return owner_templates.get("default", "Clarify the smallest credible way to close the issue.")


def _build_expected_output(owner: str, theme_key: str) -> str:
    outputs = {
        "tech": {
            "legal_compliance": "A concrete minimum control model that closes the launch blocker.",
            "privacy_trust": "A concrete minimum trust and privacy control set for MVP.",
            "data_access": "A concrete permissions and data-handling answer for the MVP workflow.",
            "quality_assurance": "A concrete quality-control answer that fits MVP scope.",
            "compliance": "A concrete compliance-safe operating baseline for MVP.",
            "default": "A concrete technical answer or a credible reduction path for the blocker.",
        },
        "growth": {
            "adoption_validation": "A concrete pilot motion with a validation signal.",
            "demand_validation": "A concrete demand-validation approach with a signal threshold.",
            "market_motion": "A concrete launch motion for the smallest credible audience.",
            "default": "A concrete GTM answer or a credible reduction path for the blocker.",
        },
        "product": {
            "metrics_validation": "A clear product decision that makes the MVP measurable.",
            "onboarding": "A clear product decision that keeps onboarding simple enough for proof.",
            "scope": "A clear product decision that narrows the wedge and removes accessories.",
            "operations": "A clear product decision on build-versus-manual scope.",
            "default": "A clear product decision or a credible reduction path for the blocker.",
        },
    }
    owner_outputs = outputs.get(owner, {})
    if theme_key in owner_outputs:
        return owner_outputs[theme_key]
    return owner_outputs.get("default", "A concrete answer or a credible reduction path for the blocker.")


def _build_contributors(owner: str, source_roles: list[str]) -> list[str]:
    source_roles = [role for role in source_roles if role]
    if owner == "product":
        return [role for role in source_roles if role != "product"]
    if owner in source_roles and len(source_roles) == 1:
        return []
    contributors = [role for role in source_roles if role not in {owner, "product"}]
    if not contributors and "product" not in source_roles:
        contributors = ["product"]
    return contributors


def _group_correction_tasks_by_owner(correction_tasks: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {"product": [], "tech": [], "growth": []}
    for task in correction_tasks:
        grouped.setdefault(task["owner"], []).append(task)
    return grouped


def _snapshot_readiness(
    blackboard: dict, loop_number: int, phase: str, correction_tasks: list[dict]
) -> dict:
    readiness = blackboard["readiness"]
    return {
        "loop": loop_number,
        "phase": phase,
        "global_status": readiness["global_status"],
        "product": readiness["product"]["status"],
        "tech": readiness["tech"]["status"],
        "growth": readiness["growth"]["status"],
        "global_blocking_gaps": list(readiness["global"]["blocking_gaps"]),
        "global_required_improvements": list(readiness["global"]["required_improvements"]),
        "known_tags": list(readiness.get("known_tags", [])),
        "tasks": correction_tasks,
    }


def _format_tagged_gap(gap: dict) -> str:
    tag = _normalize_gap_tag(gap.get("tag", ""))
    text = gap.get("merged_text") or gap.get("text", "")
    if tag and tag != "untagged":
        return f"[{tag}] {text}"
    return text


def run_v4_flow(
    project_name: str,
    project_brief: str,
    project_brief_source: str,
    progress_callback=None,
    step_timeout_seconds: int | None = None,
    workspace_factory: Callable[[str], object] | None = None,
    summary_runner: Callable[..., dict] | None = None,
    agent_runner: Callable[..., dict] | None = None,
) -> dict:
    workspace_factory = workspace_factory or create_run_workspace
    workspace = workspace_factory(project_name)
    if summary_runner is None:
        summary_runner = _v4_summary_runner_with_metrics
    state = {
        "workspace": workspace,
        "project_name": project_name,
        "project_brief": project_brief,
        "project_brief_source": project_brief_source,
        "documents": {},
        "summaries": {},
        "flow_version": "V4",
    }
    _append_v4_log(workspace, "orchestrator", "workspace_created", "app/orchestrator.py", workspace.run_id)
    _emit_progress(
        progress_callback,
        stage="brief_received",
        label="Run V4 initialisé",
        detail="Le workspace V4 a été créé pour ce run.",
        active_blocks=["brief_received"],
        done_blocks=[],
    )

    product_create = _run_v4_agent(
        role="product",
        mode_label="initial_draft",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=_open_items_for_role(workspace, "PRODUCT"),
        summaries={},
        documents={},
        extra_context=[],
        agent_runner=agent_runner,
    )
    prd_v0_path = write_document(workspace, "product", "PRD_V0.md", product_create["document_text"])
    state["documents"]["product_v0"] = prd_v0_path
    _apply_v4_item_operations(workspace, product_create, default_author="PRODUCT")
    _refresh_v4_item_state(state, workspace)
    _record_v4_stage(workspace, "product_initial", prd_v0_path, product_create)
    _emit_progress(
        progress_callback,
        stage="product_initial",
        label="PRD V0 écrit",
        detail="Product a produit le premier PRD V0 dans le run workspace.",
        active_blocks=[
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
        ],
        done_blocks=["brief_received"],
    )
    prd_v0_summary = summary_runner(workspace, prd_v0_path)
    state["summaries"]["product_v0"] = prd_v0_summary
    product_current_path = prd_v0_path
    product_current_summary = prd_v0_summary

    growth_create = _run_v4_agent(
        role="growth",
        mode_label="review",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=_open_items_for_role(workspace, "GROWTH"),
        summaries={"product": prd_v0_summary},
        documents={"product": prd_v0_path.read_text(encoding="utf-8")},
        extra_context=[
            _format_summary_context("Product summary", prd_v0_summary),
            _format_document_context("PRD_V0.md", prd_v0_path.read_text(encoding="utf-8")),
        ],
        agent_runner=agent_runner,
    )
    gtm_v0_path = write_document(workspace, "growth", "GTM_V0.md", growth_create["document_text"])
    state["documents"]["growth_v0"] = gtm_v0_path
    _apply_v4_item_operations(workspace, growth_create, default_author="GROWTH")
    _refresh_v4_item_state(state, workspace)
    _record_v4_stage(workspace, "growth_review", gtm_v0_path, growth_create)
    _emit_progress(
        progress_callback,
        stage="growth_review",
        label="GTM V0 écrit",
        detail="Growth a produit le premier GTM V0.",
        active_blocks=[
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
        ],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
        ],
    )
    gtm_v0_summary = summary_runner(workspace, gtm_v0_path)
    state["summaries"]["growth_v0"] = gtm_v0_summary
    growth_current_path = gtm_v0_path
    growth_current_summary = gtm_v0_summary

    tech_create = _run_v4_agent(
        role="tech",
        mode_label="review",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=_open_items_for_role(workspace, "TECH"),
        summaries={"product": prd_v0_summary, "growth": gtm_v0_summary},
        documents={
            "product": prd_v0_path.read_text(encoding="utf-8"),
            "growth": gtm_v0_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product summary", prd_v0_summary),
            _format_summary_context("Growth summary", gtm_v0_summary),
            _format_document_context("PRD_V0.md", prd_v0_path.read_text(encoding="utf-8")),
            _format_document_context("GTM_V0.md", gtm_v0_path.read_text(encoding="utf-8")),
        ],
        agent_runner=agent_runner,
    )
    architecture_v0_path = write_document(
        workspace, "tech", "Architecture_V0.md", tech_create["document_text"]
    )
    state["documents"]["tech_v0"] = architecture_v0_path
    _apply_v4_item_operations(workspace, tech_create, default_author="TECH")
    _refresh_v4_item_state(state, workspace)
    _record_v4_stage(workspace, "tech_review", architecture_v0_path, tech_create)
    _emit_progress(
        progress_callback,
        stage="tech_review",
        label="Architecture V0 écrite",
        detail="Tech a produit la première architecture V0.",
        active_blocks=[
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
        ],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
        ],
    )
    architecture_v0_summary = summary_runner(workspace, architecture_v0_path)
    state["summaries"]["tech_v0"] = architecture_v0_summary
    tech_current_path = architecture_v0_path
    tech_current_summary = architecture_v0_summary
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])

    product_revision = _run_v4_agent(
        role="product",
        mode_label="revision",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=open_items,
        summaries={
            "product": product_current_summary,
            "growth": growth_current_summary,
            "tech": tech_current_summary,
        },
        documents={
            "product": product_current_path.read_text(encoding="utf-8"),
            "growth": growth_current_path.read_text(encoding="utf-8"),
            "tech": tech_current_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product summary", product_current_summary),
            _format_summary_context("Growth summary", growth_current_summary),
            _format_summary_context("Tech summary", tech_current_summary),
            _format_document_context(product_current_path.name, product_current_path.read_text(encoding="utf-8")),
            _format_document_context(growth_current_path.name, growth_current_path.read_text(encoding="utf-8")),
            _format_document_context(
                tech_current_path.name, tech_current_path.read_text(encoding="utf-8")
            ),
            _format_open_items_context(workspace, open_items),
        ],
        agent_runner=agent_runner,
    )
    prd_v1_path = write_document(workspace, "product", "PRD_V1.md", product_revision["document_text"])
    state["documents"]["product_v1"] = prd_v1_path
    _apply_v4_item_operations(workspace, product_revision, default_author="PRODUCT")
    _refresh_v4_item_state(state, workspace)
    _record_v4_stage(workspace, "product_revision", prd_v1_path, product_revision)
    _emit_progress(
        progress_callback,
        stage="product_revision",
        label="PRD V1 écrit",
        detail="Product a arbitré les retours Growth et Tech.",
        active_blocks=["product_revision"],
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
        ],
    )
    prd_v1_summary = summary_runner(workspace, prd_v1_path)
    state["summaries"]["product_v1"] = prd_v1_summary
    product_current_path = prd_v1_path
    product_current_summary = prd_v1_summary

    correction_log = _run_v4_item_resolution_loop(
        workspace=workspace,
        state=state,
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        product_path=product_current_path,
        growth_path=growth_current_path,
        tech_path=tech_current_path,
        product_summary=product_current_summary,
        growth_summary=growth_current_summary,
        tech_summary=tech_current_summary,
        summary_runner=summary_runner,
        agent_runner=agent_runner,
        stage_prefix="correction",
        max_loops=2,
    )
    product_current_path = correction_log["paths"]["product"]
    growth_current_path = correction_log["paths"]["growth"]
    tech_current_path = correction_log["paths"]["tech"]
    product_current_summary = correction_log["summaries"]["product"]
    growth_current_summary = correction_log["summaries"]["growth"]
    tech_current_summary = correction_log["summaries"]["tech"]

    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])

    candidate_growth = _run_v4_agent(
        role="growth",
        mode_label="candidate_rewrite",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=open_items,
        summaries={
            "product": product_current_summary,
            "growth": growth_current_summary,
            "tech": tech_current_summary,
        },
        documents={
            "product": product_current_path.read_text(encoding="utf-8"),
            "growth": growth_current_path.read_text(encoding="utf-8"),
            "tech": tech_current_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product summary", product_current_summary),
            _format_summary_context("Growth summary", growth_current_summary),
            _format_summary_context("Tech summary", tech_current_summary),
            _format_items_context("Resolved Blackboard Items", resolved_items),
            _format_items_context("Remaining Open Blackboard Items", open_items),
            _format_open_items_context(workspace, open_items),
        ],
        agent_runner=agent_runner,
    )
    gtm_candidate_path = write_document(
        workspace, "growth", "GTM_CANDIDATE.md", candidate_growth["document_text"]
    )
    state["documents"]["growth_candidate"] = gtm_candidate_path
    _apply_v4_item_operations(workspace, candidate_growth, default_author="GROWTH")
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])
    _record_v4_stage(workspace, "growth_candidate_rewrite", gtm_candidate_path, candidate_growth)
    candidate_growth_summary = summary_runner(workspace, gtm_candidate_path)
    state["summaries"]["growth_candidate"] = candidate_growth_summary

    candidate_tech = _run_v4_agent(
        role="tech",
        mode_label="candidate_rewrite",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=open_items,
        summaries={
            "product": product_current_summary,
            "growth": candidate_growth_summary,
            "tech": tech_current_summary,
        },
        documents={
            "product": product_current_path.read_text(encoding="utf-8"),
            "growth": gtm_candidate_path.read_text(encoding="utf-8"),
            "tech": tech_current_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product summary", product_current_summary),
            _format_summary_context("Growth summary", candidate_growth_summary),
            _format_summary_context("Tech summary", tech_current_summary),
            _format_items_context("Resolved Blackboard Items", resolved_items),
            _format_items_context("Remaining Open Blackboard Items", open_items),
            _format_open_items_context(workspace, open_items),
        ],
        agent_runner=agent_runner,
    )
    architecture_candidate_path = write_document(
        workspace, "tech", "Architecture_CANDIDATE.md", candidate_tech["document_text"]
    )
    state["documents"]["tech_candidate"] = architecture_candidate_path
    _apply_v4_item_operations(workspace, candidate_tech, default_author="TECH")
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])
    _record_v4_stage(
        workspace, "tech_candidate_rewrite", architecture_candidate_path, candidate_tech
    )
    candidate_tech_summary = summary_runner(workspace, architecture_candidate_path)
    state["summaries"]["tech_candidate"] = candidate_tech_summary

    candidate_product = _run_v4_agent(
        role="product",
        mode_label="candidate_rewrite",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=open_items,
        summaries={
            "product": product_current_summary,
            "growth": candidate_growth_summary,
            "tech": candidate_tech_summary,
        },
        documents={
            "product": product_current_path.read_text(encoding="utf-8"),
            "growth": gtm_candidate_path.read_text(encoding="utf-8"),
            "tech": architecture_candidate_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product summary", product_current_summary),
            _format_summary_context("Growth summary", candidate_growth_summary),
            _format_summary_context("Tech summary", candidate_tech_summary),
            _format_items_context("Resolved Blackboard Items", resolved_items),
            _format_items_context("Remaining Open Blackboard Items", open_items),
            _format_open_items_context(workspace, open_items),
        ],
        agent_runner=agent_runner,
    )
    prd_candidate_path = write_document(
        workspace, "product", "PRD_CANDIDATE.md", candidate_product["document_text"]
    )
    state["documents"]["product_candidate"] = prd_candidate_path
    _apply_v4_item_operations(workspace, candidate_product, default_author="PRODUCT")
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])
    _record_v4_stage(workspace, "product_candidate_rewrite", prd_candidate_path, candidate_product)
    candidate_product_summary = summary_runner(workspace, prd_candidate_path)
    state["summaries"]["product_candidate"] = candidate_product_summary

    verification_notes: list[dict] = []
    verification_inputs = {
        "product": prd_candidate_path.read_text(encoding="utf-8"),
        "growth": gtm_candidate_path.read_text(encoding="utf-8"),
        "tech": architecture_candidate_path.read_text(encoding="utf-8"),
    }
    verification_summaries = {
        "product": candidate_product_summary,
        "growth": candidate_growth_summary,
        "tech": candidate_tech_summary,
    }
    for role in ("product", "growth", "tech"):
        verification_output = _run_v4_agent(
            role=role,
            mode_label="verification",
            project_brief=project_brief,
            project_brief_source=project_brief_source,
            workspace=workspace,
            state=state,
            open_items=open_items,
            summaries=verification_summaries,
            documents=verification_inputs,
            extra_context=[
                _format_summary_context("Product candidate summary", candidate_product_summary),
                _format_summary_context("Growth candidate summary", candidate_growth_summary),
                _format_summary_context("Tech candidate summary", candidate_tech_summary),
                _format_items_context("Resolved Blackboard Items", resolved_items),
                _format_items_context("Remaining Open Blackboard Items", open_items),
            ],
            agent_runner=agent_runner,
        )
        _apply_v4_item_operations(workspace, verification_output, default_author=role.upper())
        open_items = _refresh_v4_item_state(state, workspace)
        resolved_items = list(state["resolved_items"])
        verification_notes.append(
            {
                "role": role,
                "note": verification_output["document_text"],
                "items_to_create": verification_output.get("items_to_create", []),
                "items_to_update": verification_output.get("items_to_update", []),
            }
        )
        _append_v4_log(
            workspace,
            "orchestrator",
            f"{role}_verification",
            "app/orchestrator.py",
            f"items_to_create={len(verification_output.get('items_to_create', []))}; items_to_update={len(verification_output.get('items_to_update', []))}",
        )
    state["verification_notes"] = verification_notes
    post_verification_resolution_log = _run_v4_item_resolution_loop(
        workspace=workspace,
        state=state,
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        product_path=prd_candidate_path,
        growth_path=gtm_candidate_path,
        tech_path=architecture_candidate_path,
        product_summary=candidate_product_summary,
        growth_summary=candidate_growth_summary,
        tech_summary=candidate_tech_summary,
        summary_runner=summary_runner,
        agent_runner=agent_runner,
        stage_prefix="post_verification_resolution",
        max_loops=2,
    )
    state["post_verification_resolution_log"] = post_verification_resolution_log["log"]
    prd_candidate_path = post_verification_resolution_log["paths"]["product"]
    gtm_candidate_path = post_verification_resolution_log["paths"]["growth"]
    architecture_candidate_path = post_verification_resolution_log["paths"]["tech"]
    candidate_product_summary = post_verification_resolution_log["summaries"]["product"]
    candidate_growth_summary = post_verification_resolution_log["summaries"]["growth"]
    candidate_tech_summary = post_verification_resolution_log["summaries"]["tech"]
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])

    final_product = _run_v4_agent(
        role="product",
        mode_label="finalization",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=open_items,
        summaries={
            "product": candidate_product_summary,
            "growth": candidate_growth_summary,
            "tech": candidate_tech_summary,
        },
        documents={
            "product": prd_candidate_path.read_text(encoding="utf-8"),
            "growth": gtm_candidate_path.read_text(encoding="utf-8"),
            "tech": architecture_candidate_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product candidate summary", candidate_product_summary),
            _format_summary_context("Growth candidate summary", candidate_growth_summary),
            _format_summary_context("Tech candidate summary", candidate_tech_summary),
            _format_items_context("Resolved Blackboard Items", resolved_items),
            _format_items_context("Remaining Open Blackboard Items", open_items),
            _format_open_items_context(workspace, open_items),
        ],
        agent_runner=agent_runner,
    )
    prd_final_path = write_document(
        workspace, "product", "PRD_FINAL.md", final_product["document_text"]
    )
    state["documents"]["product_final"] = prd_final_path
    _apply_v4_finalization_item_operations(workspace, final_product, default_author="PRODUCT")
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])
    _record_v4_stage(workspace, "product_finalization", prd_final_path, final_product)
    product_final_summary = summary_runner(workspace, prd_final_path)
    state["summaries"]["product_final"] = product_final_summary

    growth_final_open_items = _open_items_for_role(workspace, "GROWTH")
    final_growth = _run_v4_agent(
        role="growth",
        mode_label="finalization",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=growth_final_open_items,
        summaries={
            "product": product_final_summary,
            "growth": candidate_growth_summary,
            "tech": candidate_tech_summary,
        },
        documents={
            "product": prd_final_path.read_text(encoding="utf-8"),
            "growth": gtm_candidate_path.read_text(encoding="utf-8"),
            "tech": architecture_candidate_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product final summary", product_final_summary),
            _format_summary_context("Growth candidate summary", candidate_growth_summary),
            _format_summary_context("Tech candidate summary", candidate_tech_summary),
            _format_items_context("Resolved Blackboard Items", resolved_items),
            _format_items_context("Remaining Growth Open Blackboard Items", growth_final_open_items),
        ],
        agent_runner=agent_runner,
    )
    gtm_final_path = write_document(workspace, "growth", "GTM_FINAL.md", final_growth["document_text"])
    state["documents"]["growth_final"] = gtm_final_path
    _apply_v4_finalization_item_operations(workspace, final_growth, default_author="GROWTH")
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])
    _record_v4_stage(workspace, "growth_finalization", gtm_final_path, final_growth)
    growth_final_summary = summary_runner(workspace, gtm_final_path)
    state["summaries"]["growth_final"] = growth_final_summary

    tech_final_open_items = _open_items_for_role(workspace, "TECH")
    final_tech = _run_v4_agent(
        role="tech",
        mode_label="finalization",
        project_brief=project_brief,
        project_brief_source=project_brief_source,
        workspace=workspace,
        state=state,
        open_items=tech_final_open_items,
        summaries={
            "product": product_final_summary,
            "growth": growth_final_summary,
            "tech": candidate_tech_summary,
        },
        documents={
            "product": prd_final_path.read_text(encoding="utf-8"),
            "growth": gtm_final_path.read_text(encoding="utf-8"),
            "tech": architecture_candidate_path.read_text(encoding="utf-8"),
        },
        extra_context=[
            _format_summary_context("Product final summary", product_final_summary),
            _format_summary_context("Growth final summary", growth_final_summary),
            _format_summary_context("Tech candidate summary", candidate_tech_summary),
            _format_items_context("Resolved Blackboard Items", resolved_items),
            _format_items_context("Remaining Tech Open Blackboard Items", tech_final_open_items),
        ],
        agent_runner=agent_runner,
    )
    architecture_final_path = write_document(
        workspace, "tech", "Architecture_FINAL.md", final_tech["document_text"]
    )
    state["documents"]["tech_final"] = architecture_final_path
    _apply_v4_finalization_item_operations(workspace, final_tech, default_author="TECH")
    open_items = _refresh_v4_item_state(state, workspace)
    resolved_items = list(state["resolved_items"])
    _record_v4_stage(workspace, "tech_finalization", architecture_final_path, final_tech)
    tech_final_summary = summary_runner(workspace, architecture_final_path)
    state["summaries"]["tech_final"] = tech_final_summary

    _emit_progress(
        progress_callback,
        stage="product_locking",
        label="V4 finalisation prête",
        detail=f"{len(open_items)} item(s) restent ouverts avant compilation finale.",
        done_blocks=[
            "brief_received",
            "product_brief_analysis",
            "product_problem",
            "product_users_goals",
            "product_user_stories",
            "growth_segments",
            "growth_positioning",
            "growth_channels",
            "growth_objections",
            "tech_constraints",
            "tech_components",
            "tech_mermaid",
            "tech_risks",
            "product_revision",
            "readiness_check",
            "correction_loop",
            "product_locking",
        ],
    )
    _append_v4_log(
        workspace,
        "orchestrator",
        "finalization_ready",
        "app/orchestrator.py",
        f"open_items={len(open_items)}",
    )
    state["correction_log"] = correction_log["log"]
    state["open_items"] = open_items
    state["resolved_items"] = resolved_items
    return state


def _run_v4_agent(
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
    agent_runner: Callable[..., dict] | None = None,
) -> dict:
    stage_label = _v4_stage_label(role, mode_label)
    trace_counts = state.setdefault("_v4_trace_counts", {})
    trace_index = int(trace_counts.get(stage_label, 0)) + 1
    trace_counts[stage_label] = trace_index
    trace_stage_label = stage_label if trace_index == 1 else f"{stage_label}_{trace_index:02d}"
    if agent_runner is not None:
        parsed = agent_runner(
            role=role,
            mode_label=mode_label,
            project_brief=project_brief,
            project_brief_source=project_brief_source,
            workspace=workspace,
            state=state,
            open_items=open_items,
            summaries=summaries,
            documents=documents,
            extra_context=extra_context,
        )
        parsed["role"] = role
        parsed["mode_label"] = mode_label
        parsed.setdefault("raw_response", parsed.get("document_text", ""))
    else:
        system_prompt = _build_v4_system_prompt(role)
        user_prompt = _build_v4_user_prompt(
            role=role,
            mode_label=mode_label,
            project_brief=project_brief,
            project_brief_source=project_brief_source,
            workspace=workspace,
            open_items=open_items,
            summaries=summaries,
            documents=documents,
            extra_context=extra_context,
        )
        document_schema = _build_v4_document_schema(role)
        document_json = _call_v4_llm_json(
            workspace=workspace,
            role=role,
            mode_label=mode_label,
            call_type="document",
            trace_stage_label=trace_stage_label,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            schema=document_schema,
            schema_name=f"v4_{role}_document",
        )
        document_json_trace_path = _write_v4_json_trace(
            workspace,
            f"{trace_stage_label}_document",
            document_json,
        )
        try:
            parsed = _parse_v4_structured_agent_output(document_json, role=role)
        except ValueError as error:
            raise ValueError(
                f"V4 {role} {mode_label} structured document parsing failed. "
                f"Raw trace: {document_json_trace_path}. {error}"
            ) from error
        trace_path = _write_v4_raw_response_trace(
            workspace,
            trace_stage_label,
            parsed["document_text"],
        )
        parsed["role"] = role
        parsed["mode_label"] = mode_label
        parsed["structured_document_trace_path"] = str(document_json_trace_path)
        parsed["raw_response_trace_path"] = str(trace_path)
        parsed["raw_response_trace_stage"] = trace_stage_label
        validate_v4_document(
            role=role,
            mode_label=mode_label,
            parsed_response=parsed,
            raw_response_trace_path=trace_path,
        )
        operations_schema = _build_v4_blackboard_schema(
            role=role,
            mode_label=mode_label,
            updateable_items=open_items,
        )
        if _v4_should_skip_blackboard_operations(mode_label=mode_label, open_items=open_items):
            operations_prompt = ""
            operations_json = {"create": [], "update": []}
            parsed["blackboard_operations_skipped"] = True
            _record_v4_prompt_metric(
                workspace,
                {
                    "role": role,
                    "mode_label": mode_label,
                    "stage": trace_stage_label,
                    "call_type": "blackboard",
                    "schema_name": "v4_blackboard_operations",
                    "status": "skipped",
                    "skip_reason": "no_creates_and_no_updateable_items",
                    "system_chars": len(system_prompt),
                    "user_chars": 0,
                    "schema_chars": len(json.dumps(operations_schema, ensure_ascii=False, sort_keys=True)),
                    "output_chars": len(json.dumps(operations_json, ensure_ascii=False, sort_keys=True)),
                },
            )
            _append_v4_log(
                workspace,
                "orchestrator",
                "blackboard_operations_skipped",
                "app/orchestrator.py",
                f"stage={trace_stage_label}; reason=no_creates_and_no_updateable_items",
            )
        else:
            operations_prompt = _build_v4_blackboard_prompt(
                role=role,
                mode_label=mode_label,
                project_brief=project_brief,
                project_brief_source=project_brief_source,
                workspace=workspace,
                open_items=open_items,
                summaries=summaries,
                documents=documents,
                produced_document=parsed["document_text"],
                extra_context=extra_context,
            )
            operations_json = _call_v4_llm_json(
                workspace=workspace,
                role=role,
                mode_label=mode_label,
                call_type="blackboard",
                trace_stage_label=trace_stage_label,
                system_prompt=system_prompt,
                user_prompt=operations_prompt,
                schema=operations_schema,
                schema_name="v4_blackboard_operations",
            )
        operations_trace_path = _write_v4_json_trace(
            workspace,
            f"{trace_stage_label}_blackboard",
            operations_json,
        )
        try:
            parsed_operations = parse_v4_blackboard_operations(operations_json, line_number=1)
        except ValueError as error:
            raise ValueError(
                f"V4 {role} {mode_label} blackboard operation parsing failed. "
                f"Raw trace: {operations_trace_path}. {error}"
            ) from error
        parsed["items_to_create"] = parsed_operations["items_to_create"]
        parsed["items_to_update"] = parsed_operations["items_to_update"]
        parsed["blackboard_operations_trace_path"] = str(operations_trace_path)
        parsed["blackboard_operation_format"] = "separate_json"
        existing_items = list_items(workspace)
        validate_v4_item_operations(
            role=role,
            mode_label=mode_label,
            parsed_response=parsed,
            raw_response_trace_path=operations_trace_path,
            allow_creates=_v4_allows_create_operations(mode_label),
            existing_item_ids={item["id"] for item in existing_items},
            existing_items_by_id={item["id"]: item for item in existing_items},
        )

    raw_response = str(parsed.get("raw_response") or parsed.get("document_text") or "")
    if "raw_response_trace_path" in parsed:
        trace_path = Path(str(parsed["raw_response_trace_path"]))
    else:
        trace_path = _write_v4_raw_response_trace(workspace, trace_stage_label, raw_response)
        parsed["raw_response_trace_path"] = str(trace_path)
        parsed["raw_response_trace_stage"] = trace_stage_label
    validate_v4_document(
        role=role,
        mode_label=mode_label,
        parsed_response=parsed,
        raw_response_trace_path=trace_path,
    )
    _validate_v4_external_decision_guardrails(
        role=role,
        mode_label=mode_label,
        project_brief=project_brief,
        open_items=open_items,
        summaries=summaries,
        documents=documents,
        parsed_response=parsed,
        raw_response_trace_path=trace_path,
    )
    return parsed


def _refresh_v4_item_state(state: dict, workspace) -> list[dict]:
    resolved_items = [item for item in list_items(workspace) if item.get("status") != "OPEN"]
    open_items = list_open_items(workspace)
    state["resolved_items"] = resolved_items
    state["open_items"] = open_items
    return open_items


def _v4_summary_runner_with_metrics(workspace, source_document_path):
    return generate_summary(
        workspace,
        source_document_path,
        metric_recorder=_record_v4_prompt_metric,
    )


def _call_v4_llm_json(
    *,
    workspace,
    role: str,
    mode_label: str,
    call_type: str,
    trace_stage_label: str,
    system_prompt: str,
    user_prompt: str,
    schema: dict,
    schema_name: str,
) -> dict:
    metric = {
        "role": role,
        "mode_label": mode_label,
        "stage": trace_stage_label,
        "call_type": call_type,
        "schema_name": schema_name,
        "status": "started",
        "system_chars": len(system_prompt),
        "user_chars": len(user_prompt),
        "schema_chars": len(json.dumps(schema, ensure_ascii=False, sort_keys=True)),
        "output_chars": 0,
    }
    try:
        payload = call_llm_json(
            system_prompt,
            user_prompt,
            schema,
            schema_name=schema_name,
        )
    except Exception:
        metric["status"] = "error"
        _record_v4_prompt_metric(workspace, metric)
        raise
    metric["status"] = "ok"
    metric["output_chars"] = len(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    _record_v4_prompt_metric(workspace, metric)
    return payload


def _record_v4_prompt_metric(workspace, metric: dict) -> None:
    metrics_path = workspace.root / "prompt_metrics.jsonl"
    enriched = {
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "run_id": workspace.run_id,
        "model": os.getenv("OPENAI_MODEL", ""),
        "reasoning_effort": os.getenv("OPENAI_REASONING_EFFORT", ""),
        **metric,
    }
    write_text_file(
        metrics_path,
        (
            metrics_path.read_text(encoding="utf-8")
            if metrics_path.exists()
            else ""
        )
        + json.dumps(enriched, ensure_ascii=False, sort_keys=True)
        + "\n",
    )


def _v4_should_skip_blackboard_operations(*, mode_label: str, open_items: list[dict]) -> bool:
    if _v4_allows_create_operations(mode_label):
        return False
    return not _v4_updateable_item_ids(open_items)


def _run_v4_item_resolution_loop(
    *,
    workspace,
    state: dict,
    project_brief: str,
    project_brief_source: str,
    product_path: Path,
    growth_path: Path,
    tech_path: Path,
    product_summary: dict,
    growth_summary: dict,
    tech_summary: dict,
    summary_runner: Callable[..., dict],
    agent_runner: Callable[..., dict] | None,
    stage_prefix: str,
    max_loops: int,
) -> dict:
    resolution_log: list[dict] = []
    current_paths = {
        "product": product_path,
        "growth": growth_path,
        "tech": tech_path,
    }
    current_summaries = {
        "product": product_summary,
        "growth": growth_summary,
        "tech": tech_summary,
    }
    for loop_number in range(1, max_loops + 1):
        open_items = list_open_items(workspace)
        if not open_items:
            break
        grouped = _group_items_by_owner(open_items)
        loop_changed = False

        if grouped["growth"]:
            before_document_text = current_paths["growth"].read_text(encoding="utf-8")
            growth_resolution = _run_v4_agent(
                role="growth",
                mode_label="item_resolution",
                project_brief=project_brief,
                project_brief_source=project_brief_source,
                workspace=workspace,
                state=state,
                open_items=grouped["growth"],
                summaries={
                    "product": current_summaries["product"],
                    "growth": current_summaries["growth"],
                    "tech": current_summaries["tech"],
                },
                documents={
                    "product": current_paths["product"].read_text(encoding="utf-8"),
                    "growth": before_document_text,
                    "tech": current_paths["tech"].read_text(encoding="utf-8"),
                },
                extra_context=[
                    _format_summary_context("Product summary", current_summaries["product"]),
                    _format_summary_context("Growth summary", current_summaries["growth"]),
                    _format_summary_context("Tech summary", current_summaries["tech"]),
                    _format_open_items_context(workspace, grouped["growth"]),
                ],
                agent_runner=agent_runner,
            )
            operation_result = _apply_v4_item_operations(
                workspace, growth_resolution, default_author="GROWTH"
            )
            _refresh_v4_item_state(state, workspace)
            current_paths["growth"], current_summaries["growth"] = (
                _write_v4_resolution_document_and_summary(
                    workspace=workspace,
                    state=state,
                    role="growth",
                    stage_prefix=stage_prefix,
                    loop_number=loop_number,
                    agent_output=growth_resolution,
                    summary_runner=summary_runner,
                )
            )
            _record_v4_stage(
                workspace,
                _v4_resolution_stage_name(stage_prefix, "growth", loop_number),
                current_paths["growth"],
                growth_resolution,
            )
            state.setdefault("resolution_notes", []).append(
                {
                    "phase": stage_prefix,
                    "loop": loop_number,
                    "role": "growth",
                    "items": [item["id"] for item in grouped["growth"]],
                    "document": current_paths["growth"].name,
                    "note": growth_resolution["document_text"],
                }
            )
            resolution_log.append(
                {
                    "phase": stage_prefix,
                    "loop": loop_number,
                    "agent": "growth",
                    "items": [item["id"] for item in grouped["growth"]],
                    "document": current_paths["growth"].name,
                }
            )
            loop_changed = loop_changed or _v4_resolution_changed(
                before_document_text, growth_resolution, operation_result
            )

        if grouped["tech"]:
            before_document_text = current_paths["tech"].read_text(encoding="utf-8")
            tech_resolution = _run_v4_agent(
                role="tech",
                mode_label="item_resolution",
                project_brief=project_brief,
                project_brief_source=project_brief_source,
                workspace=workspace,
                state=state,
                open_items=grouped["tech"],
                summaries={
                    "product": current_summaries["product"],
                    "growth": current_summaries["growth"],
                    "tech": current_summaries["tech"],
                },
                documents={
                    "product": current_paths["product"].read_text(encoding="utf-8"),
                    "growth": current_paths["growth"].read_text(encoding="utf-8"),
                    "tech": before_document_text,
                },
                extra_context=[
                    _format_summary_context("Product summary", current_summaries["product"]),
                    _format_summary_context("Growth summary", current_summaries["growth"]),
                    _format_summary_context("Tech summary", current_summaries["tech"]),
                    _format_open_items_context(workspace, grouped["tech"]),
                ],
                agent_runner=agent_runner,
            )
            operation_result = _apply_v4_item_operations(
                workspace, tech_resolution, default_author="TECH"
            )
            _refresh_v4_item_state(state, workspace)
            current_paths["tech"], current_summaries["tech"] = (
                _write_v4_resolution_document_and_summary(
                    workspace=workspace,
                    state=state,
                    role="tech",
                    stage_prefix=stage_prefix,
                    loop_number=loop_number,
                    agent_output=tech_resolution,
                    summary_runner=summary_runner,
                )
            )
            _record_v4_stage(
                workspace,
                _v4_resolution_stage_name(stage_prefix, "tech", loop_number),
                current_paths["tech"],
                tech_resolution,
            )
            state.setdefault("resolution_notes", []).append(
                {
                    "phase": stage_prefix,
                    "loop": loop_number,
                    "role": "tech",
                    "items": [item["id"] for item in grouped["tech"]],
                    "document": current_paths["tech"].name,
                    "note": tech_resolution["document_text"],
                }
            )
            resolution_log.append(
                {
                    "phase": stage_prefix,
                    "loop": loop_number,
                    "agent": "tech",
                    "items": [item["id"] for item in grouped["tech"]],
                    "document": current_paths["tech"].name,
                }
            )
            loop_changed = loop_changed or _v4_resolution_changed(
                before_document_text, tech_resolution, operation_result
            )

        if grouped["product"] or loop_changed:
            product_items = grouped["product"] or list_open_items(workspace)
            before_document_text = current_paths["product"].read_text(encoding="utf-8")
            product_resolution = _run_v4_agent(
                role="product",
                mode_label="item_resolution",
                project_brief=project_brief,
                project_brief_source=project_brief_source,
                workspace=workspace,
                state=state,
                open_items=product_items,
                summaries={
                    "product": current_summaries["product"],
                    "growth": current_summaries["growth"],
                    "tech": current_summaries["tech"],
                },
                documents={
                    "product": before_document_text,
                    "growth": current_paths["growth"].read_text(encoding="utf-8"),
                    "tech": current_paths["tech"].read_text(encoding="utf-8"),
                },
                extra_context=[
                    _format_summary_context("Product summary", current_summaries["product"]),
                    _format_summary_context("Growth summary", current_summaries["growth"]),
                    _format_summary_context("Tech summary", current_summaries["tech"]),
                    _format_open_items_context(workspace, product_items),
                ],
                agent_runner=agent_runner,
            )
            operation_result = _apply_v4_item_operations(
                workspace, product_resolution, default_author="PRODUCT"
            )
            _refresh_v4_item_state(state, workspace)
            current_paths["product"], current_summaries["product"] = (
                _write_v4_resolution_document_and_summary(
                    workspace=workspace,
                    state=state,
                    role="product",
                    stage_prefix=stage_prefix,
                    loop_number=loop_number,
                    agent_output=product_resolution,
                    summary_runner=summary_runner,
                )
            )
            _record_v4_stage(
                workspace,
                _v4_resolution_stage_name(stage_prefix, "product", loop_number),
                current_paths["product"],
                product_resolution,
            )
            state.setdefault("resolution_notes", []).append(
                {
                    "phase": stage_prefix,
                    "loop": loop_number,
                    "role": "product",
                    "items": [item["id"] for item in product_items],
                    "document": current_paths["product"].name,
                    "note": product_resolution["document_text"],
                }
            )
            resolution_log.append(
                {
                    "phase": stage_prefix,
                    "loop": loop_number,
                    "agent": "product",
                    "items": [item["id"] for item in product_items],
                    "document": current_paths["product"].name,
                }
            )
            loop_changed = loop_changed or _v4_resolution_changed(
                before_document_text, product_resolution, operation_result
            )

        _append_v4_log(
            workspace,
            "orchestrator",
            _v4_resolution_loop_event(stage_prefix, loop_number),
            "app/orchestrator.py",
            f"changed={loop_changed}; open_items={len(list_open_items(workspace))}",
        )
        if not loop_changed:
            break
    return {
        "log": resolution_log,
        "paths": current_paths,
        "summaries": current_summaries,
    }


def _write_v4_resolution_document_and_summary(
    *,
    workspace,
    state: dict,
    role: str,
    stage_prefix: str,
    loop_number: int,
    agent_output: dict,
    summary_runner: Callable[..., dict],
) -> tuple[Path, dict]:
    document_name = _v4_resolution_document_name(stage_prefix, role, loop_number)
    document_path = write_document(workspace, role, document_name, agent_output["document_text"])
    document_key = _v4_resolution_document_key(stage_prefix, role, loop_number)
    state.setdefault("documents", {})[document_key] = document_path
    summary = summary_runner(workspace, document_path)
    state.setdefault("summaries", {})[document_key] = summary
    return document_path, summary


def _v4_resolution_document_name(stage_prefix: str, role: str, loop_number: int) -> str:
    prefix_by_role = {
        "product": "PRD",
        "growth": "GTM",
        "tech": "Architecture",
    }
    suffix = "CORRECTION" if stage_prefix == "correction" else "POST_VERIFICATION_RESOLUTION"
    prefix = prefix_by_role[str(role).strip().lower()]
    return f"{prefix}_{suffix}_{loop_number}.md"


def _v4_resolution_document_key(stage_prefix: str, role: str, loop_number: int) -> str:
    normalized_stage = re.sub(r"[^a-z0-9]+", "_", stage_prefix.strip().lower()).strip("_")
    return f"{role}_{normalized_stage}_{loop_number}"


def _v4_resolution_changed(
    previous_document_text: str,
    agent_output: dict,
    operation_result: dict | None,
) -> bool:
    operation_result = operation_result or {}
    if operation_result.get("created") or operation_result.get("updated"):
        return True
    return previous_document_text.strip() != str(agent_output.get("document_text", "")).strip()


def _v4_resolution_stage_name(stage_prefix: str, role: str, loop_number: int) -> str:
    if stage_prefix == "correction":
        return f"{role}_item_resolution_{loop_number}"
    return f"{stage_prefix}_{role}_item_resolution_{loop_number}"


def _v4_resolution_loop_event(stage_prefix: str, loop_number: int) -> str:
    if stage_prefix == "correction":
        return f"correction_loop_{loop_number}"
    return f"{stage_prefix}_loop_{loop_number}"


def _apply_v4_finalization_item_operations(workspace, agent_output: dict, default_author: str) -> None:
    existing_items = list_items(workspace)
    existing_item_ids = {item["id"] for item in existing_items}
    existing_items_by_id = {item["id"]: item for item in existing_items}
    validate_v4_item_operations(
        role=default_author.lower(),
        mode_label=str(agent_output.get("mode_label", "finalization")),
        parsed_response=agent_output,
        raw_response_trace_path=agent_output.get("blackboard_operations_trace_path")
        or agent_output.get("raw_response_trace_path", ""),
        allow_creates=False,
        allow_updates=True,
        existing_item_ids=existing_item_ids,
        existing_items_by_id=existing_items_by_id,
    )
    _validate_v4_finalization_updates_target_role(
        agent_output,
        default_author=default_author,
        existing_items_by_id=existing_items_by_id,
    )
    for update_spec in agent_output.get("items_to_update", []):
        update_item_status(workspace, update_spec["id"], update_spec["status"])


def _validate_v4_finalization_updates_target_role(
    agent_output: dict,
    *,
    default_author: str,
    existing_items_by_id: dict[str, dict],
) -> None:
    role_target = str(default_author).strip().upper()
    if role_target not in {"GROWTH", "TECH"}:
        return
    for update_spec in agent_output.get("items_to_update", []):
        item_id = str(update_spec.get("id", "")).strip().upper()
        item = existing_items_by_id.get(item_id, {})
        targets = {
            str(target).strip().upper()
            for target in item.get("targets", [])
            if str(target).strip()
        }
        if role_target not in targets:
            raise ValueError(
                "V4 finalization update rejected: "
                f"{role_target} may only update items targeted to {role_target}. "
                f"Invalid item id: {item_id}."
            )


def _build_v4_user_prompt(
    *,
    role: str,
    mode_label: str,
    project_brief: str,
    project_brief_source: str,
    workspace,
    open_items: list[dict],
    summaries: dict[str, dict],
    documents: dict[str, str],
    extra_context: list[str],
) -> str:
    selected_documents = _select_v4_documents_for_context(
        role=role,
        mode_label=mode_label,
        documents=documents,
        call_type="document",
    )
    selected_summaries = _select_v4_summaries_for_context(
        summaries=summaries,
        selected_documents=selected_documents,
        call_type="document",
    )
    sections = [
        f"Mode: {mode_label}",
        "Phase instruction:\n" + _load_v4_phase_prompt(mode_label),
        f"Run id:\n{workspace.run_id}",
        f"Project brief source:\n{project_brief_source}",
        f"Project brief:\n{project_brief}",
        _format_open_items_context(workspace, open_items),
    ]
    for summary_label, summary in selected_summaries.items():
        sections.append(_format_summary_context(f"{summary_label.capitalize()} summary", summary))
    for document_label, document_text in selected_documents.items():
        sections.append(_format_document_context(f"{document_label.upper()} document", document_text))
    sections.extend(
        _filter_v4_extra_context_sections(
            extra_context,
            include_remaining_items=False,
        )
    )
    sections.append("Document output contract:\n" + _load_v4_document_contract(role))
    sections.append(
        "Return only one JSON object matching the document schema. Each value is "
        "Markdown body content for that section only. Do not include blackboard "
        "operations or rendered `##` section headings in this response."
    )
    return "\n\n".join(section for section in sections if section.strip())


def _build_v4_blackboard_prompt(
    *,
    role: str,
    mode_label: str,
    project_brief: str,
    project_brief_source: str,
    workspace,
    open_items: list[dict],
    summaries: dict[str, dict],
    documents: dict[str, str],
    produced_document: str,
    extra_context: list[str],
) -> str:
    selected_documents = _select_v4_documents_for_context(
        role=role,
        mode_label=mode_label,
        documents=documents,
        call_type="blackboard",
    )
    selected_summaries = _select_v4_summaries_for_context(
        summaries=summaries,
        selected_documents=selected_documents,
        call_type="blackboard",
    )
    sections = [
        f"Mode: {mode_label}",
        "Phase instruction:\n" + _load_v4_phase_prompt(mode_label),
        f"Run id:\n{workspace.run_id}",
        f"Project brief source:\n{project_brief_source}",
        f"Project brief:\n{project_brief}",
        _format_open_items_context(workspace, open_items),
    ]
    for summary_label, summary in selected_summaries.items():
        sections.append(_format_summary_context(f"{summary_label.capitalize()} summary", summary))
    for document_label, document_text in selected_documents.items():
        sections.append(_format_document_context(f"{document_label.upper()} document", document_text))
    sections.extend(
        _filter_v4_extra_context_sections(
            extra_context,
            include_remaining_items=False,
        )
    )
    sections.append(_format_document_context("Current produced document", produced_document))
    sections.append("Blackboard output contract:\n" + _load_v4_blackboard_contract())
    sections.append(
        "Role-specific blackboard constraint:\n"
        f"- Current role: {str(role).strip().upper()}.\n"
        "- Allowed create targets for this role: "
        + ", ".join(_v4_allowed_create_targets_for_role(role))
        + ".\n"
        "- If a point only concerns the current role, resolve it in the document "
        "instead of creating a blackboard item."
    )
    if not _v4_allows_create_operations(mode_label):
        sections.append(
            "Phase-specific blackboard constraint:\n"
            f"- `{mode_label}` is no-create. `create` must be empty: `[]`.\n"
            "- Update only pre-existing routed items that this document directly addresses."
        )
    sections.append("Return only one JSON object matching the schema. Do not include Markdown.")
    return "\n\n".join(section for section in sections if section.strip())


def _select_v4_documents_for_context(
    *,
    role: str,
    mode_label: str,
    documents: dict[str, str],
    call_type: str,
) -> dict[str, str]:
    if not documents:
        return {}
    normalized_mode = str(mode_label).strip().lower()
    if call_type == "blackboard":
        return {}
    if normalized_mode == "initial_draft":
        return {}
    if normalized_mode in {"review", "revision", "verification"}:
        return dict(documents)
    if normalized_mode == "finalization" and str(role).strip().lower() == "product":
        return dict(documents)
    if normalized_mode in {"item_resolution", "candidate_rewrite", "finalization"}:
        return _select_current_role_document(role, documents)
    return dict(documents)


def _select_current_role_document(role: str, documents: dict[str, str]) -> dict[str, str]:
    role_key = str(role).strip().lower()
    if role_key in documents:
        return {role_key: documents[role_key]}
    matching = {
        key: value
        for key, value in documents.items()
        if str(key).strip().lower().startswith(role_key)
    }
    return matching or dict(documents)


def _select_v4_summaries_for_context(
    *,
    summaries: dict[str, dict],
    selected_documents: dict[str, str],
    call_type: str,
) -> dict[str, dict]:
    if not summaries:
        return {}
    if call_type == "blackboard":
        return dict(summaries)
    document_keys = {str(key).strip().lower() for key in selected_documents}
    return {
        key: summary
        for key, summary in summaries.items()
        if str(key).strip().lower() not in document_keys
    }


def _filter_v4_extra_context_sections(
    sections: list[str],
    *,
    include_remaining_items: bool,
) -> list[str]:
    filtered: list[str] = []
    seen: set[str] = set()
    for section in sections:
        text = str(section).strip()
        if not text:
            continue
        first_line = text.splitlines()[0].strip()
        if first_line.startswith("Summary context:"):
            continue
        if first_line.startswith("Context document:"):
            continue
        if first_line == "Open items context":
            continue
        if first_line.startswith("Items context: Remaining") and not include_remaining_items:
            continue
        if text in seen:
            continue
        seen.add(text)
        filtered.append(text)
    return filtered


def _parse_v4_agent_output(text: str, *, role: str | None = None) -> dict:
    parsed = parse_v4_agent_response(text, role=role)
    return {
        "raw_response": parsed["raw_response"],
        "document_text": parsed["document_text"],
        "sections": parsed["sections"],
        "items_to_create": parsed["items_to_create"],
        "items_to_update": parsed["items_to_update"],
        "blackboard_operation_format": parsed.get("blackboard_operation_format", "separate_json"),
    }


def _parse_v4_structured_agent_output(payload: dict, *, role: str) -> dict:
    parsed = parse_v4_structured_document(payload, role=role)
    return {
        "raw_response": parsed["document_text"],
        "document_text": parsed["document_text"],
        "sections": parsed["sections"],
        "items_to_create": parsed["items_to_create"],
        "items_to_update": parsed["items_to_update"],
        "blackboard_operation_format": parsed.get("blackboard_operation_format", "separate_json"),
        "structured_document_format": parsed.get("structured_document_format", "json_sections"),
    }


def _apply_v4_item_operations(workspace, agent_output: dict, default_author: str) -> dict:
    existing_items = list_items(workspace)
    existing_item_ids = {item["id"] for item in existing_items}
    existing_items_by_id = {item["id"]: item for item in existing_items}
    validate_v4_item_operations(
        role=default_author.lower(),
        mode_label=str(agent_output.get("mode_label", "unknown")),
        parsed_response=agent_output,
        raw_response_trace_path=agent_output.get("blackboard_operations_trace_path")
        or agent_output.get("raw_response_trace_path", ""),
        existing_item_ids=existing_item_ids,
        existing_items_by_id=existing_items_by_id,
    )
    created = 0
    reused = 0
    updated = 0
    for item_spec in agent_output.get("items_to_create", []):
        try:
            create_item(
                workspace,
                type=item_spec["type"],
                author=default_author,
                targets=item_spec["targets"],
                priority=item_spec["priority"],
                tags=item_spec["tags"],
                title=item_spec["title"],
                content=item_spec["content"],
            )
            created += 1
        except ValueError as error:
            if "Duplicate open blackboard item rejected" not in str(error):
                raise
            reused += 1
            _append_v4_log(
                workspace,
                "orchestrator",
                "blackboard_duplicate_item_reused",
                "app/orchestrator.py",
                str(error),
            )
    for update_spec in agent_output.get("items_to_update", []):
        update_item_status(workspace, update_spec["id"], update_spec["status"])
        updated += 1
    return {"created": created, "updated": updated, "reused": reused}


def _validate_v4_external_decision_guardrails(
    *,
    role: str,
    mode_label: str,
    project_brief: str,
    open_items: list[dict],
    summaries: dict[str, dict],
    documents: dict[str, str],
    parsed_response: dict,
    raw_response_trace_path: str | Path,
) -> None:
    if str(mode_label).strip().lower() != "item_resolution":
        return
    if not _v4_has_external_decision_pressure(open_items):
        return

    document_text = str(parsed_response.get("document_text", ""))
    source_text = _v4_guardrail_source_text(
        project_brief=project_brief,
        open_items=open_items,
        summaries=summaries,
        documents=documents,
    )
    unsupported_terms = [
        term
        for term in _V4_PROTECTED_EXTERNAL_DECISION_TERMS
        if _v4_text_contains_term(document_text, term)
        and not _v4_text_contains_term(source_text, term)
    ]
    if unsupported_terms:
        terms = ", ".join(sorted(unsupported_terms))
        raise ValueError(
            "V4 external decision guardrail rejected item_resolution output: "
            f"{role} introduced unsupported external decision term(s): {terms}. "
            "External market, compliance, legal, pricing, retention, audit, and "
            "policy facts must come from the project brief or runtime context. "
            f"Raw trace: {raw_response_trace_path}"
        )


def _v4_guardrail_source_text(
    *,
    project_brief: str,
    open_items: list[dict],
    summaries: dict[str, dict],
    documents: dict[str, str],
) -> str:
    item_text = "\n".join(
        "\n".join(
            [
                str(item.get("title", "")),
                str(item.get("content", "")),
                " ".join(str(tag) for tag in item.get("tags", [])),
            ]
        )
        for item in open_items
    )
    return "\n".join(
        [
            str(project_brief),
            item_text,
            json.dumps(summaries, ensure_ascii=False, sort_keys=True),
            "\n".join(str(value) for value in documents.values()),
        ]
    )


def _v4_has_external_decision_pressure(open_items: list[dict]) -> bool:
    for item in open_items:
        targets = {str(target).strip().upper() for target in item.get("targets", [])}
        if targets == {"EXTERNAL"}:
            return True
        searchable = " ".join(
            [
                str(item.get("title", "")),
                str(item.get("content", "")),
                " ".join(str(tag) for tag in item.get("tags", [])),
            ]
        ).lower()
        if any(keyword in searchable for keyword in _V4_EXTERNAL_DECISION_KEYWORDS):
            return True
    return False


def _v4_text_contains_term(text: str, term: str) -> bool:
    if len(term) <= 3 or not term.replace(".", "").isalpha():
        return term.lower() in text.lower()
    return re.search(rf"\b{re.escape(term)}\b", text, flags=re.IGNORECASE) is not None


_V4_EXTERNAL_DECISION_KEYWORDS = {
    "audit",
    "baseline",
    "ccpa",
    "compliance",
    "consent",
    "country",
    "gdpr",
    "geograph",
    "hipaa",
    "legal",
    "market",
    "policy",
    "price",
    "pricing",
    "privacy",
    "retention",
}


_V4_PROTECTED_EXTERNAL_DECISION_TERMS = (
    "United States",
    "U.S.",
    "USA",
    "United Kingdom",
    "U.K.",
    "UK",
    "France",
    "Canada",
    "Australia",
    "Germany",
    "Spain",
    "Italy",
    "Netherlands",
    "Belgium",
    "Switzerland",
    "Ireland",
    "HIPAA",
    "GDPR",
    "CCPA",
    "SOC 2",
    "ISO 27001",
    "$",
    "€",
    "£",
)


def _write_v4_raw_response_trace(workspace, stage_label: str, raw_response: str) -> Path:
    trace_dir = workspace.root / "agent_outputs"
    trace_path = trace_dir / f"{_normalize_v4_trace_stage(stage_label)}.raw.md"
    return write_text_file(trace_path, raw_response.rstrip() + "\n")


def _write_v4_json_trace(workspace, stage_label: str, payload: dict) -> Path:
    trace_dir = workspace.root / "agent_outputs"
    trace_path = trace_dir / f"{_normalize_v4_trace_stage(stage_label)}.json"
    return write_text_file(trace_path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def _v4_stage_label(role: str, mode_label: str) -> str:
    return f"{str(role).strip().lower()}_{str(mode_label).strip().lower()}"


def _normalize_v4_trace_stage(stage_label: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", stage_label.strip().lower())
    normalized = re.sub(r"_+", "_", normalized).strip("_")
    return normalized or "v4_agent"


def _build_v4_system_prompt(role: str) -> str:
    return "\n\n".join(
        [
            _load_v4_prompt_file("roles", f"{role}.md"),
            _load_v4_prompt_file("common", "workflow_context.md"),
        ]
    )


def _load_v4_phase_prompt(mode_label: str) -> str:
    return _load_v4_prompt_file("phases", f"{mode_label}.md")


def _load_v4_document_contract(role: str) -> str:
    return _load_v4_prompt_file("contracts", f"{role}_document.md")


def _build_v4_document_schema(role: str) -> dict:
    return build_v4_document_schema(role)


def _load_v4_blackboard_contract() -> str:
    return _load_v4_prompt_file("contracts", "blackboard_operations.md")


def _build_v4_blackboard_schema(
    *,
    role: str,
    mode_label: str,
    updateable_items: list[dict] | None = None,
) -> dict:
    schema = _load_v4_blackboard_schema()
    schema["properties"]["create"]["items"]["properties"]["targets"] = (
        _v4_create_targets_schema_for_role(role)
    )
    updateable_ids = _v4_updateable_item_ids(updateable_items or [])
    if updateable_ids:
        schema["properties"]["update"]["items"]["properties"]["id"] = {
            "enum": updateable_ids
        }
    else:
        schema["properties"]["update"]["maxItems"] = 0
        schema["properties"]["update"]["description"] = (
            "No updateable item ids are available for this call."
        )
    if not _v4_allows_create_operations(mode_label):
        schema["properties"]["create"]["maxItems"] = 0
        schema["properties"]["create"]["description"] = "This phase is no-create; create must be empty."
    return schema


def _v4_updateable_item_ids(items: list[dict]) -> list[str]:
    ids = []
    for item in items:
        item_id = str(item.get("id", "")).strip().upper()
        status = str(item.get("status", "")).strip().upper()
        targets = [
            str(target).strip().upper()
            for target in item.get("targets", [])
            if str(target).strip()
        ]
        if item_id and status == "OPEN" and targets != ["EXTERNAL"]:
            ids.append(item_id)
    return sorted(set(ids))


def _v4_create_targets_schema_for_role(role: str) -> dict:
    allowed_targets = _v4_allowed_create_targets_for_role(role)
    internal_targets = [target for target in allowed_targets if target != "EXTERNAL"]
    return {
        "anyOf": [
            {
                "type": "array",
                "minItems": 1,
                "items": {"enum": internal_targets},
            },
            {
                "type": "array",
                "minItems": 1,
                "maxItems": 1,
                "items": {"enum": ["EXTERNAL"]},
            },
        ]
    }


def _v4_allowed_create_targets_for_role(role: str) -> list[str]:
    current_target = str(role).strip().upper()
    base_targets = ["PRODUCT", "GROWTH", "TECH", "ALL", "EXTERNAL"]
    if current_target not in {"PRODUCT", "GROWTH", "TECH"}:
        return base_targets
    return [target for target in base_targets if target != current_target]


def _v4_allows_create_operations(mode_label: str) -> bool:
    return str(mode_label).strip().lower() not in {
        "candidate_rewrite",
        "finalization",
        "item_resolution",
    }


def _load_v4_blackboard_schema() -> dict:
    return json.loads(_load_v4_prompt_file("contracts", "blackboard_operations.schema.json"))


def _load_v4_prompt_file(*parts: str) -> str:
    prompt_path = Path(__file__).resolve().parent / "prompts V4"
    for part in parts:
        prompt_path = prompt_path / part
    return prompt_path.read_text(encoding="utf-8").strip()


def _open_items_for_role(workspace, target: str) -> list[dict]:
    normalized_target = target.strip().upper()
    return list_items(workspace, target=normalized_target, status="OPEN")


def _format_document_context(title: str, text: str) -> str:
    body = text.strip() or "_Aucun contenu._"
    return "\n".join(
        [
            f"Context document: {title}",
            "---",
            body,
            "---",
            f"End context document: {title}",
        ]
    )


def _format_summary_context(title: str, summary: dict) -> str:
    if not summary:
        return "\n".join(
            [
                f"Summary context: {title}",
                "---",
                "_Aucun résumé._",
                "---",
                f"End summary context: {title}",
            ]
        )
    lines = [
        f"Summary context: {title}",
        "---",
        f"- Source document: {summary.get('source_document', '')}",
        f"- Source hash: {summary.get('source_hash', '')}",
        f"- Scope: {summary.get('scope', '')}",
        "- Key decisions:",
    ]
    lines.extend(f"  - {item}" for item in summary.get("key_decisions", []) or ["None"])
    lines.append("- Unresolved questions:")
    lines.extend(f"  - {item}" for item in summary.get("unresolved_questions", []) or ["None"])
    lines.append("- Critical risks:")
    lines.extend(f"  - {item}" for item in summary.get("critical_risks", []) or ["None"])
    lines.extend(["---", f"End summary context: {title}"])
    return "\n".join(lines)


def _format_open_items_context(workspace, items: list[dict]) -> str:
    if not items:
        return "\n".join(
            [
                "Open items context",
                "---",
                "- None",
                "---",
                "End open items context",
            ]
        )
    lines = ["Open items context", "---"]
    for item in items:
        lines.extend(_format_single_item_context(item))
    lines.extend(["---", "End open items context"])
    return "\n".join(lines)


def _format_items_context(title: str, items: list[dict]) -> str:
    if not items:
        return "\n".join(
            [
                f"Items context: {title}",
                "---",
                "- None",
                "---",
                f"End items context: {title}",
            ]
        )
    lines = [f"Items context: {title}", "---"]
    for item in items:
        lines.extend(_format_single_item_context(item))
    lines.extend(["---", f"End items context: {title}"])
    return "\n".join(lines)


def _format_single_item_context(item: dict) -> list[str]:
    targets = ", ".join(item.get("targets", [])) or "None"
    tags = ", ".join(item.get("tags", [])) or "None"
    return [
        "Read-only blackboard item:",
        f"Item id: {item['id']}",
        f"Type: {item['type']}",
        f"Priority: {item['priority']}",
        f"Status: {item['status']}",
        f"Author: {item['author']}",
        f"Targets: {targets}",
        f"Tags: {tags}",
        f"Title: {item['title']}",
        f"Content: {item['content']}",
        "",
    ]


def _append_v4_log(workspace, agent: str, event: str, source: str, details: str = "") -> None:
    entry = {
        "agent": agent,
        "event": event,
        "source": source,
    }
    if details:
        entry["details"] = details
    append_activity_log_entry(workspace, entry)


def _record_v4_stage(workspace, stage: str, document_path: Path, agent_output: dict) -> None:
    _append_v4_log(
        workspace,
        "orchestrator",
        stage,
        "app/orchestrator.py",
        (
            f"document={document_path.name}; "
            f"items_to_create={len(agent_output.get('items_to_create', []))}; "
            f"items_to_update={len(agent_output.get('items_to_update', []))}"
        ),
    )


def _group_items_by_owner(items: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {"product": [], "growth": [], "tech": []}
    for item in items:
        owners = _owners_for_targets(item.get("targets", []))
        for owner in owners:
            grouped.setdefault(owner, []).append(item)
    return grouped


def _owners_for_targets(targets: list[str] | tuple[str, ...] | str) -> list[str]:
    if isinstance(targets, str):
        raw_targets = [targets]
    else:
        raw_targets = list(targets)
    normalized_targets = [str(value).strip().upper() for value in raw_targets if str(value).strip()]
    owners: list[str] = []
    if "ALL" in normalized_targets:
        return ["product", "growth", "tech"]
    if "PRODUCT" in normalized_targets:
        owners.append("product")
    if "GROWTH" in normalized_targets:
        owners.append("growth")
    if "TECH" in normalized_targets:
        owners.append("tech")
    return owners
