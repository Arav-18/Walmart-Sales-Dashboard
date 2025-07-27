# Walmart Sales SQL Analysis

## Overview
This project analyzes Walmart's sales data to identify trends, seasonal patterns, and performance by store and department using SQL and Python.

##  Dataset
- `train.csv`: Weekly sales
- `stores.csv`: Store info
- `features.csv`: Temperature, markdowns, fuel price, holidays

##  Tech Stack
- Python
- SQLite
- Pandas
- SQL

##  Key Insights
- Top-performing stores and departments
- Holiday impact on sales
- Monthly trends and seasonality
- Store type-wise performance

## Output Files
- `output_total_sales_by_store.csv`
- `output_monthly_sales.csv`

##  How to Run
```bash
python main.py    # Load CSVs into DB
python test.py    # Run queries & export results
