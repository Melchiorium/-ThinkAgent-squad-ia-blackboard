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


## Architecture Mermaid Ready

True


## Architecture Mermaid Source

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/LocalLoop/version 1/architecture-diagram.mmd


## Architecture Image Ready

True


## Architecture Image Path

/Users/rodolphe.rosalie/ProjetsIA/squad-ia-blackboard/outputs/tests/LocalLoop/version 1/architecture-diagram.png


## Readiness

## Product Status

LIMITED


## Product Blocking Gaps

### demand_validation
- [demand_validation] No proof yet that curated local discovery changes user behavior in Paris

### quality_assurance
- [quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation

### untagged
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use

## Product Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and merchants in one fixed Paris micro-market

### demand_validation
- [demand_validation] Validate repeat visit and redemption behavior with coffee and lunch only
- [demand_validation] Confirm merchant willingness to continue after initial traffic testing

## Tech Status

LIMITED


## Tech Blocking Gaps

### quality_assurance
- [quality_assurance] The merchant quality gate is not yet defined as a hard publish control with required fields and approval state.

### untagged
- The redemption token lifecycle is still too implicit to guarantee reliable in-store use.
- The merchant validation path is not fixed, so staff-side execution could be inconsistent.

## Tech Required Improvements

### quality_assurance
- [quality_assurance] Implement a mandatory pre-live checklist in the admin console with required fields and approval lockout.
- [quality_assurance] Define the single redemption token format, expiry, consumption, and dispute states.

### scope
- [scope] Choose one validation path for merchants and keep it operationally minimal for MVP.

## Growth Status

LIMITED


## Growth Blocking Gaps

### demand_validation
- [demand_validation] No named Paris micro-market selected, so supply density and localized traction cannot be tested credibly
- [demand_validation] Demand proof is undefined without a concrete repeat-use and redemption threshold

### scope
- [scope] First audience is still too broad; the launch needs one narrow frequent-use segment

## Growth Required Improvements

### scope
- [scope] Select one Paris micro-market and lock the pilot boundary before merchant sourcing begins
- [scope] Keep the launch to one category pair and one offer mechanic only

### market_motion
- [market_motion] Narrow the first audience to frequent coffee/lunch decision-makers in that micro-market

### demand_validation
- [demand_validation] Define a measurable success threshold for repeat visits and redemption volume

### quality_assurance
- [quality_assurance] Require manual merchant approval and quality checklist completion before any live listing

## Global Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] No proof yet that curated local discovery changes user behavior in Paris
- [demand_validation] No named Paris micro-market selected, so supply density and localized traction cannot be tested credibly
- [demand_validation] Demand proof is undefined without a concrete repeat-use and redemption threshold

### quality_assurance
- [quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation
- [quality_assurance] The merchant quality gate is not yet defined as a hard publish control with required fields and approval state.

### untagged
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use
- The redemption token lifecycle is still too implicit to guarantee reliable in-store use.
- The merchant validation path is not fixed, so staff-side execution could be inconsistent.

### scope
- [scope] First audience is still too broad; the launch needs one narrow frequent-use segment

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and merchants in one fixed Paris micro-market
- [market_motion] Narrow the first audience to frequent coffee/lunch decision-makers in that micro-market

### demand_validation
- [demand_validation] Validate repeat visit and redemption behavior with coffee and lunch only
- [demand_validation] Confirm merchant willingness to continue after initial traffic testing
- [demand_validation] Define a measurable success threshold for repeat visits and redemption volume

### quality_assurance
- [quality_assurance] Implement a mandatory pre-live checklist in the admin console with required fields and approval lockout.
- [quality_assurance] Define the single redemption token format, expiry, consumption, and dispute states.
- [quality_assurance] Require manual merchant approval and quality checklist completion before any live listing

### scope
- [scope] Choose one validation path for merchants and keep it operationally minimal for MVP.
- [scope] Select one Paris micro-market and lock the pilot boundary before merchant sourcing begins
- [scope] Keep the launch to one category pair and one offer mechanic only

## Known Tags

- demand_validation
- quality_assurance
- untagged
- scope
- market_motion


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

[quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation Redemption flow is not yet specified with enough precision to guarantee in-store reliability Define a single end-to-end redemption flow with clear token format, validation step, and failure fallback No proof that the redemption flow is frictionless enough for live use Test the in-store redemption flow with real staff before any public launch


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

- growth


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot with real users and merchants in one Paris neighborhood cluster No validated proof that enough merchants in one micro-market will participate and remain active Run a concierge pilot in one named Paris neighborhood cluster with a fixed merchant set


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] No proof yet that curated local discovery changes user behavior in Paris Validate repeat visit and redemption behavior with a narrow category set Confirm merchant willingness to continue after initial traffic testing No validated proof that the narrowed Paris discovery loop changes user behavior versus existing defaults Validate one narrow use case and measure repeat use, not broad engagement


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

_Aucun contributeur._


### Loop 2

#### Tech Task

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation Redemption flow is not yet specified with enough precision to guarantee in-store reliability No concrete merchant quality gate exists to prevent weak or incorrect supply from going live Define a single end-to-end redemption flow with token format, expiry, consumption rules, and failure fallback


## Expected Output

A concrete quality-control answer that fits MVP scope.


## Contributors

_Aucun contributeur._


#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot with real users and merchants in one fixed Paris neighborhood cluster Add a mandatory pre-live merchant quality checklist and approval step before activation No named Paris micro-market has been selected for the pilot, so supply density cannot be assessed credibly The first audience is still too broad; the launch needs one narrow, high-frequency use case Select one Paris neighborhood cluster and set a fixed merchant target before acquisition begins Narrow the first audience to frequent local coffee/lunch decision-makers in that cluster


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

- tech


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] No proof yet that curated local discovery changes user behavior in Paris Validate repeat visit and redemption behavior with one narrow category pair Confirm merchant willingness to continue after initial traffic testing Demand proof is undefined beyond general engagement; the team needs a measurable repeat-use and redemption threshold Define a concrete demand signal such as repeat visit rate within a short window and minimum redemption volume


## Expected Output

A concrete demand-validation approach with a signal threshold.


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
- [demand_validation] No proof yet that curated local discovery changes user behavior in Paris
- [demand_validation] No validated proof that the narrowed Paris discovery loop changes user behavior versus existing defaults

### quality_assurance
- [quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation
- [quality_assurance] Redemption flow is not yet specified with enough precision to guarantee in-store reliability
- [quality_assurance] No proof that the redemption flow is frictionless enough for live use

### untagged
- No proof yet that the single redemption flow and loyalty tracking work reliably in live use
- Merchant lifecycle and offer validity rules are not defined tightly enough to prevent stale inventory from reaching users
- Loyalty state and duplicate-redemption prevention are not yet specified at the data-model level

### market_motion
- [market_motion] No validated proof that enough merchants in one micro-market will participate and remain active

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and merchants in one Paris neighborhood cluster
- [market_motion] Run a concierge pilot in one named Paris neighborhood cluster with a fixed merchant set

### demand_validation
- [demand_validation] Validate repeat visit and redemption behavior with a narrow category set
- [demand_validation] Confirm merchant willingness to continue after initial traffic testing
- [demand_validation] Validate one narrow use case and measure repeat use, not broad engagement

### quality_assurance
- [quality_assurance] Define a single end-to-end redemption flow with clear token format, validation step, and failure fallback
- [quality_assurance] Test the in-store redemption flow with real staff before any public launch

### untagged
- Add merchant and offer state transitions with expiry, pause, and archive behavior
- Specify loyalty event sourcing or equivalent idempotent storage for repeat visits and reward issuance

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation Redemption flow is not yet specified with enough precision to guarantee in-store reliability Define a single end-to-end redemption flow with clear token format, validation step, and failure fallback No proof that the redemption flow is frictionless enough for live use Test the in-store redemption flow with real staff before any public launch


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot with real users and merchants in one Paris neighborhood cluster No validated proof that enough merchants in one micro-market will participate and remain active Run a concierge pilot in one named Paris neighborhood cluster with a fixed merchant set


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] No proof yet that curated local discovery changes user behavior in Paris Validate repeat visit and redemption behavior with a narrow category set Confirm merchant willingness to continue after initial traffic testing No validated proof that the narrowed Paris discovery loop changes user behavior versus existing defaults Validate one narrow use case and measure repeat use, not broad engagement


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
- [demand_validation] No proof yet that curated local discovery changes user behavior in Paris
- [demand_validation] Demand proof is undefined beyond general engagement; the team needs a measurable repeat-use and redemption threshold

### quality_assurance
- [quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation
- [quality_assurance] Redemption flow is not yet specified with enough precision to guarantee in-store reliability
- [quality_assurance] No concrete merchant quality gate exists to prevent weak or incorrect supply from going live

### untagged
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use

### market_motion
- [market_motion] No named Paris micro-market has been selected for the pilot, so supply density cannot be assessed credibly
- [market_motion] The first audience is still too broad; the launch needs one narrow, high-frequency use case

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and merchants in one fixed Paris neighborhood cluster
- [market_motion] Add a mandatory pre-live merchant quality checklist and approval step before activation
- [market_motion] Select one Paris neighborhood cluster and set a fixed merchant target before acquisition begins
- [market_motion] Narrow the first audience to frequent local coffee/lunch decision-makers in that cluster

### demand_validation
- [demand_validation] Validate repeat visit and redemption behavior with one narrow category pair
- [demand_validation] Confirm merchant willingness to continue after initial traffic testing
- [demand_validation] Define a concrete demand signal such as repeat visit rate within a short window and minimum redemption volume

### quality_assurance
- [quality_assurance] Define a single end-to-end redemption flow with token format, expiry, consumption rules, and failure fallback

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation Redemption flow is not yet specified with enough precision to guarantee in-store reliability Define a single end-to-end redemption flow with clear token format, validation step, and failure fallback No proof that the redemption flow is frictionless enough for live use Test the in-store redemption flow with real staff before any public launch


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot with real users and merchants in one Paris neighborhood cluster No validated proof that enough merchants in one micro-market will participate and remain active Run a concierge pilot in one named Paris neighborhood cluster with a fixed merchant set


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] No proof yet that curated local discovery changes user behavior in Paris Validate repeat visit and redemption behavior with a narrow category set Confirm merchant willingness to continue after initial traffic testing No validated proof that the narrowed Paris discovery loop changes user behavior versus existing defaults Validate one narrow use case and measure repeat use, not broad engagement


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
- [demand_validation] No proof yet that curated local discovery changes user behavior in Paris
- [demand_validation] Demand proof is undefined beyond general engagement; the team needs a measurable repeat-use and redemption threshold

### quality_assurance
- [quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation
- [quality_assurance] Redemption flow is not yet specified with enough precision to guarantee in-store reliability
- [quality_assurance] No concrete merchant quality gate exists to prevent weak or incorrect supply from going live

### untagged
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use

### market_motion
- [market_motion] No named Paris micro-market has been selected for the pilot, so supply density cannot be assessed credibly
- [market_motion] The first audience is still too broad; the launch needs one narrow, high-frequency use case

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and merchants in one fixed Paris neighborhood cluster
- [market_motion] Add a mandatory pre-live merchant quality checklist and approval step before activation
- [market_motion] Select one Paris neighborhood cluster and set a fixed merchant target before acquisition begins
- [market_motion] Narrow the first audience to frequent local coffee/lunch decision-makers in that cluster

### demand_validation
- [demand_validation] Validate repeat visit and redemption behavior with one narrow category pair
- [demand_validation] Confirm merchant willingness to continue after initial traffic testing
- [demand_validation] Define a concrete demand signal such as repeat visit rate within a short window and minimum redemption volume

### quality_assurance
- [quality_assurance] Define a single end-to-end redemption flow with token format, expiry, consumption rules, and failure fallback

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation Redemption flow is not yet specified with enough precision to guarantee in-store reliability No concrete merchant quality gate exists to prevent weak or incorrect supply from going live Define a single end-to-end redemption flow with token format, expiry, consumption rules, and failure fallback


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot with real users and merchants in one fixed Paris neighborhood cluster Add a mandatory pre-live merchant quality checklist and approval step before activation No named Paris micro-market has been selected for the pilot, so supply density cannot be assessed credibly The first audience is still too broad; the launch needs one narrow, high-frequency use case Select one Paris neighborhood cluster and set a fixed merchant target before acquisition begins Narrow the first audience to frequent local coffee/lunch decision-makers in that cluster


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] No proof yet that curated local discovery changes user behavior in Paris Validate repeat visit and redemption behavior with one narrow category pair Confirm merchant willingness to continue after initial traffic testing Demand proof is undefined beyond general engagement; the team needs a measurable repeat-use and redemption threshold Define a concrete demand signal such as repeat visit rate within a short window and minimum redemption volume


## Expected Output

A concrete demand-validation approach with a signal threshold.


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
- [demand_validation] No proof yet that curated local discovery changes user behavior in Paris
- [demand_validation] No named Paris micro-market selected, so supply density and localized traction cannot be tested credibly
- [demand_validation] Demand proof is undefined without a concrete repeat-use and redemption threshold

### quality_assurance
- [quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation
- [quality_assurance] The merchant quality gate is not yet defined as a hard publish control with required fields and approval state.

### untagged
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use
- The redemption token lifecycle is still too implicit to guarantee reliable in-store use.
- The merchant validation path is not fixed, so staff-side execution could be inconsistent.

### scope
- [scope] First audience is still too broad; the launch needs one narrow frequent-use segment

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and merchants in one fixed Paris micro-market
- [market_motion] Narrow the first audience to frequent coffee/lunch decision-makers in that micro-market

### demand_validation
- [demand_validation] Validate repeat visit and redemption behavior with coffee and lunch only
- [demand_validation] Confirm merchant willingness to continue after initial traffic testing
- [demand_validation] Define a measurable success threshold for repeat visits and redemption volume

### quality_assurance
- [quality_assurance] Implement a mandatory pre-live checklist in the admin console with required fields and approval lockout.
- [quality_assurance] Define the single redemption token format, expiry, consumption, and dispute states.
- [quality_assurance] Require manual merchant approval and quality checklist completion before any live listing

### scope
- [scope] Choose one validation path for merchants and keep it operationally minimal for MVP.
- [scope] Select one Paris micro-market and lock the pilot boundary before merchant sourcing begins
- [scope] Keep the launch to one category pair and one offer mechanic only

## Loop Tasks

##### Tech

## Task

Clarify the smallest quality-control mechanism needed for MVP submissions or supply.


## Source Gap

[quality_assurance] No proof yet that merchants will provide enough quality inventory and continue participation Redemption flow is not yet specified with enough precision to guarantee in-store reliability No concrete merchant quality gate exists to prevent weak or incorrect supply from going live Define a single end-to-end redemption flow with token format, expiry, consumption rules, and failure fallback


## Expected Output

A concrete quality-control answer that fits MVP scope.


##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] Run a concierge pilot with real users and merchants in one fixed Paris neighborhood cluster Add a mandatory pre-live merchant quality checklist and approval step before activation No named Paris micro-market has been selected for the pilot, so supply density cannot be assessed credibly The first audience is still too broad; the launch needs one narrow, high-frequency use case Select one Paris neighborhood cluster and set a fixed merchant target before acquisition begins Narrow the first audience to frequent local coffee/lunch decision-makers in that cluster


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] No proof yet that curated local discovery changes user behavior in Paris Validate repeat visit and redemption behavior with one narrow category pair Confirm merchant willingness to continue after initial traffic testing Demand proof is undefined beyond general engagement; the team needs a measurable repeat-use and redemption threshold Define a concrete demand signal such as repeat visit rate within a short window and minimum redemption volume


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] **Manual supply gating before publish**
- [tech] Every merchant must pass a checklist and be explicitly approved by ops before becoming visible.
- [tech] This is the key quality-control mechanism for MVP supply.
- [tech] **Single redemption model**

