# Baseline Comparison

— a baseline comparison table on both targets. For is_top10, compare against the docent baseline (Brier 0.132). For your expansion target, compare against an appropriate baseline you justify.

=== Metrics on test set (2023-2024) ===

Primary target: is_top10  (binary)
  Brier      = 0.1322   (docent reference: 0.1320)
  Log loss   = 0.4173
  ROC-AUC    = 0.8920   (docent reference: 0.8920)
  Pos. rate  = 0.517

Expansion target: is_top5  (binary)
  Brier      = 0.0910 (our baseline reference: 0.1918)
  Log loss   = 0.2911
  ROC-AUC    = 0.9323 (our baseline reference: 0.5000)
  Pos. rate  = 0.259


**Baseline justification**: its based on answering “If we used zero features and only the historical Top-5 rate, how well would we do?”

- It helps us match against our 2 metrics (brier and ROC-AUC)
- It uses train prevalence (2019-2021) and evaluates on test (2023-2024), so no leakage from test labels.
- It is calibrated by construction to the train base rate (Predicting p=Pr(y=1) for all rows is the simplest calibrated prior model.)
- As is, it gives a practical minimum bar to beat 
