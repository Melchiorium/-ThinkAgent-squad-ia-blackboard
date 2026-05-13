# Lot 68b - V4 Item Contract Hardening And Failure Trace

## Objective

Fix the V4 runtime blocker discovered during lot 68 validation.

The V4 workflow must reject invalid blackboard item operations before they reach
the persistence layer, and every failed LLM run must leave enough run-local
evidence to inspect the exact agent output that caused the failure.

Keep the workflow explicit and readable in Python. Do not introduce a generic
agent graph engine or a broad retry framework.

## Useful Project Context

- Lot 68 failed during the first representative CareSync V4 run.
- The failure happened when `app/blackboard_items.py:create_item()` rejected an
  invalid item type emitted by a V4 agent output.
- Allowed item create types are:
  - `CONSTRAINT`
  - `DECISION`
  - `FEEDBACK`
  - `PROPOSAL`
  - `QUESTION`
  - `RISK`
  - `WARNING`
- Allowed item update statuses must match the blackboard item contract.
- Prompt constraints alone are not sufficient. The runtime must validate parsed
  item operations before applying them.
- The failed run did not persist the raw agent output before item operation
  application, so the exact malformed payload could not be recovered from the
  run workspace.
- The fix must make the next lot 68 failure diagnosable without reading console
  scrollback.
- Developer model: `GPT-5.4-mini`, reasoning `high`.

## Files Allowed To Modify

- `app/v4_parsing.py`
- `app/orchestrator.py`
- `app/run_store.py` if a small run-local trace helper is useful
- `app/blackboard_items.py` only if shared constants are needed to avoid enum
  drift
- `app/prompts V4/`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if the validation or failure-inspection command needs a
  short update
- `outputs/workflow.md` only if the V4 runtime diagnostics need to be described
- `outputs/V2/lot-68-v4-batch-validation-and-final-docs.md` only if its
  validation note needs to point to this corrective lot

## Files Not To Modify

- `app/prompts V3/`
- existing historical runs under `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- existing `runs/` folders manually
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to V4 contracts,
   flows, modules, rules, and validation.
2. Inspect the V4 parsing and item application path:
   - `app/v4_parsing.py`
   - `app/orchestrator.py`
   - `app/blackboard_items.py`
3. Add an explicit V4 item operation validation boundary after parsing and
   before any call to `create_item()` or item update persistence.
4. Validate item create operations against the exact allowed item type enum.
5. Validate item update operations against the exact allowed status enum.
6. Preserve enough source information for each parsed item operation to report
   the offending raw line when validation fails.
7. Persist each raw V4 agent response to a run-local diagnostic path before item
   operations are applied.
   - Use a simple deterministic location such as
     `runs/<run_id>/agent_outputs/<stage>.raw.md`, or an equivalent
     run-local trace path.
   - Keep these traces out of public final artifacts.
8. When validation fails, raise a clear error that includes:
   - role;
   - mode or stage;
   - invalid field name;
   - invalid value;
   - allowed values;
   - offending raw item line when available;
   - run-local trace path for the full raw response.
9. Do not silently coerce unknown item types or statuses.
10. Update V4 prompts so the allowed item type and status values are stated
    plainly.
11. Update V4 prompts so agents are told to emit `- None` when they have no
    valid item operation to create or update.
12. Keep V3 prompts unchanged.
13. Strengthen `scripts/check_v4_flow_no_llm.py` with targeted regression
    coverage:
    - a valid V4 item operation still passes;
    - an invalid create type fails before persistence;
    - an invalid update status fails before persistence;
    - a failed parsed output writes a run-local raw-response trace;
    - final public artifacts do not include internal raw traces.
14. Update `docs/ai` memory only where the runtime contract, flow, or guardrail
    changed.
15. Do not rerun full CareSync and LocalLoop lot 68 validation until this
    corrective lot passes.

## Expected Behaviors

- Invalid V4 blackboard item operations fail at a clear parser or orchestration
  boundary.
- The persistence layer is no longer the first place invalid V4 item enums are
  detected.
- Failed LLM runs leave inspectable raw response traces in the run workspace.
- Error messages are actionable for the next architect or developer agent.
- The runtime does not invent, normalize, or silently remap item types.
- V4 prompts reduce the chance of malformed item operations without becoming
  the only enforcement layer.
- Public artifacts remain compatible with the existing viewer and artifact
  names.
- V3 prompts remain unchanged.

## Acceptance Criteria

- `create_item()` is not called for a V4 item create operation with an invalid
  type.
- Existing item update persistence is not called for a V4 item update operation
  with an invalid status.
- Invalid item operation errors name the invalid value and list the allowed
  values.
- Invalid item operation errors include the role and V4 stage or mode that
  produced the operation.
- The raw V4 agent response is written to a run-local trace path before item
  operations are applied.
- A failed run can be diagnosed from files under the run workspace, without
  relying on terminal scrollback.
- Internal raw traces are not copied into `outputs/tests/` public artifacts.
- The no-LLM harness covers valid and invalid item operation paths.
- `app/prompts V3/` remains untouched.
- Existing generated history and web job files remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
git diff -- app scripts docs/ai README.md outputs/workflow.md "app/prompts V4" outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs .env .env.local
```

Optional real-LLM validation, only after the no-LLM harness passes and the
environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

## Manual Verification Expected

- Read the V4 item validation code and verify the allowed enum values are not
  duplicated inconsistently.
- Verify invalid item operations fail before blackboard persistence.
- Verify a failed V4 run records the raw response under the run workspace.
- Verify the error message points to the trace path and the offending item line.
- Verify public final artifacts still use the existing artifact names.
- Verify raw diagnostic traces are not copied into public output folders.
- Verify V4 prompts state the exact item operation enum values.
- Verify no V3 prompt file changed.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the workflow explicit in Python.
- Do not introduce a generic graph engine.
- Do not silently coerce invalid item types or statuses.
- Do not modify V3 prompts.
- Do not manually edit generated run history.
- Do not touch `.env` or `.env.local`.
- Do not print real credentials.
