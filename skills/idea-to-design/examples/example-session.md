# Example Session: Adding a Notification System

## Phase 0: Context Detection

**Skill**: I've scanned the current directory. Here's what I found:

```
Project context:
- Directory: /app/my-saas
- Status: Existing Next.js project with PostgreSQL, Prisma ORM, NextAuth
- Tech stack: TypeScript, Next.js 14, PostgreSQL, Prisma, Tailwind CSS
- Suggested approach: New feature on existing project
```

I see you have a user auth module and a task management system already. Let's figure out what you want to build.

---

## Phase 1: Clarify

**Skill**: What problem are you trying to solve? What's happening today that's not working well?

**User**: Users miss important updates — when someone comments on their task or assigns them something, they have no idea unless they manually check.

**Skill**: Makes sense. A couple of follow-ups:
- What kind of notifications are we talking about — in-app, email, push, or some combination?
- How urgent is this? Should notifications appear in real-time, or is a slight delay acceptable?

**User**: In-app only for now. Real-time would be nice but not critical — a few seconds delay is fine.

**Skill**: Got it. One more — do users need to manage their notifications? Like marking as read, or choosing which events they want to be notified about?

**User**: Mark as read yes. Preferences can wait for v2.

**Skill**:
```
Here's my understanding:

- Problem: Users miss important updates (comments, assignments) because there's no notification mechanism
- Target users: All app users
- Goal: Users see relevant updates without manually checking; reduce missed actions
- Scope: In-app notifications for comments & assignments, mark-as-read. No email/push, no preferences management in v1.
- Constraints: Existing Next.js + PostgreSQL stack, near-real-time (few seconds delay OK)
- Approach: New feature module on existing project

Does this capture it correctly?
```

**User**: Yes, that's right.

---

## Phase 2: Shape (PRD)

**Skill**: Let's walk through the user journey. When a notification-worthy event happens (say, someone comments on your task), what should the user experience?

**User**: A bell icon in the header shows a badge with unread count. Click it to see a dropdown with recent notifications. Click a notification to go to the relevant page.

**Skill**: Clear. What about these scenarios:
- What if there are 200 unread notifications — do we paginate or just show the latest N?
- Empty state — new user with zero notifications, what do they see?
- What if the notification source is deleted (e.g., a comment gets removed)?

**User**: Show latest 20 with a "view all" link. Empty state just says "No notifications yet." Deleted source — show notification but say "content no longer available" when clicked.

**Skill**: Good edge case handling. Here's the requirements table taking shape:

| ID | User Story | Requirement | Acceptance Criteria | Priority |
|---:|------------|-------------|---------------------|----------|
| R1 | As a user, I want to see a notification bell with unread count | Notification bell in header with badge | Given unread notifications exist, When I view any page, Then I see a bell icon with the unread count | P0 |
| R2 | As a user, I want to browse my notifications | Notification dropdown with latest 20 items | Given I click the bell, Then I see up to 20 notifications sorted by newest first | P0 |
| R3 | As a user, I want to navigate to the source | Click notification to navigate | Given I click a notification, Then I'm taken to the relevant task/comment | P0 |
| R4 | As a user, I want to mark notifications as read | Mark as read on click + bulk mark all | Given I click a notification, Then it's marked as read and the badge count decreases | P0 |
| R5 | As a user, I want to see all notifications | "View all" page with pagination | Given I click "View all", Then I see a paginated list of all notifications | P1 |

Does this look right? Anything to adjust in priority?

---

## Phase 3: Architect (Technical Design)

**Skill**: For the architecture, I see two approaches:

1. **Polling**: Frontend polls `/api/notifications` every 10-30 seconds. Simple, works with your current setup, but not truly real-time.
2. **Server-Sent Events (SSE)**: Server pushes to client. Near-real-time, moderate complexity, works well with Next.js API routes.

Given you said "few seconds delay is fine" and you're on Next.js, I'd lean toward SSE — it's simpler than WebSockets but still gives a good UX. What do you think?

**User**: SSE sounds good.

**Skill**: For the data model, I'm thinking:

```
Notification
- id: UUID
- userId: FK → User
- type: enum (COMMENT, ASSIGNMENT)
- sourceId: FK → Task/Comment
- sourceType: string
- title: string
- read: boolean (default false)
- createdAt: timestamp
```

This is a single table approach — simple and sufficient for v1. If you later add email/push, we'd add a `channel` and `deliveryStatus` field. Sound reasonable?

**User**: Yes, let's go with that.

---

## Phase 4: Plan

**Skill**: How do you want to break this down? I'd suggest three milestones:

| Milestone | Scope | Deliverable | Target |
|-----------|-------|-------------|--------|
| M1: Backend | Data model + API endpoints + SSE | Working API, notifications created on events | Week 1 |
| M2: Frontend | Bell component + dropdown + navigation | Functional notification UI | Week 2 |
| M3: Polish | Empty states, error handling, "view all" page, testing | Production-ready feature | Week 3 |

Does this timeline work for your team?

---

## Output

Skill generates `docs/notification-system-design.md` containing the full PRD + technical design, plus outputs a summary in the conversation.
