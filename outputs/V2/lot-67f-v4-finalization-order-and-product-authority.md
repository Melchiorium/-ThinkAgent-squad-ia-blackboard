# Lot 67f - V4 Finalization Order And Product Authority

## Objective

Fix the remaining V4 finalization ordering issues after lot 67e.

The V4 end-of-flow must preserve Product as the final arbiter while keeping all
public artifacts aligned with explicit final documents:

```text
candidate documents
-> one verification pass
-> Product finalization and item arbitration
-> Growth/Tech final document alignment from PRD_FINAL.md
-> final artifact compilation
```

Do not introduce a generic graph engine. Keep the workflow explicit and readable
inside Python.

## Useful Project Context

- Lot 67e moved Product finalization onto the V4 parser path and applies parsed
  item operations.
- The current implementation still writes `GTM_FINAL.md` and
  `Architecture_FINAL.md` before `PRD_FINAL.md`.
- Growth and Tech finalization currently read `PRD_CANDIDATE.md`, not
  `PRD_FINAL.md`.
- Growth and Tech can currently apply item updates before Product finalization,
  which weakens Product's role as final arbiter.
- The no-LLM harness confirms Product receives an open verification item, but
  does not prove that final GTM and Architecture are aligned with
  `PRD_FINAL.md`.
- Final public artifacts must still be compiled from:
  - `PRD_FINAL.md`;
  - `GTM_FINAL.md`;
  - `Architecture_FINAL.md`.

## Files Allowed To Modify

- `app/orchestrator.py`
- `app/prompts V4/`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if validation commands need a short update

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/` manually
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `runs/` manually
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to V4 flows,
   contracts, prompts, rules, and validation.
2. Inspect the current V4 finalization order in `app/orchestrator.py`.
3. Change the finalization order after verification to:
   - refresh current open and resolved item state;
   - run Product finalization first;
   - apply Product's parsed item operations;
   - write `PRD_FINAL.md`;
   - summarize `PRD_FINAL.md`;
   - refresh open and resolved item state;
   - run Growth finalization using `PRD_FINAL.md` and the latest Growth/Tech
     context;
   - write `GTM_FINAL.md`;
   - run Tech finalization using `PRD_FINAL.md`, `GTM_FINAL.md`, and the latest
     Tech context;
   - write `Architecture_FINAL.md`.
4. Ensure Growth and Tech finalization no longer receive `PRD_CANDIDATE.md` as
   their Product document.
5. Keep Product as the only finalization phase allowed to update existing
   verification item statuses.
6. For Growth and Tech finalization, implement an explicit item-operation
   policy:
   - item creations may be allowed only for new follow-up risks or warnings that
     remain visible in final `blackboard.md`;
   - item updates to existing verification items must fail fast with a clear
     error, or be disallowed by an explicit helper.
7. Keep candidate-phase item operations unchanged unless a targeted adjustment is
   needed for the finalization ordering.
8. Remove dead V4 code that builds or mutates a legacy `final_blackboard` if it
   is no longer used by runtime behavior.
9. Update V4 prompts so finalization responsibilities are explicit:
   - Product finalization arbitrates remaining verification items and locks the
     final PRD;
   - Growth finalization aligns GTM with `PRD_FINAL.md` and does not arbitrate
     item status;
   - Tech finalization aligns Architecture with `PRD_FINAL.md` and `GTM_FINAL.md`
     and does not arbitrate item status.
10. Update docs/ai memory to reflect the corrected finalization order and item
    authority rule.
11. Strengthen `scripts/check_v4_flow_no_llm.py` so it catches regressions in
    finalization order.
12. The no-LLM harness must prove:
    - Product finalization runs before Growth and Tech finalization;
    - Growth finalization receives `PRD_FINAL.md` content;
    - Tech finalization receives `PRD_FINAL.md` content and `GTM_FINAL.md`
      content;
    - non-Product finalization cannot update existing verification item
      statuses;
    - final public artifacts are still compiled from the explicit final
      filenames.

## Expected Behaviors

- Product finalization is the only final arbitration point for verification
  item status.
- `GTM_FINAL.md` is aligned with `PRD_FINAL.md`, not `PRD_CANDIDATE.md`.
- `Architecture_FINAL.md` is aligned with `PRD_FINAL.md` and `GTM_FINAL.md`.
- Growth and Tech finalization cannot close Product arbitration items.
- Remaining open items are still visible in final `blackboard.md`.
- Public artifacts keep the existing viewer-compatible names.
- V3 prompts remain unchanged.

## Acceptance Criteria

- `PRD_FINAL.md` is written before `GTM_FINAL.md` and
  `Architecture_FINAL.md`.
- Growth finalization receives `PRD_FINAL.md` as the Product document context.
- Tech finalization receives `PRD_FINAL.md` and `GTM_FINAL.md` as document
  context.
- Product finalization applies parsed item updates before Growth and Tech final
  alignment.
- Growth and Tech finalization do not update existing verification item
  statuses.
- Any remaining open items after finalization appear under `Open Items` in
  public `blackboard.md`.
- Resolved items appear under `Resolved Items` in public `blackboard.md`.
- Public `prd.md`, `architecture.md`, and `gtm.md` are still compiled from
  explicit final filenames.
- Dead unused V4 finalization helpers are removed or clearly justified.
- V3 prompts remain untouched.
- Generated history and web job files remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
git diff -- app scripts docs/ai README.md "app/prompts V4" outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs
```

Optional real-LLM validation, only when environment variables are configured
and the user expects a generated run:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

## Manual Verification Expected

- Read `app/orchestrator.py` and verify the finalization order is obvious.
- Verify `PRD_FINAL.md` is the Product source used by Growth and Tech final
  documents.
- Verify Growth and Tech finalization cannot update existing verification item
  statuses.
- Verify the no-LLM harness fails if Growth or Tech finalization reads
  `PRD_CANDIDATE.md` instead of `PRD_FINAL.md`.
- Verify final public documents contain no internal blackboard operation
  sections.
- Verify no V3 prompt file changed.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the workflow explicit in Python.
- Do not introduce a generic graph engine.
- Do not modify V3 prompts.
- Do not touch generated runs manually.
- Do not touch `.env` or `.env.local`.
- Keep Product as final arbiter.
