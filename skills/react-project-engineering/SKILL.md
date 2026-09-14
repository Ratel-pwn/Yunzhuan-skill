---
name: react-project-engineering
description: Keep React frontend projects modular during business changes, UI behavior changes, feature expansion, refactors, page additions, state/service changes, or layout/navigation work. Use before editing React/TypeScript frontend code so components, pages, feature modules, app shell/layout, hooks, services, persistence, and tests stay in the right layer instead of causing file, directory, and page-level coupling bloat.
---

# React Project Engineering

## Purpose

Use this skill before changing a React frontend when the task affects business behavior, UI behavior, feature scope, navigation, layout, shared components, state orchestration, API calls, persistence, or route/page structure.

The goal is to make the correct ownership boundary explicit before editing, so work does not accumulate in oversized pages, duplicated components, or ad hoc directories.

## Required Workflow

1. Read local project rules first.
   - Check for files such as `AGENTS.md`, `README.md`, `DESIGN.md`, architecture docs, or existing plans.
   - If the project has UI/design rules, read them before changing visible behavior.
   - If a repo-specific rule conflicts with this skill, follow the repo-specific rule and explain the conflict briefly.

2. Classify the change before editing.
   - `app shell/layout`: global frame, safe area, navigation visibility, providers, route hosts, modal hosts, page type frames.
   - `page composition`: route/page assembly, passing feature props, choosing feature hooks.
   - `feature domain`: business UI, domain hooks, reducers, model mapping, domain constants, feature services.
   - `shared UI`: buttons, fields, tabs, icon buttons, drawers, sheets, dialogs, chat primitives, reusable cards.
   - `service/integration`: API clients, native bridges, persistence, external SDKs, auth/session, runtime bridges.
   - `assets/docs/tests`: static media, documentation, verification, fixtures.

3. Inspect before creating.
   - Search existing components, hooks, services, models, constants, and page frames before adding a new file.
   - Prefer extending an existing component with a narrow prop/slot over duplicating a near-identical component.
   - If a missing directory is clearly the right boundary, create it immediately instead of parking global logic in a page.

4. Pick the owning layer.
   - `src/app/`: app shell, navigation orchestration, layout frames, providers, global session/action routing.
   - `src/app/layout/`: page frames, safe-area handling, bottom-nav/header avoidance, scroll containers, page type primitives.
   - `src/pages/`: route-level composition only. Pages may choose hooks and compose features; they should not own gesture engines, polling, API normalization, or layout infrastructure.
   - `src/features/<domain>/components/`: domain presentation components without direct API calls.
   - `src/features/<domain>/hooks/`: domain state orchestration, subscriptions, feature-level gestures.
   - `src/features/<domain>/model/`: API-to-view models, reducers, event normalization, status labels, sorting/grouping.
   - `src/features/<domain>/services/`: domain wrappers over shared API/native/persistence services.
   - `src/features/<domain>/constants/`: static options, mock fixtures, development data sources.
   - `src/components/ui/`: business-agnostic primitives.
   - `src/components/overlays/`: sheets, drawers, dialogs, modal primitives.
   - `src/components/chat/`: shared chat display/composer primitives.
   - `src/services/`: API clients, native/runtime bridges, persistence, auth/session, external integrations.

5. Block common bloat patterns.
   - Do not implement tab swipe thresholds, carousel mechanics, or tab traversal in page files when a tab component or feature tab component should own it.
   - Do not implement safe-area, fixed header height, bottom navigation avoidance, or page scroll behavior in each page.
   - Do not create private header/button/form/sheet/drawer primitives if a shared primitive can be extended.
   - Do not put API response normalization, Agent/event mapping, markdown rendering policy, sorting/grouping, or status-label generation in page files.
   - Do not leave replaced UI hidden with CSS. Delete it or guard it with a named feature flag and removal plan.

6. Split before continuing when a file is already too large.
   - Treat a page over roughly 250 lines, more than three local components, or any page containing API polling, bridge calls, gesture state machines, or non-trivial reducers as a split trigger.
   - Move responsibility first, then change behavior. Avoid combining broad refactors with unrelated visual changes.

7. Validate from the product surface.
   - Run the project’s typecheck/lint/build commands when available.
   - For visible UI changes, inspect the actual app surface with browser/device/emulator screenshots or interaction checks.
   - For mobile/native work, test through the installed app when the product requires app-level verification; direct API tests are supporting diagnostics only.

## Before Editing Checklist

State the answers briefly in your working notes or user update when the task is non-trivial:

- What layer owns this change?
- Which existing components/hooks/services did I inspect?
- Am I extending a shared primitive or creating a new one? Why?
- Does this require creating/moving a layout, model, hook, service, or constants file before editing the page?
- What verification will prove the product behavior, not just the code, works?

## Directory Creation Rule

If the correct layer does not exist, create it instead of placing logic in the nearest page. For example, if multiple pages need shared header/nav/safe-area/scroll behavior, create `src/app/layout/` and move that behavior there during the task.

## Output Expectations

When finishing, summarize:

- The ownership boundary chosen.
- Files moved or created to prevent coupling.
- Any duplicated or dead code removed.
- Verification performed and any blocked checks.
