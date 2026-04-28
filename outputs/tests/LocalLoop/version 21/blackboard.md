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

### demand_validation
- [demand_validation] No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete

### scope
- [scope] No proof that the curated, rules-based recommendation experience is better than existing alternatives

### market_motion
- [market_motion] No proof that merchants will renew after a pilot period

## Product Required Improvements

### quality_assurance
- [quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks
- [quality_assurance] Confirm a single redemption/visit verification method before launch

### market_motion
- [market_motion] Validate merchant renewal intent with a small pilot cohort

### demand_validation
- [demand_validation] Test the curated feed against a simple baseline directory

### onboarding
- [onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates

## Tech Status

LIMITED


## Tech Blocking Gaps

### quality_assurance
- [quality_assurance] No single, specified redemption verification mechanism with enforced token lifecycle
- [quality_assurance] No explicit freshness-control policy with stale visibility rules and required check cadence
- [quality_assurance] No operator-only approval and immutable audit workflow defined for supply changes

## Tech Required Improvements

### quality_assurance
- [quality_assurance] Define one redemption flow and enforce single-use or time-boxed state transitions
- [quality_assurance] Specify freshness TTL, check cadence, and auto-hide logic for stale listings
- [quality_assurance] Add operator approval queue plus append-only audit logging for every merchant and offer change

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] The launch audience is still too broad to support a focused pilot motion.
- [market_motion] The first market side to secure is not operationalized with a minimum merchant cohort target.
- [market_motion] The first acquisition motion is not tightly specified enough to test reliably.
- [market_motion] Merchant renewal intent is not yet tied to a concrete pilot bar.

## Growth Required Improvements

### market_motion
- [market_motion] Define the narrowest launch audience as people who live or work in the single launch neighborhood.
- [market_motion] Lock the first acquisition motion to founder-led merchant seeding plus local invite distribution.
- [market_motion] Add a specific merchant renewal checkpoint as the primary proof of market value.

### untagged
- Set a minimum merchant cohort and participation threshold before public launch.

## Global Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete

### scope
- [scope] No proof that the curated, rules-based recommendation experience is better than existing alternatives

### market_motion
- [market_motion] No proof that merchants will renew after a pilot period
- [market_motion] The launch audience is still too broad to support a focused pilot motion.
- [market_motion] The first market side to secure is not operationalized with a minimum merchant cohort target.
- [market_motion] The first acquisition motion is not tightly specified enough to test reliably.
- [market_motion] Merchant renewal intent is not yet tied to a concrete pilot bar.

### quality_assurance
- [quality_assurance] No single, specified redemption verification mechanism with enforced token lifecycle
- [quality_assurance] No explicit freshness-control policy with stale visibility rules and required check cadence
- [quality_assurance] No operator-only approval and immutable audit workflow defined for supply changes

## Global Required Improvements

### quality_assurance
- [quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks
- [quality_assurance] Confirm a single redemption/visit verification method before launch
- [quality_assurance] Define one redemption flow and enforce single-use or time-boxed state transitions
- [quality_assurance] Specify freshness TTL, check cadence, and auto-hide logic for stale listings
- [quality_assurance] Add operator approval queue plus append-only audit logging for every merchant and offer change

### market_motion
- [market_motion] Validate merchant renewal intent with a small pilot cohort
- [market_motion] Define the narrowest launch audience as people who live or work in the single launch neighborhood.
- [market_motion] Lock the first acquisition motion to founder-led merchant seeding plus local invite distribution.
- [market_motion] Add a specific merchant renewal checkpoint as the primary proof of market value.

### demand_validation
- [demand_validation] Test the curated feed against a simple baseline directory

### onboarding
- [onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates

### untagged
- Set a minimum merchant cohort and participation threshold before public launch.

## Known Tags

- quality_assurance
- scope
- untagged
- market_motion
- onboarding
- demand_validation


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

[quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks Confirm a simple redemption/visit verification method before launch Redemption mechanics are not specified tightly enough to ensure trust and auditability Define a concierge onboarding and verification workflow before any software expansion No proof that the recommendation experience beats existing alternatives


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

- growth


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] No proof that merchants will renew after a pilot period Validate merchant renewal intent with a small pilot cohort Lock the pilot to one redemption mechanism with audit logs and dispute handling Run a concierge pilot with a fixed launch neighborhood and manually curated supply Secure a small merchant cohort willing to renew after the pilot period


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Product Task

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] No evidence merchants will continue beyond initial onboarding


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


## Contributors

- growth


### Loop 2

#### Tech Task

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks Confirm a single redemption/visit verification method before launch No defined mandatory freshness-control workflow for merchant listings and offers. No single, auditable redemption mechanism specified for the MVP. No explicit internal approval and audit trail requirement for supply changes. Define a concierge verification workflow with required fields, cadence, and stale-visibility rules. Lock the MVP to one redemption method with single-use or time-boxed verification. Add an operator-only approval queue plus immutable audit logging for all supply edits.


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] No proof that merchants will renew after a pilot period Validate merchant renewal intent with a small pilot cohort The launch audience is still too broad to support a focused pilot motion The first market side to secure is implied, but not operationalized with a concrete merchant cohort target The first acquisition motion is not yet specified tightly enough to be testable Set a minimum merchant cohort and participation bar for pilot launch readiness Define the first acquisition motion as founder-led merchant seeding plus local invite distribution


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


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

### demand_validation
- [demand_validation] No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete
- [demand_validation] No validated supply density in a single launch neighborhood

### scope
- [scope] No proof that the curated, rules-based recommendation experience is better than existing alternatives
- [scope] Recommendation logic is still framed too broadly for a realistic MVP build

### market_motion
- [market_motion] No proof that merchants will renew after a pilot period

### untagged
- Merchant supply density and freshness are not yet proven in a controlled launch area

### quality_assurance
- [quality_assurance] Redemption mechanics are not specified tightly enough to ensure trust and auditability
- [quality_assurance] No proof that the recommendation experience beats existing alternatives

### onboarding
- [onboarding] No evidence merchants will continue beyond initial onboarding

## Global Required Improvements

### quality_assurance
- [quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks
- [quality_assurance] Confirm a simple redemption/visit verification method before launch
- [quality_assurance] Define a concierge onboarding and verification workflow before any software expansion

### market_motion
- [market_motion] Validate merchant renewal intent with a small pilot cohort
- [market_motion] Lock the pilot to one redemption mechanism with audit logs and dispute handling
- [market_motion] Run a concierge pilot with a fixed launch neighborhood and manually curated supply
- [market_motion] Secure a small merchant cohort willing to renew after the pilot period

### demand_validation
- [demand_validation] Test the curated feed against a simple baseline directory

### scope
- [scope] Replace broad personalization with deterministic ranking rules for the first release

### untagged
- Test the app against a simple directory or map-like baseline for first-session usefulness

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks Confirm a simple redemption/visit verification method before launch Redemption mechanics are not specified tightly enough to ensure trust and auditability Define a concierge onboarding and verification workflow before any software expansion No proof that the recommendation experience beats existing alternatives


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] No proof that merchants will renew after a pilot period Validate merchant renewal intent with a small pilot cohort Lock the pilot to one redemption mechanism with audit logs and dispute handling Run a concierge pilot with a fixed launch neighborhood and manually curated supply Secure a small merchant cohort willing to renew after the pilot period


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] No evidence merchants will continue beyond initial onboarding


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


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
- [demand_validation] No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete

