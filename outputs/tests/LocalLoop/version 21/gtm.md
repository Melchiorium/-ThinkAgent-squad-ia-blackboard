## Go-To-Market Notes
- **Main market bottleneck:** LocalLoop is not a demand problem first; it is a **supply-density and freshness problem**. The app only feels useful if one neighborhood has enough currently accurate, relevant, independent businesses to beat default behavior in Maps/social.
- **Side of the market to secure first:** **Merchants first, but only a small seed cohort**. Users will not activate unless the neighborhood already feels complete. The first proof comes from a tightly controlled merchant set, not broad consumer acquisition.
- **2 to 3 structural GTM decisions that shape the launch:**
  - **Choose one neighborhood and one merchant cohort:** one dense neighborhood, one category cluster, and a minimum number of participating businesses before any public push.
  - **Run a founder-led concierge pilot:** manual onboarding, manual freshness checks, and operator approval are acceptable until the market proves repeat use.
  - **Use merchant seeding as the entry point, not paid consumer acquisition:** the first motion is local merchant outreach plus neighborhood invite distribution to nearby residents/workers.
- **Initial target audience:** Urban residents and young professionals who **live or work inside the launch neighborhood** and already search nearby options on Maps or social apps. Secondary user segment can be nearby office workers if the neighborhood has strong daytime traffic.
- **Positioning:** “A curated neighborhood guide to independent local spots with verified current offers.” Not a general local search app; not a citywide directory.
- **First acquisition motion:** **Founder-led merchant seeding followed by local invite distribution** to a narrow resident/worker list in the same neighborhood.
- **Operating assumptions for the first acquisition motion:**
  - The team can recruit a minimum merchant cohort in one neighborhood without self-serve tooling.
  - Merchants will accept a simple offer/reward and a manual approval process.
  - A small local audience will try the app if the neighborhood feels complete and current.
  - The launch motion can be measured by listing density, first-session engagement, and merchant continuation interest.
- **Switching trigger:** Users switch when the app surfaces a **better immediate neighborhood option** with a verified current offer and fresher relevance than Maps/Yelp/social, especially for repeat nearby decisions like coffee, lunch, or quick errands.
- **First activation loop:** User opens app → sees nearby curated businesses with one current offer/reward → taps save/directions/redeem → merchant verifies visit/reward → app marks the business as useful and keeps freshness current → user returns for the next nearby need.
- **What must exist before public launch:**
  - One launch neighborhood clearly defined
  - Minimum merchant cohort live and current
  - One category cluster with enough density to feel useful
  - One redemption/visit verification method working reliably
  - Freshness checks in place so stale listings do not remain visible
  - Operator approval for every live merchant and offer
  - A small local user list ready for the pilot
- **What must be productized now vs. manual during pilot:**
  - **Must be productized now:** neighborhood-based discovery, merchant listing pages, freshness status, stale-listing hiding, one redemption method, save/directions flow, basic feedback, operator approval gate, minimum required listing fields.
  - **Can stay manual during pilot:** merchant sourcing, merchant onboarding, offer setup, freshness verification, neighborhood curation, user recruitment, merchant support, renewal follow-ups, fallback handling for failed redemptions.

## Review Summary
The main launch challenge is not building a broad local discovery app; it is proving that one neighborhood can be made dense, current, and trusted enough to create repeat use. The recommended direction is a founder-led concierge pilot with merchant-first seeding in one neighborhood, one category cluster, and a small local resident/worker audience.

## Build Vs Pilot Operations

### Must Be Productized Now
- One neighborhood-based discovery feed
- Merchant profile pages with required fields
- Freshness status and stale-listing hiding
- One visit/redemption verification method
- Save/favorite and map handoff
- Basic useful/not useful feedback
- Operator approval gate before publishing
- Minimum required fields before go-live
- Basic admin controls for suspension and override

### Can Stay Manual Or Operational During Pilot
- Merchant sourcing and onboarding
- Offer creation and renewal follow-up
- Freshness checks
- Category curation
- Local user recruitment
- Merchant support
- Redemption issue resolution
- Manual approval of each live listing

### Deferred Until After Proof
- Reviews and ratings
- Event feed
- Advanced personalization
- Merchant self-serve onboarding
- Merchant analytics dashboard
- Paid placements
- Multi-city rollout
- In-app payments or ordering
- Social feed mechanics

## Critical Assumptions
- A minimum merchant cohort can be recruited in one neighborhood before launch.
- The neighborhood can feel complete enough to beat default Maps/social behavior for a narrow use case.
- Users will try a curated local app if freshness and relevance are obvious.
- Merchants will tolerate manual setup and a simple pilot process.
- One verification method will be simple enough for both merchants and users to use consistently.

## Requested Changes
- Define the **launch neighborhood merchant cohort target** explicitly, including the minimum number of active listings required before launch. [supply_density]
- Narrow the first audience to **people who live or work in the launch neighborhood**, rather than broad urban residents. [market_motion]
- Specify the **first acquisition motion** as founder-led merchant seeding plus local invite distribution, with no broad consumer marketing. [onboarding]
- Set a **merchant participation bar** for launch readiness, including offer freshness and willingness to renew after the pilot. [merchant_value]
- Clarify the **single category cluster** to avoid a mixed-use feed that is too weak to create repeat behavior. [scope]

## Risks
- The merchant cohort is too small or too stale to make the app feel useful. [supply_density]
- The neighborhood audience is too broad, making acquisition unfocused and low-converting. [market_motion]
- Users do not perceive enough improvement over Maps, Yelp, or social platforms. [demand_validation]
- Merchants do not renew after the pilot because value is unclear. [merchant_value]
- Manual maintenance becomes too heavy for the team to sustain. [onboarding]

## Open Questions
- What is the exact minimum merchant count needed for one neighborhood to feel complete?
- Which single category cluster is strongest for repeat use in the chosen neighborhood?
- What is the primary local user segment: residents, workers, or both?
- What merchant renewal signal will count as credible proof after the pilot?
- What is the simplest verification method merchants will reliably use?

## Why This Could Fail Even With Good Execution
Even with strong execution, the launch can fail if the chosen neighborhood never reaches the density and freshness threshold needed to feel better than default local search. In that case, the product becomes a manually maintained directory that users try once but do not return to, and merchants do not see enough incremental value to renew.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- The launch audience is still too broad to support a focused pilot motion. [market_motion]
- The first market side to secure is not operationalized with a minimum merchant cohort target. [supply_density]
- The first acquisition motion is not tightly specified enough to test reliably. [onboarding]
- Merchant renewal intent is not yet tied to a concrete pilot bar. [merchant_value]

Required Improvements:
- Define the narrowest launch audience as people who live or work in the single launch neighborhood. [market_motion]
- Set a minimum merchant cohort and participation threshold before public launch. [supply_density]
- Lock the first acquisition motion to founder-led merchant seeding plus local invite distribution. [onboarding]
- Add a specific merchant renewal checkpoint as the primary proof of market value. [merchant_value]