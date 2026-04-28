# Blackboard

## Project Brief

Project Name: CareSync

Pitch:
A digital platform that helps families coordinate care for elderly relatives by centralizing medical appointments, medication reminders, caregiving tasks, and communication between family members and professional caregivers.

Context:
Many families struggle to manage care for aging parents or relatives, especially when multiple siblings or caregivers are involved. Information is often fragmented across phone calls, messaging apps, handwritten notes, and hospital documents.

At the same time, professional caregivers and home assistance providers often lack visibility into family decisions and day-to-day coordination.

The platform aims to simplify elderly care coordination while reducing stress for families.

Target Users:
- Adults managing care for elderly parents
- Family members living in different cities
- Professional caregivers
- Home nurses
- Elderly care agencies

Potential Use Cases:
- Scheduling medical appointments
- Medication reminders
- Shared task management
- Emergency contact coordination
- Sharing medical documents
- Tracking caregiving responsibilities

Platform Capabilities:
- Shared family dashboard
- Calendar coordination
- Notifications/reminders
- Secure document storage
- Messaging system
- Permission management for family members and caregivers

Constraints:
- High trust and privacy expectations
- Sensitive medical-related information
- Elderly users may have low digital literacy
- Potential legal/data compliance issues depending on country

Challenges:
- Convincing families to adopt a new platform
- Balancing simplicity with complex coordination needs
- Building trust around sensitive personal information
- Identifying a sustainable business model

Long-term Vision:
Become the operating system for family caregiving coordination and eventually expand into broader home healthcare services.

## Project Brief Source

projects/project-CareSync.md

## Workflow Stage

first_pass_locked

## Source Version

_Aucun contenu._

## CEO Evaluation

_Aucun contenu._

## Artifacts

## Architecture Markdown Ready

True


## Architecture Visual Ready

True


## Architecture Visual Warning

Architecture visual is partial; missing sections: main_blocks, flows, controls


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### demand_validation
- [demand_validation] Switching behavior is not yet validated in real family coordination

### compliance
- [compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed

### data_access
- [data_access] Trust and access flows are not yet validated with real users

## Product Required Improvements

### demand_validation
- [demand_validation] Run concierge pilots to validate actual switching behavior and retention

### compliance
- [compliance] Define the initial launch geography and minimum compliance baseline before any public launch

### data_access
- [data_access] Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope

## Tech Status

LIMITED


## Tech Blocking Gaps

### compliance
- [compliance] Launch geography and compliance baseline are still undefined
- [compliance] Document handling policy is not fully bounded for a compliance-safe MVP

### data_access
- [data_access] Admin export/deletion/revocation workflow is not yet specified as operationally complete

## Tech Required Improvements

### compliance
- [compliance] Select one launch geography and map the minimum privacy, consent, retention, and deletion requirements before implementation

### market_motion
- [market_motion] Decide whether document storage is included in the first pilot or deferred until compliance is verified

### data_access
- [data_access] Specify whether admin actions can be human-operated for pilot accounts or must be fully self-serve at launch

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] The first launch audience and acquisition motion are still too broad for a credible pilot
- [market_motion] The pilot notification strategy is not fully locked to the lowest-support path

### demand_validation
- [demand_validation] The smallest proof of switching behavior is not defined as a measurable activation event

## Growth Required Improvements

### market_motion
- [market_motion] Commit to a founder-led concierge pilot focused on adult children coordinating one parent, sourced through warm referrals and caregiver-adjacent outreach
- [market_motion] Lock the pilot to email-first delivery and defer SMS until the pilot proves it is necessary

### demand_validation
- [demand_validation] Define a single activation threshold: one coordinator plus 2–4 invited participants completing a real task or appointment workflow in the shared space

## Global Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Switching behavior is not yet validated in real family coordination
- [demand_validation] The smallest proof of switching behavior is not defined as a measurable activation event

### compliance
- [compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed
- [compliance] Launch geography and compliance baseline are still undefined
- [compliance] Document handling policy is not fully bounded for a compliance-safe MVP

### data_access
- [data_access] Trust and access flows are not yet validated with real users
- [data_access] Admin export/deletion/revocation workflow is not yet specified as operationally complete

### market_motion
- [market_motion] The first launch audience and acquisition motion are still too broad for a credible pilot
- [market_motion] The pilot notification strategy is not fully locked to the lowest-support path

## Global Required Improvements

### demand_validation
- [demand_validation] Run concierge pilots to validate actual switching behavior and retention
- [demand_validation] Define a single activation threshold: one coordinator plus 2–4 invited participants completing a real task or appointment workflow in the shared space

### compliance
- [compliance] Define the initial launch geography and minimum compliance baseline before any public launch
- [compliance] Select one launch geography and map the minimum privacy, consent, retention, and deletion requirements before implementation

### data_access
- [data_access] Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope
- [data_access] Specify whether admin actions can be human-operated for pilot accounts or must be fully self-serve at launch

### market_motion
- [market_motion] Decide whether document storage is included in the first pilot or deferred until compliance is verified
- [market_motion] Commit to a founder-led concierge pilot focused on adult children coordinating one parent, sourced through warm referrals and caregiver-adjacent outreach
- [market_motion] Lock the pilot to email-first delivery and defer SMS until the pilot proves it is necessary

## Known Tags

- data_access
- demand_validation
- market_motion
- compliance
- scope
- privacy_trust


## Correction Loop

## Triggered

Yes


## Current Loop Count

2


## Max Loops

2


## Initial Global Status

LIMITED


## Final Outcome

LIMITED


## Correction Tasks

### Loop 1

#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Reminder delivery channel choice is unresolved, which affects reliability design and operational support. Decide whether email-only or email-plus-SMS is required for the pilot. Choose a single launch market and define the minimum privacy/compliance requirements before broader release


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] Add a mandatory audit log and support console requirement to the MVP scope.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech


#### Tech Task

## Task

Clarify the smallest compliance-safe operating model needed for MVP.


## Source Gap

[compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed Define the initial launch geography and minimum compliance baseline before any public launch Launch geography and compliance baseline are not yet defined


## Expected Output

A concrete compliance-safe operating baseline for MVP.


## Contributors

- growth


### Loop 2

#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The first acquisition motion is still too broad without a narrow pilot-defined buyer and channel Notification-channel choice is unresolved for the pilot, which affects reliability and support burden Commit to a founder-led concierge pilot aimed at adult children coordinating one parent, sourced through caregiver-adjacent referrals and warm outreach Lock the pilot to email-first delivery and only revisit SMS after pilot data shows it is necessary


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The MVP data scope still needs a hard limit on what qualifies as permissible care information. Freeze the MVP data model to coordination metadata plus document storage only, with no clinical system ingestion.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech


#### Tech Task

## Task

Clarify the smallest compliance-safe operating model needed for MVP.


## Source Gap

[compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed Define the initial launch geography and minimum compliance baseline before any public launch First launch geography is not fixed, so the compliance model cannot be finalized. Select one launch geography and derive the minimum privacy/data-handling baseline from that jurisdiction before implementation. Launch geography and minimum compliance posture are still undefined Choose one launch geography and document the minimum privacy/compliance requirements before any public launch


## Expected Output

A concrete compliance-safe operating baseline for MVP.


## Contributors

- growth


## Readiness History

### Loop 1 before

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Switching behavior is not yet validated in real family coordination
- [demand_validation] No validated proof that families will switch from existing coordination habits

### compliance
- [compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed
- [compliance] Launch geography and compliance baseline are not yet defined

### data_access
- [data_access] The permission and audit model is not yet validated with real users
- [data_access] The minimum trusted permission model for family and caregiver access is not yet validated

### privacy_trust
- [privacy_trust] Launch-market privacy and handling requirements are not yet fixed, so the data model and controls cannot be finalized safely.
- [privacy_trust] The permission model is still too high-level; the exact roles and access rules must be locked before implementation.

### market_motion
- [market_motion] Reminder delivery channel choice is unresolved, which affects reliability design and operational support.

## Global Required Improvements

### demand_validation
- [demand_validation] Run concierge pilots to validate actual switching behavior and retention
- [demand_validation] Run concierge pilots with one family coordinator per elder and measure actual switching behavior

### compliance
- [compliance] Define the initial launch geography and minimum compliance baseline before any public launch

### data_access
- [data_access] Test the simple family-vs-caregiver permission model and auditability with real users before locking scope
- [data_access] Specify the exact MVP roles and access matrix for family members and caregivers.
- [data_access] Test a simple, explainable permission model with real families and caregivers before locking scope

### privacy_trust
- [privacy_trust] Choose the initial launch geography and define the minimum privacy/compliance baseline.

### market_motion
- [market_motion] Decide whether email-only or email-plus-SMS is required for the pilot.
- [market_motion] Choose a single launch market and define the minimum privacy/compliance requirements before broader release

### scope
- [scope] Add a mandatory audit log and support console requirement to the MVP scope.

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Reminder delivery channel choice is unresolved, which affects reliability design and operational support. Decide whether email-only or email-plus-SMS is required for the pilot. Choose a single launch market and define the minimum privacy/compliance requirements before broader release


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] Add a mandatory audit log and support console requirement to the MVP scope.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Tech

## Task

Clarify the smallest compliance-safe operating model needed for MVP.


## Source Gap

[compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed Define the initial launch geography and minimum compliance baseline before any public launch Launch geography and compliance baseline are not yet defined


## Expected Output

A concrete compliance-safe operating baseline for MVP.


### Loop 1 after

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Switching behavior is not yet validated in real family coordination

### compliance
- [compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed
- [compliance] First launch geography is not fixed, so the compliance model cannot be finalized.
- [compliance] Launch geography and minimum compliance posture are still undefined

### data_access
- [data_access] Trust and access flows are not yet validated with real users
- [data_access] Admin/support access rules for documents and audit inspection are not yet explicitly defined.

### scope
- [scope] The MVP data scope still needs a hard limit on what qualifies as permissible care information.

### market_motion
- [market_motion] The first acquisition motion is still too broad without a narrow pilot-defined buyer and channel
- [market_motion] Notification-channel choice is unresolved for the pilot, which affects reliability and support burden

## Global Required Improvements

### demand_validation
- [demand_validation] Run concierge pilots to validate actual switching behavior and retention

### compliance
- [compliance] Define the initial launch geography and minimum compliance baseline before any public launch
- [compliance] Select one launch geography and derive the minimum privacy/data-handling baseline from that jurisdiction before implementation.
- [compliance] Choose one launch geography and document the minimum privacy/compliance requirements before any public launch

### data_access
- [data_access] Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope
- [data_access] Define support/admin permissions separately from customer permissions, including what operators can and cannot see.

### scope
- [scope] Freeze the MVP data model to coordination metadata plus document storage only, with no clinical system ingestion.

### market_motion
- [market_motion] Commit to a founder-led concierge pilot aimed at adult children coordinating one parent, sourced through caregiver-adjacent referrals and warm outreach
- [market_motion] Lock the pilot to email-first delivery and only revisit SMS after pilot data shows it is necessary

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Reminder delivery channel choice is unresolved, which affects reliability design and operational support. Decide whether email-only or email-plus-SMS is required for the pilot. Choose a single launch market and define the minimum privacy/compliance requirements before broader release


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] Add a mandatory audit log and support console requirement to the MVP scope.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Tech

## Task

Clarify the smallest compliance-safe operating model needed for MVP.


## Source Gap

[compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed Define the initial launch geography and minimum compliance baseline before any public launch Launch geography and compliance baseline are not yet defined


## Expected Output

A concrete compliance-safe operating baseline for MVP.


### Loop 2 before

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Switching behavior is not yet validated in real family coordination

### compliance
- [compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed
- [compliance] First launch geography is not fixed, so the compliance model cannot be finalized.
- [compliance] Launch geography and minimum compliance posture are still undefined

### data_access
- [data_access] Trust and access flows are not yet validated with real users
- [data_access] Admin/support access rules for documents and audit inspection are not yet explicitly defined.

### scope
- [scope] The MVP data scope still needs a hard limit on what qualifies as permissible care information.

### market_motion
- [market_motion] The first acquisition motion is still too broad without a narrow pilot-defined buyer and channel
- [market_motion] Notification-channel choice is unresolved for the pilot, which affects reliability and support burden

## Global Required Improvements

### demand_validation
- [demand_validation] Run concierge pilots to validate actual switching behavior and retention

### compliance
- [compliance] Define the initial launch geography and minimum compliance baseline before any public launch
- [compliance] Select one launch geography and derive the minimum privacy/data-handling baseline from that jurisdiction before implementation.
- [compliance] Choose one launch geography and document the minimum privacy/compliance requirements before any public launch

### data_access
- [data_access] Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope
- [data_access] Define support/admin permissions separately from customer permissions, including what operators can and cannot see.

### scope
- [scope] Freeze the MVP data model to coordination metadata plus document storage only, with no clinical system ingestion.

### market_motion
- [market_motion] Commit to a founder-led concierge pilot aimed at adult children coordinating one parent, sourced through caregiver-adjacent referrals and warm outreach
- [market_motion] Lock the pilot to email-first delivery and only revisit SMS after pilot data shows it is necessary

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The first acquisition motion is still too broad without a narrow pilot-defined buyer and channel Notification-channel choice is unresolved for the pilot, which affects reliability and support burden Commit to a founder-led concierge pilot aimed at adult children coordinating one parent, sourced through caregiver-adjacent referrals and warm outreach Lock the pilot to email-first delivery and only revisit SMS after pilot data shows it is necessary


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The MVP data scope still needs a hard limit on what qualifies as permissible care information. Freeze the MVP data model to coordination metadata plus document storage only, with no clinical system ingestion.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Tech

## Task

Clarify the smallest compliance-safe operating model needed for MVP.


## Source Gap

[compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed Define the initial launch geography and minimum compliance baseline before any public launch First launch geography is not fixed, so the compliance model cannot be finalized. Select one launch geography and derive the minimum privacy/data-handling baseline from that jurisdiction before implementation. Launch geography and minimum compliance posture are still undefined Choose one launch geography and document the minimum privacy/compliance requirements before any public launch


## Expected Output

A concrete compliance-safe operating baseline for MVP.


### Loop 2 after

## Global Status

LIMITED


## Product Status

LIMITED


## Tech Status

LIMITED


## Growth Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Switching behavior is not yet validated in real family coordination
- [demand_validation] The smallest proof of switching behavior is not defined as a measurable activation event

### compliance
- [compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed
- [compliance] Launch geography and compliance baseline are still undefined
- [compliance] Document handling policy is not fully bounded for a compliance-safe MVP

### data_access
- [data_access] Trust and access flows are not yet validated with real users
- [data_access] Admin export/deletion/revocation workflow is not yet specified as operationally complete

### market_motion
- [market_motion] The first launch audience and acquisition motion are still too broad for a credible pilot
- [market_motion] The pilot notification strategy is not fully locked to the lowest-support path

## Global Required Improvements

### demand_validation
- [demand_validation] Run concierge pilots to validate actual switching behavior and retention
- [demand_validation] Define a single activation threshold: one coordinator plus 2–4 invited participants completing a real task or appointment workflow in the shared space

### compliance
- [compliance] Define the initial launch geography and minimum compliance baseline before any public launch
- [compliance] Select one launch geography and map the minimum privacy, consent, retention, and deletion requirements before implementation

### data_access
- [data_access] Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope
- [data_access] Specify whether admin actions can be human-operated for pilot accounts or must be fully self-serve at launch

### market_motion
- [market_motion] Decide whether document storage is included in the first pilot or deferred until compliance is verified
- [market_motion] Commit to a founder-led concierge pilot focused on adult children coordinating one parent, sourced through warm referrals and caregiver-adjacent outreach
- [market_motion] Lock the pilot to email-first delivery and defer SMS until the pilot proves it is necessary

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] The first acquisition motion is still too broad without a narrow pilot-defined buyer and channel Notification-channel choice is unresolved for the pilot, which affects reliability and support burden Commit to a founder-led concierge pilot aimed at adult children coordinating one parent, sourced through caregiver-adjacent referrals and warm outreach Lock the pilot to email-first delivery and only revisit SMS after pilot data shows it is necessary


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The MVP data scope still needs a hard limit on what qualifies as permissible care information. Freeze the MVP data model to coordination metadata plus document storage only, with no clinical system ingestion.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Tech

## Task

Clarify the smallest compliance-safe operating model needed for MVP.


## Source Gap

[compliance] Launch geography and minimum privacy/compliance baseline are not yet fixed Define the initial launch geography and minimum compliance baseline before any public launch First launch geography is not fixed, so the compliance model cannot be finalized. Select one launch geography and derive the minimum privacy/data-handling baseline from that jurisdiction before implementation. Launch geography and minimum compliance posture are still undefined Choose one launch geography and document the minimum privacy/compliance requirements before any public launch


## Expected Output

A concrete compliance-safe operating baseline for MVP.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Define the initial launch geography and document the minimum privacy/compliance baseline before build starts. [compliance]
- [tech] Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]

## Growth Structural Decisions

### growth
- [growth] Clarify the launch motion as **founder-led concierge pilot** for adult children coordinating one parent. [market_motion]
- [growth] Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]

## Product Locking

## Applied

True


## Confirmed In Scope

- One elder, one primary coordinator, and a small invited circle
- Invite-based access with consent and visible privacy notice
- Shared tasks, reminders, appointments, and status feed
- Email notifications only
- Coarse permissions, audit log, and access revocation
- Optional document upload and viewing for coordination only
- One launch geography with defined compliance baseline


## Confirmed Deferred

- SMS notifications
- Rich messaging
- Native mobile apps
- Advanced permissions
- Multi-elder support
- EHR, calendar, and pharmacy integrations
- AI automation
- Elder self-service onboarding
- Country expansion
- Rich clinical data capture


## Confirmed Out Of Scope

- Clinical records ingestion
- Full medical record management
- Emergency response
- Billing, insurance, and claims
- Agency marketplace or matching
- Generic project-management expansion


## Locking Note

- Scope remains intentionally narrow to prove coordination value before adding adjacent workflows.


## Expert Contributions

### Tech Summary

The key feasibility issue is that CareSync handles sensitive care information without a fixed jurisdictional baseline, so the MVP must be constrained to one launch geography with a minimal, explicit privacy and data-handling model. The safest path is a modular monolith with invite-only access, coarse permissions, auditability, email notifications, and a small admin console, while keeping all richer collaboration features out of scope.

## Tech Structural Decisions

- Define the initial launch geography and document the minimum privacy/compliance baseline before build starts. [compliance]
- Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]


## Tech Recommendations

- Define the initial launch geography and document the minimum privacy/compliance baseline before build starts. [compliance]
- Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]


## Tech Risks

- The chosen geography may impose compliance obligations that exceed the current MVP controls. [compliance]
- Document handling may create a disproportionate privacy burden relative to the rest of the product. [privacy_trust]
- Email-only notifications may be insufficient for some families, creating false negatives in the pilot. [scope]


## Tech Open Questions

- Which single launch geography is approved for the pilot? [compliance]
- Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- What minimum retention policy is required for the selected geography? [compliance]


### Growth Summary

The launch challenge is not building a bigger care platform; it is proving that one overwhelmed family coordinator will actually switch a real care workflow out of chat and into a dedicated shared space. The right direction is a founder-led, concierge pilot aimed at adult children coordinating one parent, with email-only delivery and a very narrow activation loop.

## Growth Structural Decisions

- Clarify the launch motion as **founder-led concierge pilot** for adult children coordinating one parent. [market_motion]
- Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]


## Growth Recommendations

- Clarify the launch motion as **founder-led concierge pilot** for adult children coordinating one parent. [market_motion]
- Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]
- Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]
- Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]


