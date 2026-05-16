# Hito 2 — F1 Race Strategy Advisor

## Contents

- `hito2_modeling.ipynb`: two-target modeling notebook for `is_top10` and `is_top5`.
- `baseline_comparison.md`: target-expansion rationale and model-comparison table template.
- `error_analysis.md`: error slices by strategy type, circuit type, and constructor tier.
- `whatif_scenario_selection.md`: approved target-disagreement scenario.
- `whatif_comparison.md`: final what-if recommendation.
- `leakage_audit.md`: feature roles, excluded columns, scenario-input framing, and confounding notes.
- `mitigations.md`: risks and mitigations tied to observed failure slices.
- `PROMPTS.md`: documented AI use in the required six-field format.

## Data path

The notebook expects the race-level dataset at:

```text
../../test/f1_strategy_race_level.csv
```

## Environment

Use the course-approved stack only:

```text
pandas
numpy
matplotlib
scikit-learn
xgboost
shap
```

The Hito 2 notebook currently uses:

```text
pandas
numpy
scikit-learn
```

## Locked modeling choices

- Targets: `is_top10` and `is_top5`
- Model family: logistic regression
- Split: train 2019-2021, calibration 2022, test 2023-2024
- Calibration: sigmoid/Platt-style calibration on 2022
- Feature set: conservative pre-race context plus strategy scenario inputs
- Random seed: `RANDOM_SEED = 414`

## Reproduction steps

1. Open `hito2_modeling.ipynb`.
2. Run all cells in order.
3. Confirm `split_summary` shows train 2019-2021, calibration 2022, and test 2023-2024.
4. Confirm `feature_audit` labels `n_stops`, `strategy_type`, and `compound_sequence` as scenario inputs.
5. Confirm `model_comparison` reports Brier score, log loss, and ROC-AUC for both targets.
6. Confirm `error_slice_tables` contains slices by `strategy_type`, `circuit_type`, and `constructor_tier` for both targets.
7. Read `whatif_comparison.md` for the target-disagreement recommendation.

## Test-set rule

The Hito 2 model setup was locked before viewing 2023-2024 metrics. After those metrics are viewed, do not retune the model family, feature set, preprocessing, or calibration method based on test performance.
