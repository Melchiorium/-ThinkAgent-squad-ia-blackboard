# Blackboard

## Project Brief

Project Name: ParkEasy

Pitch:
A mobile application that allows drivers to find and reserve unused private parking spots from individuals, residential buildings, and companies.

Market Context:
- Parking is difficult in large cities
- Many private parking spots remain unused during the day
- Parking owners could monetize their unused spaces

Target Users:
- Urban drivers
- Daily commuters
- Private parking spot owners
- Small businesses with unused parking spaces

MVP Features:
- Search available parking spots
- Real-time availability
- Reservation system
- Secure payment integration
- GPS/location feature
- Ratings and reviews for parking owners

Technical Constraints:
- Mobile-first product
- Secure payment processing
- Real-time location services
- Availability management
- Scalable marketplace architecture

Growth Challenge:
This is a two-sided marketplace:
- acquire drivers
- acquire parking spot owners

Business Goal:
Reduce parking friction in cities while creating a new monetization opportunity for private parking owners.

## Project Brief Source

outputs/project-brief.md

## Expert Contributions

### Tech Summary

The main technical challenge is not raw scale but **reliable marketplace correctness**: matching geo search, reservation locking, and payment finalization without double-booking or payment/booking mismatches. The recommended direction is a simple transactional backend with strong database constraints, externalized payments, and manual admin verification for early trust.

## Tech Recommendations

- Define the **minimum owner listing schema** required for MVP, including whether access instructions, photos, and exact pin confirmation are mandatory.
- Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Clarify whether the MVP supports **instant booking only** or also owner approval before confirmation; the architecture is simpler if it is instant booking only.
- Add an explicit **owner verification step** in the product flow for the first launch city, since unverified supply materially increases trust risk.
- Specify the **payout timing policy** for owners (immediate, delayed, or after reservation completion), because this affects payment provider configuration and support operations.


## Tech Risks

- **Double-booking and race conditions** if reservation locking is not implemented transactionally and tested under concurrent booking attempts.
- **Supply quality risk** if location pins, access details, or availability windows are inaccurate, which would rapidly damage trust in a parking marketplace.
- **Payment/payout complexity** if the product requires instant payouts or complex cancellation/refund behavior before the marketplace flow is stabilized.


## Tech Open Questions

- Will ParkEasy support **instant reserve** only, or do some listings require **owner acceptance** before confirmation?
- Are bookings **hourly, daily, or both** in the MVP? This changes pricing, availability modeling, and search UI.
- What is the intended **launch city/country**, since payment provider availability, tax handling, and map coverage depend on jurisdiction?


### Growth Summary

The main growth challenge is not broad demand generation; it is **creating enough trusted supply in one dense area to make the app useful on day one**. The recommended GTM path is a **tight, supply-led city launch** focused on repeat commuters and a small set of verified parking owners, with the product optimized around fast reservation and confidence that the spot is real.

## Growth Recommendations

- Add a **launch geography definition**: one city plus 1–3 specific parking clusters/destinations to avoid thin marketplace coverage.
- Require **verified supply onboarding** for initial listings, including proof of ownership/authorization and exact access instructions.
- Add a **destination-first search flow** in MVP, not just “near me,” so drivers can search around the places they actually need to park.
- Define a **minimum reservation trust package**: exact spot location, entry instructions, booking confirmation, and support contact visible before payment.
- Add an **owner onboarding shortcut** for launch: manual-assisted listing creation for the first cohort, so supply can be seeded quickly and accurately.


## Growth Risks

- If the launch zone does not reach sufficient density, drivers will churn after seeing too few usable options.
- Trust may break quickly if spot accuracy or access instructions are incomplete, because the product is tied to a physical asset and immediate arrival.
- Owners may not stay engaged if bookings are too infrequent, making supply retention a bigger issue than initial sign-up.


## Growth Open Questions

