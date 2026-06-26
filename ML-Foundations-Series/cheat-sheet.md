# Machine Learning Foundations Cheat Sheet

A quick reference guide for ML paradigms, algorithms, and evaluation concepts.

## 1. ML Paradigms
- **Supervised:** Learning from labeled data (X, y).
- **Unsupervised:** Finding patterns in unlabeled data (X only).
- **Reinforcement:** Learning from actions and rewards in an environment.

## 2. Common Algorithms
- **Regression:** Linear Regression, Decision Tree, Random Forest.
- **Classification:** Logistic Regression, SVM, Random Forest, XGBoost.
- **Clustering:** K-Means, DBSCAN.
- **Dimensionality Reduction:** PCA (Principal Component Analysis).

## 3. Bias-Variance Trade-off
- **High Bias (Underfitting):** Model is too simple; performs poorly on both train and test.
- **High Variance (Overfitting):** Model is too complex; performs great on train but poorly on test.
- **Ideal:** Balanced complexity that generalizes to unseen data.

## 4. Evaluation Checklist
- **Train-Test Split:** Usually 80/20 or 70/30.
- **Cross-Validation:** K-fold (usually K=5 or 10) to ensure robust performance.
- **Random State:** Set a seed (e.g., `42`) for reproducibility.
- **Metrics:** Accuracy (classification), MSE/RMSE (regression), Silhouette Score (clustering).

## 5. Data Types Reference
- **Structured:** Tabular data (CSV, SQL).
- **Semi-structured:** JSON, XML.
- **Unstructured:** Text, Images, Audio.
- **Labeled:** Has target variable.
- **Unlabeled:** No target variable.
