# Blackboard

## Project Brief

Project Name: LocalLoop

Pitch:
A mobile application that helps people discover local independent businesses through personalized recommendations, neighborhood deals, and loyalty rewards.

Context:
Many consumers want to support local businesses but often default to large platforms because discovering small local stores, restaurants, services, and events is fragmented and inconvenient.

At the same time, independent businesses struggle with visibility and customer retention but often lack the budget or expertise to run digital marketing campaigns.

The platform helps consumers discover relevant local businesses while giving small businesses simple tools to attract and retain nearby customers.

Target Users:
- Urban residents
- Young professionals
- Families
- Tourists
- Independent local businesses

Potential Use Cases:
- Discover nearby coffee shops
- Find local restaurants with promotions
- Discover niche stores
- Access loyalty rewards
- Local event discovery
- Neighborhood recommendations

Platform Capabilities:
- Personalized recommendations
- Geolocation
- Merchant profiles
- Promotions/offers
- Loyalty system
- Reviews
- Local event feed

Constraints:
- Limited initial budget
- Need enough local business supply in one city before expanding
- Must avoid competing directly with massive horizontal platforms

Challenges:
- Convincing local businesses to join
- Maintaining recommendation quality
- Avoiding platform saturation with irrelevant offers

Long-term Vision:
Become the default discovery platform for local commerce and neighborhood experiences.

## Project Brief Source

