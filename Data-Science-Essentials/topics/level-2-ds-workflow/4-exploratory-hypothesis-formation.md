# Topic 4: Exploratory Hypothesis Formation

## Overview
Before modeling, we must explore. Exploratory Data Analysis (EDA) in data science isn't just about plotting; it's about forming testable hypotheses about why certain features affect our target.

## Hypothesis Formation
Instead of "Does square footage matter?", ask:
- **Hypothesis:** "There is a positive linear relationship between `area_sqft` and `price` because larger homes offer more utility."
- **Hypothesis:** "Properties in 'Central' have a higher price per square foot than those in 'South' due to proximity to business hubs."

## Key EDA Steps
1. **Univariate Analysis:** Looking at the distribution of `price` (is it skewed?).
2. **Bivariate Analysis:** Scattering `area_sqft` vs. `price`.
3. **Multivariate Analysis:** How does `region` interact with `area_sqft` to influence `price`?

## Mermaid Diagram: EDA to Hypothesis
```mermaid
graph LR
    A[Visualise Data] --> B[Identify Patterns]
    B --> C[Form Hypothesis]
    C --> D[Validation through Modeling]
```

## Deliverables
Check `notebooks/hypothesis_formation.ipynb` for the interactive exploration of our real estate dataset.

## Summary
EDA gives you the intuition needed to build better models. Never skip this step!
