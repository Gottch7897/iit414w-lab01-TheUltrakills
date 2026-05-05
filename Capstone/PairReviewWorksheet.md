# Pair Review Worksheet — Capstone Hito 1
### IIT414W · Block 5 · Mon May 4, 2026 · 15:45–16:05

> **The point of this exchange is structured scrutiny, not feedback.** Polite reviews are useless. Your job for the next 14 minutes is to find the weakest decision in the partner team's framing and name it concretely. The team being reviewed commits the critique they received to GitHub at 16:00 — public artifact, no escape.

**Reviewing team:** TheUltrakills
**Reviewed team:** Model Thinkers (11 group)

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

> From looking at their decision and target, we came to the conclusion that it lacked a bit of direction, as its not clear what the end goal is for the midfield driver. If it is to get on the podium, then the target is to coarse. But, if their goal is to get points on the board, then the target is a great match (as you score when in top 10).

TIP: Pit-stop choices often shift finishing position by a few places; expected points or an ordinal/multi-class target captures that nuance better.

---

### Q2. Is their baseline plan F1-defendable? Could they justify it WITHOUT ever seeing 2023–2024 data?

Concrete answer: 

> Skipped

---

### Q3. Are their what-if scenarios specific enough to RUN, or are they generic?

Concrete answer:

> Their scenarios remain too generic and too similar between each other:
- They lack depth, as curreently they just change the amount of pit stops and compund sequence.
- They work from the base 2 variables, and because of that they lack more insight as to what a real scenario could bring.

- They do have specific values, which is good!

Suggestions: They have a good base, but the lack of depth is hurting. Therefore, we sugest the following changes and additions:
- Scenario A: n_stops=1, compound_sequence='S-M', stint_lengths=[40], avg_pit_stop_duration_s=22, grid_position=12, constructor_tier='mid' (one-stop: soft→medium; single long stint of 40 laps)
- Scenario B: n_stops=2, compound_sequence='S-M-S', stint_lengths=[22,20], avg_pit_stop_duration_s=22, grid_position=12, constructor_tier='mid' (two-stop: soft→medium→soft; stints 22 + 20 laps)

TIP: include the same temporal/covariate context (e.g., grid_position, constructor_tier, avg_pit_stop_duration_s) so scenarios are executable. For point-sensitive decisions consider adding an expected-points scenario or a is_podium alternative.

---

### Q4. Which of the five known limitations did they NOT acknowledge that they should have?

Concrete answer:

> Number (5): "Strategy choice is not independent of car pace, driver, weather, and race incidents. Teams must discuss this confounding when they make recommendations."

> They did well adressing future changes to F1 races, but missed the present cross dependance of these variables, as your baseline uses n_stops, compound_sequence, and stint_lengths as features to predict is_top10. 
> Remember, strategy choices are NOT random. They're made by strategy engineers who know the car performance, driver skill, weather, and track conditions. Better cars/drivers with better conditions tend to choose 1-stop and also tend to finish top-10 (these events are dependant on each other). This is also important to note as note of the mistakes you made in Section 4 (your lack of depth made it so you didn't acount for these cross-dependencies).

Suggestions: we reccomend that you choose between these options
1. Acknowledge the confounder in Section 5 and discuss how you'll handle it (matching, stratification, causal forests, etc.).
2. Pivot to using only pre-race observable features (weather forecast, circuit characteristics, grid position) and drop strategy features from the model.
3. Clearly frame your "what-ifss" as a descriptive correlation ("historically, 1-stop drivers finished top-10 X% of the time") not a causal effect ("recommending 1-stop will increase P(top10) by X%").

TIP: Limitation (4), consider that strategy features are post-race observations (this also hits your criteria): if n_stops and compound_sequence are known only after the race, how can you use them in a Friday pre-race model? You should clarify whether you're treating these as hypothetical counterfactuals ("if we commit to 1-stop...") or post-hoc descriptive features.

---

### Q5. If their model lands at Brier 0.20 on the test set (worse than docent grid-rule 0.208 — close to it but not better), what does their framing currently say to defend that scenario?

> *This is the "what if my model isn't good enough" question. Look at their Section 6 (experiment plan). If their framing doesn't currently have a path for "we did not beat the docent baseline, here's what we'd say," they will be exposed in Demo Day. The strongest framings have a fallback story.*

Concrete answer:

> Skipped

---

## The ONE Concrete Critique We Will Deliver

After answering 3+ questions above, decide: which critique is the most important for this team to hear? Write it as one sentence, framed as an observation, not an attack.

**Format:** "Your [section X] doesn't [specific issue]. The consequence is [what happens in Hito 1 or Demo Day]. One thing to do: [concrete action]."

> Your section 4 doesn't consider the cross dependancy between the dataset features, which in turn affects your later sections. You dont specify important variables such as driver, circuit, weather or compound. This, in turn, will lead to not having proper "what-ifs" for your first deliverable, and also may get a wrong understanding of following criteria. 
We reccomend that you shuffle the dataset and pick specific values for your scenarios (ex: constructor/team, driver, weather), that way you get more depth and can get a great result on the first deliverable.


---

## Notes for Reviewing Team (your records, not committed)

What did you learn from reading their framing that informs your own?

> That we may have mischosen our metrics, and a certain misread of the requirements.

What is one thing they did better than you did?

> Section 3 and 5, with the former understanding the metrics to use, and the latter explaining how the uncertain changes in the future could possibly affect their predictions.

---

## After the Exchange

The reviewed team writes the critique they received into their own `framing.md` Section 8 by 16:00. The reviewing team's worksheet is for their own records — keep it as a learning artifact.

Instructor records pair review participation in the session log. Pairs that visibly went through the questions vs pairs that just chatted will be visible from the artifact (the critique-received section).
