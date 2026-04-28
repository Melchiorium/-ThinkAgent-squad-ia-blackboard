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

### untagged
- enough merchant supply in one launch neighborhood is unproven
- repeat-use value versus existing discovery apps is not yet proven

### onboarding
- [onboarding] the exact launch city and neighborhood boundary are not yet locked

## Product Required Improvements

### untagged
- recruit and activate a minimum merchant set in one specific neighborhood before consumer launch
- confirm that curated discovery plus loyalty creates repeat visits better than a map search baseline

### onboarding
- [onboarding] lock one pilot city and one bounded neighborhood corridor before expanding the build

## Tech Status

LIMITED


## Tech Blocking Gaps

### operations
- [operations] City inventory and merchant verification process are not yet operationally defined.
- [operations] Redemption confirmation method is not fixed to a single reliable workflow.

### privacy_trust
- [privacy_trust] Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation.

## Tech Required Improvements

### onboarding
- [onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.

### operations
- [operations] Choose one redemption mechanism and remove fallback complexity from MVP scope.

### untagged
- Specify immutable redemption and loyalty event storage with admin-only corrections.

## Growth Status

LIMITED


## Growth Blocking Gaps

### onboarding
- [onboarding] Launch corridor and minimum merchant density are not locked

### demand_validation
- [demand_validation] Redemptions-per-merchant and repeat-redemption thresholds are not defined
- [demand_validation] One real-world redemption flow has not been validated with staff

### metrics_validation
- [metrics_validation] The launch proof metric is still vague rather than behavioral

## Growth Required Improvements

### onboarding
- [onboarding] Lock one neighborhood/corridor and the minimum active merchant count before public launch

### metrics_validation
- [metrics_validation] Define a launch-proof metric using redemptions per active merchant and repeat redemption rate within a fixed window

### demand_validation
- [demand_validation] Validate one friction-light redemption method with actual merchants under checkout conditions

### market_motion
- [market_motion] Use the pilot to prove that curated discovery plus loyalty creates repeat use better than map search

## Global Status

LIMITED


## Global Blocking Gaps

### untagged
- enough merchant supply in one launch neighborhood is unproven
- repeat-use value versus existing discovery apps is not yet proven

### onboarding
- [onboarding] the exact launch city and neighborhood boundary are not yet locked
- [onboarding] Launch corridor and minimum merchant density are not locked

### operations
- [operations] City inventory and merchant verification process are not yet operationally defined.
- [operations] Redemption confirmation method is not fixed to a single reliable workflow.

### privacy_trust
- [privacy_trust] Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation.

### demand_validation
- [demand_validation] Redemptions-per-merchant and repeat-redemption thresholds are not defined
- [demand_validation] One real-world redemption flow has not been validated with staff

### metrics_validation
- [metrics_validation] The launch proof metric is still vague rather than behavioral

## Global Required Improvements

### untagged
- recruit and activate a minimum merchant set in one specific neighborhood before consumer launch
- confirm that curated discovery plus loyalty creates repeat visits better than a map search baseline
- Specify immutable redemption and loyalty event storage with admin-only corrections.

### onboarding
- [onboarding] lock one pilot city and one bounded neighborhood corridor before expanding the build
- [onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.
- [onboarding] Lock one neighborhood/corridor and the minimum active merchant count before public launch

### operations
- [operations] Choose one redemption mechanism and remove fallback complexity from MVP scope.

### metrics_validation
- [metrics_validation] Define a launch-proof metric using redemptions per active merchant and repeat redemption rate within a fixed window

### demand_validation
- [demand_validation] Validate one friction-light redemption method with actual merchants under checkout conditions

### market_motion
- [market_motion] Use the pilot to prove that curated discovery plus loyalty creates repeat use better than map search

## Known Tags

- metrics_validation
- demand_validation
- untagged
- onboarding
- operations
- privacy_trust
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

#### Product Task

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


## Contributors

- tech


#### Product Task

## Task

Clarify the narrowest credible product decision needed to close the concern.


## Source Gap

enough merchant supply in one launch neighborhood is unproven repeat-use value versus existing discovery apps is not yet proven recruit and activate a minimum merchant set in one specific neighborhood test whether curated discovery plus loyalty drives repeat visits better than map search Specify immutable redemption and loyalty event storage with admin-only corrections. Neighbourhood-level merchant density is unproven The switching trigger versus existing discovery apps is still soft Lock one launch neighborhood and define the minimum live merchant threshold Prove that at least a small set of users return after first redemption


## Expected Output

A clear product decision or a credible reduction path for the blocker.


## Contributors

- tech
- growth


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] one standard redemption method is not yet validated with staff validate one friction-light redemption flow that merchants will actually use The redemption-to-repeat-use loop is not yet validated Validate one friction-light redemption workflow with real merchants


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Contributors

_Aucun contributeur._


### Loop 2

#### Product Task

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] the exact launch neighborhood boundary is not yet locked lock one city and one neighborhood boundary before building additional launch coverage Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


