# script to export record from articles.db
import sqlite3
import pandas as pd

# Connect to the database
path_to_crawl = './RocioCrawl/'
db_name = 'articles.db'
path_to_db = path_to_crawl + db_name
con = sqlite3.connect(path_to_db)

# Run SQL
sql_query = pd.read_sql('SELECT * FROM articles', con)

# Convert SQL to DataFrame
df = pd.DataFrame(sql_query)
print(df)

# save df to file
df_name = path_to_crawl + db_name.split('.')[0]+'.csv'
df.to_csv(df_name, encoding='utf-8')
