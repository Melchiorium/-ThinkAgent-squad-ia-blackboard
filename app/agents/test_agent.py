from llm import call_llm


def run_test_agent(blackboard: dict) -> dict:
    """Generate one PRD draft from the project brief."""
    system_prompt = (
        "You are a concise product agent. "
        "Write a short PRD draft from the given project brief."
    )
    user_prompt = f"Project brief:\n{blackboard['project_brief']}"

    prd_draft = call_llm(system_prompt, user_prompt)
    blackboard["prd_draft"] = prd_draft
    blackboard["activity_log"].append(
        {"agent": "test_agent", "event": "prd_draft_generated"}
    )
    return blackboard
