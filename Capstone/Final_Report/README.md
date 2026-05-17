# Final Report Package

This folder contains the final-report source package for **TheUltrakills**.

## Contents

- `generate_final_report.py`: regenerates the locked model evidence, tables, figures and Markdown report.
- `IIT414W_FinalReport_TheUltrakills.md`: report text in Markdown.
- `IIT414W_FinalReport_TheUltrakills.pdf`: PDF report.
- `figures/`: calibration plots, metric summary, constructor-tier slice chart, and what-if disagreement chart.
- `tables/`: regenerated CSV tables for splits, metrics, calibration summary, error slices, and the what-if scenario.

## Reproduce

From the repository root:

```bash
venv/bin/python Capstone/Final_Report/generate_final_report.py
```

Expected outputs:

- `Capstone/Final_Report/IIT414W_FinalReport_TheUltrakills.md`

- refreshed files under `Capstone/Final_Report/figures/` and `Capstone/Final_Report/tables/`

The script uses the approved course stack already used in Hito 2: `pandas`, `numpy`, `matplotlib`, and `scikit-learn`. All model `random_state` arguments use `RANDOM_SEED = 414`.

## Evidence Boundary

The report uses Hito 1 and Hito 2 as source material. It does not retune the model after reading 2023-2024 test metrics. Strategy variables are used only as user-controlled scenario inputs for what-if comparison.
