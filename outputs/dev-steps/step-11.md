# Step 11

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Refine the collaboration workflow so the three agents act as distinct expert contributors through the blackboard, and Product becomes the final arbiter and synthesizer of the framing output.

## Files concerned
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`

## Required behavior
- keep the current architecture principles:
  - explicit orchestrator
  - shared blackboard
  - no direct agent-to-agent conversation
- revise the workflow so each agent contributes a more clearly defined type of output to the blackboard
- define Product as:
  - owner of final product framing
  - owner of arbitration between competing inputs
  - owner of the final PRD output
- define Tech as:
  - owner of feasibility challenge
  - owner of technical framing and architecture proposal
  - contributor of constraints, technical decisions, and implementation risks
- define Growth as:
  - owner of GTM challenge
  - owner of distribution and adoption framing
  - contributor of target audience, acquisition logic, activation logic, and market risks
- update the workflow so Product does not simply merge upstream texts
- Product finalization must instead:
  - read structured inputs from Tech and Growth
  - arbitrate what is retained
  - consolidate only what is relevant to final product framing
- strengthen the blackboard as a collaboration surface by making the contribution types more explicit, especially for:
  - recommendations
  - retained decisions
  - open questions
  - risks
  - unresolved tensions between agents

## Workflow direction to implement
1. Product produces an initial product framing draft.
2. Tech challenges the draft from feasibility and architecture angles.
3. Growth challenges the draft from adoption and GTM angles.
4. Blackboard stores those contributions in role-appropriate structured areas.
5. Product performs a final arbitration pass and produces the final PRD from the blackboard state, not by copying review sections.

## Constraints
- preserve the blackboard-based collaboration model
- preserve explicit orchestration
- do not introduce autonomous free-form multi-agent chat
- keep the flow understandable by a middle developer
- avoid creating a generic agent framework
- prefer explicit role-specific fields and responsibilities over abstract meta-modeling

## Acceptance criteria
- the role of each agent in the workflow is more sharply defined in code structure and blackboard usage
- Product is clearly the final synthesizer rather than a passive merger
- Tech and Growth contribute structured expert challenge, not only narrative review
- the blackboard better reflects collaboration states such as recommendations, decisions, risks, and open tensions
- the overall workflow remains simple, explicit, and aligned with the original project brief

## Out of scope
- changing the model provider again
- redesigning prompts in this step unless required by the workflow change
- adding new agents
- adding GUI or frontend
- replacing the blackboard architecture

## Open questions
- [ ]

## Developer feedback
- [x] No prompt changes were required for this step; the workflow was clarified through blackboard structure and Product arbitration logic.

## Developer status
ready_for_review

## Architect decision
- the blackboard model is still the right architectural direction
- the next improvement is a workflow clarification, not an architecture replacement
- the system should evolve from “multiple texts passing through the orchestrator” to “structured expert contributions consolidated by Product”

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step is about role clarity and collaboration semantics more than output formatting.
- Prompts were intentionally left unchanged for this step.
