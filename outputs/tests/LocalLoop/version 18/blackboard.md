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
- [demand_validation] Need proof that one neighborhood and a curated merchant set can beat default discovery habits

### market_motion
- [market_motion] Need evidence that merchants will continue participation or pay after the pilot

### metrics_validation
- [metrics_validation] Need a defined success gate using activation, retention, merchant supply, and freshness coverage

## Product Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one dense neighborhood with real users and merchants

### scope
- [scope] Define the minimum merchant supply threshold before consumer launch

### metrics_validation
- [metrics_validation] Measure save or redeem as the first activation event
- [metrics_validation] Track repeat opens over a short interval as the retention signal

### demand_validation
- [demand_validation] Track merchant continuation or willingness-to-pay after initial exposure

## Tech Status

LIMITED


## Tech Blocking Gaps

### privacy_trust
- [privacy_trust] Redemption verification is not defined well enough to build a trustworthy MVP

### untagged
- Listing freshness and approval controls are not yet specified tightly enough for safe publication

### scope
- [scope] The MVP still implies personalization beyond what should be built first

## Tech Required Improvements

### untagged
- Choose one simple redemption mechanism and make it auditable

### operations
- [operations] Add mandatory admin approval, expiry, and stale-item suppression rules

### market_motion
- [market_motion] Constrain personalization to deterministic preference and proximity ranking for the pilot

## Growth Status

LIMITED


## Growth Blocking Gaps

### operations
- [operations] The primary acquisition motion is not yet explicit enough to support a credible launch plan

### scope
- [scope] The smallest launch audience is still too broad to reliably test local habit formation
- [scope] The merchant-side minimum supply threshold is not defined, so the feed could launch too thin

## Growth Required Improvements

### market_motion
- [market_motion] Lock one merchant-led acquisition motion plus one neighborhood partner channel for the pilot

### scope
- [scope] Define the smallest credible audience as users within walking distance of the pilot merchants
- [scope] Set a minimum active merchant count and freshness threshold before public launch

### metrics_validation
- [metrics_validation] Tie launch success to one activation metric and one retention metric

## Global Status

LIMITED


## Global Blocking Gaps

### demand_validation
- [demand_validation] Need proof that one neighborhood and a curated merchant set can beat default discovery habits

### market_motion
- [market_motion] Need evidence that merchants will continue participation or pay after the pilot

### metrics_validation
- [metrics_validation] Need a defined success gate using activation, retention, merchant supply, and freshness coverage

### privacy_trust
- [privacy_trust] Redemption verification is not defined well enough to build a trustworthy MVP

### untagged
- Listing freshness and approval controls are not yet specified tightly enough for safe publication

### scope
- [scope] The MVP still implies personalization beyond what should be built first
- [scope] The smallest launch audience is still too broad to reliably test local habit formation
- [scope] The merchant-side minimum supply threshold is not defined, so the feed could launch too thin

### operations
- [operations] The primary acquisition motion is not yet explicit enough to support a credible launch plan

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one dense neighborhood with real users and merchants
- [market_motion] Constrain personalization to deterministic preference and proximity ranking for the pilot
- [market_motion] Lock one merchant-led acquisition motion plus one neighborhood partner channel for the pilot

### scope
- [scope] Define the minimum merchant supply threshold before consumer launch
- [scope] Define the smallest credible audience as users within walking distance of the pilot merchants
- [scope] Set a minimum active merchant count and freshness threshold before public launch

### metrics_validation
- [metrics_validation] Measure save or redeem as the first activation event
- [metrics_validation] Track repeat opens over a short interval as the retention signal
- [metrics_validation] Tie launch success to one activation metric and one retention metric

### demand_validation
- [demand_validation] Track merchant continuation or willingness-to-pay after initial exposure

### untagged
- Choose one simple redemption mechanism and make it auditable

### operations
- [operations] Add mandatory admin approval, expiry, and stale-item suppression rules

## Known Tags

- privacy_trust
- untagged
- demand_validation
- operations
- scope
- metrics_validation
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

#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need evidence that merchants will continue participation or pay after the pilot Run a concierge pilot in one neighborhood with real users and merchants Constrain personalization to deterministic preference and proximity ranking for the pilot


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

- tech


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Measure repeat opens, saves, and redemptions over a short interval The activation metric is not fixed, so early proof could be ambiguous Choose one activation event and one retention signal for the pilot


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


#### Product Task

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Define the minimum merchant supply threshold before consumer launch The MVP still implies personalization beyond what should be built first The launch geography is too broad to prove supply density and relevance Define a single neighborhood pilot boundary and merchant count target


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Contributors

- tech
- growth


### Loop 2

#### Growth Task

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need evidence that merchants will continue participation or pay after the pilot Run a concierge pilot in one dense neighborhood with real users and merchants Constrain personalization to deterministic preference and proximity ranking for the pilot Commit to one merchant-led acquisition motion and one partner channel.


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


