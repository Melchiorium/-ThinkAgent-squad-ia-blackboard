## Architecture Notes
The main technical constraint is trust: this product only works if families are confident that sensitive care data is visible to the right people and cannot be casually exposed or edited. For MVP, the architecture should be deliberately narrow: one care circle per elder, invite-only access, and a small, explicit permission matrix tied to each data type. Do not build a flexible enterprise ACL system yet; build a few hard-coded roles and visibility rules that are easy to explain, audit, and support.

### Macro architecture choice
Use a simple multi-tenant web app with:
- authenticated users
- one care-circle domain model per elder
- role-based access control at the resource level
- event/audit logging for all sensitive actions
- notification delivery through a single provider
- manual admin tooling for overrides and support

Avoid complex workflow engines, chat, document-sharing subsystems, or deep integration layers. The MVP should be a coordination system, not a healthcare platform.

### Main technical decisions
1. **Single-circle, role-based access model**
   - One elder = one care circle.
   - Roles are fixed: `Coordinator`, `FamilyMember`, `Caregiver`, `ReadOnlySupport` if needed internally.
   - Permissions are not user-customizable in MVP; they are predefined per role and per object type.

2. **Data-type-specific visibility**
   - Tasks, appointments, reminders, and notes do not share the same visibility rules.
   - Notes are the most sensitive and should be more restricted than tasks or appointment metadata.
   - Medication schedules can be visible, but content should remain informational only, with no clinical recommendations.

3. **Auditability and support override are mandatory**
   - Every create/update/delete/invite/role-change/access-denied event must be logged.
   - Admins need a controlled override path for invite recovery and role correction.
   - Overrides should be logged and visible to support staff to preserve trust.

### Recommended implementation approach
Build a standard CRUD application with:
- Postgres as system of record
- backend policy checks for every API request
- notification jobs for reminders
- append-only audit log table
- admin support console for emergency fixes
- email and/or SMS notifications only, not in-app chat

This can be implemented as a monolith with a small set of services or modules. A single backend is preferable for MVP delivery and to keep policy enforcement centralized.

### What must be built now
The smallest proof-capable product must include:
- secure sign-up / invite acceptance
- care circle creation
- fixed roles and permission checks
- task creation, assignment, completion
- appointment entry and reminder delivery
- medication reminder schedule and reminder delivery
- care notes feed with restricted visibility
- audit log for sensitive actions
- admin support tools for invite recovery and role correction
- basic notification preferences and delivery status

### What can be handled manually or operationally first
- First-circle onboarding and data entry
- Role assignment review for pilot families
- Manual correction of mistaken permissions through support
- Manual compliance review for the first geography
- White-glove troubleshooting for reminders and invitations
- Manual follow-up if a notification fails or is delayed

### Main modules or components
- **Identity & Invitations**
  - invite-only onboarding
  - email/phone verification
  - invite acceptance flow
- **Care Circle Service**
  - elder profile
  - family/caregiver membership
  - role assignment
- **Coordination Module**
  - tasks
  - appointments
  - medication reminders
  - care notes
- **Authorization Layer**
  - role-based policy enforcement
  - object-level visibility filtering
- **Notification Service**
  - scheduled reminders
  - delivery tracking
- **Audit Log**
  - immutable event records
- **Admin/Support Console**
  - invite recovery
  - role fixes
  - access review
  - audit lookup

### Critical data or workflow states
- `circle_created`
- `invite_sent`
- `invite_accepted`
- `member_active`
- `role_assigned`
- `task_open / task_done / task_overdue`
- `appointment_scheduled / reminder_sent / reminder_acknowledged`
- `medication_schedule_active / reminder_sent / reminder_acknowledged`
- `note_created / note_updated / note_deleted`
- `access_revoked`
- `admin_override_applied`

These states must be explicit because trust depends on being able to explain who can see what and what changed.

### Minimum trust and privacy control set for MVP
This is the required minimum, not optional:

- **Invite-only access**
  - No public links
  - No self-join
  - Every participant must be explicitly invited

- **Fixed roles**
  - Coordinator: full control over the circle
  - FamilyMember: can view and act on assigned/shared coordination items
  - Caregiver: can view assigned operational items and relevant notes only
  - No arbitrary permission editing in MVP

- **Object-level visibility**
  - Tasks: visible to all active circle members unless marked restricted
  - Appointments: visible to all active circle members, with optional restricted detail fields if needed
  - Medication reminders: visible to the circle, but editable only by Coordinator
  - Notes: restricted by default to Coordinator and designated caregivers only
  - If a note is sensitive, it must be explicitly marked and only shown to allowed roles

