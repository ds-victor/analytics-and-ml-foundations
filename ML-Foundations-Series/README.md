# 🤖 ML Foundations Series

<div align="center">

### A Complete Introduction to Machine Learning

</div>

---

## 📌 Overview

This repository is dedicated to the **Data Scientist and ML Engineer** paths. It focuses on building, evaluating, and deploying predictive models using a realistic real-estate dataset.

## 📂 Independent Structure

This sub-repository is entirely independent. It contains everything you need for ML Foundations:
- **`data/raw/real_estate_dataset.csv`**: The dataset for this module.
- **`topics/`**: Detailed markdown lessons organized into scientific learning levels.
- **`notebooks/`**: Complete ML Pipeline notebook.
- **`src/`**: Modular Python scripts for training and prediction.
- **`models/`**: Where your trained `.pkl` files will be saved.

## 📚 Course Path

### Level 0-A: Career Clarity
- [Roles & Domains in Data Science](./topics/level-0-a-career-clarity/0a-roles-domains.md)
- [Machine Learning Subfields](./topics/level-0-a-career-clarity/0b-ml-subfields.md)
- [Modern AI Concepts](./topics/level-0-a-career-clarity/0c-modern-ai-concepts.md)

### Level 0-B: ML Fundamentals
- [Supervised vs Unsupervised vs Reinforcement ML](./topics/level-0-b-ml-fundamentals/0d-supervised-unsupervised-reinforcement.md)
- [Regression vs Classification vs Clustering](./topics/level-0-b-ml-fundamentals/0e-regression-classification-clustering.md)
- [Labeled Data vs Unlabeled Data](./topics/level-0-b-ml-fundamentals/0f-labeled-unlabeled-data.md)
- [Structured, Unstructured, Semi-structured Data](./topics/level-0-b-ml-fundamentals/0g-data-types.md)

### Level 1: Technical Foundation
- [IDE vs Jupyter vs Colab](./topics/level-1-technical-foundation/1-ide-jupyter-colab.md)
- [Project Structure](./topics/level-1-technical-foundation/2-project-structure.md)
- [Terminal Basics](./topics/level-1-technical-foundation/3-terminal-basics.md)
- [Virtual Environments](./topics/level-1-technical-foundation/4-virtual-environments.md)

### Level 2: Project Workflow
- [GitHub Fundamentals](./topics/level-2-project-workflow/5-github-fundamentals.md)
- [Train-Test Concepts](./topics/level-2-project-workflow/6-train-test-concepts.md)

### Level 3: Advanced ML
- [Model Selection](./topics/level-3-advanced/7-model-selection.md)
- [Deployment & Streamlit](./topics/level-3-advanced/8-deployment-streamlit.md)

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

2. **Explore the Pipeline Notebook:**
   ```bash
   jupyter notebook notebooks/01_ml_pipeline.ipynb
   ```

3. **Train the Model:**
   ```bash
   python src/train.py
   ```

4. **Run Predictions:**
   ```bash
   python src/predict.py
   ```
