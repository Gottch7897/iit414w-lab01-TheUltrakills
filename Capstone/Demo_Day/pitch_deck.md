# F1 Race Strategy Advisor - Demo Day Deck

Team: TheUltrakills  
Members: Martín Gottschalk, Marcial Ibáñez  
Format: 7-minute pitch + 5-minute Q&A  
Spine selected: headline finding first

---

## Slide 1 - Headline Finding

**Conditional strategy choice depends on the target.**

In the approved Dutch GP scenario, the one-stop `M-H` plan better protects Top 10 probability, while the two-stop `M-H-S` plan improves Top 5 upside.

Speaker note: Open with the practical decision. This is not a generic prediction model; it is a pre-race strategy-support tool.

---

## Slide 2 - Decision Context

- User: race strategy engineer.
- Time window: pre-race, after qualifying, before the start.
- Decision: compare feasible pit-stop plans for the same driver-race context.
- Prediction unit: one driver in one race.

Speaker note: Make the information boundary explicit. We can use grid and prior performance, but not realized incidents or race outcomes.

---

## Slide 3 - What the Model Sees

- Pre-race context: `grid_position`, prior driver and constructor finish averages, `driver_circuit_prior_avg`, `constructor_tier`, `circuit_type`.
- Scenario inputs: `n_stops`, `strategy_type`, `compound_sequence`.
- Excluded: outcomes, DNF/status, realized weather, safety-car/VSC fields, wet laps, temperatures.

Speaker note: Strategy variables are allowed only because they are what-if controls. They would be leakage in a normal pre-race predictor.

---

## Slide 4 - Evidence Base

| Target | Model Brier | ROC-AUC | Meaning |
|---|---:|---:|---|
| `is_top10` | 0.139039 | 0.881266 | Points security |
| `is_top5` | 0.090479 | 0.934413 | Upside finish |
| Docent `is_top10` | 0.132000 | 0.892000 | Reference floor |

Speaker note: Say the honest comparison out loud: we beat the simple baseline, but we do not beat the docent Top 10 floor.

---

## Slide 5 - What-if Disagreement

Fixed context: George Russell-style Mercedes, 2024 Dutch GP, permanent circuit, grid P4, midfield constructor tier.

| Scenario | Stops | Sequence | P(Top 10) | P(Top 5) |
|---|---:|---|---:|---:|
| A | 1 | `M-H` | 0.892756 | 0.788785 |
| B | 2 | `M-H-S` | 0.866485 | 0.811390 |

Speaker note: `is_top10` favors the one-stop by 2.6 percentage points. `is_top5` favors the two-stop by 2.3 percentage points.

---

## Slide 6 - Recommendation

Use a conditional recommendation:

- If the objective is points security, prefer the one-stop `M-H`.
- If the objective is Top 5 upside, prefer the two-stop `M-H-S`.
- Always show the relevant reliability slices beside the recommendation.

Speaker note: Do not force a single answer when the two targets represent different strategic objectives.

---

## Slide 7 - Reliability Warnings

- `is_top10` is weakest for midfield constructors: Brier 0.158903 across 407 rows.
- `is_top10` is weak for `three_plus_stop`: Brier 0.157422 across 153 rows.
- `is_top5` is weakest for front constructors: Brier 0.180871 across 170 rows.

Speaker note: Our selected scenario is midfield, so the Top 10 recommendation needs a warning.

---

## Slide 8 - Honesty Sentence

We do not recommend deploying this tool unless:

- it is limited to pre-race what-if comparisons with fixed driver-race context;
- every recommendation displays target-specific slice reliability for strategy type, circuit type, and constructor tier;
- the team validates the model on a fresh race weekend or simulator backtest before operational use.

Speaker note: Close with confidence and boundaries. This is a decision-support prototype, not causal proof.
