# Step Final Codex

## Status
- [x] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Document the final development work performed after the `V12-like` rollback, without reopening the implementation history in detail.

The goal of this step is to leave a senior developer with a clear picture of the final technical adjustments, retained decisions, rejected experiments, and current baseline.

## Context
The project had reached a good baseline around the `V12-like` workflow:
- Product creates the initial framing
- Growth challenges market and launch logic
- Tech challenges feasibility and architecture
- Product arbitrates
- readiness and targeted correction remain bounded
- Product locking protects scope

Several later workflow experiments improved internal sophistication but degraded final deliverable quality. The final work therefore focused on preserving the simple baseline while improving artifacts, context, and documentation.

## Main Developments Performed

### 1. Mermaid architecture output
Replaced the former architecture visual path based on `Diagram Blueprint` / PDF with a Mermaid-based output.

Current output contract:
- Tech produces a Mermaid diagram section
- runtime extracts the Mermaid source
- `architecture-diagram.mmd` is written as the source artifact
- `architecture-diagram.png` is generated when Mermaid CLI is available
- `architecture.pdf` is no longer generated in new batches

Relevant files:
- `app/agents/tech_agent.py`
- `app/architecture_render.py`
- `app/main.py`
- `app/blackboard.py`
- `app/prompts V3/tech_prompt.md`
- `package.json`
- `package-lock.json`
- `mermaid-puppeteer-config.json`
- `.gitignore`

Senior note:
- the Mermaid requirement is not only an output-format change
- it also nudges Tech toward clearer component and flow decomposition
- keep this if future runs continue to produce useful technical framing

### 2. Removal of active team-prompt behavior
Removed the active `team_prompt` experiment from the validated V3 runtime path.

Reason:
- team-level context looked reasonable, but weakened role sharpness in practice
- the best results came from specialized agent prompts and explicit workflow handoffs

Retained principle:
- collaboration should be carried by the blackboard and orchestrator
- agent prompts should stay role-specific

Relevant files:
- `app/orchestrator.py`
- `app/prompts V3/product_prompt.md`
- `app/prompts V3/growth_prompt.md`
- `app/prompts V3/tech_prompt.md`

### 3. Paris / France deployment assumption
Added a generic deployment assumption to V3 agent prompts:

`The projects will be implemented in France, in the city of Paris.`

Reason:
- many recurring gaps were caused by unknown geography, regulation, privacy context, or launch area
- this was not project-specific optimization
- it gave Product, Growth, and Tech a stable execution context

Observed effect:
- stronger legal, privacy, local-market, density, and GTM reasoning
- better results across CareSync, LocalLoop, Melody, and SkillBridge

Relevant files:
- `app/prompts V3/product_prompt.md`
- `app/prompts V3/growth_prompt.md`
- `app/prompts V3/tech_prompt.md`

### 4. Evaluator split clarified
Clarified and used two different evaluator postures:

Quality evaluator:
- judges the quality of Product, Tech, Growth, collaboration, and deliverables
- does not decide whether the startup deserves investment

CEO evaluator:
- judges business viability, profitability, execution complexity, GTM realism, competitive risk
- produces `APPROVE`, `REVISE`, or `REJECT`

Relevant files:
- `app/evaluations/evaluator_quality.md`
- `app/evaluations/evaluator_prompt.md`
- generated `evaluation-quality.md`
- generated `evaluation-CEO.md`

### 5. Human clarification idea documented but not retained
An optional human clarification loop was explored conceptually:
- generate a few high-impact questions from unresolved gaps
- let a human answer them
- inject answers into a later run

This was not retained as active runtime behavior in the final baseline.

Reason:
- promising, but outside the final time box
- requires its own user workflow and test campaign
- should remain documented as a future direction, not an active feature

Relevant documentation:
- `outputs/workflow.md`
- `outputs/rapport_final.md`

### 6. Final documentation pass
Cleaned and restructured the project history into a final report.

The final report now covers:
- project constraints and 48h POC framing
- technology choice
- no-code/framework/custom Python tradeoff
- blackboard and handoff model
- complementary Architecte-Dev system
- model evolution: Ollama, Gemini, OpenAI
- prompt evolution: V2, V3
- readiness and correction loop
- workflow overengineering lessons
- Mermaid output
- Paris / France assumption
- evaluator quality vs evaluator CEO
- human clarification as future track
- incident around lost test history

Relevant files:
- `outputs/rapport_final.md`
- `outputs/workflow.md`
- `outputs/architecte-dev.md`

## Test Runs Performed
Final validation runs were performed on:
- `CareSync`
- `LocalLoop`
- `Melody`
- `SkillBridge`

Recent generated outputs include:
- `prd.md`
- `architecture.md`
- `architecture-diagram.mmd`
- `architecture-diagram.png`
- `gtm.md`
- `blackboard.md`
- `activity_log.txt`

The output version numbering may restart at `version 1` because older local test versions were removed during a cleanup incident.

## Important Non-Goals
This final step intentionally did not:
- add a new autonomous agent
- add a new free-form swarm behavior
- keep the human clarification loop as runtime code
- reintroduce team-level prompts
- force every `LIMITED` project to become `READY`
- replace the custom Python orchestration with a framework

## Current Baseline To Preserve
Recommended baseline:
- custom Python orchestrator
- shared blackboard memory
- prompts V3
- no active team prompt
- deployment assumption: Paris, France
- Product as final arbiter
- Growth before Tech
- Tech receives GTM notes
- Mermaid architecture source and PNG output
- no architecture PDF in new batches
- readiness is useful, but `LIMITED` can be a valid result

## Senior Developer Notes
- Prefer small, isolated changes and compare on at least CareSync and LocalLoop before keeping them.
- Treat higher blackboard sophistication with suspicion unless final PRD / architecture / GTM quality also improves.
- Keep output artifacts human-readable; the system is only useful if its reasoning can be inspected.
- Do not optimize solely for evaluator score. Use quality and CEO evaluations as complementary signals.
- If human clarification is revisited, implement it as a separate, explicit workflow rather than hiding it inside agent prompts.

## Completion Check
- [x] Mermaid output implemented and tested
- [x] PDF architecture output removed from future batches
- [x] team prompt experiment removed from active baseline
- [x] Paris / France context added to V3 prompts
- [x] evaluator distinction documented
- [x] final report updated
- [x] human clarification documented as future direction
- [x] project runs completed after final baseline adjustments
