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