projects/project-LocalLoop.md

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


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### market_motion
- [market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful
- [market_motion] Need enough pilot data to apply the proceed/revise/reject decision rule

### untagged
- Need evidence that simple offers plus loyalty can change behavior versus existing tools

### metrics_validation
- [metrics_validation] Need validation that merchants will renew after seeing redemption value

## Product Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers
- [market_motion] Define and use one canonical redemption method across the pilot
- [market_motion] Collect pilot metrics against the explicit success threshold before launch expansion

### scope
- [scope] Measure first-visit and repeat-visit behavior before expanding scope

### demand_validation
- [demand_validation] Validate merchant willingness to continue through direct renewal conversations

## Tech Status

LIMITED


## Tech Blocking Gaps

### quality_assurance
- [quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish

### operations
- [operations] No canonical redemption/dispute state machine defined for reliable support handling

### untagged
- No explicit role model for who can verify, suspend, reactivate, or override merchant ranking

## Tech Required Improvements

### operations
- [operations] Implement a review queue with approve/reject/suspend actions and required reason codes

### untagged
- Define and implement redemption states including dispute and void paths in the backend
- Add re-verification and suspension controls for merchant lifecycle management

### privacy_trust
- [privacy_trust] Restrict admin actions through role-based permissions and log all actions immutably

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] No quantified minimum merchant density for a credible neighborhood launch
- [market_motion] No single primary acquisition motion defined for merchant supply
- [market_motion] Launch audience is still too broad relative to the pilot wedge

### metrics_validation
- [metrics_validation] Merchant renewal proof is not yet tied to a clear threshold

## Growth Required Improvements

### market_motion
- [market_motion] Set a minimum verified merchant count and freshness threshold before consumer launch.
- [market_motion] Commit to founder-led merchant recruitment as the primary acquisition motion.
- [market_motion] Narrow the first audience to nearby urban young professionals in the launch neighborhood.
- [market_motion] Define the merchant renewal trigger as a launch gate, not just a post-pilot interview.

## Global Status

LIMITED


## Global Blocking Gaps

### market_motion
- [market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful
- [market_motion] Need enough pilot data to apply the proceed/revise/reject decision rule
- [market_motion] No quantified minimum merchant density for a credible neighborhood launch
- [market_motion] No single primary acquisition motion defined for merchant supply
- [market_motion] Launch audience is still too broad relative to the pilot wedge

### untagged
- Need evidence that simple offers plus loyalty can change behavior versus existing tools
- No explicit role model for who can verify, suspend, reactivate, or override merchant ranking

### metrics_validation
- [metrics_validation] Need validation that merchants will renew after seeing redemption value
- [metrics_validation] Merchant renewal proof is not yet tied to a clear threshold

### quality_assurance
- [quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish

### operations
- [operations] No canonical redemption/dispute state machine defined for reliable support handling

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers
- [market_motion] Define and use one canonical redemption method across the pilot
- [market_motion] Collect pilot metrics against the explicit success threshold before launch expansion
- [market_motion] Set a minimum verified merchant count and freshness threshold before consumer launch.
- [market_motion] Commit to founder-led merchant recruitment as the primary acquisition motion.
- [market_motion] Narrow the first audience to nearby urban young professionals in the launch neighborhood.
- [market_motion] Define the merchant renewal trigger as a launch gate, not just a post-pilot interview.

### scope
- [scope] Measure first-visit and repeat-visit behavior before expanding scope

### demand_validation
- [demand_validation] Validate merchant willingness to continue through direct renewal conversations

### operations
- [operations] Implement a review queue with approve/reject/suspend actions and required reason codes

### untagged
- Define and implement redemption states including dispute and void paths in the backend
- Add re-verification and suspension controls for merchant lifecycle management

### privacy_trust
- [privacy_trust] Restrict admin actions through role-based permissions and log all actions immutably

## Known Tags

- demand_validation
- market_motion
- metrics_validation
- untagged
- operations
- privacy_trust
- scope
- quality_assurance


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

Turn the quality gap into one operational control for reviewing and validating submissions.


## Source Gap

[quality_assurance] Add an ops-owned verification and moderation workflow with audit logging and suspension controls.


## Expected Output

One operational control or workflow that prevents low-quality or unsafe submissions.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers Define and use one canonical redemption method across the pilot The pilot depends on a reliable, auditable redemption workflow that is simple enough for merchant staff to use consistently. The MVP lacks a defined minimum supply threshold for launch, so the app could ship into an empty or weak market. Define the minimum verified merchant count and freshness requirements before enabling consumer launch. No quantified merchant density threshold for a credible neighborhood launch Set a minimum launch-density rule for one neighborhood and one category


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

- tech


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Define the first and second visit success metrics before public launch


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


### Loop 2

#### Tech Task

## Task

Turn the quality gap into one operational control for reviewing and validating submissions.


## Source Gap

[quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish. No canonical redemption/dispute state machine defined for reliable support handling. Implement a review queue with approve/reject/suspend actions, required reason codes, and audit logging. Define and implement redemption states, including dispute and void paths, in the backend. Add re-verification and suspension controls for merchant lifecycle management.


## Expected Output

One operational control or workflow that prevents low-quality or unsafe submissions.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful Need enough pilot data to apply the proceed/revise/reject decision rule Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers Define and use one canonical redemption method across the pilot Collect pilot metrics against the explicit success threshold before launch expansion No quantified minimum merchant density for a credible neighborhood launch No single primary acquisition motion defined for merchant supply Set a minimum verified merchant count and freshness threshold before consumer launch Commit to founder-led merchant recruitment as the primary acquisition motion


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Measure first-visit and repeat-visit behavior before expanding scope


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Contributors

_Aucun contributeur._


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

### market_motion
- [market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful
- [market_motion] The pilot depends on a reliable, auditable redemption workflow that is simple enough for merchant staff to use consistently.
- [market_motion] The MVP lacks a defined minimum supply threshold for launch, so the app could ship into an empty or weak market.
- [market_motion] No quantified merchant density threshold for a credible neighborhood launch

### untagged
- Need evidence that simple offers plus loyalty can change behavior versus existing tools
- No explicit proof threshold for behavior change versus existing discovery tools

### demand_validation
- [demand_validation] Need validation that merchants will renew after seeing redemption value
- [demand_validation] No defined merchant renewal signal that proves willingness to pay or continue

### privacy_trust
- [privacy_trust] The system needs explicit operational ownership for verification, listing maintenance, and dispute handling to keep merchant state trustworthy.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers
- [market_motion] Define and use one canonical redemption method across the pilot
- [market_motion] Define the minimum verified merchant count and freshness requirements before enabling consumer launch.
- [market_motion] Set a minimum launch-density rule for one neighborhood and one category

### scope
- [scope] Measure first-visit and repeat-visit behavior before expanding scope

### demand_validation
- [demand_validation] Validate merchant willingness to continue through direct renewal conversations
- [demand_validation] Add a clear merchant continuation test tied to redemption evidence

### untagged
- Lock the redemption method to one simple, verifiable mechanism and define the exact state transitions.

### quality_assurance
- [quality_assurance] Add an ops-owned verification and moderation workflow with audit logging and suspension controls.

### metrics_validation
- [metrics_validation] Define the first and second visit success metrics before public launch

## Loop Tasks

##### Tech

## Task

Turn the quality gap into one operational control for reviewing and validating submissions.


## Source Gap

[quality_assurance] Add an ops-owned verification and moderation workflow with audit logging and suspension controls.


## Expected Output

One operational control or workflow that prevents low-quality or unsafe submissions.


##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers Define and use one canonical redemption method across the pilot The pilot depends on a reliable, auditable redemption workflow that is simple enough for merchant staff to use consistently. The MVP lacks a defined minimum supply threshold for launch, so the app could ship into an empty or weak market. Define the minimum verified merchant count and freshness requirements before enabling consumer launch. No quantified merchant density threshold for a credible neighborhood launch Set a minimum launch-density rule for one neighborhood and one category


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Define the first and second visit success metrics before public launch


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


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

### market_motion
- [market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful
- [market_motion] Need enough pilot data to apply the proceed/revise/reject decision rule
- [market_motion] No quantified minimum merchant density for a credible neighborhood launch
- [market_motion] No single primary acquisition motion defined for merchant supply

### untagged
- Need evidence that simple offers plus loyalty can change behavior versus existing tools
- No clear launch audience narrower than broad local consumers

### demand_validation
- [demand_validation] Need validation that merchants will renew after seeing redemption value

### quality_assurance
- [quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish.
- [quality_assurance] No canonical redemption/dispute state machine defined for reliable support handling.

### privacy_trust
- [privacy_trust] No explicit audit trail and approval gate for merchant and offer changes.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers
- [market_motion] Define and use one canonical redemption method across the pilot
- [market_motion] Collect pilot metrics against the explicit success threshold before launch expansion
- [market_motion] Set a minimum verified merchant count and freshness threshold before consumer launch
- [market_motion] Commit to founder-led merchant recruitment as the primary acquisition motion

### scope
- [scope] Measure first-visit and repeat-visit behavior before expanding scope

### demand_validation
- [demand_validation] Validate merchant willingness to continue through direct renewal conversations

### quality_assurance
- [quality_assurance] Implement a review queue with approve/reject/suspend actions, required reason codes, and audit logging.
- [quality_assurance] Define and implement redemption states, including dispute and void paths, in the backend.
- [quality_assurance] Add re-verification and suspension controls for merchant lifecycle management.

### privacy_trust
- [privacy_trust] Require admin approval for every merchant profile and offer before publication.

### untagged
- Narrow the first consumer audience to nearby young professionals in one walkable neighborhood

## Loop Tasks

##### Tech

## Task

Turn the quality gap into one operational control for reviewing and validating submissions.


## Source Gap

[quality_assurance] Add an ops-owned verification and moderation workflow with audit logging and suspension controls.


## Expected Output

One operational control or workflow that prevents low-quality or unsafe submissions.


##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers Define and use one canonical redemption method across the pilot The pilot depends on a reliable, auditable redemption workflow that is simple enough for merchant staff to use consistently. The MVP lacks a defined minimum supply threshold for launch, so the app could ship into an empty or weak market. Define the minimum verified merchant count and freshness requirements before enabling consumer launch. No quantified merchant density threshold for a credible neighborhood launch Set a minimum launch-density rule for one neighborhood and one category


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Define the first and second visit success metrics before public launch


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


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

### market_motion
- [market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful
- [market_motion] Need enough pilot data to apply the proceed/revise/reject decision rule
- [market_motion] No quantified minimum merchant density for a credible neighborhood launch
- [market_motion] No single primary acquisition motion defined for merchant supply

### untagged
- Need evidence that simple offers plus loyalty can change behavior versus existing tools
- No clear launch audience narrower than broad local consumers

### demand_validation
- [demand_validation] Need validation that merchants will renew after seeing redemption value

### quality_assurance
- [quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish.
- [quality_assurance] No canonical redemption/dispute state machine defined for reliable support handling.

### privacy_trust
- [privacy_trust] No explicit audit trail and approval gate for merchant and offer changes.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers
- [market_motion] Define and use one canonical redemption method across the pilot
- [market_motion] Collect pilot metrics against the explicit success threshold before launch expansion
- [market_motion] Set a minimum verified merchant count and freshness threshold before consumer launch
- [market_motion] Commit to founder-led merchant recruitment as the primary acquisition motion

### scope
- [scope] Measure first-visit and repeat-visit behavior before expanding scope

### demand_validation
- [demand_validation] Validate merchant willingness to continue through direct renewal conversations

### quality_assurance
- [quality_assurance] Implement a review queue with approve/reject/suspend actions, required reason codes, and audit logging.
- [quality_assurance] Define and implement redemption states, including dispute and void paths, in the backend.
- [quality_assurance] Add re-verification and suspension controls for merchant lifecycle management.

### privacy_trust
- [privacy_trust] Require admin approval for every merchant profile and offer before publication.

### untagged
- Narrow the first consumer audience to nearby young professionals in one walkable neighborhood

## Loop Tasks

##### Tech

## Task

Turn the quality gap into one operational control for reviewing and validating submissions.


## Source Gap

[quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish. No canonical redemption/dispute state machine defined for reliable support handling. Implement a review queue with approve/reject/suspend actions, required reason codes, and audit logging. Define and implement redemption states, including dispute and void paths, in the backend. Add re-verification and suspension controls for merchant lifecycle management.


## Expected Output

One operational control or workflow that prevents low-quality or unsafe submissions.


##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful Need enough pilot data to apply the proceed/revise/reject decision rule Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers Define and use one canonical redemption method across the pilot Collect pilot metrics against the explicit success threshold before launch expansion No quantified minimum merchant density for a credible neighborhood launch No single primary acquisition motion defined for merchant supply Set a minimum verified merchant count and freshness threshold before consumer launch Commit to founder-led merchant recruitment as the primary acquisition motion


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Measure first-visit and repeat-visit behavior before expanding scope


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


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

### market_motion
- [market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful
- [market_motion] Need enough pilot data to apply the proceed/revise/reject decision rule
- [market_motion] No quantified minimum merchant density for a credible neighborhood launch
- [market_motion] No single primary acquisition motion defined for merchant supply
- [market_motion] Launch audience is still too broad relative to the pilot wedge

### untagged
- Need evidence that simple offers plus loyalty can change behavior versus existing tools
- No explicit role model for who can verify, suspend, reactivate, or override merchant ranking

### metrics_validation
- [metrics_validation] Need validation that merchants will renew after seeing redemption value
- [metrics_validation] Merchant renewal proof is not yet tied to a clear threshold

### quality_assurance
- [quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish

### operations
- [operations] No canonical redemption/dispute state machine defined for reliable support handling

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers
- [market_motion] Define and use one canonical redemption method across the pilot
- [market_motion] Collect pilot metrics against the explicit success threshold before launch expansion
- [market_motion] Set a minimum verified merchant count and freshness threshold before consumer launch.
- [market_motion] Commit to founder-led merchant recruitment as the primary acquisition motion.
- [market_motion] Narrow the first audience to nearby urban young professionals in the launch neighborhood.
- [market_motion] Define the merchant renewal trigger as a launch gate, not just a post-pilot interview.

### scope
- [scope] Measure first-visit and repeat-visit behavior before expanding scope

### demand_validation
- [demand_validation] Validate merchant willingness to continue through direct renewal conversations

### operations
- [operations] Implement a review queue with approve/reject/suspend actions and required reason codes

### untagged
- Define and implement redemption states including dispute and void paths in the backend
- Add re-verification and suspension controls for merchant lifecycle management

### privacy_trust
- [privacy_trust] Restrict admin actions through role-based permissions and log all actions immutably

## Loop Tasks

##### Tech

## Task

Turn the quality gap into one operational control for reviewing and validating submissions.


## Source Gap

[quality_assurance] No defined ops-owned moderation workflow that blocks unsafe or low-quality submissions before publish. No canonical redemption/dispute state machine defined for reliable support handling. Implement a review queue with approve/reject/suspend actions, required reason codes, and audit logging. Define and implement redemption states, including dispute and void paths, in the backend. Add re-verification and suspension controls for merchant lifecycle management.


## Expected Output

One operational control or workflow that prevents low-quality or unsafe submissions.


##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need proof that one neighborhood can sustain enough verified merchant density to feel useful Need enough pilot data to apply the proceed/revise/reject decision rule Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers Define and use one canonical redemption method across the pilot Collect pilot metrics against the explicit success threshold before launch expansion No quantified minimum merchant density for a credible neighborhood launch No single primary acquisition motion defined for merchant supply Set a minimum verified merchant count and freshness threshold before consumer launch Commit to founder-led merchant recruitment as the primary acquisition motion


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Measure first-visit and repeat-visit behavior before expanding scope


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Add one explicit moderation workflow that blocks all submissions until reviewed and approved by ops [moderation_workflow]
- [tech] Define the canonical redemption state machine with dispute and void paths [state_machine]

## Growth Structural Decisions

### growth
- [growth] Define the **minimum verified merchant count** needed before consumer launch, plus a freshness threshold for active offers. [market_motion]
- [growth] Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]

## Product Locking

## Applied

True


## Confirmed In Scope

- One city, one neighborhood, one category: independent coffee shops/cafes
- Nearby discovery for urban young professionals
- Verified merchants only
- One active offer per merchant
- One canonical redemption flow
- Simple loyalty reward mechanic
- Admin review before publish
- Manual ranking overrides
- Redemption tracking with dispute/void handling
- Reason-coded admin actions with audit logging
- Merchant renewal checkpoint


## Confirmed Deferred

- Reviews
- Events feed
- Multi-category expansion
- Multi-city expansion
- Advanced personalization
- Push notification automation
- Merchant analytics dashboards
- In-app payments
- Social features
- Open self-serve merchant onboarding at scale
- Consumer growth automation


## Confirmed Out Of Scope

- Broad category coverage beyond coffee/cafes
- Delivery, reservations, or ordering
- Full-scale merchant CRM
- Public self-serve publishing without review
- Broad launch audience beyond nearby urban young professionals


## Locking Note

- MVP remains intentionally narrow and proof-oriented. - No new product surface area is added in this pass. - Pilot operations remain manual where they do not affect proof-critical trust or redemption reliability.


## Expert Contributions

### Tech Summary

The feasibility risk is not building the app; it is controlling quality and trust with a very small ops team. The right direction is a concierge MVP with strict admin review, a single redemption state machine, and manual curation until the pilot proves reliable behavior.

## Tech Structural Decisions

- Add one explicit moderation workflow that blocks all submissions until reviewed and approved by ops [moderation_workflow]
- Define the canonical redemption state machine with dispute and void paths [state_machine]


## Tech Recommendations

- Add one explicit moderation workflow that blocks all submissions until reviewed and approved by ops [moderation_workflow]
- Define the canonical redemption state machine with dispute and void paths [state_machine]
- Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Require reason codes and audit logging for every admin decision [audit_log]
- Specify a support resolution screen or workflow for redemption disputes [support_workflow]


## Tech Risks

- Merchant or offer quality slips if moderation is not consistently applied [quality_assurance]
- Redemption disputes damage trust if state transitions are ambiguous [state_machine]
- Ops turnaround becomes the bottleneck if the queue is too manual [operations_bottleneck]


## Tech Open Questions

- What exact fields are required for merchant submission review?
- What evidence is needed to mark a merchant verified?
- What are the allowed redemption proof methods at the point of use?


### Growth Summary

The main launch challenge is not consumer acquisition; it is whether one neighborhood can be made dense, current, and trusted enough to beat generic search defaults. The recommended direction is a founder-led, merchant-first concierge pilot in one neighborhood with one category, one offer flow, and manual curation until merchant renewal and repeat use are proven.

## Growth Structural Decisions

- Define the **minimum verified merchant count** needed before consumer launch, plus a freshness threshold for active offers. [market_motion]
- Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]


## Growth Recommendations

- Define the **minimum verified merchant count** needed before consumer launch, plus a freshness threshold for active offers. [market_motion]
- Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]


## Growth Risks

- Merchant density is too thin, making the app feel empty. [market_motion]
- The app does not beat Google Maps on trust or convenience. [demand_validation]
- Offers are not compelling enough to change behavior. [behavior_change]


## Growth Open Questions

- How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]


## Product Arbitration

## Source

heuristic_fallback


## Retained

_Aucun élément retenu._


## Deferred

- Tech: Add one explicit moderation workflow that blocks all submissions until reviewed and approved by ops [moderation_workflow]


## Rejected

- Tech: Require reason codes and audit logging for every admin decision [audit_log]
- Growth: Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Growth: Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]


## Open Points

- Tech: Define the canonical redemption state machine with dispute and void paths [state_machine]
- Tech: Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Tech: Specify a support resolution screen or workflow for redemption disputes [support_workflow]
- Growth: Define the **minimum verified merchant count** needed before consumer launch, plus a freshness threshold for active offers. [market_motion]
- Growth: Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Growth: Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Tech: What exact fields are required for merchant submission review?
- Tech: What evidence is needed to mark a merchant verified?
- Tech: What are the allowed redemption proof methods at the point of use?
- Growth: How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- Growth: What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- Growth: What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]
- Tech recommendation needing arbitration: Define the canonical redemption state machine with dispute and void paths [state_machine]
- Tech recommendation needing arbitration: Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Tech recommendation needing arbitration: Require reason codes and audit logging for every admin decision [audit_log]
- Tech recommendation needing arbitration: Specify a support resolution screen or workflow for redemption disputes [support_workflow]
- Growth recommendation needing arbitration: Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Growth recommendation needing arbitration: Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Growth recommendation needing arbitration: Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Growth recommendation needing arbitration: Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]
- Tech open question: What exact fields are required for merchant submission review?
- Tech open question: What evidence is needed to mark a merchant verified?
- Tech open question: What are the allowed redemption proof methods at the point of use?
- Growth open question: How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- Growth open question: What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- Growth open question: What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to buy local still default to large platforms because local discovery is fragmented, low-trust, and time-consuming. Independent businesses lose customers because they are hard to find, hard to compare, and have weak retention tools.

The product should prove one narrow value loop: help a nearby consumer discover a relevant independent business they would otherwise miss, and give that business a simple reason to attract repeat visits.

## Initial Wedge
Start with one city, one dense neighborhood, and one high-frequency category: independent coffee shops and cafes.

The wedge is:
- nearby discovery
- a small set of verified offers
- a simple loyalty reward
- lightweight personalization based on location and stated preferences

This is narrow enough to build supply density, test repeat usage, and avoid competing head-on with broad platforms.

## First Target User
Primary user:
- Urban young professionals who live or work in the first launch neighborhood

Secondary user:
- Independent coffee shop/cafe owners in that same neighborhood

Why this segment:
- frequent purchase behavior
- high local intent
- easy to test repeat visits
- merchants can understand the value quickly
- lower operational complexity than restaurants, events, or broad local commerce

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- neighborhood newsletters
- merchant punch cards or paper loyalty programs

Switching trigger:
- the user wants a better local recommendation than generic search results
- the user wants a nearby deal or loyalty reward without hunting across multiple apps
- the user wants a curated set of independent businesses in one neighborhood, not the entire city

LocalLoop must be better at one thing: trusted local discovery with a repeat-visit incentive. If it becomes just another directory, users and merchants will not switch.

## Core MVP Workflow
1. User opens the app and shares location plus a few preference signals.
2. App shows a small ranked list of nearby independent coffee shops/cafes.
3. Each listing includes basic merchant details, one offer, and a loyalty action.
4. User taps to view the profile, gets directions, and redeems the offer or loyalty reward.
5. Merchant sees redemption activity and can repeat the same offer through a simple merchant admin flow.

The core proof is whether the app can drive a first visit and a second visit.

## In Scope
- Neighborhood-level discovery for one category: independent coffee shops/cafes
- Location-based ranking and simple personalization
- Merchant profile pages
- One active promotion per merchant
- Basic loyalty rewards
- Basic merchant onboarding and offer management
- Redemption tracking
- Minimal user feedback signal, such as like/dislike or save
- Basic moderation/verification of merchant listings before launch

## Out of Scope
- Multiple cities
- Broad category coverage beyond coffee/cafes
- Full event discovery
- Social feed or following graph
- User-generated reviews at launch
- Complex recommendation engine
- In-app payments or checkout
- Delivery, reservations, or ordering
- Deep merchant CRM, email marketing, or campaign automation
- Open marketplace for any business type
- Aggressive consumer growth features before supply density exists

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based nearby discovery
- Merchant profile pages
- Offer display and redemption tracking
- Simple loyalty reward mechanic
- Basic preference capture
- Basic merchant admin for profile and offer updates
- Verification of listed merchants

### Manual Or Operational During Pilot
- Merchant recruitment in the launch neighborhood
- Merchant verification and setup support
- Curation of initial offers
- Quality control on listings and images
- Customer support for redemption issues
- Neighborhood-level supply balancing
- Hand-review of suspicious or low-quality submissions

### Deferred Until After Proof
- Reviews
- Events feed
- Multi-category expansion
- Multi-city expansion
- Advanced personalization
- Push notification automation
- Merchant analytics dashboards
- In-app payments
- Social features
- Open self-serve merchant onboarding at scale

## Business Model Hypothesis
Primary hypothesis:
- merchants pay a simple monthly fee for inclusion plus basic promotional placement
- or merchants pay for a premium placement / featured offer tier once redemption value is proven

Secondary hypothesis:
- consumer monetization is weaker early and should not be the primary model
- loyalty economics may support a small transaction or subscription fee later, but not in MVP

The first goal is to prove merchants will pay for measurable foot traffic, not to maximize monetization.

## Critical Assumptions
- Consumers will use a neighborhood-specific app instead of general search for local discovery
- A curated set of independent coffee shops is enough to create repeat usage
- Merchants will participate if setup is simple and value is visible
- Offers and loyalty rewards can drive measurable repeat visits
- Supply density in one neighborhood is sufficient to make the app feel useful
- Recommendation quality can be acceptable with simple rules and lightweight personalization

## How To Test Quickly
- Recruit 10 to 20 coffee shops in one neighborhood
- Launch to a small test group of nearby users
- Manually curate offers and merchant profiles
- Track:
  - profile views
  - offer redemptions
  - repeat visits
  - merchant willingness to renew
- Compare performance against paper punch cards, Google Maps, and Instagram-driven discovery
- Interview both users and merchants after the first 2 weeks

## Acceptance Criteria
- Users can see relevant independent coffee shops within a defined neighborhood
- Each merchant profile loads with accurate location, hours, and one offer
- At least 70% of listed merchants are verified and current
- A user can redeem an offer or loyalty reward in under 3 taps after opening a listing
- The system records redemptions reliably
- Merchant can update one offer without product team intervention in the pilot flow
- At least a meaningful subset of users return for a second local discovery session within the test period
- At least a meaningful subset of merchants say they would continue after the pilot

## Risks And Failure Modes
- Insufficient merchant density makes the product feel empty
- Recommendations are too generic and users fall back to Google Maps
- Offers are not compelling enough to change behavior
- Merchants do not see measurable value and churn quickly
- Loyalty mechanics are too weak to drive repeat use
- Manual pilot operations mask a product that will not scale
- Expanding categories too early dilutes quality and supply density

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Need proof that one neighborhood can sustain enough merchant density and user demand to make the app useful [market_density]
- Need evidence that simple offers plus loyalty can change behavior versus existing tools [behavior_change]
- Need validation that merchants will pay or renew after seeing redemption value [merchant_willingness]

Required Improvements:
- Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers [concierge_pilot]
- Measure first-visit and repeat-visit behavior before expanding scope [repeat_usage]
- Validate merchant willingness to continue through direct renewal conversations [retention_validation]

## Recommendation
Proceed with a narrow concierge pilot, not a full product build.

Build only the neighborhood coffee-shop discovery loop, with offers and loyalty as the proof mechanism. Defer reviews, events, broader categories, and multi-city expansion until the product shows repeat usage and merchant willingness to pay. If the pilot does not produce clear repeat behavior and merchant retention, stop or reframe before scaling.

## Retained Decisions

_Aucune décision retenue._

## Deferred Decisions

- Tech: Add one explicit moderation workflow that blocks all submissions until reviewed and approved by ops [moderation_workflow]

## Rejected Recommendations

- Tech: Require reason codes and audit logging for every admin decision [audit_log]
- Growth: Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Growth: Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]

## Unresolved Tensions

- Tech recommendation needing arbitration: Define the canonical redemption state machine with dispute and void paths [state_machine]
- Tech recommendation needing arbitration: Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Tech recommendation needing arbitration: Require reason codes and audit logging for every admin decision [audit_log]
- Tech recommendation needing arbitration: Specify a support resolution screen or workflow for redemption disputes [support_workflow]
- Growth recommendation needing arbitration: Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Growth recommendation needing arbitration: Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Growth recommendation needing arbitration: Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Growth recommendation needing arbitration: Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]
- Tech open question: What exact fields are required for merchant submission review?
- Tech open question: What evidence is needed to mark a merchant verified?
- Tech open question: What are the allowed redemption proof methods at the point of use?
- Growth open question: How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- Growth open question: What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- Growth open question: What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]

## Applied Changes

_Aucun changement appliqué._

## Remaining Open Points

- Tech: Define the canonical redemption state machine with dispute and void paths [state_machine]
- Tech: Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Tech: Specify a support resolution screen or workflow for redemption disputes [support_workflow]
- Growth: Define the **minimum verified merchant count** needed before consumer launch, plus a freshness threshold for active offers. [market_motion]
- Growth: Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Growth: Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Tech: What exact fields are required for merchant submission review?
- Tech: What evidence is needed to mark a merchant verified?
- Tech: What are the allowed redemption proof methods at the point of use?
- Growth: How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- Growth: What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- Growth: What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]
- Tech recommendation needing arbitration: Define the canonical redemption state machine with dispute and void paths [state_machine]
- Tech recommendation needing arbitration: Clarify who can perform verify, suspend, reactivate, and ranking override actions [rbac]
- Tech recommendation needing arbitration: Require reason codes and audit logging for every admin decision [audit_log]
- Tech recommendation needing arbitration: Specify a support resolution screen or workflow for redemption disputes [support_workflow]
- Growth recommendation needing arbitration: Make **founder-led merchant recruitment** the explicit primary acquisition motion in the PRD. [market_motion]
- Growth recommendation needing arbitration: Specify the **smallest credible launch audience** as nearby urban young professionals within the launch neighborhood, not broad “urban residents.” [market_motion]
- Growth recommendation needing arbitration: Clarify the **one canonical redemption method** in a user-facing way so staff and users do not interpret it differently. [market_motion]
- Growth recommendation needing arbitration: Add a **merchant renewal checkpoint** as a required launch criterion, tied to observed redemptions and not just sign-up. [metrics_validation]
- Tech open question: What exact fields are required for merchant submission review?
- Tech open question: What evidence is needed to mark a merchant verified?
- Tech open question: What are the allowed redemption proof methods at the point of use?
- Growth open question: How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- Growth open question: What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- Growth open question: What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]

