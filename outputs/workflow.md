# Workflow

## Purpose

This project turns a project brief into a multi-agent startup dossier made of:
- `project-brief.md`
- `prd.md`
- `architecture.md`
- `architecture.pdf`
- `gtm.md`
- `blackboard.md`
- `activity_log.txt`

The system is orchestrated in Python and relies on a shared in-memory `blackboard` object passed between agents.

Main code entry points:
- [app/main.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/main.py)
- [app/orchestrator.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/orchestrator.py)
- [app/blackboard.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/blackboard.py)

## Current Baseline

The current validated baseline is a `V12-like` workflow:
- keep the `V3` prompts when running validated tests
- keep the existing readiness loop
- keep the Product locking pass
- do not use the post-`V12` solution-proposal workflow experiments

Important:
- prompt loading is versioned by `BLACKBOARD_PROMPT_VERSION`
- code default is still `V2`
- the best recent runs were obtained with `BLACKBOARD_PROMPT_VERSION=V3`

## Output Structure

Current output layout:
- `outputs/dev-steps/`
- `outputs/projects/`
- `outputs/tests/<Project>/version X/`
- `outputs/tests/pretests/`

Project briefs used for normal runs live in:
- `outputs/projects/*.md`

Normal runs are written to:
- `outputs/tests/<Project Name>/version X/`

## High-Level Architecture

There are 3 agent roles:
- `Product`
- `Tech`
- `Growth`

They do not talk directly to each other.

They collaborate through:
- the evolving `prd_draft`
- the shared `blackboard`
- a later Product arbitration pass

This is important:
- `Tech` does not read `gtm.md`
- `Growth` does not read `architecture.md`
- both mainly react to the current `prd_draft`
- `Product` is the role that sees and arbitrates both perspectives together

## Real Workflow Modes

The code currently exposes 2 real workflows.

### 1. Standard first pass

Function:
- `run_v0_flow()`

Used for:
- a fresh project brief from `outputs/projects/`

### 2. Second pass

Function:
- `run_v2_flow()`

Activated only when:
- `BLACKBOARD_WORKFLOW_MODE=second_pass`

Current limitation:
- the second pass source is still hardcoded in `app/main.py`
- it reads:
  - `outputs/version 13`
  - `outputs/evaluation-version-13.md`

So this mode exists, but is not yet generalized.

## Step 0: Brief Selection

Handled in:
- [app/main.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/main.py)

Normal run behavior:
- search in `outputs/projects/`
- load one Markdown brief
- extract a project name
- store the relative source path in the blackboard

Selection env vars:
- `BLACKBOARD_PROJECT_NAME`
- `BLACKBOARD_PROJECT_BRIEF`

If several briefs exist and no selector is given:
- the run fails explicitly

## Step 1: Blackboard Creation

Handled in:
- [app/blackboard.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/blackboard.py)

The blackboard stores:
- the input brief and its source
- working drafts
- expert contributions
- extracted expert decisions
- arbitration state
- product locking state
- readiness state
- workflow trace
- artifacts state
- risks, open questions, conflicts
- activity log

Important fields:
- `prd_draft`
- `architecture_notes`
- `diagram_blueprint`
- `gtm_notes`
- `expert_contributions`
- `expert_decisions`
- `requested_changes`
- `arbitration`
- `product_locking`
- `readiness`
- `workflow_trace`
- `activity_log`

Second-pass-only fields:
- `source_version`
- `source_artifacts`
- `executive_evaluation`
- `second_pass_trace`

## Standard First-Pass Flow

Actual order in [app/orchestrator.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/orchestrator.py):

1. `run_product_agent()`
2. `run_tech_agent()`
3. `run_growth_agent()`
4. `run_product_revision()`
5. `_finalize_readiness()`
6. `_run_targeted_correction_loop()`
7. `run_product_locking_pass()`
8. `_finalize_readiness()`

This means:
- `Tech` currently runs before `Growth`
- `Growth-before-Tech` was discussed, but is not the current implementation

## Step 2: Product Initial Draft

Handled in:
- `run_product_agent()`

Prompt:
- `app/prompts <VERSION>/product_prompt.md`

User input sent to Product:
- `Mode: initial_draft`
- `Project brief`

At this stage Product only sees:
- the brief

It produces:
- the first `prd_draft`
- a readiness block parsed from the PRD

Side effects:
- `prd_draft`
- `prd_draft_initial`
- `readiness.product`
- `activity_log += prd_draft_generated`

## Step 3: Tech Review

Handled in:
- `run_tech_agent()`

Prompt:
- `app/prompts <VERSION>/tech_prompt.md`

User input sent to Tech:
- `Mode: review` or `Mode: correction`
- `Project brief`
- `PRD draft`
- `Known reusable tags`
- optional `Targeted correction tasks`

