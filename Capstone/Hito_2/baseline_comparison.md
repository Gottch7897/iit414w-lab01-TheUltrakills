# Baseline Comparison - Hito 2

## Why the second target was added

Hito 2 keeps is_top10 and adds is_top5 to capture a real strategy trade-off: a plan can protect points (Top 10) while still being weaker for high-upside finishes (Top 5). This supports the strategy-engineer use case, where safe and aggressive options can differ.

## Locked evaluation setup

The model setup was locked before looking at 2023-2024 test metrics:

- Model family: logistic regression
- Targets: `is_top10` and `is_top5`
- Split: train 2019-2021, calibration 2022, test 2023-2024
- Calibration: sigmoid/Platt-style calibration using 2022 only
- Feature set: conservative pre-race context plus strategy scenario inputs

Docent reference for is_top10 on test seasons:

- Brier: 0.132 (lower is better)
- ROC-AUC: 0.892 (higher is better)

## Obtained model-comparison results (test: 2023-2024)

| Target | Approach | Brier score | Log loss | ROC-AUC | Interpretation |
|---|---|---:|---:|---:|---|
| `is_top10` | target-rate baseline | 0.249702 | 0.692551 | 0.500 | Constant-probability baseline from train target rate |
| `is_top10` | logistic regression calibrated | 0.139039	|0.443436	|0.881266 | Compare against target-rate baseline and docent reference |
| `is_top5` | target-rate baseline | 0.191789 |	0.571728 | 0.500 | Constant-probability baseline from train target rate |
| `is_top5` | logistic regression calibrated | 0.090479 |	0.305743|	0.934413 | Shows whether expansion target adds usable probability signal |

## Calibration-quality note

For binary targets, lower Brier score and log loss indicate better probability quality. ROC-AUC is secondary because this advisor needs calibrated probabilities for strategy comparison, not only rank ordering.



## Did we beat the docent baseline for is_top10?

Short answer: no, but we were close.

Against the docent reference:

- Brier delta = 0.139039 - 0.132 = +0.007039 (worse, because lower is better)
- ROC-AUC delta = 0.881266 - 0.892 = -0.010734 (worse, because higher is better)

So the calibrated logistic model improved strongly over the naive target-rate baseline, but it did not beat the docent floor on either required metric for is_top10.

## Why we likely did not beat the docent baseline

The gap is small, and the evidence from Hito 2 suggests these likely causes:

1. Conservative model capacity.
The locked model is calibrated logistic regression. This is transparent and stable, but it may underfit non-linear interactions that matter in F1 strategy outcomes.

2. Hard test-period dynamics.
The 2023-2024 seasons can include shifts in car performance and race patterns relative to 2019-2022. A model trained on earlier seasons may lose some discrimination and calibration under those shifts.

3. Confounding and slice instability.
Error analysis shows high-error slices in exactly the contexts that matter for strategy decisions (for example, midfield for is_top10 and three_plus_stop scenarios). These slices increase probability error and can pull overall Brier and ROC-AUC down.

4. Scenario variables are observational, not causal.
Strategy fields are used as what-if inputs, but they are still confounded with race context and car pace. That limits how far a simple observational model can go on headline test metrics.

## What still counts as a valid Hito 2 result

- The locked model clearly beats the constant-probability baseline for both targets.
- is_top5 adds real signal (ROC-AUC 0.934413, Brier 0.090479), supporting the two-target decision story.
- The report should state the is_top10 shortfall honestly and frame recommendations with reliability warnings from the error slices.

## Probability-quality note

For this advisor, calibrated probabilities are primary, so Brier and log loss are first-order metrics. ROC-AUC is still reported for ranking quality, but strategy decisions should be communicated with probability reliability and slice-specific caveats.