## Risks

- The neighborhood may not reach enough merchant density to make discovery feel materially better than Google Maps. [market_density]
- Redemption fraud or duplicate claims may undermine trust in rewards. [fraud]
- Manual curation may hide a product that is too weak to operate at scale. [concierge_pilot]
- Merchant density may remain too thin to create a useful consumer experience.
- Offers may not be compelling enough to pull users away from Google Maps or paper loyalty.
- Manual curation may hide weak product-market fit during the pilot.
- Manual curation may mask weak product quality until the pilot scales. [quality_assurance]
- Without strict review gates, low-quality or unsafe merchant submissions can reach users. [privacy_trust]
- Redemption disputes may create trust issues if the canonical flow is not unambiguous. [quality_assurance]
- The neighborhood may not have enough merchant density to feel useful.
- Merchants may not see enough value to keep participating after the pilot.
- Users may still prefer Google Maps or Yelp for discovery.
- Merchant or offer quality slips if moderation is not consistently applied [quality_assurance]
- Redemption disputes damage trust if state transitions are ambiguous [state_machine]
- Ops turnaround becomes the bottleneck if the queue is too manual [operations_bottleneck]
- Merchant density is too thin, making the app feel empty. [market_motion]
- The app does not beat Google Maps on trust or convenience. [demand_validation]
- Offers are not compelling enough to change behavior. [behavior_change]

