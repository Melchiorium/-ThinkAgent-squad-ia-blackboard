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
- Verified merchant density in one neighborhood is unproven

### demand_validation
- [demand_validation] Consumer demand for a curated local discovery app remains unproven
- [demand_validation] The single redemption flow has not been validated in live merchant settings

### metrics_validation
- [metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data

## Product Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and a small merchant set

### untagged
- Finalize and test one redemption mechanism before launch

### metrics_validation
- [metrics_validation] Validate that users return after one successful visit or reward

### operations
- [operations] Confirm the launch neighborhood can support enough approved merchants before public consumer rollout

## Tech Status

LIMITED


## Tech Blocking Gaps

### untagged
- The redemption mechanism is not defined tightly enough to build a reliable proof loop
- Merchant approval and listing controls need a concrete state model before implementation

### scope
- [scope] The MVP recommendation model is too broad for the available supply and operations model

## Tech Required Improvements

### scope
- [scope] Select one deterministic redemption method and make it the only supported MVP path
- [scope] Replace advanced personalization with rules-based curation and explicit user filters

### untagged
- Define merchant lifecycle states, approval rules, and immediate disable controls

## Growth Status

LIMITED


## Growth Blocking Gaps

### market_motion
- [market_motion] Primary acquisition motion is still not concrete enough to test in-market

### demand_validation
- [demand_validation] Smallest credible launch audience is not yet tied to a measurable launch threshold

### untagged
- Merchant supply density required for credible consumer launch is unproven

## Growth Required Improvements

### market_motion
- [market_motion] Define and pilot one acquisition motion: founder-led merchant seeding plus merchant-distributed invites

### untagged
- Set a minimum neighborhood merchant count before consumer launch

### demand_validation
- [demand_validation] Narrow the first audience to frequent neighborhood coffee/lunch buyers who can be reached through merchants

## Global Status

LIMITED


## Global Blocking Gaps

### untagged
- Verified merchant density in one neighborhood is unproven
- The redemption mechanism is not defined tightly enough to build a reliable proof loop
- Merchant approval and listing controls need a concrete state model before implementation
- Merchant supply density required for credible consumer launch is unproven

### demand_validation
- [demand_validation] Consumer demand for a curated local discovery app remains unproven
- [demand_validation] The single redemption flow has not been validated in live merchant settings
- [demand_validation] Smallest credible launch audience is not yet tied to a measurable launch threshold

### metrics_validation
- [metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data

### scope
- [scope] The MVP recommendation model is too broad for the available supply and operations model

### market_motion
- [market_motion] Primary acquisition motion is still not concrete enough to test in-market

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and a small merchant set
- [market_motion] Define and pilot one acquisition motion: founder-led merchant seeding plus merchant-distributed invites

### untagged
- Finalize and test one redemption mechanism before launch
- Define merchant lifecycle states, approval rules, and immediate disable controls
- Set a minimum neighborhood merchant count before consumer launch

### metrics_validation
- [metrics_validation] Validate that users return after one successful visit or reward

### operations
- [operations] Confirm the launch neighborhood can support enough approved merchants before public consumer rollout

### scope
- [scope] Select one deterministic redemption method and make it the only supported MVP path
- [scope] Replace advanced personalization with rules-based curation and explicit user filters

### demand_validation
- [demand_validation] Narrow the first audience to frequent neighborhood coffee/lunch buyers who can be reached through merchants

## Known Tags

- untagged
- metrics_validation
- scope
- operations
- market_motion
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

#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a concierge pilot with real users and a small merchant set Run a concierge pilot with a tightly defined merchant set and real users before expanding scope


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Validate that users return after one successful visit or reward Prove repeat usage after one successful local visit or reward


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


#### Product Task

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] The MVP recommendation model is too broad for the available supply and operations model Select one deterministic redemption method and make it the only supported MVP path Replace advanced personalization with rules-based curation and explicit user filters


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Contributors

- tech


### Loop 2

#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a concierge pilot with real users and a small merchant set The primary acquisition motion is not yet specified in a way that can be tested Lock one acquisition motion: founder-led merchant seeding plus merchant-distributed invites


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data Validate that users return after one successful visit or reward Merchant density and active promotion thresholds are not defined Set a minimum pilot threshold for active merchants and first redemptions before public launch


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


#### Product Task

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] The MVP recommendation model is too broad for the available supply and operations model Select one deterministic redemption method and make it the only supported MVP path Replace advanced personalization with rules-based curation and explicit user filters The smallest credible launch audience is still too broad for a proof-oriented pilot Narrow launch audience to frequent neighborhood coffee/lunch buyers who live or work locally


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Contributors