### scope
- [scope] No proof that the curated, rules-based recommendation experience is better than existing alternatives

### market_motion
- [market_motion] No proof that merchants will renew after a pilot period
- [market_motion] The launch audience is still too broad to support a focused pilot motion
- [market_motion] The first market side to secure is implied, but not operationalized with a concrete merchant cohort target
- [market_motion] The first acquisition motion is not yet specified tightly enough to be testable

### quality_assurance
- [quality_assurance] No defined mandatory freshness-control workflow for merchant listings and offers.
- [quality_assurance] No single, auditable redemption mechanism specified for the MVP.
- [quality_assurance] No explicit internal approval and audit trail requirement for supply changes.

## Global Required Improvements

### quality_assurance
- [quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks
- [quality_assurance] Confirm a single redemption/visit verification method before launch
- [quality_assurance] Define a concierge verification workflow with required fields, cadence, and stale-visibility rules.
- [quality_assurance] Lock the MVP to one redemption method with single-use or time-boxed verification.
- [quality_assurance] Add an operator-only approval queue plus immutable audit logging for all supply edits.

### market_motion
- [market_motion] Validate merchant renewal intent with a small pilot cohort
- [market_motion] Set a minimum merchant cohort and participation bar for pilot launch readiness
- [market_motion] Define the first acquisition motion as founder-led merchant seeding plus local invite distribution

### demand_validation
- [demand_validation] Test the curated feed against a simple baseline directory

### onboarding
- [onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates

### scope
- [scope] Lock the launch to one neighborhood and one user segment: residents/workers who already make nearby mobile decisions

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks Confirm a simple redemption/visit verification method before launch Redemption mechanics are not specified tightly enough to ensure trust and auditability Define a concierge onboarding and verification workflow before any software expansion No proof that the recommendation experience beats existing alternatives


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] No proof that merchants will renew after a pilot period Validate merchant renewal intent with a small pilot cohort Lock the pilot to one redemption mechanism with audit logs and dispute handling Run a concierge pilot with a fixed launch neighborhood and manually curated supply Secure a small merchant cohort willing to renew after the pilot period


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] No evidence merchants will continue beyond initial onboarding


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


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
- [demand_validation] No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete

### scope
- [scope] No proof that the curated, rules-based recommendation experience is better than existing alternatives

### market_motion
- [market_motion] No proof that merchants will renew after a pilot period
- [market_motion] The launch audience is still too broad to support a focused pilot motion
- [market_motion] The first market side to secure is implied, but not operationalized with a concrete merchant cohort target
- [market_motion] The first acquisition motion is not yet specified tightly enough to be testable

### quality_assurance
- [quality_assurance] No defined mandatory freshness-control workflow for merchant listings and offers.
- [quality_assurance] No single, auditable redemption mechanism specified for the MVP.
- [quality_assurance] No explicit internal approval and audit trail requirement for supply changes.

## Global Required Improvements

### quality_assurance
- [quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks
- [quality_assurance] Confirm a single redemption/visit verification method before launch
- [quality_assurance] Define a concierge verification workflow with required fields, cadence, and stale-visibility rules.
- [quality_assurance] Lock the MVP to one redemption method with single-use or time-boxed verification.
- [quality_assurance] Add an operator-only approval queue plus immutable audit logging for all supply edits.

### market_motion
- [market_motion] Validate merchant renewal intent with a small pilot cohort
- [market_motion] Set a minimum merchant cohort and participation bar for pilot launch readiness
- [market_motion] Define the first acquisition motion as founder-led merchant seeding plus local invite distribution

### demand_validation
- [demand_validation] Test the curated feed against a simple baseline directory

### onboarding
- [onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates

### scope
- [scope] Lock the launch to one neighborhood and one user segment: residents/workers who already make nearby mobile decisions

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks Confirm a single redemption/visit verification method before launch No defined mandatory freshness-control workflow for merchant listings and offers. No single, auditable redemption mechanism specified for the MVP. No explicit internal approval and audit trail requirement for supply changes. Define a concierge verification workflow with required fields, cadence, and stale-visibility rules. Lock the MVP to one redemption method with single-use or time-boxed verification. Add an operator-only approval queue plus immutable audit logging for all supply edits.


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] No proof that merchants will renew after a pilot period Validate merchant renewal intent with a small pilot cohort The launch audience is still too broad to support a focused pilot motion The first market side to secure is implied, but not operationalized with a concrete merchant cohort target The first acquisition motion is not yet specified tightly enough to be testable Set a minimum merchant cohort and participation bar for pilot launch readiness Define the first acquisition motion as founder-led merchant seeding plus local invite distribution


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


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
- [demand_validation] No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete

### scope
- [scope] No proof that the curated, rules-based recommendation experience is better than existing alternatives

### market_motion
- [market_motion] No proof that merchants will renew after a pilot period
- [market_motion] The launch audience is still too broad to support a focused pilot motion.
- [market_motion] The first market side to secure is not operationalized with a minimum merchant cohort target.
- [market_motion] The first acquisition motion is not tightly specified enough to test reliably.
- [market_motion] Merchant renewal intent is not yet tied to a concrete pilot bar.

### quality_assurance
- [quality_assurance] No single, specified redemption verification mechanism with enforced token lifecycle
- [quality_assurance] No explicit freshness-control policy with stale visibility rules and required check cadence
- [quality_assurance] No operator-only approval and immutable audit workflow defined for supply changes

## Global Required Improvements

### quality_assurance
- [quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks
- [quality_assurance] Confirm a single redemption/visit verification method before launch
- [quality_assurance] Define one redemption flow and enforce single-use or time-boxed state transitions
- [quality_assurance] Specify freshness TTL, check cadence, and auto-hide logic for stale listings
- [quality_assurance] Add operator approval queue plus append-only audit logging for every merchant and offer change

### market_motion
- [market_motion] Validate merchant renewal intent with a small pilot cohort
- [market_motion] Define the narrowest launch audience as people who live or work in the single launch neighborhood.
- [market_motion] Lock the first acquisition motion to founder-led merchant seeding plus local invite distribution.
- [market_motion] Add a specific merchant renewal checkpoint as the primary proof of market value.

### demand_validation
- [demand_validation] Test the curated feed against a simple baseline directory

### onboarding
- [onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates

### untagged
- Set a minimum merchant cohort and participation threshold before public launch.

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] Run a concierge pilot in one neighborhood with manual curation and freshness checks Confirm a single redemption/visit verification method before launch No defined mandatory freshness-control workflow for merchant listings and offers. No single, auditable redemption mechanism specified for the MVP. No explicit internal approval and audit trail requirement for supply changes. Define a concierge verification workflow with required fields, cadence, and stale-visibility rules. Lock the MVP to one redemption method with single-use or time-boxed verification. Add an operator-only approval queue plus immutable audit logging for all supply edits.


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] No proof that merchants will renew after a pilot period Validate merchant renewal intent with a small pilot cohort The launch audience is still too broad to support a focused pilot motion The first market side to secure is implied, but not operationalized with a concrete merchant cohort target The first acquisition motion is not yet specified tightly enough to be testable Set a minimum merchant cohort and participation bar for pilot launch readiness Define the first acquisition motion as founder-led merchant seeding plus local invite distribution


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] Keep merchant onboarding to a minimal founder-led flow with strict approval gates


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- [tech] Define exactly **one redemption method** and specify its token lifecycle and failure handling

