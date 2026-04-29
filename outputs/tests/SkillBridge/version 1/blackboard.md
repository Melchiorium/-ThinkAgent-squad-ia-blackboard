# Blackboard

## Project Brief

Project Name: SkillBridge

Pitch:
A digital platform designed to help young graduates and career switchers gain practical experience through short-term real-world projects proposed by small companies, startups, and non-profits.

Context:
Many graduates struggle to get hired because they lack professional experience.
At the same time, small organizations often need help on short projects but cannot afford full-time hires or expensive agencies.

The platform aims to connect both sides by allowing organizations to publish short missions (2 to 8 weeks) that candidates can complete remotely or on-site.

Target Users:
- Recent graduates
- Career changers
- Small businesses
- Startups
- Associations / NGOs

Potential Use Cases:
- UX audit for a small startup
- Social media campaign for a local business
- Data cleanup project
- Website redesign
- Market research mission
- Administrative process optimization

Platform Capabilities:
- User profiles
- Project posting
- Matching system
- Messaging
- Deliverable submission
- Feedback and reputation system

Constraints:
- Limited initial budget
- Need to build trust between both sides
- Must avoid becoming a low-quality freelance marketplace
- Legal/employment boundaries may vary depending on country

Challenges:
- Attract enough companies early on
- Ensure project quality
- Prevent abuse from companies looking for free labor
- Create enough value for candidates to stay engaged

Long-term Vision:
Become an alternative path to traditional internships and junior hiring by helping people build credible experience faster.

## Project Brief Source

projects/project-Skill_Bridge.md

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

_Aucun contenu._


## Architecture Mermaid Ready

True


## Architecture Mermaid Source

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/SkillBridge/version 1/architecture-diagram.mmd


## Architecture Image Ready

True


## Architecture Image Path

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/SkillBridge/version 1/architecture-diagram.png


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### demand_validation
- [demand_validation] Legal framing for short missions in France is not yet validated
- [demand_validation] Demand-supply balance in Paris is unproven

### quality_assurance
- [quality_assurance] Trust model for preventing free-labor abuse is not yet proven

## Product Required Improvements

### demand_validation
- [demand_validation] Validate mission wording and disclaimer language with French legal review

### market_motion
- [market_motion] Run a concierge pilot to test whether startups and candidates complete the workflow
- [market_motion] Confirm a credible proof-of-work artifact format with pilot users

### quality_assurance
- [quality_assurance] Tighten the mission moderation rubric so vague or labor-like postings are rejected consistently

## Tech Status

LIMITED


## Tech Blocking Gaps

### quality_assurance
- [quality_assurance] Mission quality control is not yet formalized into an enforced workflow
- [quality_assurance] Proof-of-work issuance is not yet tied to structured completion feedback

### scope
- [scope] The launch taxonomy is not yet specified tightly enough to enforce scope

## Tech Required Improvements

### quality_assurance
- [quality_assurance] Implement a mandatory moderation state machine with publish gating and rejection reasons
- [quality_assurance] Require structured completion feedback before generating the proof artifact

### scope
- [scope] Define a small fixed mission taxonomy and enforce it at form validation time

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] The launch audience is still too broad and needs a single trusted entry segment
- [market_motion] The first market motion is not yet constrained to one mission type and one acquisition path

### demand_validation
- [demand_validation] The proof-of-work value has not been validated with hiring-side users

## Growth Required Improvements

### market_motion
- [market_motion] Define one narrow first audience: Paris-based trusted organizations already in founder reach

### scope
- [scope] Limit launch to one bounded mission category with explicit deliverables

### demand_validation
- [demand_validation] Validate proof-of-work usefulness with a small set of recruiters or hiring managers

## Global Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Legal framing for short missions in France is not yet validated
- [demand_validation] Demand-supply balance in Paris is unproven
- [demand_validation] The proof-of-work value has not been validated with hiring-side users

### quality_assurance
- [quality_assurance] Trust model for preventing free-labor abuse is not yet proven
- [quality_assurance] Mission quality control is not yet formalized into an enforced workflow
- [quality_assurance] Proof-of-work issuance is not yet tied to structured completion feedback

### scope
- [scope] The launch taxonomy is not yet specified tightly enough to enforce scope

### market_motion
- [market_motion] The launch audience is still too broad and needs a single trusted entry segment
- [market_motion] The first market motion is not yet constrained to one mission type and one acquisition path

## Global Required Improvements

### demand_validation
- [demand_validation] Validate mission wording and disclaimer language with French legal review
- [demand_validation] Validate proof-of-work usefulness with a small set of recruiters or hiring managers

