## Architecture Notes
The main constraint is not feature breadth; it is whether CareSync can safely handle sensitive care coordination data with a permission model simple enough for families to understand and support without creating trust failures. For the MVP, choose a **single launch market** and implement a **centralized, role-based workspace with object-level visibility controls**. Do not attempt cross-country compliance, EHR-like records, or rich chat.

Three structural decisions should shape the MVP:

1. **Single-tenant-per-care-recipient workspace model**
   - One care space maps to one elderly person.
   - One organizer owns the workspace lifecycle.
   - All data hangs off that workspace, not a global family account model.

2. **Fixed roles with object-level access, not advanced ACLs**
   - Roles: organizer, family member, caregiver, admin/support.
   - Permissions are applied at the object type level first: tasks, appointments, reminders, updates, documents.
   - Keep permissions coarse but explicit; avoid arbitrary sharing rules.

3. **Structured coordination only**
   - No free-form messaging replacement in MVP.
   - Use task/appointment comments or updates with templates.
   - This reduces moderation, audit complexity, and ambiguity around sensitive data.

### Concrete minimum privacy and trust control set for MVP
This is the minimum that must exist before launch:

- **Workspace invite gating**
  - Only invited users can access a care space.
  - Invite links expire.
  - Organizer approves membership before activation.

- **Role-based visibility**
  - Organizer: full access within the space.
  - Family member: read/write on tasks, appointments, updates; read-only on documents unless explicitly granted.
  - Caregiver: read/write on assigned tasks, appointments, and updates; limited document access only to documents flagged as shareable.
  - Support/admin: no default access to care content; break-glass access only for support incidents, with audit logging.

- **Object-level sharing defaults**
  - Documents default to private to organizer.
  - Appointment/task/update visibility defaults to workspace members only.
  - Any exception must be explicitly set by organizer.

- **Consent and acknowledgement**
  - Organizer must confirm they have authority to share information for the care recipient.
  - Invitees must accept that they are joining a sensitive care space.
  - Record timestamped consent/acknowledgement per member.

- **Audit trail**
  - Track who created, changed, viewed, or revoked access to each core object.
  - Track invite creation and acceptance.
  - Track document upload/download events where feasible.

- **Access revocation**
  - Organizer can revoke a member instantly.
  - Revocation must cut off future access immediately.
  - Optional session invalidation for already logged-in devices.

- **Data minimization**
  - Collect only the care-recipient identity, basic contacts, schedule items, tasks, and documents needed for coordination.
  - Avoid clinical fields beyond what is necessary for reminders and reference.

- **Support controls**
  - Internal support cannot browse content by default.
  - Support can only assist via ticket-bound, time-limited access approval or redacted metadata view.

### Recommended implementation approach
Build a **centralized web app with a managed backend**:
- frontend: web-first responsive app
- backend: single API service
- database: relational store for workspace, roles, tasks, appointments, reminders, and audit events
- file storage: separate encrypted object storage for documents
- notifications: asynchronous job queue for email/SMS/push delivery
- auth: email/password or magic-link plus optional MFA for organizers

This is the simplest architecture that can prove the workflow safely.

### What must be built now
- Workspace creation for one care recipient
- Invite flow and role assignment
- Core data models for tasks, appointments, reminders, updates, documents
- Permission enforcement at the API layer
- Audit log for access and changes
- Notification sending for reminders and changes
- Organizer controls for revocation and invite correction
- Basic consent acknowledgement on onboarding

### What can be handled manually or operationally first
- White-glove onboarding
- Manual confirmation of consent/authority during pilot
- Manual review of launch-market privacy requirements
- Manual support for document handling issues
- Manual escalation when permission questions arise
- Manual reminder fallback if delivery failures occur during pilot

### Main modules or components
- **Identity and access**
  - users, invites, roles, sessions, consent acknowledgement
- **Workspace service**
  - care space, care recipient profile, membership lifecycle
- **Coordination objects**
  - appointments, tasks, reminders, updates/comments
- **Document service**
  - upload, metadata, access flags, storage
- **Notification service**
  - reminder scheduling, delivery, retries, failure tracking
- **Audit and activity log**
  - immutable event history for admin and organizer review
- **Admin/support console**
  - invite correction, membership revocation, ticket-linked support actions

### Critical data or workflow states
- Invite: pending, accepted, expired, revoked
- Membership: active, suspended, revoked
- Task: open, assigned, in progress, done, overdue
- Appointment: scheduled, rescheduled, completed, canceled
- Reminder: scheduled, sent, failed, acknowledged
- Document: uploaded, shareable/private, revoked, deleted
- Consent: acknowledged, withdrawn if required by policy
- Audit event: created, changed, viewed, revoked, delivered

