# Demo Day Speaker Notes and Q&A Prep

## Core Narrative

The advisor helps a race strategy engineer make a pre-race strategy call after qualifying. The model compares two pit-stop scenarios while keeping the driver-race context fixed. The key finding is that the recommended strategy changes depending on whether the team wants points security (`is_top10`) or stronger upside (`is_top5`).

## One-minute Opening

Our tool is a Race Strategy Advisor for a pre-race strategy engineer. Given a fixed driver-race context, it compares two strategy scenarios and returns calibrated probabilities for two objectives: Top 10 and Top 5. In the approved Dutch GP example, the one-stop `M-H` plan gives the better Top 10 probability, but the two-stop `M-H-S` plan gives the better Top 5 probability. That is the value of the second target: it surfaces a real strategic trade-off that Top 10 alone hides.

## Disagreement Scenario Defense

Scenario context:

- George Russell-style Mercedes context.
- 2024 Dutch Grand Prix at Zandvoort.
- Permanent circuit.
- Grid P4.
- Midfield constructor tier.
- Driver prior-three average finish: 5.0.
- Constructor prior-three average finish: 5.0.
- Driver-circuit prior average: 10.5.

Scenario A changes only strategy inputs to `n_stops = 1`, `strategy_type = one_stop`, and `compound_sequence = M-H`.

Scenario B changes only strategy inputs to `n_stops = 2`, `strategy_type = two_stop`, and `compound_sequence = M-H-S`.

Operational consequence:

- Choose A if the race objective is protecting a points finish.
- Choose B if the race objective is Top 5 upside.
- Do not describe the difference as causal proof. The model estimates scenario probabilities from observational data.

## Likely Q&A

**Why not use only `is_top10`?**  
Because Top 10 hides upside. In the selected scenario, `is_top10` favors the one-stop, while `is_top5` favors the two-stop. A strategy desk needs to know that trade-off.

**Did you beat the docent baseline?**  
No. The locked Top 10 model gets Brier 0.139039 and ROC-AUC 0.881266. The docent reference is Brier 0.132 and ROC-AUC 0.892. We beat the simple target-rate baseline but not the docent floor, so the report states that honestly.

**Why use strategy columns if they are post-race observations?**  
They are not used as naturally known pre-race facts. They are user-controlled what-if inputs. If we used them as normal predictors without that scenario framing, it would be leakage.

**What is the biggest reliability risk?**  
Midfield Top 10 predictions. The selected scenario is midfield, and the midfield slice has Brier 0.158903 with 407 rows. That is why the recommendation must display slice reliability.

**Why logistic regression?**  
It is conservative, reproducible, and explainable. It may underfit nonlinear F1 interactions, which is one likely reason we did not beat the docent baseline.

**What would you improve before deployment?**  
Validate on fresh race weekends or simulator backtests, add better pre-race degradation and tyre-life estimates, and make slice reliability part of the tool interface.

## Team Defense Rule

Both teammates should be ready to defend every section. Use backups by theme only if needed:

- Modeling and metrics: explain split, calibration, Brier, ROC-AUC, and target-rate baseline.
- Domain reasoning: explain pre-race decision, target trade-off, and scenario-input boundary.
- Honesty and reproducibility: explain the docent comparison, limitations, `PROMPTS.md`, and the run command.

## Rehearsal Priority

Q&A first. Practice the five questions above until both teammates can answer without reading. Then run a timed 7-minute pass and cut details from Slide 4 before cutting the honesty sentence.
