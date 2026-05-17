"""Generate the Final Report evidence package for the F1 Race Strategy Advisor.

This script rebuilds the locked Hito 2 evidence from the race-level dataset:
the 2019-2021 / 2022 / 2023-2024 temporal split, logistic-regression models
for is_top10 and is_top5, sigmoid calibration on 2022, metric tables,
calibration plots, error slices, the approved what-if comparison, a Markdown
report.
"""

from pathlib import Path
import os
import shutil
import textwrap

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from sklearn.calibration import calibration_curve
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


RANDOM_SEED = 414
TEAM_NAME = "TheUltrakills"
TEAM_MEMBERS = "Martín Gottschalk, Marcial Ibáñez"
COURSE = "IIT414W - Artificial Intelligence Workshop - 2026-1T"
DATE = "May 17, 2026"
REPO_URL = "https://github.com/Gottch7897/iit414w-lab01-TheUltrakills.git"
COMMIT = "final-v1"
DATA_PATH = Path("test/f1_strategy_race_level.csv")
OUT_DIR = Path("Capstone/Final_Report")
FIG_DIR = OUT_DIR / "figures"
TABLE_DIR = OUT_DIR / "tables"
MD_NAME = "IIT414W_FinalReport_TheUltrakills.md"


NUMERIC_FEATURES = [
    "grid_position",
    "driver_prior3_avg_finish",
    "constructor_prior3_avg_finish",
    "driver_circuit_prior_avg",
    "n_stops",
]
CATEGORICAL_FEATURES = [
    "constructor_tier",
    "circuit_type",
    "strategy_type",
    "compound_sequence",
]
MODEL_FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGETS = ["is_top10", "is_top5"]


WHATIF_SCENARIOS = pd.DataFrame(
    [
        {
            "scenario": "A_one_stop",
            "grid_position": 4.0,
            "driver_prior3_avg_finish": 5.0,
            "constructor_prior3_avg_finish": 5.0,
            "driver_circuit_prior_avg": 10.5,
            "constructor_tier": "midfield",
            "circuit_type": "permanent",
            "n_stops": 1,
            "strategy_type": "one_stop",
            "compound_sequence": "M-H",
        },
        {
            "scenario": "B_two_stop",
            "grid_position": 4.0,
            "driver_prior3_avg_finish": 5.0,
            "constructor_prior3_avg_finish": 5.0,
            "driver_circuit_prior_avg": 10.5,
            "constructor_tier": "midfield",
            "circuit_type": "permanent",
            "n_stops": 2,
            "strategy_type": "two_stop",
            "compound_sequence": "M-H-S",
        },
    ]
)


def ensure_dirs():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)


def make_pipeline():
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, NUMERIC_FEATURES),
            ("categorical", categorical_transformer, CATEGORICAL_FEATURES),
        ]
    )
    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(random_state=RANDOM_SEED, max_iter=1000)),
        ]
    )


