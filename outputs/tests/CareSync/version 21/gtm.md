## Go-To-Market Notes
- **Main market bottleneck:** trust + adoption in a sensitive, multi-stakeholder workflow. The hardest part is not feature breadth; it is getting one coordinator to successfully pull siblings/caregivers into a new shared system and keep them active long enough to prove repeat use.
- **Side of the market to secure first:** the **family coordinator side** first, not caregivers or agencies. If the coordinator does not own the workflow, the rest of the network will not engage.
- **Structural GTM decisions:**
  1. **Single-sided initial launch:** sell to one adult child coordinating one elder, with optional invites to relatives/caregivers.
  2. **Concierge-first motion:** founder-led onboarding and setup for the first pilots; do not rely on self-serve acquisition yet.
  3. **One geography, one use case:** launch in a single compliance environment with only care coordination, not broader home healthcare.
- **Initial target audience:** adult children in their 40s–60s who are already coordinating an aging parent and actively managing siblings or a hired caregiver.
- **Positioning:** “A private coordination hub for one elder and the small circle already responsible for care.” Not an EHR, not a chat replacement, not a marketplace.
- **First acquisition motion:** founder-led outreach through caregiver support communities, aging-parent discussion groups, referrals from elder-care professionals, and direct outreach to adult children who already signal caregiving burden.
- **Operating assumptions for the first acquisition motion:**
  - The buyer already feels coordination pain weekly, not occasionally.
  - They can describe a missed-task or confusion incident in recent memory.
  - They are willing to try a private tool if setup is done for them.
  - They can invite at least one other participant within 48 hours.
- **Switching trigger:** repeated breakdown across text threads / calls / notes leading to missed appointments, duplicated work, or sibling conflict.
- **First activation loop:** coordinator creates one elder circle → imports 3–5 recurring tasks/appointments/reminders → invites 1–3 family/caregiver participants → receives first task completion/update → sees a visible reduction in confusion within the first week.
- **What must exist before public launch:** one geography selected, baseline compliance rules defined, invitation and role model validated in live use, and a paid or price-tested concierge pilot showing repeat engagement.
- **What must be productized now vs manual during pilot:**
  - **Productized now:** care circle setup, invite flow, task ownership, reminders, simple permissions, activity log, and basic admin recovery.
  - **Manual during pilot:** onboarding, initial data entry, participant coaching, support, and pilot measurement.
  - **Deferred:** documents, chat, multi-elder support, agency workflows, integrations, and advanced analytics.

## Review Summary
The main launch challenge is not feature completeness but whether a single family coordinator can get a trusted care circle to adopt and keep using the product. The right GTM direction is a concierge-led, single-elder pilot aimed at proving recurring coordination usage and willingness to pay before expanding scope.

## Build Vs Pilot Operations

### Must Be Productized Now
- Invite-only care circle
- Shared task ownership and completion
- Appointment entries and reminders
- Medication reminder schedules
- Minimal role-based permissions
- Activity log for changes and completions
- Basic notification delivery
- Admin recovery for invites and roles
- Launch geography / compliance gating

### Can Stay Manual Or Operational During Pilot
- White-glove onboarding
- Manual setup of initial tasks and reminders
- Founder-led participant coaching
- Support for role assignment and troubleshooting
- Pilot follow-up and success tracking
- Manual price collection / invoicing
- Compliance review for the selected geography

### Deferred Until After Proof
- Secure document storage
- Rich messaging / chat
- Multi-elder support
- Care agency dashboards
- EHR / pharmacy / calendar integrations
- Payments and billing automation
- Advanced analytics
- AI summaries
- Emergency escalation workflows

## Critical Assumptions
- One coordinator is willing to own setup and keep the circle active.
- Other family members/caregivers will tolerate a lightweight new workflow.
- The product creates visible value within the first coordination cycle.
- A paid pilot or price test can be run without heavy friction.
- The minimal permission model is trusted enough for sensitive care coordination.

## Requested Changes
- Add a **measurable demand threshold** for the pilot, such as: at least 3 of 5 invited participants active within 7 days, and at least 2 recurring coordination actions completed per week per circle. [demand_validation]
- Define a **price-test rule** for the coordinator, such as a paid pilot or committed deposit after the first week, to validate willingness to pay. [demand_validation]
- Clarify the **minimum permission states** needed in the MVP: coordinator, family member, caregiver, and what each can view/edit. [privacy_trust]
- Add a **pilot success definition** tied to repeated use, not just setup completion. [demand_validation]
- Narrow the launch scope to **one elder, one circle, one geography** as a hard product constraint. [scope]

## Risks
- The coordinator signs up but cannot persuade siblings/caregivers to participate.
- Families continue using WhatsApp/text and never shift behavior.
- Privacy concerns block sharing of sensitive notes.
- Reminder fatigue reduces engagement instead of improving it.
- The product looks useful in setup but fails to show repeated weekly use.
- The paid family model may be too weak to sustain conversion.

## Open Questions
- What exact activation threshold will count as real demand in the pilot?
- What price point will the coordinator accept after trying the workflow?
- Which permission boundaries are required for trust versus convenience?
- Which single geography can be launched with the least compliance friction?
- What is the minimum recurring usage pattern that proves the product is replacing coordination chaos?

## Why This Could Fail Even With Good Execution
Even with strong execution, this can fail if the market does not feel enough pain to replace familiar group chats and informal coordination habits. If families only need occasional help, they may appreciate the product but never adopt it as the default system, which means usage and willingness to pay will stall.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- No measurable threshold defines when pilot demand is real enough to proceed [demand_validation]
- Willingness to pay is still unproven for the primary coordinator [demand_validation]
- The minimum trust/permission model is not yet validated in live family usage [privacy_trust]

Required Improvements:
- Set a concrete pilot success bar for active participants, repeated actions, and retention [demand_validation]
- Run a paid or price-tested concierge pilot with the coordinator as buyer [demand_validation]
- Validate the smallest trusted role/permission model in real usage [privacy_trust]