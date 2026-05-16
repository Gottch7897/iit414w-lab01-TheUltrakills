# Error Analysis — Hito 2

## Method

The error analysis uses the locked 2023-2024 test predictions from `hito2_modeling.ipynb`. Each slice reports sample size, actual outcome rate, mean predicted probability, slice Brier score, and mean absolute probability error.

The required slices are:

- `strategy_type`
- `circuit_type`
- `constructor_tier`

Both targets are analyzed: `is_top10` and `is_top5`.

## Target: `is_top10`

### Slice: strategy type

| Strategy type | Rows | Actual Top 10 rate | Mean predicted probability | Slice Brier | Mean absolute error |
|---|---:|---:|---:|---:|---:|
| `three_plus_stop` | 153 | 0.405 | 0.482 | 0.157 | 0.326 |
| `one_stop` | 353 | 0.561 | 0.580 | 0.147 | 0.314 |
| `two_stop` | 368 | 0.543 | 0.516 | 0.128 | 0.297 |
| `no_stop` | 15 | 0.000 | 0.145 | 0.022 | 0.145 |

Failure hypothesis: the model is weakest for `three_plus_stop` strategies on `is_top10`. The mean prediction is higher than the actual rate by about 7.7 percentage points, suggesting that the model may not fully capture why extra stops happen. In real races, three-plus-stop strategies often reflect disruption, damage, poor tyre degradation, or recovery attempts, not only a planned aggressive strategy.

### Slice: circuit type

| Circuit type | Rows | Actual Top 10 rate | Mean predicted probability | Slice Brier | Mean absolute error |
|---|---:|---:|---:|---:|---:|
| `semi-street` | 118 | 0.508 | 0.518 | 0.171 | 0.339 |
| `permanent` | 579 | 0.518 | 0.529 | 0.135 | 0.303 |
| `street` | 192 | 0.521 | 0.539 | 0.131 | 0.296 |

Failure hypothesis: `semi-street` circuits have the highest `is_top10` Brier score despite a moderate sample size of 118 rows. These races may combine street-circuit disruption with permanent-circuit pace patterns, making the simple circuit-type category too coarse for reliable probability estimates.

### Slice: constructor tier

| Constructor tier | Rows | Actual Top 10 rate | Mean predicted probability | Slice Brier | Mean absolute error |
|---|---:|---:|---:|---:|---:|
| `midfield` | 407 | 0.619 | 0.625 | 0.159 | 0.336 |
| `backmarker` | 312 | 0.189 | 0.249 | 0.132 | 0.305 |
| `front` | 170 | 0.876 | 0.814 | 0.105 | 0.236 |

Failure hypothesis: the largest `is_top10` error is for `midfield` constructors. This is plausible because midfield teams are exactly where strategy, traffic, and small pace differences most often decide whether a driver reaches the points. The model's average probability is close to the actual rate, but the high absolute error suggests it may be wrong on individual midfield cases even if the slice average looks calibrated.

## Target: `is_top5`

### Slice: strategy type

| Strategy type | Rows | Actual Top 5 rate | Mean predicted probability | Slice Brier | Mean absolute error |
|---|---:|---:|---:|---:|---:|
| `three_plus_stop` | 153 | 0.196 | 0.225 | 0.103 | 0.218 |
| `one_stop` | 353 | 0.283 | 0.314 | 0.097 | 0.224 |
| `two_stop` | 368 | 0.272 | 0.281 | 0.083 | 0.203 |
| `no_stop` | 15 | 0.000 | 0.088 | 0.012 | 0.088 |

Failure hypothesis: `three_plus_stop` remains the highest-Brier strategy slice for `is_top5`, while `one_stop` has the highest mean absolute error. This suggests the model struggles to distinguish planned upside strategies from strategies caused by race disruption, especially when predicting stronger finishes rather than just points finishes.

### Slice: circuit type

| Circuit type | Rows | Actual Top 5 rate | Mean predicted probability | Slice Brier | Mean absolute error |
|---|---:|---:|---:|---:|---:|
| `street` | 192 | 0.260 | 0.283 | 0.099 | 0.224 |
| `permanent` | 579 | 0.259 | 0.280 | 0.093 | 0.213 |
| `semi-street` | 118 | 0.254 | 0.285 | 0.065 | 0.186 |

Failure hypothesis: for `is_top5`, street circuits are the weakest circuit-type slice. A likely reason is that track position, safety-car timing, and overtaking difficulty matter more for Top 5 upside on street circuits, but the model only sees coarse circuit type and strategy categories.

### Slice: constructor tier

| Constructor tier | Rows | Actual Top 5 rate | Mean predicted probability | Slice Brier | Mean absolute error |
|---|---:|---:|---:|---:|---:|
| `front` | 170 | 0.676 | 0.646 | 0.181 | 0.347 |
| `midfield` | 407 | 0.278 | 0.287 | 0.114 | 0.257 |
| `backmarker` | 312 | 0.006 | 0.075 | 0.011 | 0.080 |

Failure hypothesis: the `front` constructor tier is the highest-error slice for `is_top5`. This is different from `is_top10`, where front teams were the easiest slice. The difference makes sense: front cars almost always have high Top 10 probability, but Top 5 depends more on exact race execution, teammate competition, tyre timing, and whether the strategy converts pace into a high finish.

## Cross-target conclusion

The two targets fail in different places. For `is_top10`, the main concern is midfield and three-plus-stop reliability. For `is_top5`, the main concern shifts toward front constructors and street circuits. This supports the Hito 2 requirement: `is_top5` adds decision-value information that `is_top10` alone hides.

For the strategy advisor, the practical consequence is that a recommendation should not rely only on the overall model score. If the proposed scenario involves a midfield constructor, a three-plus-stop strategy, or a Top 5 objective for a front team, the recommendation should include a reliability warning.