- Which **single city and specific neighborhoods/destinations** are the intended launch focus?
- Will ParkEasy **manually verify initial owners/listings** before publishing them?
- Is the first wedge **daily commuters**, **event/visitor parking**, or **a specific recurring destination segment**?


## Initial PRD

# ParkEasy PRD

## 1. Product Overview

ParkEasy is a mobile-first marketplace that helps drivers find and reserve unused private parking spots from individuals, residential buildings, and small businesses in dense urban areas.

The product addresses two linked problems:
- Drivers waste time circling for parking in cities
- Parking owners have underutilized spaces that could generate income

ParkEasy’s core value is to make private parking discoverable, bookable, and trustworthy in one flow.

## 2. Problem Statement

Urban parking is inefficient:
- Drivers often cannot find convenient parking quickly
- Existing private spaces frequently sit empty during the day
- Parking owners have no easy way to monetize unused spots
- Booking private parking is often informal, fragmented, or untrustworthy

The market needs a simple way to match available spaces with nearby drivers, with clear pricing, location accuracy, and a reliable reservation process.

## 3. Goals

### Product goals
- Help drivers find and reserve nearby parking quickly
- Help parking owners monetize unused spaces with minimal friction
- Create a trusted marketplace with clear availability, payment, and confirmation
- Validate demand on both sides of the marketplace in a city launch

### Business goals
- Reduce parking friction in cities
- Build a repeatable supply-and-demand marketplace model
- Prove that private parking inventory can be reliably activated and used

## 4. Target Users

### Primary users: Urban drivers
People who need short-term or recurring parking in cities, including:
- Daily commuters
- City visitors
- Drivers with limited street parking access

### Secondary users: Parking spot owners
People or organizations with private parking inventory, including:
- Individuals with unused driveway or garage space
- Residential buildings with spare or time-based availability
- Small businesses with unused parking lots or bays

## 5. User Needs

### Drivers need to:
- Find nearby available parking quickly
- Trust that a space is real and reservable
- Know the price before arriving
- Navigate to the correct location
- Confirm their reservation without friction

### Owners need to:
- List parking spaces easily
- Control when a spot is available
- Receive payments reliably
- Minimize interruption and administrative overhead
- Build trust through ratings and reviews

## 6. Value Proposition

### For drivers
ParkEasy reduces the time, stress, and uncertainty of parking in cities by showing reservable private spaces nearby.

### For owners
ParkEasy turns idle parking capacity into income with a simple listing and booking flow.

## 7. Core User Workflow

### Driver workflow
1. Open app and allow location access
2. Search for parking near a destination or current location
3. View available spots with price, distance, and availability window
4. Select a spot and reserve it
5. Pay securely in-app
6. Navigate to the spot using GPS/location guidance
7. Use the reservation during the booked time
8. Leave a rating and review after the parking session

### Owner workflow
1. Create an account and set up a parking spot listing
2. Enter location, pricing, availability, and access details
3. Receive booking requests or instant reservations
4. Accept payment through the platform
5. Track reservations and availability
6. Receive ratings and reviews from drivers

## 8. MVP Scope

### In scope
- Mobile-first app for drivers and spot owners
- Parking spot search by location
- Map/list view of available spots
- Real-time availability status
- Reservation flow
- Secure payment integration
- GPS/location support for discovery and navigation
- Owner listing creation and availability management
- Driver ratings and reviews for owners
- Basic account creation and authentication

### Out of scope for MVP
- Advanced pricing optimization
- Dynamic surge pricing
- Long-term subscription plans
- Multi-city expansion logic
- Loyalty programs
- In-app messaging between drivers and owners
- Complex dispute resolution workflows
- Automated permit or regulatory verification
- Enterprise fleet tools
- Predictive parking recommendations

## 9. MVP Assumptions