### Minimum reliability, data, permission, and control requirements
- Permission checks on every API read/write
- No direct client-side trust for visibility decisions
- Encrypted storage for documents and sensitive records
- Delivery retries with failure logging for notifications
- Idempotent reminder dispatch to prevent duplicate sends
- Immediate revoke propagation
- Time-stamped audit records with actor identity
- Basic rate limiting and abuse protection on invites

### Control points, internal tools, or support needs
- Support console for invite correction and access revocation
- Admin review queue for suspicious invite or access activity
- Manual fallback path for reminder failures
- Exportable audit trail for incident review
- Simple consent/authority checklist for onboarding staff

### Diagram Blueprint
- **Main system blocks**
  - Web/mobile frontend
  - Auth and invite service
  - Workspace and permission service
  - Coordination data service
  - Document storage service
  - Notification queue/delivery service
  - Audit log service
  - Admin/support console

- **Main flows between blocks**
  - Organizer creates workspace -> permission service initializes roles
  - Organizer invites members -> auth service issues expiring invite
  - Members accept invite -> membership activated -> audit logged
  - Organizer adds task/appointment/document -> coordination service stores object -> permission checks applied
  - Reminder scheduled -> notification service sends delivery -> delivery status logged
  - Access change/revocation -> permission service updates membership -> sessions invalidated -> audit event emitted

- **External actors or systems**
  - Organizer
  - Family member
  - Professional caregiver
  - Email/SMS provider
  - Storage provider

- **Admin or operations control points**
  - Support console for revocation and invite correction
  - Audit review for access incidents
  - Manual consent/authority verification during pilot

## Review Summary
The key feasibility issue is not the care workflow itself but building a trustable, legally cautious access model for sensitive coordination data. The MVP should be a single-workspace, role-based system in one launch market, with object-level visibility, consent acknowledgement, immutable audit logs, and immediate revocation; everything else can stay manual until the pilot proves repeated use.

## Critical Assumptions
- One launch market can be chosen with a clear minimum privacy/consent baseline.
- The organizer can legitimately grant access to the care-related information being shared.
- A coarse role model is sufficient for the pilot without advanced sharing rules.
- Families will accept structured updates instead of free-form chat.
- Notification delivery through standard providers is reliable enough for reminder use.

## Requested Changes
- Define the launch country or region and lock the minimum privacy/consent requirements before build. [privacy_trust]
- Add explicit consent/authority acknowledgement during organizer onboarding. [privacy_trust]
- Specify object-level default visibility for tasks, appointments, reminders, updates, and documents. [privacy_trust]
- Add a support-only revocation and access correction workflow with audit logging. [operations]
- Clarify which document types are shareable by default versus organizer-private. [privacy_trust]

## Risks
- A coarse permission model may still be too weak for some families or too complex for quick setup. [privacy_trust]
- Sensitive data handling may trigger higher compliance expectations than the MVP can support. [privacy_trust]
- Reminder failures or duplicate sends could quickly damage trust. [operations]
- If organizer authority is ambiguous, the product may be unsafe to launch in practice. [privacy_trust]
- Support access mishandling could expose private care information. [operations]

## Open Questions
- Which single launch market will define the initial privacy and consent baseline? [privacy_compliance]
- What exact authority does the organizer have to share information about the elderly relative? [privacy_trust]
- Should caregivers be able to view all appointments or only assigned items? [privacy_trust]
- Are documents restricted to organizer-visible by default, or can some be workspace-wide? [privacy_trust]
- Is email/SMS sufficient for reminders, or is push notification required for pilot reliability? [operations]

## Why This Could Fail Even With Good Execution
Even with clean implementation, the project can fail if families do not trust the organizer-centered permission model enough to share sensitive information, or if the platform’s structure is still less convenient than existing texts and calendars. In that case, the product remains technically correct but operationally unused.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- Launch geography and minimum privacy/consent baseline are not yet locked. [privacy_compliance]
- Organizer authority and member visibility rules are underspecified for sensitive data. [privacy_trust]
- Support and revocation handling need a defined controlled workflow. [operations]

Required Improvements:
- Select one launch market and define the minimum compliance baseline. [privacy_compliance]
- Add explicit consent/authority acknowledgement and object-level default permissions. [privacy_trust]
- Implement a support console for invite correction and immediate revocation with audit logging. [operations]