## Contributors

- tech


#### Product Task

## Task

Clarify the narrowest credible product decision needed to close the concern.


## Source Gap

enough merchant supply in one launch neighborhood is unproven repeat-use value versus existing discovery apps is not yet proven recruit and activate a minimum merchant set in one specific neighborhood test whether curated discovery plus loyalty drives repeat visits better than map search Specify immutable redemption and loyalty event storage with admin-only corrections.


## Expected Output

A clear product decision or a credible reduction path for the blocker.


## Contributors

- tech


#### Growth Task

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] one standard redemption method is not yet validated with staff validate one friction-light redemption flow that merchants will actually use The launch neighborhood merchant base is not yet proven dense enough to sustain repeat consumer use. The first redemption flow is not yet validated with real merchants under actual checkout conditions. The demand signal is still vague; the team needs a specific behavioral threshold for repeat use and redemption. Recruit and activate a minimum merchant set in one named neighborhood before public launch. Define and track a launch proof metric based on redemptions per active merchant and repeat redemption rate within a fixed window.


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

### untagged
- enough merchant supply in one launch neighborhood is unproven
- repeat-use value versus existing discovery apps is not yet proven
- Neighbourhood-level merchant density is unproven
- The switching trigger versus existing discovery apps is still soft

### demand_validation
- [demand_validation] one standard redemption method is not yet validated with staff
- [demand_validation] The redemption-to-repeat-use loop is not yet validated

### operations
- [operations] City inventory and merchant verification process are not yet operationally defined.
- [operations] Redemption confirmation method is not fixed to a single reliable workflow.

### privacy_trust
- [privacy_trust] Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation.

## Global Required Improvements

### untagged
- recruit and activate a minimum merchant set in one specific neighborhood
- test whether curated discovery plus loyalty drives repeat visits better than map search
- Specify immutable redemption and loyalty event storage with admin-only corrections.
- Lock one launch neighborhood and define the minimum live merchant threshold
- Prove that at least a small set of users return after first redemption

### demand_validation
- [demand_validation] validate one friction-light redemption flow that merchants will actually use
- [demand_validation] Validate one friction-light redemption workflow with real merchants

### onboarding
- [onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.

### operations
- [operations] Choose one redemption mechanism and remove fallback complexity from MVP scope.

## Loop Tasks

##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


##### Product

## Task

Clarify the narrowest credible product decision needed to close the concern.


## Source Gap

enough merchant supply in one launch neighborhood is unproven repeat-use value versus existing discovery apps is not yet proven recruit and activate a minimum merchant set in one specific neighborhood test whether curated discovery plus loyalty drives repeat visits better than map search Specify immutable redemption and loyalty event storage with admin-only corrections. Neighbourhood-level merchant density is unproven The switching trigger versus existing discovery apps is still soft Lock one launch neighborhood and define the minimum live merchant threshold Prove that at least a small set of users return after first redemption


## Expected Output

A clear product decision or a credible reduction path for the blocker.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] one standard redemption method is not yet validated with staff validate one friction-light redemption flow that merchants will actually use The redemption-to-repeat-use loop is not yet validated Validate one friction-light redemption workflow with real merchants


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

### untagged
- enough merchant supply in one launch neighborhood is unproven
- repeat-use value versus existing discovery apps is not yet proven

### demand_validation
- [demand_validation] one standard redemption method is not yet validated with staff
- [demand_validation] The launch neighborhood merchant base is not yet proven dense enough to sustain repeat consumer use.
- [demand_validation] The first redemption flow is not yet validated with real merchants under actual checkout conditions.
- [demand_validation] The demand signal is still vague; the team needs a specific behavioral threshold for repeat use and redemption.

### onboarding
- [onboarding] the exact launch neighborhood boundary is not yet locked

### operations
- [operations] City inventory and merchant verification process are not yet operationally defined.
- [operations] Redemption confirmation method is not fixed to a single reliable workflow.

### privacy_trust
- [privacy_trust] Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation.

## Global Required Improvements

### untagged
- recruit and activate a minimum merchant set in one specific neighborhood
- test whether curated discovery plus loyalty drives repeat visits better than map search
- Specify immutable redemption and loyalty event storage with admin-only corrections.

### demand_validation
- [demand_validation] validate one friction-light redemption flow that merchants will actually use
- [demand_validation] Recruit and activate a minimum merchant set in one named neighborhood before public launch.
- [demand_validation] Define and track a launch proof metric based on redemptions per active merchant and repeat redemption rate within a fixed window.

