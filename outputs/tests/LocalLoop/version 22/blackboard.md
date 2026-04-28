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
- verified merchant supply in one launch neighborhood

### operations
- [operations] evidence that users prefer this workflow over existing discovery tools

### market_motion
- [market_motion] one redemption flow proven to be reliable and auditable in pilot conditions

## Product Required Improvements

### untagged
- define the single launch neighborhood and minimum merchant density threshold
- enforce listing freshness rules for hours, offers, and merchant status before broader release

### market_motion
- [market_motion] run a concierge pilot to validate offer quality and repeat usage before scaling
- [market_motion] keep merchant onboarding admin-managed until the pilot proves repeatable operations

### scope
- [scope] keep the category wedge limited to coffee and lunch until proof is achieved

## Tech Status

LIMITED


## Tech Blocking Gaps

### untagged
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined.
- The redemption model is not specified tightly enough to guarantee reliable loyalty state.

### operations
- [operations] The operational ownership model for merchant data updates and dispute handling is still implicit.

## Tech Required Improvements

### untagged
- Lock the launch geography and minimum active merchant threshold before build start.

### scope
- [scope] Choose one auditable redemption flow and encode it as the only MVP path.

### operations
- [operations] Define the internal ops workflow and admin permissions for content approval, updates, and support.

## Growth Status

LIMITED


## Growth Blocking Gaps

### untagged
- Exact launch neighborhood and merchant density threshold are not locked

### operations
- [operations] First audience is still broader than the pilot can support

### market_motion
- [market_motion] First launch motion is not yet committed as founder-led concierge only

## Growth Required Improvements

### untagged
- Freeze one neighborhood and define the minimum merchant count needed for credibility
- Narrow the first user set to nearby workers/residents making same-day decisions

### operations
- [operations] Commit to a concierge pilot with manual merchant ops before any broader launch

### market_motion
- [market_motion] Define the first activation loop and repeat-visit incentive as one simple behavior chain

## Global Status

LIMITED


## Global Blocking Gaps

### untagged
- verified merchant supply in one launch neighborhood
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined.
- The redemption model is not specified tightly enough to guarantee reliable loyalty state.
- Exact launch neighborhood and merchant density threshold are not locked

### operations
- [operations] evidence that users prefer this workflow over existing discovery tools
- [operations] The operational ownership model for merchant data updates and dispute handling is still implicit.
- [operations] First audience is still broader than the pilot can support

### market_motion
- [market_motion] one redemption flow proven to be reliable and auditable in pilot conditions
- [market_motion] First launch motion is not yet committed as founder-led concierge only

## Global Required Improvements

### untagged
- define the single launch neighborhood and minimum merchant density threshold
- enforce listing freshness rules for hours, offers, and merchant status before broader release
- Lock the launch geography and minimum active merchant threshold before build start.
- Freeze one neighborhood and define the minimum merchant count needed for credibility
- Narrow the first user set to nearby workers/residents making same-day decisions

### market_motion
- [market_motion] run a concierge pilot to validate offer quality and repeat usage before scaling
- [market_motion] keep merchant onboarding admin-managed until the pilot proves repeatable operations
- [market_motion] Define the first activation loop and repeat-visit incentive as one simple behavior chain

### scope
- [scope] keep the category wedge limited to coffee and lunch until proof is achieved
- [scope] Choose one auditable redemption flow and encode it as the only MVP path.

### operations
- [operations] Define the internal ops workflow and admin permissions for content approval, updates, and support.
- [operations] Commit to a concierge pilot with manual merchant ops before any broader launch

## Known Tags

- operations
- untagged
- market_motion
- scope


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

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] one redemption flow proven to be reliable and auditable in pilot conditions run a concierge pilot to validate offer quality and repeat usage before scaling keep merchant onboarding admin-managed until the pilot proves repeatable operations Secure a minimum merchant set and verify offer freshness in the pilot zone Run a concierge pilot that tests repeat opens, saves, and redemptions against current alternatives


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] Choose one auditable redemption flow and encode it as the only MVP path. Lock the first city and one launch neighborhood before expanding scope


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech
- growth


#### Product Task

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] evidence that users prefer this workflow over existing discovery tools The operational ownership model for merchant data updates and dispute handling is still implicit. Define the internal ops workflow and admin permissions for content approval, updates, and support.


## Expected Output

A clear product decision on build-versus-manual scope.


## Contributors

- tech


### Loop 2

#### Growth Task

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] one redemption flow proven to be reliable and auditable in pilot conditions run a concierge pilot to validate offer quality and repeat usage before scaling keep merchant onboarding admin-managed until the pilot proves repeatable operations The narrowest credible consumer audience is still broad, which makes early acquisition and messaging too diffuse. The first market motion is implied but not locked to a single pilot motion, leaving the launch strategy too vague. Commit to a founder-led concierge pilot as the only initial launch path. Define the exact activation loop and repeat-visit incentive for the first version.


## Expected Output

A concrete launch motion for the smallest credible audience.


## Contributors

_Aucun contributeur._


#### Product Task

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] keep the category wedge limited to coffee and lunch until proof is achieved Choose one auditable redemption flow and encode it as the only MVP path. Restrict the first consumer audience to people with repeated proximity and frequent local intent.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


