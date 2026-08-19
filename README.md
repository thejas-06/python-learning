# My Python for Data Science — Complete Journey

A hands-on learning path covering core Python through the essential data science stack (NumPy, Pandas, Matplotlib, Seaborn) plus practical database work with SQLite3. The notebooks and scripts are structured exercises and worked examples intended for step-by-step practice.

---

## 🎯 Goals
- Teach Python fundamentals (scripts + notebooks) with progressively numbered lessons (01 → 45+).
- Demonstrate data manipulation and analysis using **NumPy** and **Pandas** on real datasets.
- Create clear data visualizations using **Matplotlib** and **Seaborn**.
- Practice database querying and management with **SQLite3**.
- Provide self-contained exercises, challenges, and solutions to build practical skills.

---

## 📁 Repository Structure

- `Python/` — Core Python exercises (`.py`) and notebooks (`.ipynb`) covering fundamentals, OOP, decorators, iterators/generators, logging, multithreading/multiprocessing, and advanced practice tasks.
- `NumPy/` — Array manipulation, vectorized operations, mathematical functions, and practice notebooks.
- `Pandas/` — DataFrames, indexing, cleaning, merging/joining, aggregations, and practice exercises with sample datasets in `Pandas/data/`.
- `Matplotlib/` — Plotting techniques, customizable charts, subplots, and sample exports.
- `Seaborn/` — Statistical data visualization workbooks and charts.
- `SQLite3/` — SQL database queries, table operations, and practice `.db` files (`example.db`, `sales_data.db`).

---

## 🚀 Quick Start (Run Locally)

### 1. Clone the repository
```bash
git clone https://github.com/thejas-06/My-Python-for-Data-Science-Complete-Journey.git
cd My-Python-for-Data-Science-Complete-Journey
```

### 2. Create and activate a virtual environment
- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r Pandas/requirements.txt
pip install jupyterlab matplotlib seaborn
```

### 4. Launch JupyterLab
```bash
jupyter lab
```

### 5. Run standalone Python scripts
```bash
python Python/01_basics_arithmetic.py
python Python/24_args_and_kwargs.py
```

---

## 💡 Notes & Tips
- **Datasets**: Many Pandas notebooks read CSV/XLSX files directly from `Pandas/data/` — keep those files in place when running notebooks.
- **Databases**: The `SQLite3/` directory contains pre-configured sample database files (`example.db`, `sales_data.db`) for immediate testing.

---

## 🤝 Contributing
Contributions, suggestions, and corrections are welcome! Feel free to fork the repository, submit issues, or open a pull request.

---

## 📬 Contact
- **Author**: thejas-06
- **GitHub**: [https://github.com/thejas-06](https://github.com/thejas-06)