def fit_locked_models(df):
    train_df = df[df["season"].between(2019, 2021)].copy()
    calibration_df = df[df["season"].eq(2022)].copy()
    test_df = df[df["season"].between(2023, 2024)].copy()

    split_summary = pd.DataFrame(
        {
            "split": ["train", "calibration", "test"],
            "seasons": ["2019-2021", "2022", "2023-2024"],
            "rows": [len(train_df), len(calibration_df), len(test_df)],
        }
    )

    trained = {}
    calibration_rows = []
    prediction_df = test_df.copy()
    comparison_rows = []
    whatif = WHATIF_SCENARIOS.copy()

    for target in TARGETS:
        pipeline = make_pipeline()
        pipeline.fit(train_df[MODEL_FEATURES], train_df[target])

        calibration_raw = pipeline.predict_proba(calibration_df[MODEL_FEATURES])[:, 1]
        calibrator = LogisticRegression(random_state=RANDOM_SEED)
        calibrator.fit(calibration_raw.reshape(-1, 1), calibration_df[target])

        train_raw = pipeline.predict_proba(train_df[MODEL_FEATURES])[:, 1]
        train_calibrated = calibrator.predict_proba(train_raw.reshape(-1, 1))[:, 1]
        calibration_calibrated = calibrator.predict_proba(
            calibration_raw.reshape(-1, 1)
        )[:, 1]

        test_raw = pipeline.predict_proba(test_df[MODEL_FEATURES])[:, 1]
        test_calibrated = calibrator.predict_proba(test_raw.reshape(-1, 1))[:, 1]
        prediction_df[f"predicted_{target}_probability"] = test_calibrated

        whatif_raw = pipeline.predict_proba(whatif[MODEL_FEATURES])[:, 1]
        whatif[f"predicted_{target}_probability"] = calibrator.predict_proba(
            whatif_raw.reshape(-1, 1)
        )[:, 1]

        baseline_probability = train_df[target].mean()
        baseline_proba = np.repeat(baseline_probability, len(test_df))
        comparison_rows.append(
            {
                "target": target,
                "approach": "target_rate_baseline",
                "brier_score": brier_score_loss(test_df[target], baseline_proba),
                "log_loss": log_loss(test_df[target], baseline_proba),
                "roc_auc": 0.5,
            }
        )
        comparison_rows.append(
            {
                "target": target,
                "approach": "logistic_regression_calibrated",
                "brier_score": brier_score_loss(test_df[target], test_calibrated),
                "log_loss": log_loss(test_df[target], test_calibrated),
                "roc_auc": roc_auc_score(test_df[target], test_calibrated),
            }
        )

        calibration_rows.append(
            {
                "target": target,
                "train_actual_rate": train_df[target].mean(),
                "train_mean_calibrated_probability": train_calibrated.mean(),
                "calibration_actual_rate": calibration_df[target].mean(),
                "calibration_mean_calibrated_probability": calibration_calibrated.mean(),
            }
        )
        trained[target] = {"pipeline": pipeline, "calibrator": calibrator}

    comparison = pd.DataFrame(comparison_rows)
    calibration_summary = pd.DataFrame(calibration_rows)
    return {
        "train": train_df,
        "calibration": calibration_df,
        "test": test_df,
        "split_summary": split_summary,
        "models": trained,
        "predictions": prediction_df,
        "comparison": comparison,
        "calibration_summary": calibration_summary,
        "whatif": whatif,
    }


def build_error_slices(prediction_df):
    rows = []
    for target in TARGETS:
        pred_col = f"predicted_{target}_probability"
        work = prediction_df.copy()
        work["squared_probability_error"] = (work[target] - work[pred_col]) ** 2
        work["absolute_probability_error"] = (work[target] - work[pred_col]).abs()
        for slice_column in ["strategy_type", "circuit_type", "constructor_tier"]:
            table = (
                work.groupby(slice_column, dropna=False)
                .agg(
                    rows=(target, "size"),
                    actual_rate=(target, "mean"),
                    mean_predicted_probability=(pred_col, "mean"),
                    slice_brier_score=("squared_probability_error", "mean"),
                    mean_absolute_probability_error=(
                        "absolute_probability_error",
                        "mean",
                    ),
                )
                .reset_index()
                .rename(columns={slice_column: "slice_value"})
            )
            table["target"] = target
            table["slice_column"] = slice_column
            rows.append(table)
    return pd.concat(rows, ignore_index=True)


def write_tables(evidence):
    evidence["split_summary"].to_csv(TABLE_DIR / "split_summary.csv", index=False)
    evidence["comparison"].to_csv(TABLE_DIR / "model_comparison.csv", index=False)
    evidence["calibration_summary"].to_csv(
        TABLE_DIR / "calibration_summary.csv", index=False
    )
    evidence["whatif"].to_csv(TABLE_DIR / "whatif_comparison.csv", index=False)
    error_slices = build_error_slices(evidence["predictions"])
    error_slices.to_csv(TABLE_DIR / "error_slices.csv", index=False)
    return error_slices


