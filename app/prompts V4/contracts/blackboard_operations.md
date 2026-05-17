Blackboard operations contract:

Return one JSON object only. Do not return Markdown, headings, commentary, or a
code fence.

Required wrapper:

```json
{
  "create": [],
  "update": []
}
```

Create operations must contain exactly:
- type
- targets
- priority
- tags
- title
- content

Update operations must contain exactly:
- id
- status

Allowed types: QUESTION, RISK, DECISION, PROPOSAL, FEEDBACK, WARNING,
CONSTRAINT.

Allowed statuses: OPEN, ANSWERED, ACCEPTED, REJECTED, OBSOLETE.

Allowed priorities: LOW, MEDIUM, HIGH, CRITICAL.

Allowed targets: PRODUCT, GROWTH, TECH, ALL, EXTERNAL.

Rules:
- Phase-specific runtime constraints can narrow these allowed operations. If the
  phase context says `create` must be empty, return `"create": []`.
- Role-specific runtime constraints can narrow create targets. If the runtime
  lists allowed create targets, use only those targets.
- Do not include an author field. The runtime assigns the author from the
  current role.
- Do not create an item targeted only to your own role; resolve it directly in
  your document instead.
- Use EXTERNAL only when no Product, Growth, or Tech agent can decide from the
  available run context. EXTERNAL must be the only target when used.
- Update only pre-existing item ids shown in the runtime context.
- If there is no valid operation, return empty arrays.