- tech
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

### untagged
- Verified merchant density in one neighborhood is unproven
- The redemption mechanism is not defined tightly enough to build a reliable proof loop
- Merchant approval and listing controls need a concrete state model before implementation
- Verified merchant density in one neighborhood is still unproven

### demand_validation
- [demand_validation] Consumer demand for a curated local discovery app remains unproven
- [demand_validation] The single redemption flow has not been validated in live merchant settings
- [demand_validation] Consumer willingness to adopt a new discovery habit is still unproven
- [demand_validation] The live redemption workflow is not yet validated in store conditions

### scope
- [scope] The MVP recommendation model is too broad for the available supply and operations model

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and a small merchant set
- [market_motion] Run a concierge pilot with a tightly defined merchant set and real users before expanding scope

### untagged
- Finalize and test one redemption mechanism before launch
- Define merchant lifecycle states, approval rules, and immediate disable controls
- Finalize the simplest redemption method and test it with actual merchants

### metrics_validation
- [metrics_validation] Validate that users return after one successful visit or reward
- [metrics_validation] Prove repeat usage after one successful local visit or reward

### scope
- [scope] Select one deterministic redemption method and make it the only supported MVP path
- [scope] Replace advanced personalization with rules-based curation and explicit user filters

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a concierge pilot with real users and a small merchant set Run a concierge pilot with a tightly defined merchant set and real users before expanding scope


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Validate that users return after one successful visit or reward Prove repeat usage after one successful local visit or reward


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] The MVP recommendation model is too broad for the available supply and operations model Select one deterministic redemption method and make it the only supported MVP path Replace advanced personalization with rules-based curation and explicit user filters


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


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
- Verified merchant density in one neighborhood is unproven
- The redemption mechanism is not defined tightly enough to build a reliable proof loop
- Merchant approval and listing controls need a concrete state model before implementation

### demand_validation
- [demand_validation] Consumer demand for a curated local discovery app remains unproven
- [demand_validation] The single redemption flow has not been validated in live merchant settings

### metrics_validation
- [metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data
- [metrics_validation] Merchant density and active promotion thresholds are not defined

### scope
- [scope] The MVP recommendation model is too broad for the available supply and operations model
- [scope] The smallest credible launch audience is still too broad for a proof-oriented pilot

### market_motion
- [market_motion] The primary acquisition motion is not yet specified in a way that can be tested

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and a small merchant set
- [market_motion] Lock one acquisition motion: founder-led merchant seeding plus merchant-distributed invites

### untagged
- Finalize and test one redemption mechanism before launch
- Define merchant lifecycle states, approval rules, and immediate disable controls

### metrics_validation
- [metrics_validation] Validate that users return after one successful visit or reward
- [metrics_validation] Set a minimum pilot threshold for active merchants and first redemptions before public launch

### operations
- [operations] Confirm the launch neighborhood can support enough approved merchants before public consumer rollout

### scope
- [scope] Select one deterministic redemption method and make it the only supported MVP path
- [scope] Replace advanced personalization with rules-based curation and explicit user filters
- [scope] Narrow launch audience to frequent neighborhood coffee/lunch buyers who live or work locally

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a concierge pilot with real users and a small merchant set Run a concierge pilot with a tightly defined merchant set and real users before expanding scope


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Validate that users return after one successful visit or reward Prove repeat usage after one successful local visit or reward


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] The MVP recommendation model is too broad for the available supply and operations model Select one deterministic redemption method and make it the only supported MVP path Replace advanced personalization with rules-based curation and explicit user filters


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


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
- Verified merchant density in one neighborhood is unproven
- The redemption mechanism is not defined tightly enough to build a reliable proof loop
- Merchant approval and listing controls need a concrete state model before implementation

### demand_validation
- [demand_validation] Consumer demand for a curated local discovery app remains unproven
- [demand_validation] The single redemption flow has not been validated in live merchant settings