def save_figures(evidence, error_slices):
    comparison = evidence["comparison"].copy()
    model_rows = comparison[comparison["approach"] == "logistic_regression_calibrated"]

    fig, ax = plt.subplots(figsize=(7, 4.2))
    x = np.arange(len(model_rows))
    ax.bar(x - 0.18, model_rows["brier_score"], width=0.36, label="Brier")
    ax.bar(x + 0.18, model_rows["log_loss"], width=0.36, label="Log loss")
    ax.axhline(0.132, color="black", linestyle="--", linewidth=1, label="Docent Brier")
    ax.set_xticks(x, model_rows["target"])
    ax.set_ylabel("Lower is better")
    ax.set_title("Locked Test Metrics, 2023-2024")
    ax.legend()
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "metric_summary.png", dpi=180)
    plt.close(fig)

    for target in TARGETS:
        pred_col = f"predicted_{target}_probability"
        frac_pos, mean_pred = calibration_curve(
            evidence["test"][target],
            evidence["predictions"][pred_col],
            n_bins=5,
            strategy="quantile",
        )
        fig, ax = plt.subplots(figsize=(5.2, 4.4))
        ax.plot(mean_pred, frac_pos, marker="o", label=target)
        ax.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Perfect")
        ax.set_xlabel(f"Mean predicted P({target})")
        ax.set_ylabel("Observed rate")
        ax.set_title(f"Calibration Curve: {target}")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.grid(alpha=0.25)
        ax.legend()
        fig.tight_layout()
        fig.savefig(FIG_DIR / f"calibration_{target}.png", dpi=180)
        plt.close(fig)

    whatif = evidence["whatif"]
    fig, ax = plt.subplots(figsize=(7, 4.2))
    x = np.arange(len(whatif))
    width = 0.34
    ax.bar(
        x - width / 2,
        whatif["predicted_is_top10_probability"],
        width,
        label="P(is_top10)",
    )
    ax.bar(
        x + width / 2,
        whatif["predicted_is_top5_probability"],
        width,
        label="P(is_top5)",
    )
    ax.set_xticks(x, whatif["scenario"])
    ax.set_ylim(0.75, 0.92)
    ax.set_ylabel("Predicted probability")
    ax.set_title("What-if Strategy Disagreement")
    ax.legend()
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "whatif_disagreement.png", dpi=180)
    plt.close(fig)

    constructor = error_slices[error_slices["slice_column"] == "constructor_tier"]
    pivot = constructor.pivot(
        index="slice_value", columns="target", values="slice_brier_score"
    ).loc[["front", "midfield", "backmarker"]]
    fig, ax = plt.subplots(figsize=(7, 4.2))
    pivot.plot(kind="bar", ax=ax)
    ax.set_xlabel("Constructor tier")
    ax.set_ylabel("Slice Brier score")
    ax.set_title("Constructor-tier Reliability by Target")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "constructor_tier_brier.png", dpi=180)
    plt.close(fig)


def format_float(value):
    return f"{value:.3f}"


