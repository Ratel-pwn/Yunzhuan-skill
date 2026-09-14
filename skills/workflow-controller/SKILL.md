---
name: workflow-controller
description: Coordinate the topic-to-script-to-voice workflow. Use when Codex needs to decide which stage comes next, which sub-skill to call, whether to wait for user confirmation, and when to hand off to the TTS script.
---

# Workflow Controller

This skill manages the high-level sequence only.

## Stages

- prepare
- chat
- draft
- draft_confirm
- tts
- tts_confirm
- video_stub
- done

## Rules

- At `prepare`, use `prepare-topic-chat` if enabled.
- At `draft`, use `article-from-chat`.
- At `tts`, call the configured TTS script with the approved draft text.
- Stop for confirmation at any stage whose config flag is true.
- Do not invent video generation behavior yet. Keep it as a documented placeholder.

## Output

State the next stage, required input, and expected artifact.
Do not rewrite the article skill or TTS internals here.