## Growth Structural Decisions

### growth
- [growth] Define one named Paris micro-market for the pilot instead of “one neighborhood cluster.”
- [growth] Narrow the first audience to **frequent coffee/lunch decision-makers in that micro-market**.

## Product Locking

## Applied

True


## Confirmed In Scope

- Paris-only consumer app [scope]
- One named Paris micro-market [market_motion]
- Frequent coffee/lunch decision-makers as the first audience [market_motion]
- Independent coffee shops and lunch spots only [scope]
- Manual supply gating before publish [quality_assurance]
- Merchant quality checklist before activation [quality_assurance]
- One ops-approved live state with no self-serve publishing [quality_assurance]
- Single redemption model [quality_assurance]
- Explicit redemption token lifecycle in the admin workflow [quality_assurance]
- Stale-offer suppression [quality_assurance]
- Audit log for manual overrides, publish, and dispute actions [quality_assurance]
- Basic merchant analytics [scope]


## Confirmed Deferred

- Self-serve merchant portal
- Advanced personalization
- Reviews and social features
- Event discovery feed
- Multi-city rollout
- Paid merchant tools and campaigns
- Cross-merchant rewards
- Automated offer optimization
- Broad category expansion
- Multiple redemption paths
- Full merchant CRM tooling


## Confirmed Out Of Scope

