def create_blackboard(project_brief: str = "", project_brief_source: str = ""):
    """Create a fresh shared blackboard for the V1 workflow."""
    return {
        "project_brief": project_brief,
        "project_brief_source": project_brief_source,
        "prd_draft": "",
        "prd_draft_initial": "",
        "architecture_notes": "",
        "gtm_notes": "",
        "revision_trace": {
            "initial_prd_draft": "",
            "tech_input": "",
            "growth_input": "",
            "revision_summary": "",
        },
        "open_questions": [],
        "risks": [],
        "decisions": [],
        "conflicts": [],
        "activity_log": [],
    }
