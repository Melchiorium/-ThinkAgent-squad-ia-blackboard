## Go-To-Market Notes
- **Main market bottleneck:** families already have a “good enough” coordination habit in WhatsApp/SMS plus calendars, so the real bottleneck is not awareness — it is **getting one coordinator to move enough real coordination activity into a new place to create habit and trust**.
- **Side of the market to secure first:** secure the **family coordinator** first, not elderly users or agencies. If the coordinator does not adopt it, the rest of the care circle will not follow.
- **Structural GTM decisions:**
  1. **Start as a founder-led concierge pilot, not self-serve.** This is a trust-heavy category and the first proof should come from assisted onboarding and guided setup.
  2. **Launch only for one elder, one coordinator, and 2–4 invited participants.** Do not begin with agencies, multi-family cases, or broad household coordination.
  3. **Use one primary use case: shared responsibility tracking with reminders.** Calendar, tasks, and status visibility are the wedge; document storage is secondary.
- **Initial target audience:** adult children who are already the de facto care coordinator for a parent, especially families where siblings live in different cities and coordination is currently happening across chat threads and spreadsheets.
- **Positioning:** “A trusted shared coordination workspace for one parent’s care, so the family always knows what is due, who is responsible, and what happened last.”
- **First acquisition motion:** **founder-led referrals through caregiving-adjacent communities and personal networks**, then direct outreach to coordinators who already signal coordination pain.
- **Operating assumptions for the first acquisition motion:**
  - each conversation can identify a real coordinator with an immediate pain point
  - the coordinator is willing to invite at least 2 others
  - the pilot can be set up manually in under 30 minutes
  - the family will tolerate guided onboarding if it reduces missed tasks
  - reminders and access controls work reliably enough to earn trust
- **Switching trigger:** a family has already experienced missed appointments, duplicated effort, or uncertainty over who handled what, and wants a shared record stronger than chat history.
- **First activation loop:** coordinator creates one care space → adds one upcoming appointment or recurring task → invites siblings/caregiver → assigns ownership → reminders go out → someone marks completion → the timeline becomes the family’s source of truth.
- **What must exist before public launch:**
  - one launch geography chosen
  - minimum privacy/compliance posture defined for that geography
  - reminders delivered reliably with visible failure states
  - role-based access enforced
  - audit/history visible
  - pilot support process for access recovery and reminder failures
  - a clear migration story from chat/spreadsheets into CareSync
- **Must be productized now vs manual during pilot:**
  - **Productize now:** care space creation, invitations, fixed roles, task/reminder flow, calendar basics, notes/timeline, audit history, access enforcement, deletion/archive, visible delivery status.
  - **Manual during pilot:** onboarding, migration of existing coordination items, explanation of roles, support for access issues, concierge help with setup, feedback collection.
  - **Defer:** agencies, in-app chat, EHR/pharmacy integrations, broad self-serve growth, advanced permissions, multilingual support, AI features.

## Review Summary
The launch challenge is not feature breadth but **proof of real behavior change**: CareSync must get one family coordinator to move meaningful coordination activity out of chat and into a trusted shared workspace. The recommended direction is a **concierge-led pilot for a single elder care circle**, focused on reminders, ownership, and visible status rather than a broad platform launch.

## Build Vs Pilot Operations

### Must Be Productized Now
- One care space per relative
- Invitations and fixed role-based access
- Server-enforced permissions
- Task assignment and due dates
- Reminder delivery with visible success/failure states
- Basic appointment tracking
- Shared notes/timeline
- Document upload for a limited set of care docs
- Change history / audit log
- Delete/archive behavior
- Minimum privacy/compliance controls for one geography

### Can Stay Manual Or Operational During Pilot
- Founder-led onboarding
- Migrating the first tasks and documents from chat/spreadsheets
- Explaining how to use roles and permissions
- Support for invitation/access problems
- Monitoring reminder failures
- Collecting pilot feedback on switching behavior
- Handling trust concerns in live conversations

### Deferred Until After Proof
- Agency workflows
- In-app messaging
- EHR/pharmacy integrations
- Advanced permissions matrix
- Multi-language support
- Mobile-first elderly-user optimization
- Billing, subscriptions, and payments
- AI summaries or recommendations
- Broad self-serve acquisition

## Critical Assumptions
- A coordinator can be identified who feels enough pain to change tools
- That coordinator can invite at least 2 other participants
- Families will move at least some real coordination items out of chat
- Reminder delivery and access control are reliable enough to earn trust
- One geography is enough for a compliant pilot without broad legal complexity

## Requested Changes
- Define **one primary acquisition motion** explicitly: founder-led concierge outreach/referrals to coordinator-led family pilots. [market_motion]
- Specify the **smallest credible launch audience**: adult children coordinating one parent, with 2–4 participants and one active care relationship. [market_motion]
- Add a concrete **validation experiment**: measure how many real tasks, reminders, and updates migrate from chat/spreadsheets into CareSync over 2+ weeks. [demand_validation]
- Clarify the **reminder channel and failure handling** for pilot use, including what happens when delivery fails. [trust_controls]
- Fix the **launch geography and minimum privacy/compliance posture** before any broader pilot. [privacy_trust]

## Risks
- Families keep using WhatsApp and never shift enough behavior.
- The product becomes a passive document repository instead of a coordination tool.
- Trust concerns around sensitive information block invitations.
- Reminder reliability is not strong enough for users to depend on it.
- Caregivers or siblings do not consistently update the system.
- The support burden is too high without manual founder involvement.

## Open Questions
- Which exact launch geography will be used for the pilot?
- Which reminder channels are in scope first: SMS, email, push, or a combination?
- What is the minimum migration threshold that counts as real adoption?
- Who is the economic buyer in the first pilot: coordinator alone or the family group?
- What is the intended pilot length before deciding whether to expand?

## Why This Could Fail Even With Good Execution
Even if the team executes well, the product can still fail if families do not experience enough immediate relief to overcome their existing chat-based habits. In that case, CareSync becomes “another place to update” rather than the trusted source of truth, and adoption stalls before repeat use forms.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- No single primary acquisition motion is defined yet [market_motion]
- The smallest credible launch audience is not yet narrowed enough for a focused pilot [market_motion]
- Switching behavior from chat/spreadsheets to CareSync is unproven and needs a measurable experiment [demand_validation]
- Reminder channel and failure handling are not specified tightly enough for trust-critical pilot use [trust_controls]
- Launch geography and minimum compliance posture remain undefined [privacy_trust]

Required Improvements:
- Choose one founder-led acquisition motion and a clear launch threshold for the pilot [market_motion]
- Narrow the audience to one elder, one coordinator, and a small invited care circle [market_motion]
- Run a 2+ week concierge pilot measuring actual migration of coordination items [demand_validation]
- Define reminder channels, retries, and visible failure states before pilot launch [trust_controls]
- Lock one geography and minimum privacy/compliance requirements before inviting families [privacy_trust]