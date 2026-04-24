from pathlib import Path

from llm import call_llm


def _load_product_prompt() -> str:
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "product_prompt.md"
    return prompt_path.read_text(encoding="utf-8").strip()


def _build_initial_user_prompt(blackboard: dict) -> str:
    return f"Project brief:\n{blackboard['project_brief']}"


def _build_revision_user_prompt(blackboard: dict) -> str:
    return (
        f"Project brief:\n{blackboard['project_brief']}\n\n"
        f"Current PRD draft:\n{blackboard['prd_draft']}\n\n"
        f"Architecture notes:\n{blackboard['architecture_notes']}\n\n"
        f"GTM notes:\n{blackboard['gtm_notes']}\n\n"
        "Revise the PRD using the tech and growth review. "
        "Keep the result focused, consistent, and ready for the next step."
    )


def run_product_agent(blackboard: dict) -> dict:
    """Generate the PRD draft from the shared blackboard."""
    system_prompt = _load_product_prompt()
    user_prompt = _build_initial_user_prompt(blackboard)

    prd_draft = call_llm(system_prompt, user_prompt)
    blackboard["prd_draft"] = prd_draft
    blackboard["prd_draft_initial"] = prd_draft
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "prd_draft_generated",
            "source": "app/agents/product_agent.py",
        }
    )
    return blackboard


def run_product_revision(blackboard: dict) -> dict:
    """Revise the PRD draft after tech and growth review."""
    system_prompt = _load_product_prompt()
    user_prompt = _build_revision_user_prompt(blackboard)

    revised_prd_draft = call_llm(system_prompt, user_prompt)
    blackboard["revision_trace"] = {
        "initial_prd_draft": blackboard["prd_draft_initial"],
        "tech_input": blackboard["architecture_notes"],
        "growth_input": blackboard["gtm_notes"],
        "revision_summary": (
            "Updated the PRD after tech and growth review to align scope, "
            "technical constraints, and go-to-market guidance."
        ),
    }
    blackboard["prd_draft"] = revised_prd_draft
    blackboard["activity_log"].append(
        {
            "agent": "product_agent",
            "event": "prd_draft_revised",
            "source": "app/agents/product_agent.py",
        }
    )
    return blackboard