## Contributors

- tech
- growth


#### Product Task

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] evidence that users prefer this workflow over existing discovery tools The operational ownership model for merchant data updates and dispute handling is still implicit. Define the internal ops workflow and admin permissions for content approval, updates, and support.


## Expected Output

A clear product decision on build-versus-manual scope.


## Contributors

- tech


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
- verified merchant supply in one launch neighborhood
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined.
- The redemption model is not specified tightly enough to guarantee reliable loyalty state.
- No defined launch neighborhood or merchant density threshold
- Merchant supply not yet proven in a single dense area
- User differentiation versus existing discovery tools remains unproven

### operations
- [operations] evidence that users prefer this workflow over existing discovery tools
- [operations] The operational ownership model for merchant data updates and dispute handling is still implicit.

### market_motion
- [market_motion] one redemption flow proven to be reliable and auditable in pilot conditions

## Global Required Improvements

### untagged
- define the first launch neighborhood and minimum merchant density threshold
- enforce listing freshness rules for hours, offers, and merchant status before broader release
- Lock the launch geography and minimum active merchant threshold before build start.

### market_motion
- [market_motion] run a concierge pilot to validate offer quality and repeat usage before scaling
- [market_motion] keep merchant onboarding admin-managed until the pilot proves repeatable operations
- [market_motion] Secure a minimum merchant set and verify offer freshness in the pilot zone
- [market_motion] Run a concierge pilot that tests repeat opens, saves, and redemptions against current alternatives

### scope
- [scope] Choose one auditable redemption flow and encode it as the only MVP path.
- [scope] Lock the first city and one launch neighborhood before expanding scope

### operations
- [operations] Define the internal ops workflow and admin permissions for content approval, updates, and support.

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] one redemption flow proven to be reliable and auditable in pilot conditions run a concierge pilot to validate offer quality and repeat usage before scaling keep merchant onboarding admin-managed until the pilot proves repeatable operations Secure a minimum merchant set and verify offer freshness in the pilot zone Run a concierge pilot that tests repeat opens, saves, and redemptions against current alternatives


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] Choose one auditable redemption flow and encode it as the only MVP path. Lock the first city and one launch neighborhood before expanding scope


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] evidence that users prefer this workflow over existing discovery tools The operational ownership model for merchant data updates and dispute handling is still implicit. Define the internal ops workflow and admin permissions for content approval, updates, and support.


## Expected Output

A clear product decision on build-versus-manual scope.


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
- verified merchant supply in one launch neighborhood
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined.
- The redemption model is not specified tightly enough to guarantee reliable loyalty state.
- No specific first neighborhood or merchant density threshold is defined, so the launch cannot be sized credibly.

### operations
- [operations] evidence that users prefer this workflow over existing discovery tools
- [operations] The operational ownership model for merchant data updates and dispute handling is still implicit.

### market_motion
- [market_motion] one redemption flow proven to be reliable and auditable in pilot conditions
- [market_motion] The narrowest credible consumer audience is still broad, which makes early acquisition and messaging too diffuse.
- [market_motion] The first market motion is implied but not locked to a single pilot motion, leaving the launch strategy too vague.

## Global Required Improvements

### untagged
- define the single launch neighborhood and minimum merchant density threshold
- enforce listing freshness rules for hours, offers, and merchant status before broader release
- Lock the launch geography and minimum active merchant threshold before build start.
- Pick one city, one neighborhood, and a minimum viable merchant count before any broader rollout.

### market_motion
- [market_motion] run a concierge pilot to validate offer quality and repeat usage before scaling
- [market_motion] keep merchant onboarding admin-managed until the pilot proves repeatable operations
- [market_motion] Commit to a founder-led concierge pilot as the only initial launch path.
- [market_motion] Define the exact activation loop and repeat-visit incentive for the first version.

### scope
- [scope] keep the category wedge limited to coffee and lunch until proof is achieved
- [scope] Choose one auditable redemption flow and encode it as the only MVP path.
- [scope] Restrict the first consumer audience to people with repeated proximity and frequent local intent.

### operations
- [operations] Define the internal ops workflow and admin permissions for content approval, updates, and support.

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] one redemption flow proven to be reliable and auditable in pilot conditions run a concierge pilot to validate offer quality and repeat usage before scaling keep merchant onboarding admin-managed until the pilot proves repeatable operations Secure a minimum merchant set and verify offer freshness in the pilot zone Run a concierge pilot that tests repeat opens, saves, and redemptions against current alternatives


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] Choose one auditable redemption flow and encode it as the only MVP path. Lock the first city and one launch neighborhood before expanding scope


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] evidence that users prefer this workflow over existing discovery tools The operational ownership model for merchant data updates and dispute handling is still implicit. Define the internal ops workflow and admin permissions for content approval, updates, and support.


## Expected Output

A clear product decision on build-versus-manual scope.


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
- verified merchant supply in one launch neighborhood
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined.
- The redemption model is not specified tightly enough to guarantee reliable loyalty state.
- No specific first neighborhood or merchant density threshold is defined, so the launch cannot be sized credibly.

### operations
- [operations] evidence that users prefer this workflow over existing discovery tools
- [operations] The operational ownership model for merchant data updates and dispute handling is still implicit.