## Growth Risks

- Families may agree in principle but still keep using group chats for real coordination. [demand_validation]
- Trust concerns may block invite acceptance, document sharing, or permissions use. [privacy_trust]
- Email-only notifications may be insufficient for some families, reducing engagement. [market_motion]


## Growth Open Questions

- Which exact launch geography will be used for the pilot? [compliance]
- What minimum compliance posture is required for that geography? [compliance]
- Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]


## Product Arbitration

## Source

heuristic_fallback


## Retained

- Growth: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]


## Deferred

- Growth: Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]


## Rejected

- Tech: Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Tech: Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Tech: Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Growth: Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Growth: Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]


## Open Points

- Tech: Define the initial launch geography and document the minimum privacy/compliance baseline before build starts. [compliance]
- Tech: Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]
- Growth: Clarify the launch motion as **founder-led concierge pilot** for adult children coordinating one parent. [market_motion]
- Tech: Which single launch geography is approved for the pilot? [compliance]
- Tech: Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- Tech: What minimum retention policy is required for the selected geography? [compliance]
- Growth: Which exact launch geography will be used for the pilot? [compliance]
- Growth: What minimum compliance posture is required for that geography? [compliance]
- Growth: Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]
- Tech recommendation needing arbitration: Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Tech recommendation needing arbitration: Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Tech recommendation needing arbitration: Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Tech recommendation needing arbitration: Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]
- Growth recommendation needing arbitration: Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]
- Growth recommendation needing arbitration: Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Growth recommendation needing arbitration: Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]
- Growth recommendation needing arbitration: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]
- Tech open question: Which single launch geography is approved for the pilot? [compliance]
- Tech open question: Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- Tech open question: What minimum retention policy is required for the selected geography? [compliance]
- Growth open question: Which exact launch geography will be used for the pilot? [compliance]
- Growth open question: What minimum compliance posture is required for that geography? [compliance]
- Growth open question: Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care are currently forced to stitch together appointments, reminders, documents, and responsibilities across texts, calls, paper notes, and ad hoc messaging apps. That creates missed tasks, duplicated effort, poor visibility, and stress—especially when care is shared across siblings and professional caregivers.

