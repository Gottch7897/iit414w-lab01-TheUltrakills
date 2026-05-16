# F1 Race Strategy Advisor: Conditional Strategy Choice Depends on the Target

Team: Martín Gottschalk, Marcial Ibáñez  
Course: IIT414W - Artificial Intelligence Workshop - 2026-1T  
Date: May 17, 2026  
Repo: https://github.com/Gottch7897/iit414w-lab01-TheUltrakills.git  
Commit: final-v1

## 1. Executive Summary

This report turns the Hito 1 and Hito 2 work into a strategy-support recommendation for a race strategy engineer making a pre-race call after qualifying. The advisor compares a fixed driver-race context under alternative pit-stop plans and reports calibrated probabilities for two targets: `is_top10` for points security and `is_top5` for stronger upside. In the approved Dutch Grand Prix scenario, the one-stop `M-H` plan has the higher Top 10 probability by 2.6%, while the two-stop `M-H-S` plan has the higher Top 5 probability by 2.3%. The recommendation is conditional: choose the one-stop when protecting points matters most, and choose the two-stop when the strategic objective is Top 5 upside.

The model improves strongly over target-rate baselines for both targets. It nearly reaches the docent Top 10 reference but does not beat it: the locked Top 10 Brier score is 0.139039, compared with the docent Brier of 0.132. This is close, but the report does not treat it as a win. The tool is useful as decision support, not causal proof, because strategy choice is observational and confounded with car pace, driver quality, traffic, weather, and race incidents.

## 2. Problem Framing

The supported decision is a pre-race strategy call before the start, after qualifying information is available. The decision-maker is a race strategy engineer who needs to compare whether a selected driver-race context should prioritize a one-stop or two-stop plan. The time window matters: the model can use grid position, prior driver and constructor performance, circuit type, and constructor tier, but it must not use race outcomes or incident summaries as if they were known before the race.

The prediction unit is one driver in one race. The primary target is `is_top10`, matching the locked capstone requirement and the docent baseline comparison. The expansion target is `is_top5`, chosen because it preserves the probabilistic framing while exposing a higher-upside decision that `is_top10` can hide. In F1 terms, this separates points security from the chance of a stronger finish.

Strategy fields such as `n_stops`, `strategy_type`, and `compound_sequence` are scenario inputs. They are post-race observations in the raw data, so using them as normal pre-race predictors would be leakage. In this advisor, they are user-controlled values for a what-if question: "what if the strategy desk selected this plan?"

Key assumptions are: the strategy desk is comparing feasible plans, the driver and circuit context remains fixed within a scenario comparison, and the output is a model-based probability estimate rather than a causal estimate of the strategy effect. The main consequence is that recommendations must be conditional and paired with reliability warnings.

## 3. Data and Validation

The race-level dataset has 2,447 driver-race rows from 2019-2024. The locked split is temporal: train on 2019-2021, calibrate on 2022, and evaluate once on 2023-2024. The split prevents random leakage across seasons and matches the reference comparison.

The feature audit separates pre-race context from scenario inputs, audit-only columns, and outcomes. The model uses `grid_position`, `driver_prior3_avg_finish`, `constructor_prior3_avg_finish`, `driver_circuit_prior_avg`, `constructor_tier`, and `circuit_type` as known context. It uses `n_stops`, `strategy_type`, and `compound_sequence` only as scenario controls. It excludes outcomes such as `finish_position`, `points`, `positions_gained`, `is_top3`, `is_top5`, and `is_top10`, and excludes realized race-condition columns such as safety-car, VSC, weather, wet-lap, DNF, and status fields.

Known dataset limitations are carried into the interpretation. Coverage starts in 2019, `qualifying_position` is only a grid-position stand-in, `qualifying_time_s` is empty, safety-car information is coarse, and strategy choice is not independent of pace and race context.

## 4. Modeling Approach

The report uses separate logistic-regression models per target. This follows the selected narrative: each target gets its own calibrated probability model while preserving a common feature boundary and temporal split. The model family is intentionally conservative. It is easier to explain to an F1 strategy audience than a larger learner, and it reduces the risk of hiding leakage behind model complexity.

The baseline for each target is the training target rate. The Hito 1 grid-only heuristic is retained as background evidence, but the final two-target comparison uses the Hito 2 target-rate baseline so both targets are evaluated consistently. For the main models, numeric features are median-imputed and standardized; categorical features are mode-imputed and one-hot encoded; logistic regression uses `RANDOM_SEED = 414`.

Calibration uses sigmoid/Platt calibration on the 2022 block. This was selected because the calibration season is small, so a smooth calibrator is safer than isotonic calibration. Calibration is not used for model selection, and the 2023-2024 test set is only used for final locked evaluation.

