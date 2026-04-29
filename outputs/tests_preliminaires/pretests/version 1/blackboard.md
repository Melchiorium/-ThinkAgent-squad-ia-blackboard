# Blackboard

## Project Brief

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

## Project Brief Source

dev-agents/architect-context.md

## Initial PRD

# PRD: Minimal Python AI Squad Application v1 Prototype

## Product Problem
The lack of a structured and collaborative process for defining product roadmaps, technical proposals, and go-to-market strategy leads to inefficiencies in product development.

## Target Users
### Key Stakeholders:
- Product Managers
- Software Engineers
- Marketing Executives

### User Needs:
- A transparent tool that helps teams align their efforts around a single output.
- A straightforward workflow for role-based collaboration (product, tech, growth).
- Automated generation of PRD, technical notes, and GTM strategy.

## Expected Value
The AI Squad application will streamline the product development cycle by enabling:
- Faster and more coordinated decision-making within the team.
- Consistent production of high-quality project documentation.
- Reduced dependency on individual expertise, making processes accessible to all team members.

## Core Workflow
1. **Load Project Brief**: Initial input from the user specifying project details.
2. **Product Agent**: Generates a preliminary PRD draft.
3. **Tech Agent**: Reviews the PRD and provides technical insights and constraints.
4. **Growth Agent**: Offers go-to-market strategies based on the proposed product.
5. **Consolidation**: The Orchestrator merges inputs from all agents to finalize outputs.

## First Version Scope
### Minimum Requirements:
- Basic project structure with entry points (`main.py`, `orchestrator.py`, `blackboard.py`, `agents/`).
- Shared blackboard defined in Python as a dictionary.
- Simple implementation of the three core agents: Product, Tech, and Growth.
- Explicit orchestrator that manages agent turns and consolidates outputs.
- Minimum output files: PRD, Technical Notes, GTM Notes.

### Optional Enhancements:
- Export to JSON format for blackboard and activity logs.
- Basic version of each agent with hardcoded logic for testing.

## Key Constraints and Risks
### Constraints:
- **Language**: Python
- **Memory Model**: Shared blackboard centrally owned
- **Cost Sensitivity**: Low-cost architecture
- **Tooling Preference**: Easy editing from VS Code

### Risks:
- Complexity in managing state across multiple agents
- Ensuring clarity and transparency in the workflow process
- Handling potential conflicts or contradictions between agents

## Implementation Philosophy
Focus on simplicity, readability, and ease of debugging. Each agent should have a clear responsibility, and the overall system should remain understandable to junior developers.

## Initial Implementation Path
1. Setup project with essential files.
2. Implement basic blackboard structure.
3. Create utility functions for blackboard interactions.
4. Develop one test agent with hardcoded logic.
5. Introduce the Product Agent's functionality.
6. Follow same steps for Tech and Growth Agents.
7. Implement orchestrator to manage agent turns and consolidation.
8. Add output export functionality.
9. Clean up and document the code.

## V0 Milestone
Create a minimal end-to-end test version with:
- One hardcoded brief.
- One temporary test agent.
- Write to blackboard once.
- Export one text file.

**Success Condition for V0:** Code runs locally, one model call succeeds, and output file is generated.

## V1 Success Criteria
The system should meet the following criteria:
- All three required agents exist and operate through shared state.
- The orchestrator controls execution of agent turns.
- Outputs are generated locally and in a readable format.
- Architecture remains understandable by a junior developer.

## Tech Input

### Minimal Project Skeleton

#### `main.py`
```python
from orchestrator import Orchestrator
from blackboard import Blackboard, load_project_brief

def main():
    project_brief = load_project_brief("path/to/project_brief.txt")
    blackboard = Blackboard(project_brief)
    orchestrator = Orchestrator(blackboard)
    
    orchestrator.run()
    blacklist_outputs_to_files(orchestrator.blackboard)

if __name__ == "__main__":
    main()
```

#### `blackboard.py`
```python
def load_project_brief(path):
    with open(path, 'r') as file:
        return file.read()

class Blackboard:
    def __init__(self, project_brief):
        self.state = {
            "project_brief": project_brief,
            "prd_draft": "",
            "architecture_notes": "",
            "gtm_notes": "",
            "open_questions": [],
            "risks": [],
            "decisions": [],
            "conflicts": [],
            "activity_log": []
        }

    def read_state(self):
        return self.state

    def write_state(self, key, value):
        if hasattr(self.state, key):
            self.state[key] = value
```