## Contributors

- tech


#### Product Task

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Need a defined decision rule using one activation event and one retention signal for the pilot Measure save or redeem as the first activation event Track repeat opens over a short interval as the retention signal Set a numeric launch gate for active merchants, active offers, and freshness coverage.


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


## Contributors

- growth


#### Product Task

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Define the minimum merchant supply threshold before consumer launch The MVP still implies personalization beyond what should be built first The minimum supply threshold for a credible neighborhood feed is undefined. Define a single neighborhood and a single consumer segment for the pilot.


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

### demand_validation
- [demand_validation] Need proof that a single-neighborhood curated feed can beat default discovery habits
- [demand_validation] There is no quantified threshold for enough merchant supply to open to users

### market_motion
- [market_motion] Need evidence that merchants will continue participation or pay after the pilot

### privacy_trust
- [privacy_trust] Need validation that manual freshness controls keep the feed trustworthy enough to retain users
- [privacy_trust] Redemption verification is not defined well enough to build a trustworthy MVP

### untagged
- Listing freshness and approval controls are not yet specified tightly enough for safe publication

### scope
- [scope] The MVP still implies personalization beyond what should be built first
- [scope] The launch geography is too broad to prove supply density and relevance

### metrics_validation
- [metrics_validation] The activation metric is not fixed, so early proof could be ambiguous

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one neighborhood with real users and merchants
- [market_motion] Constrain personalization to deterministic preference and proximity ranking for the pilot

### scope
- [scope] Define the minimum merchant supply threshold before consumer launch
- [scope] Define a single neighborhood pilot boundary and merchant count target

### metrics_validation
- [metrics_validation] Measure repeat opens, saves, and redemptions over a short interval
- [metrics_validation] Choose one activation event and one retention signal for the pilot

### demand_validation
- [demand_validation] Track merchant continuation or willingness-to-pay after initial exposure
- [demand_validation] Set a minimum viable supply bar for launch readiness

### untagged
- Choose one simple redemption mechanism and make it auditable

### operations
- [operations] Add mandatory admin approval, expiry, and stale-item suppression rules

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need evidence that merchants will continue participation or pay after the pilot Run a concierge pilot in one neighborhood with real users and merchants Constrain personalization to deterministic preference and proximity ranking for the pilot


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Measure repeat opens, saves, and redemptions over a short interval The activation metric is not fixed, so early proof could be ambiguous Choose one activation event and one retention signal for the pilot


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Define the minimum merchant supply threshold before consumer launch The MVP still implies personalization beyond what should be built first The launch geography is too broad to prove supply density and relevance Define a single neighborhood pilot boundary and merchant count target


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

### demand_validation
- [demand_validation] Need proof that one neighborhood and a curated merchant set can beat default discovery habits

### market_motion
- [market_motion] Need evidence that merchants will continue participation or pay after the pilot

### metrics_validation
- [metrics_validation] Need a defined decision rule using one activation event and one retention signal for the pilot

### privacy_trust
- [privacy_trust] Redemption verification is not defined well enough to build a trustworthy MVP

### untagged
- Listing freshness and approval controls are not yet specified tightly enough for safe publication

### scope
- [scope] The MVP still implies personalization beyond what should be built first
- [scope] The minimum supply threshold for a credible neighborhood feed is undefined.

### operations
- [operations] The launch audience is still too broad to support a clear acquisition motion.
- [operations] The primary acquisition motion is not yet operationally specific enough to test.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one dense neighborhood with real users and merchants
- [market_motion] Constrain personalization to deterministic preference and proximity ranking for the pilot
- [market_motion] Commit to one merchant-led acquisition motion and one partner channel.

### scope
- [scope] Define the minimum merchant supply threshold before consumer launch
- [scope] Define a single neighborhood and a single consumer segment for the pilot.

### metrics_validation
- [metrics_validation] Measure save or redeem as the first activation event
- [metrics_validation] Track repeat opens over a short interval as the retention signal
- [metrics_validation] Set a numeric launch gate for active merchants, active offers, and freshness coverage.

### demand_validation
- [demand_validation] Track merchant continuation or willingness-to-pay after initial exposure

### untagged
- Choose one simple redemption mechanism and make it auditable

### operations
- [operations] Add mandatory admin approval, expiry, and stale-item suppression rules

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need evidence that merchants will continue participation or pay after the pilot Run a concierge pilot in one neighborhood with real users and merchants Constrain personalization to deterministic preference and proximity ranking for the pilot


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Measure repeat opens, saves, and redemptions over a short interval The activation metric is not fixed, so early proof could be ambiguous Choose one activation event and one retention signal for the pilot


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Define the minimum merchant supply threshold before consumer launch The MVP still implies personalization beyond what should be built first The launch geography is too broad to prove supply density and relevance Define a single neighborhood pilot boundary and merchant count target


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

