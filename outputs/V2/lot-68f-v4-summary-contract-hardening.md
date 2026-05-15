# Lot 68f - V4 Summary Contract Hardening

## Objective

Fix the V4 live blocker that appears after lot 68e: PRD V0 summary generation
fails because the LLM emits an invalid summary YAML shape.

The summary layer must be strict enough to prevent summaries from becoming a
source of truth, but robust enough to handle normal YAML list formatting and to
leave a raw trace when validation fails.

Keep this focused on V4 summaries. Do not change the Product/Growth/Tech
document contracts in this lot.

## Useful Project Context

- Lot 68e no-LLM validation passed after contextual prompt guardrails were
  added.
- The representative CareSync live run now gets past Product initial draft.
- The next blocker happens while generating the summary for `PRD_V0.md`.
- Observed error:
  `ValueError: Unexpected summary field: - MVP core features defined`
- The latest failing run noted by the developer is under `runs/`.
- `app/run_summaries.py` currently calls the LLM, parses the response, validates
  it, and only writes the final normalized summary file after validation.
- Unlike V4 agent outputs, failed summary responses do not currently leave a
  raw response trace under the run workspace.
- `app/prompts V4/summary_prompt.md` is architect-owned. The architect has
  already applied a minimal prompt patch requiring exact fields, four-space
  list indentation, and no list item directly under `summary`.
- Developer model: `GPT-5.4-mini`, reasoning `high`.

Impact map to consider before coding:

- Prompt impact: summary prompts must stay generic and source-grounded. Do not
  add project-specific examples.
- Parser impact: summary parsing must accept the canonical shape rendered by
  `_render_summary_yaml()`, plus harmless YAML fences, but must reject extra
  fields and misplaced root-level bullets.
- Trace impact: every summary LLM response must be inspectable even when
  parsing fails.
- Orchestration impact: summaries are consumed by Growth, Tech, Product
  revision, item resolution, candidate rewrite, verification, finalization, and
  final artifact compilation. A bad summary must fail early with a useful
  trace path.
- Data-contract impact: summaries remain derivatives of exactly one source
  document. They must not introduce new decisions, rewrite missing content, or
  replace source documents.
- Validation impact: the no-LLM harness must simulate malformed raw summary
  responses, not only fake pre-validated summary dictionaries.
- Live-validation impact: after this lot passes locally, rerun CareSync once.
  Do not start LocalLoop until CareSync passes at least the PRD V0 summary
  boundary.

## Files Allowed To Modify

- `app/run_summaries.py`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if a short V4 validation or trace-inspection note is needed
- `outputs/workflow.md` only if the V4 summary behavior needs a human-facing
  explanation
- `outputs/V2/lot-68-v4-batch-validation-and-final-docs.md` only if its
  validation note needs to reference this corrective lot
- `outputs/V2/lot-68e-v4-contextual-prompt-guardrails.md` only if its failure
  note needs to point to this lot

## Files Not To Modify

- `app/prompts V4/`, unless the architect explicitly provides an additional
  prompt patch
- `app/prompts V3/`
- Product/Growth/Tech document contract logic in `app/v4_parsing.py`, unless a
  test helper import is needed
- existing historical runs under `outputs/tests/`
- `outputs/tests_preliminaires/`
- `outputs/web-jobs/`
- existing `runs/` folders manually
- `.env`
- `.env.local`
- `docs/supabase-schema.sql`

## Development Steps

1. Read `docs/ai/00-index.yaml`, then the memory files related to V4 summaries,
   contracts, flows, modules, rules, prompts, and validation.
2. Inspect:
   - `app/run_summaries.py`
   - `app/prompts V4/summary_prompt.md`
   - `scripts/check_v4_flow_no_llm.py`
   - the latest failing CareSync run under `runs/`, without editing it.
3. Add run-local raw summary response traces before parsing.
   - Use a simple path under `runs/<run_id>/summary_outputs/`.
   - Use source-aware names such as `product-PRD_V0.summary.raw.yaml`.
   - Keep names repeat-safe if the same source document is summarized more
     than once.
   - Do not copy raw summary traces to public `outputs/tests/` artifacts.
4. When summary parsing or validation fails, raise an error that includes:
   - source document path;
   - expected source hash when relevant;
   - failing field or shape issue;
   - raw summary trace path.
5. Harden `_parse_summary_response()` without adding a new dependency.
   - Do not add PyYAML unless the project already depends on it.
   - Keep the parser small and readable.
   - Accept optional Markdown code fences around YAML.
   - Accept exactly one root key: `summary:`.
   - Accept exactly these fields under `summary`:
     `source_document`, `source_hash`, `scope`, `key_decisions`,
     `unresolved_questions`, `critical_risks`.
   - Accept scalar `scope: value`.
   - Accept block scalar `scope: |`.
   - Accept list fields with items indented at least four spaces under their
     field.
   - Accept `- None`, `- none`, or `- NONE` as empty-list markers only inside
     list fields.
   - Reject list bullets directly under `summary`.
   - Reject unknown fields.
   - Reject duplicate fields.
   - Reject non-list content under list fields.
