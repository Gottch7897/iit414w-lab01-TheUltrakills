# Mitigations

This document lists likely failure modes for the Hito 2 models and concrete mitigations to implement before deployment. It focuses on items raised in `leakage_audit.md` (time-ordering, strategy features, confounding) and practical production concerns (missing inputs, monitoring, human-in-the-loop).

## Key failure modes

- Rare or out-of-distribution race events: long safety-car sequences, red-flag stoppages, extreme wet-weather races, or multiple simultaneous retirements that change race dynamics.
- Leakage / post-outcome features: features computed with knowledge of future events (realized stint performance, final finishing metrics) that inflate apparent performance during development but break at inference.
- Confounding from strategy choice: strategy encodes information about car/driver/conditions (e.g., faster cars choose different strategies), leading to biased counterfactual recommendations.
- Missing, delayed, or partially observed inputs: real-time telemetry, pit-stop durations, or weather status may be unavailable or stale at decision time.
- Model calibration and misinterpretation: predicted probabilities that are poorly calibrated or misused for decision thresholds.
- Data drift and distribution shift: season-to-season rule changes, regulation changes (e.g., pit stop rules), or changes in team behaviour.
- Operational issues: slow inference, mismatched feature schemas, or untested preprocessing that causes runtime errors.

## Concrete mitigations

1. Enforce strict feature provenance and time-ordering

	- Document the source and timestamp for every engineered feature in the notebooks (add a `feature_provenance` table or metadata cell).
	- Only allow features available at the decision point; drop or re-compute any feature that requires future information (see `leakage_audit.md`).

2. Ablation and sensitivity testing

	- Run an ablation that removes strategy features entirely and measure performance degradation for both `is_top10` and the expansion target. Record results in the repo.
	- Run a permutation importance test and partial dependence plots to detect single-feature dominance.

3. Confounding controls

	- Fit a propensity model for strategy choice (e.g., propensity to select 1-stop). Use matching/stratification or include propensity scores as covariates when estimating counterfactuals.
	- Include driver- and constructor-level controls (tier, recent pace proxies, qualifying performance) and validate coefficient stability across strata.

4. Robust validation protocols

	- Locked temporal split: train 2019–2021, calibration 2022, test 2023–2024 (already implemented in `hito2_modeling.ipynb`).
	- Additional holdouts: leave-one-race, leave-one-constructor, and season-holdout experiments to estimate generalization.
	- Evaluate calibration on calibration set and re-check on test set; use isotonic or Platt scaling as needed.

5. Pre-deployment runtime checks

	- Fail-safe for missing inputs: when features are missing, apply a validated fallback imputation or abstain and surface uncertainty to the user.
	- Schema validation: run feature-schema checks at inference startup and on every data batch.

6. Monitoring and drift detection

	- Track input feature distributions (per feature) and key output metrics (predicted probabilities, calibration error) over time.
	- Alert on covariate shift or sudden drops in calibration/AUC and create an automated pipeline for re-training with recent seasons if necessary.

7. Human-in-the-loop and explainability

	- Provide per-prediction explanations (SHAP or feature-attribution summaries) and show the top 3 drivers of a recommendation.
	- Require a human review step for high-risk counterfactual recommendations (e.g., strategy changes that materially increase variance of outcomes).

8. Edge-case handling and fallback policies

	- Define explicit fallback actions when model confidence is low (e.g., stick with the default team strategy or consult a race engineer).
	- Simulate and stress-test the model on synthetic extreme scenarios (multi-SC, multiple DNFs, late heavy rain).

9. Documentation and runbook

	- Publish a short runbook in `Capstone/hito2/` explaining: intended use, input requirements, when NOT to use the model, and how to interpret probabilities.
	- Add a `leakage_validation.ipynb` that runs the checklist tests from `leakage_audit.md` and stores the outputs/artifacts.

10. Post-deployment governance

	- Schedule periodic re-evaluations (every season or after rule changes). Maintain versioned models and keep training data snapshots.
	- Maintain a small labeled backlog of odd/risky races to retrain or further investigate model failures.

## Short list: minimum before deployment

- Complete the leakage audit and include provenance metadata for all features.
- Run and record ablation tests removing strategy features; report effect sizes for both targets.
- Implement schema validation and a fallback for missing inputs.
- Add monitoring for calibration, AUC, and key input distributions; wire alerts.
- Publish a runbook and require human sign-off for any automated counterfactual recommendation system.

