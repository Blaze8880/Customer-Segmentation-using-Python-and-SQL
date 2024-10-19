import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('customer_database.db')

# Run SQL query
query = """
SELECT 
    c.customer_id, 
    c.name, 
    COUNT(t.transaction_id) AS total_purchases,
    SUM(t.amount) AS total_spent,
    MAX(t.transaction_date) AS last_purchase_date
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.name;
"""

# Load query results into Pandas DataFrame
df = pd.read_sql(query, conn)
conn.close()

# Preprocessing for segmentation (e.g., normalize the data)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['total_purchases', 'total_spent']] = scaler.fit_transform(df[['total_purchases', 'total_spent']])
