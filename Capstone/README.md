# IIT414W Hito 1

## (a) Header
- Full Names: `Martín Gottschalk, Marcial Ibañez`
- GitHub Usernames: `Gottch7897, MarcialIbanezS`
- Course Code: `IIT414W`
- Date: `2026-05-06`

## (b) System Info
- Operating System (name + version): `Microsoft Windows 11 Home Single Language (10.0.26200)`
- Python Version: `Python 3.14.2`
- Package Manager Version:
  - `pip --version`: `pip 25.3`


## (c) Install
Follow these steps from the repository root on Windows 11. The project may include a top-level `requirements.txt`.

1) Create and activate a virtual environment (recommended):

### Option 1: Setup from `requirements.txt`
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

2) Upgrade pip and install dependencies:
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Notes:
- If a subfolder has its own `requirements.txt`, run `pip install -r <path>\requirements.txt` from the repo root or that folder.
- If you use `venv` created elsewhere, ensure your active interpreter matches the virtualenv's Python.
- If PowerShell blocks activation scripts, re-open it as your user and run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once.

## (d) Run
You can run notebooks interactively using Jupyter or execute them headlessly.

- Launch Jupyter in the Capstone folder and run manually:
```powershell
cd Capstone
python -m jupyter lab    # or: python -m notebook
```

- Execute a single notebook non-interactively:
```powershell
jupyter nbconvert --to notebook --execute --inplace Capstone.ipynb
```

- Common troubleshooting:
  - Ensure the virtualenv is activated and dependencies installed.
  - Internet is required for FastF1 session downloads and any API calls.

## (e) Where to find what
- `Capstone/Capstone.ipynb`: main analysis notebook — [Capstone.ipynb](Capstone/Capstone.ipynb)
- `Capstone/f1_strategy_lap_level.csv`: lap-level strategy data — [f1_strategy_lap_level.csv](Capstone/f1_strategy_lap_level.csv)
- `Capstone/f1_strategy_race_level.csv`: race-level strategy data — [f1_strategy_race_level.csv](Capstone/f1_strategy_race_level.csv)
- `Capstone/framing.md`: project framing and decisions — [framing.md](Capstone/framing.md)
- `Capstone/PairReviewWorksheet.md`: peer-review worksheet — [PairReviewWorksheet.md](Capstone/PairReviewWorksheet.md)
- `Capstone/other_group/`: additional group artifacts — [other_group](Capstone/other_group)
- Shared data (repo root): datasets in the repository root and related folders

## (f) Expected Outputs & Notes
- Successful run: notebooks produce the figures and CSV outputs embedded in the Capstone notebook cells.
- Caching: FastF1 data is stored in `fastf1_cache/` subfolders; having this cache speeds repeated runs.

---

