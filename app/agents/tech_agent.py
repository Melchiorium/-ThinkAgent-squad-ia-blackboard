from pathlib import Path

from llm import call_llm


def _load_tech_prompt() -> str:
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "tech_prompt.md"
    return prompt_path.read_text(encoding="utf-8").strip()


def run_tech_agent(blackboard: dict) -> dict:
    """Generate architecture notes from the shared blackboard."""
    system_prompt = _load_tech_prompt()
    user_prompt = (
        f"Project brief:\n{blackboard['project_brief']}\n\n"
        f"PRD draft:\n{blackboard['prd_draft']}"
    )

    architecture_notes = call_llm(system_prompt, user_prompt)
    blackboard["architecture_notes"] = architecture_notes
    blackboard["activity_log"].append(
        {
            "agent": "tech_agent",
            "event": "architecture_notes_generated",
            "source": "app/agents/tech_agent.py",
        }
    )
    return blackboard
