# IIT414W Lab 02

## (a) Header
- Full Names: `Martín Gottschalk, Marcial Ibañez`
- GitHub Usernames: `Gottch7897, MarcialIbanezS`
- Course Code: `IIT414W`
- Date: `2026-03-23`

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
- Issue: ERROR: "Found input variables with inconsistent numbers of samples: [440, 479]"
- Cause: comparisson between "y_val" and "y_pred". 
- Fix: changed "y_val" for "y_test", as the model was trained on the latter.

### Problem 2
- Issue: Majority class and Domain Heuristic (lab1 redone model) gave the same results.
- Cause: Using the same DummyClassifier for both ("most_frequent").
- Fix: Changed the DomianHeuristic so that it uses LogisticRegression.


### Problem 3
- Issue: Baseline 2 (driver rolling form) produced missing values in the engineered featureDriverTop10RateLast5, which caused unstable training and potential model errors.
- Cause: For each driver’s first race(s), there is not enough historical data after shift(1).rolling(5), so the rolling feature becomes NaN.
- Fix: Replaced missing rolling values with a training-set prior (global_top10_prior) before evaluation, so every row has a valid numeric feature and Logistic Regression can train consistently.

## (f) Expected Outputs
Successful run indicators:
- All cells of lab02_feature_engineering.ipynb run smoothly, correctly loading libraries, creating the cache and the regression model.

---

## Submission Checklist

REQUIRED — every submission must have these:

-CHECKLIST NOT PROVIDED

