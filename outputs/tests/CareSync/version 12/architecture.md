## Architecture Notes
The decisive constraint is that CareSync cannot be treated as a generic coordination app: it will hold sensitive care data, so the MVP must be built around a **single launch geography with a fixed privacy/compliance baseline** and a **strict, server-enforced access model**. Without that, the permissions, retention, deletion, and audit rules are too ambiguous to implement safely.

Three structural decisions should shape the MVP:

1. **One-region, policy-locked deployment**
   - Pick one launch geography now and enforce one data handling policy set for that region.
   - Keep storage, backups, logs, and support access under the same policy boundary.
   - Do not attempt multi-country compliance in MVP.

2. **Fixed-role, server-side authorization**
   - Keep only the existing roles: coordinator, family member, caregiver.
   - Enforce all read/write access in the backend, not in the client.
   - Every resource must be scoped to a single care space and checked against role + membership.

3. **Operationally assisted trust model**
   - Build the minimum product plus an internal support/admin console.
   - Use manual onboarding, manual compliance review, and manual access recovery during pilot.
   - Keep messaging out of scope; use notifications and shared timeline events only.

Recommended implementation approach:
- Use a standard web app with a single backend API, relational database, and object storage.
- Store all care-space entities in a normalized model: care space, participant, role, task, appointment, medication reminder, note, document, audit event.
- Use row-level access checks in application code and, if available, database-level scoping for additional safety.
- Use a managed email/SMS/push provider only for reminders and invite delivery; track delivery status explicitly.
- Add soft-delete or archive with retention rules only if they are required by the launch geography; otherwise keep deletion simple and auditable.

What must be built now:
- Care space creation for one elderly relative
- Invitations and role assignment
- Server-enforced access control for all objects
- Task, appointment, medication reminder, note, and document CRUD
- Reminder scheduling and delivery status tracking
- Shared timeline/audit history
- Delete/archive behavior for care spaces and uploaded documents
- Internal admin/support console for access recovery, reminder monitoring, and account review
- Consent/notice capture and a configurable privacy policy acceptance flow for the selected geography
- Data retention/deletion workflow aligned to the selected geography

What can be handled manually or operationally first:
- Founder-led onboarding
- Help with structuring the first care space
- Compliance review for the launch geography
- Support for invitation issues and access recovery
- Monitoring reminder failures
- Document categorization and cleanup during pilot

Main modules or components:
- Auth and identity
- Care space management
- Membership and permissions
- Tasks and reminders
- Calendar/appointment records
- Medication reminder records
- Notes and activity timeline
- Document storage and retrieval
- Notification delivery and retry tracking
- Audit log
- Admin/support console
- Privacy/consent and retention controls

Critical data or workflow states:
- Care space: draft, active, archived, deleted
- Membership: invited, active, revoked
- Item states: open, completed, overdue, cancelled
- Reminder states: scheduled, sent, failed, retried, acknowledged
- Document states: uploaded, accessible, deleted, retained
- Audit events: created, updated, completed, reassigned, access_changed, deleted
- Support actions: access_reset, membership_fix, reminder_replay, document_recovery

Minimum reliability, data, permission, and control requirements:
- Every request must be authorized on the server against care-space membership and role.
- Invitation tokens must be single-use, expiring, and revocable.
- Reminder delivery must record success/failure with retry handling.
- Document access must be scoped to membership and logged.
- Deletion must be real, not only hidden in UI, unless the launch geography requires retention.
- Audit history must be immutable for operational integrity.
- Admin tooling must be restricted to staff roles with separate audit logging.
- Sensitive fields and documents must be encrypted at rest using managed infrastructure.

Control points, internal tools, or support needs:
- Admin view of care spaces, memberships, delivery failures, and audit trail
- Manual resend/revoke invitation controls
- Access recovery workflow for locked-out coordinators
- Reminder monitoring dashboard
- Delete/archive verification tool
- Export or deletion support only if required by the chosen geography
- Separate staff authentication and role restriction for support users

### Diagram Blueprint
- Main system blocks:
  - Family web app
  - Backend API
  - Auth service
  - Relational database
  - Object storage for documents
  - Notification/reminder service
  - Admin/support console
- Main flows between blocks:
  - User signs in → backend authorizes membership → reads/writes care-space data
  - Coordinator creates care space → invites participants → participants accept invitation
  - User creates task/appointment/reminder/document → backend stores record → activity log updates
  - Reminder job triggers → notification service sends message → delivery status returns to backend
  - Admin reviews support cases → admin console invokes restricted support actions
- External actors or systems:
  - Family coordinators
  - Family members
  - Caregivers
  - Email/SMS/push provider
- Admin or operations control points:
  - Invitation override
  - Membership revocation
  - Delivery failure replay
  - Access recovery
  - Data deletion/archive verification
  - Audit review

## Review Summary
The main feasibility issue is not feature scope but trust boundary definition: CareSync needs one fixed launch geography and a strict server-enforced privacy model before any pilot can be considered safe. The right direction is a narrow, operationally supported MVP with explicit retention, deletion, and access-control rules rather than a broader product build.

## Critical Assumptions
- One launch geography can be selected now and its baseline privacy/retention rules are implementable in the MVP.
- The product can operate with fixed roles and no custom permission matrix.
- Families will accept founder-assisted onboarding for the pilot.
- Reminder delivery can be implemented with visible failure states and operational monitoring.
- Support staff can be given a separate restricted admin surface without exposing sensitive data broadly.

## Requested Changes
- Define the initial launch geography and attach the minimum privacy, retention, consent, and deletion rules to it [privacy_trust]
- Add explicit user consent and policy acceptance flows for the chosen geography before first use [privacy_trust]
- Specify whether deletion is hard-delete or archive-first for each data type: care spaces, documents, audit logs, and reminders [privacy_trust]
- Constrain the permission model to a small, documented matrix for the three fixed roles [data_access]
- Require a restricted internal support console with audited staff actions before pilot launch [ops_tooling]

## Risks
- The selected geography may require stronger retention or deletion handling than the MVP can safely support [privacy_trust]
- Role-based access may be implemented inconsistently across resources if the backend model is not strictly enforced [data_access]
- Reminder delivery failures may erode trust if failure states and retries are not visible and operationally monitored [ops_tooling]
- Document handling may become a compliance liability if the storage and deletion rules are not defined precisely [privacy_trust]
- Support tooling may expose sensitive data unless staff permissions are separately designed and audited [data_access]

## Open Questions
- Which single country or region is the initial launch geography?
- For that geography, what are the minimum requirements for consent, retention, deletion, and breach handling?
- Is audit history retained after deletion, and if so, for how long?
- Which reminder channels are acceptable for the pilot: email, SMS, push, or a combination?
- What exact staff actions are allowed in the internal admin console?

## Why This Could Fail Even With Good Execution
Even with solid engineering, the project can still fail if the chosen launch geography imposes privacy or retention obligations that conflict with the simple family workflow, or if the trust model is too weak for people to store sensitive care information in a new system. In that case, the product would need a narrower data model or a different operational posture before it can be a credible MVP.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- Launch geography is undefined, so privacy, retention, consent, and deletion controls cannot be finalized [privacy_trust]
- The permission model is not specific enough to safely enforce access boundaries for sensitive care data [data_access]
- The internal support/admin surface is not yet defined, but pilot operations require audited staff controls [ops_tooling]

Required Improvements:
- Choose one initial launch geography and document the minimum privacy/compliance requirements [privacy_trust]
- Define the exact role-to-resource permission matrix for coordinator, family member, and caregiver [data_access]
- Specify the minimum internal admin actions and audit rules needed for pilot support [ops_tooling]