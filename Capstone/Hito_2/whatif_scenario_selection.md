# What-If Disagreement Scenario Selection

## Approved scenario

The approved Hito 2 disagreement scenario uses the Dutch Grand Prix example from `hito2_modeling.ipynb`.

Scenario context:

- Driver context: George Russell-style Mercedes context
- Race/circuit: 2024 Dutch Grand Prix, Zandvoort
- Circuit type: permanent
- Grid position: P4
- Constructor tier: midfield
- Decision rule: balance both targets

## Strategy comparison

| Strategy | `n_stops` | `strategy_type` | `compound_sequence` | Predicted `P(is_top10)` | Predicted `P(is_top5)` |
|---|---:|---|---|---:|---:|
| A | 1 | `one_stop` | `M-H` | 0.892756 | 0.788785 |
| B | 2 | `two_stop` | `M-H-S` | 0.866485 | 0.811390 |

## Disagreement

`is_top10` alone recommends Strategy A because the one-stop plan has the higher predicted Top 10 probability.

`is_top5` recommends Strategy B because the two-stop plan has the higher predicted Top 5 probability.

The difference is small but directionally meaningful:

- Strategy A improves Top 10 probability by about 2.6 percentage points.
- Strategy B improves Top 5 probability by about 2.3 percentage points.

## Recommendation style selected

Use a conditional recommendation:

- Recommend the one-stop strategy if the race objective is points security.
- Recommend the two-stop strategy if the race objective is Top 5 upside.

This is more honest than forcing a single recommendation because the two targets support different strategic objectives.
