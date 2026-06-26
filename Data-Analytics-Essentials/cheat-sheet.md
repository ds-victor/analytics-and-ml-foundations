# Data Analytics Cheat Sheet

A quick reference guide for SQL, Python (Pandas), and the Data Analytics lifecycle.

## 1. SQL Essential Clauses
```sql
SELECT columns           -- Choose fields
FROM table               -- Source data
JOIN other_table ON id   -- Combine data
WHERE condition          -- Filter rows (pre-agg)
GROUP BY category        -- Aggregate data
HAVING condition         -- Filter groups (post-agg)
ORDER BY column DESC     -- Sort results
LIMIT 10;                -- Top N results
```

## 2. Pandas Essentials (Python)
```python
import pandas as pd
df = pd.read_csv('file.csv')    # Load data
df.head()                       # Preview first 5 rows
df.info()                       # Data types and missing counts
df.describe()                   # Summary stats (mean, std, etc.)
df.isnull().sum()               # Check for missing values
df.dropna()                     # Remove missing
df.fillna(value)                # Fill missing
df[df['col'] > 50]              # Filter rows
df.groupby('cat')['val'].mean() # Aggregate
```

## 3. Terminal Quick Start
- `ls` / `dir`: List files
- `cd folder`: Change directory
- `pip install package`: Install libraries
- `jupyter notebook`: Launch interactive environment
- `python script.py`: Run script

## 4. Data Cleaning Steps
1.  **Format Check:** Ensure dates are datetime objects and numbers aren't strings.
2.  **Deduplication:** Remove exact or near-duplicates.
3.  **Missing Values:** Decide to Drop, Impute, or Flag.
4.  **Outliers:** Use Boxplots to identify; decide to remove or transform.
5.  **Standardization:** Ensure consistent spelling for categorical values.

## 5. Statistical Terms
- **Mean:** Average value.
- **Median:** Middle value (Robust to outliers).
- **p-value:** Probability of observing data if null hypothesis is true (usually < 0.05 is significant).
- **Correlation:** -1 to +1 relationship strength (Correlation != Causation).
