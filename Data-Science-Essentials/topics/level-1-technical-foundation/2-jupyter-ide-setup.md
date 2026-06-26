# Topic 2: Jupyter & IDE Setup

## Overview
A professional environment is crucial for reproducibility. We use Jupyter Notebooks for exploration and Python scripts for production-grade code.

## Key Tools
- **JupyterLab/Notebook:** Best for interactive EDA and visualization.
- **VS Code:** Recommended IDE for writing reusable scripts and debugging.
- **Virtual Environments:** Using `venv` to isolate dependencies.

## Reproducibility Checklist
- [ ] Use a `requirements.txt` with pinned versions.
- [ ] Set a global random seed for all libraries (`numpy`, `sklearn`).
- [ ] Use relative paths for data loading.
- [ ] Include a configuration file (`config.yaml`).

## Setup Walkthrough
1. **Create Venv:** `python -m venv venv`
2. **Activate:** `source venv/bin/activate`
3. **Install:** `pip install -r requirements.txt`

## Working with Paths
Avoid hardcoded paths like `C:\Users\Project\data`. Use `pathlib` or relative paths:
```python
import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "raw" / "real_estate_dataset.csv"
df = pd.read_csv(DATA_PATH)
```

## Summary
By setting up correctly, you ensure that your code works on your colleague's machine exactly as it does on yours.