- Open reviews and ratings
- Deep social features
- Delivery ordering
- Table booking
- Chain businesses and horizontal retail coverage
- Heavy gamification
- Uncurated open marketplace inventory
- Merchant-initiated live publishing without approval


## Locking Note

- Scope remains intentionally narrow for proof: local discovery, one offer, one redemption path, and verified repeat visits. - No broader marketplace, social, or monetization expansion is being added in this pass. - The remaining open questions are operational, not scope-expanding.


## Expert Contributions

### Tech Summary

The MVP is only feasible if LocalLoop is treated as a tightly controlled concierge system, not a marketplace. The critical path is merchant quality control plus a simple, reliable redemption mechanism; everything else should remain manual until the pilot proves that curated Paris supply can sustain repeat visits.

## Tech Structural Decisions

- **Manual supply gating before publish**
- Every merchant must pass a checklist and be explicitly approved by ops before becoming visible.
- This is the key quality-control mechanism for MVP supply.
- **Single redemption model**


## Tech Recommendations

- Define the merchant quality checklist as a required publish gate in the admin console, not a manual guideline. [quality_assurance]
- Specify the exact redemption token lifecycle: issued, expiring, consumed, disputed, voided. [quality_assurance]
- Constrain merchant activation to one ops-approved live state with no self-serve publishing. [quality_assurance]
- Add an explicit stale-offer suppression rule so inactive merchants cannot appear in the feed. [quality_assurance]
- Require an audit log entry for every manual override, publish, or dispute resolution action. [quality_assurance]