def markdown_report(evidence, error_slices):
    comparison = evidence["comparison"]
    whatif = evidence["whatif"]
    top10_model = comparison.query(
        "target == 'is_top10' and approach == 'logistic_regression_calibrated'"
    ).iloc[0]
    top5_model = comparison.query(
        "target == 'is_top5' and approach == 'logistic_regression_calibrated'"
    ).iloc[0]
    top10_delta = top10_model["brier_score"] - 0.132
    top10_a = whatif.loc[whatif["scenario"] == "A_one_stop"].iloc[0]
    top10_b = whatif.loc[whatif["scenario"] == "B_two_stop"].iloc[0]
    top10_gain = (
        top10_a["predicted_is_top10_probability"]
        - top10_b["predicted_is_top10_probability"]
    )
    top5_gain = (
        top10_b["predicted_is_top5_probability"]
        - top10_a["predicted_is_top5_probability"]
    )

    return f"""# F1 Race Strategy Advisor: Conditional Strategy Choice Depends on the Target

Team: {TEAM_MEMBERS}  
Course: {COURSE}  
Date: {DATE}  
Repo: {REPO_URL}  
Commit: {COMMIT}

## 1. Executive Summary

This report turns the Hito 1 and Hito 2 work into a strategy-support recommendation for a race strategy engineer making a pre-race call after qualifying. The advisor compares a fixed driver-race context under alternative pit-stop plans and reports calibrated probabilities for two targets: `is_top10` for points security and `is_top5` for stronger upside. In the approved Dutch Grand Prix scenario, the one-stop `M-H` plan has the higher Top 10 probability by {top10_gain:.1%}, while the two-stop `M-H-S` plan has the higher Top 5 probability by {top5_gain:.1%}. The recommendation is conditional: choose the one-stop when protecting points matters most, and choose the two-stop when the strategic objective is Top 5 upside.

The model improves strongly over target-rate baselines for both targets. It nearly reaches the docent Top 10 reference but does not beat it: the locked Top 10 Brier score is {top10_model['brier_score']:.6f}, compared with the docent Brier of 0.132. This is close, but the report does not treat it as a win. The tool is useful as decision support, not causal proof, because strategy choice is observational and confounded with car pace, driver quality, traffic, weather, and race incidents.

## 2. Problem Framing

The supported decision is a pre-race strategy call before the start, after qualifying information is available. The decision-maker is a race strategy engineer who needs to compare whether a selected driver-race context should prioritize a one-stop or two-stop plan. The time window matters: the model can use grid position, prior driver and constructor performance, circuit type, and constructor tier, but it must not use race outcomes or incident summaries as if they were known before the race.

The prediction unit is one driver in one race. The primary target is `is_top10`, matching the locked capstone requirement and the docent baseline comparison. The expansion target is `is_top5`, chosen because it preserves the probabilistic framing while exposing a higher-upside decision that `is_top10` can hide. In F1 terms, this separates points security from the chance of a stronger finish.

Strategy fields such as `n_stops`, `strategy_type`, and `compound_sequence` are scenario inputs. They are post-race observations in the raw data, so using them as normal pre-race predictors would be leakage. In this advisor, they are user-controlled values for a what-if question: "what if the strategy desk selected this plan?"

Key assumptions are: the strategy desk is comparing feasible plans, the driver and circuit context remains fixed within a scenario comparison, and the output is a model-based probability estimate rather than a causal estimate of the strategy effect. The main consequence is that recommendations must be conditional and paired with reliability warnings.

## 3. Data and Validation

The race-level dataset has 2,447 driver-race rows from 2019-2024. The locked split is temporal: train on 2019-2021, calibrate on 2022, and evaluate once on 2023-2024. The split prevents random leakage across seasons and matches the reference comparison.

The feature audit separates pre-race context from scenario inputs, audit-only columns, and outcomes. The model uses `grid_position`, `driver_prior3_avg_finish`, `constructor_prior3_avg_finish`, `driver_circuit_prior_avg`, `constructor_tier`, and `circuit_type` as known context. It uses `n_stops`, `strategy_type`, and `compound_sequence` only as scenario controls. It excludes outcomes such as `finish_position`, `points`, `positions_gained`, `is_top3`, `is_top5`, and `is_top10`, and excludes realized race-condition columns such as safety-car, VSC, weather, wet-lap, DNF, and status fields.

Known dataset limitations are carried into the interpretation. Coverage starts in 2019, `qualifying_position` is only a grid-position stand-in, `qualifying_time_s` is empty, safety-car information is coarse, and strategy choice is not independent of pace and race context.

## 4. Modeling Approach

The report uses separate logistic-regression models per target. This follows the selected narrative: each target gets its own calibrated probability model while preserving a common feature boundary and temporal split. The model family is intentionally conservative. It is easier to explain to an F1 strategy audience than a larger learner, and it reduces the risk of hiding leakage behind model complexity.

The baseline for each target is the training target rate. The Hito 1 grid-only heuristic is retained as background evidence, but the final two-target comparison uses the Hito 2 target-rate baseline so both targets are evaluated consistently. For the main models, numeric features are median-imputed and standardized; categorical features are mode-imputed and one-hot encoded; logistic regression uses `RANDOM_SEED = 414`.

Calibration uses sigmoid/Platt calibration on the 2022 block. This was selected because the calibration season is small, so a smooth calibrator is safer than isotonic calibration. Calibration is not used for model selection, and the 2023-2024 test set is only used for final locked evaluation.

## 5. Results and Honest Comparison

| Target | Approach | Brier | Log loss | ROC-AUC |
|---|---|---:|---:|---:|
| `is_top10` | target-rate baseline | {comparison.iloc[0]['brier_score']:.6f} | {comparison.iloc[0]['log_loss']:.6f} | {comparison.iloc[0]['roc_auc']:.3f} |
| `is_top10` | calibrated logistic regression | {top10_model['brier_score']:.6f} | {top10_model['log_loss']:.6f} | {top10_model['roc_auc']:.6f} |
| `is_top5` | target-rate baseline | {comparison.iloc[2]['brier_score']:.6f} | {comparison.iloc[2]['log_loss']:.6f} | {comparison.iloc[2]['roc_auc']:.3f} |
| `is_top5` | calibrated logistic regression | {top5_model['brier_score']:.6f} | {top5_model['log_loss']:.6f} | {top5_model['roc_auc']:.6f} |
| `is_top10` | docent calibrated reference | 0.132000 | not provided | 0.892000 |

The Top 10 model is close to the docent reference but below it. The Brier gap is {top10_delta:+.6f}, and the ROC-AUC gap is {top10_model['roc_auc'] - 0.892:+.6f}. The honest comparison is therefore: the model beats the simple baseline by a large margin but does not beat the docent floor.

The Top 5 model adds useful signal. Its Brier score is {top5_model['brier_score']:.6f} and ROC-AUC is {top5_model['roc_auc']:.6f}, showing that the expansion target is not just a formal requirement. It supports a different strategic objective: whether an aggressive plan improves higher-finish upside.

Calibration plots are regenerated as `figures/calibration_is_top10.png` and `figures/calibration_is_top5.png`. They should be read as probability-quality evidence, not as proof that every slice is reliable.

## 6. Error Analysis and What-If

The required slices are strategy type, circuit type, and constructor tier. The clearest failure modes are:

1. `is_top10` is weakest for midfield constructors: 407 rows, Brier 0.158903, mean absolute probability error 0.336403. This matters because midfield teams are where strategy, traffic, and small pace differences often decide points.
2. `is_top10` is also weak for `three_plus_stop` strategies: 153 rows, Brier 0.157422. These strategies often reflect disruption, damage, or recovery attempts rather than clean pre-race plans.
3. `is_top5` is weakest for front constructors: 170 rows, Brier 0.180871. Front teams almost always have high Top 10 probability, but Top 5 depends on exact execution, teammate competition, tyre timing, and race events.

The approved what-if scenario fixes a George Russell-style Mercedes context at the 2024 Dutch Grand Prix: permanent circuit, grid P4, midfield constructor tier, driver prior-three average finish of 5.0, constructor prior-three average finish of 5.0, and driver-circuit prior average of 10.5. Only the strategy inputs change.

| Scenario | Stops | Type | Compound sequence | P(is_top10) | P(is_top5) |
|---|---:|---|---|---:|---:|
| A | 1 | `one_stop` | `M-H` | {top10_a['predicted_is_top10_probability']:.6f} | {top10_a['predicted_is_top5_probability']:.6f} |
| B | 2 | `two_stop` | `M-H-S` | {top10_b['predicted_is_top10_probability']:.6f} | {top10_b['predicted_is_top5_probability']:.6f} |

`is_top10` alone favors the one-stop by {top10_gain:.1%}. `is_top5` favors the two-stop by {top5_gain:.1%}. The operational consequence is that the strategy desk should not ask only "which plan protects points?" If the race objective is Top 5 upside, the model changes the preferred plan.

## 7. Limitations and Risks

The main limitation is scenario dependence under regime shift and observational confounding. The dataset covers only 2019-2024, and race strategies are not randomly assigned. A two-stop plan may look better partly because of the cars, drivers, degradation regimes, or incidents associated with the historical cases where it was used.

Single-team deployment is also risky. The selected what-if context uses a midfield constructor, and midfield Top 10 predictions are the weakest constructor-tier slice. The model should therefore report a reliability warning beside the recommendation rather than hiding the slice risk.

We do not recommend deploying this tool unless (1) the strategy desk limits it to pre-race what-if comparisons with explicitly fixed driver-race context, (2) every recommendation displays target-specific slice reliability for strategy type, circuit type, and constructor tier, and (3) the team validates the model on a fresh race weekend or simulator backtest before treating the probabilities as operational guidance.

## 8. Reproducibility Note and AI Reflection

The repository includes the Hito 1 and Hito 2 source artifacts, this report generator, regenerated tables, figures, and the final PDF. A third party should run `venv/bin/python Capstone/Final_Report/generate_final_report.py` from the repository root after installing the course environment. All model `random_state` arguments use `RANDOM_SEED = 414`.

AI assistance was used to structure the final report, convert Hito evidence into executive-language prose, draft captions and Q&A prompts, and critique the honesty sentence. The outputs were checked against the locked Hito files and regenerated tables. Suggestions that implied causal strategy effects or claimed the Top 10 model beat the docent baseline were rejected because they overstated the evidence.

## 9. References

IIT414W course capstone brief and Canvas rubrics. (2026). F1 Race Strategy Advisor.

Course dataset: `f1_strategy_race_level.csv`, seasons 2019-2024.

FastF1 project documentation and historical Formula 1 timing data sources.

Jolpica F1 API documentation and historical race metadata sources.

scikit-learn developers. (2026). Logistic regression, calibration, and model evaluation documentation.
"""


