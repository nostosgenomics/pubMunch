# script to export record from articles.db
import sqlite3
import pandas as pd

# Connect to the database
con = sqlite3.connect('./myCrawl/articles.db')

# Run SQL
sql_query = pd.read_sql('SELECT * FROM articles', con)

# Convert SQL to DataFrame
df = pd.DataFrame(sql_query)
print(df)