### market_motion
- [market_motion] Run a concierge pilot to test whether startups and candidates complete the workflow
- [market_motion] Confirm a credible proof-of-work artifact format with pilot users
- [market_motion] Define one narrow first audience: Paris-based trusted organizations already in founder reach

### quality_assurance
- [quality_assurance] Tighten the mission moderation rubric so vague or labor-like postings are rejected consistently
- [quality_assurance] Implement a mandatory moderation state machine with publish gating and rejection reasons
- [quality_assurance] Require structured completion feedback before generating the proof artifact

### scope
- [scope] Define a small fixed mission taxonomy and enforce it at form validation time
- [scope] Limit launch to one bounded mission category with explicit deliverables

## Known Tags

- demand_validation
- market_motion
- scope
- quality_assurance
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

#### Tech Task

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Trust model for preventing free-labor abuse is not yet proven Tighten the mission approval rubric so vague or labor-like postings are rejected consistently Add a hard mission approval workflow with rejection reasons and publish gating. Define a narrow mission taxonomy and enforce it in the posting form. Implement a strict approval rubric for mission scope, duration, and deliverables


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

- growth


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow Manual matching and moderation are required but not yet specified as an operational control surface. Build an internal admin console for matching, moderation, and completion review. The pilot depends on proving enough organization-side mission supply in Paris Run a concierge pilot with a small set of organizations to test repeat mission posting and completion


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Legal framing for short missions in France is not yet validated Demand-supply balance in Paris is unproven Validate mission wording and disclaimer language with French legal review Legal-safe mission framing for France is not yet validated. Validate France-specific mission wording and disclaimers before launch. Validate the France-specific mission structure and disclaimers before public launch


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

- tech


### Loop 2

#### Tech Task

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Trust model for preventing free-labor abuse is not yet proven Tighten the mission approval rubric so vague or labor-like postings are rejected consistently Mission quality control is not yet formalized into a hard approval workflow. The launch taxonomy is not yet specified tightly enough to enforce scope. Proof-of-work issuance is not yet tied to structured completion feedback. Implement a mandatory mission moderation state machine with publish gating and rejection reasons. Define a small fixed taxonomy and enforce it at form validation time. Require structured completion feedback before generating the proof artifact.


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow Confirm a credible proof-of-work artifact format with pilot users Set a concrete pilot threshold for supply, applications, and completions before scaling outreach


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The first organization segment is still too broad Narrow the first supply segment to one repeatable organization class and one mission family


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


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
- [demand_validation] Legal framing for short missions in France is not yet validated
- [demand_validation] Demand-supply balance in Paris is unproven
- [demand_validation] Legal-safe mission framing for France is not yet validated.

### quality_assurance
- [quality_assurance] Trust model for preventing free-labor abuse is not yet proven

### privacy_trust
- [privacy_trust] The trust model for preventing exploitative or vague missions is not yet enforced in product.
- [privacy_trust] Trust protections against exploitative or vague missions are not yet proven

### market_motion
- [market_motion] Manual matching and moderation are required but not yet specified as an operational control surface.
- [market_motion] The pilot depends on proving enough organization-side mission supply in Paris

## Global Required Improvements

### demand_validation
- [demand_validation] Validate mission wording and disclaimer language with French legal review
- [demand_validation] Validate France-specific mission wording and disclaimers before launch.
- [demand_validation] Validate the France-specific mission structure and disclaimers before public launch

