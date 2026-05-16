# Leakage Audit — Hito 2

## Feature roles

The Hito 2 model uses a conservative feature set:

| Feature | Role | Use |
|---|---|---|
| `grid_position` | pre-race | Known after qualifying/grid formation |
| `driver_prior3_avg_finish` | pre-race historical context | Prior performance proxy |
| `constructor_prior3_avg_finish` | pre-race historical context | Team performance proxy |
| `driver_circuit_prior_avg` | pre-race historical context | Driver-circuit familiarity proxy |
| `constructor_tier` | pre-race context | Coarse team-strength category |
| `circuit_type` | pre-race context | Known circuit category |
| `n_stops` | scenario input | User-controlled what-if value |
| `strategy_type` | scenario input | User-controlled what-if value |
| `compound_sequence` | scenario input | User-controlled what-if value |

## Excluded columns

The model excludes direct outcomes:

- `finish_position`
- `points`
- `positions_gained`
- `is_top3`
- `is_top5` when modeling `is_top10`
- `is_top10` when modeling `is_top5`

The model also excludes race-incident and realized-condition columns as predictors:

- `track_status_summary`
- `safety_car_periods`
- `safety_car_laps`
- `vsc_laps`
- `weather_actual`
- `wet_laps`
- `avg_track_temp`
- `avg_air_temp`
- `dnf`
- `status`

These columns may be used only for audit slices, stress tests, or limitations. They are not treated as known pre-race inputs.

## Strategy variables

Strategy variables are post-race observations in the raw dataset, so they would be leakage in a normal pre-race prediction model. In this capstone, they are allowed only because the product is a scenario comparison tool.

The model receives `n_stops`, `strategy_type`, and `compound_sequence` as user-controlled scenario inputs. The interpretation is not “the team magically knew the observed strategy after the race.” The interpretation is “the strategy desk asks what would happen if this strategy were selected.”

This treatment holds for both targets:

- `is_top10`: probability of a points finish
- `is_top5`: probability of stronger upside

## Remaining confounding risk

The main remaining risk is not ordinary target leakage but confounding. Strategy choice is not random. It is correlated with car pace, driver quality, track position, weather, traffic, degradation, and race incidents.

For example, a two-stop strategy may look better or worse partly because stronger teams select it in specific contexts, not because the stop count itself caused the outcome. Therefore, all what-if outputs should be interpreted as model-based decision support rather than causal estimates.