6. Preserve strict source traceability:
   - `source_document` must exactly match the source document relative path;
   - `source_hash` must exactly match the source document hash;
   - mismatches must fail.
7. Preserve derivative-only semantics:
   - the parser must not infer missing fields;
   - the validator must not fill key decisions or risks from the source
     document;
   - missing required fields must fail.
8. Update `scripts/check_v4_flow_no_llm.py` with targeted summary regressions:
   - valid scalar `scope` summary passes;
   - valid block-scalar `scope` summary passes;
   - fenced YAML summary passes;
   - lowercase `- none` inside list fields becomes an empty list;
   - a root-level bullet under `summary` fails with a clear error;
   - the observed malformed shape with `- MVP core features defined` directly
     under `summary` fails with a raw trace path;
   - an unknown field fails;
   - a duplicate field fails;
   - a wrong `source_document` fails;
   - a wrong `source_hash` fails;
   - raw summary traces are written before parse/validation failure;
   - raw summary traces are not copied into public final artifacts.
9. Add at least one no-LLM flow regression where the first Product document is
   summarized through `generate_summary()` with a fake LLM response instead of
   bypassing summary parsing through a fake summary dictionary.
10. Update docs/ai memory where the V4 summary contract or guardrail changed.
11. Update the lot 68 and/or 68e validation notes to say that representative
    live validation is now blocked on 68f, not on 68e.
12. Do not rerun CareSync or LocalLoop live validation until:
    - `python3 -m compileall app` passes;
    - `python3 scripts/check_v4_flow_no_llm.py` passes;
    - `git diff -- "app/prompts V3"` is empty;
    - raw summary trace behavior is verified locally.

## Expected Behaviors

- A malformed summary response fails with a useful error and a raw trace file.
- The specific observed malformed bullet
  `- MVP core features defined` directly under `summary` fails clearly.
- Valid summary YAML emitted by the summary prompt passes.
- Valid summary files remain normalized through `_render_summary_yaml()`.
- Summary parsing remains deterministic and dependency-free.
- Summaries remain compressed derivatives, not new sources of truth.
- Summary traces stay run-local and are not copied to public artifacts.
- Downstream V4 phases receive validated summaries only.
- V3 prompts remain unchanged.

## Acceptance Criteria

- `generate_summary()` writes a raw summary trace before parsing.
- Summary parse errors include the raw summary trace path.
- Summary validation errors include the raw summary trace path.
- The parser accepts the canonical shape rendered by `_render_summary_yaml()`.
- The parser rejects root-level bullets under `summary`.
- The parser rejects unknown fields.
- The parser rejects duplicate fields.
- The parser rejects malformed list fields.
- Wrong `source_document` and wrong `source_hash` still fail.
- The no-LLM harness covers valid and invalid raw summary responses.
- Public final artifacts do not include `summary_outputs/` or raw summary trace
  files.
- `app/prompts V3/` remains untouched.
- Existing generated history, run folders, environment files, and web job files
  remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
git diff -- app scripts docs/ai README.md outputs/workflow.md outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs .env .env.local
```

Optional real-LLM validation, only after the no-LLM harness passes and the
environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

Do not run LocalLoop until CareSync passes the PRD V0 summary boundary and the
new raw summary trace behavior is confirmed.

## Manual Verification Expected

- Read `app/run_summaries.py` and verify the parser stays small, explicit, and
  dependency-free.
- Verify raw summary responses are written under the run workspace before parse
  or validation.
- Verify malformed summary errors point to the raw trace.
- Verify the observed malformed bullet case is covered by the no-LLM harness.
- Verify summaries still include source_document and source_hash exactly.
- Verify summaries do not reconstruct missing document content.
- Verify raw summary traces are not copied into `outputs/tests/`.
- Verify no V3 prompt file changed.
- Verify existing generated run history was not manually edited.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the V4 workflow explicit in Python.
- Keep summary prompts general and source-grounded.
- Do not let summaries become a source of truth.
- Do not add a YAML dependency unless the project already depends on it.
- Do not modify Product/Growth/Tech prompt files in this lot.
- Do not modify V3 prompts.
- Do not manually edit generated run history.
- Do not touch `.env` or `.env.local`.
- Do not print real credentials.

## Follow-Up Validation Note

- After 68f, CareSync advanced past PRD V0 summary generation and reached
  Growth review.
- The next live blocker is not in the summary layer. It is an item-operation
  disambiguation failure in
  `runs/20260514-143950-caresync-4a40af/agent_outputs/growth_review.raw.md`.
- Corrective lot 68g covers this new blocker.