The core product problem is not “general elder care.” It is a narrow coordination failure: **who is responsible for what, by when, and what changed since the last update**.

## Initial Wedge
A **shared care coordination workspace for one elder, one family, and one professional caregiver** centered on:
- a shared task list
- appointment/date reminders
- simple status updates
- basic document sharing

The wedge is to replace fragmented coordination for a single care recipient with one trusted place for the minimum information needed to keep care on track.

## First Target User
**Primary user:** an adult child coordinating care for one aging parent who is still mostly living at home.

Why this user first:
- they feel the coordination pain most acutely
- they usually drive adoption for the rest of the family
- they can manage setup and permissions
- they are more digitally capable than the elder in many cases

## Existing Alternatives And Switching Trigger
### Existing Alternatives
- Family group chats and phone calls
- Shared notes, calendars, and spreadsheets
- Paper notebooks and printed instructions
- Generic task apps
- Caregiver agency tools with limited family visibility
- Hospital or insurer portals that do not coordinate day-to-day care

### Switching Trigger
Families switch when:
- multiple people are involved and accountability is failing
- medication or appointment follow-through is being missed
- the primary caregiver is overwhelmed
- one family member needs visibility without repeated calling/texting
- a professional caregiver needs a simple shared source of truth

The switch is not driven by feature richness; it is driven by **coordination failures becoming costly or stressful**.