### demand_validation
- [demand_validation] Need proof that one neighborhood and a curated merchant set can beat default discovery habits

### market_motion
- [market_motion] Need evidence that merchants will continue participation or pay after the pilot

### metrics_validation
- [metrics_validation] Need a defined decision rule using one activation event and one retention signal for the pilot

### privacy_trust
- [privacy_trust] Redemption verification is not defined well enough to build a trustworthy MVP

### untagged
- Listing freshness and approval controls are not yet specified tightly enough for safe publication

### scope
- [scope] The MVP still implies personalization beyond what should be built first
- [scope] The minimum supply threshold for a credible neighborhood feed is undefined.

### operations
- [operations] The launch audience is still too broad to support a clear acquisition motion.
- [operations] The primary acquisition motion is not yet operationally specific enough to test.

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one dense neighborhood with real users and merchants
- [market_motion] Constrain personalization to deterministic preference and proximity ranking for the pilot
- [market_motion] Commit to one merchant-led acquisition motion and one partner channel.

### scope
- [scope] Define the minimum merchant supply threshold before consumer launch
- [scope] Define a single neighborhood and a single consumer segment for the pilot.

### metrics_validation
- [metrics_validation] Measure save or redeem as the first activation event
- [metrics_validation] Track repeat opens over a short interval as the retention signal
- [metrics_validation] Set a numeric launch gate for active merchants, active offers, and freshness coverage.

### demand_validation
- [demand_validation] Track merchant continuation or willingness-to-pay after initial exposure

### untagged
- Choose one simple redemption mechanism and make it auditable

### operations
- [operations] Add mandatory admin approval, expiry, and stale-item suppression rules

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need evidence that merchants will continue participation or pay after the pilot Run a concierge pilot in one dense neighborhood with real users and merchants Constrain personalization to deterministic preference and proximity ranking for the pilot Commit to one merchant-led acquisition motion and one partner channel.


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Need a defined decision rule using one activation event and one retention signal for the pilot Measure save or redeem as the first activation event Track repeat opens over a short interval as the retention signal Set a numeric launch gate for active merchants, active offers, and freshness coverage.


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Define the minimum merchant supply threshold before consumer launch The MVP still implies personalization beyond what should be built first The minimum supply threshold for a credible neighborhood feed is undefined. Define a single neighborhood and a single consumer segment for the pilot.


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

### demand_validation
- [demand_validation] Need proof that one neighborhood and a curated merchant set can beat default discovery habits

### market_motion
- [market_motion] Need evidence that merchants will continue participation or pay after the pilot

### metrics_validation
- [metrics_validation] Need a defined success gate using activation, retention, merchant supply, and freshness coverage

### privacy_trust
- [privacy_trust] Redemption verification is not defined well enough to build a trustworthy MVP

### untagged
- Listing freshness and approval controls are not yet specified tightly enough for safe publication

### scope
- [scope] The MVP still implies personalization beyond what should be built first
- [scope] The smallest launch audience is still too broad to reliably test local habit formation
- [scope] The merchant-side minimum supply threshold is not defined, so the feed could launch too thin

### operations
- [operations] The primary acquisition motion is not yet explicit enough to support a credible launch plan

## Global Required Improvements

### market_motion
- [market_motion] Run a concierge pilot in one dense neighborhood with real users and merchants
- [market_motion] Constrain personalization to deterministic preference and proximity ranking for the pilot
- [market_motion] Lock one merchant-led acquisition motion plus one neighborhood partner channel for the pilot

### scope
- [scope] Define the minimum merchant supply threshold before consumer launch
- [scope] Define the smallest credible audience as users within walking distance of the pilot merchants
- [scope] Set a minimum active merchant count and freshness threshold before public launch

### metrics_validation
- [metrics_validation] Measure save or redeem as the first activation event
- [metrics_validation] Track repeat opens over a short interval as the retention signal
- [metrics_validation] Tie launch success to one activation metric and one retention metric

### demand_validation
- [demand_validation] Track merchant continuation or willingness-to-pay after initial exposure

### untagged
- Choose one simple redemption mechanism and make it auditable

### operations
- [operations] Add mandatory admin approval, expiry, and stale-item suppression rules

## Loop Tasks

##### Growth

## Task

Specify one primary acquisition motion and the smallest credible launch audience.


## Source Gap

[market_motion] Need evidence that merchants will continue participation or pay after the pilot Run a concierge pilot in one dense neighborhood with real users and merchants Constrain personalization to deterministic preference and proximity ranking for the pilot Commit to one merchant-led acquisition motion and one partner channel.


## Expected Output

A single acquisition motion with clear operating assumptions and a launch threshold.


##### Product

## Task

State the minimum success metrics that decide whether the MVP should proceed or be revised.


## Source Gap

[metrics_validation] Need a defined decision rule using one activation event and one retention signal for the pilot Measure save or redeem as the first activation event Track repeat opens over a short interval as the retention signal Set a numeric launch gate for active merchants, active offers, and freshness coverage.


