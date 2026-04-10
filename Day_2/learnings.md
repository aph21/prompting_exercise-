# Prompt Engineering — Learning Log

---

## Day 2 — April 10, 2026

**Concept:** Multi-step Agentic Prompting / Handling Logic Gaps & Output Formats
**Scenario:** Build a Python script that takes a student's name and their 5 subject marks, calculates the average, assigns a grade, prints the pass/fail result, and saves a text file.

---

### What I Practiced Today

Today's practice involved managing multiple steps and requirements: input validation, custom logic, logic mapping (grades), string outputs, and file I/O. The goal was to refine how precisely I specify rules and exact system behaviors.

---

### Attempt 1 

**What I got right:**
- Categorized input rules, logic, output, and process clearly.
- Handled integer/string types and input valid value ranges (0 to 100).
- Instructed Claude to calculate the average and gave grade letter bounds.

**What was missing:**
- Did not specify rounding handling for averages (e.g., how to grade 50.5 vs 51).
- Grade brackets had overlaps (e.g., 35 to 50, then 50 to 65).
- Output format inside the `.txt` file wasn't strictly defined.

---

### Attempt 2 

**Improvements made:**
- Fixed the overlapping grade ranges (35 to 50, 51 to 65, 66 to 80, 81 to 100).
- Detailed what the output `.txt` file should actually contain (Student Name, Marks, Average, Grade).
- Included a robust sample input / test case.

**Still missing:**
- Still missed exactly how decimals should be treated for the average calculation. 
- The `.txt` file content instruction was still a bit vague (it listed what to include, but not the *exact* textual layout required).

---

### Attempt 3 — Final

**Improvements made:**
- Added explicit instruction to "use round() function to round the average to get the nearest integer."

**Why this worked better:**
- Handled the fractional average edge-case.
- Left less ambiguity for the agent regarding mathematical operations.

---

### The Model Prompt Analysis (The "Ideal" Prompt)

By comparing my attempts to the Model Prompt, I found these stark differences:
1. **Explicit File Layout**: The model prompt doesn't just say "file should contain X and Y", it provides an *exact* template:
   ```text
   Student Name: John
   Marks: 80, 90, 70, 60, 50
   ...
   ```
2. **Absolute Logic Bounds**: The model prompt utilizes explicit `>=` and `<=` logic brackets (e.g. `>= 51 and <= 65`) to eliminate any possibility of logic gaps or overlaps.
3. **Rigorous Edge Cases**: Testing wasn't just happy path — it forced a test for failing grades (`30,30,30,30,30`).

---

### Key Lesson of the Day

> **Explicitly define logic boundaries and exact output layouts.**
> Ambiguous boundaries (like "between 35 and 50") might break edge cases. Be declarative with bounds (like `>= 35 and <= 50`). Furthermore, when writing to files, providing a strict visual layout template ensures the AI will format the document exactly as you intend, rather than guessing your preferred styling.

---

### Code Written — `code.py`

(A fully robust Python script handling input validation loop, grade mapping, and file output has been generated.)

---

### Prompting Rules Earned Today

1. **Be absolute with mathematical bounds** — use `<=` and `>=` to prevent gaps and overlaps.
2. **Define exact output structural layouts** — if a file needs specific formatting, provide a literal text block template.
3. **Handle floating point edge cases** — if you divide, explicitly specify if/how rounding should occur.

---

*Day 2 complete. Gained clarity in multi-step boundary constraints.*