## Core MVP Workflow
1. Primary user creates a care space for one elder.
2. Primary user invites 1–4 family members and optionally one professional caregiver.
3. Primary user adds:
   - recurring appointments
   - medication reminders
   - a short task list
   - one or more important documents
4. Participants receive reminders and can mark tasks complete or add a short update.
5. Everyone sees a simple shared status view of what is upcoming, what is done, and what still needs attention.

The MVP must prove that the platform reduces coordination friction better than messaging and spreadsheets.

## In Scope
- One care space per elder
- Invite-based access for family and one or more caregivers
- Shared task list with due dates and completion status
- Appointment entries and reminders
- Medication reminders as simple scheduled reminders, not clinical management
- Basic document upload/view for care-related files
- Simple activity/status feed
- Role-based access control at a basic level
- Mobile-friendly web experience
- Notification delivery by email and/or SMS

## Out of Scope
- Full medical records management
- Clinical decision support
- Prescriptions, refills, or pharmacy integration
- AI-generated care plans
- Emergency response functionality
- Billing, insurance, or claims workflows
- Agency marketplace or caregiver matching
- Broad home healthcare operating system vision
- Direct messaging as a core product pillar
- Multi-elder household management
- Localization for many countries
- Advanced compliance certifications before proof
- Elder-facing onboarding for low-literacy users as a primary path

## MVP Build Vs Pilot Operations
### Must Build Now
- Care space creation for one elder
- Invite-based access
- Shared task list
- Appointment/reminder scheduling
- Basic document upload/view
- Simple status/activity feed
- Basic permissions by role
- Notifications

### Manual Or Operational During Pilot
- Onboarding support for first families
- Assistance setting up roles, tasks, and reminders
- Human review of edge cases in permissions or document handling
- Customer support for reminder setup and troubleshooting
- Pilot feedback collection from family coordinators

### Deferred Until After Proof
- Native mobile apps
- Rich messaging features
- Advanced permission hierarchies
- Care agency workflows
- Integrations with EHRs, calendars, or pharmacies
- AI summarization or automation
- Multi-elder support
- Country-specific compliance expansion
- Elder self-service workflows

## Business Model Hypothesis
A subscription model is most plausible:
- **B2C:** monthly fee per care space for families coordinating one elder
- **B2B2C:** paid by care agencies or home-care providers to provide family visibility as part of their service

Initial hypothesis should favor **family-paid subscription** because it is simpler to validate and avoids waiting on enterprise sales cycles.

## Critical Assumptions
- Families are willing to move care coordination out of chat apps into a dedicated tool.
- A narrow shared workspace is enough to create habitual use.
- The primary user can onboard other participants with low friction.
- Reminders and shared task visibility provide enough value to justify paying.
- Basic trust and privacy controls are sufficient for early adoption.
- The product can be useful without deep clinical integrations.
- Professional caregivers will participate if the workflow is simple and low burden.

## How To Test Quickly
- Run 10–15 concierge-led pilots with families coordinating one elder.
- Compare current coordination methods vs. CareSync for missed tasks, time spent coordinating, and perceived stress.
- Prototype the core workflow with no-code or lightweight implementation.
- Test whether families reliably use:
  - shared tasks
  - reminders
  - document uploads
  - status updates
