---
name: skill-wizard
description: Guide the user through creating a complete Skill from scratch via structured conversation. Use when users say "create a skill", "make a skill", "generate a skill", "new skill", "write a skill", "build a skill", or describe a repeatable workflow they want to automate or codify — even if they do not explicitly say "skill". Also trigger when users say "turn what we just did into a skill", "save this as a skill", or "package this workflow".
---

# Skill Wizard — Conversational Skill Generator

Guide the user step-by-step through a structured conversation, turning a vague idea into an installable, reusable, high-quality Skill.

## Core Principles

- **Conversation-driven**: Act like a patient product manager. Focus each round on key questions and collect information incrementally.
- **Prefer multiple-choice**: Users prefer picking from options over coming up with answers from scratch. Use `AskUserQuestion` to present multiple-choice questions whenever possible, and reserve open-ended questions for cases that truly require free-form input. Batch up to 4 related questions into a single `AskUserQuestion` call to reduce back-and-forth.
- **Progressive construction**: Build the skeleton first, then fill in details, then polish. The user can say "good enough" at any time to skip remaining steps.
- **Adapt to the user's level**: Pay attention to wording — technical users use jargon, non-technical users use plain language. When in doubt, briefly explain the term.
- **Fast track**: If the user provides enough information in one go (task, inputs/outputs, and steps are all clear), skip incremental questioning and jump straight to the confirmation step. Do not force every questioning step.
- **Flexible stages**: Stages are a guiding framework, not a rigid pipeline. The user can add to or revise earlier decisions at any time — handle it on the spot instead of asking them to "go back to a previous stage".

---

## Conversation Flow

The entire flow has 5 stages. Stages can be navigated flexibly; user additions and corrections take priority over stage order.

### Stage 0: Deduplication Check (Silent)

Before starting any conversation, scan the project's `skills/` directory (if it exists) to see whether a Skill with similar functionality already exists.

1. Use Glob to scan `skills/*/SKILL.md`
2. Quickly read the frontmatter (name + description) of each SKILL.md and compare it against the user's described need
3. If a highly similar Skill is found, inform the user and show key details. Let the user choose:
   - Modify the existing Skill
   - Create a new one from scratch (using the existing one as a reference)
   - Directly improve the existing one
4. If no similar Skill is found, skip silently — do not interrupt the user

This step prevents reinventing the wheel and lets users build on existing work.

### Stage 1: Understand Intent + Define Scope (Combined)

Goal: In one or two conversation rounds, clarify what the Skill does, how it works, and what the inputs/outputs are.

**Step 1: Capture the core intent.**

If the user has already given a clear description (e.g., via command args), go directly to information collection. Otherwise, ask:
"What task do you want this Skill to accomplish? Describe it in one sentence."

**Step 2: Batch-collect key decisions with multiple-choice questions.**

Based on the user's description, identify 2-4 key dimensions that require user decisions and present them via `AskUserQuestion` in one call. Provide 2-4 options per question, each with a short explanation.

Multiple-choice design principles:
- Options must be specific and distinguishable — not abstract ("Option A" vs "Option B" is bad; "Lightweight validation" vs "Full analysis" is good)
- If there is a recommended option, place it first and label it "(Recommended)"
- Include an "Other" option for free-form input, so you only need to cover the 2-4 most common cases

Typical question dimensions (choose flexibly based on the Skill type):
- Core functionality / working mode
- Output format / depth
- Target audience

**Step 3: Follow-up confirmation.**

If details not covered by the multiple-choice questions remain, ask 1-2 follow-up questions. For uncertain points, offer a default suggestion for the user to confirm rather than making them think from scratch.

**Fast track:** If the user provides very detailed requirements in one go, skip the multiple-choice questions and output the understanding confirmation directly.

**Extract from conversation history:** If the user says "turn what we just did into a skill", extract directly from the current conversation history: which tools were used, execution steps, corrections the user made, and input/output formats. Use the extracted information as the output of this stage — skip questioning and go straight to confirmation.

At the end of this stage, output:
```
Understood. Let me confirm my understanding:
- Task: [one-sentence description]
- Trigger scenario: [when would this be used]
- Rough steps: [1, 2, 3...]
- Input: [what is needed]
- Output: [what is produced, in what format]
Does this look right? Anything to add or correct?
```

Absorb any additions or corrections the user provides here directly — no need to "restart the flow".

### Stage 3: Draft — Generate the Skill

