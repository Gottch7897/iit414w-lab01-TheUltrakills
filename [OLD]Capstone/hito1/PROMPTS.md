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

## Entry [2] — Fix Experiment 3 (pit_stop_duration baseline) · [2026-05-06]

**Context:**
Experiment 3 was failing with a KeyError when trying to access `avg_pit_stop_duration_s` in calibration and test splits. The feature needed to be created on all splits (train, calibration, test) before pipeline evaluation. Additionally, Experiment 3 needed to evaluate on the TEST set (not validation) and report Brier, log loss, and ROC-AUC metrics with calibration curves, consistent with the checklist requirements.

**Prompt(s):**
Prompt 1: "FIX EXPERIMENT 3"

**Relevant Output:**
Experiment 3 cell now:
- Creates `avg_pit_stop_duration_s` on train, calibration, and test splits
- Fits Baseline 3 (grid_position + constructor_avg_finish_pos_5race_rolling + n_stops + avg_pit_stop_duration_s) on train
- Evaluates on TEST set: Brier 0.1358, Log loss 0.4276, ROC-AUC 0.8833
- Compares vs Baseline 2 on test set
- Generates calibration curve plot for both Baseline 2 and Baseline 3 on test set
- Applies pit_duration scenarios and reports probabilities

**Validation:**
- Test 1: Ran cell after fix — executed successfully without KeyError
- Test 2: Confirmed `avg_pit_stop_duration_s` is present in all three splits (train, calibration, test)
- Test 3: Verified test-set metrics (Brier, log loss, ROC-AUC) are reported and calibration plot is generated
- Test 4: Scenario impact with pit_duration computed and displayed

**Adaptations:**
- Added explicit feature creation on calibration and test splits (not just train)
- Added helper function `ensure_features()` to gracefully handle missing features with sensible defaults
- Changed evaluation from validation set to TEST set for consistency with checklist
- Added Baseline 2 to calibration curve plot for visual comparison

**Final Decision:**
USED - cell now executes without errors, meets checklist requirement for test-set evaluation with Brier, log loss, and calibration curves.

---