## 5. Results and Honest Comparison

| Target | Approach | Brier | Log loss | ROC-AUC |
|---|---|---:|---:|---:|
| `is_top10` | target-rate baseline | 0.249702 | 0.692551 | 0.500 |
| `is_top10` | calibrated logistic regression | 0.139039 | 0.443436 | 0.881266 |
| `is_top5` | target-rate baseline | 0.191789 | 0.571728 | 0.500 |
| `is_top5` | calibrated logistic regression | 0.090479 | 0.305743 | 0.934413 |
| `is_top10` | docent calibrated reference | 0.132000 | not provided | 0.892000 |

The Top 10 model is close to the docent reference but below it. The Brier gap is +0.007039, and the ROC-AUC gap is -0.010734. The honest comparison is therefore: the model beats the simple baseline by a large margin but does not beat the docent floor.

The Top 5 model adds useful signal. Its Brier score is 0.090479 and ROC-AUC is 0.934413, showing that the expansion target is not just a formal requirement. It supports a different strategic objective: whether an aggressive plan improves higher-finish upside.

Calibration plots are regenerated as `figures/calibration_is_top10.png` and `figures/calibration_is_top5.png`. They should be read as probability-quality evidence, not as proof that every slice is reliable.

## 6. Error Analysis and What-If

The required slices are strategy type, circuit type, and constructor tier. The clearest failure modes are:

1. `is_top10` is weakest for midfield constructors: 407 rows, Brier 0.158903, mean absolute probability error 0.336403. This matters because midfield teams are where strategy, traffic, and small pace differences often decide points.
2. `is_top10` is also weak for `three_plus_stop` strategies: 153 rows, Brier 0.157422. These strategies often reflect disruption, damage, or recovery attempts rather than clean pre-race plans.
3. `is_top5` is weakest for front constructors: 170 rows, Brier 0.180871. Front teams almost always have high Top 10 probability, but Top 5 depends on exact execution, teammate competition, tyre timing, and race events.

The approved what-if scenario fixes a George Russell-style Mercedes context at the 2024 Dutch Grand Prix: permanent circuit, grid P4, midfield constructor tier, driver prior-three average finish of 5.0, constructor prior-three average finish of 5.0, and driver-circuit prior average of 10.5. Only the strategy inputs change.

| Scenario | Stops | Type | Compound sequence | P(is_top10) | P(is_top5) |
|---|---:|---|---|---:|---:|
| A | 1 | `one_stop` | `M-H` | 0.892756 | 0.788785 |
| B | 2 | `two_stop` | `M-H-S` | 0.866485 | 0.811390 |

`is_top10` alone favors the one-stop by 2.6%. `is_top5` favors the two-stop by 2.3%. The operational consequence is that the strategy desk should not ask only "which plan protects points?" If the race objective is Top 5 upside, the model changes the preferred plan.

## 7. Limitations and Risks

The main limitation is scenario dependence under regime shift and observational confounding. The dataset covers only 2019-2024, and race strategies are not randomly assigned. A two-stop plan may look better partly because of the cars, drivers, degradation regimes, or incidents associated with the historical cases where it was used.

Single-team deployment is also risky. The selected what-if context uses a midfield constructor, and midfield Top 10 predictions are the weakest constructor-tier slice. The model should therefore report a reliability warning beside the recommendation rather than hiding the slice risk.

We do not recommend deploying this tool unless (1) the strategy desk limits it to pre-race what-if comparisons with explicitly fixed driver-race context, (2) every recommendation displays target-specific slice reliability for strategy type, circuit type, and constructor tier, and (3) the team validates the model on a fresh race weekend or simulator backtest before treating the probabilities as operational guidance.

## 8. Reproducibility Note and AI Reflection

The repository includes the Hito 1 and Hito 2 source artifacts, this report generator, regenerated tables, figures, and the final PDF. A third party should run `venv/bin/python Capstone/Final_Report/generate_final_report.py` from the repository root after installing the course environment. All model `random_state` arguments use `RANDOM_SEED = 414`.

AI assistance was used to structure the final report, convert Hito evidence into executive-language prose, draft captions and Q&A prompts, and critique the honesty sentence. The outputs were checked against the locked Hito files and regenerated tables. Suggestions that implied causal strategy effects or claimed the Top 10 model beat the docent baseline were rejected because they overstated the evidence.

## 9. References

IIT414W course capstone brief and Canvas rubrics. (2026). F1 Race Strategy Advisor.

Course dataset: `f1_strategy_race_level.csv`, seasons 2019-2024.

FastF1 project documentation and historical Formula 1 timing data sources.

Jolpica F1 API documentation and historical race metadata sources.

scikit-learn developers. (2026). Logistic regression, calibration, and model evaluation documentation.
