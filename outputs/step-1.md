# Step 1

## Objective
Implement the first version of `app/blackboard.py` as the shared V1 blackboard factory.

## Files concerned
- `app/blackboard.py`

## Required behavior
- define a simple factory function such as `create_blackboard(project_brief: str = "")`
- return a fresh plain Python dictionary on each call
- keep the structure aligned with `architect-context.md`
- include these keys:
  - `project_brief`
  - `prd_draft`
  - `architecture_notes`
  - `gtm_notes`
  - `open_questions`
  - `risks`
  - `decisions`
  - `conflicts`
  - `activity_log`
- initialize text fields with empty strings, except `project_brief` which may use the function argument
- initialize list fields with new empty lists
- keep the module reusable later by the orchestrator and specialist agents

## Constraints
- use plain Python only
- no external dependency
- no class
- keep the file small and easy to read
- use explicit names
- no persistence yet
- no file I/O
- no validation layer
- no agent logic
- no helper functions beyond the factory unless strictly required

## Acceptance criteria
- `app/blackboard.py` exists
- it contains one clear function to create a new blackboard
- calling the function returns the expected structure
- list fields are recreated on each call
- the code is understandable by a junior Python developer

## Out of scope
- JSON export
- save/load logic
- update helper functions
- orchestrator logic
- agent implementations

## Open questions
- no open architectural question for this step

## Developer feedback
- [ ]

## Developer status
- `ready_for_review`

## Completion check
- `app/blackboard.py` implemented with one factory function
- expected V1 keys are present
- list fields are recreated on each call

## Architect decision
- use a plain dictionary factory now; defer typed models, validation, and persistence to later steps

## Notes
- minor naming inconsistency exists in the docs: `architect.md` references `architect-context.md`, while an older wording mentions `architect-contexte.md`; use `dev-agents/architect-context.md` as source of truth
