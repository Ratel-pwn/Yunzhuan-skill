---
name: react-native-full-migration
description: Full native migration workflow for converting React web applications that use Tailwind CSS and are packaged as Android apps into real React Native applications. Use when Codex is asked to migrate, refactor, plan, or implement a full React web plus Tailwind Android-packaged app migration to React Native while preserving product behavior, business logic, user flows, visual structure, interaction patterns, and core user experience, without WebView reuse, DOM shims, React Router adapters, Tailwind web compatibility layers, browser polyfills, or old web runtime dependencies.
---

# React Native Full Migration

Use this skill to migrate a React web application that uses Tailwind CSS and is packaged as an Android app into a fully native React Native application.

The target is a full native migration. It is not a compatibility migration.

## Core Goal

Preserve the product while changing the runtime:

- Preserve product behavior, business logic, user flows, visual structure, interaction patterns, and core user experience.
- Reuse platform-independent logic where it is genuinely independent of the browser and DOM.
- Rewrite all UI runtime code as native React Native screens and components.
- Keep implementation aligned with the existing product architecture, repository rules, and verification requirements.

## Non-Negotiable Native Rule

Do not create adapter, shim, bridge, wrapper, or compatibility code whose purpose is to keep the old React web implementation running.

The migrated app must contain native React Native screens and components, not adapted web pages.

Strictly do not use:

- WebView-based old page reuse.
- Old web pages embedded inside a native shell.
- DOM-like wrapper components.
- React Router compatibility adapters.
- React Router to React Navigation bridge layers.
- Tailwind web compatibility shims.
- `window`, `document`, `HTMLElement`, `history`, or `location` browser polyfills.
- Runtime `localStorage` or `sessionStorage` browser polyfills.
- CSS compatibility layers, CSS modules, PostCSS, or browser media query compatibility in the native runtime.
- DOM event compatibility layers.
- HTML element type preservation.
- Bridge code that keeps the old web implementation running.

## Migration Workflow

1. Read the repository rules and current architecture before editing.
2. Inventory the existing web app by feature, route, state source, API client, persistence behavior, native bridge usage, and user flow.
3. Separate platform-independent logic from web runtime code.
4. Define the native application shell with React Navigation, native screens, safe-area handling, platform storage, and app lifecycle behavior.
5. Rebuild shared UI primitives as React Native components instead of adapting HTML elements.
6. Migrate feature screens one flow at a time, preserving behavior and interaction patterns while replacing Tailwind classes with native styles.
7. Replace browser-only APIs with native equivalents only where the product behavior requires them.
8. Delete replaced web runtime code from the native path instead of hiding it behind compatibility flags.
9. Verify with TypeScript, native build checks, Android install or launch checks when available, and user-flow smoke tests.

## Implementation Guidance

Prefer direct native equivalents:

- Use React Navigation for navigation state, stacks, tabs, deep links, and route params.
- Use `StyleSheet`, typed style objects, or an established React Native styling system already accepted by the project.
- Use platform storage such as AsyncStorage or secure storage according to the data sensitivity and existing product rules.
- Use native-safe API clients and runtime bridges that do not depend on browser globals.
- Use React Native gesture, keyboard, modal, safe-area, list, image, and text input primitives.

Keep business logic reusable only when it is free of:

- DOM types or HTML element assumptions.
- CSS, Tailwind, media query, or class-name parsing.
- Browser storage, browser navigation, or browser event assumptions.
- Web-only rendering lifecycle assumptions.

## Verification Expectations

After code changes:

- Run the relevant TypeScript checks.
- Run the relevant native build command.
- Install and launch on Android when a device or emulator is available.
- Verify important migrated flows in the actual app, not only through code review.
- Report exact checks performed and any blockers.

For DSGO specifically, follow the repository `AGENTS.md` Android verification guidance and prefer the local Android startup scripts documented there when user-visible Android behavior changes.
