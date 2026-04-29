# architext-context.md

## Project goal

Build a local Python project that simulates a 3-agent AI squad collaborating on a shared blackboard to produce a product framing output.

The 3 required agents are:

- Product agent
- Tech agent
- Growth agent

The system must:

- accept a project brief as input;
- maintain a shared structured state called blackboard;
- orchestrate multiple agent turns in a controlled order;
- produce consolidated outputs for PRD, architecture notes, and GTM notes;
- remain simple, transparent, and explainable.

## Non-goals

Do not build a fully autonomous open-ended agent swarm.

Do not optimize for maximum sophistication.

Do not introduce unnecessary frameworks or abstractions in V1.

Do not prioritize fancy UX over clarity of architecture. 

## Primary design constraints

- Language: Python
- Priority: understandability over cleverness
- Implementation style: modular but minimal
- Orchestration style: explicit orchestrator, not emergent agent conversation
- Memory model: shared blackboard, centrally owned
- V1 target: robust minimal prototype
- Cost sensitivity: low-cost architecture
- Tooling preference: code should be easy to edit from VS Code

## V1 architecture choice

Chosen architecture: Python application with explicit orchestrator + shared blackboard.

Rationale:

- better control than opaque agent frameworks;
- more pedagogical than workflow-only solutions;
- easier to explain during project review;
- simpler to evolve later toward V2 features.

## System overview

The system contains the following main parts:

- `main.py`: entrypoint
- `orchestrator.py`: controls execution order and consolidation
- `blackboard.py`: shared state definition and update helpers
- `agents/product_agent.py`: product specialist logic
- `agents/tech_agent.py`: technical specialist logic
- `agents/growth_agent.py`: GTM specialist logic
- `prompts/*.txt`: role prompts
- `outputs/`: generated artifacts

## Blackboard concept

The blackboard is the shared structured working memory.

It is the core of the collaboration model.

Agents do not directly converse with each other in V1.

They read from and write to the blackboard.

The orchestrator decides when each agent runs and what current state it sees.

## Expected blackboard structure

Use a simple Python-native structure first. Dictionary is acceptable for V1.

Suggested initial shape:

```python
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
}
```

## Agent responsibilities

### Product agent

Owns:

- problem framing
- target users
- user needs
- scope
- feature prioritization
- PRD draft
- product roadmap direction

Must write primarily to:

- `prd_draft`
- `open_questions`
- `decisions`
- `activity_log`

### Tech agent

Owns:

- technical feasibility
- architecture proposals
- implementation constraints
- complexity trade-offs
- technical risks

Must write primarily to:

- `architecture_notes`
- `risks`
- `conflicts`
- `activity_log`

### Growth agent

Owns:

- go-to-market logic
- positioning
- acquisition channels
- launch assumptions
- traction indicators

Must write primarily to:

- `gtm_notes`
- `open_questions`
- `decisions`
- `activity_log`

## Orchestration model

V1 orchestration must be explicit and deterministic.

Recommended order:

1. load project brief
2. Product agent creates PRD v1
3. Tech agent reviews PRD and adds architecture notes
4. Growth agent reviews PRD and adds GTM notes
5. Product agent revises PRD considering prior outputs
6. orchestrator consolidates outputs
7. system writes result files to `outputs/`

## Output expectations for V1

Minimum outputs:

- `outputs/prd.txt`
- `outputs/architecture.txt`
- `outputs/gtm.txt`
- optional `outputs/blackboard.json`
- optional `outputs/activity_log.txt`

## Implementation philosophy

Prefer:

- small files;
- readable functions;
- explicit names;
- minimal hidden magic;
- easy debugging;
- structured output handling.

Avoid:

- deep inheritance;
- framework lock-in;
- unnecessary async complexity;
- speculative abstractions;
- premature optimization.

## Initial implementation path

Build in this order:

1. minimal project skeleton
2. blackboard data structure
3. basic LLM call utility
4. one test agent end-to-end
5. three real agents
6. orchestrator flow
7. output export
8. cleanup and documentation

## V0 milestone

Before building all 3 agents, create a minimal end-to-end test version with:

- one hardcoded brief;
- one temporary test agent;
- one write to blackboard;
- one exported text file.

Success condition for V0:

- code runs locally;
- one model call succeeds;
- output file is generated.

## V1 success criteria

The V1 is successful if:

- all 3 required agents exist;
- their roles are distinct;
- they operate through shared state;
- the orchestrator controls execution;
- outputs are generated locally;
- the architecture remains understandable by a junior developer.

## Coding style guidance for the AI assistant

When generating code for this project:

- keep functions short;
- explain non-obvious choices;
- avoid overengineering;
- generate code incrementally;
- prefer practical progress over theoretical completeness;
- do not redesign the whole project unless requested;
- preserve the chosen architecture unless a concrete blocking issue appears.

## Working mode expected from the AI assistant

Preferred collaboration mode:

- first propose the smallest correct step;
- then implement only that step;
- then pause for validation;
- then move to the next file.

Do not generate the whole system at once unless explicitly requested.

## Immediate next step

Generate the minimal project skeleton and implement the first blackboard version.