### onboarding
- [onboarding] lock one city and one neighborhood boundary before building additional launch coverage
- [onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.

### operations
- [operations] Choose one redemption mechanism and remove fallback complexity from MVP scope.
- [operations] Test one friction-light redemption workflow with at least a handful of merchants and confirm staff can use it without friction.

## Loop Tasks

##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


##### Product

## Task

Clarify the narrowest credible product decision needed to close the concern.


## Source Gap

enough merchant supply in one launch neighborhood is unproven repeat-use value versus existing discovery apps is not yet proven recruit and activate a minimum merchant set in one specific neighborhood test whether curated discovery plus loyalty drives repeat visits better than map search Specify immutable redemption and loyalty event storage with admin-only corrections. Neighbourhood-level merchant density is unproven The switching trigger versus existing discovery apps is still soft Lock one launch neighborhood and define the minimum live merchant threshold Prove that at least a small set of users return after first redemption


## Expected Output

A clear product decision or a credible reduction path for the blocker.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] one standard redemption method is not yet validated with staff validate one friction-light redemption flow that merchants will actually use The redemption-to-repeat-use loop is not yet validated Validate one friction-light redemption workflow with real merchants


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

### untagged
- enough merchant supply in one launch neighborhood is unproven
- repeat-use value versus existing discovery apps is not yet proven

### demand_validation
- [demand_validation] one standard redemption method is not yet validated with staff
- [demand_validation] The launch neighborhood merchant base is not yet proven dense enough to sustain repeat consumer use.
- [demand_validation] The first redemption flow is not yet validated with real merchants under actual checkout conditions.
- [demand_validation] The demand signal is still vague; the team needs a specific behavioral threshold for repeat use and redemption.

### onboarding
- [onboarding] the exact launch neighborhood boundary is not yet locked

### operations
- [operations] City inventory and merchant verification process are not yet operationally defined.
- [operations] Redemption confirmation method is not fixed to a single reliable workflow.

### privacy_trust
- [privacy_trust] Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation.

## Global Required Improvements

### untagged
- recruit and activate a minimum merchant set in one specific neighborhood
- test whether curated discovery plus loyalty drives repeat visits better than map search
- Specify immutable redemption and loyalty event storage with admin-only corrections.

### demand_validation
- [demand_validation] validate one friction-light redemption flow that merchants will actually use
- [demand_validation] Recruit and activate a minimum merchant set in one named neighborhood before public launch.
- [demand_validation] Define and track a launch proof metric based on redemptions per active merchant and repeat redemption rate within a fixed window.

### onboarding
- [onboarding] lock one city and one neighborhood boundary before building additional launch coverage
- [onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.

### operations
- [operations] Choose one redemption mechanism and remove fallback complexity from MVP scope.
- [operations] Test one friction-light redemption workflow with at least a handful of merchants and confirm staff can use it without friction.

## Loop Tasks

##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] the exact launch neighborhood boundary is not yet locked lock one city and one neighborhood boundary before building additional launch coverage Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


##### Product

## Task

Clarify the narrowest credible product decision needed to close the concern.


## Source Gap

enough merchant supply in one launch neighborhood is unproven repeat-use value versus existing discovery apps is not yet proven recruit and activate a minimum merchant set in one specific neighborhood test whether curated discovery plus loyalty drives repeat visits better than map search Specify immutable redemption and loyalty event storage with admin-only corrections.


## Expected Output

A clear product decision or a credible reduction path for the blocker.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] one standard redemption method is not yet validated with staff validate one friction-light redemption flow that merchants will actually use The launch neighborhood merchant base is not yet proven dense enough to sustain repeat consumer use. The first redemption flow is not yet validated with real merchants under actual checkout conditions. The demand signal is still vague; the team needs a specific behavioral threshold for repeat use and redemption. Recruit and activate a minimum merchant set in one named neighborhood before public launch. Define and track a launch proof metric based on redemptions per active merchant and repeat redemption rate within a fixed window.


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

### untagged
- enough merchant supply in one launch neighborhood is unproven
- repeat-use value versus existing discovery apps is not yet proven

### onboarding
- [onboarding] the exact launch city and neighborhood boundary are not yet locked
- [onboarding] Launch corridor and minimum merchant density are not locked

### operations
- [operations] City inventory and merchant verification process are not yet operationally defined.
- [operations] Redemption confirmation method is not fixed to a single reliable workflow.

### privacy_trust
- [privacy_trust] Loyalty ledger and dispute handling rules are not specified tightly enough for trustworthy MVP operation.

### demand_validation
- [demand_validation] Redemptions-per-merchant and repeat-redemption thresholds are not defined
- [demand_validation] One real-world redemption flow has not been validated with staff

### metrics_validation
- [metrics_validation] The launch proof metric is still vague rather than behavioral

## Global Required Improvements

