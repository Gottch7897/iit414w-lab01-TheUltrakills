# Technical Memo

## Subject
Simple DNF risk prediction for race planning.

## Audience
Team principal and race-operations staff.

## Main question
Before a race weekend, can we flag which drivers are more likely to DNF (Did Not Finish)?
This helps the team choose safer or riskier strategy plans.

## What was compared
We tested 4 prediction methods on the same data and with the same evaluation setup:
- Baseline: Always predict DNF
- Logistic Regression
- Random Forest
- XGBoost

Score used: F1 score (higher is better, and 1.0 is perfect).

## Results
- Baseline (always DNF): Train F1 0.675, Validation F1 0.536, Test F1 0.526, Gap -0.149
- Logistic Regression: Train F1 0.776, Validation F1 0.550, Test F1 0.566, Gap -0.210
- Random Forest: Train F1 0.772, Validation F1 0.593, Test F1 0.658, Gap -0.114
- XGBoost: Train F1 0.798, Validation F1 0.603, Test F1 0.655, Gap -0.143

## What this means in simple terms
Random Forest got the best test result (0.658). XGBoost was almost tied (0.655).

Both of these beat the simple baseline (0.526) and Logistic Regression (0.566).

The train-to-test drop is smallest for Random Forest (-0.114), which means it stays more stable when tested on unseen races.

## Recommendation
Use Random Forest as the main model for this lab.

Keep XGBoost as backup because it is very close and could become better after more tuning.

## How to use this in practice
- Use the model to rank drivers by DNF risk.
- Do not treat it as certainty; treat it as decision support.
- A score near 0.66 is useful, but mistakes will still happen.

## Limitations and next steps
1. Accuracy is moderate, not perfect.
2. Some important race situations are not fully captured yet (weather changes, incidents, reliability shocks).
3. We still need deeper checks on difficult race types (street circuits, wet races, new circuits).

Next improvements:
1. Evaluate performance on specific race types.
2. Add better context features while keeping strict time-safe training.
3. Tune alert threshold based on team priorities (missing a real risk vs raising too many false alarms).