### market_motion
- [market_motion] one redemption flow proven to be reliable and auditable in pilot conditions
- [market_motion] The narrowest credible consumer audience is still broad, which makes early acquisition and messaging too diffuse.
- [market_motion] The first market motion is implied but not locked to a single pilot motion, leaving the launch strategy too vague.

## Global Required Improvements

### untagged
- define the single launch neighborhood and minimum merchant density threshold
- enforce listing freshness rules for hours, offers, and merchant status before broader release
- Lock the launch geography and minimum active merchant threshold before build start.
- Pick one city, one neighborhood, and a minimum viable merchant count before any broader rollout.

### market_motion
- [market_motion] run a concierge pilot to validate offer quality and repeat usage before scaling
- [market_motion] keep merchant onboarding admin-managed until the pilot proves repeatable operations
- [market_motion] Commit to a founder-led concierge pilot as the only initial launch path.
- [market_motion] Define the exact activation loop and repeat-visit incentive for the first version.

### scope
- [scope] keep the category wedge limited to coffee and lunch until proof is achieved
- [scope] Choose one auditable redemption flow and encode it as the only MVP path.
- [scope] Restrict the first consumer audience to people with repeated proximity and frequent local intent.

### operations
- [operations] Define the internal ops workflow and admin permissions for content approval, updates, and support.

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] one redemption flow proven to be reliable and auditable in pilot conditions run a concierge pilot to validate offer quality and repeat usage before scaling keep merchant onboarding admin-managed until the pilot proves repeatable operations The narrowest credible consumer audience is still broad, which makes early acquisition and messaging too diffuse. The first market motion is implied but not locked to a single pilot motion, leaving the launch strategy too vague. Commit to a founder-led concierge pilot as the only initial launch path. Define the exact activation loop and repeat-visit incentive for the first version.


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] keep the category wedge limited to coffee and lunch until proof is achieved Choose one auditable redemption flow and encode it as the only MVP path. Restrict the first consumer audience to people with repeated proximity and frequent local intent.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] evidence that users prefer this workflow over existing discovery tools The operational ownership model for merchant data updates and dispute handling is still implicit. Define the internal ops workflow and admin permissions for content approval, updates, and support.


## Expected Output

A clear product decision on build-versus-manual scope.


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
- verified merchant supply in one launch neighborhood
- One launch neighborhood with verified merchant density and freshness commitments is not yet defined.
- The redemption model is not specified tightly enough to guarantee reliable loyalty state.
- Exact launch neighborhood and merchant density threshold are not locked

### operations
- [operations] evidence that users prefer this workflow over existing discovery tools
- [operations] The operational ownership model for merchant data updates and dispute handling is still implicit.
- [operations] First audience is still broader than the pilot can support

### market_motion
- [market_motion] one redemption flow proven to be reliable and auditable in pilot conditions
- [market_motion] First launch motion is not yet committed as founder-led concierge only

## Global Required Improvements

### untagged
- define the single launch neighborhood and minimum merchant density threshold
- enforce listing freshness rules for hours, offers, and merchant status before broader release
- Lock the launch geography and minimum active merchant threshold before build start.
- Freeze one neighborhood and define the minimum merchant count needed for credibility
- Narrow the first user set to nearby workers/residents making same-day decisions

### market_motion
- [market_motion] run a concierge pilot to validate offer quality and repeat usage before scaling
- [market_motion] keep merchant onboarding admin-managed until the pilot proves repeatable operations
- [market_motion] Define the first activation loop and repeat-visit incentive as one simple behavior chain

### scope
- [scope] keep the category wedge limited to coffee and lunch until proof is achieved
- [scope] Choose one auditable redemption flow and encode it as the only MVP path.

### operations
- [operations] Define the internal ops workflow and admin permissions for content approval, updates, and support.
- [operations] Commit to a concierge pilot with manual merchant ops before any broader launch

## Loop Tasks

##### Growth

## Task

Clarify the narrowest credible launch audience and first market motion.


## Source Gap

[market_motion] one redemption flow proven to be reliable and auditable in pilot conditions run a concierge pilot to validate offer quality and repeat usage before scaling keep merchant onboarding admin-managed until the pilot proves repeatable operations The narrowest credible consumer audience is still broad, which makes early acquisition and messaging too diffuse. The first market motion is implied but not locked to a single pilot motion, leaving the launch strategy too vague. Commit to a founder-led concierge pilot as the only initial launch path. Define the exact activation loop and repeat-visit incentive for the first version.


## Expected Output

A concrete launch motion for the smallest credible audience.


##### Product

## Task

Clarify the narrowest credible wedge and remove anything not needed for proof.


## Source Gap

[scope] keep the category wedge limited to coffee and lunch until proof is achieved Choose one auditable redemption flow and encode it as the only MVP path. Restrict the first consumer audience to people with repeated proximity and frequent local intent.


## Expected Output

A clear product decision that narrows the wedge and removes accessories.


##### Product

## Task

Clarify what must be built versus what can stay manual during MVP.


## Source Gap

[operations] evidence that users prefer this workflow over existing discovery tools The operational ownership model for merchant data updates and dispute handling is still implicit. Define the internal ops workflow and admin permissions for content approval, updates, and support.


