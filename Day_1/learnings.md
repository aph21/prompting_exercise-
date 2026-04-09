# Prompt Engineering — Learning Log

---

## Day 1 — April 9, 2026

**Concept:** Task Clarity + Constraints
**Scenario:** Write a Python script that takes a list of numbers and returns the largest one.

---

### What I Practiced Today

The challenge was simple on purpose — to expose raw prompting instincts with zero guidance. The goal wasn't just to get working code; it was to learn *how* to instruct an AI clearly.

Over 3 attempts, my prompt improved dramatically. Here's how:

---

### Attempt 1 — Score: 6.5 / 10

**Prompt written:**
> "Write a python script, which should be able to take a list of numbers from user and then should return the largest number from that list. Before writing the script, plan the implementation. Only when you are fully confident about your plan and script then implement the script and verify the result."

**What I got right:**
- Task stated clearly ✅
- "Plan before writing" — genuine agentic thinking ✅
- "Verify the result" — told Claude to self-check ✅
- "Only when fully confident" — added a quality gate ✅

**What was missing:**
- No edge case handling (empty list? non-integer input?) ❌
- No output format (print it? return it? save to file?) ❌
- "Take from user" is vague — comma-separated? space-separated? ❌
- No constraint on built-ins — use `max()` or manual logic? ❌

---

### Attempt 2 — Score: 7.5 / 10

**Improvements made:**
- Specified `int` as the datatype
- Mentioned output is a single number
- Added uniqueness constraint (each number should be unique)

**Still missing:**
- Input format still vague
- No error handling instructions
- Uniqueness constraint was unnecessary for the core task (wasted constraint)

---

### Attempt 3 — Final — Score: 9.2 / 10

**Prompt written:**
> "Build a Python script that finds the largest number from a user-provided list.
>
> Input rules:
> - Ask the user to enter integers separated by commas (e.g. 3, 7, 1, 9)
> - Parse and convert each value to int
> - If the input is empty or contains non-integer values, show a clear error message and exit
>
> Logic:
> - Do NOT use Python's built-in max() — implement the comparison logic manually
>
> Output:
> - Print: "The largest number is: X"
>
> Process:
> - Plan first, implement only when confident, then run and verify with sample inputs like: 3,7,1,9 → should return 9"

**Why this worked:**
- Input format fully specified (comma-separated, `int` type) ✅
- Edge cases covered (empty input, non-integer values) ✅
- Constraint explicitly stated (no `max()`) ✅
- Output format exact (the exact print string defined) ✅
- Agentic process preserved: plan → implement → verify with test case ✅

---

### The 5-Question Framework (Discovered Day 1)

Every effective prompt answers these 5 questions:

| # | Question | Example from Attempt 3 |
|---|----------|------------------------|
| 1 | **What** to build | Python script, find largest number |
| 2 | **How** input arrives | Comma-separated integers via `input()` |
| 3 | **What** the output looks like | `"The largest number is: X"` |
| 4 | **What** can go wrong | Empty input, non-integer values → clear error |
| 5 | **What** constraints apply | No `max()`, manual comparison logic |

---

### Key Lesson of the Day

> **Every constraint must earn its place.**
> Don't add rules that don't change the outcome. Attempt 2's "unique numbers" rule was noise — it added complexity without improving the result. But "no max()" was meaningful — it forced manual logic, which is the learning objective.

---

### Code Written — `code.py`

```python
def get_largest(numbers: list[int]) -> int:
    """Return the largest integer in a list using manual comparison."""
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
```

**Test Results:**

| Input | Expected | Result |
|-------|----------|--------|
| `3,7,1,9` | 9 | ✅ 9 |
| `5` | 5 | ✅ 5 |
| `-3,-10,-1` | -1 | ✅ -1 |
| *(empty)* | Error | ✅ Error message |
| `3,abc,1` | Error | ✅ Error message |

---

### Prompting Rules Earned Today

1. **Specify input format explicitly** — never let the AI guess (comma-separated? space-separated? `int` or `float`?)
2. **Every constraint must earn its place** — don't add rules that don't affect the outcome
3. **Always include at least one concrete test case** with expected output
4. **Edge cases are your responsibility** — the AI won't add them unless you ask
5. **Agentic instruction pattern works** — plan → implement → verify is a strong process anchor

---

*Day 1 complete. Prompting score grew from 6.5 → 9.2 across 3 attempts.*