## Open Questions

- What exact redemption mechanism will merchants and staff be asked to use in-store? [redemption_flow]
- Who is responsible for day-to-day verification of merchant identity, hours, and offer validity? [verification]
- What minimum merchant count is required before launch in the target neighborhood? [market_density]
- How many verified merchants are required before the neighborhood feels “complete” enough?
- What specific offer types are most likely to produce first and second visits?
- What is the simplest measurable definition of redemption in the pilot?
- What exact submission fields are required before a merchant can enter review?
- What is the single canonical redemption method: code, staff confirmation, QR, or in-app tap?
- Who is allowed to approve, suspend, or override records in the admin workflow?
- What is the exact minimum merchant count for launch?
- What percentage of merchants must keep their offers current each week?
- What redemption method is simplest for staff and least confusing for users?
- What exact fields are required for merchant submission review?
- What evidence is needed to mark a merchant verified?
- What are the allowed redemption proof methods at the point of use?
- How many verified merchants are required before the neighborhood feels meaningfully usable? [market_motion]
- What offer format is simple enough for merchants but strong enough to drive first redemptions? [behavior_change]
- What exact evidence will count as merchant willingness to continue after the pilot? [metrics_validation]

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
Consumers who want local independent businesses still default to Google Maps, Yelp, Instagram, and large horizontal platforms because local discovery is fragmented and inconsistent. Independent businesses lack a simple, affordable way to get discovered and to bring nearby customers back.