## Expected Output

A simple decision rule for success, revision, or rejection of the MVP.


##### Product

## Task

Tighten the MVP scope so the wedge, target segment, and business model stay explicit.


## Source Gap

[scope] Define the minimum merchant supply threshold before consumer launch The MVP still implies personalization beyond what should be built first The minimum supply threshold for a credible neighborhood feed is undefined. Define a single neighborhood and a single consumer segment for the pilot.


## Expected Output

A narrowed MVP framing that makes the wedge and business hypothesis explicit.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] Define a strict merchant approval workflow with publish/pause/expire states before build [workflow_control]
- [tech] Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]

## Growth Structural Decisions

### growth
- [growth] Define one primary acquisition motion explicitly as merchant-led distribution plus one neighborhood partner channel [market_motion]
- [growth] Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]

## Product Locking

## Applied

True


## Confirmed In Scope

- One-neighborhood launch
- One consumer segment within a 10–15 minute walk
- Nearby discovery feed
- Rule-based preference matching
- Merchant profile pages
- Offer display
- Save/favorite action
- Simple redemption verification and logging
- Admin-first merchant approval and publishing
- Publish / pause / expire states
- Last-reviewed timestamp
- Stale-listing hiding
- Basic analytics
- Minimum merchant supply threshold


## Confirmed Deferred

- Full loyalty program
- Reviews and comments
- Event discovery
- Automated merchant self-serve tools
- Sophisticated recommendation models
- Multi-neighborhood or multi-city rollout
- In-app messaging
- Revenue optimization tooling for merchants


## Confirmed Out Of Scope

- Multi-city expansion
- Open merchant self-serve onboarding
- Full loyalty points wallet
- Reviews and user-generated ratings
- Event feed
- Social sharing features
- Advanced machine learning recommendations
- Automated ad management
- Deep CRM or marketing automation
- Delivery, booking, or payment processing
- Chain businesses as a primary supply strategy
- Complex merchant dashboards
- Broad citywide consumer launch


## Locking Note

- Scope is appropriately narrow for proof. - No further feature expansion is justified until freshness, activation, and merchant willingness-to-pay are demonstrated.


## Expert Contributions

### Tech Summary

The biggest feasibility challenge is not building discovery, but keeping the local supply accurate, curated, and trustworthy enough to sustain a usable feed. The safest MVP is a centrally controlled, concierge-operated system with simple ranking and strict admin governance rather than a merchant self-serve platform.

## Tech Structural Decisions

- Define a strict merchant approval workflow with publish/pause/expire states before build [workflow_control]
- Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]


## Tech Recommendations

- Define a strict merchant approval workflow with publish/pause/expire states before build [workflow_control]
- Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]


## Tech Risks

- Stale or inaccurate offers could quickly destroy trust [data_freshness]
- Merchant supply may be too thin to produce a credible feed [merchant_supply]
- Duplicate or fraudulent redemption events may distort value measurement [fraud_control]


## Tech Open Questions

- What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- What minimum merchant data is required for a listing to be publishable?


### Growth Summary

The draft is directionally sound, but the launch risk is supply density and habit change, not feature breadth. The right GTM move is a narrow, concierge-led neighborhood pilot with merchant-first acquisition and one adjacent local channel, proving that a curated supply set can generate enough consumer activation and merchant interest to justify expansion.

## Growth Structural Decisions

- Define one primary acquisition motion explicitly as merchant-led distribution plus one neighborhood partner channel [market_motion]
- Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]


## Growth Recommendations

- Define one primary acquisition motion explicitly as merchant-led distribution plus one neighborhood partner channel [market_motion]
- Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Add a minimum merchant supply threshold required before consumer launch [scope]
- Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]
- Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]


## Growth Risks

- The neighborhood feed may still feel too thin even if it is curated well [scope]
- Users may not adopt a new discovery habit when Google Maps and social platforms already exist [demand_validation]
- Merchants may participate initially but not continue after the pilot [market_motion]


## Growth Open Questions

- How many merchants are required to make one neighborhood feel genuinely useful?
- Which exact merchant category mix produces the strongest first-session engagement?
- What is the one neighborhood partner channel most likely to reach the target audience efficiently?


## Product Arbitration

## Source

heuristic_fallback


## Retained

_Aucun élément retenu._


## Deferred

_Aucun élément différé._


## Rejected

- Tech: Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Tech: Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Tech: Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]
- Growth: Add a minimum merchant supply threshold required before consumer launch [scope]
- Growth: Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]


## Open Points

