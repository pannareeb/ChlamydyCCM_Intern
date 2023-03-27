# Intern_Chlamydy_Cambridge
Details
For 300
1.	Code for 48 x 354 input matrix: to run dynGENIE3 with improved conditions and Get_link_list Code_1_links_for_300

For 17,000
2.	Code to import data and find genes that throw out error CheckforErrorGenes
3.	Code to filter them out and to run dynGENIE3 & Get_link_list with names with no max count ToRunAFinalTime_edited
4.	Code for filtering Target by CCM genes and Regulator by CCM and TF genes FilteringInterestedGenes

For source file (they all similar, except the part in Get_link_list function, shown in the table below)
5.	dynGENIE3.py: original dynGENIE3 file from Github 
6.	dynGENIE3_mod.py: same with the original file, just adding comments and some code that enable tracking the process (green highlighted)
7.	dynGENIE3_mod_for.py: change ndenumerate to nested for loop (yellow highlighted)
Note: why many source file? for 48 x 354 input matrix, any source files can be used ( though dynGENIE3.py is not recommended), but for the larger 48 x 17,777 input matrix, the dynGENIE3_mod_for.py is recommended as it is faster

dynGENIE3.py	dynGENIE3_mod.py	dynGENIE3_mod_for.py
  # Get the non-ranked list of regulatory links
    vInter = [(i,j,score) for (i,j),score in ndenumerate(VIM) if i in input_idx and i!=j]
        
    # Rank the list according to the weights of the edges
    vInter_sort = sorted(vInter,key=itemgetter(2),reverse=True) #sort vInter by score
    nInter = len(vInter_sort)
    
    # Random permutation of edges with score equal to 0
    flag = 1
    i = 0
    while flag and i < nInter:
        (TF_idx,target_idx,score) = vInter_sort[i]
        if score == 0:
            flag = 0
        else:
            i += 1
            
    if not flag:
        items_perm = vInter_sort[i:]
        items_perm = random.permutation(items_perm)
        vInter_sort[i:] = items_perm
        
    # Write the ranked list of edges
    nToWrite = nInter
    if isinstance(maxcount,int) and maxcount >= 0 and maxcount < nInter:
        nToWrite = maxcount
	 # Get the non-ranked list of regulatory links
    vInter = list()
    for (i,j),score in ndenumerate(VIM) :
        if i in input_idx and i!=j:
            vInter.append((i,j,score))
            if i%100 == 0:
                print(vInter[-1])
   
      #if regulator = 'all' then input_idx will be 0 to ngenes-1 -> so i will be each of thme in turn
     # (0,0), 0.4353463 -> (0,0,  0.4353463)
     # index, x in np.ndenumerate(a) produces (0, 0) 1 
     # may be I could add the progress bar here or just print(vInter[-1]))
    
   
    # Rank the list according to the weights of the edges
    vInter_sort = sorted(vInter,key=itemgetter(2),reverse=True) #sort vInter by score
    nInter = len(vInter_sort)
    
    # Random permutation of edges with score equal to 0
    flag = 1
    i = 0
    while flag and i < nInter:
        (TF_idx,target_idx,score) = vInter_sort[i]
        if score == 0:
            flag = 0
        else:
            i += 1
            
    if not flag:
        items_perm = vInter_sort[i:]
        items_perm = random.permutation(items_perm)
        vInter_sort[i:] = items_perm
        
    # Write the ranked list of edges
    nToWrite = nInter
    if isinstance(maxcount,int) and maxcount >= 0 and maxcount < nInter:
         nToWrite = maxcount
        print(nToWrite)
    else:
        print("No Maxcount, will write", nToWrite)

    
	# Get the non-ranked list of regulatory links
    vInter = list()
    for i in range(VIM.shape[0]) :
        for j in range(VIM.shape[1]):
            if i in input_idx and i!=j:
                score = VIM[i,j]
                vInter.append((i,j,score))
                if i%100 == 0:
                    print(vInter[-1])
                if i == 17777:
                    print("finish")
                
        #if regulator = 'all' then input_idx will be 0 to ngenes-1 -> so i will be each of thme in turn
     # (0,0), 0.4353463 -> (0,0,  0.4353463)
     # index, x in np.ndenumerate(a) produces (0, 0) 1 
     # may be I could add the progress bar here or just print(vInter[-1]))
    
   
    # Rank the list according to the weights of the edges
    vInter_sort = sorted(vInter,key=itemgetter(2),reverse=True) #sort vInter by score
    nInter = len(vInter_sort)
    
    # Random permutation of edges with score equal to 0
    flag = 1
    i = 0
    while flag and i < nInter:
        (TF_idx,target_idx,score) = vInter_sort[i]
        if score == 0:
            flag = 0
        else:
            i += 1
            
    if not flag:
        items_perm = vInter_sort[i:]
        items_perm = random.permutation(items_perm)
        vInter_sort[i:] = items_perm
        
    # Write the ranked list of edges
    nToWrite = nInter
    if isinstance(maxcount,int) and maxcount >= 0 and maxcount < nInter:
        nToWrite = maxcount
        print(nToWrite)
    else:
        print("No Maxcount, will write", nToWrite)