- The product launches in one city or tightly constrained metro area first
- Supply acquisition will focus on a limited set of verified parking owners
- Availability updates are accurate enough for reservation use at MVP scale
- Payment processing can be handled through a standard secure provider
- Ratings and reviews will help build trust without requiring a more complex reputation system at launch

## 10. Functional Requirements

### Search and discovery
- Users can search by current location or destination
- Users can view available spots near them
- Search results show key details: price, distance, availability, and spot type

### Availability
- Spots must show current availability status
- Owners can set time-based availability windows
- The system must prevent double-booking for reserved time slots

### Reservation
- Users can reserve a spot for a defined time period
- Reservation confirmation must be immediate and clear
- Reservation details must be accessible in-app

### Payments
- Users can pay securely in-app
- Owners must receive payout tracking or booking earnings visibility
- Payment confirmation must be linked to the reservation

### Location and navigation
- App must use GPS/location services for discovery
- Users must be able to navigate to the reserved spot

### Trust and reputation
- Users can rate and review parking owners after completed reservations
- Spot listings should surface basic trust indicators where available

### Owner tools
- Owners can create and edit listings
- Owners can set pricing and availability
- Owners can view upcoming reservations

## 11. Non-Functional Requirements

- Mobile-first experience with fast load times
- Secure handling of payment data through a compliant payment processor
- Reliable location detection and map performance
- Availability updates must be consistent enough to avoid double-booking
- The product must be scalable enough to support marketplace growth beyond the pilot area

## 12. Constraints

- The product must work as a two-sided marketplace, so the experience depends on both supply and demand being present
- Real-time availability is important, but the MVP should rely on a simple and dependable availability model rather than complex automation
- Trust and location accuracy are critical because users are reserving physical spaces
- Secure payments are mandatory for launchability
- The MVP should remain simple enough to launch with a limited geographic footprint

## 13. Success Metrics

### Marketplace activity
- Number of active parking listings
- Number of active drivers searching the app
- Search-to-reservation conversion rate
- Reservation completion rate

### Supply-side health
- Percentage of listed spots that receive bookings
- Owner retention rate
- Time from listing creation to first booking

### Demand-side health
- Repeat driver booking rate
- Average time to complete a reservation
- Driver satisfaction score

### Trust and reliability
- Cancellation rate
- Double-booking incidents
- Share of completed bookings that receive a rating or review

## 14. Key Risks

- Insufficient parking supply in the launch area
- Low driver adoption if search results are sparse or unreliable
- Mismatch between listed availability and actual spot availability
- Trust concerns around unknown private parking owners
- Operational friction if payments or reservation confirmation are not seamless

## 15. Product Decisions for MVP

- Launch in one constrained urban market first
- Prioritize reliable reservation and payment flow over advanced marketplace features
- Include ratings and reviews as a basic trust layer
- Keep owner listing tools simple and self-serve
- Use a straightforward availability model that minimizes booking conflicts

## 16. Next Product Steps

1. Define the initial launch geography and parking categories
2. Specify the minimum listing fields required from owners
3. Define the reservation timing rules and cancellation policy
4. Validate the payment flow and payout process for owners
5. Design the core driver search, booking, and confirmation flow
6. Test supply onboarding with a small set of parking owners
7. Measure booking conversion and availability reliability in pilot use

## Retained Decisions

- Tech: Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Growth: Define a **minimum reservation trust package**: exact spot location, entry instructions, booking confirmation, and support contact visible before payment.

## Deferred Decisions

- Growth: Add a **launch geography definition**: one city plus 1–3 specific parking clusters/destinations to avoid thin marketplace coverage.

## Rejected Recommendations

- Tech: Add an explicit **owner verification step** in the product flow for the first launch city, since unverified supply materially increases trust risk.
- Growth: Require **verified supply onboarding** for initial listings, including proof of ownership/authorization and exact access instructions.
- Growth: Add a **destination-first search flow** in MVP, not just “near me,” so drivers can search around the places they actually need to park.
- Growth: Add an **owner onboarding shortcut** for launch: manual-assisted listing creation for the first cohort, so supply can be seeded quickly and accurately.

