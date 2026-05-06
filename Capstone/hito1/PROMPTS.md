# PROMPTS.md — AI Usage Log
# IIT414W · [TheUltrakills] · [Capstone Milestone]

---

## Entry [N] — [Short title, e.g. "DNF handling for rolling avg"] · [2026-05-DD]

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

---

## Entry [1] — [Implementing 2 features] · [2026-05-05]

**Context:**
To speedup the process of implementing our 2 features, we used AI. These are
- grid_position
- constructor_avg_finish_pos_5race_rolling

**Prompt(s):**
# Include all iterations. Label Prompt 1, Prompt 2 (refinement), etc.
Prompt 1: "create the necesary features to implement a logistic regression on: [grid_position, constructor_avg_finish_pos_5race_rolling]"
Prompt 2 (refinement): "read the dataset and create the grid_position and constructor_avg_finish_pos_5race_rolling features. "
Prompt 3 (error output): "KeyError: 'constructor_avg_finish_pos_5race_rolling'"

**Relevant Output:**
"Creating necesary features" cell

**Validation:**
# Required. Describe specific tests — what you ran, on what data, what result.
- Test 1:  tried running it and failed, had to go back and ask to improve the code (prompt 3)
- Test 2: ran "df.columns" to validate the addition of the features

**Adaptations:**
- cell didn't execute properly, so I asked AI to fix it 
- first iteration overcomplicated grid_position, so I had to manually change it.

**Final Decision:**
USED - the code ran and, after validation, seems to work as intended.

---