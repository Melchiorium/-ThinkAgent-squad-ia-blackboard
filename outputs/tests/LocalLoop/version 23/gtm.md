## Go-To-Market Notes
- **Main market bottleneck:** the launch will fail if the neighborhood does not have enough participating merchants clustered tightly enough to make the feed feel useful on day one. The consumer app is not the primary bottleneck; **supply density and offer freshness in one bounded area** are.
- **Side of the market to secure first:** **merchants first, but only in one corridor/neighborhood**. Without a credible merchant set, users will churn after one open and the product will look empty. Consumer demand should be tested only after the supply base is live.
- **Structural GTM decisions:**
  1. **Single-neighborhood launch only** with a hard geographic boundary and no category sprawl.
  2. **One merchant category wedge**: independent coffee shops + casual restaurants only, because frequency and repeat visits are high enough to prove the loop.
  3. **Founder-led, curated pilot** rather than a self-serve launch; the product is not ready for broad merchant acquisition.
- **Initial target audience:** urban young professionals who already buy coffee or lunch in the chosen neighborhood 3+ times per week and are open to trying nearby independents if the path is immediate and rewards are visible.
- **Positioning:** “The curated local discovery app for one neighborhood’s best independent coffee and lunch spots, with verified offers and a simple repeat-visit reward.”
- **Primary acquisition motion:** **founder-led merchant acquisition** via in-person outreach and direct onboarding of a minimum merchant set, followed by consumer acquisition through neighborhood-specific flyers/QRs, merchant counter signage, and direct local invites.
- **Operating assumptions for the first acquisition motion:**
  - merchants will respond to a low-friction, pilot-only pitch
  - a verified offer plus a simple repeat-visit loop is enough to get first participation
  - consumers will try the app if participating merchants are dense and visibly promoted in a small area
  - the team can maintain freshness manually during pilot
- **Switching trigger:** users switch when LocalLoop is clearly better than Google Maps/Yelp for this **one narrow use case**: “what should I try nearby right now that is independently owned, open, and has a verified offer/reward?” Merchants switch when the app produces measurable foot traffic or repeat visits without requiring them to run campaigns.
- **First activation loop:** user opens app → sees a curated nearby merchant → redeems a verified offer in-store → earns one loyalty stamp immediately → returns to see progress toward the next reward → repeats within the same neighborhood.
- **What must exist before public launch:**
  - one named neighborhood or corridor with a hard boundary
  - a minimum active merchant set dense enough to avoid an empty feed
  - one validated redemption method that staff can complete reliably
  - one loyalty reward path per merchant or per pilot cohort
  - merchant profiles with accurate hours, address, and verified offer
  - a live correction path for stale offers/hours
- **What must be productized now:**
  - curated discovery feed
  - merchant profile page
  - one redemption confirmation flow
  - loyalty stamp/progress tracking
  - verified merchant status
  - immutable redemption/loyalty event log
  - internal ops tools for suspending stale offers and correcting listing details
- **What can stay manual during the pilot:**
  - recruiting the first merchants
  - approving offers before publishing
  - verifying merchant identity and participation
  - curating the initial inventory
  - resolving redemption disputes
  - maintaining minimum active supply
  - consumer onboarding help and local promotion
- **What should stay deferred until after proof:**
  - reviews
  - events feed
  - advanced personalization
  - cross-category expansion
  - public self-serve merchant signup
  - complex loyalty tiers
  - payments, booking, multi-city tooling

## Review Summary
The core launch challenge is not building the app; it is proving that one neighborhood has enough dense, trustworthy merchant supply and that one redemption/loyalty loop is compelling enough to create repeat use. The best GTM path is a tightly controlled, founder-led pilot in a single corridor with coffee shops and casual restaurants only, using manual merchant acquisition and a simple verified redemption flow to prove demand before scaling.

## Build Vs Pilot Operations

### Must Be Productized Now
- curated nearby discovery feed
- merchant profile page
- one redemption confirmation flow
- loyalty stamp/progress tracking
- verified merchant flag
- immutable loyalty/redemption event log
- internal ops console for stale offers, hours, and disputes
- basic distance and category filtering

### Can Stay Manual Or Operational During Pilot
- recruit the first merchants
- approve offers before publishing
- verify merchant identity and participation
- curate the initial neighborhood inventory
- resolve redemption disputes
- remove stale or poor-quality listings
- support merchant setup and corrections
- maintain the minimum active merchant set in the launch neighborhood
- local consumer outreach and onboarding help

### Deferred Until After Proof
- reviews
- events feed
- advanced personalization or ML ranking
- cross-category expansion
- merchant self-serve onboarding
- richer loyalty programs
- payments
- booking
- multi-city tooling
- self-serve promotion products

## Critical Assumptions
- one named neighborhood can support a dense enough merchant set to make the feed useful
- merchants will accept a simple pilot offer and participate in a lightweight redemption process
- users will open a dedicated local discovery app often enough to validate repeat use
- loyalty plus verified offers can create enough return behavior to matter
- the app can remain trustworthy with manual curation and fast correction of stale data

## Requested Changes
- Lock one specific launch neighborhood/corridor and define the minimum merchant count required to avoid an empty feed. [onboarding]
- Add a launch-proof metric tied to behavior: redemptions per active merchant and repeat redemption rate within a fixed time window. [demand_validation]
- Validate one staff-friendly redemption method with real merchants before public launch. [redemption_flow]
- Explicitly require the first merchant set to be dense enough that a user can complete the core loop without leaving the launch area. [supply_density]
- Make the launch hypothesis explicit: the MVP is proving repeat visits in one neighborhood, not broad discovery across categories. [value_proof]

## Risks
- merchant density is too thin to produce a useful feed
- users treat the app like a one-time coupon app and do not return
- the redemption flow is too awkward for staff to use consistently
- LocalLoop is not meaningfully better than Google Maps/Yelp for the narrow wedge
- manual curation becomes too heavy if the merchant set is unstable

## Open Questions
- What is the exact minimum active merchant count needed in the launch corridor before consumer launch?
- Which single redemption flow has been validated with merchants and staff as lowest friction?
- What behavioral threshold counts as credible early demand: redemptions per merchant, repeat redemption rate, or both?
- Which specific neighborhood/corridor will be used for the pilot?
- Will the first reward be merchant-specific or standardized across the pilot?

## Why This Could Fail Even With Good Execution
Even with strong execution, the project can fail if the neighborhood supply is not dense and fresh enough to beat the convenience of Google Maps/Yelp, or if the verified offer plus loyalty loop does not create enough repeat behavior to justify a dedicated app. In that case, the product will look like a thin coupon directory rather than a must-use local discovery habit.

## GTM Readiness
Status: LIMITED

Blocking Gaps:
- Launch corridor and minimum merchant density are not locked [onboarding]
- Redemptions-per-merchant and repeat-redemption thresholds are not defined [demand_validation]
- One real-world redemption flow has not been validated with staff [redemption_flow]
- The launch proof metric is still vague rather than behavioral [value_proof]

Required Improvements:
- Lock one neighborhood/corridor and the minimum active merchant count before public launch [onboarding]
- Define a launch-proof metric using redemptions per active merchant and repeat redemption rate within a fixed window [demand_validation]
- Validate one friction-light redemption method with actual merchants under checkout conditions [redemption_flow]
- Use the pilot to prove that curated discovery plus loyalty creates repeat use better than map search [value_proof]