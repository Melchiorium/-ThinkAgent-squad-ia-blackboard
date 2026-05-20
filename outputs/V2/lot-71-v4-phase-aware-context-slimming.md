# Lot 71 - V4 Phase-Aware Context Slimming

## Objective

Send only the context needed by each V4 phase while preserving source truth in
the run workspace.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- Late V4 prompts previously sent all current full documents to many calls.
- Summaries exist specifically to avoid passing every full document everywhere.

## Files Allowed To Modify

- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `outputs/workflow.md`
- `outputs/V2/lot-71-v4-phase-aware-context-slimming.md`

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Apply this context policy:
   - `initial_draft`: brief only.
   - `review` and `revision`: full documents supplied by upstream steps.
   - `item_resolution`: current role document full; other roles as summaries.
   - `candidate_rewrite`: current role document full; other roles as summaries.
   - `verification`: candidate documents full once.
   - `finalization`: current role document full; Product may see all candidate
     documents, Growth/Tech use upstream final/candidate summaries for other
     roles.
   - `blackboard`: produced document full plus summaries and updateable/open
     items; previous full documents omitted by default.
2. Keep all source documents in `runs/<run_id>/documents/`.
3. Add harness assertions around slimmed prompt content and prompt metrics.

## Expected Behaviors

- Prompt size drops materially on late-stage calls.
- Agents still have enough context to keep final documents coherent.
- Blackboard operations are based on the produced document and routed items.

## Acceptance Criteria

- No-LLM harness passes.
- Late blackboard prompts do not include previous full role documents by
  default.
- Resolved item propagation into final docs still works.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
```

## Manual Verification Expected

- Compare prompt metrics against a previous successful run.
- Confirm final public artifact names are unchanged.

## AGENTS.md Constraints

- Start from `docs/ai/00-index.yaml`.
- Do not hide source truth in external conversation state.
- Do not modify generated history manually.