- Tech: Define a strict merchant approval workflow with publish/pause/expire states before build [workflow_control]
- Tech: Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Growth: Define one primary acquisition motion explicitly as merchant-led distribution plus one neighborhood partner channel [market_motion]
- Growth: Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Growth: Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]
- Tech: What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Tech: Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- Tech: What minimum merchant data is required for a listing to be publishable?
- Growth: How many merchants are required to make one neighborhood feel genuinely useful?
- Growth: Which exact merchant category mix produces the strongest first-session engagement?
- Growth: What is the one neighborhood partner channel most likely to reach the target audience efficiently?
- Tech recommendation needing arbitration: Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Tech recommendation needing arbitration: Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Tech recommendation needing arbitration: Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Tech recommendation needing arbitration: Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]
- Growth recommendation needing arbitration: Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Growth recommendation needing arbitration: Add a minimum merchant supply threshold required before consumer launch [scope]
- Growth recommendation needing arbitration: Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]
- Growth recommendation needing arbitration: Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]
- Tech open question: What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Tech open question: Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- Tech open question: What minimum merchant data is required for a listing to be publishable?
- Growth open question: How many merchants are required to make one neighborhood feel genuinely useful?
- Growth open question: Which exact merchant category mix produces the strongest first-session engagement?
- Growth open question: What is the one neighborhood partner channel most likely to reach the target audience efficiently?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
Consumers who want to support independent local businesses still default to large platforms because local discovery is fragmented, inconsistent, and time-consuming.

Local businesses, in turn, struggle to get found and to bring customers back without expensive marketing tools.

The MVP should prove one narrow claim: a simple, city-specific mobile discovery experience can drive enough customer intent to be valuable for both sides.

## Initial Wedge
Personalized nearby discovery of independent coffee shops, restaurants, and retail deals in one city.

This wedge is narrow enough to launch with limited supply, easy to understand for users, and close to a high-frequency behavior: “What should I try nearby right now?”

## First Target User
Urban residents and young professionals in one dense city neighborhood who are already open to trying independent local places but need a better way to discover them.

Secondary users:
- Tourists looking for nearby independent options
- Local businesses willing to trade simple offers for exposure

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- Groupon-style deal platforms
- Word-of-mouth and neighborhood newsletters

Switching trigger:
- Existing tools are broad, noisy, and not optimized for independent local businesses only
- Users want a faster way to find relevant nearby places without filtering through chains, stale listings, or irrelevant content
- Businesses want a lightweight way to get discovered by nearby customers without running full campaigns

## Core MVP Workflow
1. User opens the app and shares location.
2. App shows a small, curated list of nearby independent businesses.
3. Results are personalized by basic preferences such as food, coffee, shopping, or deals.
4. Each listing shows merchant name, category, distance, simple description, and a limited-time offer if available.
5. User taps to view the merchant profile and redeem an offer or save the place.
6. Merchant sees basic engagement and redemption counts.

## In Scope
- Location-based discovery in one city
- Personalized ranking using a small set of user preferences
- Merchant profile pages with basic business info
- Offers/promotions display
- Simple save/favorite action
- Basic offer redemption tracking
- Limited merchant onboarding for a curated set of businesses
- Mobile-first consumer experience
- Basic analytics for views and redemptions
- Curated business supply to keep relevance high

## Out of Scope
- Multi-city expansion
- Open marketplace self-serve merchant onboarding
- Full loyalty wallet or points engine
- Reviews and user-generated ratings
- Event feed
- Social sharing features
- Advanced recommendation engine
- Automated ad management
- Deep CRM or marketing automation for merchants
- Delivery, booking, or transaction processing
- Chain businesses as a primary supply strategy

## MVP Build Vs Pilot Operations
### Must Build Now
- Location-based nearby discovery feed
- Basic preference capture and ranking
- Merchant profile page
- Offer display
- Save/favorite action
- Basic redemption tracking
- Minimal merchant onboarding flow
- Simple admin view for supply and content management

### Manual Or Operational During Pilot
- Curate and approve initial merchants
- Write or clean up merchant descriptions
- Manually source and upload offers
- Seed supply in one neighborhood
- Support merchant questions and onboarding
- Monitor relevance and remove low-quality listings

### Deferred Until After Proof
- Full loyalty program
- Reviews and comments
- Event discovery
- Automated merchant self-serve tools
- Sophisticated recommendation models
- Multi-city rollout
- In-app messaging
- Revenue optimization tooling for merchants

## Business Model Hypothesis
Primary hypothesis:
- Charge local businesses a monthly subscription for being featured and receiving customer engagement tools

Secondary hypothesis:
- Offer premium placement or campaign boosts later, once discovery demand is proven

For MVP validation, revenue can be tested with a small paid pilot or a willingness-to-pay interview rather than requiring full monetization on day one.

## Critical Assumptions
- Enough users in one city will install and use a local-only discovery app
- Curated local supply is sufficient to make the feed feel valuable
- Independent businesses will join despite limited tooling
- Personalized nearby recommendations outperform generic search for this use case
- Offers and simple discovery are enough to create repeat usage
- The product can maintain relevance without becoming saturated with low-quality listings

