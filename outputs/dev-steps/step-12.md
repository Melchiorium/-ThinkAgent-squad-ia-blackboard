# Step 12

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Strengthen the final arbitration phase so Product explicitly decides what is retained, deferred, rejected, or left open after Tech and Growth contributions.

## Files concerned
- `app/blackboard.py`
- `app/agents/product_agent.py`
- `app/main.py`

## Required behavior
- extend the blackboard so final arbitration is explicit, not only implicit in the revised PRD
- add structured fields to distinguish:
  - retained decisions
  - deferred decisions
  - rejected recommendations
  - open points still unresolved
- make Product responsible for writing those fields during the final synthesis pass
- Product must no longer act only as a synthesizer of inputs
- Product must explicitly arbitrate Tech and Growth recommendations and record the outcome
- update `blackboard.md` so a human reader can clearly understand:
  - what Tech proposed
  - what Growth proposed
  - what Product retained
  - what Product deferred
  - what Product rejected
  - what remains open
- keep the final PRD focused on the chosen product framing, while the blackboard preserves the decision trace

## Workflow direction to implement
1. Product creates the initial framing.
2. Tech contributes architecture and feasibility recommendations.
3. Growth contributes GTM and adoption recommendations.
4. Product performs a final arbitration pass.
5. Product records structured decision outcomes in the blackboard.
6. The final PRD reflects retained decisions only.
7. `blackboard.md` exposes the full arbitration trace for human reading.

## Constraints
- preserve the current blackboard architecture
- preserve explicit orchestration
- do not introduce direct agent-to-agent chat
- keep Product as the single owner of final arbitration
- keep data structures plain and explicit
- do not add unnecessary abstraction or framework logic

## Acceptance criteria
- the blackboard explicitly distinguishes retained, deferred, rejected, and still-open items
- Product writes those outcomes during the final pass
- `blackboard.md` becomes clearer as a decision-trace artifact
- `prd.md` is cleaner because only retained decisions should affect it
- the workflow remains simple and understandable

## Out of scope
- changing the model provider
- redesigning all prompts in this step unless strictly needed
- changing the three-agent architecture
- adding new agents
- adding frontend or GUI work

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- the next gain comes from explicit decision traceability
- the system already produces better collaboration signals; it now needs clearer arbitration semantics
- Product should be the visible decision maker in the blackboard, not just the author of the final PRD

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- This step is about decision structure and arbitration clarity, not about adding more content.