- Measure:
  - weekly active use by the family coordinator
  - number of tasks/reminders completed
  - retention after 2–4 weeks
  - willingness to pay after pilot

## Acceptance Criteria
- A primary user can create a care space in under 5 minutes.
- At least 3 other participants can be invited and access granted successfully.
- A task or reminder can be created, assigned, and completed reliably.
- Documents can be uploaded and viewed by permitted users.
- Participants can see a clear current status without asking the coordinator.
- Notifications are delivered consistently.
- The workflow is understandable without training beyond a short setup guide.
- Pilot users report reduced coordination friction compared with chat/spreadsheets.

## Risks And Failure Modes
- Families do not change behavior from existing group chats.
- Too many coordination needs exist for a simple product to solve.
- Trust concerns block document sharing and permissions use.
- Professional caregivers refuse to adopt another tool.
- Elder needs vary too widely, making the product feel generic.
- Reminder fatigue reduces engagement.
- Compliance and privacy requirements slow launch or expand scope.
- The product becomes a project-management tool instead of a care-specific workflow.

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No validated proof that families will switch from existing coordination habits [switching_trigger]
- Privacy, consent, and data-handling requirements are not yet scoped by launch market [compliance_scope]
- The minimum trusted permission model for family and caregiver access is not yet validated [trust_model]

Required Improvements:
- Run concierge pilots to validate real switching behavior and retention [pilot_validation]
- Define the initial launch geography and minimum compliance baseline before build [compliance_baseline]
- Test a simple permission model with real family and caregiver users before locking product scope [permission_validation]

## Recommendation
Proceed with a narrow concierge-led MVP focused on one elder, one family coordinator, and optional one caregiver. Build only the shared task, reminder, document, and status workflow needed to prove that CareSync reduces coordination friction better than messaging and spreadsheets.

Do not expand into broader elder care management, enterprise caregiver tooling, or clinical features until the product proves recurring use and willingness to pay.

## Retained Decisions

- Growth: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]

## Deferred Decisions

- Growth: Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]

## Rejected Recommendations

- Tech: Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Tech: Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Tech: Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Growth: Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Growth: Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]

## Unresolved Tensions

- Tech recommendation needing arbitration: Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Tech recommendation needing arbitration: Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Tech recommendation needing arbitration: Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Tech recommendation needing arbitration: Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]
- Growth recommendation needing arbitration: Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]
- Growth recommendation needing arbitration: Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Growth recommendation needing arbitration: Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]
- Growth recommendation needing arbitration: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]
- Tech open question: Which single launch geography is approved for the pilot? [compliance]
- Tech open question: Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- Tech open question: What minimum retention policy is required for the selected geography? [compliance]
- Growth open question: Which exact launch geography will be used for the pilot? [compliance]
- Growth open question: What minimum compliance posture is required for that geography? [compliance]
- Growth open question: Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]

## Applied Changes

- Growth: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]

## Remaining Open Points

- Tech: Define the initial launch geography and document the minimum privacy/compliance baseline before build starts. [compliance]
- Tech: Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]
- Growth: Clarify the launch motion as **founder-led concierge pilot** for adult children coordinating one parent. [market_motion]
- Tech: Which single launch geography is approved for the pilot? [compliance]
- Tech: Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- Tech: What minimum retention policy is required for the selected geography? [compliance]
- Growth: Which exact launch geography will be used for the pilot? [compliance]
- Growth: What minimum compliance posture is required for that geography? [compliance]
- Growth: Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]
- Tech recommendation needing arbitration: Add an explicit data classification rule stating that CareSync stores only coordination metadata and optional uploaded documents, not clinical records. [privacy_trust]
- Tech recommendation needing arbitration: Add a mandatory invite-acceptance consent step with visible privacy notice before any participant gains access. [privacy_trust]
- Tech recommendation needing arbitration: Make deletion, export, revocation, and audit review part of the required MVP admin workflow, not just support nice-to-haves. [data_access]
- Tech recommendation needing arbitration: Clarify whether documents are allowed in MVP as optional pilot-only data, or whether the first release should be tasks/reminders only if compliance cannot be confirmed quickly. [scope]
- Growth recommendation needing arbitration: Explicitly define the first acquisition channel as **warm referrals and caregiver-adjacent outreach**, not broad self-serve acquisition. [market_motion]
- Growth recommendation needing arbitration: Lock the pilot to **email-first delivery only** and state that SMS is deferred until proof justifies it. [market_motion]
- Growth recommendation needing arbitration: Add a single-line definition of the **smallest activation event**: at least one coordinator plus 2–4 invited participants successfully using the shared space for a real upcoming task or appointment. [scope]
- Growth recommendation needing arbitration: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]
- Tech open question: Which single launch geography is approved for the pilot? [compliance]
- Tech open question: Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- Tech open question: What minimum retention policy is required for the selected geography? [compliance]
- Growth open question: Which exact launch geography will be used for the pilot? [compliance]
- Growth open question: What minimum compliance posture is required for that geography? [compliance]
- Growth open question: Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]

## Risks

