# Step 14

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Add a second-pass collaboration workflow based on `version 13` and the CEO evaluation, producing revised `v2` deliverables without overwriting the existing PRD, architecture, and GTM files.

## Files concerned
- `app/orchestrator.py`
- `app/blackboard.py`
- `app/agents/product_agent.py`
- `app/agents/tech_agent.py`
- `app/agents/growth_agent.py`
- `app/main.py`

## Required behavior
- use `outputs/version 13/` as the source version for this workflow
- use `outputs/evaluation-version-13.md` as an additional structured input
- do not overwrite the existing files in `outputs/version 13/`
- generate a new revised pass as `v2` artifacts derived from version 13

## Workflow to implement
1. Load the version 13 artifacts and the CEO evaluation.
2. Product performs a first revision pass based on:
   - the original version 13 brief/framing
   - the existing version 13 PRD
   - the CEO evaluation feedback
3. Tech reviews that revised Product draft and contributes updated technical challenge/recommendations.
4. Growth reviews that revised Product draft and contributes updated GTM challenge/recommendations.
5. Product performs a final arbitration and produces the final revised PRD `v2`.

## Blackboard expectations
- extend the blackboard so it can track a second-pass review cycle explicitly
- preserve:
  - original version 13 state
  - CEO feedback input
  - product revision pass before Tech/Growth review
  - final product synthesis after Tech/Growth review
- distinguish clearly between:
  - original version 13 outputs
  - revised `v2` outputs
- keep the collaboration trace readable for a human reviewer

## Output expectations
- do not overwrite:
  - `outputs/version 13/prd.md`
  - `outputs/version 13/architecture.md`
  - `outputs/version 13/gtm.md`
- produce new revised artifacts for the second pass, for example inside the same version folder:
  - `outputs/version 13/prd-v2.md`
  - `outputs/version 13/architecture-v2.md`
  - `outputs/version 13/gtm-v2.md`
  - `outputs/version 13/blackboard-v2.md`
  - `outputs/version 13/activity_log-v2.txt`
- keep the original version 13 files unchanged

## Constraints
- preserve the blackboard-based collaboration model
- preserve explicit orchestration
- do not introduce free-form agent chat
- keep Product as the owner of final arbitration
- use the CEO evaluation as an input to improve the framing, not as a replacement for agent roles
- keep the implementation understandable and explicit

## Acceptance criteria
- the workflow starts from version 13 artifacts and CEO feedback
- Product performs an initial revision before Tech and Growth intervene
- Tech and Growth review the revised Product draft, not only the original PRD
- Product performs a final arbitration pass after Tech and Growth feedback
- `v2` outputs are produced without overwriting version 13 originals
- the new collaboration trace makes the second-pass logic understandable

## Out of scope
- changing the model provider
- redesigning prompts unless strictly necessary for the new workflow
- replacing the blackboard architecture
- adding new agents
- deleting or mutating archived outputs

## Open questions
- [ ]

## Developer feedback
- [x] Second-pass v2 artifacts were generated successfully in `outputs/version 13/` without overwriting the original version 13 files.

## Developer status
ready_for_review

## Architect decision
- the CEO evaluation should trigger a structured second-pass workflow, not a simple rerun
- Product should absorb executive feedback first, then be challenged again by Tech and Growth, then arbitrate the final `v2`
- versioned outputs must remain immutable once archived

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step is specifically about revision workflow on top of an existing version, not about first-pass generation.
