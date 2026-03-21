# PROMPTS.md — AI Usage Log
# IIT414W · [TheUltrakills] · [Lab01]
# One entry per significant AI interaction. Keep entries honest and specific.

---

## Entry [EXAMPLE] — [Short title, e.g. "DNF handling for rolling avg"] · [YYYY-MM-DD]

**Context:**
[1–3 sentences: what you were trying to solve and why it mattered for the task.]

**Prompt(s):**
# Include all iterations. Label Prompt 1, Prompt 2 (refinement), etc.
Prompt 1: "[exact text sent to AI]"
Prompt 2 (refinement): "[exact text]"

**Relevant Output:**
[Paste key output. Summarize if very long. Preserve code exactly.]

**Validation:**
# Required. Describe specific tests — what you ran, on what data, what result.
- Test 1: [what you checked, on what data, and what you found]
- Test 2: [edge case tested and outcome]
- [Comparison with baseline / manual check / unit test / visual check on real data]

**Adaptations:**
- [Bug or error found: description and fix applied]
- [Design choice changed and reason]
- [What the AI missed that you added manually]

**Final Decision:**
[Used / Partially used / Rejected] — [reason in 1–3 sentences, tied to the task.]


## Entry [1] — [LAB2, asked to "fix my heuristic for loop implementation"] [2026-03-18]
Trying to make my heuristic prediction by changing all data into a 1, but failed at implementing the function.

**Prompt(s):**
Prompt 1: "[fix my heuristic for loop implementation]"

**Relevant Output:**
"I’m going to fix that notebook cell by replacing the broken loop with a correct heuristic prediction implementation (without mutating the target), then keep your train/val/test split intact.

I’ve updated the cell; next I’ll run it to confirm the heuristic now executes and produces metrics without errors."

I stopped it here.

**Validation:**
# Required. Describe specific tests — what you ran, on what data, what result.
- Test 1: ran the code succesfully
- Test 2: looked at the dataframe to confirm it was all correct

**Adaptations:**
- It tried to rewrite the entire cell, when I only asked it for 1 small code. I copied the useful code and then went back on its output (undo), pasting the part I needed.

**Final Decision:**
USED: Small code bit, useful for the heuristic.


---