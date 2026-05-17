Phase: finalization

Produce the final document for your role.

Product locks the final PRD first. Growth reads the final PRD and finalizes the
GTM. Tech reads the final PRD and final GTM and finalizes the architecture.

Finalization is freeze-only. Do not create new blackboard items. In the
separate blackboard JSON response, `create` must be empty: `[]`.

Do not reopen decisions during finalization. Update a routed item only when the
final document directly addresses it. Leave EXTERNAL items open and surface
them as explicit assumptions or decisions required outside the run.

Integrate resolved blackboard decisions into the final document. Do not leave a
resolved decision listed as an open point, open question, or blocking gap.