## Tech Risks

- Manual approval may become a bottleneck if merchant onboarding volume rises too quickly. [ops_scalability]
- Token validation may fail at the point of visit if merchant staff do not have a simple enough process. [redemption_friction]
- Poorly controlled supply may still create a feed that feels thin or inconsistent. [quality_assurance]


## Tech Open Questions

- Should merchant validation be done by an ops staffer, or by merchant staff through a minimal validation screen?
- What exact expiry window should the one-time token use to balance safety and in-store usability?
- Which fields are mandatory for the quality checklist before a merchant can go live?


### Growth Summary

The launch challenge is not building a broad local marketplace; it is proving that one tightly curated Paris neighborhood cluster can generate enough repeat use and merchant value to justify expansion. The recommended direction is a founder-led concierge pilot in one micro-market, starting with merchant supply, then recruiting a narrow audience of frequent coffee/lunch decision-makers.

## Growth Structural Decisions

- Define one named Paris micro-market for the pilot instead of “one neighborhood cluster.”
- Narrow the first audience to **frequent coffee/lunch decision-makers in that micro-market**.


## Growth Recommendations

- Define one named Paris micro-market for the pilot instead of “one neighborhood cluster.”
- Narrow the first audience to **frequent coffee/lunch decision-makers in that micro-market**.
- Specify the first category pair explicitly and remove broader category ambiguity.
- Add a concrete demand threshold, such as minimum repeat visit rate and minimum redemption volume, for pilot success.
- Clarify the merchant activation rule: no merchant goes live without a completed quality checklist and manual approval.


## Growth Risks

- Supply density may still be too thin in the chosen micro-market.
- Users may treat the app as another local directory and revert to Google Maps.
- Merchants may not perceive enough incremental traffic to stay active.


## Growth Open Questions

- Which exact Paris micro-market will be used first?
- What is the exact first category pair: coffee + lunch, or something else?
- What is the minimum merchant count needed for the feed to feel alive?


## Product Arbitration

## Source

parsed


## Retained

- Manual supply gating before publish [quality_assurance]
- Single redemption model [quality_assurance]
- Merchant quality checklist as a required publish gate [quality_assurance]
- Explicit redemption token lifecycle in the admin workflow [quality_assurance]
- One ops-approved live state with no self-serve publishing [quality_assurance]
- Stale-offer suppression so inactive merchants do not appear in feed [quality_assurance]
- Audit log for every manual override, publish, and dispute action [quality_assurance]
- One named Paris micro-market for the pilot [market_motion]
- Narrow first audience to frequent coffee/lunch decision-makers in that micro-market [market_motion]
- First category pair limited to coffee and lunch [scope]
- Concrete pilot success threshold tied to repeat visits and redemptions [demand_validation]
- Manual approval required before any merchant goes live [quality_assurance]


## Deferred

- Self-serve merchant portal
- Advanced personalization
- Reviews and social features
- Event discovery feed
- Multi-city rollout
- Paid merchant tools and campaigns
- Cross-merchant rewards
- Automated offer optimization
- Broad category expansion
- Multiple redemption paths
- Full merchant CRM tooling


## Rejected

- Open reviews and ratings
- Deep social features
- Delivery ordering
- Table booking
- Chain businesses and horizontal retail coverage
- Heavy gamification
- Uncurated open marketplace inventory
- Merchant-initiated live publishing without approval


## Open Points

- Exact named Paris micro-market for the pilot [market_motion]
- Exact expiry window for the redemption token [quality_assurance]
- Whether merchant validation is performed by ops or merchant staff [quality_assurance]
- Exact mandatory fields in the merchant quality checklist [quality_assurance]
- Minimum merchant count needed for the feed to feel alive [demand_validation]


## Rationales