Tech sees:
- the brief
- the current PRD
- known tags
- optional correction tasks

Tech does not see:
- `gtm.md`
- Growth decisions directly

Expected useful sections in output:
- `## Review Summary`
- `### Structural Technical Decisions`
- `## Requested Changes`
- `## Risks`
- `## Open Questions`
- `## Technical Readiness`
- optional `Diagram Blueprint`

Stored into blackboard:
- `architecture_notes`
- `diagram_blueprint`
- `expert_contributions.tech`
- `expert_decisions.tech`
- `requested_changes.tech`
- `review_summaries.tech`
- `readiness.tech`
- `risks`
- `open_questions`

Notes:
- if structured technical decisions are missing, fallback is taken from the first requested changes
- `diagram_blueprint` is later used to render `architecture.pdf`

## Step 4: Growth Review

Handled in:
- `run_growth_agent()`

Prompt:
- `app/prompts <VERSION>/growth_prompt.md`

User input sent to Growth:
- `Mode: review` or `Mode: correction`
- `Project brief`
- `PRD draft`
- `Known reusable tags`
- optional `Targeted correction tasks`

Growth sees:
- the brief
- the current PRD
- known tags
- optional correction tasks

Growth does not see:
- `architecture.md`
- Tech decisions directly

Expected useful sections in output:
- `## Review Summary`
- `### 2 to 3 Structural GTM Decisions`
- `## Requested Changes`
- `## Risks`
- `## Open Questions`
- `## GTM Readiness`

Stored into blackboard:
- `gtm_notes`
- `expert_contributions.growth`
- `expert_decisions.growth`
- `requested_changes.growth`
- `review_summaries.growth`
- `readiness.growth`
- `risks`
- `open_questions`

Notes:
- if structured GTM decisions are missing, fallback is taken from the first requested changes

## Step 5: Product Revision / Arbitration

Handled in:
- `run_product_revision()`

Before Product is called:
- `_build_unresolved_tensions()` populates `unresolved_tensions`

Important limitation:
- `unresolved_tensions` is not a full contradiction detector
- it only collects:
  - non-priority Tech recommendations
  - non-priority Growth recommendations
  - Tech open questions
  - Growth open questions

It does not automatically detect:
- deeper conflicts between architecture and GTM
- semantic contradictions outside those explicit lists

User input sent to Product in revision:
- `Mode: revision` or `Mode: correction`
- `Project brief`
- `Current PRD draft`
- `CEO evaluation`
- `Tech summary`
- `Tech structural decisions`
- `Tech recommendations`
- `Growth summary`
- `Growth structural decisions`
- `Growth recommendations`
- `Unresolved tensions`
- `Known reusable tags`
- optional `Targeted correction tasks`

Product then:
- rewrites the PRD
- arbitrates what is retained, deferred, rejected, or still open
- updates readiness

Parsing behavior:
- the PRD may contain a structured `## Product Arbitration` block
- if missing, heuristic fallback is used

Stored into blackboard:
- updated `prd_draft`
- `arbitration`
- `retained_decisions`
- `deferred_decisions`
- `rejected_changes`
- `open_points`
- `applied_changes`
- `decisions`
- `revision_trace`
- `workflow_stage = first_pass_final` or `second_pass_final`

## Step 6: Readiness Aggregation

Handled in:
- `_finalize_readiness()`

Aggregation function:
- `aggregate_global_readiness()`

Three local statuses exist:
- Product readiness
- Tech readiness
- Growth readiness

One global status is then computed.

The workflow uses:
- `READY`
- `LIMITED`
- `INSUFFICIENT`

## Step 7: Targeted Correction Loop

Handled in:
- `_run_targeted_correction_loop()`

Important current behavior:
- the loop is bounded
- it does not run until full resolution

Current limit:
- `max_loops = 2`

The loop triggers only if:
- `global_status == LIMITED`

It stops when:
- status becomes `READY`
- or `INSUFFICIENT`
- or max loops is reached

### How correction tasks are built

Handled in:
- `_build_correction_plan()`

Pipeline:
1. collect blocking gaps and required improvements from Product, Tech, Growth readiness
2. deduplicate and rank them
3. keep at most 3 priority gaps
4. assign an owner for each task:
   - often `tech`
   - or `growth`
   - or `product`
5. generate a targeted task + expected output + contributors

This is a correction loop, not a separate solution-proposal workflow.

Current task format contains:
- `owner`
- `task`
- `source_gap`
- `expected_output`
- `contributors`
- `tag`

### What happens inside one correction iteration

For each loop:
1. correction tasks are appended to readiness history
2. a workflow checkpoint is recorded
3. `Tech` reruns only if it has tasks
4. `Growth` reruns only if it has tasks
5. `Product` reruns if there are correction tasks
6. readiness is recalculated

