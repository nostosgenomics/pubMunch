# script to collect results from multiple crawls
import pandas as pd
import os
import sqlite3

# read-in list of ids to crawl
path_to_split_crawls = os.getcwd() + '/40kCrawl/SplitCrawl/'
nr_of_crawls = len(os.listdir(path_to_split_crawls))
articleMeta_df = pd.DataFrame()
docStatus_df = pd.DataFrame()
articles_df = pd.DataFrame()

for i in range(0, nr_of_crawls):
    # collect ArticleMeta data
    this_articleMeta = path_to_split_crawls + 'crawl' + str(i) + '/articleMeta.tab'
    this_articleMeta_df = pd.read_csv(this_articleMeta, sep='\t')
    articleMeta_df = pd.concat([articleMeta_df, this_articleMeta_df])

    # collect docStatus data
    this_docStatus = path_to_split_crawls + 'crawl' + str(i) + '/docStatus.tab'
    this_docStatus_df = pd.read_csv(this_docStatus, sep='\t', header=None)
    docStatus_df = pd.concat([docStatus_df, this_docStatus_df])

    # collect articles data
    path_to_db = path_to_split_crawls + 'crawl' + str(i) + '/articles.db'
    con = sqlite3.connect(path_to_db)

    # Run SQL
    sql_query = pd.read_sql('SELECT * FROM articles', con)

    # Convert SQL to DataFrame
    this_articles_df = pd.DataFrame(sql_query)
    articles_df = pd.concat([articles_df, this_articles_df])

# save dfs to file
# Article Meta data
file_path = path_to_split_crawls + 'articleMeta.csv'
articleMeta_df.to_csv(file_path, encoding='utf-8')

# Document crawler status data
file_path = path_to_split_crawls + 'docStatus.csv'
docStatus_df.to_csv(file_path, encoding='utf-8')

# Articles data
file_path = path_to_split_crawls + 'articles.csv'
articles_df.to_csv(file_path, encoding='utf-8')