The MVP should prove one narrow loop: a nearby consumer discovers a vetted local business, redeems a simple offer, and the merchant sees enough value to continue.

## Initial Wedge
Launch in one city, one walkable neighborhood, and one high-frequency category: independent coffee shops and cafes.

The wedge is:
- nearby discovery
- verified merchants only
- one neighborhood
- one category
- one canonical offer/redemption flow
- a simple loyalty reward
- founder-led merchant recruitment
- manual curation during pilot
- admin-controlled publishing and moderation

This is the narrowest credible wedge to test supply density, repeat usage, and merchant willingness to continue.

## First Target User
Primary user:
- Nearby urban young professionals who live or work in the launch neighborhood

Secondary user:
- Independent coffee shop and cafe owners in the same neighborhood

Why this segment:
- frequent purchase behavior
- high local intent
- easy to test repeat visits
- merchants can judge foot traffic value quickly
- lower operational complexity than restaurants, events, or broad local commerce

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- neighborhood newsletters
- paper punch cards and in-store loyalty

Switching trigger:
- the user wants a better local recommendation than generic search results
- the user wants a nearby offer without searching across multiple apps
- the user wants a curated set of independent businesses in one neighborhood, not the whole city

LocalLoop must be better at one thing: trusted neighborhood discovery with a repeat-visit incentive. If it becomes a generic directory, users and merchants will not switch.

