import re
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
    from .readiness import aggregate_global_readiness
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
    from readiness import aggregate_global_readiness


def run_v0_flow(
    project_brief: str,
    project_brief_source: str,
    progress_callback=None,
    step_timeout_seconds: int | None = None,
) -> dict:
    """Run the staged collaboration flow and return the updated blackboard."""
    blackboard = create_blackboard(project_brief, project_brief_source)
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
    blackboard = _finalize_readiness(blackboard)
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
        if tasks_by_owner["growth"]:
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
        if correction_tasks:
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
