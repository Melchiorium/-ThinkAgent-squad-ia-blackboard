# Step 8

## Status
- [ ] todo
- [ ] in_progress
- [ ] blocked
- [x] done

## Objective
Replace the hardcoded project brief with a file-loaded input brief and make the brief source traceable through the run.

## Files concerned
- `app/orchestrator.py`
- `app/main.py`
- `app/blackboard.py`

## Required behavior
- remove the hardcoded `project_brief` string from `app/orchestrator.py`
- update the orchestrator so it receives the project brief as an input argument instead of owning the brief content directly
- load the project brief from `dev-agents/architect-context.md` in the application entry flow
- write the loaded brief into the blackboard as the actual input used for the run
- add a simple blackboard field to preserve the brief source path or source identifier
- export a readable copy of the brief used for the run into `outputs/`
- fail with a clear error if the brief file is missing or empty

## Constraints
- keep the orchestrator explicit and deterministic
- do not redesign the whole application startup
- no new dependency
- no CLI system yet
- no parsing framework for the briefing file
- treat the current file content as the input brief as-is
- keep the implementation simple and readable

## Acceptance criteria
- `app/orchestrator.py` no longer contains a hardcoded project brief
- the orchestrator takes the brief as input
- `app/main.py` loads the brief from `dev-agents/architect-context.md`
- the blackboard stores both the brief content and its source
- an output file captures the exact brief used during the run
- missing or empty brief file produces a clear error

## Out of scope
- introducing a dedicated brief extraction format
- adding CLI arguments for custom brief paths
- changing agent prompts
- modifying the multi-agent flow
- validating the semantic quality of the brief content

## Open questions
- [ ]

## Developer feedback
- [ ]

## Developer status
done

## Architect decision
- the orchestrator should consume a brief, not define it
- using `dev-agents/architect-context.md` directly is acceptable for now as the source file
- a dedicated input-brief file can come later if needed, but it is not required for this step

## Completion check
- [x] implementation done
- [x] acceptance criteria met
- [x] ready for next step

## Notes
- Prefer keeping the file-loading responsibility in `main.py` so the orchestrator stays reusable.
