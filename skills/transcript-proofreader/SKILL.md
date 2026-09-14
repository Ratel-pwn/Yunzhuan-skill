---
name: transcript-proofreader
description: Perform direct transcript proofreading for txt/srt/vtt/markdown subtitle files with semantic correction (ASR misrecognitions, homophone mistakes, wrong words in context) while preserving timing structure. Use when users ask to proofread transcript text, correct subtitle recognition errors, fix homophone substitutions, improve subtitle accuracy, or batch-correct machine transcriptions before publishing.
---

# Transcript Proofreader

## Direct-Use Rules

- Use this skill directly for text proofreading tasks; do not require external APIs by default.
- Read file content, edit text lines semantically, and write corrected output according to user-selected output mode.
- Preserve timing/index/header lines exactly for subtitle formats (`.srt`, `.vtt`).
- Prefer minimal semantic edits: fix recognition errors, keep intent unchanged.

## Workflow

1. Read the source transcript file and detect format (`.txt`, `.srt`, `.vtt`, `.md`).
2. Proofread text with semantic correction:
   - Correct ASR misrecognitions and homophone substitutions based on context.
   - Correct typo-level and grammar-level errors only when they improve transcript fidelity.
   - Preserve domain terms, names, and numbers unless clearly wrong in context.
   - Keep speaker intent unchanged; do not paraphrase for style.
3. Preserve structure:
   - For `.srt`: keep index lines and timestamp lines unchanged.
   - For `.vtt`: keep cue timing and headers unchanged.
   - Only edit spoken text lines.
4. Before writing, ask user exactly one confirmation question:
   - Output to original location as a new copy, or
   - Output to original location by overwriting, or
   - Save to a new output path.
5. Write output:
   - If original-location copy is selected, create `<filename>.proofread<ext>`.
   - If overwrite is selected, create a backup `<filename>.bak` first, then overwrite.
   - If new path is selected, write to the specified path.
6. Report result:
   - Output path.
   - Number of edited lines.
   - A short list of representative semantic corrections.
   - Any ambiguous corrections that may need manual review.

## Confirmation Template

Use one concise question:

`请选择输出方式：1) 原位置创建副本 2) 原位置覆盖（自动备份 .bak）3) 另存到新路径（请提供路径）`

If user selects option 3, require explicit target path before writing.

## Batch Mode

When user asks to process a folder:

1. Enumerate candidate files (`.srt`, `.vtt`, `.txt`, `.md`).
2. Confirm output mode once for the whole batch.
3. Process files one-by-one and continue on per-file failures.
4. Print per-file status and final summary (`success/fail/skip`).

## Correction Standard

- Prioritize transcript correctness over literal raw ASR output.
- Resolve homophone errors using surrounding sentence meaning.
- Keep punctuation natural for readability, but avoid over-editing.
- For uncertain cases, keep original wording and mark as "needs review".
- Never alter timestamps, cue order, or cue boundaries.

## Guardrails

- Do not rewrite style aggressively or summarize.
- Do not summarize or shorten content.
- Do not alter timestamps or subtitle ordering.
- If the source file is missing or unreadable, stop and request a valid path.

## Script

Use `scripts/save_proofread.py` for deterministic save behavior:
- `--mode local-copy`: write `<filename>.proofread<ext>` in the same folder.
- `--mode overwrite`: overwrite source and create `.bak` backup.
- `--mode save-as --output <path>`: write to a custom path.

Use this script only for saving outputs. The proofreading itself is performed directly by the AI on transcript text lines.

