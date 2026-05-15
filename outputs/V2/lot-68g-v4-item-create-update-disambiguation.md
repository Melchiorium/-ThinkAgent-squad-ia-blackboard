# Lot 68g - V4 Item Create/Update Disambiguation

## Objective

Fix the next V4 live blocker found after CareSync passed the Product draft and
PRD summary boundary.

Growth review produced an item line that mixed update-style identifiers with
create-item fields:

```text
ITEM-005 | OPEN | ALL | HIGH | ...
```

The runtime correctly rejects this because `ITEM-005` is not a valid create
item type. This lot must make create vs update operations harder to confuse,
improve diagnostics for this exact failure, and prevent open item context rows
from looking like output operation rows.

Keep the workflow explicit and readable. Do not introduce a generic parser
framework, graph engine, or automatic correction/retry layer.

## Useful Project Context

- Latest representative run:
  `runs/20260514-143950-caresync-4a40af/`.
- Failing trace:
  `runs/20260514-143950-caresync-4a40af/agent_outputs/growth_review.raw.md`.
- The failing section starts at:
  `## Blackboard Items To Create`.
- The invalid create line starts with `ITEM-005`, which is an existing item id,
  not a valid type.
- The Product initial draft created real items, including `ITEM-005`.
- Growth likely copied or transformed open item context into the create
  section.
- Current open item context uses compact pipe rows such as
  `ITEM-005 | CONSTRAINT | CRITICAL | OPEN`, which visually resembles the
  blackboard operation protocol.
- Architect-owned prompt patch has already been applied:
  - V4 role prompts say create items must start with a valid type, not
    `ITEM-###`;
  - contextual blackboard reminder says not to copy open item context rows into
    create items.
- Lot 68f remains valid for the summary contract and raw summary traces. This
  lot addresses a separate upstream Growth/item-operation barrier.
- Developer model: `GPT-5.4-mini`, reasoning `high`.

Impact map to consider before coding:

- Prompt impact: no new role-prompt invention. The architect has already
  patched prompt text. If more prompt text is needed, stop and ask.
- Context impact: open/resolved item context must remain readable, but should
  not use pipe-delimited rows that look like output operations.
- Parser impact: create sections must reject `ITEM-###` as first field with a
  specific create/update confusion message.
- Update parser impact: update sections must accept exactly two pipe-separated
  fields: item id and status. Extra fields should fail clearly.
- Orchestration impact: item ids must remain visible in prompts so agents can
  update existing items, but the context should be clearly read-only.
- Validation impact: the no-LLM harness must include raw-response regressions
  for the exact Growth failure, not only structured fake item dictionaries.
- Live-validation impact: after this lot passes locally, rerun CareSync once.
  Do not run LocalLoop until CareSync passes Growth review item application.

## Files Allowed To Modify

- `app/v4_parsing.py`
- `app/orchestrator.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if a short V4 validation or trace-inspection note is needed
- `outputs/workflow.md` only if the V4 item context behavior needs a
  human-facing explanation
- `outputs/V2/lot-68-v4-batch-validation-and-final-docs.md` only if its
  validation note needs to reference this corrective lot
- `outputs/V2/lot-68f-v4-summary-contract-hardening.md` only if its validation
  note needs to clarify that the current blocker moved beyond summaries

## Files Not To Modify

- `app/prompts V4/`, unless the architect explicitly provides another prompt
  patch
- `app/prompts V3/`
- `app/run_summaries.py`, unless needed only for imports in tests
- existing historical runs under `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- existing `runs/` folders manually
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Architect-Owned Prompt Patch Already Applied

The architect has already patched the V4 role prompts and contextual reminder.

The developer must verify these strings exist, but must not invent new prompt
text:

```text
create items must start with a valid item type, never with an existing `ITEM-###` id
existing `ITEM-###` ids belong only in update items
update items must contain only item id and status
```

The contextual blackboard reminder in `app/orchestrator.py` must include:

```text
In Blackboard Items To Create, the first field must be a valid item type, never an ITEM-### id.
Existing ITEM-### ids are read-only references unless they are used in Blackboard Items To Update.
In Blackboard Items To Update, output only item id and status, with no targets, priority, tags, title, or content.
Do not copy Open items context rows into Blackboard Items To Create.
```

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to V4 item
   contracts, flows, rules, prompts, and validation.
2. Inspect:
   - `app/v4_parsing.py`
   - `app/orchestrator.py`
   - `scripts/check_v4_flow_no_llm.py`
   - `runs/20260514-143950-caresync-4a40af/agent_outputs/growth_review.raw.md`
   - the existing item files for that run, without editing them.
3. Change item context formatting in `app/orchestrator.py`:
   - `_format_open_items_context()`
   - `_format_items_context()`
4. Item context must not use pipe-delimited rows.
   Replace rows like:

```text
- ITEM-005 | CONSTRAINT | CRITICAL | OPEN
```

   with labeled read-only blocks such as:

```text
Item id: ITEM-005
Type: CONSTRAINT
Priority: CRITICAL
Status: OPEN
Author: PRODUCT
Targets: PRODUCT
Tags: privacy
Title: ...
Content: ...
```

5. Keep item ids visible and easy to copy for update operations.
6. Make it visually clear that item context is read-only source context, not an
   operation template.
7. In `parse_item_creates()` or `validate_v4_item_operations()`, add a specific
   guard for create lines whose first field matches `ITEM-###`.
   - Fail before persistence.
   - Error must say the line is in `Blackboard Items To Create`.
   - Error must say existing item ids belong in `Blackboard Items To Update`.
   - Error must include role, mode, raw line, and trace path.
