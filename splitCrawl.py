# script to split/parallelize a single crawl into smaller ones by creating crawls sub-folders
import pandas as pd
import numpy as np
import os

# flags
nr_of_crawls = 10

# read-in list of ids to crawl
path_to_split_crawls = './40kCrawl/SplitCrawl/'
id_filename = 'rare_disease_pmids.txt'
path_to_id = './sources/' + id_filename
id_list = pd.read_csv(path_to_id, header=None)
id_splits = np.linspace(0, len(id_list), nr_of_crawls+1).round()

# check if output folder(s) exist
if not os.path.exists(path_to_split_crawls):
    os.mkdir(path_to_split_crawls)

# create separate folders for each id split
list_nr = 0
for i in id_splits[0:-1]:
    print('Processing split: ' + str(list_nr))
    new_list = id_list.loc[list_nr:id_splits[list_nr+1]]
    path_to_folder = path_to_split_crawls + 'crawl' + str(list_nr) + '/'
    os.mkdir(path_to_folder)
    new_filename = path_to_folder + 'pmids.txt'
    new_list.to_csv(new_filename, index=None, header=None)
    list_nr += 1