### metrics_validation
- [metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data
- [metrics_validation] Merchant density and active promotion thresholds are not defined

### scope
- [scope] The MVP recommendation model is too broad for the available supply and operations model
- [scope] The smallest credible launch audience is still too broad for a proof-oriented pilot

### market_motion
- [market_motion] The primary acquisition motion is not yet specified in a way that can be tested

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and a small merchant set
- [market_motion] Lock one acquisition motion: founder-led merchant seeding plus merchant-distributed invites

### untagged
- Finalize and test one redemption mechanism before launch
- Define merchant lifecycle states, approval rules, and immediate disable controls

### metrics_validation
- [metrics_validation] Validate that users return after one successful visit or reward
- [metrics_validation] Set a minimum pilot threshold for active merchants and first redemptions before public launch

### operations
- [operations] Confirm the launch neighborhood can support enough approved merchants before public consumer rollout

### scope
- [scope] Select one deterministic redemption method and make it the only supported MVP path
- [scope] Replace advanced personalization with rules-based curation and explicit user filters
- [scope] Narrow launch audience to frequent neighborhood coffee/lunch buyers who live or work locally

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a concierge pilot with real users and a small merchant set The primary acquisition motion is not yet specified in a way that can be tested Lock one acquisition motion: founder-led merchant seeding plus merchant-distributed invites


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data Validate that users return after one successful visit or reward Merchant density and active promotion thresholds are not defined Set a minimum pilot threshold for active merchants and first redemptions before public launch


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] The MVP recommendation model is too broad for the available supply and operations model Select one deterministic redemption method and make it the only supported MVP path Replace advanced personalization with rules-based curation and explicit user filters The smallest credible launch audience is still too broad for a proof-oriented pilot Narrow launch audience to frequent neighborhood coffee/lunch buyers who live or work locally


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

### untagged
- Verified merchant density in one neighborhood is unproven
- The redemption mechanism is not defined tightly enough to build a reliable proof loop
- Merchant approval and listing controls need a concrete state model before implementation
- Merchant supply density required for credible consumer launch is unproven

### demand_validation
- [demand_validation] Consumer demand for a curated local discovery app remains unproven
- [demand_validation] The single redemption flow has not been validated in live merchant settings
- [demand_validation] Smallest credible launch audience is not yet tied to a measurable launch threshold

### metrics_validation
- [metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data

### scope
- [scope] The MVP recommendation model is too broad for the available supply and operations model

### market_motion
- [market_motion] Primary acquisition motion is still not concrete enough to test in-market

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot with real users and a small merchant set
- [market_motion] Define and pilot one acquisition motion: founder-led merchant seeding plus merchant-distributed invites

### untagged
- Finalize and test one redemption mechanism before launch
- Define merchant lifecycle states, approval rules, and immediate disable controls
- Set a minimum neighborhood merchant count before consumer launch

### metrics_validation
- [metrics_validation] Validate that users return after one successful visit or reward

### operations
- [operations] Confirm the launch neighborhood can support enough approved merchants before public consumer rollout

### scope
- [scope] Select one deterministic redemption method and make it the only supported MVP path
- [scope] Replace advanced personalization with rules-based curation and explicit user filters

### demand_validation
- [demand_validation] Narrow the first audience to frequent neighborhood coffee/lunch buyers who can be reached through merchants

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Run a concierge pilot with real users and a small merchant set The primary acquisition motion is not yet specified in a way that can be tested Lock one acquisition motion: founder-led merchant seeding plus merchant-distributed invites


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data Validate that users return after one successful visit or reward Merchant density and active promotion thresholds are not defined Set a minimum pilot threshold for active merchants and first redemptions before public launch


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] The MVP recommendation model is too broad for the available supply and operations model Select one deterministic redemption method and make it the only supported MVP path Replace advanced personalization with rules-based curation and explicit user filters The smallest credible launch audience is still too broad for a proof-oriented pilot Narrow launch audience to frequent neighborhood coffee/lunch buyers who live or work locally


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Replace “personalized recommendations” with explicit location + category + curated ranking for MVP [recommendation_scope]
- [tech] Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]

## Growth Structural Decisions

### growth
- [growth] Specify the primary acquisition motion as **founder-led merchant seeding plus merchant-distributed invites**.
- [growth] Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.

## Product Locking

## Applied

True


## Confirmed In Scope

- one-neighborhood launch
- coffee and lunch / casual food only
- curated nearby feed of approved independent businesses
- merchant approval state before listing
- one supported redemption mechanism only
- basic loyalty ledger tracking
- save and navigate actions
- anonymous browsing with optional sign-in if needed for loyalty recording


## Confirmed Deferred

- reviews
- event feed
- advanced personalization
- richer loyalty mechanics
- automated merchant marketing tools
- multi-city expansion
- sponsored placements
- social features
- multiple redemption methods


## Confirmed Out Of Scope

- broad coverage across all local business types
- citywide or multi-city expansion
- reservations, delivery, or booking flows
- full payments, wallet, or financing features
- deep analytics suites
- consumer community features


## Locking Note

The MVP remains tightly locked around discovery plus one reliable redemption loop in a single neighborhood. No accessory features are reintroduced.


