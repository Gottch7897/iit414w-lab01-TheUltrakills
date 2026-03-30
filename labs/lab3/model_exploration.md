# Model Exploration - [`Martín Gottschalk, Marcial Ibañez`]
## IIT414W - Lab 3 - Initial exploration - March 30, 2026

## 0. Framing Decision (initial - you can revise for Lab 3 final submission)
- **Business question:** "how many points should we expect?"
- **Target:** [points]
- **Metric:** MAE
- **Why this framing:** We need to predict a numeric outcome (expected points), so regression is the most direct framing for the team-principal question. MAE is appropriate because it reports the average absolute error in points (easy to interpret operationally), and it is less dominated by a few large misses than RMSE in this zero-inflated F1 target.
- **Rejected alternative:** Using Logistic Regression (classification), because it is designed for categorical outputs (e.g., top-10 yes/no), not continuous point values. That framing would lose point-level detail (for example, 1 point vs 25 points) and would not align directly with our business question of expected points.


## 1. Models Trained
| Model | Key Hyperparameters | Features Used |
|---|---|---|
| [Ridge] | [alpha=1.0, random_state=RANDOM_SEED] | ['grid, position_lag_1, rolling_avg_pos_3, constructor_avg_grid_5, rolling_avg_pts_3, circuit_id, constructor_id'] |
| [Random Forest] | [n_estimators=100,
        max_depth=10,
        min_samples_leaf=5,] | ['grid, position_lag_1, rolling_avg_pos_3, constructor_avg_grid_5, rolling_avg_pts_3, circuit_id, constructor_id'] |
| [Random Forest OWN] | [n_estimators=50,
        max_depth=5,
        min_samples_leaf=5,] | ['grid, position_lag_1, rolling_avg_pos_3, constructor_avg_grid_5, rolling_avg_pts_3, circuit_id, constructor_id'] |

## 2. Comparison Table (same metric, same validation)
| Model | Features | Validation | Train [MAE] | Test [MAE] | WHY this result |
|---|---|---|---|---|---|
| [baseline MEAN] | - | 2023-2024 | - | [5.923] | [Just a direct mean comparisson] |
| [Ridge] | ['grid, position_lag_1, rolling_avg_pos_3, constructor_avg_grid_5, rolling_avg_pts_3, circuit_id, constructor_id'] | 2023-2024 | [3.350]	 | [3.299] | [Linear + regularized model; may miss nonlinear grid-to-points effects.] |
| [Random Forest] | ['grid, position_lag_1, rolling_avg_pos_3, constructor_avg_grid_5, rolling_avg_pts_3, circuit_id, constructor_id'] | 2023-2024 | [2.482] | [2.838] | [Captures nonlinear patterns + can overfit on limited data] |
| [Random Forest OWN] | ['grid, position_lag_1, rolling_avg_pos_3, constructor_avg_grid_5, rolling_avg_pts_3, circuit_id, constructor_id'] | 2023-2024 | [2.960] | [2.854] | [Shallower trees reduce variance] |


## 3. Best Model Justification (3+ sentences)
The best model in this comparison is the Random Forest (n_estimators=100, max_depth=10, min_samples_leaf=5) because it achieved the lowest test MAE (2.838). This is a clear improvement over Ridge (3.299) and a major improvement over the baseline mean predictor (5.923), which means it is reducing average prediction error by several points per driver entry. The train-test gap is moderate (2.482 train vs 2.838 test), so there is some overfitting risk, but not enough to cancel its advantage on the test set. Mechanistically, this model can learn nonlinear effects and interactions (for example, grid position behaving differently depending on constructor and circuit), which a linear Ridge model cannot capture as effectively. For the current objective of estimating expected points, this gives the strongest balance between predictive accuracy and practical usefulness.

## 4. One Honest Limitation
One honest limitation is that the best model (Random Forest) is less interpretable and still shows a non-trivial generalization gap (train MAE 2.482 vs test MAE 2.838), which indicates some sensitivity to the training set. In practice, this means the model may be less reliable when race conditions shift (new circuits, unusual weather, or regulation changes), because tree-based patterns learned from past seasons may not transfer perfectly. So even with the best MAE in this notebook, predictions should be used as decision support, not as a standalone race-strategy truth.


