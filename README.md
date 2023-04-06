# Intern_Chlamydy_Cambridge

This project was an internship projec, carrying out over 2 months, under the supervision of Gitanjali Yadav, Department of Plant Sciences, University of Cambridge.

Please refer to the ReadMe.txt in the folder Input Data for the description of the file in that folder.

The description of the files in the Code folder as the following:

1. For 300 genes, Code for 48 x 354 input matrix: to run dynGENIE3 with improved conditions and Get_link_list Code_1_links_for_300
2. For 17,000 genes, Code to import data and find genes that throw out error CheckforErrorGenes
3. For 17,000 genes, Code to filter them out and to run dynGENIE3 & Get_link_list with names with no max count ToRunAFinalTime_edited
4. For 17,000 genes, Code for filtering Target by CCM genes and Regulator by CCM and TF genes FilteringInterestedGenes

For source file (they all similar, except the part in Get_link_list function, shown in the table below)
1. dynGENIE3.py: original dynGENIE3 file from Github 
2. dynGENIE3_mod.py: same with the original file, just adding comments and some code that enable tracking the process (green highlighted)
3. dynGENIE3_mod_for.py: change ndenumerate to nested for loop (yellow highlighted)

Note: why many source file? for 48 x 354 input matrix, any source files can be used ( though dynGENIE3.py is not recommended), but for the larger 48 x 17,777 input matrix, the dynGENIE3_mod_for.py is recommended as it is faster


Summary Table
![image](https://user-images.githubusercontent.com/83533049/227964172-76897dfa-3951-4cad-b6ed-d0dd0d06ec31.png)