### market_motion
- [market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow
- [market_motion] Build an internal admin console for matching, moderation, and completion review.
- [market_motion] Run a concierge pilot with a small set of organizations to test repeat mission posting and completion

### quality_assurance
- [quality_assurance] Tighten the mission approval rubric so vague or labor-like postings are rejected consistently
- [quality_assurance] Add a hard mission approval workflow with rejection reasons and publish gating.
- [quality_assurance] Define a narrow mission taxonomy and enforce it in the posting form.
- [quality_assurance] Implement a strict approval rubric for mission scope, duration, and deliverables

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Trust model for preventing free-labor abuse is not yet proven Tighten the mission approval rubric so vague or labor-like postings are rejected consistently Add a hard mission approval workflow with rejection reasons and publish gating. Define a narrow mission taxonomy and enforce it in the posting form. Implement a strict approval rubric for mission scope, duration, and deliverables


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow Manual matching and moderation are required but not yet specified as an operational control surface. Build an internal admin console for matching, moderation, and completion review. The pilot depends on proving enough organization-side mission supply in Paris Run a concierge pilot with a small set of organizations to test repeat mission posting and completion


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Legal framing for short missions in France is not yet validated Demand-supply balance in Paris is unproven Validate mission wording and disclaimer language with French legal review Legal-safe mission framing for France is not yet validated. Validate France-specific mission wording and disclaimers before launch. Validate the France-specific mission structure and disclaimers before public launch


## Expected Output

A concrete demand-validation approach with a signal threshold.


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
- [demand_validation] Legal framing for short missions in France is not yet validated
- [demand_validation] Demand-supply balance in Paris is unproven
- [demand_validation] France-specific legal framing is not yet validated
- [demand_validation] The demand signal threshold is not defined clearly enough

### quality_assurance
- [quality_assurance] Trust model for preventing free-labor abuse is not yet proven
- [quality_assurance] Mission quality control is not yet formalized into a hard approval workflow.
- [quality_assurance] The launch taxonomy is not yet specified tightly enough to enforce scope.
- [quality_assurance] Proof-of-work issuance is not yet tied to structured completion feedback.

### scope
- [scope] The first organization segment is still too broad

## Global Required Improvements

### demand_validation
- [demand_validation] Validate mission wording and disclaimer language with French legal review
- [demand_validation] Define and validate a Paris/France mission template and disclaimer set before public launch

### market_motion
- [market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow
- [market_motion] Confirm a credible proof-of-work artifact format with pilot users
- [market_motion] Set a concrete pilot threshold for supply, applications, and completions before scaling outreach

### quality_assurance
- [quality_assurance] Tighten the mission approval rubric so vague or labor-like postings are rejected consistently
- [quality_assurance] Implement a mandatory mission moderation state machine with publish gating and rejection reasons.
- [quality_assurance] Define a small fixed taxonomy and enforce it at form validation time.
- [quality_assurance] Require structured completion feedback before generating the proof artifact.

### scope
- [scope] Narrow the first supply segment to one repeatable organization class and one mission family

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Trust model for preventing free-labor abuse is not yet proven Tighten the mission approval rubric so vague or labor-like postings are rejected consistently Add a hard mission approval workflow with rejection reasons and publish gating. Define a narrow mission taxonomy and enforce it in the posting form. Implement a strict approval rubric for mission scope, duration, and deliverables


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow Manual matching and moderation are required but not yet specified as an operational control surface. Build an internal admin console for matching, moderation, and completion review. The pilot depends on proving enough organization-side mission supply in Paris Run a concierge pilot with a small set of organizations to test repeat mission posting and completion


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] Legal framing for short missions in France is not yet validated Demand-supply balance in Paris is unproven Validate mission wording and disclaimer language with French legal review Legal-safe mission framing for France is not yet validated. Validate France-specific mission wording and disclaimers before launch. Validate the France-specific mission structure and disclaimers before public launch


## Expected Output

A concrete demand-validation approach with a signal threshold.


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
- [demand_validation] Legal framing for short missions in France is not yet validated
- [demand_validation] Demand-supply balance in Paris is unproven
- [demand_validation] France-specific legal framing is not yet validated
- [demand_validation] The demand signal threshold is not defined clearly enough

### quality_assurance
- [quality_assurance] Trust model for preventing free-labor abuse is not yet proven
- [quality_assurance] Mission quality control is not yet formalized into a hard approval workflow.
- [quality_assurance] The launch taxonomy is not yet specified tightly enough to enforce scope.
- [quality_assurance] Proof-of-work issuance is not yet tied to structured completion feedback.

### scope
- [scope] The first organization segment is still too broad

## Global Required Improvements

### demand_validation
- [demand_validation] Validate mission wording and disclaimer language with French legal review
- [demand_validation] Define and validate a Paris/France mission template and disclaimer set before public launch

### market_motion
- [market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow
- [market_motion] Confirm a credible proof-of-work artifact format with pilot users
- [market_motion] Set a concrete pilot threshold for supply, applications, and completions before scaling outreach

### quality_assurance
- [quality_assurance] Tighten the mission approval rubric so vague or labor-like postings are rejected consistently
- [quality_assurance] Implement a mandatory mission moderation state machine with publish gating and rejection reasons.
- [quality_assurance] Define a small fixed taxonomy and enforce it at form validation time.
- [quality_assurance] Require structured completion feedback before generating the proof artifact.

### scope
- [scope] Narrow the first supply segment to one repeatable organization class and one mission family

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Trust model for preventing free-labor abuse is not yet proven Tighten the mission approval rubric so vague or labor-like postings are rejected consistently Mission quality control is not yet formalized into a hard approval workflow. The launch taxonomy is not yet specified tightly enough to enforce scope. Proof-of-work issuance is not yet tied to structured completion feedback. Implement a mandatory mission moderation state machine with publish gating and rejection reasons. Define a small fixed taxonomy and enforce it at form validation time. Require structured completion feedback before generating the proof artifact.


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow Confirm a credible proof-of-work artifact format with pilot users Set a concrete pilot threshold for supply, applications, and completions before scaling outreach


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The first organization segment is still too broad Narrow the first supply segment to one repeatable organization class and one mission family


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


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
- [demand_validation] Legal framing for short missions in France is not yet validated
- [demand_validation] Demand-supply balance in Paris is unproven
- [demand_validation] The proof-of-work value has not been validated with hiring-side users

### quality_assurance
- [quality_assurance] Trust model for preventing free-labor abuse is not yet proven
- [quality_assurance] Mission quality control is not yet formalized into an enforced workflow
- [quality_assurance] Proof-of-work issuance is not yet tied to structured completion feedback

### scope
- [scope] The launch taxonomy is not yet specified tightly enough to enforce scope

### market_motion
- [market_motion] The launch audience is still too broad and needs a single trusted entry segment
- [market_motion] The first market motion is not yet constrained to one mission type and one acquisition path

## Global Required Improvements

### demand_validation
- [demand_validation] Validate mission wording and disclaimer language with French legal review
- [demand_validation] Validate proof-of-work usefulness with a small set of recruiters or hiring managers

### market_motion
- [market_motion] Run a concierge pilot to test whether startups and candidates complete the workflow
- [market_motion] Confirm a credible proof-of-work artifact format with pilot users
- [market_motion] Define one narrow first audience: Paris-based trusted organizations already in founder reach

### quality_assurance
- [quality_assurance] Tighten the mission moderation rubric so vague or labor-like postings are rejected consistently
- [quality_assurance] Implement a mandatory moderation state machine with publish gating and rejection reasons
- [quality_assurance] Require structured completion feedback before generating the proof artifact

### scope
- [scope] Define a small fixed mission taxonomy and enforce it at form validation time
- [scope] Limit launch to one bounded mission category with explicit deliverables

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Trust model for preventing free-labor abuse is not yet proven Tighten the mission approval rubric so vague or labor-like postings are rejected consistently Mission quality control is not yet formalized into a hard approval workflow. The launch taxonomy is not yet specified tightly enough to enforce scope. Proof-of-work issuance is not yet tied to structured completion feedback. Implement a mandatory mission moderation state machine with publish gating and rejection reasons. Define a small fixed taxonomy and enforce it at form validation time. Require structured completion feedback before generating the proof artifact.


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot to test whether organizations and candidates complete the workflow Confirm a credible proof-of-work artifact format with pilot users Set a concrete pilot threshold for supply, applications, and completions before scaling outreach


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] The first organization segment is still too broad Narrow the first supply segment to one repeatable organization class and one mission family


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Add a **mandatory moderation state machine** for every mission, with `submitted`, `under_review`, `approved`, `rejected`, and `published` as enforced states. [quality_assurance]
- [tech] Add a **fixed mission taxonomy** at form validation time so organizations cannot submit open-ended or unclassified work. [scope]

## Growth Structural Decisions

### growth
- [growth] Add a defined **pilot audience**: “Paris-based small companies, startups, and associations already known to the founders” [market_motion]
- [growth] Add a **single mission category** for launch, rather than a broad taxonomy [scope]

## Product Locking

## Applied

True


## Confirmed In Scope

- Paris-only pilot
- Startups only as the launch customer segment
- One mission family only: short product/UX-support missions
- Mandatory mission moderation and rejection reasons
- Fixed mission taxonomy
- Manual matching/admin queue
- Basic application, messaging, deliverable submission, completion, and proof-of-work issuance
- Structured feedback before proof issuance


## Confirmed Deferred

- Algorithmic matching
- Reputation scoring
- Payments or escrow rails
- Rich analytics
- Multi-country compliance handling
- Automated contract workflows
- Advanced fraud detection
- Public candidate portfolios with social features
- Additional organization types
- Additional mission families


## Confirmed Out Of Scope

- Open-ended freelance marketplace
- Broad taxonomy at launch
- Self-serve public posting without approval
- Chat-heavy collaboration tools
- Community features
- Time tracking
- AI-generated mission creation or candidate ranking
- Dispute resolution beyond manual handling
- Full employment or internship administration


## Locking Note

- Scope remains intentionally narrow to prove the exchange, trust model, and proof-of-work value before any expansion.


## Expert Contributions

### Tech Summary

The MVP is feasible only if it is built as a tightly controlled concierge platform, not as an open marketplace. The main correction is to formalize mission quality control as a hard moderation workflow with a fixed taxonomy, approval gating, and proof issuance only after structured feedback.

## Tech Structural Decisions

- Add a **mandatory moderation state machine** for every mission, with `submitted`, `under_review`, `approved`, `rejected`, and `published` as enforced states. [quality_assurance]
- Add a **fixed mission taxonomy** at form validation time so organizations cannot submit open-ended or unclassified work. [scope]


## Tech Recommendations

- Add a **mandatory moderation state machine** for every mission, with `submitted`, `under_review`, `approved`, `rejected`, and `published` as enforced states. [quality_assurance]
- Add a **fixed mission taxonomy** at form validation time so organizations cannot submit open-ended or unclassified work. [scope]
- Add **structured rejection reasons** in the admin workflow so moderation decisions are consistent and auditable. [quality_assurance]
- Gate **proof-of-work generation** on mandatory structured completion feedback from the organization. [quality_assurance]
- Make the **approval queue an internal control surface** rather than a passive content review step. [quality_assurance]


## Tech Risks

- Moderation may become the bottleneck if the taxonomy is too broad or approvals are too manual.
- Organizations may still attempt to stretch bounded missions into ongoing labor.
- Proof artifacts may lose credibility if completion feedback is inconsistent.


## Tech Open Questions

- What are the exact 3 to 5 mission categories allowed at launch?
- Which fields are mandatory to classify a mission as bounded and safe?
- What minimum feedback schema is needed before proof issuance?


### Growth Summary

The main launch challenge is not building a marketplace; it is proving that a small set of Paris organizations will trust the format enough to post real missions and that candidates will complete them for credible proof-of-work. The right GTM direction is a founder-led, concierge pilot with a tightly constrained mission type and a small, trusted supply-first launch.

## Growth Structural Decisions

- Add a defined **pilot audience**: “Paris-based small companies, startups, and associations already known to the founders” [market_motion]
- Add a **single mission category** for launch, rather than a broad taxonomy [scope]


## Growth Recommendations

- Add a defined **pilot audience**: “Paris-based small companies, startups, and associations already known to the founders” [market_motion]
- Add a **single mission category** for launch, rather than a broad taxonomy [scope]
- Add a **pilot threshold** for supply and completion before expanding outreach [demand_validation]
- Add a **proof-of-work acceptance criterion** that tests whether the artifact is useful in real applications [quality_assurance]
- Add a **mission trust gate** that explicitly blocks unpaid labor-like or vague missions [privacy_trust]


## Growth Risks

- Organizations may treat the platform as a source of cheap or free labor.
- Candidate supply may exist, but not convert into completions.
- The proof-of-work artifact may not be credible enough to influence hiring.


## Growth Open Questions

- Which exact mission type is the safest and most credible first wedge in Paris?
- What proof-of-work format do hiring managers actually value?
- Which organization segment is most likely to accept a concierge pilot first?


## Product Arbitration

## Source

parsed


## Retained

- Mandatory moderation state machine for every mission [quality_assurance]
- Fixed mission taxonomy at launch [scope]
- Structured rejection reasons in moderation [quality_assurance]
- Proof-of-work issuance only after structured completion feedback [quality_assurance]
- Founder-led concierge pilot [market_motion]
- Mission trust gate blocking vague or labor-like postings [privacy_trust]
- Pilot threshold before broadening outreach [demand_validation]
- Proof-of-work acceptance criterion tested in real applications [quality_assurance]
- Paris-only launch scope [scope]


## Deferred

- Algorithmic matching [quality_assurance]
- Reputation scoring [quality_assurance]
- Payments or escrow rails [scope]
- Rich analytics [scope]
- Multi-country compliance handling [scope]
- Automated contract workflows [legal_risk]
- Advanced fraud detection [quality_assurance]
- Public candidate portfolios with social features [scope]
- Broad mission taxonomy beyond launch family [scope]
- Additional organization types beyond startups [scope]


## Rejected

- Open-ended freelance marketplace [scope]
- Self-serve public posting without approval [quality_assurance]
- Chat-heavy collaboration tools [scope]
- Community features [scope]
- Time tracking [scope]
- AI-generated mission creation or candidate ranking [quality_assurance]
- Dispute resolution system beyond manual handling [scope]
- Full employment or internship administration [legal_risk]


## Open Points

- Exact legal framing and disclaimer language for short missions in France [legal_risk]
- Exact proof-of-work artifact format that hiring managers value [proof_credibility]
- Minimum feedback schema required before proof issuance [quality_assurance]
- Exact startup qualification criteria for the pilot [market_motion]


## Rationales

- The project only works if moderation is a hard control surface, not a soft review step [quality_assurance]
- A single launch segment and one mission family are enough to test whether the exchange is valuable without drifting into marketplace sprawl [scope]
- Startup-only launch reduces variability and improves trust during the pilot [market_motion]
- Broadening the organization mix too early would weaken the proof of value and increase moderation risk [demand_validation]
- Requiring structured feedback before proof issuance is necessary for credibility [quality_assurance]
- Legal uncertainty is material in France and must be reduced before scale [legal_risk]


## Reconciliation Notes

- Parsed Product Arbitration supplied by Product; heuristic reconciliation was not needed.


## Reconciliation Warnings

_Aucune contradiction détectée._


## Source PRD

_Aucun contenu._

## Initial PRD

# SkillBridge — MVP Product Proposal

## Product Problem
Recent graduates and career switchers in Paris struggle to prove practical experience fast enough to access junior roles.

Small companies, startups, and associations need short, affordable help on real work but do not want to hire full-time or use agencies.

The product must solve both sides with a narrow, trusted exchange: real short missions that create credible experience for candidates and useful output for organizations.

## Initial Wedge
Start with vetted, short, low-risk, portfolio-building missions for Paris-based small organizations that can be completed in 2 to 4 weeks.

The wedge is not “all freelance work.” It is “structured starter missions” for early-career talent that are simple enough to scope, review, and complete without deep client management.

Best initial wedge:
- remote-first missions
- one-function tasks with clear outputs
- low legal ambiguity
- measurable deliverables

## First Target User
Primary user:
- Recent graduates and career switchers in Paris with little or no professional experience, actively seeking their first credible project proof

Primary supply-side customer:
- Small businesses, startups, and associations in Paris that need a defined piece of work and cannot justify a hire or agency fee

First use case:
- A candidate completes a short structured mission, receives feedback and a portfolio artifact, and can show proof of work in applications

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Internships
- Unpaid volunteering
- Freelance marketplaces
- Job boards
- Informal networking and referrals
- Student association projects or hackathons

Why they are not enough:
- Internships are slower to access and often require commitment beyond a short project
- Freelance marketplaces skew toward paid execution and experienced workers
- Job boards do not solve the experience gap
- Informal projects are hard to verify and standardize

Switching trigger:
- The user needs a credible, structured project credential now, not a long internship or a competitive entry-level job
- The organization needs a small piece of work completed with low overhead and some trust in delivery

## Core MVP Workflow
1. An organization submits a mission with a template: objective, scope, duration, deliverable, required skills, location, and whether it is paid or unpaid
2. The platform reviews or lightly vets the mission before it goes live
3. Candidates browse a limited set of missions and apply with a short profile and motivation
4. The organization selects one candidate or a small cohort
5. Candidate and organization complete the mission using basic messaging and deliverable submission
6. Organization gives structured feedback and confirms completion
7. Candidate receives a verified proof-of-work artifact for their profile

## In Scope
- Candidate profiles with basic skills, education, availability, and location
- Organization profiles with identity and basic verification
- Mission posting using a strict template
- Manual or lightweight moderation of missions before publication
- Simple browse and apply flow
- Basic messaging
- Deliverable upload or link submission
- Completion confirmation
- Structured feedback
- Verified proof-of-work artifact for completed missions
- Basic trust signals such as organization verification and mission rules
- Paris-only launch scope

## Out of Scope
- Open-ended freelance marketplace
- Payment processing in MVP unless required for a specific mission type
- Complex algorithmic matching
- Ratings/reputation marketplace mechanics
- Multi-country launch
- Full employment or internship administration
- Contract generation for every possible legal case
- Time tracking
- Escrow
- Deep analytics dashboards
- AI-generated mission creation or candidate ranking
- Community features
- Chat-heavy collaboration tools
- Dispute resolution system beyond manual handling

## MVP Build Vs Pilot Operations
### Must Build Now
- Candidate profile creation
- Organization profile creation
- Mission posting template
- Mission listing and browsing
- Application submission
- Basic messaging
- Deliverable submission
- Completion status
- Feedback capture
- Proof-of-work artifact generation
- Lightweight verification and moderation controls

### Manual Or Operational During Pilot
- Mission sourcing from a small set of trusted organizations
- Review of mission scope before publication
- Candidate screening for suitability
- Matching assistance when supply is thin
- Human review of completed deliverables if needed
- Support for disputes or unclear mission scope
- Legal review of mission templates and disclaimers for France

### Deferred Until After Proof
- Algorithmic matching
- Reputation scoring
- Payments or escrow rails
- Rich analytics
- Multi-country compliance handling
- Full messaging suite
- Public candidate portfolios with social features
- Automated contract workflows
- Advanced fraud detection

## Business Model Hypothesis
Primary hypothesis:
- Charge organizations a fee for posting or filling a mission, or a subscription for access to vetted candidates and structured missions

Secondary hypothesis:
- Offer candidates free access to maximize supply and reduce adoption friction

Most plausible early model:
- Organization-side fee only, because the product value is concentrated on hiring relief and task completion
- If trust is weak, keep pilot missions free or subsidized to focus on proof, then test charging after retention and completion are demonstrated

## Critical Assumptions
- Organizations will post real missions instead of treating the platform as a free labor source
- Candidates will value short missions enough to join and complete them
- The platform can vet missions well enough to avoid exploitative or vague work
- Short missions can produce useful proof of skill for entry-level hiring
- Paris has enough concentrated demand and supply for a narrow pilot
- Legal framing can be kept within safe boundaries for France
- A lightweight trust model is sufficient at first

## How To Test Quickly
- Recruit 10 to 15 Paris organizations through direct outreach and existing networks
- Ask each organization to submit one real mission using a strict template
- Manually vet the missions for scope, feasibility, and risk
- Recruit 20 to 30 candidates from universities, bootcamps, and career-switcher communities
- Run the pilot with manual matching and structured completion tracking
- Measure whether missions are accepted, completed, and perceived as credible proof
- Interview both sides after completion to identify friction and trust issues

## Acceptance Criteria
- At least 5 vetted missions are posted in Paris within the pilot window
- At least 10 candidates apply to available missions
- At least 3 missions are matched and completed
- At least 2 organizations say the output was useful enough to repeat
- At least 2 candidates say the proof-of-work artifact improves their job applications
- No material trust or legal issues emerge from the pilot format
- Mission quality remains structured and not indistinguishable from generic freelance gigs

## Risks And Failure Modes
- Organizations post vague or exploitative missions
- Candidates treat it like unpaid labor with weak career value
- Supply and demand fail to match early, causing low activity
- The product drifts into a low-quality freelance marketplace
- Trust breaks if deliverables are not useful or feedback is inconsistent
- Legal boundaries around unpaid work or work-like arrangements create risk in France
- Manual moderation becomes too heavy to scale

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Legal framing for short missions in France is not yet validated [legal_risk]
- Trust model for preventing free-labor abuse is not yet proven [trust_model]
- Demand-supply balance in Paris is unproven [market_liquidity]

Required Improvements:
- Validate mission structure and disclaimer language with French legal review [legal_review]
- Define a stricter mission approval rubric to block vague or exploitative postings [quality_gate]
- Run a concierge pilot to test whether organizations and candidates both complete the workflow [pilot_validation]

## Recommendation
Proceed with a concierge-style pilot in Paris, not a full product build.

The narrowest credible MVP is a vetted mission marketplace for short starter projects with proof-of-work completion, not a general freelance platform.

Build only the workflow needed to prove:
- real organizations will post credible missions
- early-career candidates will complete them
- the resulting artifact is valued as proof of experience

If the pilot cannot confirm legal safety, mission quality, and repeat demand, do not scale the product yet.

## Retained Decisions

- Mandatory moderation state machine for every mission [quality_assurance]
- Fixed mission taxonomy at launch [scope]
- Structured rejection reasons in moderation [quality_assurance]
- Proof-of-work issuance only after structured completion feedback [quality_assurance]
- Founder-led concierge pilot [market_motion]
- Mission trust gate blocking vague or labor-like postings [privacy_trust]
- Pilot threshold before broadening outreach [demand_validation]
- Proof-of-work acceptance criterion tested in real applications [quality_assurance]
- Paris-only launch scope [scope]

## Deferred Decisions

- Algorithmic matching [quality_assurance]
- Reputation scoring [quality_assurance]
- Payments or escrow rails [scope]
- Rich analytics [scope]
- Multi-country compliance handling [scope]
- Automated contract workflows [legal_risk]
- Advanced fraud detection [quality_assurance]
- Public candidate portfolios with social features [scope]
- Broad mission taxonomy beyond launch family [scope]
- Additional organization types beyond startups [scope]

## Rejected Recommendations

- Open-ended freelance marketplace [scope]
- Self-serve public posting without approval [quality_assurance]
- Chat-heavy collaboration tools [scope]
- Community features [scope]
- Time tracking [scope]
- AI-generated mission creation or candidate ranking [quality_assurance]
- Dispute resolution system beyond manual handling [scope]
- Full employment or internship administration [legal_risk]

## Unresolved Tensions

- Tech recommendation needing arbitration: Add a **fixed mission taxonomy** at form validation time so organizations cannot submit open-ended or unclassified work. [scope]
- Tech recommendation needing arbitration: Add **structured rejection reasons** in the admin workflow so moderation decisions are consistent and auditable. [quality_assurance]
- Tech recommendation needing arbitration: Gate **proof-of-work generation** on mandatory structured completion feedback from the organization. [quality_assurance]
- Tech recommendation needing arbitration: Make the **approval queue an internal control surface** rather than a passive content review step. [quality_assurance]
- Growth recommendation needing arbitration: Add a **single mission category** for launch, rather than a broad taxonomy [scope]
- Growth recommendation needing arbitration: Add a **pilot threshold** for supply and completion before expanding outreach [demand_validation]
- Growth recommendation needing arbitration: Add a **proof-of-work acceptance criterion** that tests whether the artifact is useful in real applications [quality_assurance]
- Growth recommendation needing arbitration: Add a **mission trust gate** that explicitly blocks unpaid labor-like or vague missions [privacy_trust]
- Tech open question: What are the exact 3 to 5 mission categories allowed at launch?
- Tech open question: Which fields are mandatory to classify a mission as bounded and safe?
- Tech open question: What minimum feedback schema is needed before proof issuance?
- Growth open question: Which exact mission type is the safest and most credible first wedge in Paris?
- Growth open question: What proof-of-work format do hiring managers actually value?
- Growth open question: Which organization segment is most likely to accept a concierge pilot first?

## Applied Changes

- Mandatory moderation state machine for every mission [quality_assurance]
- Fixed mission taxonomy at launch [scope]
- Structured rejection reasons in moderation [quality_assurance]
- Proof-of-work issuance only after structured completion feedback [quality_assurance]
- Founder-led concierge pilot [market_motion]
- Mission trust gate blocking vague or labor-like postings [privacy_trust]
- Pilot threshold before broadening outreach [demand_validation]
- Proof-of-work acceptance criterion tested in real applications [quality_assurance]
- Paris-only launch scope [scope]

## Remaining Open Points

- Exact legal framing and disclaimer language for short missions in France [legal_risk]
- Exact proof-of-work artifact format that hiring managers value [proof_credibility]
- Minimum feedback schema required before proof issuance [quality_assurance]
- Exact startup qualification criteria for the pilot [market_motion]

## Risks

- Organizations use the platform to source free or underpaid labor.
- Candidate demand is high but mission supply stays thin.
- Missions are too broad to be completed cleanly in 2–4 weeks.
- Missions may still be interpreted as free labor or internship substitution in France. [legal_risk]
- Manual moderation may become the bottleneck if mission volume rises. [quality_assurance]
- Candidates may apply broadly while organizations remain selective, creating operational imbalance. [market_motion]
- Operators may still approve missions too loosely if the rubric is underspecified.
- The taxonomy may be too narrow to source enough missions in Paris.
- Manual moderation may become the bottleneck if volume rises unexpectedly.
- Organizations may try to use the platform for free labor instead of bounded starter work.
- Candidates may perceive the experience as disguised unpaid work.
- The Paris supply pool may be too thin for repeat mission flow.
- Moderation may become the bottleneck if the taxonomy is too broad or approvals are too manual.
- Organizations may still attempt to stretch bounded missions into ongoing labor.
- Proof artifacts may lose credibility if completion feedback is inconsistent.
- Organizations may treat the platform as a source of cheap or free labor.
- Candidate supply may exist, but not convert into completions.
- The proof-of-work artifact may not be credible enough to influence hiring.

## Open Questions

- Which 2–3 mission categories are safest and most credible for the Paris pilot?
- Are pilot missions paid, unpaid, or mixed, and what is the minimum acceptable structure?
- What exact proof artifact will candidates be able to show to employers?
- Which exact mission categories are allowed in the Paris pilot?
- Are pilot missions paid, unpaid, or mixed, and what is the minimum acceptable structure?
- What legal wording and disclaimers are required for France?
- Which exact mission categories are in the initial approved taxonomy?
- What minimum fields are mandatory for a mission to be reviewable?
- What rejection reasons should be standardized in the moderation rubric?
- What exact France-compliant mission framing will be used for unpaid or lightly compensated work?
- Which 1–2 organization types are most likely to repeat missions fastest in Paris?
- What minimum proof-of-work artifact is actually considered credible by hiring managers?
- What are the exact 3 to 5 mission categories allowed at launch?
- Which fields are mandatory to classify a mission as bounded and safe?
- What minimum feedback schema is needed before proof issuance?
- Which exact mission type is the safest and most credible first wedge in Paris?
- What proof-of-work format do hiring managers actually value?
- Which organization segment is most likely to accept a concierge pilot first?

## Final Revised PRD

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

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Mandatory moderation state machine for every mission [quality_assurance]
- Fixed mission taxonomy at launch [scope]
- Structured rejection reasons in moderation [quality_assurance]
- Proof-of-work issuance only after structured completion feedback [quality_assurance]
- Founder-led concierge pilot [market_motion]
- Mission trust gate blocking vague or labor-like postings [privacy_trust]
- Pilot threshold before broadening outreach [demand_validation]
- Proof-of-work acceptance criterion tested in real applications [quality_assurance]
- Paris-only launch scope [scope]

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- growth_agent: gtm_notes_generated
- tech_agent: architecture_notes_generated
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
- product_agent: arbitration_reconciled