## Expected Output

A clear product decision on build-versus-manual scope.


## Expert Decisions

## Tech Structural Decisions

### tech
- [tech] **Manual merchant content management first, self-serve later**
- [tech] **Deterministic ranking, not ML personalization**
- [tech] **Redemption must be simple and auditable**
- [tech] Mobile app for users

## Growth Structural Decisions

### growth
- [growth] Define one exact launch neighborhood and the minimum merchant count needed for the feed to look credible. [launch_focus]
- [growth] Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]

## Product Locking

## Applied

True


## Confirmed In Scope

- one city
- one launch neighborhood
- coffee and lunch only
- curated nearby discovery feed
- merchant profiles with essential info
- one active offer per merchant
- save/favorite
- simple loyalty tracking
- one auditable redemption flow
- deterministic ranking
- internal admin-managed merchant onboarding and approvals
- listing freshness checks
- ops console for verification and disputes


## Confirmed Deferred

- reviews and ratings
- event discovery
- advanced personalization
- automated recommendation engine
- self-serve merchant onboarding
- multi-city expansion tools
- cross-merchant loyalty wallet
- payments and checkout
- additional categories
- broader consumer acquisition automation


## Confirmed Out Of Scope

- chains and franchises
- complex social features
- in-app messaging
- table booking, ordering, delivery
- merchant advertising marketplace
- anonymous public UGC moderation
- multiple redemption mechanisms
- broad launch beyond the pilot neighborhood


## Locking Note

- Scope is intentionally narrower than a general local discovery product. - Keep the pilot operationally managed and do not broaden categories, channels, or redemption paths before proof.


## Expert Contributions

### Tech Summary

The MVP is feasible only if it is treated as a controlled local pilot with manual merchant operations and a strict redemption ledger. The main risk is not feature breadth; it is whether the system can maintain accurate local supply and trustworthy offer state in one city without overbuilding merchant self-service or personalization.

## Tech Structural Decisions

- **Manual merchant content management first, self-serve later**
- **Deterministic ranking, not ML personalization**
- **Redemption must be simple and auditable**
- Mobile app for users


## Tech Recommendations

- Define the single launch city and 2–3 initial neighborhoods before implementation. [launch_focus]
- Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]


## Tech Risks

- Inaccurate or stale business/offer data will quickly erode trust. [data_freshness]
- Redemption ambiguity could break loyalty and create support overhead. [redemption_reliability]
- Feed quality may be too weak if neighborhood supply is thin. [supply_validation]


## Tech Open Questions

_Aucune question._


### Growth Summary

The launch challenge is not building a fuller discovery platform; it is proving that one dense neighborhood can sustain enough merchant supply and repeat user intent to feel useful. The recommended direction is a founder-led concierge pilot in one neighborhood with a narrow coffee/lunch audience, one redemption loop, and manual merchant operations until the market shows repeat engagement.

## Growth Structural Decisions

- Define one exact launch neighborhood and the minimum merchant count needed for the feed to look credible. [launch_focus]
- Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]


## Growth Recommendations

- Define one exact launch neighborhood and the minimum merchant count needed for the feed to look credible. [launch_focus]
- Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]
- Narrow the first audience to people who live or work within walking distance of the launch neighborhood. [audience_narrowing]
- Define the first activation loop around “open → see 3–7 relevant places → save/redeem → return for fresh local options.” [activation_loop]
- Specify the repeat-visit incentive as a simple loyalty reward tied to one merchant or one visit pattern, not a broad universal wallet. [loyalty_loop]


## Growth Risks

- The merchant feed may look empty or stale if density is insufficient. [supply_validation]
- Consumers may not see enough advantage over Google Maps or Yelp. [user_differentiation]
- Offer quality may be too uneven, hurting trust quickly. [offer_quality]


## Growth Open Questions

- Which exact neighborhood is dense enough to support the pilot?
- How many merchants are needed before the app feels credible?
- What is the single redemption method that is easiest to audit in person?


## Product Arbitration

## Source

heuristic_fallback


## Retained

- Tech: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]


## Deferred

_Aucun élément différé._


## Rejected

- Tech: Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Tech: Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Growth: Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]
- Growth: Narrow the first audience to people who live or work within walking distance of the launch neighborhood. [audience_narrowing]


## Open Points

- Tech: Define the single launch city and 2–3 initial neighborhoods before implementation. [launch_focus]
- Tech: Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Growth: Define one exact launch neighborhood and the minimum merchant count needed for the feed to look credible. [launch_focus]
- Growth: Define the first activation loop around “open → see 3–7 relevant places → save/redeem → return for fresh local options.” [activation_loop]
- Growth: Specify the repeat-visit incentive as a simple loyalty reward tied to one merchant or one visit pattern, not a broad universal wallet. [loyalty_loop]
- Growth: Which exact neighborhood is dense enough to support the pilot?
- Growth: How many merchants are needed before the app feels credible?
- Growth: What is the single redemption method that is easiest to audit in person?
- Tech recommendation needing arbitration: Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Tech recommendation needing arbitration: Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Tech recommendation needing arbitration: Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Tech recommendation needing arbitration: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]
- Growth recommendation needing arbitration: Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]
- Growth recommendation needing arbitration: Narrow the first audience to people who live or work within walking distance of the launch neighborhood. [audience_narrowing]
- Growth recommendation needing arbitration: Define the first activation loop around “open → see 3–7 relevant places → save/redeem → return for fresh local options.” [activation_loop]
- Growth recommendation needing arbitration: Specify the repeat-visit incentive as a simple loyalty reward tied to one merchant or one visit pattern, not a broad universal wallet. [loyalty_loop]
- Growth open question: Which exact neighborhood is dense enough to support the pilot?
- Growth open question: How many merchants are needed before the app feels credible?
- Growth open question: What is the single redemption method that is easiest to audit in person?


