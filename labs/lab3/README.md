# IIT414W Lab 03

## (a) Header
- Full Names: `Martín Gottschalk, Marcial Ibañez`
- GitHub Usernames: `Gottch7897, MarcialIbanezS`
- Course Code: `IIT414W`

- Date: `2026-04-20`

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
python -m jupyter nbconvert --to notebook --execute --inplace 

```

```bash
# OR launch Jupyter UI and run all cells in order manually
python -m notebook
```

Notes:
- Internet access is required for FastF1 session loading and Jolpica API requests.

## (e) Problems Encountered

### Problem 1
- Issue: 
- Cause: 
- Fix: 




## (f) Expected Outputs
Successful run indicators:
- 
---

## Submission Checklist

REQUIRED — every submission must have these:

labs/lab3/
├── framing_decision.md            # Framing choice + justification (graded under C2)
├── model_exploration.md           # In-class checkpoint (W5 Mon) — bonus artifact
├── lab3_model_comparison.ipynb    # Main notebook with visible outputs
├── comparison_table.md            # Standalone comparison table
├── memo.md                        # 1-page technical memo
├── PROMPTS.md                     # AI documentation (authenticity-scored)
└── README.md                      # Reproduction instructions