## Expert Contributions

### Tech Summary

The MVP is feasible only if LocalLoop is built as a curated, controlled local marketplace with manual supply operations and a deterministic redemption flow. The biggest challenge is not the mobile app—it is proving a reliable merchant-side redemption loop and keeping the feed relevant without an overbuilt recommendation system.

## Tech Structural Decisions

- Replace “personalized recommendations” with explicit location + category + curated ranking for MVP [recommendation_scope]
- Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]


## Tech Recommendations

- Replace “personalized recommendations” with explicit location + category + curated ranking for MVP [recommendation_scope]
- Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]


## Tech Risks

- Redemption may be too awkward for merchant staff, causing unreliable proof [redemption_flow]
- Feed quality may degrade if curation is inconsistent or supply is thin [market_motion]
- Merchant onboarding may require more manual effort than the team can sustain [ops_load]


## Tech Open Questions

- What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- What minimum merchant data is required for approval and listing?


### Growth Summary

The core launch challenge is not building discovery software; it is proving there is enough merchant supply in one neighborhood to make the app useful enough for consumers to try and redeem. The right GTM direction is a founder-led, merchant-seeded concierge pilot in one dense neighborhood, with coffee and lunch as the only categories, and merchant-distributed invites as the first acquisition motion.

## Growth Structural Decisions

- Specify the primary acquisition motion as **founder-led merchant seeding plus merchant-distributed invites**.
- Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.


## Growth Recommendations

- Specify the primary acquisition motion as **founder-led merchant seeding plus merchant-distributed invites**.
- Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.
- Add a launch threshold for merchant supply, such as a minimum number of approved merchants needed before consumer rollout.
- Clarify the first activation event as **browse → save/redeem → verified visit → repeat return**.
- State that public launch should not happen until one redemption flow works reliably in live merchant settings.


## Growth Risks

- merchant supply remains too thin to create a useful feed
- merchants do not actively distribute invites to nearby customers
- users default back to Google Maps, Yelp, or social discovery


## Growth Open Questions

- How many approved merchants are needed before the feed feels credible to first users?
- Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- What minimum merchant participation level counts as active distribution?


## Product Arbitration

## Source

heuristic_fallback


## Retained

_Aucun élément retenu._


## Deferred

- Tech: Replace “personalized recommendations” with explicit location + category + curated ranking for MVP [recommendation_scope]


## Rejected

- Tech: Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Growth: Add a launch threshold for merchant supply, such as a minimum number of approved merchants needed before consumer rollout.
- Growth: State that public launch should not happen until one redemption flow works reliably in live merchant settings.


## Open Points

- Tech: Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Tech: Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Tech: Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]
- Growth: Specify the primary acquisition motion as **founder-led merchant seeding plus merchant-distributed invites**.
- Growth: Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.
- Growth: Clarify the first activation event as **browse → save/redeem → verified visit → repeat return**.
- Tech: What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Tech: Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- Tech: What minimum merchant data is required for approval and listing?
- Growth: How many approved merchants are needed before the feed feels credible to first users?
- Growth: Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- Growth: What minimum merchant participation level counts as active distribution?
- Tech recommendation needing arbitration: Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Tech recommendation needing arbitration: Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Tech recommendation needing arbitration: Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Tech recommendation needing arbitration: Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]
- Growth recommendation needing arbitration: Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.
- Growth recommendation needing arbitration: Add a launch threshold for merchant supply, such as a minimum number of approved merchants needed before consumer rollout.
- Growth recommendation needing arbitration: Clarify the first activation event as **browse → save/redeem → verified visit → repeat return**.
- Growth recommendation needing arbitration: State that public launch should not happen until one redemption flow works reliably in live merchant settings.
- Tech open question: What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Tech open question: Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- Tech open question: What minimum merchant data is required for approval and listing?
- Growth open question: How many approved merchants are needed before the feed feels credible to first users?
- Growth open question: Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- Growth open question: What minimum merchant participation level counts as active distribution?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local businesses still default to large platforms because local discovery is fragmented, unevenly surfaced, and hard to act on in one place. Independent businesses, meanwhile, need a low-cost way to be discovered by nearby customers and bring them back again.

The MVP should prove one narrow thing: a user can discover a relevant nearby local business, see a compelling offer, and take a first repeatable action that creates value for both sides.

## Initial Wedge
Neighborhood-local discovery for one city, focused on one repeatable use case:

- find a nearby independent coffee shop, restaurant, or similar local spot
- see a simple offer or reward
- get directions and visit

