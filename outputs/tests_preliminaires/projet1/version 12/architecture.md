## Architecture Notes

### Recommended Technical Approach
A **Modular Monolith Backend with Native Mobile Clients**. This approach leverages a single, cohesive backend application that encapsulates distinct functional modules, providing a unified API for both driver and owner mobile applications. This balances the need for separation of concerns with the simplicity required for an MVP, avoiding the overhead of distributed systems.

### Main Components or Modules

1.  **Mobile Clients:**
    *   **Driver App:** Native iOS and Android application for searching, viewing, reserving, paying, navigating, and reviewing.
    *   **Owner App:** Native iOS and Android application for listing spots, managing availability, viewing bookings, and managing payouts.
2.  **API Gateway/Backend Service:** A central application handling all incoming API requests, user authentication, authorization, and routing to internal domain-specific modules.
3.  **User Management Module:** Manages user registration, profiles (driver/owner roles), authentication credentials, and basic account settings.
4.  **Parking Spot Management Module:** Handles CRUD operations for parking spots, including location, photos, description, access instructions, and base pricing.
5.  **Availability & Booking Module:** Manages the availability schedule for each spot, processes reservation requests, enforces real-time availability, and prevents double-bookings.
6.  **Payment & Payout Module:** Integrates with a third-party payment gateway to process driver payments, manage funds in escrow, and initiate payouts to parking owners.
7.  **Location & Search Module:** Provides geospatial querying capabilities, allowing drivers to search for spots within a given radius or near a destination, and handles geocoding.
8.  **Rating & Review Module:** Stores and retrieves ratings and textual reviews submitted by drivers for spots/owners.
9.  **Notification Module:** Manages and sends push notifications to both drivers (e.g., booking confirmation, reminders) and owners (e.g., new booking, payout confirmation).

### Main Data Flow

*   **Driver Search & Reserve:**
    1.  Driver App sends current location/destination to API Gateway.
    2.  API Gateway queries Location & Search Module for nearby spots, filtered by Availability & Booking Module.
    3.  Driver App displays spots on map.
    4.  Driver selects spot, sends reservation request (duration, payment details) to API Gateway.
    5.  API Gateway orchestrates: Availability & Booking Module (reserves spot) -> Payment & Payout Module (processes payment via gateway) -> Notification Module (sends confirmation to driver and owner).
*   **Parking Owner List & Manage:**
    1.  Owner App sends spot details (location, photos, access) to API Gateway.
    2.  API Gateway invokes Parking Spot Management Module (creates/updates spot) and Availability & Booking Module (sets initial availability schedule).
    3.  Owner App receives booking notifications from Notification Module and views payout status from Payment & Payout Module.

### Concrete Technical Choices with Short Rationale

*   **Mobile Development Framework:** **React Native**.
    *   *Rationale:* Enables a single codebase for both iOS and Android driver/owner apps, significantly accelerating MVP development while providing a native-like user experience.
*   **Backend Framework:** **Python with Django REST Framework**.
    *   *Rationale:* Provides a robust and rapidly developable foundation for the modular monolith, with excellent ORM capabilities, built-in admin, and a mature ecosystem for API development.
*   **Database:** **PostgreSQL with PostGIS extension**.
    *   *Rationale:* A highly reliable and scalable relational database. PostGIS natively supports advanced geospatial queries, essential for location-based search and filtering, simplifying the overall data architecture.
*   **Payment Gateway:** **Stripe Connect**.
    *   *Rationale:* Specifically designed for marketplace platforms to handle multi-party payments and payouts (driver pays platform, platform pays owner), simplifying PCI compliance and complex escrow logic.
*   **Cloud Provider:** **AWS (Amazon Web Services)**.
    *   *Rationale:* Offers a comprehensive suite of scalable, managed services (e.g., EC2, RDS, S3, SQS, SNS) reducing operational burden and providing a strong foundation for future growth.
*   **Mapping/Location Services:** **Google Maps Platform (API & SDKs)**.
    *   *Rationale:* Industry-leading and widely recognized for accuracy, rich features (mapping, geocoding, navigation), and ease of integration into mobile applications.
*   **Push Notifications:** **Firebase Cloud Messaging (FCM)**.
    *   *Rationale:* A unified, cross-platform messaging solution for delivering notifications reliably to both Android and iOS devices, simplifying backend integration.

### Implementation Constraints

*   **Real-time Availability Accuracy:** The system must handle concurrent booking requests and updates efficiently to prevent double-bookings, requiring careful database transaction management and potentially optimistic locking.
*   **Third-Party API Dependency:** Heavy reliance on Stripe Connect and Google Maps Platform means careful integration, error handling, API key management, and awareness of their respective rate limits and service stability are critical.
*   **Data Migration (Future):** While a modular monolith is recommended for MVP, anticipating potential future migration to a more distributed architecture (if justified by extreme scale) implies maintaining clear module boundaries from the start.
*   **Mobile Development Tooling:** Ensuring a smooth CI/CD pipeline for React Native apps across both iOS and Android platforms, including signing and deployment to app stores, will require dedicated setup.

## Review Summary
The core technical challenge for ParkEasy's MVP is establishing a robust and reliable two-sided marketplace, particularly in managing real-time parking spot availability and secure multi-party payment processing within a mobile-first context. The recommended direction is to build a modular monolith backend using Python/Django, serving native mobile applications developed with React Native, and leveraging specialized third-party services like Stripe Connect and Google Maps Platform to streamline complex features.

## Requested Changes
- **Clarify Parking Spot Access Mechanisms:** Define precisely how a driver gains access to a reserved spot (e.g., smart lock integration, manual code entry, meeting owner, key box) as this significantly impacts app features and potential hardware integrations.
- **Specify "Real-time Availability" SLAs:** Quantify the acceptable latency for availability updates (e.g., within 5 seconds, 30 seconds) to guide technical implementation choices (e.g., WebSockets vs. polling).
- **Detail Owner & Spot Verification Process:** Outline the onboarding steps and verification requirements for parking spot owners and their listed spaces to build trust and ensure compliance.
- **Define Booking Cancellation & Dispute Flows:** Provide initial product requirements for handling booking cancellations, refunds, and simple dispute resolution for both drivers and owners.

## Risks
- **Cold Start Problem for Supply & Demand:** The success of a two-sided marketplace heavily relies on acquiring both sufficient parking spots (supply) and drivers (demand) concurrently. Technical efforts can only facilitate, not guarantee, this market liquidity.
- **Concurrency & Double-Booking Failures:** Inaccurate or delayed real-time availability management could lead to overbookings, severely damaging user trust and operational reputation.
- **Third-Party Service Outages/Changes:** Heavy reliance on external APIs (Stripe, Google Maps, Push Notifications) introduces a dependency risk; outages or significant API changes could impact core functionality.

## Open Questions
- What are the specific requirements for geographic coverage for the MVP launch, and are there any known regional regulatory constraints for parking monetization?
- Will there be a basic communication channel (e.g., in-app chat) between drivers and owners, or is direct contact outside the app assumed for issues?
- What are the initial plans for managing owner payout cycles and minimum payout thresholds (e.g., weekly, monthly, minimum $25)?