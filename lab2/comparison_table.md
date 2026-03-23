# Lab 1 vs Lab 2 — Comparison Table
## [Martín Gottschalk, Marcial Ibañez]

| Model / Baseline | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------------------------|----------|-----------|--------|-------|---------|
| Majority class (Lab 1) | 0.50 | 0.0 | 0.0 | 0.0 | 0.5 |
| Domain heuristic (Lab 1)| 0.67 | 0.62 | 0.89 | 0.73 | 0.67 |
| Prior-period (if done) | 0.XX | 0.XX | 0.XX | 0.XX | 0.XX |
| Lab 2 model (LogReg/DT) | 0.73 | 0.72 | 0.74 | 0.73 | 0.73 |
## Primary metric: [ACCURACY] (justified in Lab 1)
## Interpretation (3–5 sentences)
[Did the model beat the baselines? By how much? Which baseline was hardest to beat? What does this tell you about the value of your features vs. the baseline rules? If the model did NOT beat a baseline, what does that mean and what would you change?]

**NOTE**: Previously reported results in baseline_report.md were flawed, as the method used for the domain heuristic model was incorrect, using the same method as the `Majority-class baseline`. As such, the numbers and analysis done in that report are wrong, and should not be compared to the ones here. Instead, check lab1/baseline2.ipynb for the correct results. 