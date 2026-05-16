# What-If Comparison — Hito 2

## Scenario

The comparison uses a fixed 2024 Dutch Grand Prix context at Zandvoort:

- Driver context: George Russell-style Mercedes context
- Circuit type: permanent
- Grid position: P4
- Constructor tier: midfield
- Decision: compare a one-stop plan against a two-stop plan

Only the strategy inputs change between scenarios.

| Strategy | `n_stops` | `strategy_type` | `compound_sequence` | Predicted `P(is_top10)` | Predicted `P(is_top5)` |
|---|---:|---|---|---:|---:|
| A | 1 | `one_stop` | `M-H` | 0.892756 | 0.788785 |
| B | 2 | `two_stop` | `M-H-S` | 0.866485 | 0.811390 |

## What `is_top10` alone would recommend

If the strategy desk only uses `is_top10`, the model recommends Strategy A, the one-stop `M-H` plan.

The reason is that Strategy A has the higher predicted Top 10 probability:

```text
0.892756 - 0.866485 = +0.026271
```

That is a Top 10 advantage of about 2.6 percentage points for the one-stop strategy.

## What the expansion target reveals

The `is_top5` target changes the recommendation. Strategy B, the two-stop `M-H-S` plan, has the higher predicted Top 5 probability:

```text
0.811390 - 0.788785 = +0.022605
```

That is a Top 5 advantage of about 2.3 percentage points for the two-stop strategy.

This is the Hito 2 disagreement: `is_top10` favors the safer one-stop plan, while `is_top5` favors the higher-upside two-stop plan.

## Recommendation

Use a conditional recommendation.

If the race objective is points security, recommend Strategy A: the one-stop `M-H` plan. It has the higher expected Top 10 probability and therefore better protects the points-finish objective.

If the race objective is Top 5 upside, recommend Strategy B: the two-stop `M-H-S` plan. It gives up about 2.6 percentage points of Top 10 probability but gains about 2.3 percentage points of Top 5 probability.

## Reliability and assumptions

This recommendation depends on several assumptions.

First, the strategy inputs are scenario values. They are not treated as naturally known post-race facts. The model is being asked a what-if question: how would the predicted outcome change if the strategy desk selected a different stop pattern and compound sequence?

Second, the relevant error-analysis slice is `constructor_tier = midfield`. For `is_top10`, midfield cars had the highest constructor-tier Brier score: 0.158903 across 407 rows. That means the Top 10 side of this recommendation should be treated with caution.

Third, the relevant circuit type is `permanent`. Permanent circuits had a Brier score of 0.135177 for `is_top10` and 0.092797 for `is_top5`, which is not the worst circuit-type slice, but still shows non-trivial probability error.

Fourth, the strategy-type slices show that one-stop and two-stop strategies are not equally reliable. For `is_top10`, one-stop had Brier 0.147379 and two-stop had Brier 0.128149. For `is_top5`, one-stop had Brier 0.096733 and two-stop had Brier 0.082512. In this test set, the two-stop slice is more reliable under both targets.

## Limitation

This comparison is not causal proof that the two-stop strategy causes a better Top 5 chance. Strategy choice is confounded with car pace, driver, traffic, degradation, and race incidents. The result should be used as strategy decision support, not as a standalone deployment recommendation.