- The MVP only works if supply quality is tightly controlled; otherwise it collapses into a generic local listings app.
- Coffee and lunch are the cleanest repeat-use wedge for Paris because they support frequent decisions and short feedback loops.
- Manual operations are acceptable in the pilot because they are proof-critical, not scalable product scope.
- Reviews, social, and broader category expansion add complexity without helping the MVP prove visits, retention, or merchant value.
- Exact micro-market naming and token timing are important, but the brief does not provide enough evidence to lock them safely yet.


## Reconciliation Notes

- Parsed Product Arbitration supplied by Product; heuristic reconciliation was not needed.


## Reconciliation Warnings

_Aucune contradiction détectée._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
People in Paris who want to support local businesses still default to Google Maps, Instagram, Deliveroo/Tripadvisor, or word-of-mouth because local discovery is fragmented and not personalized enough.

Independent businesses want nearby customers and repeat visits, but they lack simple tools and distribution to compete for attention.

The product must prove one narrow thing first: whether a localized discovery loop can drive real visits to independent businesses in one city better than generic search and social browsing.

## Initial Wedge
A Paris-only mobile app for young professionals and urban residents that recommends nearby independent coffee shops, lunch spots, and small retail businesses with simple neighborhood offers and a lightweight loyalty reward.

This wedge is narrow enough to solve a frequent local need and practical enough to build a credible supply base in one city.

## First Target User
Primary user:
- Urban residents in Paris, especially young professionals aged 22–40

First use case:
- “I want a good nearby independent place to go right now, with a reason to choose it over a chain.”

Secondary supply-side target:
- Independent coffee shops, casual restaurants, and small neighborhood businesses in central Paris

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps for discovery and directions
- Instagram/TikTok for informal recommendations
- Deliveroo/Uber Eats for food discovery
- City guides and blogs for editorial discovery
- Paper loyalty cards or POS-linked loyalty tools for retention

Switching trigger:
- The user wants a curated, local-only recommendation with an immediate incentive, not a generic map result or influencer content.
- The merchant wants first-time foot traffic or repeat visits without running paid ads or building their own app.

## Core MVP Workflow
1. User opens the app and sets a few preferences: neighborhood, category, and broad interests.
2. App shows a small feed of nearby independent businesses.
3. Each listing includes:
   - short merchant description
   - distance
   - one offer or reward
   - one loyalty action
4. User taps a merchant and sees enough detail to decide to visit.
5. User redeems an offer in-store or via a simple code/QR check-in.
6. Loyalty accrues through repeat visits to the same merchant.
7. Merchant sees basic redemptions and repeat activity.

## In Scope
- Paris-only consumer app
- Independent business listings
- Basic personalization by location and category
- Merchant profile page with essential details
- Simple offer display
- Simple loyalty tracking for repeated visits
- Manual merchant onboarding for pilot
- Basic merchant analytics: views, redemptions, repeat visits
- Curated neighborhood inventory to reduce irrelevant listings

## Out of Scope
- Citywide expansion beyond Paris
- Multi-city marketplace mechanics
- Deep social features
- Open reviews and ratings
- Full event aggregation feed
- Advanced recommendation engine
- Merchant self-serve onboarding
- Ad marketplace or paid promotion system
- Delivery ordering
- Table booking
- Full CRM or marketing automation for merchants
- Chain businesses and horizontal retail coverage
- Heavy gamification

## MVP Build Vs Pilot Operations
### Must Build Now
- Consumer mobile app
- Merchant profile pages
- Nearby discovery feed
- Basic preference and location filtering
- Offer display
- Loyalty tracking for repeat visits
- Simple redemption mechanism
- Basic merchant analytics

### Manual Or Operational During Pilot
- Merchant sourcing and onboarding in Paris
- Offer setup and validation
- Content curation to keep feed relevant
- Quality checks on listings and merchant details
- Customer support for redemption issues
- Outreach to merchants and initial users
- Neighborhood selection and inventory balancing

### Deferred Until After Proof
- Self-serve merchant portal
- Advanced personalization
- Reviews and social features
- Automated offer optimization
- Event discovery feed
- Multi-city rollout
- Paid merchant tools and campaigns
- Complex loyalty tiers or cross-merchant rewards

## Business Model Hypothesis
Primary hypothesis:
- Charge merchants a simple monthly subscription for visibility, offers, and basic retention tools once the product proves it can drive visits.

Secondary hypothesis:
- Eventually add paid promotion placements or premium analytics, but only after proving merchant ROI and user engagement.

For the pilot, the objective is not monetization optimization; it is validating willingness to pay after measurable foot traffic and repeat visits.

## Critical Assumptions
- Users will trust the app enough to try a local recommendation instead of using Google Maps.
- Enough independent businesses in one Paris neighborhood will participate.
- Offers and loyalty rewards will be compelling enough to change behavior.
- The app can keep recommendations relevant without a large inventory.
- Merchants will see value in simple visit and repeat-visit tracking.
- Redeeming offers in-store can be made simple and reliable.
- The experience can avoid looking like a noisy coupon directory.

## How To Test Quickly
- Run a concierge pilot in 1–2 Paris neighborhoods with 20–30 independent businesses.
- Manually curate a small set of merchants in one or two high-frequency categories.
- Offer users a limited beta focused on “where should I go nearby?”
- Track:
  - app opens
  - listing clicks
  - offer redemptions
  - repeat visits
  - merchant willingness to continue
- Interview users after visits to understand what made them choose the business.
- Interview merchants to determine whether the app delivered incremental traffic or retention.

