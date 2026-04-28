# CareSync MVP Product Proposal

## Product Problem
Families coordinating elder care use fragmented tools: chat threads, phone calls, paper notes, shared calendars, and scattered documents. That creates missed appointments, duplicated effort, unclear ownership, and stress.

The core problem is not general elder-care management. It is:

**How can one family maintain a trusted shared source of truth for one older relative’s care coordination without forcing everyone to learn a complex system?**

## Initial Wedge
A **single shared care coordination workspace for one elderly relative and their close care circle**.

This wedge is intentionally narrow:
- one care recipient
- one primary coordinator
- 2–4 family participants
- optionally one professional caregiver
- appointments, responsibilities, reminders, notes, and a small set of key documents in one place

The MVP must prove that families will move meaningful coordination activity out of chat and into a dedicated workspace when it clearly reduces misses and ambiguity.

## First Target User
**Primary user:** an adult child who is the de facto coordinator for an elderly parent.

Why this user:
- already manages appointments, reminders, and family updates
- feels the coordination pain most acutely
- can invite others into the workflow
- is the most likely first buyer

Secondary participants:
- siblings in other cities
- one caregiver or home nurse

## Existing Alternatives And Switching Trigger
Current alternatives:
- WhatsApp / SMS group chats
- shared calendars
- handwritten notes or spreadsheets
- paper medication lists
- hospital portals and scattered PDFs
- agency caregiver logs

Why these are used:
- zero learning curve
- familiar
- immediate messaging

Switching trigger:
- coordination is breaking down because information is fragmented across channels
- multiple people need the same current information
- missed appointments, duplicated tasks, or uncertainty about responsibility
- the family wants a more reliable record than chat threads

CareSync must win on:
- clear ownership
- reliable reminders
- shared visibility
- reduced back-and-forth
- trust and access control for sensitive information

## Core MVP Workflow
1. Primary user creates a care space for one relative.
2. Invites family members and optionally one caregiver.
3. Accepts required consent and privacy terms for the launch geography.
4. Sets fixed roles and permissions.
5. Adds appointments, recurring tasks, medication reminders, and important notes.
6. Assigns responsibility to a person for each item.
7. Participants receive reminders and can mark items complete.
8. Participants can view a shared timeline of updates and permitted documents.
9. The coordinator checks what is due, what is complete, and who is responsible without relying on a separate chat thread.

## In Scope
- One care space per elderly relative
- Founder-led onboarding for pilot users
- Invitations and fixed role-based access
- Coordinator, family member, caregiver roles only
- Server-enforced access rules for each role
- Explicit consent and policy acceptance for the launch geography
- Shared task list with assignment and due dates
- Basic calendar view for appointments
- Medication reminder entries
- Shared notes / timeline feed
- Document upload for a limited set of care documents
- Notifications / reminders for assigned items
- Visible reminder failure states
- Basic audit history of updates and completion
- Delete / archive behavior for care spaces and uploaded documents
- Minimum privacy, retention, and deletion controls for one initial launch geography
- Restricted internal support/admin tooling with audited staff actions

## Out of Scope
- Full telehealth or clinical decision support
- Emergency response workflows
- Direct integration with hospitals, pharmacies, or EHR systems
- Advanced AI care planning
- Broad home healthcare marketplace
- Insurance, billing, or payments
- Complex multi-patient agency operations
- Elderly-user-first UX optimization
- In-app chat as a replacement for messaging apps
- Multi-language support in MVP
- Advanced permissions beyond the fixed role model
- Long-term archive management beyond MVP needs
- Full global compliance coverage for every country
- Self-serve launch at broad scale
- Native caregiver agency workflows
- Premium tiers or expanded pricing mechanics

## MVP Build Vs Pilot Operations
### Must Build Now
- One care space per relative
- Invitations and role-based access
- Fixed coordinator / family member / caregiver roles
- Server-side access enforcement
- Explicit consent and policy acceptance
- Task assignment with reminders
- Basic appointment tracking
- Medication reminder entries
- Shared notes / timeline
- Document upload
- Change history / audit log
- Delete / archive care space and documents
- Reminder delivery with visible failure states
- Restricted internal support/admin console
- Minimum privacy and compliance controls for one launch geography