### Test Agent Implementation

#### `agents/test_agent.py`
```python
class TestAgent:
    def run(self, blackboard):
        blackboard.write_state("prd_draft", "Test PRD Draft")
        blackboard.write_state("architecture_notes", "Test Architecture Notes")
        blackboard.write_state("gtm_notes", "Test GTM Notes")

def run(agent, blackboard):
    agent.run(blackboard)
```

### Orchestrator Implementation

#### `orchestrator.py`
```python
from agents.test_agent import TestAgent

class Orchestrator:
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.agents = [TestAgent()]

    def run(self):
        for agent in self.agents:
            agent.run(self.blackboard)
```

### Output Export Functionality

#### `main.py` (modified)
```python
import json

def blacklist_outputs_to_files(blackboard):
    with open("outputs/prd.txt", "w") as f:
        f.write(blackboard.state["prd_draft"])
    
    with open("outputs/architecture.txt", "w") as f:
        f.write(blackboard.state["architecture_notes"])

    with open("outputs/gtm.txt", "w") as f:
        f.write(blackboard.state["gtm_notes"])
    
    # Optional: exporting blackboard
    with open("outputs/blackboard.json", "w") as f:
        json.dump(blackboard.state, f)
        
    # Optional: exporting activity log
    if blackboard.state["activity_log"]:
        with open("outputs/activity_log.txt", "w") as f:
            for item in blackboard.state["activity_log"]:
                f.write(f"{item}\n")
```

### Initial Validation

Run the above code to validate the minimal end-to-end test version. Ensure that it meets the V0 success criteria.

Next step is to implement and integrate the Product, Tech, Growth agents in a similar manner as the Test Agent.

## Growth Input

## Go-to-Market Notes

### Value Proposition
Improve your team's productivity and output consistency with a structured, collaborative AI-driven tool for product development.

### Likely Audience
- Product Managers
- Software Engineers
- Marketing Executives
- Project Teams

### First Distribution Angle
GitHub Repository: Share the project on GitHub and invite interested teams to try it. Highlight open-source credentials and ease of setup.

### Adoption and Activation Ideas
- Run a series of webinars showcasing the tool's capabilities.
- Host user testing sessions to gather feedback and refine the product.
- Offer tutorials and guides for beginners to get started quickly.

### Simple Positioning
"AI-Accelerated Collaboration: Rapidly Draft PRD, Technical Notes, and GTM Strategy."

### Early Growth Risks
- Complexity in managing cross-agent communication and coordination.
- Ensuring all three required agents operate as designed.
- User resistance due to perceived complexity of AI integration.

---

## Final Revised PRD

# PRD: Minimal Python AI Squad Application v1 Prototype

## Product Problem
Lack of a structured and collaborative process for defining product roadmaps, technical proposals, and go-to-market strategy leads to inefficiencies in product development.

## Target Users
### Key Stakeholders:
- Product Managers
- Software Engineers
- Marketing Executives

### User Needs:
- Transparent tool that helps teams align their efforts around a single output.
- Straightforward workflow for role-based collaboration (product, tech, growth).
- Automated generation of PRD, technical notes, and GTM strategy.

## Expected Value
The AI Squad application will streamline the product development cycle by enabling:
- Faster and more coordinated decision-making within the team.
- Consistent production of high-quality project documentation.
- Reduced dependency on individual expertise, making processes accessible to all team members.

## Core Workflow
1. **Load Project Brief**: Initial input from the user specifying project details.
2. **Product Agent**: Generates a preliminary PRD draft.
3. **Tech Agent**: Reviews the PRD and provides technical insights and constraints.
4. **Growth Agent**: Offers go-to-market strategies based on the proposed product.
5. **Consolidation**: The Orchestrator merges inputs from all agents to finalize outputs.

## First Version Scope
### Minimum Requirements:
- Basic project structure with entry points (`main.py`, `orchestrator.py`, `blackboard.py`, `agents/`).
- Shared blackboard defined in Python as a dictionary.
- Simple implementation of the three core agents: Product, Tech, and Growth.
- Explicit orchestrator that manages agent turns and consolidates outputs.
- Minimum output files: PRD, Technical Notes, GTM Notes.