## Growth Structural Decisions

### growth
- [growth] Define the **launch neighborhood merchant cohort target** explicitly, including the minimum number of active listings required before launch. [supply_density]
- [growth] Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]

## Product Locking

## Applied

True


## Confirmed In Scope

- One neighborhood launch
- One category cluster
- Live merchant listings with freshness status
- Automatic stale hiding
- One redemption method
- Operator-only approval
- Immutable audit log
- Manual pilot onboarding
- Basic save, directions, and feedback


## Confirmed Deferred

- Reviews and ratings
- Event feed
- Advanced personalization
- Self-serve merchant onboarding
- Merchant analytics dashboard
- Paid placements
- Multi-city rollout
- In-app ordering or payments


## Confirmed Out Of Scope

- Multiple redemption methods
- Broad category expansion
- Social feed mechanics
- User-to-merchant messaging
- Delivery
- General local search competition


## Locking Note

Scope remains intentionally narrow and pilot-led. Any additional capability should wait until the concierge pilot proves density, trust, and merchant renewal.


## Expert Contributions

### Tech Summary

The MVP is only feasible if it is treated as a concierge-controlled supply system with hard freshness rules, one redemption method, and operator approval on every publishable change. Anything more automated or merchant-driven would introduce trust and quality risk before the neighborhood wedge is proven.

## Tech Structural Decisions

- Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Define exactly **one redemption method** and specify its token lifecycle and failure handling


## Tech Recommendations

- Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Add an **operator-only approval queue** for all merchant and offer changes
- Require an **immutable audit log** for publishing, edits, suspension, and redemption events
- Clarify the **minimum required fields** for a listing to become live


## Tech Risks

- Freshness operations may become too manual to sustain even a narrow pilot [onboarding]
- Single redemption flow may still fail in real-world merchant execution [quality_assurance]
- Operator approval latency could make the experience feel stale [quality_assurance]


## Tech Open Questions

- What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- What is the freshness TTL for a listing before it is hidden?
- Who is allowed to approve, edit, and override supply states?


### Growth Summary

The main launch challenge is not building a broad local discovery app; it is proving that one neighborhood can be made dense, current, and trusted enough to create repeat use. The recommended direction is a founder-led concierge pilot with merchant-first seeding in one neighborhood, one category cluster, and a small local resident/worker audience.

## Growth Structural Decisions

- Define the **launch neighborhood merchant cohort target** explicitly, including the minimum number of active listings required before launch. [supply_density]
- Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]


## Growth Recommendations

- Define the **launch neighborhood merchant cohort target** explicitly, including the minimum number of active listings required before launch. [supply_density]
- Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]
- Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]


## Growth Risks

- The merchant cohort is too small or too stale to make the app feel useful. [supply_density]
- The neighborhood audience is too broad, making acquisition unfocused and low-converting. [market_motion]
- Users do not perceive enough improvement over Maps, Yelp, or social platforms. [demand_validation]


## Growth Open Questions

- What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Which single category cluster is strongest for repeat use in the chosen neighborhood?
- What is the primary local user segment: residents, workers, or both?


## Product Arbitration

## Source

heuristic_fallback


## Retained

- Tech: Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Tech: Require an **immutable audit log** for publishing, edits, suspension, and redemption events


## Deferred

_Aucun élément différé._


## Rejected

- Tech: Add an **operator-only approval queue** for all merchant and offer changes
- Growth: Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Growth: Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]


## Open Points

