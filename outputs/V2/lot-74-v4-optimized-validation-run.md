# Lot 74 - V4 Optimized Validation Run

## Objective

Validate the optimized V4 workflow with static checks and one controlled local
Ollama run.

## Useful Project Context

- Developer model for implementation: `GPT-5.4-mini`, reasoning `high`.
- Runtime validation requested by the user uses local Ollama
  `qwen2.5-coder:7b`.
- The goal of the local run is workflow validation, not final artifact quality.
- If the live/local run fails, stop and review; do not retry blindly.

## Files Allowed To Modify

- `outputs/V2/lot-74-v4-optimized-validation-run.md` for validation notes
- Documentation files only if validation reveals an incorrect documented status

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/web-jobs/`
- historical generated runs by manual edit
- `app/promptsV5/`

## Development Steps

1. Run static validations:
   - `python3 -m compileall app scripts/check_v4_flow_no_llm.py`
   - `python3 scripts/check_v4_flow_no_llm.py`
   - `git diff --check`
2. Run exactly one local validation:
   - `OPENAI_BASE_URL=http://localhost:11434/v1`
   - `OPENAI_API_KEY=ollama`
   - `OPENAI_MODEL=qwen2.5-coder:7b`
   - `BLACKBOARD_PROMPT_VERSION=V4`
   - `BLACKBOARD_PROJECT_NAME=CareSync`
3. If it fails, document failing stage, trace path if any, and likely boundary.
4. If it succeeds, inspect `prompt_metrics.jsonl` and final artifact presence.

## Expected Behaviors

- Static checks pass before the local run.
- The run emits prompt metrics and skipped call metrics.
- Final quality is not used as acceptance because the local model is small.

## Acceptance Criteria

- At most one Ollama run is executed.
- Success or failure is documented clearly.
- No repeated trial-and-error loop is performed.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
set -a; source .env; export BLACKBOARD_PROMPT_VERSION=V4; export BLACKBOARD_PROJECT_NAME=CareSync; export OPENAI_BASE_URL=http://localhost:11434/v1; export OPENAI_API_KEY=ollama; export OPENAI_MODEL=qwen2.5-coder:7b; export OPENAI_REASONING_EFFORT=; set +a; python3 app/main.py
```

## Manual Verification Expected

- Inspect latest run `prompt_metrics.jsonl`.
- Confirm generated final artifacts exist only if the local run succeeds.
- If the local model fails strict JSON, keep the failure as validation evidence.

## Validation Notes

- Static checks passed:
  - `python3 -m compileall app scripts/check_v4_flow_no_llm.py`
  - `python3 scripts/check_v4_flow_no_llm.py`
  - `git diff --check`
- One local Ollama run was executed:
  - run id: `20260518-144314-caresync-5f06d2`
  - model: `qwen2.5-coder:7b`
  - result: failed at `product_verification`
  - trace: `runs/20260518-144314-caresync-5f06d2/agent_outputs/product_verification.raw.md`
- Review finding:
  - The structured JSON document used `Out of Scope: []`, which is valid under
    the V4 document contract.
  - The runtime rendered that empty array as `- None`, then the strict Markdown
    validator rejected its own rendered document as placeholder-only content.
  - This was a renderer/validator contract bug, not a reason to relax V4
    validation.
- Corrective patch applied:
  - Empty JSON arrays now render as explicit absence statements instead of
    `None`.
  - The no-LLM harness covers the `Out of Scope: []` regression and verifies the
    rendered document passes validation without `- None`.
- Metrics emitted before failure:
  - total metrics: 31
  - statuses: 26 `ok`, 5 `skipped`
  - call types: 11 document, 10 blackboard, 10 summary
  - skipped calls: 2 `summary_cache_hit`, 3 `no_creates_and_no_updateable_items`
  - largest user prompt before failure: `product_verification`, 15,707 chars
- No second local run was launched after the failure.
- A later explicit rerun request was executed after the corrective patch:
  - run id: `20260520-124442-caresync-8a446b`
  - model: `qwen2.5-coder:7b`
  - result: success, exit code 0
  - public output version: `outputs/tests/CareSync/version 70/`
  - run final outputs: `runs/20260520-124442-caresync-8a446b/final_outputs/`
- Rerun metrics:
  - total metrics: 60
  - statuses: 52 `ok`, 8 `skipped`
  - call types: 21 document, 21 blackboard, 18 summary
  - skipped calls: 1 `summary_cache_hit`, 7 `no_creates_and_no_updateable_items`
  - largest user prompt: `product_finalization`, 16,208 chars
- Workflow observations from the successful rerun:
  - The previous `Out of Scope: []` / `- None` renderer bug did not recur.
  - Initial correction loop closed in two bounded iterations.
  - Verification created one Growth item, then post-verification resolution
    closed it before finalization.
  - Product, Growth, and Tech finalization all remained freeze-only with no
    blackboard create/update operations.
  - Final artifacts were written: `prd.md`, `gtm.md`, `architecture.md`,
    `architecture-diagram.mmd`, `blackboard.md`, `project-brief.md`, and
    `activity_log.txt`.
  - Mermaid PNG rendering remained unavailable because the local Puppeteer
    Chrome cache is missing; this is reported as an artifact-quality warning,
    not a workflow failure.

## AGENTS.md Constraints

- Start from `docs/ai/00-index.yaml`.
- Stop after the first local run failure.
- Do not manually edit generated outputs.