### Optional Enhancements:
- Export to JSON format for blackboard and activity logs.
- Basic version of each agent with hardcoded logic for testing.

## Key Constraints and Risks
### Constraints:
- **Language**: Python
- **Memory Model**: Shared blackboard centrally owned
- **Cost Sensitivity**: Low-cost architecture
- **Tooling Preference**: Easy editing from VS Code

### Risks:
- Complexity in managing state across multiple agents
- Ensuring clarity and transparency in the workflow process
- Handling potential conflicts or contradictions between agents

## Implementation Philosophy
Focus on simplicity, readability, and ease of debugging. Each agent should have a clear responsibility, and the overall system should remain understandable to junior developers.

## Initial Implementation Path
1. Setup project with essential files.
2. Implement basic blackboard structure.
3. Create utility functions for blackboard interactions.
4. Develop one test agent with hardcoded logic.
5. Introduce the Product Agent's functionality.
6. Follow same steps for Tech and Growth Agents.
7. Implement orchestrator to manage agent turns and consolidation.
8. Add output export functionality.
9. Clean up and document the code.

## V0 Milestone
Create a minimal end-to-end test version with:
- One hardcoded brief.
- One temporary test agent.
- Write to blackboard once.
- Export one text file.

**Success Condition for V0:** Code runs locally, one model call succeeds, and output file is generated.

## V1 Success Criteria
The system should meet the following criteria:
- All three required agents exist and operate through shared state.
- The orchestrator controls execution of agent turns.
- Outputs are generated locally and in a readable format.
- Architecture remains understandable by a junior developer.

---

# Minimal Project Skeleton Implementation

### `main.py`
```python
from orchestrator import Orchestrator
from blackboard import Blackboard, load_project_brief

def main():
    project_brief = load_project_brief("path/to/project_brief.txt")
    blackboard = Blackboard(project_brief)
    orchestrator = Orchestrator(blackboard)
    
    orchestrator.run()
    write_outputs_to_files(orchestrator.blackboard)

if __name__ == "__main__":
    main()
```

#### `blackboard.py`
```python
def load_project_brief(path):
    with open(path, 'r') as file:
        return file.read()

class Blackboard:
    def __init__(self, project_brief):
        self.state = {
            "project_brief": project_brief,
            "prd_draft": "",
            "architecture_notes": "",
            "gtm_notes": "",
            "open_questions": [],
            "risks": [],
            "decisions": [],
            "conflicts": [],
            "activity_log": []
        }

    def read_state(self):
        return self.state

    def write_state(self, key,value):
        if hasattr(self.state, key):
            self.state[key] = value
```

### Test Agent Implementation

#### `agents/test_agent.py`
```python
class ProductAgent:
    def run(self, blackboard):
        blackboard.write_state("prd_draft", "Test PRD Draft")
        blackboard.write_state("activity_log", ["Product agent ran"])

def run(agent, blackboard):
    agent.run(blackboard)
```

### Orchestrator Implementation

#### `orchestrator.py`
```python
from agents.product_agent import ProductAgent

class Orchestrator:
    def __init__(self, blackboard):
        self.blackboard = blackboard
        self.agents = [ProductAgent()]

    def run(self):
        for agent in self.agents:
            agent.run(self.blackboard)
```

### Output Export Functionality

#### `main.py` (modified)
```python
import json

def write_outputs_to_files(blackboard):
    with open("outputs/prd.txt", "w") as f:
        f.write(blackboard.state["prd_draft"])
    
    with open("outputs/architecture_notes.txt", "w") as f:
        f.write(blackboard.state["architecture_notes"])

    with open("outputs/gtm_notes.txt", "w") as f:
        f.write(blackboard.state["gtm_notes"])
    
    # Optional: exporting blackboard
    with open("outputs/blackboard.json", "w") as f:
        json.dump(blackboard.state, f)
        
    # Optional: exporting activity log
    if blackboard.state["activity_log"]:
        with open("outputs/activity_log.txt", "w") as f:
            for item in blackboard.state["activity_log"]:
                f.write(f"{item}\n")
```

### Initial Validation

Run the above code to validate the minimal end-to-end test version. Ensure that it meets the V0 success criteria.

Next step is to implement and integrate the Tech, Growth agents in a similar manner as the Product Agent.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Open Questions

_Aucune question._

## Risks

_Aucun risque._

## Decisions

_Aucune décision._

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
