# Lot 67e - V4 Verification Arbitration And Mode Contract

## Objective

Fix the remaining V4 review findings after lots 67b, 67c, and 67d.

This lot must make the end of the Option B workflow coherent:

```text
candidate documents
-> one verification pass
-> Product arbitration of verification items
-> final documents
-> final artifact compilation
```

The goal is not to add a generic agent engine. Keep the workflow explicit,
readable, and deterministic in Python.

## Useful Project Context

- V4 now strips internal blackboard item sections from public deliverables.
- V4 now writes candidate documents after the bounded item-resolution loop.
- V4 now compiles public artifacts from explicit final documents:
  `PRD_FINAL.md`, `GTM_FINAL.md`, and `Architecture_FINAL.md`.
- The current implementation still has three important gaps:
  - Product finalization does not receive and arbitrate the actual open
    verification items.
  - Some V4 agent outputs are parsed for item operations, but those operations
    are ignored in candidate/finalization phases.
  - The V4 mode labels used by the orchestrator and the mode labels documented
    in V4 prompts are not fully aligned.
- The current no-LLM harness checks the presence of item section headings, but
  does not prove that one open item and one resolved item are rendered in the
  correct final `blackboard.md` sections.

## Files Allowed To Modify

- `app/orchestrator.py`
- `app/v4_parsing.py` only if parser behavior needs a small targeted adjustment
- `app/agents/product_agent.py` only if keeping a Product-specific locking
  helper is simpler than moving Product finalization fully into `_run_v4_agent`
- `app/prompts V4/`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if validation commands need a short documented update

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
2. Inspect the current V4 orchestration around:
   - verification pass;
   - Growth finalization;
   - Tech finalization;
   - Product finalization;
   - final artifact compilation.
3. Make Product finalization consume the actual remaining open items after the
   verification pass.
4. Prefer using the V4 parser path for Product finalization:
   - call `_run_v4_agent(role="product", mode_label="finalization", ...)`;
   - pass candidate/final document context;
   - pass full remaining open item context;
   - write `PRD_FINAL.md` from parsed `document_text`;
   - apply parsed item updates before final output compilation.
5. If a legacy Product locking helper is still used, it must receive the full
   open item details and still produce/apply V4 item operations. Do not leave
   verification item arbitration as a count-only note.
6. Ensure every V4 agent output that includes parsed item operations follows one
   explicit policy:
   - either `_apply_v4_item_operations(...)` is called immediately after the
     output is produced;
   - or the prompt and code clearly disallow item operations for that phase and
     assert that no operations were returned.
7. Apply the policy consistently to candidate and finalization phases.
8. Recompute `open_items` and `resolved_items` after every batch of item
   operations that can change the blackboard state.
9. Align the V4 mode contract across orchestrator, prompts, and docs.
   The final implementation must have one canonical list of modes. It is
   acceptable to keep existing mode names such as `review` and `revision` if
   the V4 prompts and docs declare them explicitly.
10. Update V4 prompts so each phase is clear about what the agent should do:
    - item-resolution phases update blackboard state and may produce short
      internal notes;
    - candidate phases produce consolidated deliverables and should not reopen
      broad strategy;
    - verification creates only targeted verification items;
    - finalization resolves or explicitly leaves remaining verification items.
11. Update the no-LLM harness so it proves item state rendering, not only
    heading presence.
12. The harness must include at least:
    - one item that remains `OPEN`;
    - one item that is `ANSWERED`, `ACCEPTED`, `REJECTED`, or `OBSOLETE`;
    - assertions that each item appears under the expected `blackboard.md`
      section.
13. Add a harness check for Product finalization item updates if this can be
    done without real LLM calls.
14. Update docs/ai memory for any changed V4 flow, mode contract, parser
    behavior, or validation rule.

## Expected Behaviors

- Verification items are not reduced to a count-only note.
- Product receives the remaining verification items and either resolves them or
  leaves them visibly open.
- `blackboard.md` reflects the final item state after finalization, not the
  pre-finalization state.
- Final documents do not include `## Blackboard Items To Create` or
  `## Blackboard Items To Update`.
- Mode labels are consistent between code, prompts, and docs.
- The no-LLM harness catches regressions in final item state rendering.
- V3 prompts remain unchanged.

## Acceptance Criteria

- Product finalization receives the full remaining open item list after
  verification.
- Product finalization applies returned V4 item updates before final artifacts
  are compiled.
- Growth and Tech candidate/finalization phases either apply parsed item
  operations or explicitly disallow and validate that none were returned.
- `state["open_items"]` is computed after the last applied item operation.
- Public `blackboard.md` shows unresolved items under `Open Items` and resolved
  items under `Resolved Items`.
- The V4 orchestrator mode labels match the mode labels documented in
  `app/prompts V4/` and `docs/ai/flows.yaml`.
- Public `prd.md`, `architecture.md`, and `gtm.md` are still compiled from
  `PRD_FINAL.md`, `Architecture_FINAL.md`, and `GTM_FINAL.md` by explicit
  filename.
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

- Read `app/orchestrator.py` and verify the final phase order is obvious.
- Verify Product finalization sees actual verification item details, not only a
  summary count.
- Verify every parsed V4 item operation is either applied or explicitly
  disallowed by code and prompt.
- Verify final public documents contain no internal blackboard operation
  sections.
- Verify no V3 prompt file changed.
- Verify the no-LLM harness has at least one real open-item assertion and one
  real resolved-item assertion.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the workflow explicit in Python.
- Do not introduce a generic graph engine.
- Do not modify V3 prompts.
- Do not touch generated runs manually.
- Do not touch `.env` or `.env.local`.
- Keep Product as final arbiter.