- Tech: Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Tech: Clarify the **minimum required fields** for a listing to become live
- Growth: Define the **launch neighborhood merchant cohort target** explicitly, including the minimum number of active listings required before launch. [supply_density]
- Growth: Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Growth: Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]
- Tech: What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- Tech: What is the freshness TTL for a listing before it is hidden?
- Tech: Who is allowed to approve, edit, and override supply states?
- Growth: What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Growth: Which single category cluster is strongest for repeat use in the chosen neighborhood?
- Growth: What is the primary local user segment: residents, workers, or both?
- Tech recommendation needing arbitration: Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Tech recommendation needing arbitration: Add an **operator-only approval queue** for all merchant and offer changes
- Tech recommendation needing arbitration: Require an **immutable audit log** for publishing, edits, suspension, and redemption events
- Tech recommendation needing arbitration: Clarify the **minimum required fields** for a listing to become live
- Growth recommendation needing arbitration: Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Growth recommendation needing arbitration: Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Growth recommendation needing arbitration: Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]
- Growth recommendation needing arbitration: Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]
- Tech open question: What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- Tech open question: What is the freshness TTL for a listing before it is hidden?
- Tech open question: Who is allowed to approve, edit, and override supply states?
- Growth open question: What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Growth open question: Which single category cluster is strongest for repeat use in the chosen neighborhood?
- Growth open question: What is the primary local user segment: residents, workers, or both?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
Consumers who want to discover local independent businesses face fragmented discovery across maps, social apps, review sites, and word of mouth. Independent businesses, in turn, struggle to get noticed without relying on expensive or complex marketing tools. The product opportunity is to create a focused local discovery loop that helps users find relevant nearby businesses and gives merchants a simple way to attract first visits.

## Initial Wedge
Start with one city and one repeatable use case: personalized discovery of nearby independent coffee shops, cafes, and casual food spots with simple neighborhood offers. This is narrow enough to build supply density, simple enough to trust, and frequent enough to test repeat usage.

## First Target User
Urban young professionals and residents in one launch neighborhood who:
- already use mobile search and maps for local decisions
- want to support independent businesses
- are open to trying new places if recommendations feel relevant and nearby

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps and Apple Maps for nearby search
- Yelp for reviews and ratings
- Instagram/TikTok for local discovery
- merchant websites and social pages for promotions
- deal apps for discounts

Switching trigger:
- the user gets a more relevant, neighborhood-specific recommendation than generic search results
- the app surfaces a better nearby option with a real offer or loyalty incentive
- the experience is faster than searching across multiple apps and easier to trust than random social posts

## Core MVP Workflow
1. User opens the app and shares location.
2. App shows a small set of nearby independent businesses in the launch area.
3. User filters by simple intent such as coffee, lunch, or “open now.”
4. Each listing shows a short profile, distance, hours, and one current offer or reward.
5. User taps through to save, redeem, or get directions.
6. User can optionally rate the recommendation or mark it as useful.
7. Merchant sees basic interest and redemption activity.

## In Scope
- Location-based discovery within one city or neighborhood
- Curated listings for independent businesses only
- Basic personalization using simple preferences and behavior
- Merchant profile pages with hours, category, location, and short description
- One offer type per merchant
- Simple loyalty stamp or visit reward
- Basic save/favorite functionality
- Basic direction handoff to maps
- Minimal feedback signal such as useful / not useful
- Manual merchant onboarding for pilot supply

## Out of Scope
- Full reviews and social commentary
- Event feed
- Broad category coverage across the entire city at launch
- Marketplace-style ad bidding or paid placement
- Complex recommendation engine
- In-app payment or ordering
- Delivery or reservation management
- Multi-city expansion
- Deep merchant analytics dashboard
- Messaging between users and merchants
- Horizontal comparison with big-platform search features

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based nearby discovery
- Merchant profile pages
- Basic personalization rules
- Offer display and redemption marker
- Simple loyalty reward tracking
- Save/favorite and map handoff
- Basic feedback signal

### Manual Or Operational During Pilot
- Merchant sourcing and onboarding
- Offer setup and verification
- Categorization and quality checks
- Local supply curation
- Customer support for merchant issues
- Neighborhood launch coordination

### Deferred Until After Proof
- Reviews and ratings system
- Event discovery feed
- Automated merchant self-serve onboarding
- Advanced recommendation models
- Merchant analytics dashboard
- Paid promotions and sponsored placement
- Cross-city expansion

## Business Model Hypothesis
The likely early model is a merchant subscription or monthly fee for being featured with offers and loyalty tools in a dense local neighborhood, possibly paired with a free trial during the pilot. A later model could add paid premium placement or performance-based promotion, but the MVP should first test whether merchants value customer visits enough to pay.

## Critical Assumptions
- Users will try a new app for local discovery if recommendations are relevant and localized.
- A dense set of participating independent businesses can be assembled in one area.
- Simple offers or loyalty rewards are enough to motivate first visits.
- Merchants will participate without a complex self-serve platform.
- The app can provide enough differentiation versus Google Maps and Yelp through neighborhood specificity and exclusivity.

## How To Test Quickly
- Recruit 20 to 40 independent businesses in one neighborhood manually.
- Launch to a small user group of local residents and young professionals.
- Compare engagement on recommended businesses versus a basic directory view.
- Measure saves, taps to directions, offer redemptions, and repeat opens.
- Interview merchants weekly about perceived value and willingness to continue.
- Test whether one or two offer types outperform generic listings.