This wedge is narrow enough to test supply, demand, and repeat behavior without needing a full local commerce marketplace.

## First Target User
Urban residents and young professionals in one dense neighborhood of a single city.

Why this segment first:
- high frequency of nearby local purchases
- familiar with mobile discovery
- more likely to respond to nearby deals and loyalty rewards
- easier to serve with a dense merchant footprint

Secondary users, such as families and tourists, should be deferred until the core loop is proven.

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Google Maps / Search for local discovery
- Yelp / reviews for evaluation
- Instagram / TikTok for informal local discovery
- merchant-owned loyalty cards or punch apps
- neighborhood newsletters and deal sites

Switching trigger:
- users want a faster, more curated way to discover local places that combines proximity, a relevant offer, and lightweight rewards in one place
- merchants want a simpler way to get visibility without buying broad ads or managing complex marketing tools

LocalLoop must beat the current patchwork on simplicity, relevance, and immediate local value. It does not need to replace general search or review platforms in the MVP.

## Core MVP Workflow
1. User opens the app and allows location access.
2. App shows a small set of nearby independent businesses curated for the user’s neighborhood.
3. User filters or browses by a simple category, such as coffee, lunch, or casual shopping.
4. User sees a merchant profile with a brief description, location, and one clear offer or reward.
5. User taps to save, navigate, or redeem the offer in-store.
6. Merchant records the redemption or visit through a simple flow.
7. User earns a basic loyalty reward if applicable.

The workflow must prove discovery, relevance, and at least one repeatable conversion action.

## In Scope
- location-based discovery within one city or neighborhood cluster
- curated merchant profiles for independent local businesses
- simple offers or promotions
- lightweight loyalty/reward tracking
- basic category browsing
- simple save, navigate, or redeem action
- merchant onboarding for a limited pilot set
- basic merchant dashboard or interface to manage profile, offer, and redemptions
- minimal quality controls to reduce irrelevant or low-value listings

## Out of Scope
- multi-city expansion
- broad vertical coverage across all local commerce
- event feed as a primary feature
- review system at launch
- social sharing features
- advanced personalization engine
- automated ad buying or campaign management for merchants
- marketplace bidding or sponsored ranking complexity
- deep analytics suites
- full wallet, payments, or financing features
- restaurant reservations, delivery, or full booking flows
- consumer-to-consumer community features

## MVP Build Vs Pilot Operations
### Must Build Now
- location-based browse/feed for nearby local businesses
- merchant profile pages
- one simple offer or reward mechanic
- basic loyalty tracking
- save / navigate / redeem actions
- merchant-side offer setup and redemption logging
- minimal curation controls

### Manual Or Operational During Pilot
- recruiting initial merchants
- verifying business legitimacy
- curating which businesses appear in the feed
- writing or editing merchant copy
- monitoring offer quality and relevance
- handling merchant support and onboarding
- manually resolving redemption issues

### Deferred Until After Proof
- reviews
- event feed
- advanced personalization
- richer loyalty mechanics
- automated merchant campaign tools
- multi-city expansion
- sponsored placements
- social features

## Business Model Hypothesis
Primary hypothesis: independent businesses will pay a small monthly fee or per-location fee for visibility, offer distribution, and repeat customer acquisition if LocalLoop delivers measurable nearby visits and redemptions.

Secondary hypothesis: the consumer app stays free, with monetization driven by merchant subscriptions, featured placement, or paid promotion only after trust and traction are proven.

The MVP should not assume a complex ad model. Revenue should be tested only after repeat usage and merchant willingness to pay are observed.

## Critical Assumptions
- enough independent businesses in one neighborhood will join to create useful supply
- users will adopt a new app for local discovery if the results feel better than existing tools
- a simple offer plus location context is enough to motivate visits
- merchants will see enough value from nearby discovery to participate
- low-friction redemption tracking is feasible in real-world store settings
- relevance can be maintained without a sophisticated recommendation engine

## How To Test Quickly
- launch in one dense neighborhood with 20 to 50 merchants in one or two categories
- run concierge onboarding for merchants and manually curate listings
- test a simple consumer flow with one offer per merchant
- measure profile views, saves, redemptions, and repeat visits
- compare conversion against a baseline of businesses relying on Google Maps or walk-ins
- interview merchants weekly on perceived value and operational friction
- test whether users return after initial redemption within 2 to 4 weeks

