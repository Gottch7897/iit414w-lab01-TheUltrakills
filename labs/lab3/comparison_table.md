# Comparison Table Across Models

| Model | n_features | Train F1 | Val F1 | Test F1 | F1 Gap |
|---|---:|---:|---:|---:|---:|
| Baseline: Always DNF | 0 | 0.675 | 0.536 | 0.526 | -0.149 |
| Logistic Regression | 9 | 0.776 | 0.550 | 0.566 | -0.210 |
| Random Forest | 9 | 0.772 | 0.593 | 0.658 | -0.114 |
| XGBoost | 9 | 0.798 | 0.603 | 0.655 | -0.143 |

## WHY each model performed the way they did

- **Baseline (always DNF):** This captures the class imbalance signal (many DNFs), so it gets a non-trivial F1 without learning race context. Its lower test F1 confirms that a "blind guess" (guess always) misses event-specific patterns.

- **Logistic Regression:** Performance is better than baseline, but lower than tree models. This is because linear decision boundaries cannot model nonlinear interactions, where these other models gain an advantage.

- **Random Forest:** Best test F1 in this run (0.658). The model benefits from nonlinear splits and feature interactions, while staying very slightly more robust than XGBoost on the test period (0.003 diff). However, it has the lowest gap between all the models.

- **XGBoost:** Very strong train and validation performance, and very close to RF (0.655 vs 0.658). The tiny drop versus Random Forest suggests mild temporal generalization sensitivity, but overall it remains one of the strongest models (2nd best F1 and gap).

## Takeaways

- Tree-based models (Random Forest and XGBoost) are the strongest for DNF prediction here, while Logistic Regression is a useful, interpretable baseline and Always-DNF is a minimal reference point. 
- The Test F1 results are not that great across the board (~65%), and as such, will require a deeper investigation on the input data (ex: amount of features too low?).