final Report plan
Step ID: FR.S01
Name: Audit source artifacts
Rubric mapping: D1 Technical completeness 25%, D4 Reproducibility 20%
Inputs: Capstone/Hito_1/, Capstone/Hito_2/, test/f1_strategy_race_level.csv, Canvas Markdown files
Outputs: Inventory of reusable tables, figures, notebooks, metric values, scenario files, prompt logs
Decisions for me:

Confirm team metadata: names, repo URL, exact team name for IIT414W_FinalReport_TheUltrakills.pdf
- **Team name:** TheUltrakills
- **Team members:** Martín Gottschalk, Marcial Ibáñez
- **GitHub repo URL:** https://github.com/Gottch7897/iit414w-lab01-TheUltrakills.git
Confirm whether existing Hito artifacts are final source of truth or whether any file has known errors: they are final source of truth


Step ID: FR.S02
Name: Lock report framing
Rubric mapping: D2 Domain reasoning 20%, D3 Honest comparison 20%
Inputs: Hito 1 framing, Hito 2 what-if files, race-level columns: driver_id, circuit_type, grid_position, strategy scenario columns
Outputs: Final §2 framing draft: decision, decision-maker, time window, prediction unit, targets, assumptions
Decisions for me:

Mandatory checkpoint 1: choose the supported strategy decision: pre-race strategy call before start.




Step ID: FR.S03
Name: Define modeling narrative
Rubric mapping: D1 Technical completeness 25%, D2 Domain reasoning 20%, D3 Honest comparison 20%
Inputs: hito1_baseline.ipynb, hito2_modeling.ipynb, baseline_comparison.md, model metrics and feature sets
Outputs: Final §4 outline covering baselines, model family per target, feature boundary, hyperparameter rationale
Decisions for me:

Mandatory checkpoint 2: choose baseline/story order.
Options:  separate model family per target.


Step ID: FR.S04
Name: Lock calibration approach
Rubric mapping: D1 Technical completeness 25%, D3 Honest comparison 20%
Inputs: 2022 calibration block, binary targets is_top10 and selected expansion target if binary, calibration plots from Hito 2
Outputs: Calibration method note, final calibration figure requirements, probability-quality wording
Decisions for me:

Mandatory checkpoint 3: choose sigmoid/Platt


Step ID: FR.S05
Name: Select expansion target story
Rubric mapping: D1 Technical completeness 25%, D2 Domain reasoning 20%
Inputs: Hito 2 target results, columns is_top5, is_top3, finish_position, points
Outputs: Final target-pair explanation for §2, §4, §5, and §6
Decisions for me:

Mandatory checkpoint 5: choose the expansion target to emphasize: is_top5


Step ID: FR.S06
Name: Build results evidence package
Rubric mapping: D1 Technical completeness 25%, D3 Honest comparison 20%, D5 Written communication 15%
Inputs: Hito 2 metric tables, docent baseline Brier 0.132 and ROC-AUC 0.892, calibration plots, model outputs
Outputs: Final §5 metric table, calibration plot references, plain-English result bullets
Decisions for me:

Confirm how to phrase underperformance if our model does not beat the docent baseline: “matched/beat baseline,”


Step ID: FR.S07
Name: Lock error-analysis slices
Rubric mapping: D1 Technical completeness 25%, D2 Domain reasoning 20%, D3 Honest comparison 20%
Inputs: error_analysis.md, columns strategy_type, circuit_type, candidate third-slice columns
Outputs: Final §6 slice table plan and three failure-mode hypotheses

Decisions for me:

Mandatory checkpoint 6: choose third slice beyond strategy type and circuit type: constructor_tier



Step ID: FR.S08
Name: Lock what-if comparison
Rubric mapping: D1 Technical completeness 25%, D2 Domain reasoning 20%, D3 Honest comparison 20%
Inputs: whatif_comparison.md, whatif_scenario_selection.md, strategy scenario columns: n_stops, strategy_type, compound_sequence, stint_lengths
Outputs: Final §6 disagreement scenario with exact feature values and operational consequence
Decisions for me:

