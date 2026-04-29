# SkillBridge — MVP Product Proposal

## Product Problem
Recent graduates and career switchers in Paris struggle to prove practical experience fast enough to access junior roles.

Small organizations need short, affordable help on real work but cannot justify full-time hires or agencies.

The MVP must prove a narrow exchange: bounded real missions that produce credible proof-of-work for candidates and useful output for organizations.

## Initial Wedge
A concierge-led, Paris-only pilot for one repeatable organization class: startups, with one mission family: short product/UX-support missions that can be completed in 2 to 8 weeks.

The wedge is not a general marketplace, internship replacement, or open-ended freelancing platform. It is a tightly moderated channel for structured, bounded work with a proof-of-work outcome.

## First Target User
Primary candidate user:
- Recent graduates and career switchers in Paris with little or no professional experience who need credible project proof now

Primary supply-side customer:
- Early-stage Paris startups already known to the founders that need a small, bounded piece of product or UX work and cannot justify an agency or junior hire

First use case:
- A candidate completes one structured startup mission, receives structured feedback, and gets a verified proof-of-work artifact they can use in applications

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Internships
- Unpaid volunteering
- Freelance marketplaces
- Job boards
- Informal networking and referrals
- Hackathons or student association projects

Why they are not enough:
- Internships are slower and broader than a short project
- Freelance marketplaces favor experienced workers and open-ended client work
- Job boards do not solve the experience gap
- Informal projects are hard to verify and standardize

Switching trigger:
- The candidate needs credible project proof quickly
- The startup needs a bounded piece of work with low overhead and some trust in delivery

## Core MVP Workflow
1. A startup submits a mission using a strict template with objective, taxonomy tag, scope, deliverable, duration, effort range, location mode, compensation status, and review method
2. The platform approves only missions that fit the launch taxonomy and quality rubric
3. Candidates browse the limited set of approved missions and apply with a short profile and motivation
4. The operator uses a manual matching queue to assign a candidate
5. The candidate completes the mission with basic messaging and deliverable submission
6. The startup confirms completion and submits structured feedback
7. The candidate receives a standardized proof-of-work artifact for their profile

## In Scope
- Candidate profiles with basic skills, education, availability, and location
- Startup organization profiles with identity and commitment fields
- Mission posting with a strict France-specific template
- Mandatory mission moderation state machine
- Fixed launch taxonomy limited to one mission family
- Startup qualification gate before publication
- Manual matching/admin queue
- Mission listing and browsing of approved missions only
- Simple application submission
- Basic messaging
- Deliverable upload or link submission
- Completion status
- Structured feedback capture
- Standardized proof-of-work artifact
- Structured rejection reasons for moderation
- Paris-only launch scope
- Completion feedback required before proof-of-work issuance
- Hard block on open-ended or unclassified missions

## Out of Scope
- Open-ended freelance marketplace
- Broad mission taxonomy at launch
- Complex algorithmic matching
- Reputation scoring or ratings marketplace mechanics
- Payment processing in MVP unless required for a specific mission
- Multi-country launch
- Full employment or internship administration
- Automatic contract generation for all legal cases
- Time tracking
- Escrow
- Deep analytics dashboards
- AI-generated mission creation or candidate ranking
- Community features
- Chat-heavy collaboration tools
- Self-serve public posting without approval
- Dispute resolution system beyond manual handling
- Public candidate portfolios with social features
- Multiple launch segments beyond startups
- Associations, NGOs, and local businesses in the initial wedge

## MVP Build Vs Pilot Operations
### Must Build Now
- Candidate profile creation
- Startup profile creation
- Startup identity and commitment fields
- Mission posting template
- Mandatory moderation state machine
- Fixed mission taxonomy
- Startup qualification gate
- Mission listing and browsing
- Application submission
- Manual matching/admin queue
- Basic messaging
- Deliverable submission
- Completion status
- Structured feedback capture
- Standardized proof-of-work artifact generation
- Structured rejection reasons
- Hard validation against open-ended or unclassified missions
- Completion feedback dependency before proof issuance

