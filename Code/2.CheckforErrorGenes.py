#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:09:34 2021

@author: panareeboonyuen
"""

import pandas as pd
import numpy as np
expall48_df = pd.read_csv("Normalized_counts_chlamy_EdgeR_2019_data.csv")
gene_names = expall48_df['Genes'].tolist()

x = np.array([0,2,4,6,8,10,10.5,11,11.5,12,14,16,18,20,22,24])
time_points = [x, x, x]

from dynGENIE3 import *


expall48 = expall48_df.to_numpy()
expall48_tp = np.transpose(expall48)

ErrorList = list() #List of genes that give error
ErrorTargetNumber = 0 #Number of those genes

for x in range(1,17282) :
    try:
        ts1 = expall48_tp[1::3,x:x+1]
        ts2 = expall48_tp[2::3,x:x+1]
        ts3 = expall48_tp[3::3,x:x+1]
        TS_data =[ts1,ts2,ts3]
        #print("gene",x, "is a target", end='\n')
        (VIM_ccm_tf, alphas, prediction_score, stability_score, treeEstimators) = dynGENIE3(TS_data,time_points) 
        #print("gene",x, "is a okay")
    except:
        print("error in gene", x)
        ErrorTargetNumber = ErrorTargetNumber+1
        ErrorList.append(x)

#A[4,1:2] means row index 4, column index 1, that's it

for x in ErrorList:
    print(gene_names[x])