Mandatory checkpoint 4: choose two concrete scenarios
- {
        "scenario": "A_one_stop",
        "grid_position": 4.0,
        "driver_prior3_avg_finish": 5.0,
        "constructor_prior3_avg_finish": 5.0,
        "driver_circuit_prior_avg": 10.5,
        "constructor_tier": "midfield",
        "circuit_type": "permanent",
        "n_stops": 1,
        "strategy_type": "one_stop",
        "compound_sequence": "M-H",
    },
    {
        "scenario": "B_two_stop",
        "grid_position": 4.0,
        "driver_prior3_avg_finish": 5.0,
        "constructor_prior3_avg_finish": 5.0,
        "driver_circuit_prior_avg": 10.5,
        "constructor_tier": "midfield",
        "circuit_type": "permanent",
        "n_stops": 2,
        "strategy_type": "two_stop",
        "compound_sequence": "M-H-S",
    }


Step ID: FR.S09
Name: Write limitations and honesty sentence
Rubric mapping: D2 Domain reasoning 20%, D3 Honest comparison 20%
Inputs: mitigations.md, leakage_audit.md, known dataset limitations, error-analysis failures
Outputs: Final §7 limitations, risks, and mandatory deployment gate sentence
Decisions for me:

Mandatory checkpoint 7: choose limitation emphasis: emphasis on regime shifts, single-team bias, and scenario dependence, mention others too.


Step ID: FR.S10
Name: Assemble reproducibility package
Rubric mapping: D4 Reproducibility 20%, D1 Technical completeness 25%
Inputs: notebooks, generated artifacts, README.md, PROMPTS.md, repo status, environment files
Outputs: Updated runbook plan, writing-phase PROMPTS.md entries, final artifact checklist, final-v1 tag plan
Decisions for me:

Confirm exact reproduction command sequence to document.
Confirm whether AI-assisted prose/caption/critique prompts should be documented as separate entries or grouped by writing phase: separated entries



Step ID: FR.S11
Name: Draft and package PDF
Rubric mapping: D1 Technical completeness 25%, D5 Written communication 15%, D4 Reproducibility 20%
Inputs: Sections from FR.S02–FR.S10, figures, tables, references, title metadata
Outputs: IIT414W_FinalReport_TheUltrakills.pdf, title page with headline and final-v1 hash, 8–12 page report
Decisions for me:

Confirm headline finding after results and what-if evidence are locked.
Confirm references style: APA


DEMO DAY PLAN

Step ID: DD.S01
Name: Choose pitch spine
Rubric mapping: Final presentation/defense using same report evidence; connected to D2 Domain reasoning and D3 Honesty
Inputs: Final Report §1, §6, §7; same metrics and what-if artifacts
Outputs: 7-minute narrative outline
Decisions for me:

Mandatory checkpoint 8: choose the slide/narrative spine: headline finding first


Step ID: DD.S02
Name: Build seven-minute deck
Rubric mapping: Final presentation/defense of same evidence base; D5 communication carryover
Inputs: Final Report figures, metric table, calibration plot, slice table, what-if scenario
Outputs: Pitch deck with headline, decision context, target comparison, evidence, recommendation, honesty sentence
Decisions for me:

Choose deck format: Markdown slides


Step ID: DD.S03
Name: Prepare disagreement scenario defense
Rubric mapping: Demo Day Q&A readiness; D2 Domain reasoning and D3 Honest comparison
Inputs: Final Report §6 what-if scenario, exact feature values, both target outputs, operational consequence
Outputs: Q&A-ready scenario script explaining why the targets disagree and what the strategy desk should do
Decisions for me:

Choose how assertive the recommendation should be: recommend conditional deployment


Step ID: DD.S04
Name: Write speaker notes
Rubric mapping: Demo Day individual Q&A readiness; D4 reproducibility and D3 honesty carryover
Inputs: Final Report sections, README, PROMPTS.md, limitations, baseline comparison
Outputs: Speaker notes/team prep covering framing, metrics, calibration, error analysis, limitations, reproducibility, AI use
Decisions for me:

Assign ownership by teammate for Q&A sections: all teammates defend all sections with backups.



Step ID: DD.S05
Name: Rehearse and tighten
Rubric mapping: Demo Day communication and defense quality
Inputs: Draft deck, speaker notes, final report evidence
Outputs: 7-minute timing pass, likely Q&A list, final honesty sentence for spoken delivery
Decisions for me:

Choose rehearsal priority: Q&A first
