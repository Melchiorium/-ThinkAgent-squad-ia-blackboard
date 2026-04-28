## Architecture Notes
The main technical constraint is **trustworthy handling of sensitive care data with simple, enforceable access control**. For this MVP, the safest path is a **single-tenant-per-care-space logical model on a shared application stack** rather than trying to build a complex multi-org healthcare platform. The system should prove one reliable coordination workflow end-to-end before any deeper automation.

### Macro architecture choice
Use a **modular monolith** with:
- one web app
- one backend API
- one relational database
- one object store for documents
- one notification service integration
- one audit/event log

This is the simplest architecture that can support invite-based family coordination, role permissions, reminders, document sharing, and an activity history without introducing distributed-system complexity too early.

### Structural technical decisions
1. **Care-space scoped data model**
   - Every record belongs to exactly one care space.
   - All access checks are enforced against care-space membership and role.
   - No cross-care-space sharing in MVP.

2. **Permission model must be explicit, not implied**
   - Roles: owner/admin, family member, caregiver, viewer.
   - Permissions should be coarse and predictable for MVP.
   - Document visibility, task edit rights, and reminder edits must be tied to role.

3. **Notifications must be scheduled, persisted, and auditable**
   - Reminder jobs should be stored as records, not only derived on the fly.
   - Each delivery attempt should have a status.
   - Users need to see what was scheduled, sent, failed, or dismissed.

### Recommended implementation approach
Build the MVP as a **single backend service** with these bounded modules:
- authentication and invites
- care-space management
- appointments
- tasks
- medications
- documents
- notifications
- activity/audit log
- role and access control

Use managed infrastructure where possible:
- managed Postgres
- object storage for files
- email/SMS/push via a provider
- scheduled jobs/queue for reminders

### What must be built now
- Care space creation for one elder relative
- Invite flow with acceptance and membership tracking
- Role-based access control
- Appointment CRUD with reminder scheduling
- Task CRUD with assignment and completion states
- Medication reminder entries with simple recurrence rules
- Document upload, storage, retrieval, and access restriction
- Activity timeline showing who changed what
- Notification sending plus basic delivery status tracking
- Admin/support tooling for user lookup, invite resend, record inspection, and account recovery

### What can be handled manually or operationally first
- Family onboarding and first care-space setup
- Migration of existing notes/docs into the system
- Confirming caregiver participation
- Troubleshooting reminder preferences and notification delivery issues
- Initial compliance review and market-specific policy guidance
- First-line support for older or low-digital-literacy users

### Main modules or components
- **Auth and identity**: login, session, invite acceptance
- **Care space service**: elder profile, membership, roles
- **Appointments module**: events, dates, reminder rules
- **Tasks module**: ownership, status, due dates, completion history
- **Medication module**: medication name, schedule, reminder instances
- **Documents module**: upload, metadata, access control, download/view
- **Notification engine**: queue, schedule, send, retry, log
- **Activity log**: immutable record of changes and key actions
- **Admin console**: internal support and audit review

### Critical data or workflow states
- **Care space**: draft, active, archived
- **Invitation**: pending, accepted, expired, revoked
- **Member**: invited, active, suspended
- **Task**: open, claimed, completed, overdue, cancelled
- **Appointment**: planned, updated, cancelled, completed
- **Medication reminder**: active, paused, expired
- **Document**: uploaded, available, deleted, restricted
- **Notification**: queued, sent, delivered, failed, dismissed

### Minimum reliability, data, permission, or control requirements
- All access must be checked server-side on every request
- Documents must never be publicly accessible
- Invitations must be single-use or tightly bound to the intended recipient
- Activity entries should be append-only
- Notification sending must be idempotent to avoid duplicate reminders
- Failed reminders must be visible in the admin console
- Basic retention and deletion rules must exist for sensitive data
- Support staff need constrained internal access with full audit logging

### Control points, internal tools, or support needs
- Invite resend and revocation
- Membership removal and role changes
- Reminder replay or suppression
- Document access troubleshooting
- Audit log search by care space, user, or time window
- Support flag for emergency account recovery without exposing full document content

### Diagram Blueprint
- **Main system blocks**
  - Web app
  - Backend API
  - Postgres database
  - Object storage
  - Notification provider
  - Job scheduler/queue
  - Admin console

- **Main flows between blocks**
  - User login/invite acceptance → backend API → database
  - Appointment/task/medication changes → backend API → database → activity log
  - Reminder scheduling → database → job queue → notification provider → recipient
  - Document upload/view → backend API → object storage → access check
  - Support actions → admin console → backend API → audit log

- **External actors or systems**
  - Family members
  - Caregivers
  - Email/SMS/push provider

- **Admin or operations control points**
  - Invite management
  - Membership and role changes
  - Notification failure review
  - Audit log inspection
  - User support and account recovery

## Review Summary
The MVP is technically feasible only if it stays centered on one care-space, one permission model, and a reliable reminder/audit pipeline. The biggest risk is not feature breadth but trust: if access control, document handling, and notifications are not dependable and auditable, the product will not be safe enough for sensitive family care use.

## Critical Assumptions
- The initial launch market can be served with a simple role-based access model.
- Reminder delivery can be made sufficiently reliable with a standard notification provider and retry logic.
- Families will tolerate a lightweight onboarding flow that is partly supported by manual setup.
- The MVP does not require EMR integration or clinical-grade interoperability.
- Basic audit logs and document restrictions are sufficient for pilot use in the chosen market.

## Requested Changes
- Define the exact minimum permission matrix for owner, family member, caregiver, and viewer [privacy_trust]
- Specify the initial launch country or compliance boundary so data handling rules are implementable [privacy_trust]
- Narrow medication support to simple reminder schedules, not full medication management [privacy_trust]
- Add explicit support for support/admin tooling in the MVP scope [privacy_trust]
- Clarify notification channels for MVP and which ones are required versus optional [privacy_trust]

## Risks
- Reminder logic may become unreliable if recurrence rules are too flexible too early [reliability]
- A weak permission model could expose documents or updates to the wrong participant [privacy_trust]
- Support burden may be high if onboarding is not partially concierge-assisted [market_motion]
- Older or low-digital-literacy users may struggle if the UI assumes self-service setup [user_validation]
- Compliance ambiguity across countries could block release or force rework [privacy_trust]

## Open Questions
- Which country or regulatory scope is the first MVP constrained to?
- What exact notification channels are required at launch: email, SMS, push, or all three?
- Can caregivers be invited with view-only access, or must they be able to update tasks and notes?
- What document types are allowed in MVP, and are any restricted by policy?
- What is the minimum support workflow for account recovery, invite errors, and role changes?

## Why This Could Fail Even With Good Execution
Even with solid engineering, the project can fail if families do not treat the care-space as the authoritative coordination source. If the product does not quickly become more trusted and easier than existing messaging and note-taking habits, users will keep coordination fragmented and the MVP will remain a parallel record rather than the system of record.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- The compliance boundary and initial data-handling policy are undefined, which prevents a safe data model and access strategy [privacy_trust]
- The minimum role and permission matrix is not precise enough to implement trustworthy access control [privacy_trust]
- Notification reliability requirements and delivery channels are not specified, which blocks reminder architecture decisions [reliability]

Required Improvements:
- Choose the first launch jurisdiction and define the minimum privacy/compliance constraints [privacy_trust]
- Finalize an explicit permission matrix for all MVP roles and actions [privacy_trust]
- Define required notification channels and acceptable delivery failure behavior [reliability]
- Add internal support/admin requirements for invite recovery, role changes, and audit inspection [privacy_trust]