## How To Test Quickly
- Launch in one dense neighborhood or city zone
- Recruit 20 to 50 independent businesses with a small set of offers
- Run a concierge pilot with manually curated listings
- Measure whether users browse, save, and redeem offers
- Interview merchants on perceived value after initial exposure
- Test whether users return within 2 to 4 weeks
- Compare engagement against a simple curated list or newsletter baseline

## Acceptance Criteria
- User can see nearby independent businesses based on location
- User can apply at least a few basic preferences
- User can open a merchant profile and view an active offer
- User can save a business or redeem an offer
- Merchant engagement/redemption can be tracked
- Curated supply is sufficient to avoid a barren feed
- At least a small cohort of users return after initial use
- At least a subset of merchants express willingness to continue or pay

## Risks And Failure Modes
- Supply problem: too few quality local businesses in one area
- Relevance problem: recommendations feel generic or repetitive
- Trust problem: stale offers or inaccurate merchant information
- Adoption problem: users already rely on Google Maps or Yelp
- Merchant value problem: businesses do not see enough customer lift
- Operational burden: manual curation becomes expensive to sustain
- Market positioning risk: drifting into a broad local platform instead of a focused wedge

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Insufficient proof that users will switch from existing discovery tools [switching_trigger]
- Unproven merchant willingness to join and maintain offers [merchant_supply]
- No evidence yet that curated local discovery produces repeat usage [retention_signal]

Required Improvements:
- Run a concierge pilot in one neighborhood with real users and merchants [pilot_validation]
- Test willingness to pay or continued participation with a small merchant cohort [merchant_validation]
- Measure repeat opens, saves, and redemptions over a short interval [retention_test]

## Recommendation
Proceed with a narrow concierge pilot rather than a full build.

Keep the MVP focused on nearby discovery of independent businesses with basic offers and minimal personalization. Do not add loyalty, reviews, or events until the core loop proves that users engage repeatedly and merchants see clear value.

## Retained Decisions

_Aucune décision retenue._

## Deferred Decisions

_Aucune décision différée._

## Rejected Recommendations

- Tech: Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Tech: Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Tech: Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]
- Growth: Add a minimum merchant supply threshold required before consumer launch [scope]
- Growth: Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]

## Unresolved Tensions

- Tech recommendation needing arbitration: Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Tech recommendation needing arbitration: Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Tech recommendation needing arbitration: Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Tech recommendation needing arbitration: Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]
- Growth recommendation needing arbitration: Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Growth recommendation needing arbitration: Add a minimum merchant supply threshold required before consumer launch [scope]
- Growth recommendation needing arbitration: Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]
- Growth recommendation needing arbitration: Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]
- Tech open question: What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Tech open question: Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- Tech open question: What minimum merchant data is required for a listing to be publishable?
- Growth open question: How many merchants are required to make one neighborhood feel genuinely useful?
- Growth open question: Which exact merchant category mix produces the strongest first-session engagement?
- Growth open question: What is the one neighborhood partner channel most likely to reach the target audience efficiently?

## Applied Changes

_Aucun changement appliqué._

## Remaining Open Points

- Tech: Define a strict merchant approval workflow with publish/pause/expire states before build [workflow_control]
- Tech: Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Growth: Define one primary acquisition motion explicitly as merchant-led distribution plus one neighborhood partner channel [market_motion]
- Growth: Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Growth: Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]
- Tech: What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Tech: Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- Tech: What minimum merchant data is required for a listing to be publishable?
- Growth: How many merchants are required to make one neighborhood feel genuinely useful?
- Growth: Which exact merchant category mix produces the strongest first-session engagement?
- Growth: What is the one neighborhood partner channel most likely to reach the target audience efficiently?
- Tech recommendation needing arbitration: Add a mandatory last-reviewed timestamp and stale-listing hiding rule for every public listing [data_freshness]
- Tech recommendation needing arbitration: Replace any implied “merchant self-serve” MVP plan with admin-first content management [admin_first]
- Tech recommendation needing arbitration: Specify the exact redemption mechanism for the pilot, including how it is verified and logged [redemption_tracking]
- Tech recommendation needing arbitration: Narrow “personalized recommendations” to rule-based preference matching for MVP [rule_based_logic]
- Growth recommendation needing arbitration: Specify the smallest credible launch audience as people living, working, or spending time within a 10–15 minute walk of pilot merchants [scope]
- Growth recommendation needing arbitration: Add a minimum merchant supply threshold required before consumer launch [scope]
- Growth recommendation needing arbitration: Add a launch decision rule for the merchant side, e.g. how many merchants must be active and fresh before opening to users [metrics_validation]
- Growth recommendation needing arbitration: Clarify the first activation metric and the return metric used to judge whether the pilot is working [metrics_validation]
- Tech open question: What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Tech open question: Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- Tech open question: What minimum merchant data is required for a listing to be publishable?
- Growth open question: How many merchants are required to make one neighborhood feel genuinely useful?
- Growth open question: Which exact merchant category mix produces the strongest first-session engagement?
- Growth open question: What is the one neighborhood partner channel most likely to reach the target audience efficiently?

