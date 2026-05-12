# Team Decision Sheet — Capstone Hito 1
### IIT414W · F1 Race Strategy Advisor · Mon May 4, 2026

> **Instructions.** Complete this sheet in your team repo as `framing.md`. Every team has 60 minutes during the studio block (14:45–15:45). Required commits: by 15:00 (sections 1–4 populated) and by 15:40 (full sheet + dataset-load notebook). No section can be left blank — write "TBD with rationale" if you are uncertain, but blank entries fail the framing rubric.

**Team name:** TheUltrakills
**Team members:** Martín Gottschalk, Marcial Ibáñez
**GitHub repo URL:** https://github.com/Gottch7897/iit414w-lab01-TheUltrakills.git

---

## 1. Decision Context

**What strategy decision is this tool supporting?**

Choose amount of pit stops, depending on current grid placement (ex: midfield driver).

**Who makes this decision?**
The strategy desk in charge of the pits, during a Friday evening meeting.

**When in the race weekend is the decision made?**
"Friday evening, after FP2, so the team has time to prepare and adapt for race Sunday"

---

## 2. Target & Metric

**Target (LOCKED for Hito 1):** `is_top10`

**Primary metric:** Brier 0.132

**Why this metric for this decision?** We choose Brier 0.132 as our primary metric because it directly measures the mean-squared error of predicted probabilities (rewarding both calibration and sharpness), is threshold‑independent for probability-based decisions, and 0.132 represents a meaningful improvement over the baseline that meets our calibration requirements for reliable P(top10) predictions.


**Secondary metric (optional but recommended):** ROC-AUC 0.892

**Temporal split (LOCKED for Hito 1):**
- Train: seasons 2019, 2020, 2021
- Calibration: season 2022 (used to fit calibration mapping; never for model selection)
- Test: seasons 2023, 2024 (untouched until final evaluation)

---

## 3. Baseline Plan

**Baseline approach (one sentence):**
>Logistic regression on: [grid_position, constructor_avg_finish_pos_5race_rolling]


**Why is this baseline F1-defendable?** (One sentence — could you justify it without ever seeing 2023–2024 data?)

> Constructor rolling average is computed from training data (2019–2021) and frozen; no test-set leakage. Captures team form without overfitting.

**Direction check:** higher baseline score means higher predicted P(top10). Yes / No / Explain.

> "Yes. Better grid position (lower number) and stronger constructor form (lower average finish position) both increase predicted P(top10), which matches F1 operational intuition."

**Expected baseline performance vs docent floor:**
- Grid-rule docent baseline: Brier = 0.208 on test
- Calibrated docent model: Brier = 0.132 on test, ROC-AUC = 0.892
- Our team's best baseline expected to land near: Likely Brier ≈ 0.17–0.20

---

## 4. What-If Comparison Plan

**Strategy variables we will vary:**
- [X] `n_stops`
- [ ] `compound_sequence`
- [ ] `stint_lengths` (or stint1_length, stint2_length, etc.)
- [X] `avg_pit_stop_duration_s`
- [X] Other: `constructor_avg_finish_pos_5race_rolling`

**Concrete scenarios to compare (at least two, with specific values):**

> Scenario A — Aggressive 1‑stop (Dry): grid_position: 10, constructor_avg_finish_pos_5race_rolling: 8.5, n_stops: 1, stint1_length_laps: 40, stint2_length_laps: 0, avg_pit_stop_duration_s: 22, wet_day: 0.

> Scenario B — Conservative 2‑stop (Wet / slower stops): grid_position: 10, constructor_avg_finish_pos_5race_rolling: 8.5, n_stops: 2, stint1_length_laps: 18, stint2_length_laps: 24, avg_pit_stop_duration_s: 26, wet_day: 1.

**Decision metric for the comparison:**
"Difference in calibrated P(is_top10) between Scenario A and Scenario B, with bootstrap 95% confidence interval."

---

