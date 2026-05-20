# Lot 68h - V4 Post-Verification Resolution Propagation

## Objective

Ensure item-resolution outputs are actually propagated into the current V4
documents and summaries before finalization.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- Version 63 showed `product_item_resolution_document.json` resolving points
  that were later missing from `PRD_FINAL.md`.
- The current flow applies blackboard item updates, but finalization can still
  read the pre-resolution candidate document.
- Final documents must reflect resolved blackboard items; otherwise the
  blackboard and final artifacts disagree.
- V4 must remain explicit Python orchestration, not a generic graph engine.

## Files Allowed To Modify

- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `outputs/workflow.md`
- `outputs/V2/lot-68h-v4-post-verification-resolution-propagation.md` for
  implementation notes

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the V4 memory files for contracts,
   flows, rules, and modules.
2. Inspect the current V4 post-verification flow in `app/orchestrator.py`,
   especially `_run_v4_item_resolution_loop(...)` and the finalization inputs.
3. Update `_run_v4_item_resolution_loop(...)` so a role document produced
   during item resolution can become the current document for that role.
4. Use an explicit return value or explicit mutable state object for current
   role document paths and summaries. Do not rely on implicit latest-file
   sorting.
5. When a resolution document becomes current, regenerate the affected summary
   before downstream finalization.
6. After post-verification Product item resolution, Product finalization must
   read the updated Product document and summary, not the stale
   `PRD_CANDIDATE.md` and stale candidate summary.
7. Apply the same pattern for Growth and Tech if their item-resolution documents
   become current in the correction loop or post-verification loop.
8. Fix `loop_changed` so Product-only item-resolution updates are logged as
   `changed=True` when the Product resolution stage updates at least one item
   or emits a current replacement document.
9. Keep finalization freeze-only. This lot must not re-enable create operations
   during finalization.
10. Update `docs/ai` memory and `outputs/workflow.md` to document that V4
    item-resolution documents can advance the current document state before
    finalization.
11. Extend the no-LLM harness with a regression where Product post-verification
    resolution changes a document and the final PRD includes that change.

## Expected Behaviors

- A resolved item cannot disappear from final outputs because finalization read
  an older document.
- `PRD_FINAL.md`, `GTM_FINAL.md`, and `Architecture_FINAL.md` are based on the
  latest resolved document state available to their roles.
- Resolution summaries are regenerated when resolution documents become current.
- Activity log loop status is truthful for Product-only resolution loops.

## Acceptance Criteria

- Fake V4 flow proves a Product post-verification resolution appears in
  `PRD_FINAL.md`.
- Fake V4 flow proves Product finalization receives the updated Product summary
  after Product item resolution.
- Product-only resolution updates log `changed=True`.
- Existing V4 no-create finalization tests still pass.
- No generated history is manually edited.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs app/promptsV5
```

## Manual Verification Expected

- Inspect the fake run final artifacts and confirm resolved decisions are not
  listed as open points.
- Inspect the fake run activity log and confirm Product-only resolution is not
  logged as unchanged when it updates items.
- Confirm no existing generated run was manually modified.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep V4 explicit in Python; do not introduce a graph engine.
- Do not touch V3 prompts.
- Do not manually edit generated history.
- Do not touch `.env`, `.env.local`, `outputs/web-jobs/`, or historical `runs/`.
