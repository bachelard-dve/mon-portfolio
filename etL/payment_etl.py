import mysql.connector
import pandas as pd

# 1. EXTRACT
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TON_MOT_DE_PASSE",
    database="sakila"
)
query = "SELECT customer_id, amount, payment_date FROM payment"
df = pd.read_sql(query, conn)

# 2. TRANSFORM
df_top = df.groupby('customer_id')['amount'].sum().reset_index()
df_top = df_top.sort_values(by='amount', ascending=False)
df_top.rename(columns={'amount': 'total_depense'}, inplace=True)

# 3. LOAD
df_top.to_csv('top_clients.csv', index=False)
print(df_top.head())

conn.close()
