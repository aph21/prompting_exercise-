# Prompt Engineering Practice Log
### Goal: Become a Top 1% Agentic + Full Stack AI Engineer

This repo documents my daily Claude Code prompting practice. Each day I work through one scenario, write multiple prompt attempts, receive evaluation feedback, and lock in one core lesson.

---

## Why This Repo Exists

Prompting is an engineering skill — not intuition. This repo is my training log. Every bad prompt, every correction, every rewrite is tracked here so I can measure real growth over time.

---

## Daily Structure

Each day lives in its own folder:

```
Prompt_engineering/
├── Day_1/
│   ├── Scenario.txt    ← the task description given for the day
│   ├── prompts.txt     ← all attempts + feedback in one file
│   └── code.py         ← the final working script
├── Day_2/
│   └── ...
├── learnings.md        ← detailed learning log (all days)
└── README.md
```

### Inside `prompts.txt`

```
SCENARIO
--------
[the task description]

=== ATTEMPT 1 ===
[my prompt]

--- Feedback ---
Score: X/10
[evaluation notes]

=== ATTEMPT 2 ===
[my revised prompt]

--- Feedback ---
Score: X/10
[evaluation notes]

=== ATTEMPT 3 (Final) ===
[my final prompt]

--- Feedback ---
Score: X/10
[evaluation notes]

--- Model Prompt ---
[the ideal prompt revealed after attempt 3]
```

---

## Progress Tracker

| Day | Concept | Attempt 1 | Attempt 2 | Attempt 3 | Lesson |
|-----|---------|-----------|-----------|-----------|--------|
| 01 ✅ | Task Clarity + Constraints | 6.5 | 7.5 | 9.2 | Every constraint must earn its place |
| 02 ✅ | Multi-step Agentic Prompting | - | - | - | Explicitly define data gaps and exact output formats |
| 03  | - | - | - | - | - |

---

## Prompting Template (Discovered Day 1)

Every good Claude Code prompt answers these 5 things:

```
Task    → What exactly needs to be built
Input   → How data arrives, format, datatype
Logic   → Constraints, what NOT to use, rules
Output  → Exact format of the result
Process → Plan first → implement → verify with test cases
```

---

## My Prompting Rules (Built Over Time)

These rules get added as I learn them. Each one was earned through a mistake.

1. Every constraint must earn its place — don't add rules that don't affect the outcome
2. Prompting is additive revision — carry what worked, fix what didn't
3. Specify input format explicitly — never let Claude guess (comma-separated? space-separated?)
4. Always include at least one concrete test case with expected output
5. An agentic prompt tells Claude how to handle decisions, not just what to build

---

## Concepts Roadmap

### Phase 1 — Prompting Foundations (Days 1–10)
- [x] Day 01 — Task clarity + constraints → [Learning Log](Day_1/learnings.md)
- [x] Day 02 — Multi-step agentic prompting → [Learning Log](Day_2/learnings.md)
- [ ] Day 03 — Handling ambiguity and decision gaps
- [ ] Day 04 — File I/O and side effects
- [ ] Day 05 — Error handling instructions
- [ ] Day 06 — Prompting for APIs
- [ ] Day 07 — Prompting with context (existing codebase)
- [ ] Day 08 — Iterative building (prompt chaining)
- [ ] Day 09 — Prompting for debugging
- [ ] Day 10 — Full mini-project prompt

### Phase 2 — Agentic Prompting (Days 11–20)
- [ ] Day 11 — Multi-agent task delegation
- [ ] Day 12 — Prompting with tools (file system, APIs)
- [ ] Day 13 — Memory and context passing between steps
- [ ] Day 14 — Agentic loop design
- [ ] Day 15 — Error recovery instructions
- [ ] Day 16 — Prompting for code review
- [ ] Day 17 — Prompting for refactoring
- [ ] Day 18 — Prompting with constraints (time, tokens, cost)
- [ ] Day 19 — Agentic workflow with external services
- [ ] Day 20 — Full agentic mini-project

### Phase 3 — Full Stack Prompting (Days 21–30)
- [ ] Day 21 — Frontend component prompting
- [ ] Day 22 — Backend API prompting
- [ ] Day 23 — Database schema prompting
- [ ] Day 24 — Auth flow prompting
- [ ] Day 25 — End-to-end feature prompting
- [ ] Day 26 — Prompting for testing
- [ ] Day 27 — Prompting for deployment scripts
- [ ] Day 28 — Full stack debugging prompt
- [ ] Day 29 — Architecture decision prompting
- [ ] Day 30 — Complete full stack feature from one prompt

---

## Stack Focus
- Language: Python / JavaScript
- Backend: Node.js + Express / FastAPI
- Frontend: React
- AI/LLM: Claude API, OpenAI API
- Tools: Claude Code, Git, GitHub

---

*Started: 2026 | Target: Top 1% Agentic + Full Stack AI Engineer*