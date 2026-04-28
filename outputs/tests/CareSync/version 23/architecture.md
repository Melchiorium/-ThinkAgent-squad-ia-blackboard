## Architecture Notes
The main technical constraint is **sensitive care data handling under an undefined jurisdiction**: without a fixed launch geography and baseline privacy posture, the MVP cannot be safely built as a general-purpose health product. The simplest viable architecture is a **single-tenant, invite-only web application** for one elder care space per account, with strict role-based access, auditable actions, and email-only notifications.  

**Macro architecture choice**
- Use a **modular monolith** rather than microservices.
- Host in **one launch geography** only, with data residency aligned to that region.
- Treat the product as a **care coordination app handling sensitive personal data**, not a clinical record system.
- Keep documents and task metadata separate from any clinical interpretation or AI layer.

**Structural technical decisions that shape the MVP**
1. **Single care-space data model**
   - One elder per care space.
   - One primary coordinator role.
   - A small number of invited participants with coarse roles: coordinator, family member, caregiver.
   - This avoids multi-tenant permission complexity and reduces trust risk.

2. **Invite-based access only**
   - No self-signup into care spaces.
   - Access is granted only after invite acceptance and visible consent.
   - All access changes are recorded in an audit log.

3. **Minimal sensitive-data posture**
   - Store only coordination metadata plus optional uploaded documents.
   - No prescriptions, no clinical decision support, no messaging threads, no EHR sync.
   - This keeps the compliance baseline manageable for a pilot.

**Recommended implementation approach**
- Build a **mobile-friendly web app** with:
  - authentication
  - care-space membership
  - tasks/reminders
  - appointments
  - document upload/view
  - activity feed
  - audit log
  - admin support console
- Use a managed cloud stack in one region:
  - relational database for core entities and audit records
  - object storage for documents
  - background job runner for reminders
  - email service for notifications
- Encrypt data at rest and in transit.
- Use signed, expiring links for document access.
- Use server-side authorization on every read/write path.

**What must be built now**
- Care space creation for one elder
- Invitation and acceptance flow
- Role-based permissions
- Task CRUD, assignment, completion, due dates
- Appointment entries and reminders
- Document upload and controlled viewing
- Activity feed / audit trail
- Access revocation
- Email notification delivery
- Admin tools for export, deletion, revocation, and audit review
- Privacy notice + consent capture before access is activated
- Basic support workflow for manual intervention

**What can be handled manually or operationally first**
- Concierge onboarding of the first pilot families
- Manual setup help for roles, reminders, and document organization
- Human support for failed invites or notification issues
- Manual review of edge cases during the pilot
- Manual compliance review and data handling checks for the first geography
- Manual export/deletion processing only if the admin console is not fully complete at pilot start

**Main modules or components**
- Identity and access management
- Care space and membership management
- Tasks and reminders service
- Appointment tracking
- Document storage and access control
- Activity/audit logging
- Notification service via email
- Admin/support console
- Compliance configuration module for jurisdiction-specific baseline settings

**Critical data or workflow states**
- Care space status: draft, active, archived, deleted
- Invite status: pending, accepted, expired, revoked
- Membership status: active, suspended, revoked
- Task status: open, completed, overdue, cancelled
- Reminder status: scheduled, sent, failed, dismissed
- Document status: uploaded, accessible, revoked, deleted
- Consent status: pending, accepted, withdrawn
- Audit event state: immutable append-only record

**Minimum reliability, data, permission, or control requirements**
- Server-side authorization on every action
- Immutable audit log for membership, document, task, reminder, and access changes
- Revocation must take effect immediately for both UI and signed document access
- Email delivery failures must be visible to support
- Deletion and export must be operationally supported from day one
- Least-privilege roles only; no advanced hierarchies
- No cross-care-space access
- No default sharing of documents or personal data
- Backups and disaster recovery for the database and object storage
- Basic retention/deletion policy aligned to the selected geography

