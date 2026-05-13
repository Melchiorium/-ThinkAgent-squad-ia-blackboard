# Lot 68c - V4 Document Completeness Guardrails

## Objective

Prevent V4 from accepting role documents whose required human-facing sections
are empty, placeholder-only, or filled with cross-references such as
`See above`.

This lot addresses a separate validation blocker discovered after lot 68:
`PRD_V0.md` can contain required sections like `## Product Problem` with only
`- See above`. That is not an acceptable deliverable, even if the parser can
technically extract the section.

Keep the validation explicit, role-aware, and easy to read. Do not introduce a
generic document-quality framework.

## Useful Project Context

- Lot 68 failed before full validation completed.
- The failed CareSync run still wrote `PRD_V0.md`.
- In that file, most Product sections contained only `- See above`.
- This is not a viewer issue and not a markdown parsing issue. The LLM output
  was accepted too easily as a valid role document.
- V4 prompts currently require exact headings, but they do not clearly forbid
  placeholder cross-references inside required sections.
- Summaries are derivatives only and must not be used to reconstruct missing
  source content.
- This lot should be implemented after lot 68b, so failed outputs are already
  traceable.
- Developer model: `GPT-5.4-mini`, reasoning `high`.

## Files Allowed To Modify

- `app/v4_parsing.py`
- `app/orchestrator.py`
- `app/prompts V4/`
- `scripts/check_v4_flow_no_llm.py`
- `docs/ai/contracts.yaml`
- `docs/ai/flows.yaml`
- `docs/ai/modules.yaml`
- `docs/ai/rules.yaml`
- `README.md` only if a short validation note is needed
- `outputs/workflow.md` only if the V4 document validation rules need to be
  described
- `outputs/V2/lot-68-v4-batch-validation-and-final-docs.md` only if its
  blocker note needs to reference this corrective lot

## Files Not To Modify

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
2. Inspect the current V4 role document parsing path in:
   - `app/v4_parsing.py`
   - `app/orchestrator.py`
   - `app/prompts V4/`
3. Add an explicit role-document validation boundary after V4 response parsing
   and before writing `document_text` to the run workspace.
4. Define simple role-specific required human-facing sections for Product,
   Growth, and Tech.
5. Validate that every required human-facing section is present.
6. Validate that required human-facing sections are not empty.
7. Validate that required human-facing sections are not placeholder-only.
   At minimum, reject sections whose meaningful content is only one of:
   - `See above`
   - `As above`
   - `Same as above`
   - `See previous section`
   - `TBD`
   - `To be defined`
   - `N/A`
8. Keep `- None` allowed only where the prompt contract explicitly allows an
   empty subsection or an empty internal item operation section.
9. Do not try to auto-fill missing content from summaries or other documents.
10. When validation fails, raise a clear error that includes:
    - role;
    - mode or stage;
    - missing or invalid section name;
    - invalid placeholder text when relevant;
    - run-local raw-response trace path created by lot 68b when available.
11. Update V4 prompts so every agent is explicitly told:
    - every required human-facing section must be self-contained;
    - never use `See above`, `As above`, `TBD`, or equivalent placeholders;
    - if information is missing, write the concrete gap in the relevant section
      and create a blackboard item.
12. Keep V3 prompts unchanged.
13. Strengthen `scripts/check_v4_flow_no_llm.py` with targeted regression
    coverage:
    - a Product output containing `## Product Problem` with only `- See above`
      fails validation;
    - a Growth output with a placeholder-only required section fails
      validation;
    - a Tech output with a placeholder-only required section fails validation;
    - a valid concise role document still passes;
    - internal `Blackboard Items To Create` and `Blackboard Items To Update`
      sections may still use `- None`.
14. Update `docs/ai` memory where the V4 document contract or guardrail changed.
15. After this lot and lot 68b pass, lot 68 can be rerun for representative
    LLM validation.

## Expected Behaviors

- V4 no longer accepts human-facing documents filled with `See above`.
- Required Product, Growth, and Tech sections must contain concrete content or
  a concrete unresolved gap.
- The runtime fails early when a required section is missing or placeholder-only.
- Error messages are actionable and point to the failing role and section.
- Summaries remain derivatives and are not used to recreate missing source
  content.
- Public artifacts remain compatible with the existing viewer and artifact
  names.
- V3 prompts remain unchanged.

## Acceptance Criteria

- A required Product section containing only `- See above` fails validation.
- Required Growth and Tech sections have equivalent placeholder-only protection.
- Missing required human-facing sections fail validation.
- Empty required human-facing sections fail validation.
- `- None` remains allowed for internal blackboard operation sections and for
  explicitly optional subsections only.
- The no-LLM harness covers placeholder-only failures for Product, Growth, and
  Tech.
- V4 prompts clearly forbid cross-reference placeholders in deliverable
  sections.
- Final public artifacts do not contain placeholder-only required sections.
- `app/prompts V3/` remains untouched.
- Existing generated history and web job files remain untouched.

## Validation Commands

```bash
python3 -m compileall app
python3 scripts/check_v4_flow_no_llm.py
git diff -- app scripts docs/ai README.md outputs/workflow.md "app/prompts V4" outputs/V2
git diff -- "app/prompts V3"
git status --short outputs/tests outputs/web-jobs runs .env .env.local
```

Optional real-LLM validation, only after lots 68b and 68c pass and the
environment variables are configured:

```bash
BLACKBOARD_PROMPT_VERSION=V4 BLACKBOARD_PROJECT_NAME=CareSync python3 app/main.py
```

## Manual Verification Expected

- Read the V4 document validation code and verify it is explicit and
  role-aware.
- Verify the failed CareSync symptom `## Product Problem` plus `- See above`
  would now fail before `PRD_V0.md` is accepted.
- Verify V4 prompts forbid placeholder cross-references in human-facing
  sections.
- Verify internal blackboard item sections can still use `- None`.
- Verify no V3 prompt file changed.
- Verify public final artifacts keep the existing names and viewer-compatible
  structure.

## AGENTS.md Constraints

- Start by reading `docs/ai/00-index.yaml`.
- Keep the workflow explicit in Python.
- Do not introduce a generic document-quality framework.
- Do not use summaries to reconstruct missing source content.
- Do not modify V3 prompts.
- Do not manually edit generated run history.
- Do not touch `.env` or `.env.local`.
- Do not print real credentials.