## Acceptance Criteria
- At least 20 active independent businesses in one launch area
- At least 60 percent of listed businesses have verified hours, location, and one current offer
- Users can discover, save, and navigate to a business in under 60 seconds
- Offer or loyalty redemption can be tracked reliably
- At least 25 percent of activated users engage with a listing in the first session
- At least 10 percent of activated users return within 30 days
- At least a small pilot cohort of merchants expresses willingness to continue after trial

## Risks And Failure Modes
- Supply density is too weak, making the app feel empty [supply_density]
- Recommendations feel generic and fail to outperform maps or social apps [recommendation_quality]
- Merchants do not see enough value to participate or pay [merchant_value]
- Low-quality or stale offers reduce trust [offer_freshness]
- The app drifts into trying to cover too many local use cases at once [scope_creep]
- Manual curation becomes too expensive to scale [operational_burden]

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No validated supply model for acquiring enough independent businesses in one city [supply_density]
- No evidence that the localized recommendation experience beats existing alternatives [recommendation_quality]
- No proof that merchants will sustain participation after the pilot [merchant_value]

Required Improvements:
- Run a concierge pilot in one neighborhood with manually curated listings and offers [concierge_pilot]
- Validate merchant willingness to join and renew with a small signed cohort [merchant_validation]
- Test recommendation relevance and retention against a simple directory baseline [baseline_test]

## Recommendation
Proceed with a narrow concierge-style pilot in one neighborhood focused on independent coffee shops and casual food spots. Do not broaden into events, reviews, or citywide discovery until the pilot proves that users return and merchants see enough value to stay engaged.

## Retained Decisions

- Tech: Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Tech: Require an **immutable audit log** for publishing, edits, suspension, and redemption events

## Deferred Decisions

_Aucune décision différée._

## Rejected Recommendations

- Tech: Add an **operator-only approval queue** for all merchant and offer changes
- Growth: Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Growth: Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]

## Unresolved Tensions

- Tech recommendation needing arbitration: Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Tech recommendation needing arbitration: Add an **operator-only approval queue** for all merchant and offer changes
- Tech recommendation needing arbitration: Require an **immutable audit log** for publishing, edits, suspension, and redemption events
- Tech recommendation needing arbitration: Clarify the **minimum required fields** for a listing to become live
- Growth recommendation needing arbitration: Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Growth recommendation needing arbitration: Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Growth recommendation needing arbitration: Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]
- Growth recommendation needing arbitration: Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]
- Tech open question: What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- Tech open question: What is the freshness TTL for a listing before it is hidden?
- Tech open question: Who is allowed to approve, edit, and override supply states?
- Growth open question: What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Growth open question: Which single category cluster is strongest for repeat use in the chosen neighborhood?
- Growth open question: What is the primary local user segment: residents, workers, or both?

## Applied Changes

- Tech: Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Tech: Require an **immutable audit log** for publishing, edits, suspension, and redemption events

## Remaining Open Points

- Tech: Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Tech: Clarify the **minimum required fields** for a listing to become live
- Growth: Define the **launch neighborhood merchant cohort target** explicitly, including the minimum number of active listings required before launch. [supply_density]
- Growth: Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Growth: Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]
- Tech: What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- Tech: What is the freshness TTL for a listing before it is hidden?
- Tech: Who is allowed to approve, edit, and override supply states?
- Growth: What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Growth: Which single category cluster is strongest for repeat use in the chosen neighborhood?
- Growth: What is the primary local user segment: residents, workers, or both?
- Tech recommendation needing arbitration: Define exactly **one redemption method** and specify its token lifecycle and failure handling
- Tech recommendation needing arbitration: Add an **operator-only approval queue** for all merchant and offer changes
- Tech recommendation needing arbitration: Require an **immutable audit log** for publishing, edits, suspension, and redemption events
- Tech recommendation needing arbitration: Clarify the **minimum required fields** for a listing to become live
- Growth recommendation needing arbitration: Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Growth recommendation needing arbitration: Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Growth recommendation needing arbitration: Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]
- Growth recommendation needing arbitration: Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]
- Tech open question: What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- Tech open question: What is the freshness TTL for a listing before it is hidden?
- Tech open question: Who is allowed to approve, edit, and override supply states?
- Growth open question: What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Growth open question: Which single category cluster is strongest for repeat use in the chosen neighborhood?
- Growth open question: What is the primary local user segment: residents, workers, or both?

## Risks

