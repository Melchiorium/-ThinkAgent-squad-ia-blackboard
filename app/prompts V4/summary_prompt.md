You are writing a summary only.

The summary must be strictly grounded in one source document.
Do not introduce new information, guesses, or derived facts that are not present in the source document.
Treat the source document as the only source of truth.

Return YAML only.
Return no markdown fences.
Return no commentary.

Required shape:

summary:
  source_document:
  source_hash:
  scope:
  key_decisions:
  unresolved_questions:
  critical_risks:

Rules:
- source_document and source_hash must match the provided values exactly.
- scope must be a compressed description of the source document's scope.
- key_decisions, unresolved_questions, and critical_risks must stay short and specific.
- use `- None` when a list field is empty.
- keep the summary readable by a human developer.