- Families may still prefer existing group chat workflows, making the product underused despite working technically. [demand_validation]
- Permission mistakes or weak access revocation would destroy trust quickly. [privacy_trust]
- Notification delivery failures or duplicates could create missed tasks and safety concerns. [notification_reliability]
- Families may continue using chat apps because they are already “good enough.” [demand_validation]
- Trust concerns around medical documents may slow or block adoption. [privacy_trust]
- Professional caregivers may refuse to maintain a second system. [market_motion]
- The chosen launch geography may impose stricter health-data obligations than the MVP team expects. [compliance]
- Families may refuse to upload documents unless access controls feel extremely trustworthy. [privacy_trust]
- A weak support process could lead to accidental access leakage or broken invites. [data_access]
- Families may keep using WhatsApp/texts because the switching cost is still too high. [demand_validation]
- Trust concerns may block document sharing and permissions use. [privacy_trust]
- Email-only reminders may underperform for some users, reducing the perceived value of the product. [scope]
- The chosen geography may impose compliance obligations that exceed the current MVP controls. [compliance]
- Document handling may create a disproportionate privacy burden relative to the rest of the product. [privacy_trust]
- Email-only notifications may be insufficient for some families, creating false negatives in the pilot. [scope]
- Families may agree in principle but still keep using group chats for real coordination. [demand_validation]
- Trust concerns may block invite acceptance, document sharing, or permissions use. [privacy_trust]
- Email-only notifications may be insufficient for some families, reducing engagement. [market_motion]

## Open Questions

- Which country or launch market is first, so the minimum privacy and data handling rules can be set?
- Is SMS required for the pilot, or is email sufficient for all reminders and invites?
- Should professional caregivers have read-only access by default, or can they edit tasks and updates?
- What is the single launch country or state, and what privacy/compliance threshold must be met there? [compliance]
- Is the first pilot user paying, or is the pilot free with a later conversion test? [market_motion]
- What exact care scenario is the narrowest first audience: parent at home, post-discharge recovery, or recurring chronic coordination? [scope]
- Which specific country or jurisdiction is the first launch geography? [compliance]
- Will CareSync store any diagnosis, medication name, or other health-content fields beyond user-entered coordination notes? [scope]
- Is the pilot intended to include professional caregivers under the same access rules as family members? [privacy_trust]
- Which single geography will be used for the first pilot and what exact compliance baseline is required there? [compliance]
- Is the first pilot strictly family-paid, or will pilots be free/concierge-only until proof is established? [market_motion]
- What minimum proof of switching is required: reduced missed tasks, fewer coordination messages, or willingness to pay? [demand_validation]
- Which single launch geography is approved for the pilot? [compliance]
- Are uploaded documents in scope for MVP, or should the first release exclude them until compliance is confirmed? [scope]
- What minimum retention policy is required for the selected geography? [compliance]
- Which exact launch geography will be used for the pilot? [compliance]
- What minimum compliance posture is required for that geography? [compliance]
- Which caregiver-adjacent referral sources are most likely to produce qualified pilot families first? [market_motion]

## Final Revised PRD

# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care lose track of who is doing what, when it is due, and what changed since the last update. The information is scattered across texts, calls, paper notes, and generic chat apps, which creates missed follow-through and repeated coordination effort.

The MVP should solve only the coordination loop: a shared source of truth for tasks, reminders, status updates, and optional document sharing for one elder.

## Initial Wedge
A single shared care space for **one elder and one family coordinator**, with optional access for a small number of family members and one professional caregiver if needed.

The wedge is intentionally narrow:
- shared tasks
- appointment and reminder tracking
- simple status view
- optional document storage for care coordination only

This wedge exists to prove that families will switch from chat/spreadsheets to a dedicated care space for recurring coordination.

## First Target User
**Primary user:** an adult child coordinating care for one aging parent who lives at home or mostly at home.

Why this user first:
- they feel the coordination pain most directly
- they are usually the person who can set up the system
- they are the most likely adoption driver for the rest of the family
- they can evaluate whether the product reduces coordination burden

## Existing Alternatives And Switching Trigger
### Existing Alternatives
- Family group chats and phone calls
- Shared notes, calendars, and spreadsheets
- Paper notebooks and printed instructions
- Generic task apps
- Basic caregiver agency tools
- Hospital and insurer portals that do not coordinate day-to-day care

### Switching Trigger
Families switch when:
- multiple people are involved and accountability is failing
- appointments or follow-through are being missed
- the primary coordinator is overwhelmed
- someone needs visibility without repeated calling or texting

The trigger is coordination breakdown, not feature richness.

## Core MVP Workflow
1. The primary user creates a care space for one elder.
2. The primary user invites a few participants.
3. The primary user adds:
   - upcoming appointments
   - recurring reminders
   - a short task list
   - optional care-related documents for coordination only
4. Participants receive email notifications and can view the shared status.
5. Participants can mark tasks complete or add a short update.
6. The coordinator can see what is upcoming, what is done, and what still needs attention.

This workflow must prove that CareSync reduces coordination friction better than messaging and spreadsheets.

## In Scope
- One care space per elder
- One primary coordinator plus a small number of family members
- Optional one caregiver participant
- Invite-based access
- Shared task list with due dates and completion status
- Appointment entries
- Recurring reminders
- Simple activity/status feed
- Email notifications only
- Mobile-friendly web experience
- Coarse role-based permissions
- Consent on invite acceptance
- Visible privacy notice for each participant
- Audit log for key actions
- Access revocation
- One launch geography with a defined minimum privacy/compliance baseline
- Data limited to coordination metadata plus optional uploaded documents; no clinical records ingestion

