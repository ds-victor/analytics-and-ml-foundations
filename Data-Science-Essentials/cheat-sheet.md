# Data Science Cheat Sheet

A quick reference guide for the end-to-end Data Science lifecycle, feature engineering, and evaluation.

## 1. DS Workflow (The 5 Levels)
1.  **Problem Framing:** Define SMART objectives and technical metrics.
2.  **Technical Foundation:** Environment setup, Git, and Project structure.
3.  **DS Workflow:** EDA, Hypothesis Testing, and Feature Engineering.
4.  **Modeling Optimization:** Model selection, tuning, and tracking.
5.  **Business & Ethics:** Translation of results to ROI and Fairness audits.

## 2. Feature Engineering Techniques
- **Encoding:** One-Hot (categorical) or Target Encoding.
- **Scaling:** StandardScaler (mean=0, std=1) or MinMaxScaler (0 to 1).
- **Transformation:** Log-transform for skewed numerical features.
- **Creation:** Interaction terms (e.g., `price * sqft`) or Domain-specific ratios.

## 3. Regression Metrics
- **MAE (Mean Absolute Error):** Easy to explain; all errors weighted equally.
- **RMSE (Root Mean Squared Error):** Penalizes large errors heavily.
- **R² (Coefficient of Determination):** Percentage of variance explained by the model (0 to 1).
- **Residual Plot:** Check for randomness; patterns suggest model bias.

## 4. Experiment Tracking (MLflow)
- **Parameters:** Input configurations (e.g., `max_depth`, `learning_rate`).
- **Metrics:** Performance outputs (e.g., `RMSE`, `Validation Accuracy`).
- **Artifacts:** Saved models (`.pkl`), plots, and data snapshots.

## 5. Ethics & Fairness
- **Demographic Parity:** Similar average predictions across different groups.
- **Disparate Impact Ratio:** Ratio of favorable outcome rates between groups (threshold typically > 0.8).
- **Proxy Variables:** Features that indirectly reveal sensitive attributes (e.g., Zip Code -> Race).