## Acceptance Criteria
- A user can find a relevant nearby independent business in under 30 seconds.
- A merchant profile clearly shows location, offer, and reason to visit.
- Redemption works reliably with minimal staff confusion.
- At least 20 participating businesses are active in the pilot area.
- Users can redeem an offer or loyalty reward without support intervention in most cases.
- Merchants can see basic activity metrics.
- At least one-third of pilot merchants report perceived incremental value.
- A meaningful share of users return for a second visit to the same merchant within a short test window.

## Risks And Failure Modes
- Poor supply density makes the app feel empty [supply_density]
- Recommendations are too generic and users revert to Google Maps [recommendation_quality]
- Merchants do not see enough ROI to stay active [merchant_roi]
- Offers attract deal-seekers who do not convert into repeat customers [low_quality_traffic]
- Manual curation does not scale beyond the pilot [ops_scalability]
- Redemption friction causes failure at the point of visit [redemption_friction]
- The product becomes another irrelevant local listing app [category_blur]

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No proof yet that curated local discovery changes user behavior in Paris [demand_validation]
- No proof yet that merchants will provide enough quality inventory and continue participation [supply_validation]
- No proof yet that redemption and loyalty are simple enough to work reliably in live use [redemption_friction]

Required Improvements:
- Run a concierge pilot with real users and merchants in one Paris neighborhood [concierge_pilot]
- Validate repeat visit and redemption behavior with a narrow category set [behavior_proof]
- Confirm merchant willingness to continue after initial traffic testing [merchant_roi]

## Recommendation
Proceed with a tightly scoped Paris concierge pilot.

Do not build a broad marketplace yet. The right next step is to prove one repeatable use case: nearby independent business discovery with a simple offer and loyalty loop.

If pilot results show weak user pull or merchant retention, stop or re-scope before expanding beyond a few neighborhoods.

## Retained Decisions

- Manual supply gating before publish [quality_assurance]
- Single redemption model [quality_assurance]
- Merchant quality checklist as a required publish gate [quality_assurance]
- Explicit redemption token lifecycle in the admin workflow [quality_assurance]
- One ops-approved live state with no self-serve publishing [quality_assurance]
- Stale-offer suppression so inactive merchants do not appear in feed [quality_assurance]
- Audit log for every manual override, publish, and dispute action [quality_assurance]
- One named Paris micro-market for the pilot [market_motion]
- Narrow first audience to frequent coffee/lunch decision-makers in that micro-market [market_motion]
- First category pair limited to coffee and lunch [scope]
- Concrete pilot success threshold tied to repeat visits and redemptions [demand_validation]
- Manual approval required before any merchant goes live [quality_assurance]

## Deferred Decisions

- Self-serve merchant portal
- Advanced personalization
- Reviews and social features
- Event discovery feed
- Multi-city rollout
- Paid merchant tools and campaigns
- Cross-merchant rewards
- Automated offer optimization
- Broad category expansion
- Multiple redemption paths
- Full merchant CRM tooling

## Rejected Recommendations

- Open reviews and ratings
- Deep social features
- Delivery ordering
- Table booking
- Chain businesses and horizontal retail coverage
- Heavy gamification
- Uncurated open marketplace inventory
- Merchant-initiated live publishing without approval

## Unresolved Tensions

- Tech recommendation needing arbitration: Specify the exact redemption token lifecycle: issued, expiring, consumed, disputed, voided. [quality_assurance]
- Tech recommendation needing arbitration: Constrain merchant activation to one ops-approved live state with no self-serve publishing. [quality_assurance]
- Tech recommendation needing arbitration: Add an explicit stale-offer suppression rule so inactive merchants cannot appear in the feed. [quality_assurance]
- Tech recommendation needing arbitration: Require an audit log entry for every manual override, publish, or dispute resolution action. [quality_assurance]
- Growth recommendation needing arbitration: Narrow the first audience to **frequent coffee/lunch decision-makers in that micro-market**.
- Growth recommendation needing arbitration: Specify the first category pair explicitly and remove broader category ambiguity.
- Growth recommendation needing arbitration: Add a concrete demand threshold, such as minimum repeat visit rate and minimum redemption volume, for pilot success.
- Growth recommendation needing arbitration: Clarify the merchant activation rule: no merchant goes live without a completed quality checklist and manual approval.
- Tech open question: Should merchant validation be done by an ops staffer, or by merchant staff through a minimal validation screen?
- Tech open question: What exact expiry window should the one-time token use to balance safety and in-store usability?
- Tech open question: Which fields are mandatory for the quality checklist before a merchant can go live?
- Growth open question: Which exact Paris micro-market will be used first?
- Growth open question: What is the exact first category pair: coffee + lunch, or something else?
- Growth open question: What is the minimum merchant count needed for the feed to feel alive?

## Applied Changes

- Manual supply gating before publish [quality_assurance]
- Single redemption model [quality_assurance]
- Merchant quality checklist as a required publish gate [quality_assurance]
- Explicit redemption token lifecycle in the admin workflow [quality_assurance]
- One ops-approved live state with no self-serve publishing [quality_assurance]
- Stale-offer suppression so inactive merchants do not appear in feed [quality_assurance]
- Audit log for every manual override, publish, and dispute action [quality_assurance]
- One named Paris micro-market for the pilot [market_motion]
- Narrow first audience to frequent coffee/lunch decision-makers in that micro-market [market_motion]
- First category pair limited to coffee and lunch [scope]
- Concrete pilot success threshold tied to repeat visits and redemptions [demand_validation]
- Manual approval required before any merchant goes live [quality_assurance]

## Remaining Open Points

- Exact named Paris micro-market for the pilot [market_motion]
- Exact expiry window for the redemption token [quality_assurance]
- Whether merchant validation is performed by ops or merchant staff [quality_assurance]
- Exact mandatory fields in the merchant quality checklist [quality_assurance]
- Minimum merchant count needed for the feed to feel alive [demand_validation]

