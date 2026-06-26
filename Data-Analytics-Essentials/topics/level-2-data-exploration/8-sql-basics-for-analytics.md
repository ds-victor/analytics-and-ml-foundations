# SQL Basics for Analytics

## 1. Why This Matters
SQL is the most important skill for a data analyst. Most company data lives in databases.

## 2. Core Concept
SQL (Structured Query Language) lets you retrieve, filter, aggregate, and join data. Core commands: `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN`.

```mermaid
graph LR
    Sel[SELECT Columns] --> Fr[FROM Table]
    Fr --> Wh[WHERE Filter]
    Wh --> Grp[GROUP BY Category]
    Grp --> Hav[HAVING Filter Agg]
    Hav --> Ord[ORDER BY Sort]
```

## 3. Real-World Examples
• `SELECT AVG(price) FROM houses WHERE city = 'Austin'`
• `SELECT property_type, COUNT(*) FROM houses GROUP BY property_type`
• `SELECT * FROM houses JOIN sales ON houses.id = sales.house_id`

## 4. Comparison
| SQL clause | Purpose | Example |
|------------|---------|---------|
| SELECT | Choose columns | `SELECT price, area` |
| WHERE | Filter rows | `WHERE bedrooms >= 3` |
| GROUP BY | Aggregate groups | `GROUP BY property_type` |
| JOIN | Combine tables | `LEFT JOIN agents` |
| ORDER BY | Sort | `ORDER BY price DESC` |

## 5. Decision Tree
1. Need all rows? → `SELECT *`
2. Need only certain rows? → `WHERE`
3. Need summary (average, count)? → `GROUP BY`
4. Need data from multiple tables? → `JOIN`

## 6. Common Misconceptions
• SQL is not case-sensitive for keywords (but often uppercase is convention).
• `NULL` is not zero or empty – it's unknown. Use `IS NULL` not `= NULL`.

## 7. FAQ
**Q: How long to learn SQL?** Basics in a weekend, proficiency in 2-3 weeks.
**Q: What's the difference between `INNER JOIN` and `LEFT JOIN`?** Inner returns only matching rows; left returns all rows from left table, with NULL for non-matching.

## 8. Next Steps
Consider learning statistical analysis (optional) or dashboarding next.

## 9. Running Example
We'll load the real estate CSV into a SQLite database. Then you'll write queries to answer questions like: average price by property type, most expensive neighborhoods, number of sales per year, and correlation between pool and price.

## 10. Interview Prep
1. Write a query to get the top 5 most expensive houses sold in 2023.
2. What's the difference between `WHERE` and `HAVING`?