## Acceptance Criteria
- a new user can enable location and see relevant nearby businesses within seconds
- at least 20 active merchants are available in the pilot area
- each merchant has a functioning profile and at least one active offer or reward
- a user can save, navigate to, or redeem an offer without assistance
- merchants can record a redemption reliably
- the feed shows enough relevance that users do not abandon it as generic or spammy
- pilot merchants report at least some measurable customer interest or visits attributable to the app
- the system supports repeat use without manual intervention in the consumer flow

## Risks And Failure Modes
- insufficient merchant supply creates a thin or irrelevant experience
- users already rely on Google Maps or Yelp and do not switch
- offers feel generic or low value, reducing engagement
- redemption tracking is too awkward for merchants
- personalization is too weak to keep the feed relevant
- supply quality degrades if onboarding is too easy
- unit economics fail if merchant acquisition is too manual or expensive

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Verified merchant supply density in one city or neighborhood is unproven [supply_density]
- Consumer demand for a new local discovery app versus existing alternatives is unproven [demand_validation]
- A low-friction redemption and loyalty flow is unproven in live merchant settings [redemption_flow]

Required Improvements:
- Run a concierge pilot with a small merchant set and real users before full build [concierge_pilot]
- Define the simplest possible redemption mechanism that merchants can use consistently [low_friction_redemption]
- Validate that users return after one successful visit or reward [retention_signal]

## Recommendation
Proceed with a narrow concierge-backed MVP in one dense neighborhood and one or two categories. Do not expand scope until you prove merchant supply, consumer repeat usage, and reliable redemption. If those signals do not appear quickly, the project should remain a pilot or be reconsidered rather than broadened.

## Retained Decisions

_Aucune décision retenue._

## Deferred Decisions

- Tech: Replace “personalized recommendations” with explicit location + category + curated ranking for MVP [recommendation_scope]

## Rejected Recommendations

- Tech: Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Growth: Add a launch threshold for merchant supply, such as a minimum number of approved merchants needed before consumer rollout.
- Growth: State that public launch should not happen until one redemption flow works reliably in live merchant settings.

## Unresolved Tensions

- Tech recommendation needing arbitration: Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Tech recommendation needing arbitration: Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Tech recommendation needing arbitration: Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Tech recommendation needing arbitration: Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]
- Growth recommendation needing arbitration: Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.
- Growth recommendation needing arbitration: Add a launch threshold for merchant supply, such as a minimum number of approved merchants needed before consumer rollout.
- Growth recommendation needing arbitration: Clarify the first activation event as **browse → save/redeem → verified visit → repeat return**.
- Growth recommendation needing arbitration: State that public launch should not happen until one redemption flow works reliably in live merchant settings.
- Tech open question: What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Tech open question: Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- Tech open question: What minimum merchant data is required for approval and listing?
- Growth open question: How many approved merchants are needed before the feed feels credible to first users?
- Growth open question: Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- Growth open question: What minimum merchant participation level counts as active distribution?

## Applied Changes

_Aucun changement appliqué._

## Remaining Open Points

- Tech: Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Tech: Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Tech: Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]
- Growth: Specify the primary acquisition motion as **founder-led merchant seeding plus merchant-distributed invites**.
- Growth: Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.
- Growth: Clarify the first activation event as **browse → save/redeem → verified visit → repeat return**.
- Tech: What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Tech: Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- Tech: What minimum merchant data is required for approval and listing?
- Growth: How many approved merchants are needed before the feed feels credible to first users?
- Growth: Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- Growth: What minimum merchant participation level counts as active distribution?
- Tech recommendation needing arbitration: Define a single redemption mechanism and make it the only supported path at launch [redemption_flow]
- Tech recommendation needing arbitration: Add a merchant approval state and exclude unverified businesses from the live feed [merchant_verification]
- Tech recommendation needing arbitration: Specify how loyalty is recorded as a simple ledger event rather than a complex rewards system [loyalty_ledger]
- Tech recommendation needing arbitration: Clarify the first neighborhood boundary and merchant count target as an operational constraint, not just a pilot goal [supply_density]
- Growth recommendation needing arbitration: Define the smallest credible launch audience as **people who live or work in one dense neighborhood and buy coffee or lunch frequently**.
- Growth recommendation needing arbitration: Add a launch threshold for merchant supply, such as a minimum number of approved merchants needed before consumer rollout.
- Growth recommendation needing arbitration: Clarify the first activation event as **browse → save/redeem → verified visit → repeat return**.
- Growth recommendation needing arbitration: State that public launch should not happen until one redemption flow works reliably in live merchant settings.
- Tech open question: What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Tech open question: Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- Tech open question: What minimum merchant data is required for approval and listing?
- Growth open question: How many approved merchants are needed before the feed feels credible to first users?
- Growth open question: Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- Growth open question: What minimum merchant participation level counts as active distribution?

