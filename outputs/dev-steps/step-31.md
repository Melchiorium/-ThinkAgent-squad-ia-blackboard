# Step 31

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Turn the current correction loop into a solution-oriented loop: for each priority problem, the relevant agent should propose 1 to 2 concrete resolution options, then Product should explicitly arbitrate and continue the PRD from the chosen hypothesis.

## Files concerned
- `app/orchestrator.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/blackboard.py`
- any helper used for correction-task generation, loop storage, or blackboard rendering

## Architect scope
- no prompt rewrite in this step unless strictly required later
- prefer evolving the existing correction loop rather than adding a parallel loop
- focus on workflow and state handling first

## Context
Across the latest 5 project runs:
- problems are often identified correctly
- but they remain too often unresolved
- the loop is good at surfacing gaps
- it is weaker at converting those gaps into concrete, arbitrated solutions

Typical examples:
- `CareSync`: compliance boundary, permission model, notification fallback, messaging in/out of MVP
- `LocalLoop`: redemption mechanism, merchant threshold, partner channel
- `Melody`: city/scene choice, scoring simplification, safety/moderation
- `SkillBridge`: legal frame, verification, dispute handling
- `simple`: humor validation, local launch zone, safety/moderation

The system should not stop at:
- "this remains unclear"

It should move to:
- "here are 1 to 2 concrete ways to close this"
- "here is the option Product chose"

But it should also be allowed to conclude:
- "no credible solution yet"
- "more information is required before arbitrating"

## Required behavior
- keep the current limited correction loop structure
- but change the unit of work from:
  - generic gap correction
to:
  - solution proposal on the priority problem
- Product should then arbitrate explicitly and continue from the chosen hypothesis

## Expected implementation
1. Keep selecting a small number of priority problems per loop:
   - ideally 2 to 3 max
2. For each selected problem, build a solution task that asks the owner agent to provide:
   - `Option A`
   - `Option B` (optional if no credible second option)
   - short tradeoff / risk of each
   - recommended option
   - or, if no credible option exists yet:
     - `No viable solution yet`
     - `Required information`
3. Store these solution proposals in the blackboard in a structured way.
4. When Product re-runs, include those proposed options explicitly in its input.
5. Require Product to arbitrate:
   - chosen option
   - rejected option if relevant
   - what this changes in scope / architecture / GTM assumptions
6. Reflect that arbitration in the blackboard and in the final PRD revision.

## Suggested output shape for solution proposals
For each priority problem:
- `Problem`
- `Owner`
- `Option A`
- `Option B`
- `Tradeoffs`
- `Recommended Option`

If no credible solution exists yet:
- `No Viable Solution Yet`
- `Why`
- `Required Information`
- `Suggested Next Validation`

Then Product should record:
- `Chosen Option`
- `Reason`
- `Impact on MVP`

Or, when no option is good enough:
- `Decision: unresolved`
- `Reason`
- `Information required before decision`

## Important workflow principle
Do not ask all agents to rewrite their whole document again just to respond to one unresolved issue.

Prefer:
- targeted solution proposals
- then Product arbitration
- then one revised PRD pass

Do not force artificial solutions when the real answer is:
- the issue cannot be closed responsibly yet
- more field, legal, technical, or operating information is needed

## Acceptance criteria
- correction loop no longer only reformulates gaps
- at least some unresolved issues are transformed into concrete solution options
- Product receives explicit alternatives to choose from
- the system can also explicitly state that no relevant solution is available yet
- missing information is made explicit instead of being buried in generic open questions
- the blackboard shows both:
  - proposed solutions
  - chosen solution
  - or required information when no solution is yet credible
- test runs completed on:
  - `CareSync`
  - `LocalLoop`
  - ideally one harder case like `Melody`

## Out of scope
- redesigning all prompts immediately
- changing the number of agents
- replacing the whole workflow
- making every issue auto-resolved in one pass

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the next gain should come from better problem resolution, not from identifying more gaps
- the existing loop is the right place to evolve this behavior

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] test runs completed
- [x] ready for next step

## Notes
- The correction loop now asks Tech/Growth for concrete solution options and Product for an explicit solution arbitration before continuing the PRD.