## Unresolved Tensions

- Tech recommendation needing arbitration: Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Tech recommendation needing arbitration: Clarify whether the MVP supports **instant booking only** or also owner approval before confirmation; the architecture is simpler if it is instant booking only.
- Tech recommendation needing arbitration: Add an explicit **owner verification step** in the product flow for the first launch city, since unverified supply materially increases trust risk.
- Tech recommendation needing arbitration: Specify the **payout timing policy** for owners (immediate, delayed, or after reservation completion), because this affects payment provider configuration and support operations.
- Growth recommendation needing arbitration: Require **verified supply onboarding** for initial listings, including proof of ownership/authorization and exact access instructions.
- Growth recommendation needing arbitration: Add a **destination-first search flow** in MVP, not just “near me,” so drivers can search around the places they actually need to park.
- Growth recommendation needing arbitration: Define a **minimum reservation trust package**: exact spot location, entry instructions, booking confirmation, and support contact visible before payment.
- Growth recommendation needing arbitration: Add an **owner onboarding shortcut** for launch: manual-assisted listing creation for the first cohort, so supply can be seeded quickly and accurately.
- Tech open question: Will ParkEasy support **instant reserve** only, or do some listings require **owner acceptance** before confirmation?
- Tech open question: Are bookings **hourly, daily, or both** in the MVP? This changes pricing, availability modeling, and search UI.
- Tech open question: What is the intended **launch city/country**, since payment provider availability, tax handling, and map coverage depend on jurisdiction?
- Growth open question: Which **single city and specific neighborhoods/destinations** are the intended launch focus?
- Growth open question: Will ParkEasy **manually verify initial owners/listings** before publishing them?
- Growth open question: Is the first wedge **daily commuters**, **event/visitor parking**, or **a specific recurring destination segment**?

## Applied Changes

- Tech: Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Growth: Define a **minimum reservation trust package**: exact spot location, entry instructions, booking confirmation, and support contact visible before payment.

## Remaining Open Points

- Tech: Define the **minimum owner listing schema** required for MVP, including whether access instructions, photos, and exact pin confirmation are mandatory.
- Tech: Clarify whether the MVP supports **instant booking only** or also owner approval before confirmation; the architecture is simpler if it is instant booking only.
- Tech: Specify the **payout timing policy** for owners (immediate, delayed, or after reservation completion), because this affects payment provider configuration and support operations.
- Tech: Will ParkEasy support **instant reserve** only, or do some listings require **owner acceptance** before confirmation?
- Tech: Are bookings **hourly, daily, or both** in the MVP? This changes pricing, availability modeling, and search UI.
- Tech: What is the intended **launch city/country**, since payment provider availability, tax handling, and map coverage depend on jurisdiction?
- Growth: Which **single city and specific neighborhoods/destinations** are the intended launch focus?
- Growth: Will ParkEasy **manually verify initial owners/listings** before publishing them?
- Growth: Is the first wedge **daily commuters**, **event/visitor parking**, or **a specific recurring destination segment**?
- Tech recommendation needing arbitration: Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Tech recommendation needing arbitration: Clarify whether the MVP supports **instant booking only** or also owner approval before confirmation; the architecture is simpler if it is instant booking only.
- Tech recommendation needing arbitration: Add an explicit **owner verification step** in the product flow for the first launch city, since unverified supply materially increases trust risk.
- Tech recommendation needing arbitration: Specify the **payout timing policy** for owners (immediate, delayed, or after reservation completion), because this affects payment provider configuration and support operations.
- Growth recommendation needing arbitration: Require **verified supply onboarding** for initial listings, including proof of ownership/authorization and exact access instructions.
- Growth recommendation needing arbitration: Add a **destination-first search flow** in MVP, not just “near me,” so drivers can search around the places they actually need to park.
- Growth recommendation needing arbitration: Define a **minimum reservation trust package**: exact spot location, entry instructions, booking confirmation, and support contact visible before payment.
- Growth recommendation needing arbitration: Add an **owner onboarding shortcut** for launch: manual-assisted listing creation for the first cohort, so supply can be seeded quickly and accurately.
- Tech open question: Will ParkEasy support **instant reserve** only, or do some listings require **owner acceptance** before confirmation?
- Tech open question: Are bookings **hourly, daily, or both** in the MVP? This changes pricing, availability modeling, and search UI.
- Tech open question: What is the intended **launch city/country**, since payment provider availability, tax handling, and map coverage depend on jurisdiction?
- Growth open question: Which **single city and specific neighborhoods/destinations** are the intended launch focus?
- Growth open question: Will ParkEasy **manually verify initial owners/listings** before publishing them?
- Growth open question: Is the first wedge **daily commuters**, **event/visitor parking**, or **a specific recurring destination segment**?

