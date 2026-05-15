# Lot 68d - V4 Live Output Boundaries And Routing

## Objective

Fix the remaining V4 live-validation defects found after lots 68b and 68c.

The V4 runtime must keep each role document inside its own deliverable
boundary, parse internal blackboard sections consistently, reject unresolved
readiness placeholders, and route blackboard items explicitly.

Keep the workflow explicit, readable, and Python-first. Do not introduce a
generic agent graph engine, retry framework, or broad document-quality system.

## Useful Project Context

- Lot 68 still fails on the latest CareSync V4 run:
  `runs/20260513-165821-caresync-6d1282/`.
- The failing raw trace is:
  `runs/20260513-165821-caresync-6d1282/agent_outputs/product_item_resolution_02.raw.md`.
- The trace contains `## BlackBoard Items To Create` and
  `## BlackBoard Items To Update`.
- `app/v4_parsing.py` strips internal sections through normalized headings, but
  item parsing and document validation still read exact section keys such as
  `Blackboard Items To Create`.
- `PRD_V1.md` from the same run is polluted with copied GTM and Tech sections,
  including `## GTM_V0.md`, `## Go-To-Market Notes`, and
  `## Technical Readiness`.
- `_format_document_context()` currently formats context as `## {title}`,
  which makes context documents look like output contract sections.
- Tech output accepted the literal readiness placeholder
  `Status: READY / LIMITED / INSUFFICIENT` instead of choosing one status.
- Many blackboard items used topic-only targets such as `PRICING_MODEL`.
  `_owners_for_targets()` currently falls back to Product when no role target
  is found, which hides routing mistakes.
- A Product output attempted to update `ITEM-001` in the same response that
  created it. V4 agents must only update items that already existed before the
  current response was parsed.
- V4 prompts are architect-owned from now on. The architect has already made a
  narrow V4 prompt adjustment for these protocol invariants. Do not modify
  prompt files in this lot unless the architect explicitly asks for it.
- Developer model: `GPT-5.4-mini`, reasoning `high`.

## Files Allowed To Modify

- `app/v4_parsing.py`
- `app/orchestrator.py`
- `app/blackboard_items.py` only if shared role-target constants or lookup
  helpers are needed
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if a short V4 validation note is needed
- `outputs/workflow.md` only if the V4 runtime behavior needs a human-facing
  explanation
- `outputs/V2/lot-68-v4-batch-validation-and-final-docs.md` only if its
  blocker note needs to reference this corrective lot

## Files Not To Modify

- `app/prompts V4/`, unless the architect explicitly asks for a prompt change
- `app/prompts V3/`
- existing historical runs under `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- existing `runs/` folders manually
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to V4 contracts,
   flows, modules, rules, prompts, and validation.
2. Inspect the current V4 parser and orchestration path:
   - `app/v4_parsing.py`
   - `app/orchestrator.py`
   - `app/blackboard_items.py`
   - `scripts/check_v4_flow_no_llm.py`
3. In `app/v4_parsing.py`, make section lookup consistently normalized:
   - keep original section headings for traceability;
   - add a small helper to fetch a section by normalized heading;
   - use that helper for `Blackboard Items To Create`;
   - use that helper for `Blackboard Items To Update`;
   - use that helper for required human and internal section validation;
   - fail clearly if duplicate top-level headings normalize to the same key.
4. Confirm that `## BlackBoard Items To Create` and
   `## BlackBoard Items To Update` are stripped from `document_text`, parsed as
   internal item sections, and accepted by document validation.
5. Add a role output-boundary validation:
   - Product may only return Product top-level human-facing sections plus the
     internal blackboard sections;
   - Growth may only return Growth top-level human-facing sections plus the
     internal blackboard sections;
   - Tech may only return Tech top-level human-facing sections plus the
     internal blackboard sections;
   - unexpected top-level `##` headings must fail before the document is
     written.
6. Add targeted forbidden-heading coverage for the known pollution case:
   - Product output containing `## GTM_V0.md` must fail;
   - Product output containing `## Go-To-Market Notes` must fail;
   - Product output containing `## Technical Readiness` must fail.
7. Change V4 context formatting in `app/orchestrator.py` so source documents,
   summaries, and item context do not use top-level Markdown headings that
   look like deliverable sections.
   - Prefer simple delimiters such as `Context document: <name>` and
     `End context document: <name>`.
   - Do not wrap the context in headings that start with `##`.
   - Keep the resulting prompts readable in raw run traces.
8. Add readiness-status validation for Product, Growth, and Tech:
   - accept exactly one of `Status: READY`, `Status: LIMITED`, or
     `Status: INSUFFICIENT`;
   - reject the literal placeholder
     `Status: READY / LIMITED / INSUFFICIENT`;
   - include role, mode, section, invalid status, and raw trace path in the
     error message.
9. Harden V4 item target validation before persistence:
   - every create operation must include at least one routing target among
     `PRODUCT`, `GROWTH`, `TECH`, or `ALL`;
   - topic-only targets such as `PRICING_MODEL` must fail;
   - topical labels belong in `tags`;
   - `ALL` must route to Product, Growth, and Tech;
   - `_owners_for_targets()` must not silently default unknown targets to
     Product.
10. Harden item update validation:
    - collect the item IDs that existed before the current response is applied;
    - reject an update for any ID not present in that pre-existing set;
    - this must catch attempts to update an item created in the same response;
    - include the offending item ID, raw line, role, mode, and trace path in
      the error message.