Cannot track	Can track	Can track &
Use for instead of ndenumerate (which is slower)

dynGENIE3.py	dynGENIE3_mod.py	dynGENIE3_mod_for.py
  # Get the non-ranked list of regulatory links
    vInter = [(i,j,score) for (i,j),score in ndenumerate(VIM) if i in input_idx and i!=j]
        
    # Rank the list according to the weights of the edges
    vInter_sort = sorted(vInter,key=itemgetter(2),reverse=True) #sort vInter by score
    nInter = len(vInter_sort)
    
    # Random permutation of edges with score equal to 0
    flag = 1
    i = 0
    while flag and i < nInter:
        (TF_idx,target_idx,score) = vInter_sort[i]
        if score == 0:
            flag = 0
        else:
            i += 1
            
    if not flag:
        items_perm = vInter_sort[i:]
        items_perm = random.permutation(items_perm)
        vInter_sort[i:] = items_perm
        
    # Write the ranked list of edges
    nToWrite = nInter
    if isinstance(maxcount,int) and maxcount >= 0 and maxcount < nInter:
        nToWrite = maxcount
	 # Get the non-ranked list of regulatory links
    vInter = list()
    for (i,j),score in ndenumerate(VIM) :
        if i in input_idx and i!=j:
            vInter.append((i,j,score))
            if i%100 == 0:
                print(vInter[-1])
   
      #if regulator = 'all' then input_idx will be 0 to ngenes-1 -> so i will be each of thme in turn
     # (0,0), 0.4353463 -> (0,0,  0.4353463)
     # index, x in np.ndenumerate(a) produces (0, 0) 1 
     # may be I could add the progress bar here or just print(vInter[-1]))
    
   
    # Rank the list according to the weights of the edges
    vInter_sort = sorted(vInter,key=itemgetter(2),reverse=True) #sort vInter by score
    nInter = len(vInter_sort)
    
    # Random permutation of edges with score equal to 0
    flag = 1
    i = 0
    while flag and i < nInter:
        (TF_idx,target_idx,score) = vInter_sort[i]
        if score == 0:
            flag = 0
        else:
            i += 1
            
    if not flag:
        items_perm = vInter_sort[i:]
        items_perm = random.permutation(items_perm)
        vInter_sort[i:] = items_perm
        
    # Write the ranked list of edges
    nToWrite = nInter
    if isinstance(maxcount,int) and maxcount >= 0 and maxcount < nInter:
         nToWrite = maxcount
        print(nToWrite)
    else:
        print("No Maxcount, will write", nToWrite)

    
	# Get the non-ranked list of regulatory links
    vInter = list()
    for i in range(VIM.shape[0]) :
        for j in range(VIM.shape[1]):
            if i in input_idx and i!=j:
                score = VIM[i,j]
                vInter.append((i,j,score))
                if i%100 == 0:
                    print(vInter[-1])
                if i == 17777:
                    print("finish")
                
        #if regulator = 'all' then input_idx will be 0 to ngenes-1 -> so i will be each of thme in turn
     # (0,0), 0.4353463 -> (0,0,  0.4353463)
     # index, x in np.ndenumerate(a) produces (0, 0) 1 
     # may be I could add the progress bar here or just print(vInter[-1]))
    
   
    # Rank the list according to the weights of the edges
    vInter_sort = sorted(vInter,key=itemgetter(2),reverse=True) #sort vInter by score
    nInter = len(vInter_sort)
    
    # Random permutation of edges with score equal to 0
    flag = 1
    i = 0
    while flag and i < nInter:
        (TF_idx,target_idx,score) = vInter_sort[i]
        if score == 0:
            flag = 0
        else:
            i += 1
            
    if not flag:
        items_perm = vInter_sort[i:]
        items_perm = random.permutation(items_perm)
        vInter_sort[i:] = items_perm
        
    # Write the ranked list of edges
    nToWrite = nInter
    if isinstance(maxcount,int) and maxcount >= 0 and maxcount < nInter:
        nToWrite = maxcount
        print(nToWrite)
    else:
        print("No Maxcount, will write", nToWrite)


Summary Table
![image](https://user-images.githubusercontent.com/83533049/227964172-76897dfa-3951-4cad-b6ed-d0dd0d06ec31.png)

