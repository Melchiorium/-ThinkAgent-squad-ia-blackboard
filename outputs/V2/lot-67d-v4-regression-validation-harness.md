# Lot 67d - V4 Regression Validation Harness

## Objective

Add targeted validation coverage for the V4 corrective flow introduced by lots
67b and 67c.

This lot should prove the corrected behavior without requiring real LLM calls,
then document the optional real-LLM validation path.

## Useful Project Context

- V4 now depends on parsing structured agent responses.
- V4 must not leak internal blackboard operation sections into public
  deliverables.
- V4 final artifacts must come from explicit final documents.
- The item-resolution loop should not rewrite main documents until candidate
  generation.
- Existing web and CLI behavior should continue to compile.

## Files Allowed To Modify

- `app/` test-adjacent helpers only if needed for no-LLM injection
- `scripts/` only if a small validation script is useful
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if a short validation command needs to be documented
- `outputs/V2/` if this lot needs validation notes

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/` manually
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to V4 flows,
   contracts, rules, and validation.
2. Add a no-LLM validation path for V4 parser and artifact compilation.
3. The validation must use fake agent responses that include:
   - a normal document section;
   - `## Blackboard Items To Create`;
   - `## Blackboard Items To Update`.
4. Verify the parser returns:
   - clean document text;
   - item creations;
   - item updates.
5. Create a fake run workspace with:
   - initial documents;
   - candidate documents;
   - final documents;
   - open and resolved items;
   - an activity log.
6. Compile fake final outputs without LLM calls.
7. Verify public `prd.md`, `architecture.md`, and `gtm.md` use explicit final
   documents.
8. Verify public documents do not include internal blackboard operation
   sections.
9. Verify `blackboard.md` includes open items and resolved items.
10. Document optional real-LLM validation commands for CareSync and LocalLoop,
    but do not run them unless environment variables are configured and the user
    expects LLM usage.

## Expected Behaviors

- The corrected V4 parser and compiler can be checked without an LLM.
- Regression checks catch the original review findings.
- Optional real-LLM validation remains reproducible.
- Generated history is not patched manually.

## Acceptance Criteria

- No-LLM validation passes.
- `python3 -m compileall app` passes.
- A fake final output directory contains:
  - `prd.md`;
  - `architecture.md`;
  - `gtm.md`;
  - `blackboard.md`;
  - `activity_log.txt`.
- Fake public documents do not contain `Blackboard Items To Create`.
- Fake public documents do not contain `Blackboard Items To Update`.
- `blackboard.md` includes remaining open items.
- V3 prompts remain unchanged.
- `outputs/web-jobs/` remains clean in git status.

## Validation Commands

```bash
python3 -m compileall app
# Use the repository's chosen validation script or inline no-LLM harness.
python3 scripts/check_v4_flow_no_llm.py
git diff -- app scripts docs/ai README.md outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

Optional real-LLM validation, only when environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=LocalLoop python3 app/main.py
```

## Manual Verification Expected

- Read the no-LLM validation script and verify it tests the three review
  findings.
- Inspect fake compiled artifacts and confirm only final documents are public.
- Verify the script does not write under `outputs/tests/` unless it uses an
  isolated temporary root.
- Verify optional real-LLM commands are documented as optional.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Prefer no-LLM validation for deterministic checks.
- Do not modify V3 prompts.
- Do not touch generated runs manually.
- Do not commit secrets.