## Risks

- Stale or inaccurate offers could quickly destroy trust [data_freshness]
- Merchant supply may be too thin to produce a credible feed [merchant_supply]
- Duplicate or fraudulent redemption events may distort value measurement [fraud_control]
- Users default back to Google Maps, Yelp, or social discovery after first use.
- Merchant supply becomes stale and the feed loses credibility quickly.
- The app feels too broad if coffee, restaurants, retail, and events all launch together.
- Merchants do not actively promote the app, limiting distribution. [market_motion]
- The neighborhood inventory is too thin to feel meaningfully better than Google Maps. [demand_validation]
- Users sample once but do not return because the use case is too occasional. [retention_risk]
- The neighborhood feed may still feel too thin even if it is curated well [scope]
- Users may not adopt a new discovery habit when Google Maps and social platforms already exist [demand_validation]
- Merchants may participate initially but not continue after the pilot [market_motion]

## Open Questions

- What is the exact redemption flow: QR code, code word, in-person verification, or merchant confirmation?
- Will users need accounts, or can the MVP support anonymous sessions with device-based state?
- What minimum merchant data is required for a listing to be publishable?
- What is the exact neighborhood or district for the pilot?
- How many merchants are needed before the consumer feed feels “alive”?
- What offer format is easiest for merchants to maintain and most compelling for users?
- How many active merchants are required before the feed feels complete in one neighborhood? [scope]
- Which merchant category is the strongest wedge: coffee, quick food, or retail? [scope]
- What specific merchant action counts as successful participation in the pilot? [metrics_validation]
- How many merchants are required to make one neighborhood feel genuinely useful?
- Which exact merchant category mix produces the strongest first-session engagement?
- What is the one neighborhood partner channel most likely to reach the target audience efficiently?

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support independent local businesses default to Google Maps, Yelp, Instagram, and deal platforms because local discovery is fragmented, noisy, and hard to trust.

Independent businesses need nearby customer attention, but they cannot support complex marketing tools or broad platform overhead.

The MVP must prove a narrow claim: a curated, neighborhood-level discovery feed for independent businesses can create repeat user engagement and enough merchant value to justify expansion.

## Initial Wedge
A concierge-curated discovery feed for one dense neighborhood, focused first on independent coffee shops and quick-service restaurants.

This is the narrowest credible wedge because it concentrates supply, keeps relevance manageable, and avoids direct competition with horizontal discovery platforms.

## First Target User
Primary target:
- Urban residents and young professionals who live, work, or spend time within a 10–15 minute walk of the pilot neighborhood

Secondary pilot users:
- Nearby families and tourists already in the same area
- Independent merchants willing to trial a low-lift exposure channel

## Existing Alternatives And Switching Trigger
Current alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok discovery
- Groupon-style deals
- Word of mouth and neighborhood newsletters

Switching trigger:
- Existing tools are broad, cluttered, and not optimized for independent local businesses only
- Users want a faster, more relevant way to find nearby independent places without sorting through chains, stale listings, or unrelated content
- Merchants want local visibility without running full campaigns or adopting heavy tooling

## Core MVP Workflow
1. Admin curates and approves merchants for a single neighborhood.
2. Each merchant listing includes category, location, short description, and one active offer if available.
3. Every public listing shows a last-reviewed timestamp and is hidden automatically if stale.
4. User shares location and sees a small nearby feed ranked by proximity and a few explicit preferences.
5. User opens a merchant profile, saves the place, or redeems the offer.
6. Redemption is verified through a simple pilot flow and logged for both user and merchant tracking.
7. Admin monitors feed quality, pauses stale listings, and updates merchant content as needed.

## In Scope
- One-neighborhood launch
- One consumer segment: people within a 10–15 minute walk of pilot merchants
- Nearby discovery feed
- Rule-based preference matching for ranking
- Merchant profile pages with essential business info
- Offer display
- Save/favorite action
- Simple redemption verification and logging
- Admin-first merchant approval and publishing
- Publish / pause / expire listing states
- Mandatory last-reviewed timestamp for public listings
- Stale-listing hiding rule
- Basic analytics for views, saves, redemptions, active merchants, active offers, and freshness coverage
- Curated supply to maintain relevance
- Mobile-first consumer experience
- Minimum merchant supply threshold before consumer launch

## Out of Scope
- Multi-city expansion
- Open merchant self-serve onboarding
- Full loyalty points wallet
- Reviews and user-generated ratings
- Event feed
- Social sharing features
- Advanced machine learning recommendations
- Automated ad management
- Deep CRM or marketing automation
- Delivery, booking, or payment processing
- Chain businesses as a primary supply strategy
- Complex merchant dashboards
- Broad citywide consumer launch

