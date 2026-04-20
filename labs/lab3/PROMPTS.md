# PROMPTS.md — AI Usage Log
# IIT414W · [TheUltrakills] · [Lab03]
# One entry per significant AI interaction. Keep entries honest and specific.

---
PROMPTS.md demonstrates: (a) Traceability — claims map to specific notebook outputs ("AI suggested Ridge alpha=0.1; I tested alpha=0.1/1.0/10.0 and results are in cell 15"). (b) Operational detail —  (c) AI failure with specifics — what went wrong, why, what you did instead. (d) Critical distance — a specific AI limitation that affected THIS lab (not generic "AI can hallucinate").


## Entry [EXAMPLE] — [Short title, e.g. "DNF handling for rolling avg"] · [YYYY-MM-DD]

**Context:**
[1–3 sentences: what you were trying to solve and why it mattered for the task.]

**Prompt(s):**
 # Include all iterations. Label Prompt 1, Prompt 2 (refinement), etc.
Prompt 1: "[exact text sent to AI]"
Prompt 2 (refinement): "[exact text]"

**Relevant Output:**
[Paste key output. Summarize if very long. Preserve code exactly.]

**Operational detail:**
# exact error messages, specific metric values, cell references.
- Test 1: [what you checked, on what data, and what you found]
- Test 2: [edge case tested and outcome]
- [Comparison with baseline / manual check / unit test / visual check on real data]

**Adaptations. What went wrong:**
- what went wrong, why, what you did instead

**Critical distance**
 # a specific AI limitation that affected THIS lab (not generic "AI can hallucinate").

**Final Decision:**
[Used / Partially used / Rejected] — [reason in 1–3 sentences, tied to the task.]

-----

## Entry [1] — ["Miscellaneous Translation of previous code"] · [2026-04-19]

**Context:**
With previously used code in hand, it was copy-pasted into the notebook. Knowing the expected outcome and how the new dataframe should be adapted

**Prompt(s):**
# Include all iterations. Label Prompt 1, Prompt 2 (refinement), etc.
Prompt 1: "adapt the context, numeric and categorical features for the "DNF" target"
Prompt 2 (refinement): "UPdate the call to the 3 models so that it also includes random forest and XGBboost"

**Relevant Output:**
- Most cells related to the Comparisson Table section of the notebook, translating other code to use the modles inside this file.

**Operational detail:**
- Test 1: Manually accepted each line of code added, reading what small changes it did so no ligical mistakes were made.
- Test 2: Ran the edited cells, saw the output contained extra metrics, so I removed them (kept it simple).

**Adaptations. What went wrong:**
- Added more metrics than needed for the comparison. I removed them manually.
- Tried adding the baselines after the testing (instead of before). Removed.
- Misinpertetred some instructions, so I rewrote them (doing more than I asked).

**Final Decision:**
Used - The code runs correctly after some small adjustments.

-----

## Entry [2] — ["Leackage safety"] · [2026-04-19]

**Context:**
After running the above prompts [1], the AI agent warned about a posible leackage risk coming from DriverReliability and ConstructorStrength features. This made sense, so it was asked to fix those. The changes made can be seen in cell 2.

**Prompt(s):**
Prompt 1: "add a  leakage-safe version of DriverReliability and ConstructorStrength (computed only from past seasons) so DNF evaluation is temporally strict."

**Relevant Output:**
    "# Leakage-safe versions: each season uses only information from prior seasons.
    driver_year = (
        df.groupby(['FullName', 'Year'], as_index=False)
        .agg(SeasonStarts=('DNF', 'size'), SeasonDNFs=('DNF', 'sum'))
        .sort_values(['FullName', 'Year'])
    )"

**Operational detail:**
- Cell changed: cell 2.
- Test 1: Scanned the code and saw the changes it made. Got slighlty confused at the cummulative sum but later understood what it meant.
- Test 2: the cells ran as they did before, no errors raised.

**Adaptations. What went wrong:**
- No changes needed.

**Final Decision:**
Used - the code now is independant of later test years, freeing itself from leackage.

-----

## Entry [3] — ["Consistency check across artifacts"] · [2026-04-20]

**Context:**
Before final submission, we needed to verify that the narrative artifacts matched the implemented model. The goal was to confirm consistency between framing_decision.md, memo.md, and the notebook outputs.

**Prompt(s):**
Prompt 1: "es lo realizado consistente con el modelo? compara framing decision, memo y lab3 model"

**Relevant Output:**
- The review confirmed alignment on business question (DNF risk), target (DNF binary), metric (F1), and best-model recommendation (Random Forest).
- It also noted minor editorial issues (for example, spelling in notebook headings) and recommended running all cells before submission.

**Operational detail:**
- Test 1: Checked target consistency: `TARGET = "DNF"` in notebook versus framing and memo text.
- Test 2: Checked metric consistency: F1 usage in notebook cells and F1 reported in memo.
- Test 3: Checked result consistency: Train/Val/Test values (including RF test F1 0.658 and XGB 0.655) matched memo and comparison table.

**Adaptations. What went wrong:**
- No technical mismatch was found.
- Minor wording and spelling issues were identified as editorial (not modeling) issues.

**Critical distance**
- AI could confirm consistency quickly, but it may overlook context if outputs are stale or not re-executed. Manual verification of saved notebook outputs is still necessary.

**Final Decision:**
Used — the consistency check was accepted and used to validate final documentation coherence.

-----

## Entry [4] — ["Editorial quality review and prompt logging"] · [2026-04-20]

**Context:**
After consistency was confirmed, the next step was to review editorial quality and keep a transparent record of AI interactions. This entry documents the request to improve writing quality control and to log both prompts in PROMPTS.md.

**Prompt(s):**
Prompt 1: "Revisa la calidad editorial, guarda este prompt y el anterior en PROMPTS.md"

**Relevant Output:**
- Editorial review was completed for memo.md and framing_decision.md.
- Two prompt-traceability entries were added to PROMPTS.md (consistency check and editorial review request).

**Operational detail:**
- Test 1: Read memo.md and framing_decision.md to check clarity, tone, and terminology.
- Test 2: Verified that writing remains consistent with DNF classification framing and F1 evaluation.
- Test 3: Added structured entries with context, prompts, operational checks, and final decision.

**Adaptations. What went wrong:**
- No blocking issue occurred.
- Main adjustment was ensuring detailed traceability while keeping entries concise.

**Critical distance**
- AI can improve editorial quality, but final tone and authenticity should still be reviewed by the author to match course expectations and personal writing style.

**Final Decision:**
Used — prompt logging and editorial QA were incorporated into the final documentation workflow.

-----