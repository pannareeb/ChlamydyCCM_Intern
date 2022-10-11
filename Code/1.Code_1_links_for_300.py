
import pandas as pd
import numpy as np
import sklearn; sklearn.show_versions()

#import expression data of CCM genes and TF genes (48 samples x 354 genes), which was previously wrangled in R
expall48_ccm_tf_fromR_df = pd.read_csv("expall48_ccm_tf_fromR.csv") #read by pandas

#create gene_names
gene_names = expall48_ccm_tf_fromR_df['Genes'].tolist()#indicate Cre ID as gene names

#create time_points
x = np.array([0,2,4,6,8,10,10.5,11,11.5,12,14,16,18,20,22,24]) #as a set of time points used in one time-series experiment
time_points = [x, x, x]#we have data from 3 experiments, so need to match data with corresponding time points

#create TS_data
expall48_ccm_tf_fromR = expall48_ccm_tf_fromR_df.to_numpy()
expall48_ccm_tf_tp = np.transpose(expall48_ccm_tf_fromR)
ts1 = expall48_ccm_tf_tp[2::3,:] #data from 1st experiment
ts2 = expall48_ccm_tf_tp[3::3,:] #data from 2nd experiment
ts3 = expall48_ccm_tf_tp[4::3,:] #data from 3rd experiment
TS_data =[ts1,ts2,ts3] #collate data to form 48 samples

#run dynGENIE3 
#with added optional arguments gene_names (to have Cre ID written) and k = "all" (to improve score)
from dynGENIE3 import *
(VIM_ccm_tf, alphas, prediction_score, stability_score, treeEstimators) = dynGENIE3(TS_data,time_points, gene_names=gene_names, k = 'all')
#get all the links 
get_link_list(VIM_ccm_tf, gene_names=gene_names, file_name= "ranking_improvedscore_allranks.txt")


#to write VIM_ccm_tf, for future use if needed
import csv
with open('VIM_ccm_tf.csv', 'w', newline = '') as myfile:
    writer = csv.writer(myfile)
    writer.writerows(VIM_ccm_tf)