Goal: Based on information collected in the previous stages, generate the SKILL.md and related files.

#### Naming

Generate a name for the Skill following these rules:
- Lowercase English + hyphens (`-`)
- Reflect verb intent, e.g., `generate-changelog`, `analyze-csv`, `review-pr`
- Avoid overly broad names (e.g., `utils`, `helper`)

Propose a name for the user to confirm: "I suggest calling it `xxx-yyy` — does that name work for you?"

#### File Structure

```
skills/<skill-name>/
├── SKILL.md          # Core instruction file (required, written in English)
├── README.md         # Human-facing documentation (recommended, written in Chinese)
├── scripts/          # Optional: helper scripts
├── references/       # Optional: reference documents
├── examples/         # Optional: examples
└── assets/           # Optional: resource files
```

Only create the files that are necessary. A simple Skill may only need SKILL.md + README.md.

#### SKILL.md Writing Rules

**Language conventions:**
- SKILL.md (including frontmatter) must be written entirely in **English** — SKILL.md is an instruction file for the Agent, and English yields more stable comprehension and execution.
- README.md must be written in **Chinese** — README is documentation for team members to read.
- Files under examples/ can be in any language; follow the natural language of the example content.

**Frontmatter (required):**
- `name`: Must match the directory name
- `description`: Under 200 characters. Clearly describe "what it does + when to use it" (in English). Write it in a slightly "pushy" tone so the Agent can more easily auto-invoke it in the right scenario. For example, do not just write "Generate changelog" — instead write "Generate changelog from Git commit history. Use when users mention changelog, release notes, version summary, or pre-release preparation."

**Body writing principles:**
- Use imperative sentences for instructions ("Read the file" not "You should read the file")
- Explain why rather than piling on MUST/NEVER — today's LLMs are smart enough to handle nuance when they understand the reasoning
- Provide 1-2 concrete input/output examples
- If there are more than 5 steps, consider splitting into subsections with subheadings
- Keep total length under 500 lines; move details to `references/` if longer

#### Quality Self-Check Checklist

After generating SKILL.md, go through the following checklist item by item before writing the file. If any item fails, fix it first:

| # | Check Item | Pass Criteria |
|---|------------|---------------|
| 1 | Frontmatter complete | Both `name` and `description` exist and are non-empty |
| 2 | Description trigger coverage | Includes "what it does" and at least 3 trigger keywords/scenarios |
| 3 | Input/output documented | Body clearly states what input is needed and what output is produced |
| 4 | At least 1 example | Contains a concrete input/output example, not just abstract description |
| 5 | Boundary/exclusion documented | States when the Skill should not be used or what it should not handle |
| 6 | No hardcoded sensitive info | Contains no API keys, passwords, tokens, etc. |
| 7 | Referenced paths correct | All referenced scripts/references/assets paths exist |
| 8 | Total length reasonable | Does not exceed 500 lines; overflow has been moved to references/ |

#### Description Polishing

The description is the key factor in whether the Agent decides to invoke the Skill. After generating the initial description, polish it using the following method:

1. **Coverage check**: Imagine 3 things a user might actually say (casual, formal, terse). Check whether the description would match. If not, add keywords.
2. **Exclusivity check**: Imagine 2 scenarios that should not trigger the Skill but could easily be confused with it. Check whether the description would false-match. If so, add qualifying conditions.
3. **Final format**: `[What it does]. Use when users [trigger scenario 1], [trigger scenario 2], [trigger scenario 3]. [Optional: how it differs from X / when not to use].`

Show the polished description to the user for confirmation.

#### Post-Generation Presentation

Show the user the complete generated SKILL.md and explain:
- What scenarios will trigger this Skill
- What the core execution logic is
- Which files were created
- Quality self-check checklist pass status

### Stage 4: Validate — Test Run

Goal: Verify the Skill works as expected using test cases.

#### Construct Test Cases

Based on the Skill's functionality, construct 2-3 test prompts and show them to the user:

"I have prepared a few test scenarios to validate this Skill. Let me know if they look reasonable:"
- Test 1: [Typical scenario] — the most common usage
- Test 2: [Edge case] — empty input / extreme values / non-standard format
- Test 3: [Error-prone scenario] — easy to get wrong or easily confused with another Skill

Write test prompts as a real user would speak — include specific file names, paths, and context rather than abstract descriptions.

#### Execution Method

Choose the validation approach based on the runtime environment:

