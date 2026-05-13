# Lot 62 - V4 Blackboard Items

## Objective

Implement V4 blackboard items as atomic coordination objects stored as readable
files inside each run workspace.

This lot must provide the item model and storage helpers. It must not rewrite
the agent workflow yet.

## Useful Project Context

- V4 agents collaborate through blackboard items, documents, summaries, and
  activity logs.
- Blackboard items are atomic reasoning and coordination units.
- Documents remain the long-form source of truth.
- Summaries remain compressed derivatives.
- Items must be easy to inspect and update manually.

## Files Allowed To Modify

- `app/`
- `docs/ai/contracts.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/rules.yaml`

## Files Not To Modify

- `app/prompts V3/`
- `app/prompts V4/`
- `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- `.env`
- `.env.local`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to blackboard
   contracts and modules.
2. Add a small item module, for example `app/blackboard_items.py`.
3. Define the V4 item fields:
   - `id`
   - `type`
   - `author`
   - `targets`
   - `priority`
   - `status`
   - `tags`
   - `title`
   - `content`
   - `created_at`
   - `updated_at`
4. Support item types:
   - `QUESTION`
   - `RISK`
   - `DECISION`
   - `PROPOSAL`
   - `FEEDBACK`
   - `WARNING`
   - `CONSTRAINT`
5. Support priorities:
   - `LOW`
   - `MEDIUM`
   - `HIGH`
   - `CRITICAL`
6. Support statuses:
   - `OPEN`
   - `ANSWERED`
   - `ACCEPTED`
   - `REJECTED`
   - `OBSOLETE`
7. Write items to `runs/<run_id>/blackboard/items/ITEM-XXX.yaml`.
8. Implement helpers to:
   - create an item;
   - list all items;
   - list open items;
   - filter by target, author, type, status, or tag;
   - update an item status.
9. Normalize tags to short stable lowercase identifiers.
10. Reject invalid types, priorities, and statuses with clear errors.
11. Update `docs/ai/contracts.yaml` to document the V4 item contract.

## Expected Behaviors

- Items are small, explicit, and manually readable.
- Item IDs are sequential within a run.
- Status changes preserve the item content.
- Agents in later lots can rely on these helpers instead of editing item files
  directly.

## Acceptance Criteria

- Creating an item writes a valid YAML file.
- Listing items returns the created item.
- Filtering open items works.
- Updating status changes `status` and `updated_at`.
- Invalid item types, priorities, or statuses fail loudly.
- No runtime workflow behavior is changed yet.
- No V3 prompt is modified.
- No generated run output is modified.

## Validation Commands

```bash
python3 -m compileall app
python3 - <<'PY'
from app.run_store import create_run_workspace
from app.blackboard_items import create_item, list_items, list_open_items, update_item_status

run = create_run_workspace("Item Check")
item = create_item(
    run,
    type="QUESTION",
    author="TECH",
    targets=["PRODUCT"],
    priority="HIGH",
    tags=["scope"],
    title="Clarify MVP scope",
    content="Need a decision before architecture is finalized.",
)
assert item["id"] == "ITEM-001"
assert len(list_items(run)) == 1
assert len(list_open_items(run)) == 1
update_item_status(run, "ITEM-001", "ANSWERED")
assert len(list_open_items(run)) == 0
print("ok")
PY
git diff -- app docs/ai
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs
```

## Manual Verification Expected

- Open the generated `ITEM-001.yaml` and verify it is easy to read.
- Verify tags are normalized and not long natural-language phrases.
- Verify item storage is scoped to the run workspace.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Respect the blackboard contract.
- Keep the item model simple.
- Do not rewrite agent behavior in this lot.
- Do not modify V3 prompts.
- Do not touch generated runs.
