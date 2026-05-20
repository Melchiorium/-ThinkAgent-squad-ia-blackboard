# Lot 68i - V4 External Decision Guardrails And Item Deduplication

## Objective

Prevent V4 agents from inventing external decisions and prevent near-duplicate
external blackboard items.

## Useful Project Context

- Developer model: `GPT-5.4-mini`, reasoning `high`.
- Start from `docs/ai/00-index.yaml`.
- Version 63 created two similar `EXTERNAL` items about pilot market and
  privacy baseline.
- Product also inferred a concrete country during item resolution without an
  explicit external input.
- `EXTERNAL` means outside the current run. Agents may surface the missing
  decision, but they must not decide it from inference.
- Keep rules generalist. Do not hardcode CareSync-specific text.

## Files Allowed To Modify

- `app/orchestrator.py`
- `app/blackboard_items.py`
- `app/prompts V4/common/workflow_context.md`
- `app/prompts V4/phases/item_resolution.md`
- `app/prompts V4/contracts/blackboard_operations.md`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/rules.yaml`
- `outputs/V2/lot-68i-v4-external-decision-guardrails-and-item-deduplication.md`
  for implementation notes

## Files Not To Modify

- `app/prompts V3/`
- `.env`
- `.env.local`
- `outputs/tests/`
- `outputs/web-jobs/`
- historical `runs/`
- `app/promptsV5/`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then V4 contract, flow, rules, prompt, and
   blackboard memory.
2. Strengthen the V4 common workflow and item-resolution prompt context:
   agents must not choose market, compliance, legal, pricing, retention,
   audit, or policy facts absent from the brief or runtime context.
3. Preserve the ability to document assumptions. The key distinction is:
   assumptions may be surfaced, but absent external facts must not be converted
   into decisions.
4. Add deterministic runtime validation or a focused review helper for
   item-resolution outputs touching `EXTERNAL` items. It must reject cases
   where an agent closes or resolves an external item by introducing a concrete
   unsupported value.
5. Keep the validation simple and inspectable. Do not use an LLM for this
   guardrail.
6. Add deterministic duplicate detection before blackboard item creation:
   compare target set, normalized title, normalized tag set, and normalized
   content gist.
7. If an equivalent open item already exists, reject the duplicate with a clear
   error or reuse the existing item explicitly. Prefer the simpler behavior
   that matches existing blackboard write patterns.
8. Ensure `EXTERNAL` duplicate detection works even when title wording differs
   slightly but the target, tags, and content gist are materially the same.
9. Add no-LLM tests for duplicate external market/compliance questions.
10. Add no-LLM tests proving Product may leave an `EXTERNAL` item open but may
    not replace it with an invented country or legal baseline.
11. Update `docs/ai/contracts.yaml` and `docs/ai/rules.yaml` to document the
    external-decision and duplicate-item rules.

## Expected Behaviors

- `EXTERNAL` items remain open unless external information is explicitly
  supplied in the project brief or runtime context.
- Agents can document assumptions, but cannot silently turn assumptions into
  decisions.
- Similar unresolved `EXTERNAL` items are not duplicated.
- Duplicate item failures point to the existing item id and the rejected new
  operation when possible.

## Acceptance Criteria

- Attempting to create a duplicate `EXTERNAL` item fails clearly or maps to the
  existing item according to the chosen implementation.
- A Product item-resolution output that invents a concrete country from no
  source is rejected in the harness.
- A final document may say a decision requires external input, but must not
  fabricate the decision.
- V3 prompts remain unchanged.

## Validation Commands

```bash
python3 -m compileall app scripts/check_v4_flow_no_llm.py
python3 scripts/check_v4_flow_no_llm.py
git diff --check
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs app/promptsV5
```

## Manual Verification Expected

- Review prompt edits and confirm they are workflow/contextual, not role prompt
  overfitting.
- Review duplicate detection and confirm it is deterministic, readable, and not
  CareSync-specific.
- Confirm no generated history is manually edited.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- V4 prompt changes are explicitly authorized for this lot.
- Keep rules generalist; do not hardcode CareSync-specific text.
- Do not touch V3 prompts.
- Do not touch `.env`, `.env.local`, `outputs/web-jobs/`, or historical `runs/`.
