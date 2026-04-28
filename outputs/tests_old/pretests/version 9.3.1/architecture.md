## Architecture Notes

### Recommended Technical Approach
A modular monolith architecture is recommended for this MVP due to its simplicity, lower complexity, and cost-effectiveness given the limited budget and modest scalability requirements.

### Main Components or Modules
1. **Event Management Module**
   - Handles event creation, editing, and deletion.
2. **User Authentication & Authorization**
   - Manages user registration, login, and access control.
3. **Attendance Tracking Module**
   - Processes RSVPs and confirms attendance via invitation links.
4. **Budgetary Monitoring Module**
   - Tracks spending against the set budget in real-time.
5. **Notification Module**
   - Sends reminders for upcoming events and alerts about changes.

### Main Data Flow
1. **User Registration**: 
   - New users register through a form and are authenticated using OAuth (e.g., Google, Facebook).
2. **Event Creation**:
   - Users create an event with details, selecting activities and setting a budget.
3. **Invitation Sending**:
   - Invitation links are generated and sent via various channels (email, social media).
4. **Attendance Tracking**:
   - RSVPs received through the invitation links.
5. **Budget Monitoring**:
   - Transactions made during events are recorded against the set budget.
6. **Notifications**:
   - Notifications sent to users for upcoming events and attendance changes.

### Concrete Technical Choices with Short Rationale
1. **Backend Language**: Python (Django) or Node.js (Express)
   - Both languages have strong communities, robust frameworks, and a good balance between ease of learning and performance.
2. **Database**: PostgreSQL or MongoDB
   - PostgreSQL for relational data, MongoDB for flexible document storage.
3. **Frontend**: React or Vue.js
   - Modern JavaScript frameworks that offer a rich user experience and good developer tools.
4. **Authentication**: OAuth/OIDC with Okta or Auth0
   - Secure, standards-compliant authentication service that simplifies user management.
5. **Notification Service**: AWS SNS or Twilio
   - Robust notification services to handle SMS and email reminders.

### Implementation Constraints
- Limited time for development (depends on project timeline)
- Budget constraints for third-party services if required
- Ensuring a straightforward design to avoid technical debt

## Review Summary
The main technical challenge is implementing the modular monolith architecture within the given constraints. The recommended direction focuses on simplicity and flexibility, making it easier to scale and add features in future iterations.

## Requested Changes
1. **Integration with Event Planning Plugins/APIs**:
   - Integrate with popular social media platforms (Instagram, Facebook) for easy event invitation sharing.
2. **Simplified Budgeting Interface**:
   - Simplify the budget tracking interface for users to better manage expenses during events.
3. **Enhanced User Profile Functionality**:
   - Allow users to create and manage profiles with past event participation history.
4. **Activity Suggestions Feature**:
   - Introduce a basic system of suggesting activities based on user preferences and location.

## Risks
1. **User Adoption & Engagement**:
   - Limited initial features may not attract a large user base.
2. **Data Privacy & Security**:
   - Ensuring robust security measures to protect user data and event details.
3. **Scalability Issues**:
   - The modular monolith might need refactoring for higher demand but is acceptable for MVP.

## Open Questions
1. **Third-Party Services for Event Planning Integration**:
   - Are there specific APIs that could enhance the event planning capabilities of the app?
2. **User Authentication Providers**:
   - Which third-party authentication service is preferred between Okta and Auth0?
3. **Notification Preferences**:
   - Should users have the option to choose receiving notifications via SMS or email?