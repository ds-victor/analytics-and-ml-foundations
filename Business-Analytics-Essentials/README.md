# 📈 Business Analytics Essentials

<div align="center">

### Learn to Bridge the Gap Between Business and Data

</div>

---

## 📌 Overview

This repository is dedicated to the **Business Analyst** path. It focuses on defining KPIs, data-driven decision-making, and translating business problems into data requirements using a realistic real-estate dataset.

## 📂 Independent Structure

This sub-repository is entirely independent. It contains everything you need for Business Analytics:
- **`data/raw/real_estate_dataset.csv`**: The dataset for this module.
- **`topics/`**: Structured lessons organized by learning levels.
- **`notebooks/`**: BI Data preparation notebook.
- **`scripts/`**: Scripts to aggregate and prepare data.
- **`app/`**: An interactive Streamlit dashboard.

## 📚 Course Path

### Level 0: Career Clarity
- [The Business Analyst Role](./topics/level-0-career-clarity/0a-business-analyst-role.md)

### Level 1: Technical Foundation
- [Project Structure for BAs](./topics/level-1-technical-foundation/1-project-structure-ba.md)
- [GitHub for Business Analysts](./topics/level-1-technical-foundation/5-github-fundamentals-ba.md)

### Level 2: Core Analytics
- [Business Metrics & KPIs](./topics/level-2-core-analytics/a-business-metrics-kpis.md)
- [Data-Driven Decision Making](./topics/level-2-core-analytics/b-data-driven-decision-making.md)
- [Basic Data Analysis for Business](./topics/level-2-core-analytics/c-basic-data-analysis-business.md)

### Level 3: BI & Stakeholders
- [Data Visualization for Stakeholders](./topics/level-3-bi-stakeholders/d-data-visualization-stakeholders.md)
- [Business Intelligence Platforms](./topics/level-3-bi-stakeholders/e-business-intelligence-platforms.md)

---

## 🏁 Assessment & Resources
- [Cheat Sheet](./cheat-sheet.md)
- [Interview Questions](./interview-questions.md)
- [Final Quiz](./final-quiz.md)

## 🚀 Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare the Data:**
   ```bash
   python scripts/prepare_bi_data.py
   ```

3. **Launch the Dashboard:**
   ```bash
   streamlit run app/dashboard_app.py
   ```
