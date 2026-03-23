# Lab 1 vs Lab 2 — Comparison Table
## [Martín Gottschalk, Marcial Ibañez]

| Model / Baseline | Accuracy | Precision | Recall | F1 | ROC-AUC |
|------------------------|----------|-----------|--------|-------|---------|
| Majority class (Lab 1) | 0.50 | 0.0 | 0.0 | 0.0 | 0.5 |
| Domain heuristic (Lab 1)| 0.67 | 0.62 | 0.89 | 0.73 | 0.67 |
| Lab 2 model (LogReg/DT) | 0.73 | 0.72 | 0.74 | 0.73 | 0.73 |
## Primary metric: [ACCURACY] (justified in Lab 1)
## Interpretation (3–5 sentences)
Overall, our Lab2 model beat the previously done baselines in all metrics except for the Recall when compared to the Domain heuristic. Comparing it against that model, it beat its metrics: 
-Accuracy by 6%
-Precision by 10%
-Recall by -15% (not beaten)
-F1 by 0% (matched)
-ROC-AUC by 6%
As seen in our Notebook, some features were weaker than others, and as such, dragged the overall model down when used all together. This tells us that not all features are good for training, and that for future occasions, we should consider removing them to improve the model.
As the Majority class didn't provide great results, the hardest baseline to beat was the Recall, followed by the F1 score. From this, we gather that the current model is not the best at catching ALL the positives, atleast in comparison to the Domain Heuristic. 

**NOTE**: Previously reported results in baseline_report.md were flawed, as the method used for the domain heuristic model was incorrect, using the same method as the `Majority-class baseline`. As such, the numbers and analysis done in that report are wrong, and should not be compared to the ones here. Instead, check lab1/baseline2.ipynb for the correct results. 