### Manual Or Operational During Pilot
- Mission sourcing from trusted startups
- Review of mission scope before publication
- Candidate screening for suitability
- Assignment decisions when supply is thin
- Human review of completed deliverables if needed
- Support for disputes or unclear scope
- Legal review of mission wording and disclaimers for France
- Founder-led outreach to seed both sides

### Deferred Until After Proof
- Algorithmic matching
- Reputation scoring
- Payments or escrow rails
- Rich analytics
- Multi-country compliance handling
- Full messaging suite
- Automated contract workflows
- Advanced fraud detection
- Public candidate portfolios with social features
- Additional organization types beyond startups
- Additional mission families beyond the initial product/UX-support wedge

## Business Model Hypothesis
Primary hypothesis:
- Charge startups a fee for posting or filling a mission, or a subscription for access to vetted candidates and structured missions

Secondary hypothesis:
- Keep candidate access free to reduce friction and maximize supply

Most plausible early model:
- Startup-side fee after proof of repeat demand
- For pilot validation, missions may need to be free or subsidized to reduce friction and focus on proving completion, usefulness, and trust

## Critical Assumptions
- Startups will submit real missions instead of using the platform for free labor
- Candidates will value short missions enough to join and complete them
- The mission moderation rubric can block vague, exploitative, or work-like postings
- Short missions can produce useful proof for entry-level hiring
- Paris has enough concentrated supply and demand for a narrow pilot
- Legal framing can be kept safe enough for France
- A manual trust model is sufficient for the pilot
- A standardized proof-of-work artifact will be credible enough for candidates and employers
- One startup mission family is enough to prove the exchange

## How To Test Quickly
- Recruit 10 to 15 Paris startups through direct outreach and existing networks
- Ask each startup to submit one real mission using the strict template
- Review each mission against the moderation rubric and fixed taxonomy
- Recruit 20 to 30 candidates from universities, bootcamps, and career-switcher communities
- Run manual matching and completion tracking
- Measure mission acceptance, completion, and perceived credibility of the proof artifact
- Interview both sides after completion to identify trust and scope issues
- Validate mission wording and rejection criteria with French legal review before wider pilot use
- Check whether at least one startup mission family produces repeatable, bounded work

## Acceptance Criteria
- At least 5 vetted missions are approved and published in Paris during the pilot
- At least 10 candidates apply to available missions
- At least 3 missions are matched and completed
- At least 2 startups say the output was useful enough to repeat
- At least 2 candidates say the proof-of-work artifact improves their job applications
- No material trust or legal issues emerge from the pilot format
- Missions remain structured and do not drift into generic freelance work
- Moderation decisions are consistent enough that vague or labor-like missions are rejected reliably
- The proof-of-work artifact is understood by pilot users as evidence of practical experience

## Risks And Failure Modes
- Startups post vague or exploitative missions
- Candidates experience the platform as unpaid labor with weak career value
- Supply and demand fail to match early
- The product drifts into a low-quality freelance marketplace
- Trust breaks if deliverables are not useful or feedback is inconsistent
- Legal boundaries around unpaid or work-like arrangements create risk in France
- Manual moderation becomes too heavy to scale
- The proof-of-work artifact is not credible enough to matter to hiring managers
- The single mission family does not create enough repeat demand

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Legal framing for short missions in France is not yet validated [legal_risk]
- Trust model for preventing free-labor abuse is not yet proven [trust_model]
- Demand-supply balance in Paris is unproven [market_liquidity]

Required Improvements:
- Validate mission wording and disclaimer language with French legal review [legal_review]
- Run a concierge pilot to test whether startups and candidates complete the workflow [pilot_validation]
- Tighten the mission moderation rubric so vague or labor-like postings are rejected consistently [quality_gate]
- Confirm a credible proof-of-work artifact format with pilot users [proof_credibility]

## Recommendation
Proceed with a concierge-style pilot in Paris, not a full self-serve build.

The narrowest credible MVP is a vetted starter-mission marketplace for Paris startups only, focused on one mission family, with manual matching, hard moderation gating, and proof-of-work completion.

Build only what is required to prove:
- real startups will post credible missions
- early-career candidates will complete them
- the resulting artifact is valued as proof of experience
- the legal and trust model is safe enough for France

If the pilot cannot confirm legal safety, mission quality, repeat demand, and proof credibility, do not scale the product yet.