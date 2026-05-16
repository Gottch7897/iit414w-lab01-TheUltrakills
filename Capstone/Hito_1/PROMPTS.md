# PROMPTS — Hito 1

## Entry 1 — Phase A planning

**Context:** We needed an execution plan for Hito 1 and Hito 2 using the capstone brief, Hito 1 rubric, Hito 2 rubric, and the race-level CSV preview.

**Prompts:** Asked Codex to read `test/capstone.md`, `test/hito1.md`, `test/hito2.md`, and the head of `test/f1_strategy_race_level.csv`, then produce a step-by-step execution plan without writing code.

**Output:** Codex produced a plan with Hito 1 and Hito 2 sections, step IDs, rubric mappings, inputs, outputs, decision checkpoints, and rough effort estimates.

**Validation:** We checked the plan against the Canvas requirements: locked target `is_top10`, locked temporal split, baseline requirement, leakage audit, PROMPTS requirement, Hito 2 two-target requirement, and required error-analysis slices.

**Adaptations:** Several decisions were moved into `test/decisions.md` so the methodology would not be chosen silently. The Hito 2 disagreement scenario was deferred until model outputs can identify real candidate disagreements.

**Final Decision:** Use the plan as the execution structure, with explicit stops before methodology decisions and no implementation before approval.

## Entry 2 — Rejected split-summary suggestion

**Context:** During Hito 1 step `H1.S03`, Codex added a temporal split cell that summarized the train, calibration, and test rows.

**Prompts:** Asked Codex to continue to the next step and create the locked split.

**Output:** The first version included `target_rate_is_top10` for the 2023-2024 test set.

**Validation:** This violated the test-set rule because it inspected a test outcome summary before the baseline was locked.

**Adaptations:** The user asked to redo the step. Codex corrected the notebook so the test split only reports row count and season range, while target rates are shown only for train and calibration.

**Final Decision:** Keep the corrected split cell. Do not inspect 2023-2024 target rates or metrics until the baseline is locked.
