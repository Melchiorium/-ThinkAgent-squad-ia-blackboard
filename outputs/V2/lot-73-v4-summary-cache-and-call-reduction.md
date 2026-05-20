# Lot 73 - V4 Summary Cache And Call Reduction

## Objective

Avoid repeated LLM summary calls for identical document content within the same
run.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- V4 summaries are derivatives, not source of truth.
- Some correction/resolution documents can have unchanged content.

## Files Allowed To Modify

- `app/run_summaries.py`
- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`
- `outputs/workflow.md`
- `outputs/V2/lot-73-v4-summary-cache-and-call-reduction.md`

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Compute each source document hash before summary generation.
2. Search existing run summary raw traces for the same `source_hash`.
3. On cache hit, reuse summary content, rewrite `source_document` to the new
   document path, keep the same hash, and render YAML.
4. Record a skipped summary metric with reason `summary_cache_hit`.
5. Do not use summaries to mutate documents or blackboard items.

## Expected Behaviors

- Identical document content is summarized once per run.
- New document paths still get inspectable raw summary JSON and YAML.
- Summary metadata remains strict.

## Acceptance Criteria

- Harness proves an identical document does not call the fake summary LLM twice.
- Cached summary output has the new `source_document` and exact original hash.
- Summary validation still rejects wrong source metadata when no cache applies.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
```

## Manual Verification Expected

- Inspect `summary_outputs/` and `summaries/` in a fake run.
- Confirm cache hits are metrics-only optimizations.

## AGENTS.md Constraints

- Start from `docs/ai/00-index.yaml`.
- Summaries remain derived artifacts.
- Do not touch generated history manually.