## Out of Scope
- Full medical records management
- Clinical decision support
- Prescriptions, refills, or pharmacy integrations
- AI-generated care plans or summaries
- Emergency response functionality
- Billing, insurance, or claims workflows
- Agency marketplace or caregiver matching
- Rich in-product messaging
- Multi-elder household management
- Native mobile apps
- Advanced permission hierarchies
- SMS notifications
- Multi-country localization
- Elder-first onboarding as the primary path
- Complex document workflows beyond simple file storage and viewing
- Rich health-content data models beyond basic coordination metadata
- Public launch before the launch geography and compliance baseline are defined
- Clinical system ingestion of any kind

## MVP Build Vs Pilot Operations
### Must Build Now
- Care space creation for one elder
- Invite-based access
- Shared task list
- Appointment and reminder scheduling
- Optional document upload and viewing
- Simple status/activity feed
- Coarse permissions by role
- Invite acceptance consent
- Visible privacy notice
- Audit log for membership, document, task, reminder, and access actions
- Access revocation
- Email notifications
- Minimal admin tooling for deletion, export, revocation, and audit review

### Manual Or Operational During Pilot
- Concierge onboarding for first families
- Help setting up roles, tasks, and reminders
- Human support for invite and notification issues
- Manual handling of edge cases during pilot
- Pilot feedback collection from family coordinators

### Deferred Until After Proof
- SMS notifications
- Native mobile apps
- Rich messaging features
- Advanced permission hierarchies
- Care agency workflows
- EHR, calendar, or pharmacy integrations
- AI automation
- Multi-elder support
- Country-specific expansion
- Elder self-service workflows
- Rich clinical data capture

## Business Model Hypothesis
A subscription model is the best initial hypothesis.

- **Primary hypothesis:** family-paid monthly subscription per care space
- **Why:** simplest to validate, closest to the user who feels the pain, and avoids enterprise sales complexity
- **Later possibility:** B2B2C licensing for agencies or home-care providers if the family workflow proves valuable

The MVP should not depend on agency procurement to succeed.

## Critical Assumptions
- Families will move at least part of coordination out of chat apps into a dedicated tool
- A narrow shared workspace is enough to create repeat use
- The primary coordinator can onboard others with low friction
- Email-only reminders are enough for the pilot
- Coarse permissions and auditability are sufficient to establish trust early
- The product can be useful without deep clinical integrations
- Professional caregivers will participate if the workflow is simple and low burden
- A defined launch geography and baseline compliance posture are enough for a safe pilot
- Optional document sharing is necessary for proof, but only if limited to coordination use

## How To Test Quickly
- Run 10–15 concierge-led pilots with families coordinating one elder
- Use one launch geography and one minimum compliance baseline
- Compare current coordination methods vs. CareSync on:
  - missed tasks
  - time spent coordinating
  - perceived stress
  - willingness to continue using the tool
- Test whether families actually use:
  - shared tasks
  - reminders
  - optional document upload/view
  - status updates
- Measure:
  - weekly active use by the coordinator
  - completion rate of assigned tasks/reminders
  - retention after 2–4 weeks
  - willingness to pay after pilot
- Validate whether invite acceptance and privacy notice flows reduce trust friction
- Define activation as at least one coordinator plus 2–4 invited participants using the shared space for a real upcoming task or appointment

## Acceptance Criteria
- A primary user can create a care space in under 5 minutes
- At least 3 other participants can be invited and granted access successfully
- A task or reminder can be created, assigned, and completed reliably
- Optional documents can be uploaded and viewed only by permitted users
- Participants can see a clear current status without asking the coordinator
- Email notifications are delivered consistently
- Key actions are recorded in an audit log
- Access can be revoked successfully
- Invite acceptance consent and privacy notice are visible before access is granted
- Admin can export, delete, or review audit data for a pilot account
- The workflow is understandable without training beyond a short setup guide
- Pilot users report reduced coordination friction compared with chat or spreadsheets
- No clinical records ingestion is required for successful use

## Risks And Failure Modes
- Families do not change behavior from existing group chats
- The product is still too broad for a simple workflow
- Trust concerns block document sharing and permission use
- Professional caregivers refuse to adopt another tool
- Email-only delivery is not enough for some families
- Compliance requirements vary by launch geography and delay release
- The product drifts into generic project management instead of care-specific coordination
- The MVP becomes too dependent on operational support instead of proving product value
- Optional document support creates compliance complexity without improving proof enough

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Switching behavior is not yet validated in real family coordination [demand_validation]
- Launch geography and minimum privacy/compliance baseline are not yet fixed [compliance]
- Trust and access flows are not yet validated with real users [privacy_trust]

Required Improvements:
- Run concierge pilots to validate actual switching behavior and retention [demand_validation]
- Define the initial launch geography and minimum compliance baseline before any public launch [compliance]
- Test invite acceptance, privacy notice, permissions, and revocation with real users before locking scope [privacy_trust]

## Recommendation
Proceed with a narrow concierge-led MVP focused on one elder, one family coordinator, a small set of family participants, and optional one caregiver.

Keep the product centered on shared tasks, reminders, status, optional coordination-only documents, coarse permissions, consent, and auditability. Use email-only notifications and one launch geography for the pilot. Defer richer messaging, SMS, clinical data, integrations, and multi-elder support until the product proves recurring use and willingness to pay.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Growth: Tighten the launch audience to **one elder, one coordinator, small invited circle** and avoid implying broader household or agency use in the first release. [scope]

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
- main: architecture_visual_warning
