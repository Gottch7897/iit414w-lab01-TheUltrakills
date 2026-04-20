# Framing Decision

## 1) Business question
Before each race weekend, a team principal wants to know: which drivers are at higher risk of DNF (Did Not Finish), so the team can adjust strategy risk, pit flexibility, and contingency planning. The model supports this by estimating DNF risk from pre-race and historical context.

## 2) Target variable
The target is DNF (binary classification), defined as 1 when the race status is not "Finished" and 0 otherwise.

## 3) Metric
The primary metric is F1 score for the DNF class. F1 is appropriate because DNF prediction is an imbalanced problem and we need a balance between precision (not over-flagging risk) and recall (not missing true DNFs). Accuracy alone would be misleading here, since a majority-class strategy can appear strong while failing to identify the minority outcome reliably.

## 4) Rejected alternatives
We considered a regression framing that predicts points directly (for example, with MAE). We rejected it for this lab objective because race-operations planning in this stage is specifically about failure risk, and a single point estimate can hide whether zero points came from low pace versus non-finish risk.

We also considered a Top-10 binary target. We rejected it because Top-10 focuses on competitive performance, while the current decision problem is reliability and finish risk management. DNF framing aligns better with safety-margin and contingency decisions.

## Trade-off summary
This framing sacrifices fine-grained point prediction detail in exchange for a clearer and more actionable reliability signal. Given the operational question in this lab, that trade-off is intentional and appropriate.
