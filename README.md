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
Run notebooks in this order because `data_check.ipynb` depends on environment and package checks first.

### Required Run Order
1. `setup_check.ipynb`
2. `data_check.ipynb`

### Command Examples
```bash

# run notebook 1
python -m jupyter nbconvert --to notebook --execute --inplace setup_check.ipynb

# run notebook 2
python -m jupyter nbconvert --to notebook --execute --inplace data_check.ipynb
```

```bash
# OR launch Jupyter UI and run all cells in order manually
python -m notebook
```

Notes:
- Keep notebook order: `setup_check.ipynb` then `data_check.ipynb`.
- Internet access is required for FastF1 session loading and Jolpica API requests.

## (e) Problems Encountered
Documented issues from this environment and setup flow:

### Problem 1
- Issue: `conda --version` failed because conda was not recognized.
- Cause: Conda is not installed or not available in `PATH` on this machine.
- Fix: Used a virtual environment with `requirements.txt` instead:
	- `python -m venv .venv`
	- `.\.venv\Scripts\Activate.ps1`
	- `pip install -r requirements.txt`

### Problem 2
- Issue: No `environment.yml` was available, so conda-based setup instructions were not runnable.
- Cause: Repository currently provides dependency specification through `requirements.txt` only.
- Fix: Updated setup process to a pip/venv workflow and validated with:
  - `python --version`
  - `pip --version`
  - notebook execution commands in Section (d)

### Problem 3
- Issue: `python -m jupyter nbconvert` failed with `No module named jupyter` after creating the `.venv`.
- Cause: `jupyter` and `nbconvert` were not listed in `requirements.txt`, so they were not installed as part of the standard setup.
- Fix: Added `jupyter>=1.0` and `nbconvert>=7.0` to `requirements.txt`, then ran:
  - `pip install -r requirements.txt`

## (f) Expected Outputs
Successful run indicators:

- `setup_check.ipynb`:
  - Reproducibility header: `Python  : 3.14.2`, `NumPy   : 2.4.3`, `Seed    : 414`
  - Dependency check: `All required packages already installed ✓`
  - 6-row package/version table:
    ```
    package  version
      numpy    2.4.3
     pandas    2.3.3
    sklearn    1.8.0
 matplotlib   3.10.8
    seaborn   0.13.2
     fastf1    3.8.1
    ```
  - FastF1 cache path printed and Git version + recent commits listed.

- `data_check.ipynb`:
  - FastF1 loads 2024 Bahrain Race for 20 drivers with INFO log output.
  - Session metadata: `Session event: Bahrain Grand Prix 2024`, `Session: Race`, `Number of laps in the result: 20`
  - Lap data head (5 rows with VER/Red Bull Racing laps) printed.
  - API request status: `API request successful (code 200).`
  - Standings: `Number of driver standings records: 24`
  - Top 3: Max Verstappen (437 pts), Lando Norris (374 pts), Charles Leclerc (356 pts)

---

## Submission Checklist
- [x] Header is fully filled out
- [x] System info includes exact versions
- [x] Setup commands are complete and tested
- [x] Notebook run order is stated clearly
- [x] At least 2 real problems + fixes documented
- [x] Expected outputs are specific and match actual results