## Risks

- **Double-booking and race conditions** if reservation locking is not implemented transactionally and tested under concurrent booking attempts.
- **Supply quality risk** if location pins, access details, or availability windows are inaccurate, which would rapidly damage trust in a parking marketplace.
- **Payment/payout complexity** if the product requires instant payouts or complex cancellation/refund behavior before the marketplace flow is stabilized.
- If the launch zone does not reach sufficient density, drivers will churn after seeing too few usable options.
- Trust may break quickly if spot accuracy or access instructions are incomplete, because the product is tied to a physical asset and immediate arrival.
- Owners may not stay engaged if bookings are too infrequent, making supply retention a bigger issue than initial sign-up.

## Open Questions

- Will ParkEasy support **instant reserve** only, or do some listings require **owner acceptance** before confirmation?
- Are bookings **hourly, daily, or both** in the MVP? This changes pricing, availability modeling, and search UI.
- What is the intended **launch city/country**, since payment provider availability, tax handling, and map coverage depend on jurisdiction?
- Which **single city and specific neighborhoods/destinations** are the intended launch focus?
- Will ParkEasy **manually verify initial owners/listings** before publishing them?
- Is the first wedge **daily commuters**, **event/visitor parking**, or **a specific recurring destination segment**?

## Final Revised PRD

# ParkEasy PRD

## 1. Product Overview

ParkEasy is a mobile-first marketplace that helps drivers find and reserve unused private parking spots from individuals, residential buildings, and small businesses in dense urban areas.

The product addresses two linked problems:
- Drivers waste time searching for parking in cities
- Parking owners have underutilized spaces that could generate income

ParkEasy’s core value is to make private parking discoverable, reservable, and trustworthy in one flow.

## 2. Problem Statement

Urban parking is inefficient:
- Drivers often cannot find convenient parking quickly
- Existing private spaces frequently sit empty during the day
- Parking owners have limited ways to monetize unused spots
- Booking private parking is often informal, fragmented, or untrustworthy

The market needs a simple way to match available spaces with nearby drivers, with clear pricing, accurate location details, and a reliable reservation process.

## 3. Product Goals

### User goals
- Help drivers find and reserve nearby parking quickly
- Help parking owners monetize unused spaces with minimal friction
- Create a trusted marketplace with clear availability, payment, and confirmation
- Validate demand on both sides of the marketplace in a single launch city

### Business goals
- Reduce parking friction in cities
- Prove that private parking inventory can be reliably activated and used
- Establish a repeatable marketplace model for future city expansion

## 4. Target Users

### Primary users: Urban drivers
People who need short-term parking in cities, including:
- Daily commuters
- City visitors
- Drivers with limited street parking access

### Secondary users: Parking spot owners
People or organizations with private parking inventory, including:
- Individuals with unused driveway or garage space
- Residential buildings with spare or time-based availability
- Small businesses with unused parking lots or bays