### Manual Or Operational During Pilot
- Founder-led onboarding for first families
- Helping set up the first care space
- Defining what counts as a task vs note
- Supporting document organization
- Customer support for access issues
- Compliance review for pilot geography
- Monitoring reminder delivery failures
- Directly collecting feedback on switching behavior
- Tracking whether real coordination moves from chat/spreadsheets into CareSync

### Deferred Until After Proof
- Native caregiver agency workflows
- EHR / pharmacy integrations
- In-app messaging
- Advanced permissions matrix
- Multi-language support
- Mobile-first optimization for elderly users
- Billing, subscriptions, and payments
- AI summaries and recommendations
- Broad self-serve acquisition
- Expanded archive management

## Business Model Hypothesis
Best initial model: **subscription paid by the family coordinator**.

Hypothesis:
- families will pay a modest monthly fee for reduced stress and fewer missed coordination steps
- pricing can later expand to caregiver agencies or premium family plans

Initial pricing direction:
- simple family subscription
- no pricing complexity in the MVP

## Critical Assumptions
- Families will adopt a dedicated tool instead of staying in chat
- The coordinator has enough pain to onboard others
- Shared visibility and reminders are valuable enough to change behavior
- Caregivers will participate if the workflow is simple
- Privacy, permissions, consent, and deletion behavior are strong enough to earn trust
- The product can be used without elderly users needing strong digital skills
- One launch geography can support a compliant pilot with minimal scope
- Reminder delivery is reliable enough to be trusted for basic coordination
- Internal support tooling is enough to manage pilot access and recovery safely

## How To Test Quickly
- Run concierge pilots with 5–10 families coordinating one elder each
- Measure whether they move real coordination items from chat / spreadsheets into CareSync
- Track weekly repeat use over at least 2 weeks
- Track missed appointments, forgotten tasks, and time spent coordinating before vs after
- Test whether families consistently assign tasks and check the shared record
- Confirm invited participant acceptance rate
- Interview coordinators on whether they would be disappointed if the product were removed
- Validate willingness to pay after the pilot period
- Test reminder delivery, permissions, audit history, consent, deletion behavior, and staff recovery workflows with real families in the launch geography

## Acceptance Criteria
- A coordinator can create a care space in under 10 minutes
- At least 3 participants can be invited and given access successfully
- Fixed roles are understandable and enforced correctly
- Required consent and policy acceptance are completed before use
- A family can add and assign an appointment, task, and medication reminder
- Reminders are delivered reliably or fail visibly with fallback handling
- Participants can mark items complete and see update history
- Documents can be uploaded and viewed by permitted users
- The coordinator can understand current status without needing a separate chat thread
- Users can delete or archive a care space and documents according to the chosen geography rules
- Pilot users report the tool is clearer than their current coordination method
- The pilot shows repeated weekly use from the same family group
- Pilot usage demonstrates meaningful migration of coordination activity from chat/spreadsheets into CareSync

## Risks And Failure Modes
- Families keep using WhatsApp and ignore the platform
- The product becomes too broad and loses simplicity
- Privacy concerns prevent adoption
- Caregivers do not consistently update the system
- Elderly users are assumed to be primary users when they are not
- Compliance requirements vary too much by region
- Reminder delivery is not trusted enough for appointments or medication
- The product becomes a document vault instead of a coordination tool
- Reminder fatigue reduces usefulness
- Permission confusion undermines trust
- Support burden is too high without internal admin tooling
- Launch geography rules are under-specified and block safe pilot use

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Initial launch geography and its minimum privacy, retention, deletion, and consent rules are not yet fixed [privacy_trust]
- Real switching behavior from chat/spreadsheets to CareSync is not yet proven [demand_validation]
- Reminder delivery, role permissions, and audit history need real-world validation with families [trust_controls]

Required Improvements:
- Define one initial launch geography and attach the minimum privacy and deletion rules [privacy_trust]
- Validate coordination migration with concierge pilots using real families [demand_validation]
- Test reminder delivery, permissions, audit history, and visible failure handling with pilot users [trust_controls]

## Recommendation
Proceed with a narrow concierge-style MVP focused on one family coordinating one elderly relative.

Do not launch as a broad elder-care platform.  
Do not start with agencies, marketplace features, in-app chat, or deep integrations.

The best path is to prove one reliable coordination workflow:
- invite participants
- assign responsibilities
- share current status
- deliver reminders
- maintain trust through permissions, consent, audit history, deletion controls, and operational support

If families do not meaningfully replace part of their current chat / spreadsheet process, revise before building beyond the wedge.