8. Harden `parse_item_updates()`:
   - split update lines on all `|` separators;
   - accept exactly two fields: item id and status;
   - reject lines with extra fields such as
     `ITEM-005 | OPEN | ALL | HIGH | ...`;
   - error must explain that updates contain only item id and status.
9. Keep the existing validation that update ids must exist before the current
   response is applied.
10. Do not silently move malformed create lines into updates.
11. Do not auto-correct item ids, statuses, targets, or priorities.
12. Update `scripts/check_v4_flow_no_llm.py` with targeted regressions:
    - raw Growth review output with
      `## Blackboard Items To Create` containing
      `- ITEM-005 | OPEN | ALL | HIGH | ...` fails clearly;
    - the error mentions `Blackboard Items To Create`;
    - the error mentions `Blackboard Items To Update`;
    - the error includes the raw trace path;
    - update section line `ITEM-005 | OPEN | ALL | HIGH | ...` fails because
      updates have exactly two fields;
    - a valid update line `ITEM-005 | ANSWERED` still passes when `ITEM-005`
      exists;
    - item context formatting no longer emits lines matching
      `^- ITEM-\d+ \|`;
    - item ids remain present in context after the formatting change.
13. Update docs/ai memory where the item operation/context guardrail changed.
14. Update lot 68 and/or 68f notes to say the current representative blocker
    moved to Growth create/update disambiguation.
15. Do not rerun CareSync or LocalLoop live validation until:
    - `python3 -m compileall app` passes;
    - `python3 scripts/check_v4_flow_no_llm.py` passes;
    - `git diff -- "app/prompts V3"` is empty;
    - no V4 prompt contains `TARGET1` or a copyable fake create row.

## Expected Behaviors

- Agents can still see open item ids for updates.
- Open/resolved item context no longer looks like the operation protocol.
- A create item starting with `ITEM-###` fails with a specific and actionable
  error.
- An update line with extra fields fails with a specific and actionable error.
- The runtime never auto-moves malformed create lines into updates.
- Valid create operations and valid update operations still pass.
- Public final artifacts remain compatible with the existing viewer and
  artifact names.
- V3 prompts remain unchanged.

## Acceptance Criteria

- `_format_open_items_context()` does not emit pipe-delimited item rows.
- `_format_items_context()` does not emit pipe-delimited item rows.
- Item ids remain visible in item context.
- `parse_item_creates()` or item validation rejects create lines starting with
  `ITEM-###`.
- `parse_item_updates()` rejects update lines with more than two fields.
- The exact Growth failure from
  `runs/20260514-143950-caresync-4a40af/agent_outputs/growth_review.raw.md`
  is covered by the no-LLM harness.
- A valid `ITEM-005 | ANSWERED` update still passes when `ITEM-005` exists.
- The no-LLM harness covers both context formatting and parser validation.
- `app/prompts V3/` remains untouched.
- Existing generated history, run folders, environment files, and web job files
  remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
rg -n "TARGET1|^- TYPE \\| AUTHOR \\||TYPE \\| AUTHOR" "app/prompts V4" || true
git diff -- app scripts docs/ai README.md outputs/workflow.md outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs .env .env.local
```

Optional real-LLM validation, only after the no-LLM harness passes and the
environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

Do not run LocalLoop until CareSync passes Growth review item application.

## Manual Verification Expected

- Read the item context in a generated V4 user prompt and verify it is clearly
  read-only context.
- Verify no item context line looks like a create or update operation row.
- Verify the exact failing Growth line now produces an actionable error.
- Verify valid create and update operations still work.
- Verify no V3 prompt file changed.
- Verify no existing generated run was manually edited.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the V4 workflow explicit in Python.
- Do not introduce a generic parser framework or retry loop.
- Do not auto-correct malformed item operations.
- Do not modify V4 prompts unless the architect provides another patch.
- Do not modify V3 prompts.
- Do not manually edit generated run history.
- Do not touch `.env` or `.env.local`.
- Do not print real credentials.
