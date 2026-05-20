Growth document contract:

Return one JSON object with exactly the fields below. The field names are the
canonical document sections. Unless a field is documented as a structured
object below, its value is the Markdown body for that section only.

Do not write `##` headings in any value. The runtime renders the final Markdown
headings from the JSON field names. If a section needs named parts, write them
as `###` subsections inside the section body. Do not create continuation
headings such as `(cont.)` or `(continued)`.

Required JSON fields:
- Go-To-Market Notes
- Review Summary
- Build Vs Pilot Operations
- Critical Assumptions
- Requested Changes
- Risks
- Open Questions
- Why This Could Fail Even With Good Execution
- GTM Readiness

Most fields are strings.

These fields are arrays of strings. Use an empty array when there is no content;
do not write "None" or "N/A" as an item:
- Critical Assumptions
- Requested Changes
- Risks
- Open Questions
- Why This Could Fail Even With Good Execution

These fields are structured objects:

`Build Vs Pilot Operations`:
```json
{
  "must_be_productized_now": ["..."],
  "can_stay_manual_or_operational_during_pilot": ["..."],
  "deferred_until_after_proof": ["..."]
}
```

`GTM Readiness`:
```json
{
  "status": "READY | LIMITED | INSUFFICIENT",
  "blocking_gaps": ["..."],
  "required_improvements": ["..."]
}
```

The runtime renders Build Vs Pilot Operations subsections and GTM Readiness
labels from the structured object fields.
If you need to discuss uncertainty, contradiction, caveats, or why the GTM plan
could be wrong, put that content inside Risks, Open Questions, Requested
Changes, Why This Could Fail Even With Good Execution, or GTM Readiness. Do
not create a new caveat heading.

For GTM Readiness, choose exactly one status: READY, LIMITED, or INSUFFICIENT.
If `status` is READY, `blocking_gaps` must be empty. If `blocking_gaps` is not
empty, `required_improvements` must contain the concrete action needed to remove
the gap; otherwise move the point out of `blocking_gaps`.

Required human-facing sections must contain concrete content or a concrete
unresolved gap. Do not use placeholder cross-references such as See above,
As above, Same as above, TBD, To be defined, N/A, or a section that only says
None.
