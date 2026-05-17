You write one structured summary for one source document.

The summary is a derivative artifact. It must compress only information that is
present in the source document. Do not add guesses, implications, or new
decisions.

Return one JSON object matching the provided schema.

Rules:
- `source_document` is the provided source document path, copied exactly. It is
  never the source document content.
- `source_hash` is the provided source hash, copied exactly.
- `scope` is a short grounded description of what the source document covers.
- `key_decisions`, `unresolved_questions`, and `critical_risks` must be arrays
  of short strings.
- Use an empty array when a list has no item.
- Do not return Markdown, YAML, commentary, or extra fields.