## 5. User Needs

### Drivers need to:
- Find nearby available parking quickly
- Trust that a space is real and reservable
- Know the price before arriving
- Navigate to the correct location
- Confirm the reservation without friction

### Owners need to:
- List parking spaces easily
- Control when a spot is available
- Receive payments reliably
- Minimize administrative overhead
- Build trust with drivers through verification and reviews

## 6. Value Proposition

### For drivers
ParkEasy reduces the time, stress, and uncertainty of parking in cities by showing reservable private spaces nearby.

### For owners
ParkEasy turns idle parking capacity into income with a simple listing and booking flow.

## 7. Core User Workflow

### Driver workflow
1. Open the app and allow location access
2. Search for parking by destination or current location
3. View available spots with price, distance, availability window, and access details
4. Select a spot and reserve it instantly
5. Pay securely in-app
6. Navigate to the reserved spot using GPS/location guidance
7. Use the reservation during the booked time
8. Leave a rating and review after the parking session

### Owner workflow
1. Create an account
2. Submit a parking spot listing with required details
3. Complete verification for the initial launch city
4. Set location, pricing, availability, and access instructions
5. Publish the listing
6. Receive booking notifications and payout status updates
7. Track upcoming reservations
8. Receive ratings and reviews from drivers

## 8. MVP Scope

### In scope
- Mobile-first app for drivers and spot owners
- Destination-first and current-location search
- Map and list views of available spots
- Real-time availability status
- Instant booking only; no owner approval flow in MVP
- Secure payment integration
- GPS/location support for discovery and navigation
- Owner listing creation and availability management
- Basic owner verification for initial launch supply
- Ratings and reviews for parking owners
- Basic account creation and authentication

### Out of scope for MVP
- Owner approval before booking confirmation
- Advanced pricing optimization
- Dynamic surge pricing
- Long-term subscription plans
- Multi-city expansion logic
- Loyalty programs
- In-app messaging between drivers and owners
- Complex dispute resolution workflows
- Automated permit or regulatory verification
- Enterprise fleet tools
- Predictive parking recommendations

## 9. MVP Assumptions

- The product launches in one city, with coverage concentrated in 1–3 dense parking clusters or destinations
- Supply acquisition will focus on a limited set of verified parking owners
- The MVP will use instant booking only to reduce operational complexity and booking ambiguity
- Availability updates are accurate enough for reservation use at MVP scale
- Payment processing can be handled through a standard secure provider
- Ratings and reviews will help build trust without requiring a more complex reputation system at launch

## 10. Functional Requirements

### Search and discovery
- Users can search by destination or current location
- Users can view available spots near a chosen area
- Search results show key details: price, distance, availability, and spot type
- Search should surface exact location and access instructions before booking

### Availability
- Spots must show current availability status
- Owners can set time-based availability windows
- The system must prevent double-booking for reserved time slots

### Reservation
- Users can reserve a spot for a defined time period
- Reservation confirmation must be immediate and clear
- Reservation details must be accessible in-app
- If payment succeeds but the reservation lock fails, the booking must not be left in an ambiguous state; the transaction should fail safely and trigger refund handling

### Booking rules
- The MVP uses a simple reservation rule set with fixed booking durations supported by the listing
- A booking must include a minimum reservation duration and a small buffer between back-to-back reservations
- Cancellations must follow a basic cutoff window defined at launch
- The product should avoid complex, configurable booking logic in MVP

### Payments
- Users can pay securely in-app
- Owners must receive payout status visibility
- Payouts should be delayed until after the reservation completes, to reduce marketplace risk in the initial launch
- Payment confirmation must be linked to the reservation

### Location and navigation
- App must use GPS/location services for discovery
- Users must be able to navigate to the reserved spot
- The reservation view should show exact spot location and access instructions