## MVP Build Vs Pilot Operations
### Must Build Now
- Nearby discovery feed
- Rule-based ranking using a small set of preferences
- Merchant profile page
- Offer display
- Save/favorite action
- Simple redemption verification and logging
- Admin-first content management
- Publish / pause / expire listing states
- Last-reviewed timestamp display
- Stale-listing hiding rule
- Basic analytics for views, saves, redemptions, active merchants, active offers, and freshness coverage

### Manual Or Operational During Pilot
- Curate and approve merchants
- Write or clean up merchant descriptions
- Source and upload offers
- Verify listings are current
- Manually refresh stale content
- Support merchant onboarding and questions
- Monitor feed quality and suppress low-quality listings
- Run redemption verification if needed
- Enforce the minimum merchant supply threshold before opening to users

### Deferred Until After Proof
- Full loyalty program
- Reviews and comments
- Event discovery
- Automated merchant self-serve tools
- Sophisticated recommendation models
- Multi-neighborhood or multi-city rollout
- In-app messaging
- Revenue optimization tooling for merchants

## Business Model Hypothesis
Primary hypothesis:
- Charge local businesses a monthly subscription for inclusion and ongoing featured exposure in a curated neighborhood feed

Pilot hypothesis:
- A small set of merchants will continue participating, or express willingness to pay, if the feed delivers measurable nearby attention or redemptions

Secondary later hypothesis:
- Premium placement or campaign boosts may become viable after discovery demand is proven

## Critical Assumptions
- A single neighborhood can generate enough supply to make the feed feel useful
- Users will engage with a local-only discovery app instead of defaulting to existing platforms
- Independent businesses will accept a manually managed pilot in exchange for exposure
- Rule-based matching is good enough to feel personalized at MVP stage
- Offers and save/redemption actions are sufficient to show value
- Supply can stay accurate enough to avoid stale or misleading listings
- One dense neighborhood with a sufficient merchant count can produce a credible discovery experience

## How To Test Quickly
- Launch in one dense neighborhood, not a full city
- Secure a minimum curated merchant set before consumer launch
- Run a concierge pilot with manual merchant approval and offer setup
- Make save or redeem the first activation event
- Track repeat opens over a short interval as the retention signal
- Track merchant continuation or willingness to pay after initial exposure
- Compare engagement to a simple curated list or neighborhood newsletter baseline

## Acceptance Criteria
- User can see nearby independent businesses in the pilot neighborhood
- User can apply basic preferences and receive a ranked feed
- User can open a merchant profile and view an active offer
- User can save a business
- User can redeem an offer through a defined pilot flow
- Redemption is logged and attributable
- Every public listing has a last-reviewed timestamp
- Stale listings are hidden automatically
- Merchants are manually approved before publish
- A minimum merchant supply threshold is met before consumer launch
- Feed quality remains high enough that users are not seeing obvious stale or irrelevant listings
- A pilot cohort shows save or redeem behavior within the test window
- A pilot cohort shows repeat opens within the test window
- A subset of merchants indicates willingness to continue or pay

## Risks And Failure Modes
- Supply risk: too few quality merchants in one neighborhood
- Freshness risk: stale or inaccurate listings erode trust quickly
- Relevance risk: rule-based personalization feels generic
- Adoption risk: users continue to rely on existing discovery tools
- Merchant value risk: businesses do not see enough lift to continue
- Operational risk: manual curation becomes too costly to sustain
- Positioning risk: the product drifts toward a broad local platform instead of a disciplined wedge

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Need proof that one neighborhood and a curated merchant set can beat default discovery habits [demand_validation]
- Need evidence that merchants will continue participation or pay after the pilot [market_motion]
- Need a defined success gate using activation, retention, merchant supply, and freshness coverage [metrics_validation]

Required Improvements:
- Run a concierge pilot in one dense neighborhood with real users and merchants [operations]
- Define the minimum merchant supply threshold before consumer launch [scope]
- Measure save or redeem as the first activation event [metrics_validation]
- Track repeat opens over a short interval as the retention signal [metrics_validation]
- Track merchant continuation or willingness-to-pay after initial exposure [market_motion]

## Recommendation
Proceed with a narrow concierge pilot, not a broader build.

Keep the MVP limited to one dense neighborhood, one consumer segment, curated supply, rule-based ranking, basic offers, and simple redemption tracking. Do not add loyalty, reviews, events, or automated self-serve tooling until the core loop proves that users engage repeatedly and merchants see enough value to stay.

Decision rule for the pilot:
- Proceed if at least 30% of activated users save or redeem within the test window, at least 20% of activated users return for a second open within 14 days, at least 10 merchants are active, at least 80% of live listings are fresh, and at least 5 merchants express willingness to continue or pay
- Revise if engagement is meaningful but one of the thresholds is missed
- Reject if the feed cannot stay fresh, users do not activate, or merchants do not see credible value

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
- product_agent: prd_draft_revised
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- growth_agent: gtm_notes_generated
- product_agent: product_arbitration_fallback_used
- product_agent: prd_draft_revised
- product_agent: product_locking_applied
