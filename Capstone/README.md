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
Follow these steps from the repository root. The project may include a top-level `requirements.txt`.

1) Create and activate a virtual environment (recommended):

### Option 1: Setup from `requirements.txt`
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Upgrade pip and install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Notes:
- If a subfolder has its own `requirements.txt`, run `pip install -r <path>/requirements.txt` from the repo root or that folder.
- If you use `venv` created elsewhere, ensure your active interpreter matches the virtualenv's Python.

## (d) Run
You can run notebooks interactively using Jupyter or execute them headlessly.

- Launch Jupyter in the Capstone folder and run manually:
```bash
cd Group/iit414w-lab01-TheUltrakills/Capstone
python -m jupyter lab    # or: python -m notebook
```

- Execute a single notebook non-interactively:
```bash
jupyter nbconvert --to notebook --execute --inplace Group/iit414w-lab01-TheUltrakills/Capstone/Capstone.ipynb
```

- Common troubleshooting:
  - Ensure the virtualenv is activated and dependencies installed.
  - Internet is required for FastF1 session downloads and any API calls.

## (e) Where to find what
- `Capstone/Capstone.ipynb`: main analysis notebook — [Capstone.ipynb](Group/iit414w-lab01-TheUltrakills/Capstone/Capstone.ipynb)
- `Capstone/f1_strategy_lap_level.csv`: lap-level strategy data — [f1_strategy_lap_level.csv](Group/iit414w-lab01-TheUltrakills/Capstone/f1_strategy_lap_level.csv)
- `Capstone/f1_strategy_race_level.csv`: race-level strategy data — [f1_strategy_race_level.csv](Group/iit414w-lab01-TheUltrakills/Capstone/f1_strategy_race_level.csv)
- `Capstone/framing.md`: project framing and decisions — [framing.md](Group/iit414w-lab01-TheUltrakills/Capstone/framing.md)
- `Capstone/PairReviewWorksheet.md`: peer-review worksheet — [PairReviewWorksheet.md](Group/iit414w-lab01-TheUltrakills/Capstone/PairReviewWorksheet.md)
- `Capstone/other_group/`: additional group artifacts — [other_group](Group/iit414w-lab01-TheUltrakills/Capstone/other_group)
- Shared data (repo root): [data/f1_dnf_prediction.csv](data/f1_dnf_prediction.csv) and other datasets in `data/`

## (f) Expected Outputs & Notes
- Successful run: notebooks produce the figures and CSV outputs embedded in the Capstone notebook cells.
- Caching: FastF1 data is stored in `fastf1_cache/` subfolders; having this cache speeds repeated runs.

---

If you'd like, I can also:
- run the Capstone notebook headlessly here and verify it executes without errors,
- or commit these README changes for you.