Checkpoint data is stored in:
- `workflow_trace.checkpoints`

Readiness history is stored in:
- `readiness.history`

## Step 8: Product Locking Pass

Handled in:
- `run_product_locking_pass()`

User input sent to Product:
- `Mode: final_locking_pass`
- current final PRD
- retained decisions
- deferred decisions
- rejected changes
- Tech structural decisions
- Growth structural decisions
- remaining unresolved tensions

Intent of this pass:
- do not redesign the project
- do not add new ideas
- lock the MVP scope
- keep deferred items deferred unless proof-critical
- remove accessory features

Expected structured block:
- `## Product Locking`
- `### Confirmed In Scope`
- `### Confirmed Deferred`
- `### Confirmed Out Of Scope`
- `### Locking Note`

If missing:
- heuristic fallback is used

Stored into blackboard:
- `product_locking`
- locked `prd_draft`
- updated product readiness
- `workflow_stage = first_pass_locked` or `second_pass_locked`

## Step 9: Artifact Writing

Handled in:
- `_write_run_artifacts()` in [app/main.py](/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/app/main.py)

Written files:
- `project-brief.md`
- `prd.md`
- `architecture.md`
- `architecture.pdf`
- `gtm.md`
- `blackboard.md`
- `activity_log.txt`

Optional:
- `evaluator-report.md` if `BLACKBOARD_EVALUATOR_REPORT` is provided

### Architecture PDF

Rendered through:
- `render_architecture_pdf()`

Its result updates:
- `artifacts.architecture_markdown_ready`
- `artifacts.architecture_visual_ready`
- `artifacts.architecture_visual_warning`

Warnings are also appended to:
- `activity_log`

## Blackboard Rendering

`blackboard.md` is a rendered summary of the internal state.

It includes:
- brief metadata
- workflow stage
- artifacts state
- readiness blocks
- correction loop history
- expert decisions
- product locking
- expert contributions
- product arbitration
- retained / deferred / rejected / open points
- risks
- open questions
- final PRD
- activity log

Important:
- `blackboard.md` is not the main deliverable
- `prd.md`, `architecture.md`, and `gtm.md` are the final user-facing deliverables
- but `blackboard.md` should remain coherent with them

## Second Pass Workflow

Current second-pass flow:
1. load source artifacts from a fixed version directory
2. create blackboard with `source_artifacts` + `executive_evaluation`
3. set `workflow_stage = second_pass_initial`
4. call `run_product_second_pass_initial()`
5. then same chain as first pass:
   - Tech
   - Growth
   - Product revision
   - readiness
   - correction loop
   - Product locking
   - readiness

Important caveat:
- current second-pass output is written back into the same source version directory
- this mode should be treated carefully until generalized

## Environment Variables That Matter

Most useful ones:
- `BLACKBOARD_PROJECT_NAME`
- `BLACKBOARD_PROJECT_BRIEF`
- `BLACKBOARD_PROMPT_VERSION`
- `BLACKBOARD_WORKFLOW_MODE`
- `BLACKBOARD_EVALUATOR_REPORT`

Common validated run setup:
- `BLACKBOARD_PROMPT_VERSION=V3`

## Key Limitations To Know

### 1. Tech and Growth do not cross-read each other

Current behavior:
- each one reads the PRD
- not the other specialist document

Consequence:
- many tensions are only reconciled when Product revises

### 2. Unresolved tensions are partial

`_build_unresolved_tensions()` only uses:
- non-priority recommendations
- open questions

It is not a general contradiction engine.

### 3. Correction loop is bounded

It is not:
- “keep looping until all problems disappear”

It is:
- “run at most 2 targeted correction passes”

### 4. Prompt version and validated baseline are different concepts

Code default:
- `V2`

Best known baseline:
- workflow `V12-like`
- prompts `V3`

### 5. Second pass is still partly hardcoded

It exists, but is not yet a flexible reusable mode.

## Current Recommended Mental Model

If another agent has to resume the project, the right mental model is:

- stable baseline = `V12-like workflow + prompts V3`
- main generation path = `Product -> Tech -> Growth -> Product revision -> readiness loop -> Product locking`
- Product is the true arbiter
- Tech and Growth are structured challengers, not co-authors of the final PRD
- `blackboard.md` is the internal memory and trace
- `prd.md`, `architecture.md`, `gtm.md` are the final outputs

## Current Best Next-Step Discipline

Given the project history, changes should be treated carefully:
- avoid large workflow additions without isolated testing
- avoid broad prompt rewrites
- prefer one small change at a time
- validate first on `CareSync` and `LocalLoop`

This caution matters because several post-`V12` workflow experiments improved internal sophistication but reduced final output quality.