## Risks

- Users default back to Google Maps because LocalLoop is not clearly better on first use.
- Supply density is too low, making the app feel empty or repetitive.
- Merchants join initially but do not stay active after the pilot period.
- Redemption failure at the merchant counter creates immediate trust loss. [quality_assurance]
- Curated inventory may become stale quickly without operational discipline. [supply_validation]
- Loyalty tracking may be gamed or duplicated without idempotent state handling. [data_integrity]
- Staff confusion at redemption if the validation flow is not extremely simple.
- Broken or stale merchant data creating mistrust in the feed.
- Manual curation overhead becoming too high if supply quality checks are too heavy.
- The neighborhood feed may feel too small to sustain repeat use.
- Merchants may join once but not stay active after initial curiosity.
- Users may treat the app like a coupon app rather than a discovery habit.
- Manual approval may become a bottleneck if merchant onboarding volume rises too quickly. [ops_scalability]
- Token validation may fail at the point of visit if merchant staff do not have a simple enough process. [redemption_friction]
- Poorly controlled supply may still create a feed that feels thin or inconsistent. [quality_assurance]
- Supply density may still be too thin in the chosen micro-market.
- Users may treat the app as another local directory and revert to Google Maps.
- Merchants may not perceive enough incremental traffic to stay active.

## Open Questions

- Which exact Paris neighborhoods have enough independent density to support the first loop?
- Which single category is strongest for repeat use: coffee, lunch, retail, or services?
- What merchant incentive is enough to get the first 20–30 businesses live?
- What is the single redemption method merchants in Paris will consistently accept?
- Will loyalty be based on QR check-ins, staff confirmation, or both?
- How often will merchant status and offer validity be reviewed operationally?
- Should redemption be validated by merchant staff in their own web view, or only by an internal ops tool?
- Is the loyalty mechanic a simple count of verified visits, or does it require merchant-specific reward rules?
- What is the exact token lifetime before expiry?
- Which exact Paris neighborhood cluster is the best first market?
- What is the minimum merchant density needed before acquisition starts?
- Which narrow category should be first: coffee, lunch, or another high-frequency use case?
- Should merchant validation be done by an ops staffer, or by merchant staff through a minimal validation screen?
- What exact expiry window should the one-time token use to balance safety and in-store usability?
- Which fields are mandatory for the quality checklist before a merchant can go live?
- Which exact Paris micro-market will be used first?
- What is the exact first category pair: coffee + lunch, or something else?
- What is the minimum merchant count needed for the feed to feel alive?

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
People in Paris who want to support local independent businesses still default to Google Maps, Instagram, Deliveroo/Tripadvisor, or word of mouth because discovery is fragmented and not personalized enough.

Independent businesses want nearby customers and repeat visits, but they lack simple tools and distribution to compete for attention.

The MVP must prove one narrow thing first: whether a tightly curated Paris discovery loop can drive real visits to independent businesses better than generic search and social browsing.

## Initial Wedge
A Paris-only mobile app for frequent coffee/lunch decision-makers in one named micro-market, focused on independent coffee shops and lunch spots, with a simple offer and a verified visit-based loyalty loop.

This is narrow enough to control supply quality, keep the feed alive, and test repeat usage in a real neighborhood context.

## First Target User
Primary user:
- Urban residents in Paris who make frequent coffee and lunch decisions on weekdays
- Young professionals aged 22–40 within the pilot micro-market

First use case:
- “I want a good nearby independent place to go right now, with a reason to choose it over a chain.”

Secondary supply-side target:
- Independent coffee shops and casual lunch spots in the same pilot micro-market

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps for discovery and directions
- Instagram/TikTok for informal recommendations
- Deliveroo/Uber Eats for food discovery
- City guides and blogs for editorial discovery
- Paper loyalty cards or POS-linked loyalty tools for retention

Switching trigger:
- The user wants a curated local-only recommendation with an immediate incentive, not a generic map result or influencer content.
- The merchant wants first-time foot traffic or repeat visits without running paid ads or building their own app.

## Core MVP Workflow
1. User opens the app and sets a few preferences: neighborhood and category.
2. App shows a small feed of nearby independent businesses that are currently active.
3. Each listing includes:
   - short merchant description
   - distance
   - one offer or reward
   - basic loyalty status
4. User taps a merchant and sees enough detail to decide to visit.
5. User redeems the offer in-store through a single one-time token shown in-app and validated by staff or ops.
6. Redemption is marked consumed once validated; failed validation can be marked disputed for later support resolution.
7. Loyalty accrues through verified repeat visits to the same merchant.
8. Merchant sees basic activity and redemption metrics.

## In Scope
- Paris-only consumer app
- One named Paris micro-market for the pilot
- Independent coffee shops and lunch spots only
- Basic filtering by location and category
- Merchant profile page with essential details
- One offer per merchant
- One loyalty mechanic tied to verified repeat visits
- One redemption method using a one-time token
- Manual merchant onboarding for pilot
- Curated inventory to reduce irrelevant listings
- Required merchant quality checklist before activation
- Manual approval for live status
- Basic merchant analytics: views, redemptions, repeat visits
- Admin controls to manage merchant live/inactive state and suppress stale offers
- Audit logs and override permissions for support-side adjustments
- Disputed redemption handling
- Fixed category set for pilot

## Out of Scope
- Citywide expansion beyond Paris
- Multi-city marketplace mechanics
- Deep social features
- Open reviews and ratings
- Full event aggregation feed
- Advanced recommendation engine
- Merchant self-serve onboarding
- Ad marketplace or paid promotion system
- Delivery ordering
- Table booking
- Full CRM or marketing automation for merchants
- Chain businesses and horizontal retail coverage
- Heavy gamification
- Multiple redemption methods
- Complex loyalty tiers or cross-merchant rewards
- Broad category coverage beyond coffee and lunch
- Automated offer optimization
- Merchant-initiated live publishing without approval
- Uncurated open marketplace inventory

