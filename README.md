# My Python for Data Science — Complete Journey

A hands-on learning path covering core Python through the essential data‑science stack (NumPy, Pandas, Matplotlib, Seaborn) plus practice with SQLite. The notebooks and scripts are the author's practice exercises and worked examples intended for learners who want runnable examples and step‑by‑step practice.

## Goals
- Teach Python fundamentals (scripts + notebooks) with progressively numbered lessons.
- Demonstrate NumPy and Pandas techniques on real datasets.
- Show plotting with Matplotlib and Seaborn, and simple database work with SQLite.
- Provide self-contained exercises and solutions to build practical skills.

## Contents (top-level)
- Python/        — Numbered core-Python exercises (.py) and notebooks (01 → 42+), OOP, decorators, iterators, short practice tasks and small utilities
- NumPy/         — NumPy introduction and practice notebooks (+ small data/images)
- Pandas/        — Large Pandas notebooks, practice sets, `Pandas/data/` and `Pandas/requirements.txt`
- Matplotlib/    — Matplotlib notebooks, example images
- Seaborn/       — Seaborn workbook (visualization-focused notebook)
- SQLite3/       — SQLite notebooks and example .db files
- README.md      — (this file)
- .gitignore

## Quick start (run locally)
1. Clone:
	git clone https://github.com/thejas-06/My-Python-for-Data-Science-Complete-Journey.git
	cd My-Python-for-Data-Science-Complete-Journey

2. Create a virtual environment and install dependencies:
	python -m venv venv
	# macOS/Linux:
	source venv/bin/activate
	# Windows:
	# venv\Scripts\activate

	# Install core deps (Pandas folder contains a concise list)
	pip install -r Pandas/requirements.txt

	# Optional: ensure notebook & plotting tools
	pip install jupyterlab matplotlib seaborn

3. Open the notebooks:
	jupyter lab
	# then open notebooks in the Python/, NumPy/, Pandas/, Matplotlib/, Seaborn/, or SQLite3/ folders

4. Run small exercises directly:
	python Python/01_basics_arithmetic.py
	python Python/24_args_and_kwargs.py

## Notes & tips
- Many Pandas notebooks read CSV/XLSX files from `Pandas/data/` — keep those files in place when running those notebooks.
- SQLite3 includes sample database files (`example.db`, `sales_data.db`) for queries and exercises.
- If you prefer a single dependency file, consider adding a top-level `requirements.txt` that consolidates `Pandas/requirements.txt` plus jupyterlab/matplotlib/seaborn.

## Contributing
This is a personal learning repo, but contributions (corrections, clearer examples, smaller notebook splits) are welcome. If you plan to reuse or redistribute, please request a license or add one — currently no license file is present.

## Suggested next steps (for repo owner)
- Consolidate dependencies into a top-level `requirements.txt` with pinned versions.
- Split very large notebooks (e.g., Seaborn/ or Matplotlib/ scratch files) into focused examples for readability.
- Add a LICENSE and a small CONTRIBUTING.md if you want external contributions.
- Optionally add Binder/Voila or GitHub Actions to run notebooks or tests.

## Contact
Author: thejas-06 — https://github.com/thejas-06