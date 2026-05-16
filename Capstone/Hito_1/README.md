# Hito 1 — F1 Race Strategy Advisor

## Contents

- `framing.md`: Hito 1 problem framing, baseline plan, leakage discussion, limitations, and Hito 2 experiment plan.
- `hito1_baseline.ipynb`: runnable baseline notebook for the locked target `is_top10`.
- `PROMPTS.md`: documented AI use in the required six-field format.

## Data path

The notebook expects the race-level dataset at:

```text
../../test/f1_strategy_race_level.csv
```

Run the notebook from the `Capstone/Hito_1/` folder or keep the relative path unchanged.

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

The Hito 1 baseline notebook currently uses:

```text
pandas
numpy
matplotlib
scikit-learn
```

## Reproduction steps

1. Open `hito1_baseline.ipynb`.
2. Run all cells in order.
3. Confirm the leakage audit classifies strategy columns as scenario inputs.
4. Confirm the temporal split is train 2019-2021, calibration 2022, and test 2023-2024.
5. Confirm the final evaluation reports Brier score, log loss, ROC-AUC, and a calibration curve for `is_top10`.

## Locked Hito 1 decisions

- Target: `is_top10`
- Split: train 2019-2021, calibration 2022, test 2023-2024
- Baseline: grid-only heuristic using `grid_position`
- Calibration: sigmoid/Platt calibration on 2022
- Random seed: `RANDOM_SEED = 414`

After the final test metrics are viewed, the baseline must not be retuned.
