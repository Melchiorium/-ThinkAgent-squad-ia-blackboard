# Lot 72 - V4 Blackboard No-Op Skip And Slim Operations

## Objective

Avoid blackboard LLM calls when the runtime can prove that no valid operation is
possible.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- `finalization`, `candidate_rewrite`, and `item_resolution` are no-create
  phases.
- EXTERNAL items are not updateable by agents.

## Files Allowed To Modify

- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `outputs/workflow.md`
- `outputs/V2/lot-72-v4-blackboard-noop-skip-and-slim-operations.md`

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Before calling the blackboard LLM, check whether creates are forbidden and no
   currently open non-EXTERNAL item id can be updated.
2. If so, skip the LLM call and emit deterministic operations:
   `{"create": [], "update": []}`.
3. Write the normal blackboard trace JSON for auditability.
4. Record `blackboard_operations_skipped` in activity log.
5. Record a skipped prompt metric with reason
   `no_creates_and_no_updateable_items`.
6. Keep normal validation for all non-skipped blackboard calls.

## Expected Behaviors

- Finalization with only EXTERNAL open items does not call the LLM for
  blackboard operations.
- Public artifacts remain unchanged.
- Auditors can see why a blackboard call was skipped.

## Acceptance Criteria

- Harness proves skipped blackboard metrics are emitted.
- Finalization still rejects create operations when a blackboard call is not
  skipped.
- Existing finalization freeze-only behavior remains intact.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
```

## Manual Verification Expected

- Inspect activity log and `prompt_metrics.jsonl` in a fake run.
- Confirm skipped calls still have trace JSON.

## AGENTS.md Constraints

- Start from `docs/ai/00-index.yaml`.
- Keep blackboard operations JSON-first.
- Do not touch V3 prompts.
