# Step 13

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Improve MVP arbitration discipline so Product retains only what is essential for the MVP, defers what is useful but not necessary now, and avoids over-enriching the final framing.

## Files concerned
- `app/prompts/product_prompt.md`
- `app/prompts/tech_prompt.md`
- `app/prompts/growth_prompt.md`
- `app/agents/product_agent.py`

## Required behavior
- tighten `product_prompt.md` so Product explicitly arbitrates recommendations with an MVP-first mindset
- Product must:
  - retain only what is necessary for MVP viability, trust, compliance, or launchability
  - defer what is useful but not essential now
  - avoid pulling detailed operational or future-phase recommendations into the final PRD
- tighten `tech_prompt.md` so Tech recommendations focus on decisions required for MVP feasibility, not on broad enhancement ideas
- tighten `growth_prompt.md` so Growth recommendations focus on launch-critical GTM choices, not on secondary launch optimizations
- update `product_agent.py` so non-retained recommendations are treated more conservatively:
  - unresolved clarifications should stay open
  - useful but non-essential items should be deferred
  - rejected recommendations should be used sparingly
- preserve the current blackboard-based workflow and structured extraction headings

## Workflow intent
1. Tech and Growth continue to challenge the project.
2. Product explicitly filters their recommendations through an MVP-now vs later lens.
3. The final PRD reflects only retained MVP-relevant decisions.
4. The blackboard preserves deferred and still-open items without forcing them into the product deliverable.

## Constraints
- do not change model provider
- do not redesign the orchestrator
- preserve the existing extraction-compatible headings in Tech and Growth outputs
- keep the implementation simple and explicit
- avoid topic-specific hardcoding tied to one single example project

## Acceptance criteria
- Product prompt explicitly encodes MVP arbitration discipline
- Tech and Growth prompts bias recommendations toward MVP-critical choices
- Product arbitration in code becomes less mechanical and more conservative
- retained decisions become more selective
- deferred and open items become more meaningful
- the final PRD is less overloaded by non-essential details

## Out of scope
- redesigning the entire blackboard
- adding new agents
- changing output rendering structure beyond what is needed for arbitration quality
- introducing a generic rules engine

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- the next improvement should come from stricter MVP discipline, not from adding more content
- Product must become a stronger arbiter of what belongs in the MVP now versus later

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- This step intentionally targets decision quality and scope discipline rather than raw output richness.
