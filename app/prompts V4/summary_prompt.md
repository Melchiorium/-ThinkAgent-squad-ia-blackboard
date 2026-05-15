You are writing a summary only.

The summary must be strictly grounded in one source document.
Do not introduce new information, guesses, or derived facts that are not present in the source document.
Treat the source document as the only source of truth.

Return YAML only.
Return no markdown fences.
Return no commentary.

Required shape:

summary:
  source_document: <exact source document path>
  source_hash: <exact source hash>
  scope: |
    <short grounded scope summary>
  key_decisions:
    - <short grounded decision>
  unresolved_questions:
    - <short grounded question>
  critical_risks:
    - <short grounded risk>

Rules:
- source_document and source_hash must match the provided values exactly.
- scope must be a compressed description of the source document's scope.
- key_decisions, unresolved_questions, and critical_risks must stay short and specific.
- only these fields are allowed under `summary`.
- list items must be indented under their field with four spaces.
- never put a list item directly under `summary`.
- never add headings, commentary, or extra fields.
- use `    - None` when a list field is empty.
- keep the summary readable by a human developer.
