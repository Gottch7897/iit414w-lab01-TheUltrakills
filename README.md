# IIT414W Lab 01

## (a) Header
- Full Names: `Martín Gottschalk, Marcial Ibañez`
- GitHub Usernames: `Gottch7897, MarcialIbanezS`
- Course Code: `IIT414W`
- Date: `2026-03-16`

## (b) System Info
- Operating System (name + version): `Microsoft Windows 11 Home Single Language (10.0.26200)`
- Python Version: `Python 3.14.2`
- Package Manager Version:
  - `pip --version`: `pip 25.3`

## (c) Setup Instructions

### Option 1: Setup from `requirements.txt`
```bash
# 1) Open terminal in project root
cd c:\Users\your-file-directory

# 2) (Recommended) Create and activate virtual environment
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# 3) Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### Verify Setup
```bash
python --version
pip --version
```

## (d) How To Run
Run notebooks in this order.

### Required Run Order
No required run order.

### Command Examples
```bash

# run notebook 1
python -m jupyter nbconvert --to notebook --execute --inplace eda.ipynb

# run notebook 2
python -m jupyter nbconvert --to notebook --execute --inplace baseline.ipynb
```

```bash
# OR launch Jupyter UI and run all cells in order manually
python -m notebook
```

Notes:
- Internet access is required for FastF1 session loading and Jolpica API requests.

## (e) Problems Encountered
Documented issues from this environment and setup flow:

### Problem 1
- Issue: 
- Cause: 
- Fix: 

## (f) Expected Outputs
Successful run indicators:

- `eda.ipynb`:
 

- `baseline.ipynb`:
 

---

## Submission Checklist

REQUIRED — every submission must have these:

+ eda.ipynb — Kernel → Restart & Run All completes without errors

+ eda.ipynb — At least 5 research questions with Question → Plot → Interpretation → Decision
+ eda.ipynb — Temporal split defined with written rationale
+ eda.ipynb — Class balance analysis for target variable
+ eda.ipynb — At least 1 explicit trap check (spurious correlation, survivorship, anchoring)
+ eda.ipynb — 1-3-1 summary in final Markdown cell
□ baseline.ipynb — Kernel → Restart & Run All completes without errors
□ baseline.ipynb — 1 domain heuristic baseline (rule-based, no ML code)
□ baseline.ipynb — Accuracy reported on validation set (not training set)
□ baseline.ipynb — Reflection: "What could accuracy be hiding?"
□ baseline.ipynb — Lower bound statement: "Lab 2 model must beat this"
□ baseline.ipynb — No post-race features used (leakage check)
+ DATA_QUALITY_LOG.md — At least 5 issues documented
+ PROMPTS.md — Complete with at least 2 entries (or "no AI used" statement)
□ README.md — Runbook that works in <10 minutes
+ environment.yml or requirements.txt — Complete and working
+ .gitignore — Excludes cache, checkpoints, __pycache__
+ RANDOM_SEED = 414 in both notebooks
□ Canvas text entry — Repo URL + 3-sentence 1-3-1 summary
+ All team members listed in README.md

STRETCH — optional, rewarded if present:
□ baseline.ipynb — Additional metrics (Precision, Recall, F1, ROC-AUC)
□ baseline.ipynb — Second baseline (sklearn model or second heuristic)
□ baseline.ipynb — Metric choice justification
□ PROMPTS.md — Documents how you learned/computed the stretch metrics via AI