## Risks

- Redemption may be too awkward for merchant staff, causing unreliable proof [redemption_flow]
- Feed quality may degrade if curation is inconsistent or supply is thin [market_motion]
- Merchant onboarding may require more manual effort than the team can sustain [ops_load]
- Merchant supply may be too thin to prevent a generic or empty-feeling app. [supply_density]
- Consumers may not switch from Google Maps, Yelp, or social discovery unless the app offers a clearly better immediate outcome. [demand_validation]
- Offers may be too weak to change behavior, reducing both user activation and merchant interest. [demand_validation]
- Merchant supply may be too thin to create a credible feed [supply_density]
- Consumers may default back to Google Maps, Yelp, or social discovery [demand_validation]
- Merchant staff may not consistently support redemption [redemption_flow]
- merchant supply remains too thin to create a useful feed
- merchants do not actively distribute invites to nearby customers
- users default back to Google Maps, Yelp, or social discovery

## Open Questions

- What exact redemption mechanism will be used: code, QR, staff tap, or another method?
- Will users need accounts at launch, or can the MVP support anonymous browsing with optional sign-in for loyalty?
- What minimum merchant data is required for approval and listing?
- What is the exact first neighborhood, and why is it dense enough to support the pilot?
- Which two merchant categories are most likely to produce repeat visits and clear offer value?
- What is the minimum merchant action required to count as “live” in the pilot?
- Which exact neighborhood has enough independent coffee/lunch density to support launch?
- How many merchants must actively promote LocalLoop for consumer acquisition to be viable?
- What offer type produces the clearest first redemption behavior?
- How many approved merchants are needed before the feed feels credible to first users?
- Which merchant-distributed channel will be used first: QR at checkout, receipt inserts, or staff verbal invite?
- What minimum merchant participation level counts as active distribution?

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local independent businesses still default to large platforms because local discovery is fragmented, hard to trust, and inconvenient to act on in one place. Independent businesses need a low-cost way to get discovered by nearby customers and bring them back again, but they cannot rely on broad ad tools or complex marketing systems.

The MVP must prove one narrow outcome: a person who lives or works in the launch neighborhood can find a relevant nearby independent coffee or lunch spot, redeem one simple offer, and have that visit recorded reliably enough to support a repeat-visit loop.

## Initial Wedge
One dense neighborhood in one city, focused on two repeat-visit categories:

- coffee shops
- lunch / casual food spots

The wedge is a curated nearby feed, not a broad local commerce marketplace. It is narrow enough to test merchant supply, user interest, redemption behavior, and repeat usage without competing head-on with horizontal discovery platforms.

## First Target User
People who live or work in the launch neighborhood and make frequent coffee or lunch purchases.

Why this segment first:
- high frequency, repeatable use case
- easy to reach inside one dense area
- more likely to respond to simple neighborhood offers
- more likely to repeat if the experience is faster than checking existing apps

Broader audiences like families, tourists, and citywide users are deferred until the core loop is proven.

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- merchant punch cards or loyalty apps
- neighborhood newsletters and deal sites

Switching trigger:
- users want a faster, more curated way to find nearby independent coffee or lunch options than checking multiple existing apps
- merchants want visibility to nearby customers without buying broad ads or managing complex tools

LocalLoop does not need to replace general search or review platforms in the MVP. It only needs to be faster and more relevant for the narrow launch use case.

## Core MVP Workflow
1. User opens the app and allows location access.
2. App shows a curated feed of approved independent businesses within the launch neighborhood, ranked by location, category match, and manual curation.
3. User filters by coffee or lunch.
4. User opens a merchant profile with a short description, location, and one active offer.
5. User saves the place, gets directions, or shows a single redemption code in-store.
6. Merchant verifies the redemption through the same code flow.
7. If the merchant has a loyalty offer, the visit is recorded as a simple ledger event.

The workflow must prove that LocalLoop can surface relevant nearby businesses and support one reliable first conversion action.

## In Scope
- one-neighborhood launch
- two launch categories: coffee and lunch / casual food
- curated nearby feed of approved independent businesses
- rules-based ranking using location, category match, and manual curation
- merchant profile pages
- one simple offer per merchant
- one supported redemption mechanism only
- basic loyalty ledger tracking as visit count / stamp history
- save and navigate actions
- merchant approval state before listing
- merchant onboarding for a limited pilot set
- minimal quality controls to exclude unverified or low-value listings
- anonymous browsing with optional sign-in only if needed for loyalty recording

