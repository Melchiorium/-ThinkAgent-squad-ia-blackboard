# Step 16

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Align the application with the new `outputs/` directory structure for projects, tests, pretests, versioned runs, and evaluator reports.

## Files concerned
- `app/main.py`
- `app/orchestrator.py`
- any output-path helper if one exists
- any brief-loading helper if one exists

## New target structure
- `outputs/dev-steps`
  - developer handoffs and build history
- `outputs/projects`
  - reusable source briefs for test runs
- `outputs/tests/<Project X>/version X`
  - outputs of one run for one project
  - evaluator report for that run must also be stored there
- `outputs/tests/pretests`
  - legacy or exploratory Ollama-based runs

## Required behavior
- stop treating `outputs/project-brief.md` as the main default source of truth
- support loading the input brief from `outputs/projects/`
- keep project runs grouped by project name under `outputs/tests/`
- create versioned run folders inside each project folder:
  - `outputs/tests/<Project X>/version 1`
  - `outputs/tests/<Project X>/version 2`
  - etc.
- keep `outputs/tests/pretests/` isolated from normal test runs
- ensure evaluator outputs can be stored alongside the run artifacts inside the corresponding `version X` folder

## Expected implementation
1. Identify how the app currently loads the input brief.
2. Replace the old single-brief path logic with a project-oriented input path under `outputs/projects/`.
3. Identify how the app currently creates run output folders.
4. Replace the old global versioning logic with per-project versioning under `outputs/tests/<Project X>/`.
5. Ensure the generated run folder can contain:
   - `project-brief.md`
   - `prd.md`
   - `architecture.md`
   - `gtm.md`
   - `blackboard.md`
   - `activity_log.txt`
   - evaluator report file when available
6. Keep `outputs/tests/pretests/` untouched by the standard run flow.

## Constraints
- do not touch `outputs/dev-steps/`
- do not delete or mutate archived historical outputs
- do not mix pretests with standard test runs
- keep the implementation explicit and readable
- avoid introducing a large configuration system unless clearly necessary

## Acceptance criteria
- the app can read a source brief from `outputs/projects/`
- standard runs are written under `outputs/tests/<Project X>/version X`
- version numbers increment within a project folder, not globally across all projects
- `outputs/tests/pretests/` remains separate
- the run folder is ready to also store evaluator results
- the old ad hoc output layout is no longer used by the normal run path

## Out of scope
- redesigning prompts
- changing agent logic
- changing the blackboard structure
- changing model provider
- reprocessing historical runs

## Open questions
- [ ]

## Developer feedback
- [x] CareSync was run from `outputs/projects/project-CareSync.md` into `outputs/tests/CareSync/version 1`, and the V2 prompts were used for Product, Tech, and Growth.

## Developer status
ready_for_review

## Architect decision
- outputs are now organized by project first, then by run version
- source briefs should live in `outputs/projects/`
- normal test runs and pretests must remain clearly separated
- evaluator outputs belong next to the run they evaluate

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- This step is about file-system organization and path logic only.
- It should make future comparisons between projects and runs much easier.