## Core MVP Workflow
1. Merchant is recruited by ops and submitted for review.
2. Ops approves or rejects the merchant profile and offer before publication.
3. User opens the app, shares location, and optionally sets a few preference signals.
4. App shows a small ranked list of verified nearby independent coffee shops/cafes.
5. Each listing includes merchant details, one active offer, and one loyalty action.
6. User opens a merchant profile, gets directions, and redeems the offer through one canonical method.
7. Redemption is recorded in a defined status flow and can be disputed or voided by support.
8. Merchant can request profile or offer updates, which go through admin review before publishing.
9. Ops can verify, re-verify, suspend, reactivate, or override ranking with reason codes and audit logging.

The core proof is whether the app can drive first visits and repeat visits in a dense neighborhood.

## In Scope
- Neighborhood-level discovery for one category: independent coffee shops/cafes
- One city, one launch neighborhood
- Nearby urban young professionals as the launch audience
- Verified merchant listings only
- Location-based ranking and basic preference capture
- Merchant profile pages
- One active offer per merchant
- One canonical redemption method
- Basic loyalty reward mechanic
- Merchant onboarding and offer updates through admin review
- Redemption tracking with dispute/void handling
- Merchant verification, re-verification, suspension, and reactivation states
- Ops-approved publishing gate for all merchant content
- Manual ranking overrides during the pilot
- Minimal user feedback signal, such as save or like
- Basic moderation of listings before launch
- Audit logging for merchant edits and admin actions
- Founder-led merchant recruitment for the pilot
- Merchant renewal checkpoint based on observed redemption value

