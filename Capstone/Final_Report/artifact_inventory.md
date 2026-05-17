# Final Report Artifact Inventory

## Source Material

| Artifact | Role |
|---|---|
| `Capstone/Hito_1/framing.md` | Source for final problem framing, leakage distinction, and first scenario framing. |
| `Capstone/Hito_1/hito1_baseline.ipynb` | Source for locked split, Hito 1 grid-only baseline, and leakage audit structure. |
| `Capstone/Hito_2/hito2_modeling.ipynb` | Source for two-target model design, metrics, calibration, error slices, and what-if predictions. |
| `Capstone/Hito_2/baseline_comparison.md` | Source for model comparison and docent-baseline honesty language. |
| `Capstone/Hito_2/error_analysis.md` | Source for failure-mode hypotheses and required slices. |
| `Capstone/Hito_2/whatif_comparison.md` | Source for the target-disagreement scenario and conditional recommendation. |
| `Capstone/Hito_2/leakage_audit.md` | Source for feature roles and excluded columns. |
| `Capstone/Hito_2/mitigations.md` | Source for limitations and deployment-risk wording. |
| `Capstone/decisions.md` | Source for all selected final-report and Demo Day checkpoint choices. |
| `data/f1_strategy_race_level.csv` | Primary race-level dataset. |

## Regenerated Final Outputs

| Artifact | Produced by |
|---|---|
| `Capstone/Final_Report/IIT414W_FinalReport_TheUltrakills.md` | `generate_final_report.py` | `Capstone/Final_Report/tables/model_comparison.csv` | `generate_final_report.py` |
| `Capstone/Final_Report/tables/error_slices.csv` | `generate_final_report.py` |
| `Capstone/Final_Report/tables/whatif_comparison.csv` | `generate_final_report.py` |
| `Capstone/Final_Report/figures/calibration_is_top10.png` | `generate_final_report.py` |
| `Capstone/Final_Report/figures/calibration_is_top5.png` | `generate_final_report.py` |
| `Capstone/Final_Report/figures/whatif_disagreement.png` | `generate_final_report.py` |

## Demo Day Outputs

| Artifact | Role |
|---|---|
| `Capstone/Demo_Day/pitch_deck.md` | 7-minute headline-first pitch deck. |
| `Capstone/Demo_Day/speaker_notes.md` | Q&A and rehearsal prep for both teammates. |

## Tagging Note

The final report title page names the release as `final-v1`. Practical workflow:



If the instructor requires a literal short hash on the title page, insert the tagged commit hash manually after tagging and document that the printed hash identifies the submitted release lineage.