**Smallest compliance-safe operating model for MVP**
- Launch in **one explicitly chosen geography only**
- Classify CareSync as handling **sensitive personal / health-related information**
- Collect only the data necessary for coordination
- Require consent before participants access a care space
- Provide visible privacy notice at invite acceptance
- Keep a human-auditable record of who accessed what and when
- Support deletion, export, and revocation for all pilot accounts
- Do not process data outside the approved region unless the chosen jurisdiction explicitly permits it and the vendor stack is covered
- Do not store or infer clinical data beyond user-entered coordination metadata
- If the launch geography has stronger health-data requirements, treat the MVP as **pilot-only** until legal review confirms the minimum controls

**Diagram Blueprint**
- **Main system blocks**
  - Web app frontend
  - API/backend monolith
  - Relational database
  - Object storage for documents
  - Email notification service
  - Background job scheduler/worker
  - Admin/support console
- **Main flows between blocks**
  - User invite → backend → membership/consent record → email invite
  - Accepted invite → backend → role assignment → active membership
  - Task/appointment/reminder create/update → database → activity log → email notification
  - Document upload → object storage + metadata DB row → permission check → signed access link
  - Revocation/deletion/export request → admin console → backend → state change + audit event
- **External actors or systems**
  - Primary coordinator
  - Family members
  - Optional caregiver
  - Email delivery provider
  - Cloud storage provider
- **Admin or operations control points**
  - Invite recovery/resend
  - Access revocation
  - Audit review
  - Export/deletion execution
  - Failed notification monitoring

## Review Summary
The key feasibility issue is that CareSync handles sensitive care information without a fixed jurisdictional baseline, so the MVP must be constrained to one launch geography with a minimal, explicit privacy and data-handling model. The safest path is a modular monolith with invite-only access, coarse permissions, auditability, email notifications, and a small admin console, while keeping all richer collaboration features out of scope.

## Critical Assumptions
- One launch geography can be selected before implementation and kept fixed for the pilot.
- The selected geography allows a lightweight pilot model with consent, auditability, and deletion/export controls.
- Families will accept email-only notifications for the MVP.
- The product can function with coarse roles and no messaging subsystem.
- Manual concierge support is acceptable during the pilot to cover edge cases and compliance handling.

## Requested Changes
- Define the initial launch geography and document the minimum privacy/compliance baseline before build starts. [compliance]
- Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]

## Risks
- The chosen geography may impose compliance obligations that exceed the current MVP controls. [compliance]
- Document handling may create a disproportionate privacy burden relative to the rest of the product. [privacy_trust]
- Email-only notifications may be insufficient for some families, creating false negatives in the pilot. [scope]
- Revocation and deletion workflows may be mishandled operationally if the admin console is incomplete. [data_access]
- The product may drift toward general collaboration tooling if task/document scope is not tightly enforced. [scope]

## Open Questions
- Which single launch geography is approved for the pilot? [compliance]
- Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- What minimum retention policy is required for the selected geography? [compliance]
- Does the chosen jurisdiction require any specific consent wording or data-subject rights workflow beyond standard invite acceptance? [compliance]
- Should the admin/support workflow be fully self-serve at launch, or is human-operated deletion/export acceptable for the pilot? [data_access]

## Why This Could Fail Even With Good Execution
Even with solid delivery, the project can still fail if the selected geography’s health-data obligations or user trust expectations are heavier than the team’s minimal controls, making the product too constrained or operationally burdensome for a normal pilot. In that case, the MVP would need to shrink further, likely to coordination metadata only, before documents and broader sharing can be safely added.

## Technical Readiness
Status: LIMITED

Blocking Gaps:
- Launch geography and compliance baseline are still undefined [compliance]
- Document handling policy is not fully bounded for a compliance-safe MVP [scope]
- Admin export/deletion/revocation workflow is not yet specified as operationally complete [data_access]

Required Improvements:
- Select one launch geography and map the minimum privacy, consent, retention, and deletion requirements before implementation [compliance]
- Decide whether document storage is included in the first pilot or deferred until compliance is verified [scope]
- Specify whether admin actions can be human-operated for pilot accounts or must be fully self-serve at launch [data_access]