11. Keep item creation and update application order explicit and easy to read.
    Do not hide it behind a generic batch engine.
12. Update `scripts/check_v4_flow_no_llm.py` with regression cases for:
    - `BlackBoard Items To Create` casing still parses and validates;
    - duplicate normalized headings fail clearly;
    - Product output with copied GTM or Tech top-level headings fails;
    - Tech readiness with
      `Status: READY / LIMITED / INSUFFICIENT` fails;
    - a valid single readiness status passes;
    - topic-only item targets fail before persistence;
    - `ALL` targets route to all three roles;
    - unknown targets do not fall back to Product;
    - updating a non-existing item fails before persistence;
    - updating an item created in the same response fails before persistence;
    - V4 formatted context strings no longer start context documents with
      `##`.
13. Update `docs/ai` memory where the V4 contract, flow, or guardrail changed.
14. Update lot 68 only to document that representative LLM validation depends
    on this corrective lot.
15. Do not rerun CareSync or LocalLoop live validation until the no-LLM harness
    passes.

## Expected Behaviors

- The live `BlackBoard` casing variation no longer breaks parsing or document
  validation.
- Internal blackboard sections remain internal and are not copied into public
  deliverables.
- Product documents cannot contain Growth or Tech top-level deliverable
  sections.
- Growth and Tech documents cannot contain unrelated role top-level sections.
- Context passed to agents is readable but no longer resembles output contract
  headings.
- Readiness sections always choose one concrete status.
- Topic-only blackboard targets fail fast instead of being routed to Product.
- `ALL` is the only broad routing target and routes to Product, Growth, and
  Tech.
- Item updates can only target items that existed before the current response.
- Public final artifacts remain compatible with the existing viewer and
  artifact names.
- V3 prompts remain unchanged.

## Acceptance Criteria

- `parse_v4_agent_response()` parses internal item sections by normalized
  heading.
- `validate_v4_document()` validates required sections by normalized heading.
- Duplicate normalized top-level headings fail with a clear error.
- A Product document containing `## Go-To-Market Notes` fails before write.
- A Product document containing `## Technical Readiness` fails before write.
- A Tech or Growth document with an unrelated role top-level heading fails
  before write.
- `Status: READY / LIMITED / INSUFFICIENT` fails validation for every role.
- `Status: READY`, `Status: LIMITED`, and `Status: INSUFFICIENT` can each pass
  when the rest of the document is valid.
- A create item with targets `PRICING_MODEL` fails before persistence.
- A create item with target `ALL` is accepted and routed to all three role
  owners.
- `_owners_for_targets()` no longer returns Product for unknown or empty
  targets.
- An update for an item created in the same response fails before persistence.
- The no-LLM harness covers the regression cases listed above.
- `app/prompts V3/` remains untouched.
- The developer does not modify `app/prompts V4/` in this lot.
- Existing generated history, run folders, environment files, and web job files
  remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
git diff -- app scripts docs/ai README.md outputs/workflow.md outputs/V2
git diff -- "app/prompts V3"
git diff -- "app/prompts V4"
git status --short outputs/tests outputs/web-jobs runs .env .env.local
```

Optional real-LLM validation, only after the no-LLM harness passes and the
environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

## Manual Verification Expected

- Read the parser code and verify all V4 section lookups use the same
  normalized-heading helper.
- Re-read the known failing trace and verify the `BlackBoard` casing would now
  parse as internal blackboard sections.
- Re-read the polluted `PRD_V1.md` symptom and verify the copied GTM and Tech
  headings would now fail validation.
- Inspect the context formatting in `app/orchestrator.py` and verify context
  documents are not emitted with top-level `##` headings.
- Verify readiness validation rejects the literal placeholder and accepts one
  concrete status.
- Verify item routing is explicit and never defaults unknown targets to
  Product.
- Verify item update validation checks IDs that existed before the current
  response was applied.
- Verify public final artifacts still use the existing artifact names.
- Verify no V3 prompt file changed.
- Verify the developer did not edit V4 prompts without architect approval.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the V4 workflow explicit in Python.
- Do not introduce a generic graph engine or broad retry framework.
- Do not use summaries to reconstruct missing source content.
- Do not silently coerce unknown item targets.
- Do not silently default unknown item targets to Product.
- Do not modify V3 prompts.
- Do not modify V4 prompts without architect approval.
- Do not manually edit generated run history.
- Do not touch `.env` or `.env.local`.
- Do not print real credentials.

## Validation Attempt

- The no-LLM harness passed after the 68d parser, routing, readiness, and
  update-ownership fixes.
- A single representative live run was then started with:

  ```bash
  set -a; source .env; export BLACKBOARD_PROMPT_VERSION=V4; export BLACKBOARD_PROJECT_NAME=CareSync; set +a; python3 app/main.py
  ```

- LocalLoop was not started.

## Failure Report

- The representative CareSync live run failed at the first Product draft
  boundary, before any downstream validation could run.
- The failing trace is
  `runs/20260513-180526-caresync-bf8154/agent_outputs/product_initial_draft.raw.md`.
- The runtime now rejects the response with:
  `field 'targets': invalid value 'TARGET1, TARGET2'`.
- That means the current V4 Product prompt or stage instruction still emits
  topic labels in the routing slot instead of explicit routing targets.
- The parser and runtime guards from 68d are working; the remaining fix is on
  the architect-owned prompt/instruction side.
- Do not mark lot 68d as fully representative until Product initial draft
  emits explicit routing targets such as PRODUCT, TECH, GROWTH, or ALL.