## 5. Limitations Acknowledgment

**Five known dataset limitations are documented in the Capstone Brief. Which TWO most affect our team's specific approach?**

Limitation #1 we acknowledge: "Strategy features are observed post-race (see Leakage Rules above). They are scenario inputs in this capstone, not pre-race signals."

> Why it matters for our approach (1 sentence): as our approach is focused on avg finish position, we need to be careful of them as using them as inputs inflates apparent baseline performance. Treating n_stops as a pre-race predictor will produce optimistic, non-deployable estimates and bias model selection.

Limitation #2 we acknowledge: "Strategy choice is not independent of car pace, driver, weather, and race incidents. Teams must discuss this confounding when they make recommendations."

> Why it matters for our approach (1 sentence):  Teams choose strategy based on latent factors (car pace, driver strength, weather, incidents). If our baseline doesn’t model those confounders, the estimated effect of strategy (or its predictive value) mixes causal and correlational signals. That makes counterfactual comparisons unreliable and can mislead decisions that assume the model isolates strategy impact.

---

## 6. Experiment Plan for Hito 1

**Three experiments we will run between today and Wednesday 16:20:**

1. Fit a calibrated logistic regression baseline using grid_position and constructor_tier only, then compare it against a model that also includes n_stops.
2. Run two concrete what-if scenarios for the same driver/circuit pair: one-stop (M-H, longer final stint) versus two-stop (S-M-M, shorter stints).
3. Test whether adding avg_pit_stop_duration_s changes calibrated P(is_top10) enough to matter in the comparison plan.

**Hypothesis for each (one line each — what do we expect to happen and why?):**

> 1. Adding n_stops should improve the baseline a little because pit strategy is part of the race outcome, but grid position will still remain the strongest single signal.
> 2. The one-stop and two-stop scenarios should produce different top-10 probabilities because tire freshness and pit-loss trade off differently by stint length.
> 3. avg_pit_stop_duration_s should have a smaller effect than grid position, but it may still shift the comparison when two strategies are otherwise close.

---

## 7. Team Workflow

**Who is doing what between now and Wednesday?**

| Member | Owns | Branch / file in repo |
|---|---|---|
| Marcial | Dataset preparation, features | main |
| Martin  | Notebook and modeling | main |

**When does each member commit by?** (We need at least one commit per member per day Tue and Wed.)
> Marcial: between Monday and Tuesday
> Martin: between Tuesday and Wednesday, before class. 

---

## 8. Critique Received in Pair Review


**Reviewing team:** Model Thinkers

**Concrete critique we received:**

> "Your Section 6 does not define a fallback if model quality stays near docent baseline levels. The consequence is that on Demo Day you may show results without a defensible decision policy. One thing to do: add a pre-committed fallback rule (calibrated scenario ranking + uncertainty thresholds) for cases where Brier does not clearly improve."

**How we will address this critique by Wednesday:**

> We shall follow their advice and add a pre-committed fallback rule: if the calibrated model does not improve Brier by at least 0.01 over the docent-calibrated baseline, we will not force a model-based recommendation. Instead, we will rank the pre-defined strategy scenarios by calibrated `P(is_top10)` and only pick a winner when the bootstrap 95% confidence interval for the top-vs-runner-up gap is entirely above 0.03; otherwise we report “no clear winner” and fall back to the conservative 2-stop scenario.

---

## Self-Check Before Committing

Before you push this to GitHub, verify:

- [X] Decision context is one sentence, not a paragraph
- [X] Target says exactly `is_top10` (not "Top-10" or "P(top10)")
- [X] Temporal split shows three blocks: 2019–2021 / 2022 / 2023–2024
- [X] Baseline is described in code-realistic terms (we could implement it)
- [X] What-if scenarios have specific feature values, not generic words
- [X] At least 2 of the 5 limitations are acknowledged with consequence
- [X] PROMPTS.md exists in the repo (even if empty for now — will be populated by Wednesday)