## Rationales

_Aucune rationale._


## Source PRD

_Aucun contenu._

## Initial PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local independent businesses still default to large discovery platforms because local options are fragmented, hard to compare, and not personalized.

Independent businesses, meanwhile, need a simple way to get discovered and bring customers back, but most marketing tools are too broad, too expensive, or too complex.

The product problem for the MVP is not “build a full local commerce platform.” It is:
- help one user segment quickly discover a few relevant local businesses nearby
- prove that merchants will participate if the offer is simple
- prove that a repeatable discovery-to-visit loop exists in one city

## Initial Wedge
A neighborhood-based mobile discovery app for urban residents and young professionals that surfaces nearby independent coffee shops, restaurants, and small retailers with simple promotions and a lightweight loyalty reward.

The narrow wedge:
- one city
- a few dense neighborhoods
- one high-frequency use case: “What local place should I go to right now?”
- one merchant value proposition: “List a promotion and get nearby customers”

This wedge is credible because it focuses on repeat behavior and immediate intent, rather than broad lifestyle discovery.

## First Target User
Primary user:
- urban residents and young professionals living in the launch city
- already use mobile discovery apps
- interested in trying local businesses but need convenience and relevance

First use case:
- finding a nearby independent coffee shop, restaurant, or casual retail store with an offer or loyalty incentive within the user’s current neighborhood

Secondary user for the pilot:
- independent business owners or managers in those same neighborhoods who want foot traffic and repeat visits without running campaigns themselves

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok
- delivery and deal apps
- word of mouth
- merchant-specific loyalty apps

Why users switch:
- the current tools are broad, cluttered, and not neighborhood-specific enough
- offers are scattered across channels and hard to compare
- loyalty is fragmented across individual merchants
- independent businesses are hard to discover unless the user already knows them

Why merchants switch:
- they need a simple way to get discovered locally
- they want something lighter than full ad platforms or loyalty infrastructure
- they will participate if setup is minimal and they can see nearby customer traffic

## Core MVP Workflow
1. User opens app and shares location or selects a neighborhood.
2. App shows a curated feed of nearby independent businesses.
3. User filters by category and sees a small number of relevant recommendations.
4. User taps a merchant profile to view:
   - basic details
   - offer or promotion
   - distance
   - hours
   - loyalty reward if available
5. User saves the place or redeems an offer in person.
6. Merchant records redemption or visit through a simple code/manual confirmation.
7. User accumulates a basic loyalty reward after repeat visits.

The MVP should prove that:
- neighborhood discovery is useful
- offers increase intent
- a simple loyalty mechanic encourages return visits
- merchants can manage participation with low friction

## In Scope
- location-based browsing within one city
- neighborhood and category filtering
- merchant profiles with essential info
- merchant-submitted promotions/offers
- simple loyalty tracking
- basic save/favorite function
- lightweight recommendation ranking using location, category, and stated preferences
- a curated local business feed for the launch area
- manual merchant onboarding and profile setup support during pilot

## Out of Scope
- broad national or multi-city expansion
- all-business onboarding, including chains and franchises
- complex social features
- full review and rating system
- event discovery feed
- in-app messaging between users and merchants
- advanced personalization or ML-driven ranking
- built-in payments
- table booking, ordering, or delivery
- merchant advertising marketplace
- cross-merchant universal loyalty currency
- anonymous public user-generated content moderation

## MVP Build Vs Pilot Operations
### Must Build Now
- location-based neighborhood discovery
- merchant profiles
- offer display
- basic filter/sort by category and proximity
- simple loyalty mechanism
- save/favorite function
- minimal merchant admin flow for offer updates and redemption tracking

### Manual Or Operational During Pilot
- merchant recruitment
- merchant profile creation support
- offer curation and quality control
- neighborhood selection
- tracking redemption issues
- customer support for early users
- basic analytics review and reporting

### Deferred Until After Proof
- reviews and ratings
- event discovery
- advanced personalization
- automated recommendation engine
- cross-merchant loyalty wallet
- payments and checkout
- merchant self-serve onboarding at scale
- multi-city expansion tools

## Business Model Hypothesis
Primary hypothesis:
- merchants pay a small monthly subscription or listing fee for inclusion, promotion slots, and loyalty tools once the app proves local foot traffic value

Secondary hypothesis:
- premium promotion placement or featured neighborhood visibility can generate additional revenue later

For the MVP, revenue is not the main proof point. The goal is to validate that:
- merchants will participate
- users will engage
- the loop can support a paid model later

