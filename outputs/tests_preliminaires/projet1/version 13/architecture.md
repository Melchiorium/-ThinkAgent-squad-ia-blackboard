## Architecture Notes
Recommended MVP approach: build a **modular monolith backend** with a **mobile app frontend** and a **simple admin web console** for owner onboarding and internal ops. Keep all marketplace logic in one backend service initially to reduce operational complexity and make reservation/payment consistency easier to control.

### Main components / modules
- **Mobile app (driver + owner roles)**
  - Search/map, spot detail, reservation checkout, booking history, listing management for owners.
- **Backend API**
  - **Auth & user profile**: email/phone sign-in, role handling, basic profile data.
  - **Listings**: create/edit parking spots, photos, price, access notes, location coordinates.
  - **Availability & booking**: time-window availability, reservation creation, cancellation rules, anti-double-booking.
  - **Payments**: payment intent creation, webhook processing, booking payment state.
  - **Reviews**: post-booking owner ratings/reviews with simple moderation flags.
  - **Search**: geo query + filters over indexed listings.
  - **Notifications**: booking confirmation, reminders, cancellation notices.
- **Database**
  - PostgreSQL as the system of record.
- **Maps/location**
  - External maps/geocoding provider for place search, map rendering, route launch, and distance calculation.
- **Payments provider**
  - Stripe or equivalent with marketplace/payout support.
- **Object storage**
  - For listing photos and simple media assets.
- **Admin console**
  - Verify/approve owners and listings, inspect reservations, handle manual support actions.

### Main data flow
1. **Owner onboarding**
   - Owner signs up → creates listing with address/map pin, pricing, availability, and access notes → listing stored as draft/pending review.
2. **Search**
   - Driver opens app → grants location → backend queries listings by geo radius and time overlap → app shows results with distance, price, and current availability.
3. **Reservation**
   - Driver selects spot and time window → backend creates a short-lived hold/lock on that slot → payment intent is created → payment success webhook finalizes booking → reservation becomes confirmed.
4. **Availability enforcement**
   - All booking writes go through one reservation service in the backend, which checks overlapping windows in the database before confirming.
5. **Post-booking**
   - Booking completes → driver prompted to review owner → review stored and shown on listing details.

### Concrete technical choices with short rationale
- **React Native for the mobile app**
  - One codebase for driver and owner experiences; simplest mobile-first path for MVP.
- **Node.js/TypeScript backend**
  - Good fit for marketplace CRUD, webhook handling, and fast iteration with shared types.
- **PostgreSQL**
  - Strong transactional guarantees for reservation locking and overlap checks.
- **PostGIS**
  - Practical for location-based search and radius queries.
- **Stripe Connect**
  - Best simple path for secure payments plus owner payouts in a two-sided marketplace.
- **Redis only if needed for short reservation holds**
  - Use only for ephemeral booking locks; keep PostgreSQL as source of truth.
- **Expo for React Native**
  - Speeds mobile delivery and reduces native setup complexity unless a specific native dependency blocks it.
- **Basic role-based access control**
  - Separate driver and owner capabilities without building separate apps.

### Implementation constraints
- **Single-city launch assumption**
  - Search and pricing logic should be tuned for one constrained geography; do not build multi-region abstractions now.
- **Reservation consistency is critical**
  - Double-booking prevention must be transactional, not “eventually consistent.”
- **Availability model must stay simple**
  - Use explicit weekly availability windows plus exceptions; avoid live sensor-based or automated occupancy detection for MVP.
- **Payments and payouts must be webhook-driven**
  - Booking state must only finalize after verified payment events.
- **Listing verification should be operational, not automated**
  - Use admin review/manual approval for early supply trust rather than trying to build complex trust scoring.
- **Reviews should be post-completion only**
  - Prevent review abuse and keep the trust layer simple.
- **Location accuracy needs validation**
  - Require pin verification during owner onboarding; otherwise search quality will degrade quickly.

## Review Summary
The main technical challenge is not raw scale but **reliable marketplace correctness**: matching geo search, reservation locking, and payment finalization without double-booking or payment/booking mismatches. The recommended direction is a simple transactional backend with strong database constraints, externalized payments, and manual admin verification for early trust.

## Requested Changes
- Define the **minimum owner listing schema** required for MVP, including whether access instructions, photos, and exact pin confirmation are mandatory.
- Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Clarify whether the MVP supports **instant booking only** or also owner approval before confirmation; the architecture is simpler if it is instant booking only.
- Add an explicit **owner verification step** in the product flow for the first launch city, since unverified supply materially increases trust risk.
- Specify the **payout timing policy** for owners (immediate, delayed, or after reservation completion), because this affects payment provider configuration and support operations.

## Risks
- **Double-booking and race conditions** if reservation locking is not implemented transactionally and tested under concurrent booking attempts.
- **Supply quality risk** if location pins, access details, or availability windows are inaccurate, which would rapidly damage trust in a parking marketplace.
- **Payment/payout complexity** if the product requires instant payouts or complex cancellation/refund behavior before the marketplace flow is stabilized.

## Open Questions
- Will ParkEasy support **instant reserve** only, or do some listings require **owner acceptance** before confirmation?
- Are bookings **hourly, daily, or both** in the MVP? This changes pricing, availability modeling, and search UI.
- What is the intended **launch city/country**, since payment provider availability, tax handling, and map coverage depend on jurisdiction?