
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:11:11 2021

@author: panareeboonyuen
"""
import os
os.getcwd()

os.chdir('/Users/panareeboonyuen/Desktop/Python_Try_folder')
os.getcwd()

import sklearn; sklearn.show_versions()
import pandas as pd
import numpy as np
import pickle 
import time

#import all-gene expression data
expall48_df = pd.read_csv("Normalized_counts_chlamy_EdgeR_2019_data.csv")

#create gene_names (before)
gene_names_bf = expall48_df['Genes'].tolist() #indicate that column "Gene" is the gene_names

# import the list of genes that throw out error #Errorlist contain the number that are the indices of the genes we do not want to consider
ErrorList = [2622, 
 3286,
 3933,
 4264,
 4725,
 4903,
 5870,
 7082,
 7083,
 7084,
 7085,
 7279,
 7340,
 7636,
 8233,
 8577,
 10828,
 11289,
 11300,
 11308,
 11328,
 11568,
 11614,
 11792,
 12665,
 13105,
 13606,
 13814,
 14050,
 14301,
 14452,
 15595,
 15779,
 15782,
 15783,
 15785,
 15788,
 15798,
 15806,
 15837,
 16478,
 17126,
 17149,
 17188,
 17212,
 17214
]

#delete the member of the list gene_names_bf that has the same order with the number in the error list 
for i in sorted(ErrorList, reverse=True): 
    del gene_names_bf[i]   #now we get gene_names_bf that has been filtered 
gene_names = gene_names_bf 
expall48_filtered = expall48_df.drop(ErrorList) #drop the row of which the index is in the Errorlist


#create time_points
x = np.array([0,2,4,6,8,10,10.5,11,11.5,12,14,16,18,20,22,24]) #as a set of time points used in one time-series experiment
time_points = [x, x, x]#we have data from 3 experiments, so need to match data with corresponding time points

#create TS_data
expall48 = expall48_filtered.to_numpy()
expall48_tp = np.transpose(expall48)
ts1 = expall48_tp[1::3,:]
ts2 = expall48_tp[2::3,:]
ts3 = expall48_tp[3::3,:]
TS_data =[ts1,ts2,ts3]
 
from dynGENIE3_mod_for import *

#to run dynGENIE3
start= time.time()
(VIM_Filtered_withName, alphas, prediction_score, stability_score, treeEstimators) = dynGENIE3(TS_data,time_points, gene_names=gene_names)
end = time.time()
print ("run dyngenie3 for", (end-start), "sec")

#to get link lists of all genes
start2= time.time()
get_link_list(VIM_Filtered_withName, gene_names=gene_names,file_name='rankingAll_Filtered_withName')
end2 = time.time()
print ("run getlink for", (end2-start2), "sec")