### Trust and reputation
- Users can rate and review parking owners after completed reservations
- Initial listings in the launch city must be manually verified before publication
- Each listing must show the minimum trust package: exact location, access instructions, booking confirmation, and support contact

### Owner tools
- Owners can create and edit listings
- Owners can set pricing and availability
- Owners can view upcoming reservations
- Owners can see verification status and payout status

## 11. Minimum Listing Data

Each owner listing must include:
- Spot title or label
- Exact location pin
- Address or directional location description
- Spot type
- Pricing
- Availability windows
- Access instructions
- Photos
- Verification status
- Support contact or help path

## 12. Non-Functional Requirements

- Mobile-first experience with fast load times
- Secure handling of payment data through a compliant payment processor
- Reliable location detection and map performance
- Availability updates must be consistent enough to avoid double-booking
- The product must be stable enough for a constrained launch city
- The system must support manual review and approval of initial supply

## 13. Constraints

- The product must work as a two-sided marketplace, so launch success depends on both supply and demand being present in the same area
- The MVP should stay within one city and a few concentrated parking zones to avoid thin marketplace coverage
- Trust and location accuracy are critical because users are reserving physical spaces
- Secure payments are mandatory for launchability
- The MVP should use instant booking only to keep the reservation flow simple and dependable
- Initial supply must be verified before publication to protect trust in the marketplace
- Payouts should be delayed until after reservation completion to reduce risk and simplify early operations

## 14. Success Metrics

### Marketplace activity
- Number of active verified parking listings
- Number of active drivers searching the app
- Search-to-reservation conversion rate
- Reservation completion rate

### Supply-side health
- Percentage of listed spots that receive bookings
- Owner retention rate
- Time from listing creation to first booking

### Demand-side health
- Repeat driver booking rate
- Average time to complete a reservation
- Driver satisfaction score

### Trust and reliability
- Cancellation rate
- Double-booking incidents
- Share of completed bookings that receive a rating or review
- Percentage of bookings with successful payment and confirmed reservation on first attempt

## 15. Key Risks

- Insufficient verified parking supply in the launch area
- Low driver adoption if search results are sparse or unreliable
- Mismatch between listed availability and actual spot availability
- Trust concerns around unknown private parking owners
- Operational friction if payments, verification, or reservation confirmation are not seamless

## 16. Product Decisions for MVP

- Launch in one constrained urban market first
- Concentrate supply in 1–3 dense destinations or parking clusters
- Require verification for initial owner listings
- Use destination-first search as the primary discovery path
- Support instant booking only in MVP
- Keep booking rules simple with fixed reservation logic, a minimum duration, and a basic cancellation window
- Delay owner payouts until after reservation completion
- Include ratings and reviews as a basic trust layer
- Keep owner listing tools simple and self-serve, with manual-assisted onboarding for the first cohort

## 17. Next Product Steps

1. Define the initial launch city and the first 1–3 parking clusters or destinations
2. Finalize the minimum listing fields and verification checklist for owners
3. Define reservation timing rules, cancellation policy, and buffer time
4. Confirm payment provider setup and delayed payout handling
5. Design the destination-first search, booking, and confirmation flow
6. Build a manual-assisted onboarding process for the first supply cohort
7. Pilot with a small set of verified owners and measure booking conversion, reservation reliability, and trust signals

## Revision Summary

Updated the PRD after tech and growth review to align scope, technical constraints, and go-to-market guidance.

## Decisions

- Tech: Specify the **reservation rule set**: minimum booking duration, buffer time between bookings, cancellation window, and what happens if payment succeeds but the reservation lock fails.
- Growth: Define a **minimum reservation trust package**: exact spot location, entry instructions, booking confirmation, and support contact visible before payment.

## Conflicts

_Aucun conflit._

## Activity Log

- product_agent: prd_draft_generated
- tech_agent: architecture_notes_generated
- growth_agent: gtm_notes_generated
- product_agent: prd_draft_revised
