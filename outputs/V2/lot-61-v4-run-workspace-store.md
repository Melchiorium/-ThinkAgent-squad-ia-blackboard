# Lot 61 - V4 Run Workspace Store

## Objective

Create the V4 file-system workspace foundation used to isolate each generation
run by `run_id`.

This lot introduces reusable storage helpers only. It must not rewrite the
orchestrator or migrate the current workflow to V4.

## Useful Project Context

- V4 stores intermediate orchestration data under `runs/<run_id>/`.
- The project should remain file-system first and easy to inspect manually.
- The workflow must use reusable helper functions for paths, writes, reads, and
  activity logging.
- Genericity is useful at the storage-helper level, not as a generic agent graph
  engine.
- Existing outputs under `outputs/tests/<Project>/version X/` remain the public
  generated artifacts and must not be changed manually.

## Files Allowed To Modify

- `app/`
- `docs/ai/modules.yaml`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`
- `docs/ai/00-index.yaml` only if a new key path is needed

## Files Not To Modify

- `app/prompts V3/`
- `app/prompts V4/`
- `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to modules,
   contracts, flows, and rules.
2. Add a small V4 run storage module, for example `app/run_store.py`.
3. Implement a run workspace object or simple dictionary that exposes standard
   paths for:
   - `runs/<run_id>/blackboard/items/`
   - `runs/<run_id>/documents/product/`
   - `runs/<run_id>/documents/tech/`
   - `runs/<run_id>/documents/growth/`
   - `runs/<run_id>/summaries/`
   - `runs/<run_id>/activity_log/`
   - `runs/<run_id>/final_outputs/`
4. Implement `run_id` generation using a readable timestamp and normalized
   project slug.
5. Ensure two runs with the same project title do not overwrite each other.
6. Add helpers for:
   - creating the workspace directories;
   - resolving standard paths;
   - writing text files;
   - reading text files;
   - appending activity log entries.
7. Keep the helper API simple and explicit. Do not introduce a generic storage
   backend abstraction in this lot.
8. Update `docs/ai/modules.yaml`, `contracts.yaml`, `flows.yaml`, and
   `rules.yaml` to document the new module and run workspace contract.

## Expected Behaviors

- A V4 run workspace can be created without an LLM call.
- The folder tree is readable by a human.
- The workspace is independent from the existing web job store.
- Existing CLI and web flows continue to compile.
- No generated project history is modified.

## Acceptance Criteria

- `runs/<run_id>/...` is created with the full V4 directory structure.
- Two consecutive workspace creations produce distinct directories.
- The helper can append an activity log entry.
- The helper can write and read a simple text file under the workspace.
- `python3 -m compileall app` passes.
- No V3 prompt is modified.
- No output under `outputs/tests/` or `outputs/web-jobs/` is modified.

## Validation Commands

```bash
python3 -m compileall app
python3 - <<'PY'
from app.run_store import create_run_workspace

first = create_run_workspace("Workspace Check")
second = create_run_workspace("Workspace Check")
print(first.run_id)
print(second.run_id)
print(first.root)
print(second.root)
assert first.root != second.root
assert first.items_dir.exists()
assert first.final_outputs_dir.exists()
PY
git diff -- app docs/ai
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Manual Verification Expected

- Inspect one created workspace and verify that it matches the V4 target tree.
- Verify the run directory name is readable and includes a project slug.
- Verify that the helper API is small and easy to understand.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep code simple and readable.
- Do not rewrite orchestration in this lot.
- Do not touch generated runs.
- Do not edit V3 prompts.
- Do not add external dependencies unless absolutely necessary.