- Supply may still be too thin even with manual curation, causing the app to feel empty [supply_density]
- Offers may become stale if operations cannot refresh them fast enough [offer_freshness]
- Redemption disputes may erode merchant trust if the verification path is weak [quality_assurance]
- Supply may still be too thin to make the app feel trustworthy [supply_density]
- Recommendations may not outperform default Maps behavior [recommendation_quality]
- Merchants may join once but not continue after the pilot [merchant_value]
- Supply may still feel thin even with manual curation. [supply_density]
- Freshness operations may become too labor-intensive. [onboarding]
- Redemption may fail if merchants do not follow the process precisely. [quality_assurance]
- The neighborhood never feels dense enough, so the app looks empty [supply_density]
- Manual freshness maintenance becomes too burdensome to sustain [onboarding]
- Users do not switch from Maps/Instagram because the experience is not meaningfully better [demand_validation]
- Freshness operations may become too manual to sustain even a narrow pilot [onboarding]
- Single redemption flow may still fail in real-world merchant execution [quality_assurance]
- Operator approval latency could make the experience feel stale [quality_assurance]
- The merchant cohort is too small or too stale to make the app feel useful. [supply_density]
- The neighborhood audience is too broad, making acquisition unfocused and low-converting. [market_motion]
- Users do not perceive enough improvement over Maps, Yelp, or social platforms. [demand_validation]

## Open Questions

- What exact redemption method will be used in pilot: QR, code, or merchant-confirmed stamp?
- Who is responsible for verifying merchant data freshness and how often?
- What minimum merchant density is required for the launch neighborhood to avoid an empty feed?
- Which exact neighborhood will be the first launch area?
- What minimum merchant density is needed before consumer recruitment starts?
- What is the simplest credible redemption mechanism for pilot use?
- What exact redemption mechanism will be used in the pilot?
- What freshness cadence is operationally realistic: daily, weekly, or event-based?
- Who on the team is responsible for merchant approval and ongoing verification?
- What exact neighborhood is the first launch zone, and how many merchants are needed for it to feel complete?
- Which single category cluster is most likely to drive repeat use in that neighborhood?
- What is the one redemption/visit verification method the pilot will use?
- What exact redemption mechanism is preferred for MVP: code, QR, or operator-confirmed check-in?
- What is the freshness TTL for a listing before it is hidden?
- Who is allowed to approve, edit, and override supply states?
- What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Which single category cluster is strongest for repeat use in the chosen neighborhood?
- What is the primary local user segment: residents, workers, or both?

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to discover and support local independent businesses default to Google Maps, Yelp, and social platforms because local discovery is fragmented and inconsistent. Independent businesses also struggle to earn repeat visits without expensive marketing tools. LocalLoop’s MVP should prove a narrow wedge: a trusted, neighborhood-specific discovery experience for one dense area that helps users find relevant places and gives merchants a simple way to attract first visits.

## Initial Wedge
Launch in one neighborhood in one city with a tightly curated set of independent coffee shops, cafes, and casual lunch spots. The wedge is not all local commerce; it is a repeat-use local discovery loop where density, freshness, and relevance can be maintained manually.

## First Target User
People who live or work in the launch neighborhood and already use mobile search or maps for nearby decisions. They are most likely to try a new app if results feel clearly local, current, and better than generic search.

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps and Apple Maps for nearby search and directions
- Yelp for ratings and reviews
- Instagram/TikTok for local discovery
- Merchant websites and social pages for offers
- Deal apps for discounts

Switching trigger:
- The app surfaces a better nearby option from the immediate neighborhood
- The result includes a verified current offer or reward
- The feed feels denser and more trustworthy than generic search because it is manually curated and freshness-checked

## Core MVP Workflow
1. User opens the app and shares location.
2. App shows a small set of nearby independent businesses in the launch neighborhood.
3. Results are ranked with simple rules based on proximity, category fit, freshness, and available offer.
4. Each merchant listing shows hours, distance, category, short description, freshness status, and one current offer or loyalty reward.
5. User taps to save, get directions, or redeem a reward.
6. Redemption is verified using one predefined MVP method.
7. User can mark the result useful or not useful.
8. Merchant activity and redemptions are tracked for pilot review.

## In Scope
- One launch neighborhood only
- Independent businesses only
- One category cluster for dense repeat use
- Rules-based ranking, not advanced AI personalization
- Merchant profile pages with hours, location, category, short description, and freshness status
- One current offer or loyalty reward per merchant
- Single MVP redemption/visit verification method
- Save/favorite functionality
- Map handoff for directions
- Basic useful / not useful feedback
- Operator-only approval before anything goes live
- Immutable audit log for merchant, offer, suspension, and redemption events
- Manual merchant onboarding for pilot supply
- Basic admin controls for offer approval, suspension, and support override
- Automatic hiding of stale listings
- Minimum required fields before a listing can go live
- Freshness-control workflow with required fields and check cadence