### untagged
- recruit and activate a minimum merchant set in one specific neighborhood before consumer launch
- confirm that curated discovery plus loyalty creates repeat visits better than a map search baseline
- Specify immutable redemption and loyalty event storage with admin-only corrections.

### onboarding
- [onboarding] lock one pilot city and one bounded neighborhood corridor before expanding the build
- [onboarding] Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.
- [onboarding] Lock one neighborhood/corridor and the minimum active merchant count before public launch

### operations
- [operations] Choose one redemption mechanism and remove fallback complexity from MVP scope.

### metrics_validation
- [metrics_validation] Define a launch-proof metric using redemptions per active merchant and repeat redemption rate within a fixed window

### demand_validation
- [demand_validation] Validate one friction-light redemption method with actual merchants under checkout conditions

### market_motion
- [market_motion] Use the pilot to prove that curated discovery plus loyalty creates repeat use better than map search

## Loop Tasks

##### Product

## Task

Clarify the smallest onboarding flow that still proves value.


## Source Gap

[onboarding] the exact launch neighborhood boundary is not yet locked lock one city and one neighborhood boundary before building additional launch coverage Define one pilot city, one neighborhood boundary, and a manual merchant approval pipeline.


## Expected Output

A clear product decision that keeps onboarding simple enough for proof.


##### Product

## Task

Clarify the narrowest credible product decision needed to close the concern.


## Source Gap

enough merchant supply in one launch neighborhood is unproven repeat-use value versus existing discovery apps is not yet proven recruit and activate a minimum merchant set in one specific neighborhood test whether curated discovery plus loyalty drives repeat visits better than map search Specify immutable redemption and loyalty event storage with admin-only corrections.


## Expected Output

A clear product decision or a credible reduction path for the blocker.


##### Growth

## Task

Clarify the clearest early demand signal and how it will be observed.


## Source Gap

[demand_validation] one standard redemption method is not yet validated with staff validate one friction-light redemption flow that merchants will actually use The launch neighborhood merchant base is not yet proven dense enough to sustain repeat consumer use. The first redemption flow is not yet validated with real merchants under actual checkout conditions. The demand signal is still vague; the team needs a specific behavioral threshold for repeat use and redemption. Recruit and activate a minimum merchant set in one named neighborhood before public launch. Define and track a launch proof metric based on redemptions per active merchant and repeat redemption rate within a fixed window.


## Expected Output

A concrete demand-validation approach with a signal threshold.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] **Curated supply, not open marketplace**
- [tech] Only approved merchants in one city/neighborhood cluster.
- [tech] No public merchant signup flow until the pilot proves supply quality.
- [tech] Prevents empty inventory and stale listings from undermining trust.

## Growth Structural Decisions

### growth
- [growth] Lock one specific launch neighborhood/corridor and define the minimum merchant count required to avoid an empty feed. [onboarding]
- [growth] Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]

## Product Locking

## Applied

True


## Confirmed In Scope

- one city
- one bounded launch neighborhood or corridor
- independent coffee shops and casual restaurants only
- curated merchant inventory with internal approval before publishing
- merchant verification and publishing workflow
- merchant profiles with hours, address, offer, and basic description
- rules-based feed using distance, open status, and category preference
- one standard redemption mechanism
- basic loyalty progress tracking
- append-only loyalty/redemption event log
- internal ops tools for stale offers, hours, and disputes
- verified merchant flag


## Confirmed Deferred

- reviews
- events
- advanced personalization
- cross-category expansion
- merchant self-serve onboarding
- richer loyalty programs
- payments
- booking
- multi-city tooling
- self-serve promotion products
- multiple redemption methods


## Confirmed Out Of Scope

- broad multi-category marketplace
- public self-serve merchant signup
- in-app payments
- delivery
- social sharing
- deep merchant analytics dashboard
- complex loyalty tiers or configurable loyalty rules
- large-scale coupon aggregation


## Locking Note

- Scope remains intentionally narrow and proof-oriented - No new features added in this locking pass - Operational support stays operational, not productized, except where required for trust and proof


## Expert Contributions

### Tech Summary

The main feasibility challenge is not the app itself but **keeping a city-local inventory of verified merchants, offers, and loyalty redemptions trustworthy enough to use**. The recommended direction is a tightly controlled pilot with curated supply, a simple redemption confirmation flow, and a lightweight ops console rather than a broad self-serve marketplace.

## Tech Structural Decisions

- **Curated supply, not open marketplace**
- Only approved merchants in one city/neighborhood cluster.
- No public merchant signup flow until the pilot proves supply quality.
- Prevents empty inventory and stale listings from undermining trust.


## Tech Recommendations

- Add an explicit **merchant verification and publishing workflow** with internal approval before any listing goes live. [onboarding]
- Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]


## Tech Risks

