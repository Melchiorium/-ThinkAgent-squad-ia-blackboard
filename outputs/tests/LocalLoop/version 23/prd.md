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