## Out of Scope
- Multiple cities
- Broad category coverage beyond coffee/cafes
- Events feed
- Social feed or following graph
- User-generated reviews at launch
- Advanced personalization
- Complex recommendation engine
- In-app payments or checkout
- Delivery, reservations, or ordering
- Deep merchant CRM, email marketing, or campaign automation
- Open self-serve marketplace for any business type
- Automated consumer growth features before supply density exists
- Full-scale merchant analytics dashboard
- Public self-serve publishing without review
- Broad launch audience beyond nearby urban young professionals

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based nearby discovery
- Merchant profile pages
- Verified merchant status
- Merchant verification and re-verification states
- Required admin review gate before publishing
- One canonical redemption flow
- Offer display and redemption tracking
- Simple loyalty reward mechanic
- Basic preference capture
- Basic merchant admin for profile and offer update requests
- Merchant suspension, reactivation, and override states
- Reason-coded admin actions with audit logging
- Basic ops tools for ranking override and verification review
- Redemption dispute and void handling
- Moderation workflow that blocks all submissions until approved
- Canonical redemption state machine

### Manual Or Operational During Pilot
- Founder-led merchant recruitment in the launch neighborhood
- Merchant onboarding setup
- Merchant verification and re-verification review
- Curation of initial offers
- Quality control on listings and images
- Customer support for redemption issues
- Neighborhood supply balancing
- Hand-review of suspicious submissions
- Merchant renewal conversations