- Merchant participation may remain too sparse for the city-scoped feed to feel credible. [supply_density]
- Redemption may be too slow or confusing for merchant staff if the confirmation flow is not extremely simple. [workflow]
- Stale offers or wrong hours could damage trust quickly if ops review is weak. [data_quality]


## Tech Open Questions

- What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- What is the pilot city and the maximum geographic boundary for the first feed?


### Growth Summary

The core launch challenge is not building the app; it is proving that one neighborhood has enough dense, trustworthy merchant supply and that one redemption/loyalty loop is compelling enough to create repeat use. The best GTM path is a tightly controlled, founder-led pilot in a single corridor with coffee shops and casual restaurants only, using manual merchant acquisition and a simple verified redemption flow to prove demand before scaling.

## Growth Structural Decisions

- Lock one specific launch neighborhood/corridor and define the minimum merchant count required to avoid an empty feed. [onboarding]
- Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]


## Growth Recommendations

- Lock one specific launch neighborhood/corridor and define the minimum merchant count required to avoid an empty feed. [onboarding]
- Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]


## Growth Risks

- merchant density is too thin to produce a useful feed
- users treat the app like a one-time coupon app and do not return
- the redemption flow is too awkward for staff to use consistently


## Growth Open Questions

- What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Which single redemption flow has been validated with merchants and staff as lowest friction?
- What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?


## Product Arbitration

## Source

heuristic_fallback


## Retained

_Aucun élément retenu._


## Deferred

- Tech: Add an explicit **merchant verification and publishing workflow** with internal approval before any listing goes live. [onboarding]
- Growth: Lock one specific launch neighborhood/corridor and define the minimum merchant count required to avoid an empty feed. [onboarding]


## Rejected

- Tech: Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Tech: Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]
- Growth: Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Growth: Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Growth: Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Growth: Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]


## Open Points

- Tech: Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Tech: Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Tech: What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Tech: Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- Tech: What is the pilot city and the maximum geographic boundary for the first feed?
- Growth: What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Growth: Which single redemption flow has been validated with merchants and staff as lowest friction?
- Growth: What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?
- Tech recommendation needing arbitration: Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Tech recommendation needing arbitration: Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Tech recommendation needing arbitration: Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Tech recommendation needing arbitration: Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]
- Growth recommendation needing arbitration: Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Growth recommendation needing arbitration: Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Growth recommendation needing arbitration: Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Growth recommendation needing arbitration: Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]
- Tech open question: What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Tech open question: Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- Tech open question: What is the pilot city and the maximum geographic boundary for the first feed?
- Growth open question: What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Growth open question: Which single redemption flow has been validated with merchants and staff as lowest friction?
- Growth open question: What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local businesses still default to large platforms because local discovery is fragmented, time-consuming, and hard to trust. Independent businesses need a way to get found and retain nearby customers without running full marketing campaigns.

The product must prove one narrow value loop: a nearby user can quickly discover a relevant local business deal and return to the business again via a simple loyalty mechanism.

## Initial Wedge
A city-specific mobile app for discovering nearby independent coffee shops and casual restaurants with verified promotions and a simple stamp-style loyalty reward.

This is the narrowest credible wedge because:
- it has frequent repeat behavior
- offers are easy to understand
- loyalty can demonstrate retention value
- supply can be concentrated in one neighborhood or one city

## First Target User
Urban young professionals in one city who want convenient nearby places to eat or get coffee and are open to supporting local businesses if the option is easy and worthwhile.

Secondary beneficiary, not the initial target:
- independent coffee shops and casual restaurants in the same city

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Apple Maps for nearby discovery
- Yelp for reviews and browsing
- Instagram or TikTok for local promotion discovery
- business websites or walk-in discovery for loyalty and offers
- generic coupon apps for deals

Switching trigger:
- users switch when LocalLoop makes local discovery faster and more personally relevant than general apps, and when the offer + loyalty loop gives a clear reason to return
- businesses switch participation when they can reach nearby customers with minimal setup and see repeat visits without running campaigns themselves

## Core MVP Workflow
1. User opens the app and sees nearby independent coffee shops and casual restaurants.
2. The app shows a small set of personalized recommendations based on location and basic preferences.
3. User taps a merchant profile to see the offer, hours, and a simple reason to visit.
4. User redeems an offer in-store or through a merchant-generated code/confirmation.
5. The merchant records the visit and stamps the loyalty reward.
6. The app surfaces the remaining progress toward a reward on the next visit.

## In Scope
- city- and neighborhood-level discovery
- one merchant category to start: coffee shops and casual restaurants
- merchant profiles with hours, address, offer, and basic description
- simple location-based recommendations
- promotional offers from participating merchants
- basic loyalty tracking tied to repeat visits
- lightweight onboarding for merchants
- basic trust signals such as verified merchant status
- minimal filtering to avoid irrelevant offers

