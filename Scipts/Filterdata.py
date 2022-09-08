#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:22:18 2020

@author: mads
"""

import numpy as np 
from inputNumberFilter import inputNumberFilter

def filterData(data):
    
    #Gemmer input fra bruger i variabler 
    Bacteriatype = inputNumberFilter("Write bacteria type:")
    GrowthrateUpper = inputNumberFilter("Insert an upper bound for growthrate:")
    GrowthrateLower = inputNumberFilter("Insert a lower bound for growthrate:")
    
    
    #Disse funktioner tager højde for intet input fra bruger i upper/lower bounds og bacterietype 
    if Bacteriatype not in [1,2,3,4]:
       Bacteriatype = None 
    
    if GrowthrateUpper == "":
        GrowthrateUpper = None 
    
    if GrowthrateLower == "":
        GrowthrateLower =  None 
    
#--------Filtreringsfunktioner------------------------------------------------
# Funktionerne filterer efter type af bakterie 
    if Bacteriatype == "1" or Bacteriatype == "Salmonella enterica":
        data = data[data[:,2] == 1]
        
    elif Bacteriatype == "2" or Bacteriatype == "Bacillus cereus":
        data = data[data[:,2] == 2]
    
    elif Bacteriatype == "3" or Bacteriatype == "Listeria": 
        data = data[data[:,2] == 3]
    
    elif Bacteriatype == "4" or Bacteriatype == "Brochothrix thermosphacta":
        data = data[data[:,2] == 4]
    
    else:
        print("Bacteriatype not found. Bacteriatype set to all types")
    
#Funktionerne her filterer efter valgte bounds i Growthrate
    if ((GrowthrateLower is not None) and (GrowthrateUpper is not None)):
       data = data[np.logical_and(data[:,1] > GrowthrateLower, data[:,1] < GrowthrateUpper)]

#Funktion tager højde for at der kun er input i GrowthrateUpper        
    elif (GrowthrateLower == None) and GrowthrateUpper is not None:
        data = data[data[:,1] < GrowthrateUpper]
        
#Funktion tager højde for at der kun er input i GrowthrateLower     
    elif (GrowthrateUpper == None) and (GrowthrateLower is not None):
        data = data[data[:,1] > GrowthrateLower]
 
#Denne funktion tager højde for om intet af dataen matcher filtret 
    if data.size == 0: 
        print("No data matches your filter, to use the plot function, data must contain at least one row")
    
    #Retunerer 4 forskellige ting i en liste,  da alle elementer skal bruges i Mainscript 
    return [data, GrowthrateUpper, GrowthrateLower, Bacteriatype]


