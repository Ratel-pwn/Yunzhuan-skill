---
name: dsgo-app-agent-test
description: Standardize testing of the DSGO Android APP Agent. Use when Codex is asked to test, verify, debug, repair, or benchmark DSGO APP Agent generation flows, including creating a game through the installed Android app, iterating Agent repairs, validating Dora runtime behavior, collecting screenshots/logs/task records, and producing a concise troubleshooting brief for follow-up iteration.
---

# DSGO APP Agent Test

## Purpose

Test the DSGO Agent only through the installed Android APP path. Do not generate or repair the target game by external scripts, desktop browser flows, direct file edits, or manual Dora project writes unless the explicit task is to fix the APP/Agent infrastructure itself.

For detailed report templates and the historical baseline from the gravity Tetris test, read `references/test-brief-template.md` when preparing the final brief.

## Required Boundaries

- Treat Android APP Agent execution as the product path: DSGO APK -> embedded Dora Android runtime/core -> APP private Dora project files -> native play/debug/log bridge.
- Use `local/dev/start-android.ps1` for rebuild/install/launch when frontend, Android, native bridge, Agent prompt, or visible behavior changes.
- Verify `adb reverse tcp:4000 tcp:4000` before installed-APP API tests.
- The generated game must be produced by the APP Agent conversation. Inspect generated files and logs only to diagnose; feed repairs back into the APP Agent conversation.
- Do not use external Dora Web IDE, external Dora WebServer, `localhost:8866` as a product runtime dependency, or host-side generation as a substitute for APP Agent generation.

## Workflow

1. Establish baseline context.
   - Read `AGENTS.md`, `frontend/DESIGN.md` if UI changes are involved, and relevant ADRs when runtime/Agent boundaries are touched.
   - Record branch, dirty files, emulator id, backend/API status, and current APP screen.

2. Prepare Android connectivity.
   - Run `adb devices`.
   - Run `adb reverse tcp:4000 tcp:4000`.
   - Run `adb reverse --list`.
   - Check the host API URL required by the test, usually `http://127.0.0.1:4000/api/app/games/feed`.
   - If code changed, run `local/dev/start-android.ps1`; otherwise confirm the currently installed APK contains the intended code.

3. Start the APP Agent test from the Android APP.
   - Navigate in the installed APP to the relevant Agent entry point.
   - Enter the user’s prompt through the APP UI.
   - If ADB text input cannot type Chinese, use an English prompt that preserves the same product intent and note this in the brief.
   - Do not create the target project through any non-APP route.

4. Monitor Agent task execution.
   - Track the latest record in `backend/api/.local/agent-tasks.json`.
   - Capture task id, status, prompt, final files, validation result, and the last significant events.
   - If the task fails, classify the failure as APP bridge, backend/API, embedded Dora host, Agent prompt/validation, generated Lua runtime, or UI/run-button behavior.

5. Diagnose failures without bypassing APP generation.
   - It is acceptable to inspect generated `init.lua`, manifest, logcat, screenshots, and app-private files.
   - If generated code is wrong, send a repair request through the same Android APP Agent conversation.
   - If product infrastructure is wrong, fix product code, rebuild/install the APP, then continue the APP Agent conversation.

6. Run and verify on the emulator/device.
   - Use the APP “运行” entry or product run path.
   - Capture at least two screenshots several seconds apart.
   - For games, verify visible content, continuous update, touch input, and the requested gameplay mechanic.
   - A build pass alone is not verification.

7. Iterate until useful outcome or hard blocker.
   - Each Agent repair is a separate round. Record what prompt was sent and what problem it addressed.
   - Stop only when the APP-generated project runs and satisfies the user’s core requirement, or when a clear infrastructure blocker remains with evidence.

## Brief Requirements

Always include:

- Number of APP Agent rounds.
- Per-round prompt intent, result, failure, and next action.
- Product code changes made to enable the APP Agent path.
- Exact validation commands and whether they passed.
- Screenshot/log/task artifact paths.
- Whether the final result is suitable for phone operation, with evidence.
- Residual risks and the next recommended fix if applicable.

Keep the brief concise enough for issue triage, but include concrete task ids, file paths, and screenshots so the next iteration can start without rediscovery.
