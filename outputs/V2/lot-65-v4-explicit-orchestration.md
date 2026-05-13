# Lot 65 - V4 Explicit Orchestration

## Objective

Implement the V4 workflow as explicit Python orchestration using the V4 run
workspace, documents, summaries, and blackboard items.

The workflow should be generic through reusable helpers, but the orchestration
itself must remain direct and readable. Do not introduce a generic graph engine.

## Useful Project Context

- The current orchestrator runs Product, Growth, Tech, Product revision,
  readiness, correction loop, and Product locking.
- V4 changes the internal coordination model.
- V4 should write intermediate state under `runs/<run_id>/`.
- Public generated artifacts still need to be produced later by Lot 66.
- V3 functions may remain available as historical or fallback code during this
  transition.

## Files Allowed To Modify

- `app/orchestrator.py`
- `app/agents/`
- `app/generation_service.py`
- `app/main.py`
- V4 helper modules added by earlier lots
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/` manually
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to generation,
   agents, contracts, flows, and rules.
2. Add a dedicated V4 orchestration function, for example `run_v4_flow`.
3. Keep the workflow explicit with readable stages:
   - initialize run workspace;
   - Product creates `PRD_V0.md`;
   - generate `PRD_V0` summary;
   - Growth reviews PRD summary, relevant full document context, and open
     items;
   - Growth creates `GTM_V0.md` and item changes;
   - generate GTM summary;
   - Tech reviews PRD/GTM summaries, relevant full document context, and open
     items;
   - Tech creates `Architecture_V0.md` and item changes;
   - generate architecture summary;
   - Product arbitrates Tech/Growth items and creates `PRD_V1.md`;
   - run a bounded iteration loop over critical or open items;
   - prepare finalization state.
4. Keep the iteration loop bounded. Recommended default: maximum 2 iterations.
5. Make agents consume controlled context:
   - brief;
   - latest relevant summaries;
   - full source document only when needed for creation, review, convergence,
     or finalization;
   - open items targeted to that agent.
6. Parse agent output into:
   - document text;
   - items to create;
   - item status updates.
7. Append activity log entries for every stage.
8. Keep old V3 workflow functions unless a later cleanup lot explicitly removes
   them.
9. Update docs/ai memory files to describe the implemented V4 workflow.

## Expected Behaviors

- A V4 workflow run writes intermediate files under `runs/<run_id>/`.
- Product, Growth, and Tech operate through the V4 structures.
- The orchestration remains easy to follow in Python.
- Unresolved items are preserved instead of silently disappearing.
- V3 prompts are not modified.

## Acceptance Criteria

- `run_v4_flow` or equivalent exists and is callable.
- A V4 run can execute end to end when LLM configuration is available.
- Documents are written under `runs/<run_id>/documents/`.
- Items are written under `runs/<run_id>/blackboard/items/`.
- Summaries are written under `runs/<run_id>/summaries/`.
- Activity logging captures stage transitions.
- The workflow does not use a generic graph engine.
- `python3 -m compileall app` passes.

## Validation Commands

```bash
python3 -m compileall app
# Run only when LLM environment variables are configured:
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
git diff -- app docs/ai
git diff -- "app/prompts V3"
git status --short outputs/web-jobs
```

## Manual Verification Expected

- Inspect the V4 orchestrator and verify each stage is named and explicit.
- Inspect one V4 run workspace and verify documents, items, summaries, and logs
  exist.
- Verify unresolved items remain visible after Product arbitration.
- Verify V3 prompt files are unchanged.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Respect parser contracts when introducing new output sections.
- Keep orchestration simple and deterministic.
- Do not introduce a generic autonomous agent framework.
- Do not edit generated history manually.
