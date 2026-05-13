# Lot 67b - V4 Parser Tracking And Deliverable Boundaries

## Objective

Fix the immediate V4 review findings that can break runtime or leak internal
blackboard protocol into final deliverables.

This lot must make V4 import-safe and enforce a clean separation between:

- agent documents;
- blackboard item operations;
- public generated artifacts.

## Useful Project Context

- `app/orchestrator.py` and `app/artifact_writer.py` import `app/v4_parsing.py`.
- `app/v4_parsing.py` must be tracked in git or V4 imports will fail after
  commit/push.
- V4 prompts currently ask agents to output `## Blackboard Items To Create` and
  `## Blackboard Items To Update`.
- Those sections are internal coordination protocol and must not appear in
  `prd.md`, `architecture.md`, or `gtm.md`.
- Blackboard items remain the atomic coordination layer.
- Documents remain the long-form human-facing source of truth.
- Summaries remain compressed derivatives of documents.

## Files Allowed To Modify

- `app/v4_parsing.py`
- `app/orchestrator.py`
- `app/artifact_writer.py`
- `app/run_documents.py` only if document helpers need a clean-document helper
- `app/prompts V4/`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`

## Files Not To Modify

- `app/prompts V3/`
- `outputs/tests/` manually
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then memory files related to V4 modules,
   contracts, flows, prompts, and artifact writing.
2. Ensure `app/v4_parsing.py` is included in the final commit.
3. Add or update a parser helper that splits a V4 agent response into:
   - `document_text`;
   - `items_to_create`;
   - `items_to_update`;
   - optional raw response for trace/debug only.
4. Make `document_text` exclude internal sections:
   - `## Blackboard Items To Create`;
   - `## Blackboard Items To Update`.
5. Keep parsed item operations available for `create_item` and
   `update_item_status`.
6. Do not write internal item-operation sections into:
   - `runs/<run_id>/documents/...`;
   - `runs/<run_id>/final_outputs/...`;
   - `outputs/tests/<Project>/version X/prd.md`;
   - `outputs/tests/<Project>/version X/architecture.md`;
   - `outputs/tests/<Project>/version X/gtm.md`.
7. If raw agent output is useful for debugging, store it in a clearly internal
   trace location, not in public deliverables.
8. Update V4 prompt wording if needed so agents still return parseable item
   sections while understanding that these sections are system instructions,
   not part of the human deliverable.
9. Update `docs/ai/contracts.yaml` to document the separation between document
   text and blackboard operation sections.

## Expected Behaviors

- V4 imports work after a clean checkout.
- V4 agent outputs can still create and update blackboard items.
- Internal item-operation sections do not appear in final human-facing files.
- Public artifacts remain readable as PRD, Architecture, and GTM deliverables.

## Acceptance Criteria

- `app/v4_parsing.py` is tracked by git.
- Parsing a sample V4 response returns clean `document_text`.
- Parsed `items_to_create` and `items_to_update` still work.
- Clean documents do not include `## Blackboard Items To Create`.
- Clean documents do not include `## Blackboard Items To Update`.
- `prd.md`, `architecture.md`, and `gtm.md` are compiled from clean documents.
- V3 prompts remain unchanged.
- Generated history is not patched manually.

## Validation Commands

```bash
python3 -m compileall app
python3 - <<'PY'
from app.v4_parsing import parse_v4_agent_response

sample = """## Product Problem
- Real content.

## Blackboard Items To Create
- QUESTION | PRODUCT | TECH | HIGH | scope | Clarify scope | Need a decision.

## Blackboard Items To Update
- ITEM-001 | ANSWERED
"""
parsed = parse_v4_agent_response(sample)
assert "Blackboard Items To Create" not in parsed["document_text"]
assert "Blackboard Items To Update" not in parsed["document_text"]
assert len(parsed["items_to_create"]) == 1
assert len(parsed["items_to_update"]) == 1
print("ok")
PY
git status --short app/v4_parsing.py
git diff -- app docs/ai "app/prompts V4"
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Manual Verification Expected

- Read the V4 parser helper and verify its responsibility is narrow.
- Inspect a sample clean document and verify internal item protocol is absent.
- Inspect item creation/update behavior and verify it still uses the parsed
  sections.
- Verify `app/v4_parsing.py` is not left untracked.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep documents, items, summaries, and activity logs distinct.
- Do not modify V3 prompts.
- Do not touch generated runs manually.
- Do not hide unresolved questions by stripping normal document sections.
