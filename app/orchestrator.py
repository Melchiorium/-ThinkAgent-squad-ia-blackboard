from blackboard import create_blackboard
from agents.product_agent import run_product_agent, run_product_revision
from agents.tech_agent import run_tech_agent
from agents.growth_agent import run_growth_agent


def run_v0_flow(project_brief: str, project_brief_source: str) -> dict:
    """Run the four-pass flow and return the updated blackboard."""
    blackboard = create_blackboard(project_brief, project_brief_source)
    blackboard = run_product_agent(blackboard)
    blackboard = run_tech_agent(blackboard)
    blackboard = run_growth_agent(blackboard)
    blackboard = run_product_revision(blackboard)
    return blackboard
