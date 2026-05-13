# Baseline Comparison

— a baseline comparison table on both targets. For is_top10, compare against the docent baseline (Brier 0.132). For your expansion target, compare against an appropriate baseline you justify.


=== Metrics on test set (2023-2024) ===

Primary target: is_top10  (binary)
  Brier      = 0.1322   (docent reference: 0.1320)
  Log loss   = 0.4173
  ROC-AUC    = 0.8920   (docent reference: 0.8920)
  Pos. rate  = 0.517

Expansion target: is_top5  (binary)
  Brier      = 0.0910
  Log loss   = 0.2911
  ROC-AUC    = 0.9323
  Pos. rate  = 0.259