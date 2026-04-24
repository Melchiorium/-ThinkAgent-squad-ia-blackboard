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