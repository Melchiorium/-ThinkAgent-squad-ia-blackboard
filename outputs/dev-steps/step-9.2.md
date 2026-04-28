# Step 9.2

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [ ] done

## Objective
Rewrite the Product, Tech, and Growth prompts so the agents act as distinct expert challengers and co-producers of the final framing deliverables: PRD, architecture proposal, and GTM plan.

## Files concerned
- `app/prompts/product_prompt.md`
- `app/prompts/tech_prompt.md`
- `app/prompts/growth_prompt.md`

## Required behavior
- rewrite `tech_prompt.md` so Tech behaves as the architecture and feasibility owner
- Tech must now produce:
  - a concrete recommended architecture proposal for the current brief
  - explicit technical choices with short rationale
  - module responsibilities and system boundaries
  - key implementation constraints
  - concrete feasibility challenges
  - architecture risks and open questions only where genuinely needed
- rewrite `growth_prompt.md` so Growth behaves as the GTM and acquisition owner
- Growth must now produce:
  - a concrete MVP GTM proposal for the current brief
  - a primary audience to prioritize first
  - a positioning angle
  - a first acquisition channel
  - a simple activation loop
  - a short set of measurable early success indicators
  - growth risks and open questions only where genuinely needed
- rewrite `product_prompt.md` so Product behaves as the product framing owner
- Product must now:
  - build the initial PRD
  - revise the final PRD after challenge from Tech and Growth
  - integrate relevant technical and GTM decisions when they affect scope, roadmap direction, constraints, rollout assumptions, or success metrics
  - keep the final PRD as a product document, not a review dump
- preserve stable headings for Tech and Growth so the structured extraction from step 9 remains possible

## Prompt design decisions to implement
- `tech_prompt.md` must move from “review comments” to “recommended architecture proposal”
- `tech_prompt.md` must bias toward one recommended approach instead of listing broad alternatives
- `tech_prompt.md` must explicitly forbid speculative full-stack sprawl unless the brief strongly requires it
- `tech_prompt.md` must ask for “recommended choice + short rationale” when a technical decision is made
- `growth_prompt.md` must move from “review comments” to “recommended GTM proposal”
- `growth_prompt.md` must bias toward one realistic GTM path for MVP instead of broad marketing brainstorming
- `growth_prompt.md` must ask for concrete near-term actions, not generic awareness ideas
- `growth_prompt.md` must require at least one concrete acquisition recommendation and one concrete activation recommendation
- `product_prompt.md` must explicitly position Product as the owner of the final PRD and roadmap direction
- `product_prompt.md` must instruct Product to absorb technical and GTM decisions into:
  - MVP scope
  - roadmap direction
  - constraints
  - launch assumptions
  - success metrics
- `product_prompt.md` must explicitly forbid copying raw review headings or review notes into the final PRD

## Constraints
- do not change orchestrator logic in this step
- do not change parsing logic in this step
- preserve the existing section anchors used by the current extraction layer
- keep prompts concise and operational
- do not overfit prompts to one single example brief
- prefer concrete defaults over open-ended brainstorming

## Acceptance criteria
- Tech prompt clearly asks for a recommended architecture proposal, not only review comments
- Growth prompt clearly asks for a recommended GTM proposal, not only review comments
- Product prompt clearly asks to integrate relevant review outcomes into the final PRD without leaking review structure
- the prompts reflect the final collaboration goal:
  - Product owns PRD and product framing
  - Tech owns architecture and feasibility
  - Growth owns GTM and acquisition
- the three prompts remain compatible with the structured blackboard workflow introduced in step 9
- a future run should be more likely to produce substantial `architecture.md` and `gtm.md` outputs, not just lists of suggestions

## Out of scope
- changing agent Python code
- changing blackboard schema
- changing rendering in `blackboard.md`
- fixing every remaining quality issue in one step

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
pending

## Architect decision
- prompt quality is now the highest-leverage bottleneck
- the next improvement should come from stronger agent guidance before touching more code
- Tech and Growth must move from “reviewers who suggest” to “specialists who recommend”
- the prompts must reflect the final target system: three distinct agents that challenge the project and produce a complete framing outcome through collaboration

## Completion check
- [ ] implementation done
- [ ] acceptance criteria met
- [ ] ready for next step

## Notes
- Keep the current extraction headings stable, but increase the expected substance behind each section.
- Architect changes already completed in this step:
  - `app/prompts/product_prompt.md` rewritten so Product owns the PRD and absorbs Tech/Growth decisions without leaking review structure into the final PRD
  - `app/prompts/tech_prompt.md` rewritten so Tech produces a concrete MVP architecture proposal with explicit choices and short rationale
  - `app/prompts/growth_prompt.md` rewritten so Growth produces a concrete MVP GTM proposal with audience, acquisition, activation, and success indicators
- Developer should treat these prompt changes as already decided and implemented.
- Developer scope from this point is code behavior only, unless a prompt/code mismatch is found during implementation.
