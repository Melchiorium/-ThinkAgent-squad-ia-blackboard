# Lot 69 - V4 Prompt Metrics And Context Baseline

## Objective

Make V4 API usage inspectable before and after context optimization.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- Runs 65 and 66 used more than 50 API calls each.
- Prompt sizes were not persisted, making context optimization hard to audit.
- V4 must remain JSON-first and file-system inspectable.

## Files Allowed To Modify

- `app/orchestrator.py`
- `app/run_summaries.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `outputs/workflow.md`
- `outputs/V2/lot-69-v4-prompt-metrics-and-context-baseline.md`

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Add run-local prompt metrics at `runs/<run_id>/prompt_metrics.jsonl`.
2. Record one JSON line for each V4 document, blackboard, and summary call.
3. Include role, mode, stage, call type, schema name, model, reasoning effort,
   status, and system/user/schema/output character counts.
4. Record skipped calls with a `skip_reason`.
5. Do not store full prompt text in the metrics file.
6. Add no-LLM harness assertions for document, blackboard, summary, and skipped
   metrics.

## Expected Behaviors

- A run can be audited for API call count and context size without reading
  prompts.
- Metrics are available even when calls are skipped or fail.
- Metrics are local run artifacts and do not change public output names.

## Acceptance Criteria

- The no-LLM harness confirms prompt metrics are emitted.
- Metrics include `model` and `reasoning_effort`.
- No full prompt content is written to metrics.
- Existing V4 strict parser tests still pass.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
```

## Manual Verification Expected

- Inspect a fake run `prompt_metrics.jsonl`.
- Confirm metrics contain sizes, not full prompt bodies.

## AGENTS.md Constraints

- Start from `docs/ai/00-index.yaml`.
- Keep V4 explicit in Python; do not introduce a graph engine.
- Do not touch V3 prompts or generated history.