## Critical Assumptions
- enough independent businesses in one city will join a pilot
- users care enough about local discovery to open the app repeatedly
- simple offers and loyalty are enough to change behavior
- recommendation quality can be achieved without heavy AI
- merchants will tolerate a basic operational process during early testing
- the app can avoid feeling like a cluttered deal directory

## How To Test Quickly
- recruit 20–30 independent businesses in 2–3 dense neighborhoods
- launch a limited pilot to 100–300 local users
- manually curate the initial feed and offers
- track:
  - app opens per user
  - offer taps
  - save/favorite rate
  - redemption rate
  - repeat visits
  - merchant retention after first month
- interview users after first few uses to learn whether the app is replacing generic search
- interview merchants to verify whether foot traffic or repeat visits justify continued participation

## Acceptance Criteria
- a user can find relevant nearby businesses in under 3 taps after opening the app
- each merchant profile displays essential info accurately and consistently
- at least a basic offer or loyalty action can be redeemed without operational confusion
- merchants can update offers or participation with minimal support
- the pilot can demonstrate repeated user engagement in at least one neighborhood
- enough merchants stay active to keep the feed fresh in the launch area
- the product can show evidence that discovery leads to visits or saves, not just clicks

## Risks And Failure Modes
- insufficient merchant supply makes the app look empty
- users do not trust the recommendations or offers
- the feed becomes generic and does not feel local enough
- manual merchant support does not scale even in the pilot
- loyalty is too weak to change repeat behavior
- the app overlaps too much with Google Maps/Yelp and fails to differentiate
- low-quality offers reduce credibility quickly
- without one dense neighborhood, network effects do not appear

## Product Readiness
Status: LIMITED

Blocking Gaps:
- Verified merchant supply in one launch neighborhood [supply_validation]
- Evidence that users prefer this workflow over existing discovery tools [user_differentiation]
- A simple redemption and loyalty flow that works reliably in pilot conditions [redemption_reliability]

Required Improvements:
- Define the first launch neighborhood and merchant density threshold [launch_focus]
- Run a concierge pilot to validate offer quality and repeat usage before scaling [pilot_validation]
- Tighten the merchant onboarding process so participation is simple enough for a small team to manage [merchant_onboarding]

## Recommendation
Proceed with a narrow concierge-style MVP pilot, not a broad product build.

Build only the neighborhood discovery, merchant profile, offer display, basic filters, and simple loyalty loop needed to test whether LocalLoop can create repeat local visits in one city. Keep event discovery, reviews, payments, and advanced personalization out of scope.

If the pilot cannot secure enough merchant supply and repeat user engagement in one dense neighborhood, pause and revise the wedge before investing in a fuller platform.

## Retained Decisions

- Tech: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]

## Deferred Decisions

_Aucune décision différée._

## Rejected Recommendations

- Tech: Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Tech: Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Growth: Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]
- Growth: Narrow the first audience to people who live or work within walking distance of the launch neighborhood. [audience_narrowing]

## Unresolved Tensions

- Tech recommendation needing arbitration: Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Tech recommendation needing arbitration: Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Tech recommendation needing arbitration: Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Tech recommendation needing arbitration: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]
- Growth recommendation needing arbitration: Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]
- Growth recommendation needing arbitration: Narrow the first audience to people who live or work within walking distance of the launch neighborhood. [audience_narrowing]
- Growth recommendation needing arbitration: Define the first activation loop around “open → see 3–7 relevant places → save/redeem → return for fresh local options.” [activation_loop]
- Growth recommendation needing arbitration: Specify the repeat-visit incentive as a simple loyalty reward tied to one merchant or one visit pattern, not a broad universal wallet. [loyalty_loop]
- Growth open question: Which exact neighborhood is dense enough to support the pilot?
- Growth open question: How many merchants are needed before the app feels credible?
- Growth open question: What is the single redemption method that is easiest to audit in person?

## Applied Changes

- Tech: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]

## Remaining Open Points

- Tech: Define the single launch city and 2–3 initial neighborhoods before implementation. [launch_focus]
- Tech: Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Growth: Define one exact launch neighborhood and the minimum merchant count needed for the feed to look credible. [launch_focus]
- Growth: Define the first activation loop around “open → see 3–7 relevant places → save/redeem → return for fresh local options.” [activation_loop]
- Growth: Specify the repeat-visit incentive as a simple loyalty reward tied to one merchant or one visit pattern, not a broad universal wallet. [loyalty_loop]
- Growth: Which exact neighborhood is dense enough to support the pilot?
- Growth: How many merchants are needed before the app feels credible?
- Growth: What is the single redemption method that is easiest to audit in person?
- Tech recommendation needing arbitration: Replace “merchant self-serve” in the MVP with internal admin-managed content creation and approval. [merchant_onboarding]
- Tech recommendation needing arbitration: Specify one redemption mechanism only: QR/code-based or staff-confirmed, not both. [redemption_reliability]
- Tech recommendation needing arbitration: Add required listing freshness rules for hours, offers, and merchant status. [data_freshness]
- Tech recommendation needing arbitration: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]
- Growth recommendation needing arbitration: Commit the first launch motion to a founder-led concierge pilot with no self-serve consumer acquisition at launch. [market_motion]
- Growth recommendation needing arbitration: Narrow the first audience to people who live or work within walking distance of the launch neighborhood. [audience_narrowing]
- Growth recommendation needing arbitration: Define the first activation loop around “open → see 3–7 relevant places → save/redeem → return for fresh local options.” [activation_loop]
- Growth recommendation needing arbitration: Specify the repeat-visit incentive as a simple loyalty reward tied to one merchant or one visit pattern, not a broad universal wallet. [loyalty_loop]
- Growth open question: Which exact neighborhood is dense enough to support the pilot?
- Growth open question: How many merchants are needed before the app feels credible?
- Growth open question: What is the single redemption method that is easiest to audit in person?