## Out of Scope
- Reviews and public ratings
- Event discovery feed
- Citywide or multi-city rollout
- Broad category expansion beyond the launch cluster
- In-app ordering, booking, or payments
- Delivery
- Paid promotions or sponsored placement
- Complex recommendation models
- Merchant self-serve onboarding
- Deep merchant analytics dashboard
- User-to-merchant messaging
- Social feed mechanics
- Horizontal competition with general-purpose local search platforms
- Multiple redemption methods
- Automatic merchant onboarding
- Broader personalization experiments

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based discovery for one neighborhood
- Merchant profile pages
- Rules-based ranking
- Freshness status on listings
- Automatic hiding of stale entries
- One redemption/visit verification method
- Save/favorite and map handoff
- Basic feedback signal
- Operator-only approval queue
- Immutable audit log
- Minimum fields required before go-live
- Basic admin controls for approval, suspension, and support override
- Freshness-control workflow

### Manual Or Operational During Pilot
- Merchant sourcing and onboarding
- Offer setup and verification
- Freshness checks
- Category curation
- Consumer recruitment in the launch neighborhood
- Customer support for merchant issues
- Renewal check-ins with merchants
- Fallback handling when redemption verification fails

### Deferred Until After Proof
- Reviews and ratings
- Event feed
- Advanced personalization models
- Automated self-serve merchant onboarding
- Merchant analytics dashboard
- Paid placements
- Multi-city expansion
- In-app payments or ordering

## Business Model Hypothesis
The early model is a merchant subscription or monthly fee for inclusion, offer participation, and loyalty exposure within a dense neighborhood, potentially preceded by a free pilot period. A later model could add premium placement or performance-based promotion, but the MVP should only test whether merchants value incremental visits enough to continue after the pilot.

## Critical Assumptions
- A dense enough set of independent businesses can be assembled and kept current in one neighborhood
- Users will try a neighborhood-specific app if results feel relevant and verified
- Simple offers or loyalty rewards are enough to motivate first visits
- Merchants will participate without requiring a full self-serve platform
- Users will prefer this curated local layer over default behavior in Maps or social apps
- A single redemption method can be executed reliably by merchants and users
- A minimal onboarding flow is sufficient for merchants to join and stay active through the pilot

## How To Test Quickly
- Manually recruit a small cohort of independent businesses in one neighborhood
- Keep onboarding to a founder-led process that collects only required business details, validates hours and location, agrees on one offer, and obtains operator approval before publishing
- Curate only the chosen category cluster to maintain density
- Launch to a small local user group
- Compare engagement on curated recommendations versus a basic directory view
- Track saves, taps to directions, redemptions, and repeat opens
- Review merchant willingness to continue after the pilot period
- Monitor whether freshness and verification reduce trust issues
- Measure how long onboarding takes and how many merchants complete the process without follow-up

## Acceptance Criteria
- One launch neighborhood is fully defined and populated with a dense set of participating businesses
- At least 60% of listed businesses have verified hours, location, and one current offer
- Each listing shows freshness status and stale entries are hidden automatically
- Users can discover, save, and navigate to a business in under 60 seconds
- One redemption/visit verification method works reliably in pilot
- At least 25% of activated users engage with a listing in their first session
- At least 10% of activated users return within 30 days
- A meaningful subset of merchants indicates willingness to continue after the pilot
- Merchant onboarding can be completed with a minimal founder-led flow and no product-heavy setup
- No merchant or offer appears without operator approval and required minimum fields

## Risks And Failure Modes
- Supply density is too weak, making the app feel empty [supply_density]
- Listings become stale and trust erodes [quality_assurance]
- The chosen category cluster does not create repeat use [market_motion]
- Rules-based ranking is still too generic to beat Maps or social apps [demand_validation]
- Merchants do not see enough value to continue [merchant_value]
- Manual curation and freshness checks create too much operational burden [onboarding]
- Redemption is confusing or unreliable for merchants and users [quality_assurance]
- The app tries to broaden scope before the neighborhood wedge is proven [scope]

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No validated evidence that one neighborhood can sustain enough current, trusted supply to feel complete [supply_density]
- No proof that the curated, rules-based recommendation experience is better than existing alternatives [demand_validation]
- No proof that merchants will renew after a pilot period [merchant_value]

Required Improvements:
- Run a concierge pilot in one neighborhood with manual curation and freshness checks [quality_assurance]
- Validate merchant renewal intent with a small pilot cohort [merchant_value]
- Test the curated feed against a simple baseline directory [demand_validation]
- Confirm a single redemption/visit verification method before launch [quality_assurance]
- Keep merchant onboarding to a minimal founder-led flow with strict approval gates [onboarding]

## Recommendation
Proceed only as a concierge-first pilot in one neighborhood with a narrow category cluster and manually maintained supply. Keep the MVP focused on proving density, freshness, redemption, and merchant willingness to continue. Do not expand into reviews, events, broader personalization, or multi-city rollout until the pilot shows repeat user engagement and credible merchant retention.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Tech: Add a mandatory **freshness-control workflow** with required fields, check cadence, and automatic stale hiding
- Tech: Require an **immutable audit log** for publishing, edits, suspension, and redemption events

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