## MVP Build Vs Pilot Operations
### Must Build Now
- Consumer mobile app
- Merchant profile pages
- Nearby discovery feed
- Basic preference and location filtering
- Offer display
- Single redemption flow
- Verified loyalty tracking for repeat visits
- Basic merchant analytics
- Admin console for merchant status, offers, disputes, and support overrides
- Audit logging for manual adjustments
- Merchant quality checklist workflow
- Manual approval gate for live status
- Stale-offer suppression controls

### Manual Or Operational During Pilot
- Merchant sourcing and onboarding in Paris
- Offer setup and validation
- Content curation to keep feed relevant
- Quality checks on listings and merchant details
- Customer support for redemption issues
- Outreach to merchants and initial users
- Micro-market selection and inventory balancing
- Manual review of active/inactive merchant status
- Manual verification of repeat visits when needed
- Dispute resolution for failed redemptions

### Deferred Until After Proof
- Self-serve merchant portal
- Advanced personalization
- Reviews and social features
- Event discovery feed
- Multi-city rollout
- Paid merchant tools and campaigns
- Cross-merchant rewards
- Automated offer optimization
- Broad category expansion
- Multiple redemption paths
- Full merchant CRM tooling

## Business Model Hypothesis
Primary hypothesis:
- Charge merchants a simple monthly subscription for visibility, offers, and basic retention tools once the product proves it can drive visits.

Secondary hypothesis:
- Later add premium analytics or promoted placements, but only after proving merchant ROI and user engagement.

For the pilot, the objective is not monetization optimization; it is validating willingness to pay after measurable foot traffic and repeat visits.

## Critical Assumptions
- Users will trust the app enough to try a local recommendation instead of using Google Maps.
- Enough independent businesses in one fixed Paris micro-market will participate.
- Coffee and lunch use cases can generate enough repeat use to create habit.
- Offers and loyalty rewards will be compelling enough to change behavior.
- The app can keep recommendations relevant without a large inventory.
- Merchants will see value in simple visit and repeat-visit tracking.
- The redemption flow can be made simple and reliable.
- The experience can avoid looking like a noisy coupon directory.

## How To Test Quickly
- Run a concierge pilot in one fixed Paris micro-market with 20–30 independent businesses.
- Manually curate a small set of merchants in coffee and lunch.
- Launch a limited beta focused on “where should I go nearby?”
- Track:
  - app opens
  - listing clicks
  - offer redemptions
  - repeat visits
  - merchant willingness to continue
- Interview users after visits to understand what made them choose the business.
- Interview merchants to determine whether the app delivered incremental traffic or retention.

## Acceptance Criteria
- A user can find a relevant nearby independent business in under 30 seconds.
- A merchant profile clearly shows location, offer, and reason to visit.
- The one-time token redemption flow works reliably with minimal staff confusion.
- A required merchant quality checklist is completed before activation for every live merchant.
- At least 20 participating businesses are active in the pilot area.
- Users can redeem an offer or loyalty reward without support intervention in most cases.
- Merchants can see basic activity metrics.
- A meaningful share of users return for a second visit to the same merchant within a short test window.
- Pilot results show enough repeat visits and redemptions to justify continued investment.

## Risks And Failure Modes
- Poor supply density makes the app feel empty [supply_density]
- Recommendations are too generic and users revert to Google Maps [recommendation_quality]
- Merchants do not see enough ROI to stay active [merchant_roi]
- Offers attract deal-seekers who do not convert into repeat customers [low_quality_traffic]
- Manual curation does not scale beyond the pilot [ops_scalability]
- Redemption friction causes failure at the point of visit [redemption_friction]
- The product becomes another irrelevant local listing app [category_blur]
- Quality control is too burdensome and slows supply activation [quality_assurance]

## Product Readiness
Status: LIMITED

Blocking Gaps:
- No proof yet that curated local discovery changes user behavior in Paris [demand_validation]
- No proof yet that merchants will provide enough quality inventory and continue participation [supply_validation]
- No proof yet that the one-time token redemption flow and verified loyalty tracking work reliably in live use [redemption_friction]

Required Improvements:
- Run a concierge pilot with real users and merchants in one fixed Paris micro-market [concierge_pilot]
- Validate repeat visit and redemption behavior with coffee and lunch only [behavior_proof]
- Confirm merchant willingness to continue after initial traffic testing [merchant_roi]

## Recommendation
Proceed with a tightly scoped Paris concierge pilot.

Do not build a broad marketplace yet. The right next step is to prove one repeatable use case: nearby independent business discovery with a simple offer and verified loyalty loop.

If pilot results show weak user pull or merchant retention, stop or re-scope before expanding beyond a few neighborhoods.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Manual supply gating before publish [quality_assurance]
- Single redemption model [quality_assurance]
- Merchant quality checklist as a required publish gate [quality_assurance]
- Explicit redemption token lifecycle in the admin workflow [quality_assurance]
- One ops-approved live state with no self-serve publishing [quality_assurance]
- Stale-offer suppression so inactive merchants do not appear in feed [quality_assurance]
- Audit log for every manual override, publish, and dispute action [quality_assurance]
- One named Paris micro-market for the pilot [market_motion]
- Narrow first audience to frequent coffee/lunch decision-makers in that micro-market [market_motion]
- First category pair limited to coffee and lunch [scope]
- Concrete pilot success threshold tied to repeat visits and redemptions [demand_validation]
- Manual approval required before any merchant goes live [quality_assurance]

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
