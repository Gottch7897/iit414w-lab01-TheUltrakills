# Mitigations — Hito 2

## Risk 1: Midfield Top 10 predictions are noisy

Observed failure slice:

- Target: `is_top10`
- Slice: `constructor_tier = midfield`
- Rows: 407
- Slice Brier score: 0.158903
- Mean absolute probability error: 0.336403

Consequence: the selected what-if scenario uses a midfield constructor context, so the Top 10 side of the recommendation is less reliable than the overall story may suggest.

Mitigation for final report: include a reliability warning whenever the recommendation uses a midfield constructor context. Report the midfield slice metric beside the scenario result instead of only reporting the overall model metric.

## Risk 2: Three-plus-stop strategies are difficult to interpret

Observed failure slice:

- Target: `is_top10`
- Slice: `strategy_type = three_plus_stop`
- Rows: 153
- Slice Brier score: 0.157422
- Mean absolute probability error: 0.326359

Consequence: three-plus-stop strategies may reflect disruption, damage, degradation, or recovery attempts. Treating them as ordinary planned strategy options can overstate the model's ability to compare strategy quality.

Mitigation for final report: separate planned one-stop/two-stop comparisons from disruption-heavy three-plus-stop cases. If three-plus-stop scenarios are shown, label them as high-risk and avoid using them as the main recommendation.

## Risk 3: Front-team Top 5 predictions are less reliable

Observed failure slice:

- Target: `is_top5`
- Slice: `constructor_tier = front`
- Rows: 170
- Slice Brier score: 0.180871
- Mean absolute probability error: 0.346881

Consequence: `is_top10` is easy for front teams because they usually finish in the points, but `is_top5` depends on finer differences in execution, tyre timing, teammate pace, and race events.

Mitigation for final report: when the selected decision context involves front teams and `is_top5`, avoid claiming precise upside probabilities. Present the Top 5 result as directional unless calibration improves for this slice.

## Risk 4: Street-circuit Top 5 upside is hard to model

Observed failure slice:

- Target: `is_top5`
- Slice: `circuit_type = street`
- Rows: 192
- Slice Brier score: 0.099396
- Mean absolute probability error: 0.224219

Consequence: street circuits are sensitive to track position, safety-car timing, and overtaking difficulty. The current model uses only coarse circuit type and does not include detailed race-control timing as a pre-race input.

Mitigation for final report: if a final scenario uses a street circuit, include a stress-test discussion rather than a single-point recommendation. Do not silently add safety-car or weather outcome columns as predictors.

## Risk 5: Strategy choice is confounded with car pace and race context

Observed evidence:

- The model's failure slices differ across `strategy_type` and `constructor_tier`.
- `is_top10` is weakest for midfield constructors, while `is_top5` is weakest for front constructors.

Consequence: strategy effects cannot be interpreted causally. A strategy may appear better because of who used it and under what race conditions.

Mitigation for final report: state recommendations as conditional model outputs, not causal claims. For each what-if comparison, show the fixed driver-race context and explicitly list which features changed between strategies.
