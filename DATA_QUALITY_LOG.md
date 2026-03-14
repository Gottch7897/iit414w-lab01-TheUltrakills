# Data Quality Log — Lab 1 - [TheUltrakills]

## Issue 1: GridPosition — Missingness Mechanism
- **What:** Missing `GridPosition` values can appear in raw race-result feeds for context-dependent reasons (for example, invalid/absent starting assignment).
- **Classification:** Likely MNAR
- **Impact:** Baseline logic and derived features depend on grid position, so missingness can bias analysis if untreated.
- **Decision:** Coerce to numeric, then drop rows with missing `GridPosition` in the modeling table.
- **Justification:** This preserves clean, comparable records for Top-10 baseline analysis and avoids introducing speculative imputation for a key predictor.

## Issue 2: Position — Missingness Mechanism
- **What:** Missing `Position` values are outcome-related in race data (retirements/disqualifications/reporting gaps).
- **Classification:** Likely MNAR
- **Impact:** `Top10` label creation and performance checks are invalid when finish position is unknown.
- **Decision:** Coerce to numeric, then drop rows with missing `Position` for evaluated analyses.
- **Justification:** The target variable requires a valid finishing position; dropping invalid rows prevents corrupted labels.

## Issue 3: Status — Conditional Missingness / Completeness Risk
- **What:** `Status` availability may vary by event/source completeness.
- **Classification:** Likely MAR
- **Impact:** DNF derivation can be distorted when status text is absent or inconsistent.
- **Decision:** Keep the column, derive `DNF` with null-safe logic (`str.contains(..., na=False)`), and treat DNF-sensitive metrics as part of robustness checks.
- **Justification:** This keeps useful reliability information while preventing null values from breaking transformations.

## Issue 4: Numeric Type Consistency — Type Integrity
- **What:** Raw fields such as `grid` and `position` are ingested as text/object in API responses.
- **Classification:** Type quality issue
- **Impact:** Incorrect dtypes can break comparisons, arithmetic, and statistical summaries.
- **Decision:** Standardize via `pd.to_numeric(..., errors='coerce')` before feature engineering.
- **Justification:** Numeric coercion is required for reliable computations (`Top10`, `PositionsGained`, correlations, and outlier checks).

## Issue 5: Outliers in Race Performance Features — Distribution Tail Risk
- **What:** Features like `PositionsGained` and race points can contain extreme values.
- **Classification:** Outlier (IQR rule)
- **Impact:** Tail values can dominate mean-based summaries and overstate/understate correlations.
- **Decision:** Keep outliers for EDA visibility; log IQR-based outlier rates and plan robust handling if modeling sensitivity appears.
- **Justification:** Extreme race outcomes are often real events, not data-entry errors, so immediate removal is not always appropriate.

## Issue 6: Temporal Availability — Leakage Control
- **What:** Some columns are only known after the race (`Position`, `Points`, `Top10`, `DNF`, `PositionsGained`).
- **Classification:** Temporal leakage risk
- **Impact:** Using post-race fields in prediction would inflate performance unrealistically.
- **Decision:** Restrict predictive feature set to pre-race available fields (`GridPosition`, `Year`, `Round`, historical reliability/constructor proxies).
- **Justification:** Ensures evaluation matches real forecasting conditions and supports valid temporal train/validation/test use.