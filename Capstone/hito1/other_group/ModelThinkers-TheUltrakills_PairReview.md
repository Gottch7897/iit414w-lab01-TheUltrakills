# Pair Review Worksheet — Capstone Hito 1
### IIT414W · Block 5 · Mon May 4, 2026 · 15:45–16:05

> **The point of this exchange is structured scrutiny, not feedback.** Polite reviews are useless. Your job for the next 14 minutes is to find the weakest decision in the partner team's framing and name it concretely. The team being reviewed commits the critique they received to GitHub at 16:00 — public artifact, no escape.

**Reviewing team:** Model Thinkers
**Reviewed team:** TheUltrakills

---

## How this works (instructor reads aloud at 15:45)

1. **Minutes 1–7:** read the partner team's `framing.md` and look at their dataset-load notebook. Write your answers below to at least 3 of the 5 questions.
2. **Minutes 8–14:** structured conversation. Each team gives the other ONE concrete critique — the strongest one you found. Not three. Not five. ONE that lands.
3. **Minutes 15–18:** each team writes the critique they RECEIVED into their own `framing.md` under section 8 ("Critique Received").
4. **Minute 19:** instructor calls time. Critique-received sections committed to GitHub.

There is no debate phase. The reviewed team writes down the critique, decides whether they agree, and writes a 1-line plan for how they'll address it. The reviewer's job is to deliver the critique, not to defend it.

---

## The Five Required Review Questions

For each question, write a concrete answer based on what you read in the partner team's framing.md. "Looks good" is not a concrete answer. You must give answers to at least 3 of the 5.

### Q1. Does their target match their decision context, or is `is_top10` chosen because it's the easiest binary?

Concrete answer:

Skipped

---

### Q2. Is their baseline plan F1-defendable? Could they justify it WITHOUT ever seeing 2023–2024 data?

> *Look at their Section 3. Did they describe the baseline based on F1 logic (qualifying → grid → constructor tier → recent form), or did they describe it based on what they think will work on the test set? The first is defendable. The second is contaminated reasoning.*

Concrete answer:

> Yes, this is F1-defendable and logically clean. Their baseline (grid position + frozen constructor rolling form) is explainable with racing context and with the structure of points and positions of the F1.

What they did well:
- They use a simple model that aligns with pit-wall intuition (starting position and team form matter).
- They explicitly freeze rolling constructor statistics from train years, reducing leakage risk.

Suggestion: Keep one explicit sentence in the demo narrative: "this baseline was chosen from domain logic, not test-set optimization."

---

### Q3. Are their what-if scenarios specific enough to RUN, or are they generic?

> *Look at their Section 4. Do their scenarios have actual feature values (e.g. "n_stops=1, compound_sequence=M-H, stint_lengths=[35, 35]")? Or do they say something vague like "we'll compare 1-stop vs 2-stop strategies"? Generic scenarios cannot be executed against the model on Wednesday.*

Concrete answer:

> The scenarios are executable because they include concrete values (`n_stops`, stint lengths, pit duration, wet flag, grid position, constructor form). However, they currently mix multiple changes at once, so attribution becomes unclear.

Observed issue:
- Scenario A vs B changes strategy and race context simultaneously (dry vs wet and stop-time shifts), which makes it hard to isolate what drove probability differences.

Suggestions:
1. Build one "controlled pair" where only `n_stops` changes and all other variables are fixed.
2. Keep a second "context-shift pair" (e.g., dry vs wet) as a separate analysis.
3. Reference a concrete driver/circuit row when presenting scenarios to make replication easy.

TIP: A what-if is strongest when one variable changes at a time from a shared baseline row.

---

### Q4. Which of the five known limitations did they NOT acknowledge that they should have?

skipped

---

### Q5. If their model lands at Brier 0.20 on the test set (worse than docent grid-rule 0.208 — close to it but not better), what does their framing currently say to defend that scenario?

> *This is the "what if my model isn't good enough" question. Look at their Section 6 (experiment plan). If their framing doesn't currently have a path for "we did not beat the docent baseline, here's what we'd say," they will be exposed in Demo Day. The strongest framings have a fallback story.*

Concrete answer:

> Right now, there is no explicit fallback defense. Section 6 lists experiments, but it does not say what decision value remains if performance is near Brier 0.20 and not clearly better than the docent rule.

What is missing:
- A predefined interpretation path for underperforming results.
- A communication plan for "useful but not superior" model behavior.

Suggestions:
1. Add a fallback statement: if Brier is not better, they will prioritize calibrated ranking stability across scenarios.
2. Report uncertainty bands (bootstrap CI) and emphasize directional consistency rather than absolute gain.
3. Define one threshold for "no-go" model usage in final recommendations.

TIP: Demo resilience improves a lot when failure conditions are planned in advance.

---

## The ONE Concrete Critique We Will Deliver

> Your Section 6 does not define a fallback if model quality stays near docent baseline levels. The consequence is that on Demo Day you may show results without a defensible decision policy. One thing to do: add a pre-committed fallback rule (calibrated scenario ranking + uncertainty thresholds) for cases where Brier does not clearly improve.

---

## Notes for Reviewing Team (your records, not committed)

What did you learn from reading their framing that informs your own?

> Their Section 4 is operationally stronger than ours because it already includes runnable scenario values, not only conceptual comparisons.

What is one thing they did better than you did?

> They were clearer in connecting the what-if setup to a decision metric (delta calibrated probability with uncertainty) and in stating why pit-stop duration matters.

---

## After the Exchange

The reviewed team writes the critique they received into their own `framing.md` Section 8 by 16:00. The reviewing team's worksheet is for their own records — keep it as a learning artifact.

Instructor records pair review participation in the session log. Pairs that visibly went through the questions vs pairs that just chatted will be visible from the artifact (the critique-received section).
