# Mitigations

a list of risks and mitigations for the final report. At minimum: what would your model fail on, and what would you change before deployment?


## What would our model fail on?

Here are some scenarios and/or situations where our model could fail:

1) Rare race scenarios it has not seen often, like unusual safety car patterns, wet conditions, red flags, or multiple DNFs in the same race.

2) Missing or delayed inputs at prediction time (ex: if a feature depends on information that is not available before the decision point).



## Changes before deployment?

Some changes to do before a full deployment:

1) Validate that the leakage audit is correct with the help of field experts.

2) Documentation (use case, how to use, when NOT to use)
