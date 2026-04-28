## Architecture Notes
The main technical constraint is **trustworthy handling of sensitive care data without overbuilding compliance or permissions**. For an MVP, the safest path is a **single-tenant-like care-space model on a standard web app**, with **fixed roles, object-level access rules, audit logging, and a manual support backstop**. Do not build a flexible permission engine or chat-like messaging system now; that will increase risk without improving proof.

### Structural decisions
1. **Fixed permission matrix, not custom sharing**
   - Use a small set of roles: `coordinator`, `family_member`, `caregiver`, `viewer/admin_support`.
   - Apply permissions by object type: `appointments`, `tasks`, `updates`, `documents`, `emergency_contacts`.
   - Store permissions centrally and enforce them on every read/write/download action.

2. **Care-space as the core security boundary**
   - One care space = one elder / one shared coordination context.
   - All objects belong to exactly one care space.
   - No cross-space visibility, no agency hierarchy, no multi-recipient graphs.

3. **Explicit activation gate before any sensitive sharing**
   - A care space is created in `draft` state.
   - It becomes `active` only after coordinator completes access review and consent confirmation.
   - Sensitive object sharing and invitations should be blocked until activation is complete.

### Recommended implementation approach
Use a conventional SaaS stack with:
- frontend: mobile-first web app
- backend API: monolith
- database: relational DB with row-level tenancy by care_space_id
- file storage: encrypted object storage for documents
- notifications: email/SMS/push via external provider
- audit log: append-only table with immutable event entries
- admin console: internal support view for permission review, revocation, and resend/recovery actions

Avoid microservices. Avoid event-driven complexity beyond notification jobs and audit events.

### What must be built now
- Care-space creation and invitation flow
- Fixed role assignment and role-to-object permission matrix
- Access review / consent confirmation at activation
- Read/write enforcement for all core objects
- Document upload/download access controls
- Emergency contact visibility controls
- Audit log for permission changes, uploads, downloads, revocations, and activation
- Notification delivery with status tracking
- Revocation flow and support escalation path
- Basic internal admin tools for troubleshooting access and invitations

### What can be handled manually or operationally first
- Support-led onboarding and setup
- Manual help mapping current coordination items into the system
- Manual recovery for failed invitations or reminder delivery issues
- Manual handling of permission disputes during pilot
- Manual review of whether the family should activate a care space before sharing documents
- Manual validation of recurring reminder usefulness

### Main modules or components
- **Identity and invitation service**
  - invite links, email/phone verification, membership acceptance
- **Care-space service**
  - creation, activation state, membership, role assignment
- **Permission service**
  - fixed authorization rules by role and object type
- **Task/calendar module**
  - appointments, recurring tasks, completion states
- **Updates module**
  - structured status updates attached to tasks/events
- **Document module**
  - secure upload, metadata, controlled download
- **Notification module**
  - reminder scheduling, delivery tracking, retry state
- **Audit log module**
  - immutable record of sensitive actions
- **Admin/support console**
  - revoke access, resend invite, inspect audit trail, resolve delivery failures

### Critical data or workflow states
- `draft` → `active` care space
- invitation states: `sent`, `accepted`, `expired`, `revoked`
- object states:
  - task/event: `open`, `scheduled`, `completed`, `overdue`
  - update: `draft`, `posted`
  - document: `uploaded`, `available`, `revoked`
- access states:
  - `pending_review`, `approved`, `revoked`
- notification states:
  - `queued`, `sent`, `delivered`, `failed`, `retried`

### Minimum reliability, data, permission, or control requirements
- Every sensitive read/download must check authorization server-side
- Every permission change must create an audit event
- Every invitation must expire and be revocable
- Every document must be encrypted at rest and access-logged
- Every reminder must have a visible delivery status and retry path
- A revoked member must lose access immediately, including document access links
- Activation must require explicit coordinator confirmation that the invited people are allowed to see the space

### Control points, internal tools, or support needs
- Internal support console for:
  - resend invite
  - revoke user access
  - inspect permission state
  - view reminder delivery failures
  - view audit history for a care space
- Manual support workflow for:
  - permission disputes
  - accidental invitation recovery
  - document access complaints
- A trust gate in the product UI:
  - show who can see what
  - require coordinator acknowledgment before activation
  - require confirmation before adding sensitive documents

### Diagram Blueprint
- **Main system blocks**
  - Web/mobile frontend
  - API/backend monolith
  - relational database
  - secure object storage
  - notification provider
  - internal admin console
- **Main flows between blocks**
  - invite creation → notification provider → invite acceptance
  - care-space draft → access review → active state
  - task/event creation → reminder job → notification delivery
  - document upload → object storage → permission-checked download
  - sensitive action → audit log write
- **External actors or systems**
  - coordinator
  - family member
  - caregiver
  - notification provider
- **Admin or operations control points**
  - revoke access
  - resend invitation
  - inspect audit log
  - check notification failures
  - resolve permission disputes

## Review Summary
The key feasibility issue is not feature breadth but whether the product can safely expose sensitive care data with a fixed permission model that families trust. The right MVP is a single-care-space, server-enforced access-control system with explicit activation, auditability, and manual support for edge cases—not a flexible collaboration platform.

## Critical Assumptions
- The family can accept a fixed role model without needing custom sharing rules.
- Server-side enforcement plus audit logs are enough to establish baseline trust for pilot users.
- A manual support backstop is acceptable during the MVP.
- One care space per elder is sufficient to prove coordination value.
- Reminder delivery can be implemented with acceptable reliability through a standard notification provider.

## Requested Changes
- Add an explicit **privacy/trust gate** before activation: show participants, roles, and exactly which object types they can access.
- Define the **role-to-object permission matrix** for tasks, events, updates, documents, and emergency contacts.
- Require **coordinator consent confirmation** before the care space becomes active and before sensitive documents are shared.
- Add a **revocation and dispute workflow** with immediate access removal and support escalation.
- Specify **reminder delivery reliability rules** for the pilot, including delivery status visibility and retry behavior.

## Risks
- Families may still distrust shared document storage even with fixed permissions.
- A fixed role model may be too rigid for some real caregiving arrangements.
- Notification failures could undermine the core trust loop.
- Manual support load may be high during onboarding and revocation cases.
- If caregivers do not post updates, the coordination record will remain incomplete.

## Open Questions
- Which exact document types are allowed in MVP, and which are blocked?
- Should caregivers be able to upload documents or only comment on task/event updates?
- What are the default permissions for emergency contacts: view-only or editable by coordinator only?
- What notification channels are in scope for pilot trust: email, SMS, push, or all three?
- What is the minimum support response time required for revoked access and invite failures?

## Why This Could Fail Even With Good Execution
Even if the build is implemented correctly, the project can still fail if families do not believe a fixed permissioned space is safer or easier than their current chat-and-phone workflow. In that case, the product remains technically sound but never becomes the trusted shared record needed to replace even a small portion of existing coordination.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- No concrete role-by-role access policy for sensitive objects [privacy_trust]
- No defined trust gate before first sharing of documents or private updates [privacy_trust]
- No confirmed support workflow for permission disputes or revocation [operations]
- Reminder delivery requirements are not specified tightly enough for pilot trust [metrics_validation]

Required Improvements:
- Define and implement a fixed permission matrix for tasks, events, updates, documents, and emergency contacts [privacy_trust]
- Add an explicit access review and consent step at care-space activation [privacy_trust]
- Build immediate revocation plus internal support tooling for access disputes and recovery [operations]
- Specify delivery-status visibility and retry rules for reminders [metrics_validation]