## Out of Scope
- broad multi-category marketplace
- events feed
- reviews and ratings system
- social sharing
- advanced personalization or ML ranking
- multi-city launch
- deep merchant analytics dashboard
- self-serve ad products
- in-app payments
- delivery or booking
- large-scale coupon aggregation
- full loyalty ecosystem across all merchant types

## MVP Build Vs Pilot Operations
### Must Build Now
- nearby merchant discovery feed
- merchant profile page
- offer display and redemption flow
- basic loyalty stamp/progress tracking
- simple onboarding for merchants
- verified merchant flag
- location filtering and category filtering

### Manual Or Operational During Pilot
- recruiting the first merchant set
- approving and uploading offers
- verifying merchant participation
- resolving redemption issues
- curating the first city/neighborhood inventory
- quality control for irrelevant or stale offers

### Deferred Until After Proof
- reviews
- event discovery
- advanced recommendations
- cross-category expansion
- merchant self-serve campaign tools
- richer loyalty rules
- payments
- broader personalization
- multi-city scaling tools

## Business Model Hypothesis
Primary hypothesis:
- merchants pay a small monthly fee or per-location subscription for inclusion, promotion placement, and loyalty participation
- alternatively, the pilot may test a low-cost lead or redemption-based fee if merchants resist subscription

The model should only be considered viable if merchants see repeat visits or measurable redemptions without needing extra operational effort.

## Critical Assumptions
- enough local businesses in one city will participate to create useful supply
- nearby users care enough about independent businesses to try a dedicated app
- simple offers plus loyalty are enough to drive repeat behavior
- merchants will accept a lightweight workflow for redemption tracking
- the app can maintain relevance without broad marketplace coverage
- users will choose this over Google Maps/Yelp for this narrow use case

## How To Test Quickly
- launch in one city and one neighborhood cluster
- recruit a small set of coffee shops and casual restaurants manually
- offer one simple promotion format and one loyalty mechanic
- measure whether users open the app repeatedly and redeem offers
- track whether merchants see return visits and want to continue after the pilot
- test whether curated recommendations outperform a plain nearby list in engagement

## Acceptance Criteria
- a user can find a nearby participating merchant in under 30 seconds
- a merchant profile clearly shows offer, location, and hours
- a redemption can be completed with a simple merchant-side confirmation
- loyalty progress is visible to the user after redemption
- at least a small initial set of merchants is live in one city
- stale or irrelevant offers are removable quickly
- pilot users demonstrate repeat opens and redemptions
- participating merchants can complete setup without significant support burden

## Risks And Failure Modes
- insufficient merchant supply makes the app feel empty
- recommendation quality is too weak to beat existing apps
- users treat it as a coupon app and do not return
- merchants do not see enough incremental value to stay
- manual curation burden becomes too high
- loyalty does not create meaningful repeat behavior
- narrow category focus may limit early appeal but is necessary for proof

## Product Readiness
Status: LIMITED

Blocking Gaps:
- merchant supply in one city is unproven [supply_density]
- redemption and loyalty mechanics may be too weak to drive repeat use [retention_loop]
- differentiation versus existing discovery apps is not yet validated [switching_trigger]

Required Improvements:
- recruit and activate a small merchant cohort in one neighborhood [merchant_onboarding]
- define one friction-light redemption method that merchants will actually use [redemption_flow]
- test whether the app creates measurable repeat visits versus basic map search [value_proof]

## Recommendation
Proceed with a tightly scoped pilot in one city focused only on coffee shops and casual restaurants with a simple offer-plus-loyalty loop. Do not expand to reviews, events, or broad multi-category discovery until the pilot proves users repeatedly choose LocalLoop over general-purpose alternatives and merchants see enough repeat value to continue.

## Retained Decisions

_Aucune décision retenue._

## Deferred Decisions

- Tech: Add an explicit **merchant verification and publishing workflow** with internal approval before any listing goes live. [onboarding]
- Growth: Lock one specific launch neighborhood/corridor and define the minimum merchant count required to avoid an empty feed. [onboarding]

## Rejected Recommendations

- Tech: Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Tech: Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]
- Growth: Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Growth: Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Growth: Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Growth: Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]

## Unresolved Tensions

- Tech recommendation needing arbitration: Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Tech recommendation needing arbitration: Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Tech recommendation needing arbitration: Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Tech recommendation needing arbitration: Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]
- Growth recommendation needing arbitration: Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Growth recommendation needing arbitration: Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Growth recommendation needing arbitration: Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Growth recommendation needing arbitration: Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]
- Tech open question: What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Tech open question: Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- Tech open question: What is the pilot city and the maximum geographic boundary for the first feed?
- Growth open question: What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Growth open question: Which single redemption flow has been validated with merchants and staff as lowest friction?
- Growth open question: What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?

## Applied Changes

_Aucun changement appliqué._

## Remaining Open Points

