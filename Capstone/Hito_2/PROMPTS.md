# PROMPTS — Hito 2

## Entry 1 — Expansion target selection

**Context:** Hito 2 required a second target in addition to `is_top10`.

**Prompts:** Asked Codex to explain the available expansion targets and how each would support the race-strategy decision context.

**Output:** Codex described `is_top5`, `is_top3`, `finish_position`, and `points`, including trade-offs for calibration, interpretability, and decision value.

**Validation:** The Hito 2 rubric requires a target that adds decision value beyond `is_top10`. We checked the chosen decision context: a strategy engineer comparing one-stop vs two-stop strategies.

**Adaptations:** We selected `is_top5` because it supports upside detection beyond a points-finish target while remaining a binary probability target.

**Final Decision:** Model both `is_top10` and `is_top5` in Hito 2.

## Entry 2 — Corrected what-if scenario selection

**Context:** The original Hito 1 what-if scenario used Qatar 2024, but the selected strategy encodings were inconsistent with the stop counts.

**Prompts:** Asked Codex to inspect the dataset for cleaner one-stop and two-stop scenario candidates.

**Output:** Codex found that the Qatar 2024 rows had compressed or inconsistent strategy fields, then proposed cleaner alternatives from Monza 2024, Dutch GP 2024, and Las Vegas 2023.

**Validation:** We checked that the final scenario had internally consistent `n_stops`, `strategy_type`, `compound_sequence`, and concrete strategy values.

**Adaptations:** We rejected the Qatar scenario and selected the Dutch GP 2024 scenario because it provided a clean one-stop vs two-stop comparison.

**Final Decision:** Use the Dutch GP scenario for Hito 1 planning and Hito 2 what-if analysis.

## Entry 3 — Error-analysis reasoning

**Context:** Hito 2 required concrete error analysis by strategy type, circuit type, and one additional context.

**Prompts:** Asked Codex to help turn the notebook's slice tables into an `error_analysis.md` write-up with failure hypotheses.

**Output:** Codex drafted hypotheses for high-error slices such as `three_plus_stop`, `semi-street`, `midfield`, `street`, and `front`.

**Validation:** The hypotheses were checked against the actual pasted slice outputs, including sample sizes, actual rates, mean predicted probabilities, Brier scores, and absolute errors.

**Adaptations:** The write-up used only the provided metrics and did not invent sample sizes or additional failure slices.

**Final Decision:** Use the generated `error_analysis.md` as the Hito 2 error-analysis artifact.

## Entry 4 — Conditional recommendation

**Context:** The Hito 2 scenario predictions created a disagreement between `is_top10` and `is_top5`.

**Prompts:** Asked Codex to interpret the scenario where one-stop had higher Top 10 probability but two-stop had higher Top 5 probability.

**Output:** Codex offered three recommendation options: recommend one-stop, recommend two-stop, or use a conditional recommendation.

**Validation:** The prediction table showed that one-stop improved Top 10 probability by about 2.6 percentage points, while two-stop improved Top 5 probability by about 2.3 percentage points.

**Adaptations:** We chose the conditional recommendation because it was more honest than forcing a single strategy when the targets pointed in different directions.

**Final Decision:** Recommend one-stop for points security and two-stop for Top 5 upside.
