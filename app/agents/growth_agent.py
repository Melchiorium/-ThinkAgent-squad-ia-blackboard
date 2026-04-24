from pathlib import Path

from llm import call_llm


def _load_growth_prompt() -> str:
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "growth_prompt.md"
    return prompt_path.read_text(encoding="utf-8").strip()


def run_growth_agent(blackboard: dict) -> dict:
    """Generate GTM notes from the shared blackboard."""
    system_prompt = _load_growth_prompt()
    user_prompt = (
        f"Project brief:\n{blackboard['project_brief']}\n\n"
        f"PRD draft:\n{blackboard['prd_draft']}"
    )

    gtm_notes = call_llm(system_prompt, user_prompt)
    blackboard["gtm_notes"] = gtm_notes
    blackboard["activity_log"].append(
        {
            "agent": "growth_agent",
            "event": "gtm_notes_generated",
            "source": "app/agents/growth_agent.py",
        }
    )
    return blackboard