- Tech: Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Tech: Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Tech: What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Tech: Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- Tech: What is the pilot city and the maximum geographic boundary for the first feed?
- Growth: What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Growth: Which single redemption flow has been validated with merchants and staff as lowest friction?
- Growth: What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?
- Tech recommendation needing arbitration: Define one **single redemption mechanism** for the MVP, such as QR or staff code confirmation, and remove alternatives from the first release. [workflow]
- Tech recommendation needing arbitration: Add an **ops console requirement** for suspending stale offers, correcting hours, and resolving redemption disputes. [ops_tooling]
- Tech recommendation needing arbitration: Specify that the recommendation feed is **rules-based** with distance, open status, and category preference only. [ranking]
- Tech recommendation needing arbitration: Add an **append-only loyalty ledger** and audit trail so stamps cannot be edited without trace. [audit_log]
- Growth recommendation needing arbitration: Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Growth recommendation needing arbitration: Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Growth recommendation needing arbitration: Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Growth recommendation needing arbitration: Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]
- Tech open question: What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Tech open question: Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- Tech open question: What is the pilot city and the maximum geographic boundary for the first feed?
- Growth open question: What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Growth open question: Which single redemption flow has been validated with merchants and staff as lowest friction?
- Growth open question: What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?

## Risks

- Merchant participation may remain too sparse for the city-scoped feed to feel credible. [supply_density]
- Redemption may be too slow or confusing for merchant staff if the confirmation flow is not extremely simple. [workflow]
- Stale offers or wrong hours could damage trust quickly if ops review is weak. [data_quality]
- The inventory may be too thin to create consumer habit [supply_density]
- Merchants may not see enough incremental visits to renew [value_proof]
- The app may be perceived as a coupon list rather than a discovery product [positioning]
- merchant supply in the launch zone is too thin to feel useful
- the app is still weaker than Google Maps/Yelp for the first use case
- users treat it as a one-time deal app and do not return
- merchant density is too thin to produce a useful feed
- users treat the app like a one-time coupon app and do not return
- the redemption flow is too awkward for staff to use consistently

## Open Questions

- What exact redemption mechanism will merchant staff use in-store: QR scan, code entry, or staff button?
- Will users need full accounts at first, or can the app support guest browsing with account creation only at redemption?
- What is the pilot city and the maximum geographic boundary for the first feed?
- Which exact neighborhood will be the first launch zone? [supply_density]
- How many merchants are needed before the consumer app is worth opening? [supply_density]
- Will redemption be handled by code, stamp, QR, or staff confirmation? [redemption_flow]
- What exact threshold of active merchants is enough to make the neighborhood feed feel alive?
- Which one redemption method is simplest enough for staff to reliably use without training?
- Is the first wedge coffee-only, or coffee plus casual lunch?
- What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Which single redemption flow has been validated with merchants and staff as lowest friction?
- What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local businesses default to Google Maps, Yelp, and social platforms because local discovery is fragmented and hard to trust. Independent businesses need a simple way to get discovered and drive repeat visits, but they cannot afford broad digital marketing tools.

The MVP must prove one narrow loop: a user can discover a relevant nearby independent business, redeem a verified offer, and return again through a simple loyalty mechanism.

## Initial Wedge
A founder-curated pilot in one city and one bounded neighborhood corridor, focused only on independent coffee shops and casual restaurants with verified offers and one loyalty reward path.

This is the narrowest credible wedge because:
- it supports frequent repeat visits
- offers are simple to understand and verify
- loyalty can prove retention value
- inventory can be controlled in a dense local area

## First Target User
Primary target:
- urban young professionals in the launch neighborhood who regularly buy coffee or casual meals and are open to trying independent businesses if discovery is easy

Secondary beneficiary, not the initial target:
- independent coffee shops and casual restaurants in the same launch area

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Apple Maps for nearby discovery
- Yelp for browsing and reviews
- Instagram / TikTok for local promotions
- walk-in discovery and business websites for offers and loyalty
- generic coupon apps for discounts

Switching trigger:
- users switch when LocalLoop is more relevant than general maps for this narrow local use case
- merchants join when they get nearby foot traffic and repeat visits without running campaigns
- the app must feel curated, not like another empty local directory

## Core MVP Workflow
1. A user opens the app and sees a curated feed of nearby participating businesses.
2. The feed is filtered by distance, open status, and basic category preference.
3. The user opens a merchant profile to see hours, address, offer, and a short reason to visit.
4. The user redeems the offer using one standard in-store confirmation method.
5. The merchant confirms the redemption and the app records one loyalty stamp in an append-only history.
6. The user can see progress toward the next reward on the merchant profile.

