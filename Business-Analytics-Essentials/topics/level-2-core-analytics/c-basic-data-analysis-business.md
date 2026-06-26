# Basic Data Analysis for Business

## 1. Why This Matters
BAs often need to analyse data themselves – not just request reports. Basic Excel skills go a long way.

## 2. Core Concept
Common analysis techniques for BAs:

```mermaid
graph LR
    Raw[Raw Data] --> Clean[Cleaning/Merging]
    Clean --> Pivot[Summarizing/PivotTables]
    Pivot --> Viz[Visualization/Charts]
    Viz --> Insight[Business Insight]
```

- **PivotTables**: summarise and aggregate data.
- **VLOOKUP/XLOOKUP**: merge data from different tables.
- **Conditional formatting**: highlight outliers.
- **Charts**: visualise trends.
- **Basic statistics**: average, median, percentiles, correlation.

## 3. Real-World Examples
• Use a PivotTable to calculate average sales by region.
• Use XLOOKUP to add customer segment to a sales table.
• Create a line chart to show monthly revenue.

## 4. Comparison
| Task | Excel tool | When to use |
|------|------------|-------------|
| Group and summarise | PivotTable | Large datasets, many categories |
| Combine tables | XLOOKUP, Power Query | Merging data from different sources |
| Find top/bottom | Sort, filter | Ranking |
| Calculate % change | Formula | Time series comparison |

## 5. Decision Tree
1. Need to sum/average by category? → PivotTable.
2. Need to look up values from another table? → XLOOKUP.
3. Need to see distribution? → Histogram (Analysis ToolPak).
4. Need to find correlation? → CORREL function.

## 6. Common Misconceptions
• You don't need to be an Excel wizard – a handful of functions cover 80% of BA work.
• PivotTables are not scary – practice with small data.

## 7. FAQ
**Q: Do I need to learn Python as a BA?** Not essential, but helpful for advanced analysis.
**Q: What about Power BI?** Yes, many BAs use Power BI for visualisation.

## 8. Next Steps
Read about data visualisation for stakeholders.

## 9. Running Example
You'll open the real estate dataset in Excel. Use PivotTables to find average price by property type and year. Use XLOOKUP to add a 'luxury' flag (price > $500k). Create a chart showing the trend of days on market over time.

## 10. Interview Prep
1. How would you calculate the average order value per month in Excel?
2. Explain how to use VLOOKUP.

