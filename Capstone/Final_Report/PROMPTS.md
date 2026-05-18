# PROMPTS.md — AI Usage Log
# IIT414W · [TheUltrakills] · [Capstone Milestone]
# One entry per significant AI interaction. Keep entries honest and specific.

---

---

## Entry [1] — Final report structure and rubric mapping · 2026-05-16

**Context:**
We needed to turn the completed Hito 1 and Hito 2 artifacts into the final 8-12 page report and Demo Day plan without recreating the milestones. This mattered because the final report rubric grades technical completeness, domain reasoning, honesty, reproducibility, and writing quality.

**Prompt(s):**
Prompt 1: "Read the Canvas pages and dataset head, then produce an execution plan for the Final Report and Demo Day. Do not write code until the plan is approved."

**Relevant Output:**
The AI produced a step-by-step plan with checkpoints for framing, modeling narrative, calibration, expansion target, error slices, what-if scenario, limitations, reproducibility, PDF packaging, and Demo Day.

**Validation:**
- Checked the plan against Markdowns containing the Canvas instructions.
- Confirmed the plan preserved the locked target, split, seed, leakage rule, and docent baseline comparison.
- Confirmed it treated Hito 1 and Hito 2 as source material, not deliverables to recreate.

**Adaptations:**
- Added `Capstone/decisions.md` to lock the selected choices before implementation.
- Rejected any plan path that would retune after seeing 2023-2024 test metrics.

**Final Decision:**
Used. The plan became the implementation checklist for the final report and Demo Day package.

---

## Entry [2] — Final report prose and evidence packaging · 2026-05-16

**Context:**
We needed a report generator, final report prose, tables, figures, and a PDF that matched the locked Hito evidence. The key risk was overstating the model, especially because the Top 10 model did not beat the docent baseline.

**Prompt(s):**
Prompt 1: "Implement the approved plan using `Capstone/decisions.md` as the list of selected choices."

**Relevant Output:**
The AI created `Capstone/Final_Report/generate_final_report.py`, regenerated metric tables, calibration plots, error-slice tables, the what-if table, the Markdown report, and `IIT414W_FinalReport_TheUltrakills.pdf`.

**Validation:**
- Ran `venv/bin/python Capstone/Final_Report/generate_final_report.py`.
- Confirmed the regenerated metrics match Hito 2: `is_top10` Brier 0.139039 and ROC-AUC 0.881266; `is_top5` Brier 0.090479 and ROC-AUC 0.934413.
- Confirmed the what-if numbers match Hito 2: one-stop Top 10 0.892756, two-stop Top 10 0.866485, one-stop Top 5 0.788785, two-stop Top 5 0.811390.

**Adaptations:**
- The AI initially noted the system `python3` lacked `scikit-learn`; we validated that the repository `venv/bin/python` includes it and used the venv for generation.
- The report wording was kept honest: the model beats the simple baseline but does not beat the docent Top 10 reference.
- Causal language was removed from the what-if recommendation.
- Removed any part related to PDF generation, as it could overwrite our report if run in the same directory.
- Created our own PDF report from the Markdown file, applying changes where needed.

**Final Decision:**
Used Partially with validation. The generated report package is accepted as the final evidence package, though the PDF itself was made by us in another Google Drive document.

---

## Entry [3] — Demo Day deck and Q&A prep · 2026-05-16

**Context:**
We needed a 7-minute Demo Day pitch that presented the same evidence as the final report and prepared both teammates for individual Q&A.

**Prompt(s):**
Prompt 1: "Build the Demo Day plan from the same final report evidence. Use headline finding first, Markdown slides, conditional deployment, all teammates defend all sections, and Q&A-first rehearsal."

**Relevant Output:**
The AI produced `Capstone/Demo_Day/pitch_deck.md` and `Capstone/Demo_Day/speaker_notes.md`.

**Validation:**
- Checked that the deck uses the same metric table, what-if scenario, error slices, and honesty sentence as the final report.
- Confirmed it does not introduce a separate analysis track or new unsupported claims.
- Confirmed the Q&A includes the docent-baseline shortfall and leakage/scenario-input boundary.

**Adaptations:**
- Kept the recommendation conditional rather than forcing a single strategy.
- Included a reliability warning for midfield Top 10 predictions because the selected what-if context is midfield.

**Final Decision:**
Used. The deck and speaker notes are the Demo Day preparation package.
