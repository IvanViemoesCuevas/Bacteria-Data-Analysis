#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:58:25 2020

@author: mads
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#dataRaw = pd.read_csv("Testdata.csv")
#data = dataRaw.to_numpy()

#Funktionen tager data iform af matrice fra mainscript som input og outputter de to plots
def dataPlot(data): 

#______________________Histogram______________________________________________    
    Bacteria = data[:,2]#Laver et array ud af bakterie collonen
    plt.hist(Bacteria, bins=[1,2,3,4,5], align = "left",rwidth= 0.5)#Plotter histogram ud fra array
    plt.xticks([0,1,2,3,4,5]) #Definerer hvilke ticks vi vil have på plot
    plt.xlabel("Bacteria type")
    plt.ylabel("Amouont of bacteria")
    plt.title("Number of Bacteria")
    Bachis = plt.show() #Definerer plottet som variabel
    
    
#_____________________Graf____________________________________________________
    #Laver matricer med kun 1 type bakterie i hver...
    B1 = data[data[:,2] == 1]
    B2 = data[data[:,2] == 2]
    B3 = data[data[:,2] == 3]
    B4 = data[data[:,2] == 4]
    
    #Sorterer ifht x akse,(Bevarer tilhørende y-værdier til sorteret x værdi)
    B1 = B1[B1[:,0].argsort()]
    B2 = B2[B2[:,0].argsort()]
    B3 = B3[B3[:,0].argsort()]
    B4 = B4[B4[:,0].argsort()]
    
    
    #x og y værdier som numpy arrays og sorterer dem efter størrelse
    x1 = B1[:,0]
    y1 = B1[:,1]
    x2 = B2[:,0]
    y2 = B2[:,1]
    x3 = B3[:,0]
    y3 = B3[:,1]
    x4 = B4[:,0]
    y4 = B4[:,1]
    
    #plotter alle grafer 
    plt.title("Growth rate by Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.plot(x1,y1,"y",marker = "o")
    plt.plot(x2,y2,"g",marker = "o")
    plt.plot(x3,y3,"r",marker = "o")
    plt.plot(x4,y4,"b",marker = "o")
    plt.legend(["Type 1","Type 2","Type 3","Type 4"])

    growth = plt.show()

    return Bachis, growth

#print(dataPlot(data))
   
                             