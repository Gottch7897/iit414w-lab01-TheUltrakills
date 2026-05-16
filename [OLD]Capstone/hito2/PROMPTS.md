# PROMPTS.md — AI Usage Log
# IIT414W · [TheUltrakills] · [Capstone Milestone]

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


## Entry [3] — Baseline for top 5 · [2026-05-13]

**Context:**
We needed a quick baseline to compare against our top 5 model.

**Prompt(s):**
# Include all iterations. Label Prompt 1, Prompt 2 (refinement), etc.
Prompt 1: "create a simple baseline for the top 5 model to compare against"
Prompt 2 (refinement): "justify the baseline you just added"

**Relevant Output:**
created a "Prevalence baseline (constant prediction = train positive rate)" and all the cells related to it.


**Validation:**
# Required. Describe specific tests — what you ran, on what data, what result.
- Test 1: cell runs
- Test 2: ran a similar baseline, got the same results.

**Adaptations:**
- Asked the AI to explain the baseline according to our strategy
- Manually added the print against the Model top 5 for easier copy-paste into baseline_comparison.md

**Final Decision:**
Used: the baseline is simple and works for the scenario.

---

