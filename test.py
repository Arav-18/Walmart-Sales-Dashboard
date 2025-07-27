import pandas as pd
import sqlite3

conn = sqlite3.connect('walmart_sales.db')

# Query 1: Total Sales by Store
q1 = '''
SELECT Store, SUM(Weekly_Sales) AS Total_Sales
FROM sales
GROUP BY Store
ORDER BY Total_Sales DESC
'''
df1 = pd.read_sql_query(q1, conn)
df1.to_csv("output_total_sales_by_store.csv", index=False)

# Query 2: Monthly Sales Trend
q2 = '''
SELECT SUBSTR(Date, 1, 7) AS Month, SUM(Weekly_Sales) AS Monthly_Sales
FROM sales
GROUP BY Month
ORDER BY Month
'''
df2 = pd.read_sql_query(q2, conn)
df2.to_csv("output_monthly_sales.csv", index=False)

print("✅ Queries executed and CSVs saved.")
conn.close()
