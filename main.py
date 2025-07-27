import pandas as pd
import sqlite3

# Create or connect to DB
conn = sqlite3.connect('walmart_sales.db')
cursor = conn.cursor()

# Load CSVs
train = pd.read_csv('Walmart_Sales_SQL_Analysis/data/train.csv')
stores = pd.read_csv('Walmart_Sales_SQL_Analysis/data/stores.csv')
features = pd.read_csv('Walmart_Sales_SQL_Analysis/data/features.csv')

# Save to SQLite
train.to_sql('sales', conn, if_exists='replace', index=False)
stores.to_sql('stores', conn, if_exists='replace', index=False)
features.to_sql('features', conn, if_exists='replace', index=False)

print("✅ Data imported to SQLite database.")
conn.close()
