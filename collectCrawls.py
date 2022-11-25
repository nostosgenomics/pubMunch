# script to collect results from multiple crawls
import pandas as pd
import os


# read-in list of ids to crawl
path_to_split_crawls = os.getcwd() + '/SplitCrawl/'
nr_of_crawls = len(os.listdir(path_to_split_crawls))
articleMeta_df = pd.DataFrame()
docStatus_df = pd.DataFrame()

for i in range(0, nr_of_crawls):
    # collect ArticleMeta data
    this_articleMeta = path_to_split_crawls + 'crawl' + str(i) + '/articleMeta.tab'
    this_articleMeta_df = pd.read_csv(this_articleMeta, sep='\t')
    articleMeta_df = pd.concat([articleMeta_df, this_articleMeta_df])
    # collect docStatus data
    this_docStatus = path_to_split_crawls + 'crawl' + str(i) + '/docStatus.tab'
    this_docStatus_df = pd.read_csv(this_docStatus, sep='\t')
    docStatus_df = pd.concat([docStatus_df, this_docStatus_df])