def add_wrapped_text(fig, text, x=0.08, y=0.90, width=92, size=11, line_gap=0.035):
    current_y = y
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            current_y -= line_gap
            continue
        for line in textwrap.wrap(paragraph, width=width):
            fig.text(x, current_y, line, fontsize=size, va="top", ha="left")
            current_y -= line_gap
    return current_y


def add_text_page(pdf, title, body):
    fig = plt.figure(figsize=(8.5, 11))
    fig.text(0.08, 0.95, title, fontsize=15, weight="bold", va="top")
    add_wrapped_text(fig, body, y=0.90)
    pdf.savefig(fig)
    plt.close(fig)


def add_table_page(pdf, title, table, note=None):
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis("off")
    fig.text(0.08, 0.95, title, fontsize=15, weight="bold", va="top")
    display_table = table.copy()
    for col in display_table.columns:
        if pd.api.types.is_float_dtype(display_table[col]):
            display_table[col] = display_table[col].map(
                lambda v: "not provided" if pd.isna(v) else f"{v:.3f}"
            )
    tbl = ax.table(
        cellText=display_table.values,
        colLabels=display_table.columns,
        loc="center",
        cellLoc="center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1.0, 1.4)
    if note:
        add_wrapped_text(fig, note, y=0.18, size=10)
    pdf.savefig(fig)
    plt.close(fig)


def main():
    ensure_dirs()
    df = pd.read_csv(DATA_PATH)
    evidence = fit_locked_models(df)
    error_slices = write_tables(evidence)
    save_figures(evidence, error_slices)
    report_md = markdown_report(evidence, error_slices)
    (OUT_DIR / MD_NAME).write_text(report_md, encoding="utf-8")
    print(f"Wrote {(OUT_DIR / MD_NAME)}")


if __name__ == "__main__":
    main()
