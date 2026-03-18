# Baseline Report — [`Martín Gottschalk, Marcial Ibañez`]

## 1. Prediction target
[One sentence: what you predict, for which unit, at which moment.]
[Predicted if the drivers eneded in the Top10 or not, from 2021-2024]

## 2. Majority-class baseline
- Metric: [accuracy/F1]
- Value: [0.50]
- Code: `DummyClassifier(strategy='most_frequent', random_state=414)`

## 3. Domain heuristic baseline
- Rule: ["Ferrari always ends in the top 10"]
- Metric (same as above): Value is [0.50]

- Code cell:    `df_heuristic['HeuristicPred'] = 0`
                `for idx, row in df_heuristic.iterrows():`
                    `if row['TeamName'] == 'Ferrari':`
                        `df_heuristic.at[idx, 'HeuristicPred'] = 1`


## 4. Metric choice + justification
[3–5 sentences. Address: (a) class balance in your dataset, (b) cost of
false positives vs false negatives, (c) which metric you chose and why.]

(a) The class balance is 50/50, so its right in the middle for either. This is beacuse of how being in the top10 works in a competition of 20 racers (basically half and half).
(b) The cost of false positives in this case, would create a false sense of hope for the team or fans. In other contexts, if used for bets, it would result in a loss. False negatives, on the other hand, would cause the sense of depreciation for teams and drivers. For bets, it would lead to missing a chance to make money.
(c) We chose accuracy and f1 score as our metric, as it tells us how many true values we got in total.


## 5. Leakage guard item

(a) These items were used: 'FullName', 'TeamName', 'GridPosition', 'Year', 'Circuit', 'Round'
(b) Some issues arose as there was not enough data, so we expanded it to include more years in the test data.
(c) A small fix had to be done to remove the 'Year' column after the test dataset was expanded to include more than one.

## 6. Baseline comparison & interpretation
(a) Either model is equally beatable, as both gave the same 0.50 result. The gap between the 2 baselines (or lack thereof) shows that the domain heuristic was a weak choice, as there were no changes to the results.

(b) If our ML model gets a lower score, then we can conclude that we need to make even stronger predictions, as our current ones have not made a dent to the results.

```