## In Scope
- one city
- one launch neighborhood or corridor with a clearly defined geographic boundary
- independent coffee shops and casual restaurants only
- curated merchant inventory with internal approval before publishing
- merchant profiles with hours, address, offer, and basic description
- rules-based feed using distance, open status, and category preference
- one standard redemption mechanism
- basic loyalty progress tracking
- verified merchant status
- append-only loyalty/redemption event storage with admin-only corrections
- internal ops tools to suspend stale offers and correct listing details
- manual merchant onboarding support for the pilot
- minimal filtering to avoid stale or irrelevant offers

## Out of Scope
- reviews and ratings
- events feed
- broad multi-category marketplace
- advanced personalization or ML ranking
- public self-serve merchant signup
- self-serve ad products
- in-app payments
- delivery or booking
- cross-city launch
- social sharing
- deep merchant analytics dashboard
- complex loyalty tiers or configurable loyalty rules
- large-scale coupon aggregation
- multiple redemption methods

## MVP Build Vs Pilot Operations
### Must Build Now
- curated nearby discovery feed
- merchant profile page
- one redemption confirmation flow
- loyalty stamp/progress tracking
- merchant verification and publishing workflow
- internal ops console for stale offers, hours, and disputes
- verified merchant flag
- append-only loyalty/redemption event log
- basic category and distance filtering

### Manual Or Operational During Pilot
- recruit the first merchants
- approve offers before publishing
- verify merchant identity and participation
- curate the initial neighborhood inventory
- resolve redemption disputes
- remove stale or poor-quality listings
- support merchant setup and corrections
- maintain the minimum active merchant set in the launch neighborhood

### Deferred Until After Proof
- reviews
- events
- advanced personalization
- cross-category expansion
- merchant self-serve onboarding
- richer loyalty programs
- payments
- booking
- multi-city tooling
- self-serve promotion products

## Business Model Hypothesis
Primary hypothesis:
- participating merchants pay a small monthly subscription per location for verified listing placement, offers, and loyalty participation

Secondary fallback hypothesis:
- a low-cost pilot fee tied to participation or redemptions may be easier to test if subscription resistance is high

The business model is only credible if merchants see repeat visits and low-effort visibility without needing ongoing hands-on marketing support.

## Critical Assumptions
- one neighborhood has enough high-quality merchant supply to feel useful
- users will try a dedicated local discovery app for a narrow, frequent use case
- curated offers plus loyalty create a reason to return
- merchants will tolerate a lightweight redemption process
- the app can stay trustworthy with curated inventory and internal approval
- LocalLoop can beat Google Maps or Yelp for this specific wedge

## How To Test Quickly
- launch in one dense neighborhood or corridor
- recruit a small set of coffee shops and casual restaurants manually
- use one offer format and one redemption method
- track whether users open the app repeatedly and redeem offers
- measure whether merchants see repeat visits and want to continue
- compare engagement against a simple nearby list to validate curation value
- remove stale offers quickly and observe whether trust holds
- require an admin-only correction path for redemption and loyalty records before pilot launch

## Acceptance Criteria
- the pilot is limited to one city and one clearly bounded neighborhood or corridor
- a user can find a nearby participating merchant in under 30 seconds
- merchant profiles clearly show offer, hours, and address
- only approved merchants can go live
- one redemption can be completed with a simple staff confirmation flow
- loyalty progress is visible immediately after redemption
- redemption and loyalty events are stored in an append-only log with admin-only correction capability
- stale offers and hours can be corrected or suspended quickly
- the pilot neighborhood has enough active supply to avoid an empty feed
- users demonstrate repeat opens and redemptions during the pilot
- merchants can participate without heavy ongoing support

## Risks And Failure Modes
- merchant supply is too thin to make the app feel useful
- curated feed quality is not better than Google Maps or Yelp
- users treat the app like a one-time coupon app and do not return
- merchants do not see enough incremental value to stay
- manual curation and support become too heavy
- loyalty does not materially improve repeat behavior
- trust breaks if stale offers, hours, or redemption records are not controlled tightly

## Product Readiness
Status: LIMITED

Blocking Gaps:
- enough merchant supply in one launch neighborhood is unproven [supply_density]
- repeat-use value versus existing discovery apps is not yet proven [value_proof]
- the exact launch city and neighborhood boundary are not yet locked [onboarding]

Required Improvements:
- recruit and activate a minimum merchant set in one specific neighborhood before consumer launch [supply_density]
- confirm that curated discovery plus loyalty creates repeat visits better than a map search baseline [value_proof]
- lock one pilot city and one bounded neighborhood corridor before expanding the build [onboarding]

## Recommendation
Proceed with a tightly controlled pilot in one neighborhood focused only on independent coffee shops and casual restaurants. Build the smallest product that can prove curated discovery, verified redemption, and repeat visitation. Keep reviews, events, advanced personalization, broad category expansion, and open merchant self-serve out of the MVP until the pilot shows clear merchant demand and repeat consumer usage.

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
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
