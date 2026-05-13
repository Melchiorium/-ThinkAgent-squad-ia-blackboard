# Lot 67c - V4 Resolution, Candidate, Verification, Final Flow

## Objective

Refactor V4 orchestration to use the agreed Option B workflow:

```text
initial documents
-> bounded item-resolution loop
-> consolidated candidate documents
-> one verification pass
-> final documents
-> public artifact compilation
```

This fixes the final PRD versioning issue and makes item resolution the working
space before documents are rewritten.

## Useful Project Context

- The current V4 implementation updates Product, Growth, and Tech documents
  inside correction loops.
- That makes document version selection fragile.
- The reviewed implementation can write `PRD_V3.md` during loop 2 and then
  write the locked PRD back to `PRD_V2.md`, causing public `prd.md` to use the
  wrong version.
- V4 should treat blackboard items as the coordination layer and documents as
  consolidated deliverables.
- A second verification pass is useful, but it must not become another broad
  design loop.

## Files Allowed To Modify

- `app/orchestrator.py`
- `app/artifact_writer.py`
- `app/v4_parsing.py`
- `app/run_documents.py`
- `app/run_summaries.py` only if summary generation needs final/candidate naming support
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

1. Read `docs/ai/00-index.yaml`, then memory files related to V4 orchestration,
   contracts, prompts, artifact writing, and rules.
2. Replace the current "rewrite documents during every correction loop" behavior
   with a bounded item-resolution loop.
3. Keep initial documents:
   - `documents/product/PRD_V0.md`;
   - `documents/growth/GTM_V0.md`;
   - `documents/tech/Architecture_V0.md`.
4. During the item-resolution loop:
   - agents receive relevant open items, summaries, and required document
     context;
   - agents create new items or update item statuses;
   - agents may produce short internal resolution notes if needed;
   - agents do not write new PRD/GTM/Architecture versions as final candidate
     documents.
5. Bound the item-resolution loop to a small fixed maximum. Recommended default:
   2 passes.
6. After the item-resolution loop, generate consolidated candidate documents:
   - `PRD_CANDIDATE.md`;
   - `Architecture_CANDIDATE.md`;
   - `GTM_CANDIDATE.md`.
7. Candidate documents must be generated from:
   - the project brief;
   - initial documents;
   - current summaries;
   - resolved items;
   - remaining open items.
8. Add exactly one verification pass over the candidate documents.
9. The verification pass must create only verification items such as:
   - contradiction;
   - missing decision;
   - unresolved critical risk;
   - resolved item missing from document;
   - critical open question still visible.
10. The verification pass must not reopen the whole product strategy.
11. Product arbitrates verification items and finalizes.
12. Write final documents with explicit names:
   - `PRD_FINAL.md`;
   - `Architecture_FINAL.md`;
   - `GTM_FINAL.md`.
13. Update artifact compilation to read final document names explicitly instead
    of relying on "latest document" sorting.
14. Ensure remaining open items are surfaced in final documents or
    `blackboard.md`.
15. Update V4 prompts so each mode is explicit:
    - `initial_draft`;
    - `item_resolution`;
    - `candidate_rewrite`;
    - `verification`;
    - `finalization`.
16. Update docs/ai memory to document the new V4 flow.

## Expected Behaviors

- Correction loops reduce or clarify blackboard items before document rewrite.
- Candidate documents are produced only after the resolution loop.
- Verification is one targeted pass, not a new design loop.
- Final public artifacts come from explicit final documents.
- No final PRD version can be shadowed by an older or later numbered draft.

## Acceptance Criteria

- The V4 orchestrator no longer writes `PRD_V2.md`, `PRD_V3.md`,
  `GTM_V1.md`, or `Architecture_V1.md` during the item-resolution loop as
  deliverable candidates.
- `PRD_CANDIDATE.md`, `Architecture_CANDIDATE.md`, and `GTM_CANDIDATE.md`
  are written after item resolution.
- Exactly one verification pass is implemented.
- `PRD_FINAL.md`, `Architecture_FINAL.md`, and `GTM_FINAL.md` are written after
  verification and Product finalization.
- Public `prd.md`, `architecture.md`, and `gtm.md` are compiled from the final
  documents by explicit filename.
- Remaining open items are visible in `blackboard.md`.
- V3 prompts remain unchanged.

## Validation Commands

```bash
python3 -m compileall app
python3 - <<'PY'
from pathlib import Path
from app.run_store import create_run_workspace
from app.run_documents import write_document

run = create_run_workspace("Final Selection Check")
write_document(run, "product", "PRD_V0.md", "# Old")
write_document(run, "product", "PRD_CANDIDATE.md", "# Candidate")
write_document(run, "product", "PRD_FINAL.md", "# Final")
assert (run.product_documents_dir / "PRD_FINAL.md").read_text(encoding="utf-8").strip() == "# Final"
print("ok")
PY
git diff -- app docs/ai "app/prompts V4"
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Manual Verification Expected

- Read the V4 orchestrator and verify the phase order is obvious.
- Verify item-resolution stages do not pretend to produce final documents.
- Verify verification creates targeted verification items only.
- Verify final artifacts are selected by explicit final filenames.
- Verify unresolved items remain visible.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the workflow explicit in Python.
- Do not introduce a generic graph engine.
- Do not modify V3 prompts.
- Do not touch generated runs manually.
- Keep Product as final arbiter.
