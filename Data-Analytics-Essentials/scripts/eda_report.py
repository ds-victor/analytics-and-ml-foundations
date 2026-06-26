"""
Data Analytics Essentials
Automated EDA Reporting Script

Generates:
- Dataset Summary
- Missing Value Report
- Distribution Charts
- Correlation Heatmap
- Markdown Report

Author: Data Analytics Essentials
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

DATA_PATH = "../data/raw/real_estate_dataset.csv"
REPORT_DIR = Path("../reports")
FIGURE_DIR = REPORT_DIR / "figures"

REPORT_DIR.mkdir(parents=True, exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# BASIC INFORMATION
# --------------------------------------------------

rows, cols = df.shape

missing_values = df.isnull().sum()
total_missing = missing_values.sum()

numeric_cols = df.select_dtypes(include="number").columns

# --------------------------------------------------
# DISTRIBUTION CHARTS
# --------------------------------------------------

print("Generating visualizations...")

for col in numeric_cols[:5]:

    plt.figure(figsize=(7, 4))

    sns.histplot(df[col], kde=True)

    plt.title(f"Distribution of {col}")
    plt.tight_layout()

    plt.savefig(FIGURE_DIR / f"{col}_distribution.png")

    plt.close()

# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------

if len(numeric_cols) > 1:

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    plt.savefig(FIGURE_DIR / "correlation_heatmap.png")

    plt.close()

# --------------------------------------------------
# BUSINESS SUMMARY
# --------------------------------------------------

summary_file = REPORT_DIR / "EDA_SUMMARY.md"

with open(summary_file, "w", encoding="utf-8") as report:

    report.write("# Automated EDA Report\n\n")

    report.write("## Dataset Overview\n\n")
    report.write(f"- Rows: {rows}\n")
    report.write(f"- Columns: {cols}\n")
    report.write(f"- Total Missing Values: {total_missing}\n\n")

    report.write("## Missing Values\n\n")

    for col, value in missing_values.items():
        report.write(f"- {col}: {value}\n")

    report.write("\n## Numeric Summary\n\n")
    report.write(df[numeric_cols].describe().to_markdown())

    report.write("\n\n## Analyst Notes\n\n")

    report.write(
        "Use the generated charts to identify:\n\n"
        "- Key drivers of property prices\n"
        "- Outliers\n"
        "- Correlations\n"
        "- Potential business opportunities\n"
    )

print("=" * 60)
print("EDA REPORT GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"Summary Report : {summary_file}")
print(f"Charts Folder  : {FIGURE_DIR}")
