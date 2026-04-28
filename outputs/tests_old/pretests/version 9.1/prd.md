# Product Requirements Document (PRD)

## 1. Product Description
**Product Name:** Friend Night Organizer (FNO)
**Description:** Friend Night Organizer is a mobile application that simplifies the process of organizing social gatherings with friends, including event planning, guest lists, and reminders.

## 2. Problem Statement
Social events are often stressful, time-consuming, and require significant coordination efforts among participants. Friends Night Organizer aims to streamline this process by automating scheduling, inviting guests, managing RSVPs, and providing real-time updates.

## 3. Target User
**Demographics:** Primarily young professionals (18-45 years old) who enjoy socializing but struggle with organizing events.
**Psychographics:** Digital natives who prefer convenience and automation in their daily lives. They value ease of use and seamless integration into their existing ecosystems.

## 4. Expected Value
**For Users:**
- **Time节省：** Reduce planning time by automating tasks like inviting guests, managing RSVPs, and sending out invitations.
- **Engagement增长：** Increase engagement with friends by simplifying the process of organizing events.
- ** Convenience便携性：** Have a single platform for all event-related activities.

## 5. Core Workflow
1. **Event Creation:** Users can create an event with essential details such as date, time, location, and theme.
2. **Guest List Management:** Easily add guests to the list and set their responses (e.g., attending, possibly attending).
3. **Invitations:** Send automated invitations to guests via email or SMS using React Native for the front-end and Node.js with Express for the back-end.
4. **Reminders:** Receive reminders a day before and the morning of the event leveraging Socket.IO for real-time communication.
5. **Real-time Updates:** View real-time attendance status and any changes made by other users.

## 6. First Version Scope
### Features:
- Event creation with basic details (name, date, time, location).
- Guest list management and response tracking.
- Automated invitation sending via email and SMS using an SMTP service.
- Basic reminders using a notification system within the app.
- Real-time attendee status display.

### Non-functional Requirements:
- User-friendly interface: A clean, intuitive design that matches popular social media platforms for easy adoption.
- Reliability and performance: Ensure the app is stable and can handle multiple concurrent users and events.
- Security: Encrypt sensitive data (guest information) to protect user privacy using token-based authentication.

## 7. Key Constraints and Risks
**Constraints:**
- Limited time until the MVP release.
- Budget constraints for marketing and development resources.