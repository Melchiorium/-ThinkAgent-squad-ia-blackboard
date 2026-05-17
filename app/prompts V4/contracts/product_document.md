Product document contract:

Return one JSON object with exactly the fields below. The field names are the
canonical document sections. Unless a field is documented as a structured
object below, its value is the Markdown body for that section only.

Do not write `##` headings in any value. The runtime renders the final Markdown
headings from the JSON field names. If a section needs named parts, write them
as `###` subsections inside the section body. Do not create continuation
headings such as `(cont.)` or `(continued)`.

Required JSON fields:
- Product Problem
- Initial Wedge
- First Target User
- Existing Alternatives And Switching Trigger
- Core MVP Workflow
- In Scope
- Out of Scope
- MVP Build Vs Pilot Operations
- Business Model Hypothesis
- Critical Assumptions
- How To Test Quickly
- Acceptance Criteria
- Risks And Failure Modes
- Product Readiness
- Product Arbitration
- Product Locking

Most fields are strings.

These fields are arrays of strings. Use an empty array when there is no content;
do not write "None" or "N/A" as an item:
- In Scope
- Out of Scope
- Critical Assumptions
- How To Test Quickly
- Acceptance Criteria
- Risks And Failure Modes

These fields are structured objects:

`Product Readiness`:
```json
{
  "status": "READY | LIMITED | INSUFFICIENT",
  "blocking_gaps": ["..."],
  "required_improvements": ["..."]
}
```

`Product Arbitration`:
```json
{
  "retained": ["..."],
  "deferred": ["..."],
  "rejected": ["..."],
  "open_points": ["..."],
  "rationales": ["..."]
}
```

`Product Locking`:
```json
{
  "confirmed_in_scope": ["..."],
  "confirmed_deferred": ["..."],
  "confirmed_out_of_scope": ["..."],
  "locking_note": ["..."]
}
```

If you need to discuss uncertainty, contradiction, caveats, or why the proposal
could be wrong, put that content inside the listed Risks, Open Points,
Required Improvements, or Arbitration sections. Do not create a new caveat
heading.

For Product Readiness, choose exactly one status: READY, LIMITED, or
INSUFFICIENT. The runtime renders readiness labels and Product Arbitration /
Product Locking subsections from the structured object fields.

Required human-facing sections must contain concrete content or a concrete
unresolved gap. Do not use placeholder cross-references such as See above,
As above, Same as above, TBD, To be defined, N/A, or a section that only says
None.
