# Leakage Audit

## Executive summary

This document records the leakage and confounding checks for Hito 2. It uses only artifacts present in `Capstone/hito2` (notebooks, analysis notes, and README) and the shared data pointers from `README.md`. Where the folder does not document a check, this audit records a finding and a recommended action.

## Checklist results (status + notes)

- **Data sources identified:** Present — `f1_strategy_lap_level.csv` and `f1_strategy_race_level.csv` (referenced in `README.md`).
- **Time-ordering / feature availability at decision point:** NOT documented in `hito2` files. ACTION: explicitly list which features are available at the prediction/decision time in the modeling notebooks and freeze that schema.
- **Targets & dual-target handling:** Not documented in prose; notebooks include a dual-target scaffold file (`hito2_dual_target_scaffold.ipynb`). ACTION: add a short note in the notebooks stating which features are permitted for each target and why.
- **Strategy features treated as scenario inputs:** Not yet validated in folder docs. Finding: the repo prompts require this check; it is not shown as completed. ACTION: verify that strategy features are encoded only from pre-decision information (planned pit laps or intended stint lengths), not as post-outcome aggregates.
- **Derived features / aggregates that may leak:** NOT audited in `hito2` docs. ACTION: flag and review any feature that aggregates post-decision race outcomes (e.g., realized stint times, final-race aggregates) and remove or re-compute them as pre-decision summaries.
- **Confounding acknowledged:** Required in prompt; present as a limitation to address but no formal adjustment is shown. ACTION: implement confounding controls (see mitigations below).
- **Validation tests performed (ablation, temporal split, holdout by race/team):** Not documented. ACTION: run temporal validation and race/team holdouts; run ablation removing strategy features to quantify effect.
- **What-if / counterfactual checks:** `whatif_comparison.md` documents the intended analysis. This is an appropriate validation route — ensure the example uses only pre-decision inputs.

## Confounding (strategy choice correlates with pace/driver/weather)

Finding: the hito2 notes explicitly require addressing this confounding but do not show completed controls.

Recommended mitigations (prioritized):

- Enforce time-ordering: only include features available at the moment the strategy decision is made.
- Include control covariates: constructor/driver tier, recent lap-speed proxies, qualifying performance, and observed weather at decision time.
- Propensity stratification / matching: estimate propensity to choose a strategy (e.g., 1-stop vs 2-stop) and compare outcomes within propensity strata or include propensity as a model input.
- Use causal graph thinking: document assumed causal relationships so feature inclusion/exclusion is explicit.
- Sensitivity analysis: evaluate how model recommendations change when controlling for driver/constructor and when removing strategy features.
- Holdout experiments: validate on seasons/races not used in training and on teams/drivers with different pace profiles.

## Specific check: strategy features as scenario inputs

Status: not validated in repository docs. Guidance:

- If strategy features are recorded as the team's chosen plan (a scenario under the team's control) and are encoded using only pre-decision information (e.g., planned pit lap numbers or intended stint lengths), then treating them as scenario inputs is appropriate for counterfactual reasoning.
- If strategy features were engineered using post-decision information (e.g., realized stint performance, final finishing position), they leak and must be removed or re-computed.

Decision for Hito 2 (required action):

- Annotate every strategy feature in the modeling notebooks with its source and timestamp relative to the decision point.
- Re-run a brief ablation that trains the expansion target and `is_top10` with and without strategy features; record changes in calibration and ranking. If the model's predictive power collapses without strategy features, report this as part of mitigation and quantify the external information the strategy encodes.

## Tests to run (minimum set)

- Temporal split (train on earlier seasons, test on later seasons).
- Race-level and constructor/driver-level holdouts.
- Ablation: drop strategy features; measure drop in AUC/Brier/target metrics for both targets.
- Permutation importance and partial dependence to detect unusually strong single-feature influence.
- Counterfactual what-if runs constrained to pre-decision inputs (use `whatif_comparison.md` example flow).

## Deployment notes / unresolved items

- `mitigations.md` lists generic pre-deployment steps; extend that list to include: (1) formal leakage validation notebook with the above tests, (2) feature provenance documentation, (3) drift+leakage monitoring for production data.
- Until the explicit time-ordering and ablation tests are in the repo, the statement "strategy features can be used as scenario inputs for both targets" is UNVERIFIED.

## Conclusion

- Current state (based only on `Capstone/hito2`): important checks and documentation are requested by the prompts and supporting files but not yet shown as completed. The folder contains the right scaffolding (`hito2_dual_target_scaffold.ipynb`, `whatif_comparison.md`, `mitigations.md`) to finish the audit.
- Next immediate actions: (1) annotate strategy feature provenance in the modeling notebooks, (2) run the ablation and temporal/holdout tests, (3) add a short leakage-validation notebook cell that reproduces the checklist tests and records results.


