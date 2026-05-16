# Hito 1 Framing — F1 Race Strategy Advisor

## 1. Decision context

This project supports a race strategy engineer who needs to compare pit-stop plans before the race, after qualifying information is available. The decision is whether a selected driver-race context is better served by a one-stop or multi-stop strategy, using the model output as decision support rather than as an automatic strategy selector.

The prediction unit is one driver in one race. For Hito 1, the locked target is `is_top10`, so the first question is: given the pre-race context and a strategy scenario, what is the expected probability that the driver finishes in the Top 10?

The time window matters because it defines what information is allowed. Since this framing is pre-race after qualifying, the model may use known context such as season, race, circuit type, driver/team identifiers, grid position, historical prior-performance features, and constructor tier. It should not treat race outcomes, incident summaries, or realized weather effects as if they were known before the race.

Strategy variables such as `n_stops`, `strategy_type`, `compound_sequence`, and `stint_lengths` are post-race observations in the raw dataset. In this capstone, they are only acceptable when framed as user-controlled scenario inputs for a what-if comparison. They are not being treated as naturally available pre-race predictors.

## 2. First what-if comparison plan

The first planned what-if comparison uses the 2024 Dutch Grand Prix at Zandvoort, a permanent circuit, with George Russell as the driver context. The scenario is framed as a pre-race strategy-desk question after qualifying: for a Mercedes driver starting P4, should the strategy desk prefer a one-stop plan or a two-stop plan?

The comparison will keep the driver-race context fixed and change only the strategy scenario inputs:

| Scenario | Driver context | Strategy type | `n_stops` | `compound_sequence` | `stint_lengths` |
|---|---|---:|---:|---|---|
| A | George Russell, 2024 Dutch GP, grid P4, Mercedes, midfield constructor tier | one-stop | 1 | `M-H` | `25-44` |
| B | George Russell, 2024 Dutch GP, grid P4, Mercedes, midfield constructor tier | two-stop | 2 | `M-H-S` | `23-27-17` |

These strategy values are scenario inputs. They are not being claimed as two simultaneously observed historical strategies for Russell. The point is to compare two feasible plans in the same driver-race context and ask how the expected Top 10 probability changes under the model.

## 3. Target and primary metric

The locked Hito 1 target is `is_top10`. This target is appropriate for the first milestone because it matches the cohort-wide comparison requirement and can be evaluated against the docent baseline on the same temporal split.

The primary metric is Brier score because the advisor produces probabilities, not only class labels. A lower Brier score means the predicted Top 10 probabilities are closer to the observed outcomes. Log loss and ROC-AUC will be reported as supporting metrics: log loss penalizes overconfident wrong probabilities, while ROC-AUC checks whether the baseline ranks likely Top 10 finishes above unlikely ones.

## 4. Baseline plan

The Hito 1 baseline is a grid-only heuristic using `grid_position`. This is defendable from F1 logic because starting position strongly shapes track position, traffic exposure, and the number of overtakes required to reach the points.

The baseline assigns fixed probabilities before test evaluation:

| Grid position | Assigned `P(is_top10)` |
|---:|---:|
| P1-P5 | 0.90 |
| P6-P10 | 0.70 |
| P11-P15 | 0.35 |
| P16+ | 0.15 |
| Missing | 0.50 |

The raw probabilities will be calibrated using sigmoid/Platt calibration on the 2022 calibration block only. The model will then be evaluated once on the locked 2023-2024 test set and compared against the grid-rule baseline Brier score of 0.208 and the docent calibrated model reference of Brier 0.132 and ROC-AUC 0.892.

## 5. Temporal validation and leakage control

The split is locked:

| Block | Seasons | Purpose |
|---|---|---|
| Train | 2019-2021 | Define the baseline logic and development summaries |
| Calibration | 2022 | Fit the sigmoid calibration mapping |
| Test | 2023-2024 | Final evaluation only |

The calibration block is not used for feature selection or test-oriented tuning. The test block is not inspected until the baseline is locked.

The leakage audit classifies columns into four groups:

| Group | Examples | Hito 1 baseline use |
|---|---|---|
| Pre-race | `season`, `race_name`, `circuit_type`, `driver_id`, `Team`, `grid_position`, prior average finish features, `constructor_tier` | Eligible if justified |
| Scenario input | `n_stops`, `strategy_type`, `compound_sequence`, `stint_lengths`, pit-lap and stint-length fields | Excluded from Hito 1 baseline; used only for what-if scenario framing |
| Audit-only | `safety_car_periods`, `track_status_summary`, `weather_actual`, `wet_laps`, temperature fields, `dnf`, `status` | Excluded from baseline; allowed only for limitations, stress tests, or later error analysis |
| Target/outcome | `finish_position`, `points`, `positions_gained`, `is_top3`, `is_top5`, `is_top10` | Excluded from features |

`qualifying_time_s` is not used because the capstone brief states it is empty and should not be treated as a meaningful signal. `constructor_tier` is treated only as coarse pre-race context, not as a race outcome.

## 6. Known data limitations and consequences

Three limitations are especially important for this decision context.

First, the dataset starts in 2019. This limits historical coverage and means the model may not fully learn circuit-specific strategy patterns that require many seasons of evidence.

Second, `qualifying_position` is a stand-in for grid position and `qualifying_time_s` is empty. The project therefore uses `grid_position` for the baseline and avoids any claim about qualifying pace gaps.

Third, strategy choice is confounded with car pace, driver quality, weather, and race incidents. A one-stop strategy is not assigned randomly; stronger cars or better track position may make a strategy look better than it would be for another team. Any recommendation must therefore be stated as model-based decision support, not causal proof that the strategy alone caused the outcome.

## 7. Hito 2 experiment plan

Three conservative Hito 2 experiments are planned.

1. Add `is_top5` as the expansion target and compare it with `is_top10`. Hypothesis: a strategy can preserve Top 10 probability while changing Top 5 upside, which `is_top10` alone cannot reveal.

2. Train a simple logistic-regression model for both targets using leakage-audited features and strategy variables only as scenario inputs. Hypothesis: a simple model with calibrated probabilities can improve decision value over the grid-only baseline while staying interpretable.

3. Run error analysis by strategy type, circuit type, and constructor tier. Hypothesis: model reliability will vary across one-stop vs two-stop strategies and across constructor tiers because strategy choice is confounded with car performance.

## 8. Team workflow

The immediate workflow is to complete the Hito 1 baseline notebook, verify that it runs from a clean clone, and document AI use in `PROMPTS.md`. After Hito 1, the work moves to Hito 2 by adding the `is_top5` target, building the two-target model comparison, and writing concrete error-analysis and mitigation artifacts.