### Deferred Until After Proof
- Reviews
- Events feed
- Multi-category expansion
- Multi-city expansion
- Advanced personalization
- Push notification automation
- Merchant analytics dashboards
- In-app payments
- Social features
- Open self-serve merchant onboarding at scale
- Consumer growth automation

## Business Model Hypothesis
Primary hypothesis:
- Merchants pay a simple monthly fee for inclusion and local promotion once redemption value is proven
- or merchants pay for a featured placement tier after foot traffic value is demonstrated

Secondary hypothesis:
- consumer monetization is not the MVP focus
- loyalty economics may support a later subscription or transaction fee, but not now

The first goal is to prove merchants will pay for measurable foot traffic and repeat visits.

## Critical Assumptions
- Consumers will use a neighborhood-specific app instead of general search for local discovery
- A curated set of coffee shops is enough to create repeat usage
- Merchants will participate if setup is simple and value is visible
- A single redemption method can be understood by staff and users without confusion
- Offers and loyalty rewards can drive measurable repeat visits
- Supply density in one neighborhood is sufficient to make the app feel useful
- Simple ranking plus manual ops can produce acceptable discovery quality in the pilot
- One neighborhood can sustain enough verified merchants to feel worthwhile
- Merchant data can be kept trustworthy through review and audit controls
- Merchants will renew after seeing real redemption activity

## How To Test Quickly
- Recruit 10 to 20 verified coffee shops in one walkable neighborhood
- Launch to a small group of nearby urban young professionals
- Use manual merchant onboarding and curated offers
- Use one canonical redemption method for all pilot merchants
- Track:
  - profile views
  - offer redemptions
  - repeat visits
  - merchant renewal interest
- Interview users and merchants after 2 weeks
- Test willingness to continue with a renewal conversation after pilot activity is visible
- Use a simple decision rule:
  - Proceed if at least 30% of launched merchants record redemptions and at least 20% of active users return for a second session within 14 days
  - Revise if one metric clears and the other misses modestly
  - Reject or reframe if both miss materially or merchants do not express renewal intent

## Acceptance Criteria
- Users can see relevant verified coffee shops within the defined neighborhood
- Each merchant profile loads with accurate location, hours, and one active offer
- No merchant or offer is visible without admin approval
- The neighborhood includes enough verified merchants to feel meaningfully usable
- A user can redeem an offer or loyalty reward through one clear flow
- The system records redemptions reliably
- Failed redemptions can be voided or disputed by support
- Merchant can request one offer update without product team intervention during the pilot
- Ops can verify, re-verify, suspend, reactivate, and override merchants
- Ops actions are reason-coded and auditable
- A meaningful subset of users return for a second discovery session in the test period
- A meaningful subset of merchants say they would continue after the pilot
- Pilot metrics support the proceed/revise/reject decision rule above

## Risks And Failure Modes
- Insufficient merchant density makes the product feel empty
- Recommendations are too generic and users fall back to Google Maps
- Offers are not compelling enough to change behavior
- Merchants do not see measurable value and churn quickly
- Loyalty mechanics are too weak to drive repeat use
- Manual pilot operations hide a product that will not scale
- Expanding categories too early dilutes quality and supply density
- Redemption disputes create trust issues if the flow is unclear
- Admin review may slow the launch if operational turnaround is too slow
- The launch audience is too broad to create a repeatable wedge

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Need proof that one neighborhood can sustain enough verified merchant density to feel useful [market_motion]
- Need evidence that simple offers plus loyalty can change behavior versus existing tools [behavior_change]
- Need validation that merchants will renew after seeing redemption value [metrics_validation]
- Need enough pilot data to apply the proceed/revise/reject decision rule [metrics_validation]

Required Improvements:
- Run a concierge pilot in one neighborhood with manual merchant onboarding and curated offers [concierge_pilot]
- Define and use one canonical redemption method across the pilot [redemption_flow]
- Measure first-visit and repeat-visit behavior before expanding scope [repeat_usage]
- Validate merchant willingness to continue through direct renewal conversations [merchant_willingness]
- Collect pilot metrics against the explicit success threshold before launch expansion [metrics_validation]

## Recommendation
Proceed with a narrow concierge pilot, not a full product build.

Build only the neighborhood coffee-shop discovery loop with verified merchants, one redemption flow, admin review gates, and loyalty as the proof mechanism. Keep reviews, events, broader categories, multi-city expansion, and consumer growth automation out of scope until the pilot shows repeat usage, merchant renewal intent, and minimum success metrics. If the pilot does not meet the decision rule, revise or stop before scaling.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

_Aucune décision._

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
