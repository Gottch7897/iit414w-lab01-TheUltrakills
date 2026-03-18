# Baseline Report — [Your Name]

## 1. Prediction target
[One sentence: what you predict, for which unit, at which moment.]

## 2. Majority-class baseline
- Metric: [accuracy / F1 / precision / recall — choose one]
- Value: [FILL FROM CODE]
- Code: `DummyClassifier(strategy='most_frequent', random_state=414)`

## 3. Domain heuristic baseline
- Rule: [One sentence. Must use pre-race information only.]
- Metric (same as above): [FILL FROM CODE]
- Code cell: [paste the function you wrote]

## 4. Metric choice + justification
[3–5 sentences. Address: (a) class balance in your dataset, (b) cost of
false positives vs false negatives, (c) which metric you chose and why.]

Template: "I chose [METRIC] as my primary metric because my dataset has a
class imbalance of approximately [X%] positive class. A false positive in
this context means [describe], which carries [cost description]. A false
negative means [describe], which carries [cost description]. Given this
trade-off, [METRIC] is more informative than accuracy because [reason]."

## 5. Leakage guard item
[(a) which item from the 10-item checklist, (b) what you found,
(c) whether it required a fix.]

## 6. Baseline comparison & interpretation
(a) Which baseline is harder to beat? What does the gap between your
    two baselines tell you about your prediction problem?
(b) If your ML model later scores below the domain heuristic baseline,
    what would you conclude and what would you try next?
```