## Risks

- Inaccurate or stale business/offer data will quickly erode trust. [data_freshness]
- Redemption ambiguity could break loyalty and create support overhead. [redemption_reliability]
- Feed quality may be too weak if neighborhood supply is thin. [supply_validation]
- Merchant supply remains too thin and the app feels empty.
- Users do not see enough differentiation from Google Maps/Yelp.
- Offers are low quality or outdated, reducing trust quickly.
- the merchant base is too thin to make the app feel useful
- users do not see enough differentiation from Google Maps or Yelp
- offers become stale and trust drops quickly
- The merchant feed may look empty or stale if density is insufficient. [supply_validation]
- Consumers may not see enough advantage over Google Maps or Yelp. [user_differentiation]
- Offer quality may be too uneven, hurting trust quickly. [offer_quality]

## Open Questions

- Which exact city and neighborhoods are being targeted first?
- What merchant density is enough to create a credible feed?
- Which merchant category has the strongest repeat visit potential for the first wedge?
- Which single city and neighborhood will be the first proof location?
- What is the minimum number of active merchants required before launch?
- Which category cluster will be the wedge for the first feed?
- Which exact neighborhood is dense enough to support the pilot?
- How many merchants are needed before the app feels credible?
- What is the single redemption method that is easiest to audit in person?

## Final Revised PRD

# LocalLoop MVP Product Proposal

## Product Problem
People who want to support local independent businesses still default to large discovery platforms because local options are fragmented, hard to compare, and not personalized enough for immediate neighborhood intent.

Independent businesses need a lightweight way to be discovered locally and bring customers back, but most marketing tools are too broad, expensive, or complex for a small pilot city.

The MVP problem is narrow:
- help one user segment quickly discover relevant nearby independent businesses
- prove that merchants will participate if the workflow is simple and managed for them
- prove that a repeatable discovery-to-visit loop exists in one dense neighborhood

## Initial Wedge
A single-city, single-neighborhood mobile discovery app for people who live or work within walking distance of that neighborhood, focused only on independent coffee shops and lunch spots.

The wedge is intentionally narrow:
- one launch city
- one dense launch neighborhood
- one category cluster: coffee and lunch only
- one consumer use case: “What local place should I go to right now?”
- one merchant value proposition: “List one offer and get nearby customers”

## First Target User
Primary user:
- urban residents and young professionals who live or work in the launch neighborhood
- make same-day local decisions for coffee or lunch
- already use mobile discovery apps
- want local options but need convenience and relevance

First use case:
- finding a nearby independent coffee shop or lunch spot with an offer or loyalty incentive in the user’s current neighborhood

Secondary pilot user:
- independent business owners or managers in the same neighborhood who want foot traffic and repeat visits without running campaigns themselves

## Existing Alternatives And Switching Trigger
Existing alternatives:
- Google Maps / Search
- Yelp
- Instagram / TikTok
- delivery and deal apps
- word of mouth
- merchant-specific loyalty apps

Why users switch:
- current tools are broad, cluttered, and not neighborhood-specific enough
- offers are scattered across channels and hard to compare
- loyalty is fragmented across individual merchants
- independent businesses are hard to discover unless the user already knows them

Why merchants switch:
- they need a simple way to get discovered locally
- they want something lighter than full ad platforms or loyalty infrastructure
- they will participate if setup is minimal and they can see nearby customer traffic

## Core MVP Workflow
1. User opens the app and shares location or selects the launch neighborhood.
2. App shows a small curated feed of nearby independent coffee and lunch businesses.
3. User sees 3–7 relevant recommendations ranked by proximity, category match, freshness, and stated preferences.
4. User taps a merchant profile to view:
   - basic details
   - one active offer or promotion
   - distance
   - hours
   - simple loyalty reward, if available
5. User saves the place or redeems an offer in person.
6. The single redemption method is validated by the merchant using one auditable flow only.
7. User earns a basic loyalty reward after repeat visits to the same merchant.

The MVP must prove that:
- neighborhood discovery is useful
- offers increase intent
- one simple loyalty mechanic encourages return visits
- merchants can participate with low friction
- the app can maintain trustworthy local supply in one neighborhood

## In Scope
- location-based browsing within one city
- one launch neighborhood only
- coffee and lunch category cluster only
- merchant profiles with essential info
- merchant-submitted promotions/offers
- one redemption mechanism only
- simple loyalty tracking
- save/favorite function
- deterministic ranking using location, category, freshness, and stated preferences
- curated local business feed for the launch area
- internal admin-managed merchant onboarding, profile setup, offer approval, and status updates during pilot
- listing freshness rules for hours, offers, and merchant status
- internal ops console for merchant verification, offer approval, and dispute handling