**When subagent capability is available (Claude Code):**
Launch a subagent for each test prompt. Have it read the Skill and execute the task. Save output to `<skill-name>-workspace/test-<N>/`. Multiple tests can be launched in parallel.

```
Subagent prompt template:
"Read <skill-path>/SKILL.md, then follow its instructions to complete the following task:
<test prompt>
Save output to <workspace>/test-<N>/outputs/"
```

**When subagent is not available:**
Execute each test prompt directly following the SKILL.md instructions and show the results to the user.

#### Result Evaluation

After execution:
1. Show the user the output of each test
2. Ask for feedback: "Do these results match your expectations? Anything to adjust?"
3. Modify SKILL.md based on feedback and re-run the failed test cases
4. Loop until the user is satisfied

If the user says "no need to test" or "this is fine for now", skip this stage.

### Stage 5: Deliver — Installation Guide

Goal: Help the user install the Skill to a usable location.

Ask the user about their usage scenario first, then provide the corresponding installation method:

**Local project usage:**
```bash
# Copy the Skill to the project's .claude/skills/ directory
cp -r skills/<skill-name> .claude/skills/<skill-name>
```

**Global usage (available across all projects):**
```bash
# Install the Skill to the global skills directory
cp -r skills/<skill-name> ~/.agents/skills/<skill-name>
# For agents that need symlinks (e.g., Claude Code)
ln -s $(pwd)/skills/<skill-name> ~/.claude/skills/<skill-name>
```

**Team sharing:**
Remind the user they can commit to the awesome-joto-skills repository for team use:
1. Place the Skill directory under `skills/`
2. Add a README.md
3. Submit a PR

Close with a summary:
```
Your Skill "<name>" is ready!

- Location: skills/<skill-name>/
- Trigger: [describe trigger keywords and scenarios]
- Files included: [file list]
- Quality check: [pass count]/8 items passed

Next steps:
- Try using it to see how it works
- For deeper optimization and benchmarking, use /skill-creator
- To improve trigger accuracy, use skill-creator's description optimization feature
```

---

## Special Scenario Handling

### Extracting a Skill from an Existing Conversation

When the user says "turn what we just did into a skill" or "save this workflow as a skill":

1. **Extract information**: Review the current conversation history and extract the following:
   - Which tools were used (Bash/Read/Write/Grep, etc.)
   - The order of execution steps
   - Corrections and preferences the user expressed
   - Input/output formats
   - Errors encountered and how they were resolved (these are good sources for boundary conditions)

2. **Generate summary**: Organize the extracted information into the Stage 1 confirmation format and ask the user to confirm

3. **Continue the flow**: Enter Stage 2 to fill in missing information, then proceed with subsequent stages normally

### User Has an Existing Draft

When the user provides a SKILL.md draft or partial content:

1. **Read and analyze** by reviewing each of the following dimensions:
   - Is the frontmatter complete (name + description)?
   - Is the description trigger coverage sufficient?
   - Is there a clear input/output specification?
   - Are there concrete examples?
   - Is there a boundary/exclusion statement?
   - Is the instruction style appropriate (imperative vs. preachy, explaining why vs. piling on MUST)?
   - Do referenced file paths exist?
   - Is the length reasonable?

2. **Output a review report** in this format:
   ```
   Review results:
   PASS [item]: [brief note]
   WARN [item to improve]: [problem description] -> [suggested fix]
   FAIL [missing item]: [what is missing] -> [suggested content to add]
   ```

3. **Confirm then modify**: Go through each improvement suggestion with the user. After confirmation, modify the file directly.

### User Has Only a Vague Idea

When the user says "I want to make a skill but I don't know what to build":

1. Ask: "Is there anything in your daily work that you do repeatedly — roughly the same each time but takes a lot of time?"
2. Help them list 3-5 candidate tasks
3. For each candidate, evaluate the "Skill-ification benefit":
   - High frequency + fixed steps -> very suitable
   - Low frequency but highly complex each time -> suitable
   - Different every time -> not ideal as a Skill
4. After the user selects one, enter the normal flow

---

## Tone and Style

- Act like an experienced colleague helping organize requirements, not a bureaucratic form-filling process
- Keep each reply to a reasonable length — do not dump too much content at once
- When uncertain, offer a suggestion with reasoning and let the user choose, rather than making them think from scratch
- Mirror the user's tone: if the user uses emoji, use emoji; if the user is formal, be formal
- If the user is clearly in a hurry (e.g., "make it quick", "keep it simple"), compress conversation steps and take the fast track