- **Edit restrictions**
  - Only Coordinator can change roles, revoke access, and edit medication schedules
  - Family members can update tasks assigned to them or shared tasks
  - Caregivers can complete tasks assigned to them and add care notes if granted
  - No one can silently broaden visibility

- **Audit trail**
  - Log access changes, role changes, content edits, deletes, and admin overrides
  - Support staff need searchable audit lookup
  - Users should be able to see recent changes in activity history

- **Data minimization**
  - Store only what is needed for coordination
  - Avoid clinical decision support language
  - Avoid storing highly sensitive medical history in notes unless essential for care coordination

- **Notification safety**
  - Notifications must not expose sensitive note content in lock-screen previews by default
  - Reminder messages should be generic unless the user opts in
  - Delivery should be retryable and status-tracked

### Control points, internal tools, or support needs
- Admin console for:
  - re-sending invites
  - changing a broken role assignment
  - disabling access
  - checking delivery failures
  - reviewing audit history
- Support playbook for:
  - mistaken invitations
  - duplicate accounts
  - revoked caregiver access
  - notification complaints
- Manual approval process for the first pilot families if compliance or trust requires it

### Diagram Blueprint
**Main system blocks**
- Web/mobile client
- Auth and invite service
- Care circle service
- Coordination data service
- Authorization/policy layer
- Notification scheduler/provider
- Audit log store
- Admin/support console
- Postgres database

**Main flows between blocks**
- User accepts invite → auth service → membership created
- Coordinator creates tasks/appointments/notes → policy check → coordination store
- Scheduler reads reminder state → notification provider → delivery status update
- Any sensitive write/read → authorization layer → audit log write
- Support admin action → admin console → policy override → audit log

**External actors or systems**
- Family coordinator
- Family members
- Caregiver
- Email/SMS provider

**Admin or operations control points**
- invite recovery
- role correction
- access revocation
- delivery retry
- audit review

## Review Summary
The biggest feasibility issue is not feature breadth but trust: the MVP needs a simple, enforceable permission model that families can understand and support can repair. The safest direction is a narrow invite-only care circle with fixed roles, object-level visibility rules, and mandatory audit logging, while keeping everything else operationally manual where possible.

## Critical Assumptions
- One care circle per elder is sufficient for the MVP.
- Families will accept fixed roles rather than custom permissions.
- Notes can be safely restricted more tightly than tasks and appointments.
- Notification delivery via email/SMS is adequate for the pilot.
- A manual support process can handle early permission mistakes without breaking trust.

## Requested Changes
- Define the exact role-to-data visibility matrix for tasks, appointments, medication reminders, and notes. [privacy_trust]
- Make notes explicitly more restricted than tasks and appointments, with default private visibility and explicit sharing. [privacy_trust]
- Add a non-negotiable audit requirement for all permission and access changes. [privacy_trust]
- Clarify that invite-only access is the only onboarding path in MVP; no self-serve public joining. [scope]
- Add a support/admin recovery flow as a first-class MVP requirement for role fixes and access revocation. [operations]

## Risks
- Families may not understand the fixed roles and may expect flexible sharing. [privacy_trust]
- A single mistake in permissions or notifications could permanently damage trust. [privacy_trust]
- Support overhead may be higher than expected if invite and role recovery is frequent. [operations]
- Reminder delivery failures could make the product appear unreliable even if core data is correct. [operations]
- Storing too much care detail too early may create compliance exposure across launch geographies. [compliance_scope]

## Open Questions
- Which exact fields inside a note are visible to caregivers versus family members? [privacy_trust]
- Are reminders allowed to reveal medication names in notifications, or must they remain generic? [privacy_trust]
- Should caregivers be able to create notes, or only append comments/updates? [privacy_trust]
- What is the minimum support SLA for invite recovery and access correction during pilot? [operations]
- Which launch geography defines the compliance baseline for stored care data? [compliance_scope]

## Why This Could Fail Even With Good Execution
Even with solid engineering, the product can fail if the permission model still feels too risky or too confusing for families to trust with sensitive care information. If users cannot instantly understand who can see what, or if one bad access event undermines confidence, they will fall back to chat threads and paper regardless of feature quality.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- Exact role-to-data visibility rules are still not fully specified for notes, appointments, tasks, and reminders. [privacy_trust]
- Notification content policy for sensitive care data is not defined. [privacy_trust]
- Admin/support recovery workflow is required but not yet operationalized as a controlled process. [operations]

Required Improvements:
- Publish a fixed permission matrix with default visibility and edit rights per role and object type. [privacy_trust]
- Define safe notification payload rules, including what can appear in email/SMS previews. [privacy_trust]
- Implement an audit-backed support console and a documented recovery workflow for invite and role mistakes. [operations]