## Out of Scope
- multi-city expansion
- chains and franchises
- other category clusters beyond coffee and lunch
- complex social features
- full review and rating system
- event discovery feed
- in-app messaging between users and merchants
- ML-driven personalization
- built-in payments
- table booking, ordering, or delivery
- merchant advertising marketplace
- cross-merchant universal loyalty currency
- anonymous public user-generated content moderation
- merchant self-serve onboarding at scale
- multiple redemption mechanisms
- broad consumer acquisition beyond the pilot neighborhood
- additional launch neighborhoods before proof

## MVP Build Vs Pilot Operations
### Must Build Now
- location-based neighborhood discovery
- merchant profiles
- offer display
- category and proximity filters
- save/favorite function
- simple loyalty mechanism
- one auditable redemption flow
- internal admin console for merchant verification, offer approval, status updates, and disputes
- deterministic ranking based on location, category, freshness, and stated preferences
- listing freshness checks for hours, offers, and merchant status

### Manual Or Operational During Pilot
- merchant recruitment
- merchant profile creation
- offer curation and quality control
- neighborhood selection
- redemption exception handling
- customer support for early users
- basic analytics review and reporting
- consumer invitation into the launch neighborhood
- merchant data correction and updates

### Deferred Until After Proof
- reviews and ratings
- event discovery
- advanced personalization
- automated recommendation engine
- self-serve merchant onboarding
- multi-city expansion tools
- cross-merchant loyalty wallet
- payments and checkout
- additional category clusters
- broader consumer acquisition automation

## Business Model Hypothesis
Primary hypothesis:
- merchants pay a small monthly subscription or listing fee for inclusion, promotion slots, and loyalty tools once the app proves local foot traffic value

Secondary hypothesis:
- featured placement within the launch neighborhood can create additional revenue later

For the MVP, revenue is not the main proof point. The goal is to validate that:
- merchants will participate
- users will engage
- the loop can support a paid model later

## Critical Assumptions
- enough independent businesses in one neighborhood will join a pilot
- users care enough about local discovery to open the app repeatedly
- simple offers and loyalty are enough to change behavior
- recommendation quality can be achieved without ML
- merchants will tolerate a manual operational process during early testing
- the app can avoid feeling like a cluttered deal directory
- one redemption method is sufficient to create trust and operational clarity
- the launch neighborhood can sustain enough supply density to feel alive

## How To Test Quickly
- define one launch city and one launch neighborhood before implementation
- recruit a minimum viable merchant set in that neighborhood
- launch a limited pilot to a small group of people who live or work there
- manually curate the initial feed and offers
- use one redemption method only and track it tightly
- monitor:
  - app opens per user
  - offer taps
  - save/favorite rate
  - redemption rate
  - repeat visits
  - merchant retention after first month
- interview users after their first few uses to learn whether the app is replacing generic search
- interview merchants to verify whether foot traffic or repeat visits justify continued participation

## Acceptance Criteria
- a user can find relevant nearby businesses in under 3 taps after opening the app
- each merchant profile displays essential info accurately and consistently
- the single redemption method works without operational ambiguity
- merchant offers and hours are updated enough to maintain trust in the launch neighborhood
- merchants can be onboarded and kept current through the internal admin process
- the pilot demonstrates repeat user engagement in the launch neighborhood
- enough merchants stay active to keep the feed credible and fresh
- the product shows evidence that discovery leads to saves or visits, not just clicks

## Risks And Failure Modes
- insufficient merchant supply makes the app look empty
- users do not trust the recommendations or offers
- the feed becomes generic and does not feel local enough
- manual merchant support does not scale even in the pilot
- loyalty is too weak to change repeat behavior
- the app overlaps too much with Google Maps / Yelp and fails to differentiate
- low-quality offers reduce credibility quickly
- without one dense neighborhood, the product never feels alive

## Product Readiness
Status: LIMITED

Blocking Gaps:
- verified merchant supply in one launch neighborhood [supply_validation]
- evidence that users prefer this workflow over existing discovery tools [user_differentiation]
- one redemption flow proven to be reliable and auditable in pilot conditions [redemption_reliability]

Required Improvements:
- define the single launch neighborhood and minimum merchant density threshold [launch_focus]
- run a concierge pilot to validate offer quality and repeat usage before scaling [pilot_validation]
- keep merchant onboarding admin-managed until the pilot proves repeatable operations [merchant_onboarding]
- enforce listing freshness rules for hours, offers, and merchant status before broader release [data_freshness]
- keep the category wedge limited to coffee and lunch until proof is achieved [scope]

## Recommendation
Proceed with a narrow concierge-style MVP pilot, not a broad product build.

Build only the neighborhood discovery, merchant profile, offer display, basic filters, one redemption flow, and simple loyalty loop needed to test whether LocalLoop can create repeat local visits in one city. Keep event discovery, reviews, payments, additional categories, and advanced personalization out of scope.

If the pilot cannot secure enough merchant supply and repeat user engagement in one dense neighborhood, pause and revise the wedge before investing in a fuller platform.

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Tech: Add an internal ops console requirement for offer approval, merchant verification, and dispute handling. [ops_tooling]

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