## Out of Scope
- citywide or multi-city expansion
- broad coverage across all local business types
- event feed as a launch feature
- reviews
- social sharing features
- advanced personalization
- multiple redemption methods
- automated merchant campaign tools
- sponsored ranking or bidding systems
- deep analytics suites
- full payments, wallet, or financing features
- reservations, delivery, or booking flows
- consumer community features

## MVP Build Vs Pilot Operations
### Must Build Now
- location-based curated feed for the launch neighborhood
- approved merchant profile pages
- one supported redemption mechanism
- basic loyalty ledger
- save and navigate actions
- merchant approval state
- simple user filters for coffee or lunch

### Manual Or Operational During Pilot
- recruiting initial merchants
- verifying business legitimacy
- selecting which merchants appear in the feed
- writing or editing merchant copy
- monitoring offer quality and relevance
- handling merchant onboarding
- resolving redemption issues manually
- encouraging merchant participation in the pilot area
- measuring repeat usage and user return behavior

### Deferred Until After Proof
- reviews
- event feed
- advanced personalization
- richer loyalty mechanics
- automated merchant marketing tools
- multi-city expansion
- sponsored placements
- social features
- multiple redemption methods

## Business Model Hypothesis
Primary hypothesis: independent businesses will pay a small monthly fee or per-location fee for visibility and repeat-customer acquisition if LocalLoop drives measurable nearby visits and redemptions.

Secondary hypothesis: the consumer app remains free, with monetization later through merchant subscriptions or featured placement after trust and traction are proven.

The MVP should not assume a complex ad model or broad marketplace monetization.

## Critical Assumptions
- enough independent businesses exist in one neighborhood to create a useful feed
- merchants are willing to join a curated pilot
- users will try a new app if nearby results feel faster and more relevant than existing tools
- a simple offer is enough to motivate a visit
- the single redemption flow is practical in real store settings
- a simple loyalty ledger is understandable and reliable
- relevance can be maintained without advanced personalization
- merchant approval can keep unverified businesses out of the live feed

## How To Test Quickly
- launch in one dense neighborhood with a target of 20 to 50 approved merchants across coffee and lunch
- run founder-led merchant onboarding and curation
- use one redemption method only
- measure profile views, saves, redemptions, and repeat visits
- interview merchants weekly on value and operational friction
- test whether users return after one successful redemption within 2 to 4 weeks

Decision rule:
- Proceed if the pilot reaches at least 20 approved merchants, at least 25% of active users redeem an offer, and at least 20% of redeemers return for a second visit or reward within 30 days.
- Revise if merchant density is met but redemption or repeat use falls below target.
- Reject or restart the wedge if the neighborhood cannot sustain enough approved merchants or the redemption flow breaks repeatedly in live use.

## Acceptance Criteria
- a new user can enable location and see approved nearby businesses within seconds
- the feed contains enough relevant merchants to feel curated rather than generic
- each listed merchant has an approved profile and one active offer
- a user can save, navigate to, and redeem an offer without assistance
- merchants can verify redemption reliably through the supported flow
- loyalty, if offered, is recorded as a simple ledger event
- pilot merchants report measurable customer interest or visits attributable to the app
- the consumer flow works without manual intervention once the merchant is listed
- the product can prove repeat usage, not just one-time browsing

## Risks And Failure Modes
- merchant supply is too thin to make the feed useful
- users stay with Google Maps, Yelp, or social discovery habits
- offers are too generic or low-value to drive action
- the single redemption flow is awkward for merchants or staff
- relevance degrades without strong curation
- unverified listings reduce trust
- manual merchant acquisition makes scaling expensive
- repeat usage does not emerge after the first redemption

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Verified merchant density in one neighborhood is unproven [supply_density]
- Consumer demand for a curated local discovery app remains unproven [demand_validation]
- The single redemption flow has not been validated in live merchant settings [redemption_flow]
- Minimum success metrics for proceed, revise, or reject are not yet validated in live pilot data [metrics_validation]

Required Improvements:
- Run a concierge pilot with real users and a small merchant set [concierge_pilot]
- Finalize and test one redemption mechanism before launch [redemption_flow]
- Validate that users return after one successful visit or reward [metrics_validation]
- Confirm the launch neighborhood can support enough approved merchants before public consumer rollout [supply_density]

## Recommendation
Proceed with a narrow concierge-backed MVP in one neighborhood and two categories. Keep the product as a curated nearby feed with one redemption path, merchant approval, and a simple loyalty ledger. Do not expand into personalization, reviews, events, or broader category coverage until merchant supply, redemption reliability, and repeat usage are proven.

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
