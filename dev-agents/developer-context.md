# developer-context.md

## Project summary

This project is a local Python application.

Goal: simulate a 3-agent AI squad that collaborates through a shared structured state called `blackboard`.

The 3 domain agents are:
- Product
- Tech
- Growth

A central orchestrator controls execution order.

There is no GUI.
There is no frontend.
Outputs are local files.

## Core architecture

Main parts of the project:
- `main.py`: entrypoint
- `orchestrator.py`: execution flow
- `blackboard.py`: shared state
- `agents/product_agent.py`
- `agents/tech_agent.py`
- `agents/growth_agent.py`
- `prompts/*.txt`
- `outputs/`

## Blackboard

The `blackboard` is the shared structured state of the system.

Agents do not freely chat with each other in V1.
They read from and write to the blackboard.
The orchestrator decides when each agent runs.

Suggested initial blackboard shape:

'''python
blackboard = {
    "project_brief": "",
    "prd_draft": "",
    "architecture_notes": "",
    "gtm_notes": "",
    "open_questions": [],
    "risks": [],
    "decisions": [],
    "conflicts": [],
    "activity_log": []
}'''

## Development style

* Python only
* modular but minimal
* explicit orchestration
* beginner-friendly code
* readable and easy to modify
* no overengineering
* no unnecessary dependencies
* no deep abstraction unless clearly needed

## Working mode

You do not define architecture.
You implement the current assigned task only.
Architecture comes from:

* initial-briefing.md
* Architect handoff
* existing codebase