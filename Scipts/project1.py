# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:01:27 2020

@author: krist
"""

import numpy as np
import pandas as pd
import os.path

def dataLoad(filename):
    
    #Check if file exists using the os.path module
    #If exists/ read file and convert to numpy
    if os.path.isfile(filename):
        CSV = pd.read_csv(filename) 
        npCSV = CSV.to_numpy()
    else:
        return print("File not found! Remember to specify .csv - Returning to main menu.")
    
    #Error handling for CSV file
    #___________________________________________________________________________
    
    #Remove extra columns
    length = len(npCSV[0,:])
    if length > 3:
        print("Too many columns in CSV! These will be deleted.")
        npCSV = np.delete(npCSV, np.s_[3:length], axis=1)
    
    #Error handling for bacteria class
    C1 = np.where(np.logical_or(npCSV[:,0]<10 , npCSV[:,0]>60))
    for l in C1[0]:
        print("Temp error, line", l ,"out of bounds at:",npCSV[l,0])
    
    #Error handling for growth rate
    C2 = np.where(npCSV[:,1] < 0)
    for l in C2[0]:
        print('Growth rate error, line {}. Negative value.'.format(l))
        
    #Error handling for bacteria class bound
    C3 = np.where(np.logical_or(npCSV[:,2]<1, npCSV[:,2]>4))
    for l in C3[0]:
        print('Bacteria class out of bounds, line {}!'.format(l))
    
    #Error handling for wrong format in bact.class
    C4 = np.where(np.remainder(npCSV[:,2],1) > 0 )
    for l in C4[0]:
        print(f'Bacteria class error, line {l}, {npCSV[l,2]}: Check for decimal points.')
    
    #Index of all errors, removal of all rows with errors
    Indexarr = np.unique(np.concatenate([C1[0],C2[0],C3[0],C4[0]],0))
    npCSV = np.delete(npCSV, [Indexarr],0)
    
    #Check if the array is empty
    if npCSV.size:
        return npCSV
    else:
        return print("No valid data!")
     









