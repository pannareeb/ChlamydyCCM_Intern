#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 20:38:13 2021

@author: panareeboonyuen
"""

import pandas as pd
import os
import sklearn; sklearn.show_versions()
import numpy as np
import pickle 
import time

os.getcwd()

os.chdir('/Users/panareeboonyuen/Desktop/Python_Try_folder')
os.getcwd()

#create name lists for filtering
NameCCM = pd.read_csv("ExpCCM2019csv-Copy.csv")["ID"]  
NameTarget = list(NameCCM) #target can only be CCM genes
NameTF = pd.read_csv("updated_TF_list_Citu_June2k20.csv")["ID"] #import a TF list of around 700 genes 
NameRegulator = NameTarget + list(NameTF) #regulator can be both CCM and TF

#it takes long with all 3 billions links, so could be better if choose a random cut-off 
#so with just a part of a large file, it is faster (0.001 cut off was used in this case)
#step 1 filtered by score more than 0.001
Dx =[]
j= 0
with open('rankingAll_withName.txt') as f: #open a ranking all file
    for line in f.readlines(): #read each line
        Ax = line.split() #split line into words -> here we get 3 words: Regulator, target, and score, respectively
        if float(Ax[2]) >= 0.00100: #compare score with 0.001
            Cx = np.array(Ax) 
            Dx.append(Cx) #we produce a list Dx containing the numpy arrays, each containing 
            j= j+1
            if j%100 == 0:
                print(Dx[-1], j)
        else:
            break
#step 2 filtered by target:CCM only
Dx2 = []
k = 0       
for i in range(len(Dx)):
    for name in NameTarget:
            if Dx[i][1] == name:
                k = k+1
                if k%100 == 0:
                    print("found CCM gene", name, "as a target order", k) #to check the progress
                Dx2.append(Dx)
                break
Ex = np.array(Dx)
#step 3 filtered by regilator:CCM and TF
for i in range(len(Ex)):
    for name in NameRegulator:
        if (Ex[i,0]) == name:
            print("found Tf or CCM gene", name, "as a regulator")
            F.append(Ex[i])

#save the final link list as pickle
with open('filtered_1', 'wb') as fp:
    pickle.dump(F,fp)
    
#load the final list, member 193338 links    
with open('filtered_1', 'rb') as fpp:
    Sorted_rank = pickle.load(fpp)

Sorted_rank_np = np.array(filtered)
Sorted_rank_df = pd.DataFrame(filtered)
Sorted_rank.columns = ["Reg","Tar","Score"]

#write the CCM-TF-link by switching position
Sorted_rank_df2 = Sorted_rank_dfdf[["Tar","Reg","Score"]]
Sorted_rank_df3 = Sorted_rank_df3.sort_values(by=['Tar', 'Score'])

with open('Sorted_rank_final_df', 'wb') as fppp:
    pickle.dump(Sorted_rank_df3,fppp)