#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:57:41 2020

@author: mads
"""
#Importerer nødvendige libraries og funktioner
import numpy as np 
import pandas as pd 
import matplotlib as mp
from plotfunk import dataPlot
from Datastatistics import dataStatistics
from project1 import dataLoad
from Filterdata import filterData
from displayMenu import displayMenu

#Authors: Ivan Viemoes Cuevas s205823, Kristian Mathies Friis Nielsen s204120 og Mads Andersen s204137

#-----------------------------------Main script-------------------------------
#Menu options: 
menuItems =np.array(["Load data","Filter data","Display statistics","Generate plots","Quit","Deactivate filter" ])

# Array der gemmer forskellige muligheder for statistic
statistic_items = np.array(["Mean Temperature","Mean Growth rate","Std Temperature",
                            "Std Growth rate","Rows","Mean Hot Growth rate",
                            "Mean Cold Growth rate"])

#Creates a variable with an empty string for saving user input
filename = ""

#Sætter filter variabler til standard at være ingenting. 
CSV_data = None
GrowthrateLower = None 
GrowthrateUpper = None 
Bacteriatype = None 
#-------------------------Menu options----------------------------------------
while True: 
    choice = displayMenu(menuItems)
    #Data Load funktion 
    if choice == 1: 
        filename = input("Please write name of csv file:")#Tager input fra bruger 
        CSV_data = dataLoad(filename)
        print(CSV_data)
    
    #Filter funktion 
    elif choice == 2: 
        if filename == "" or CSV_data is None:
            print("Error: please load data first")
        else: 
            #Output fra filterdata er en liste, hvor den filtrerededata er på index 0 
            Output = filterData(CSV_data)
            CSV_data = Output[0] #Den filtrerededata er på index 0
            GrowthrateUpper = str(Output[1]) #Øvregrænse er index 1 
            GrowthrateLower = str(Output[2]) #Nedregrænse er index 2
            Bacteriatype = str(Output[3]) #Backterietypen er index 3
            print(CSV_data)
    
    #Statistic funktion
    elif choice == 3: 
        if filename == ""  or CSV_data is None:
            print("Error please load file first")
        else: 
            stat_index = int(displayMenu(statistic_items) -1) #Tager brugers valg og "oversætter" til index
            #Laver statestik på baggrund af indlæst fil, og bruger index til at matche med tilsvarende statestik i array.
            #Med denne funktion undgår man at bruger skal "Stave" præcis hvilken statestik de vil have 
            #Viser hvilken statistik der er valgt og printer den beregnede statistik
            print(statistic_items[stat_index]+":",dataStatistics(CSV_data,statistic_items[stat_index])) 
    
    #Plotter data der er gemt i CSV filen
    elif choice == 4: 
        if filename == ""  or CSV_data is None:
            print("Error: Need datafile to run!")
        else: 
            print(dataPlot(CSV_data))
    
    #ends the while loop, and therefore the program. 
    elif choice == 5: 
        break 
    
    #Deaktiverer et evt. tændt filter og sæt data tilbage til orignal tilstand
    elif choice == 6:
        if filename == ""  or CSV_data is None:
            print("Error: No filter to reset!")
            
    #Sætter filtermulighederne til None, og sætter datafilen tilbage til original
        else: 
            CSV_data = dataLoad(filename)
            GrowthrateUpper = None 
            GrowthrateLower = None 
            Bacteriatype = None 
     
#________________________Display filter warning_______________________________

#Checker om der er aktivt filter og displayer en warning + valgte filter
    if (GrowthrateUpper is not None) or (GrowthrateLower is not None) or (Bacteriatype is not None): 
        print("Warning! Filter is active:" "|Upperbound:"+ GrowthrateUpper +"|Lowerbound:"+ GrowthrateLower+ "|Bacteriatype:"+ Bacteriatype + "|")

#Checker om der ikke er noget aktivt filter og giver feedback
    elif (GrowthrateUpper is None) and (GrowthrateLower is None) and (GrowthrateUpper is None): 
        print("No active filter")
    
    
#Printer farvel besked:
print("Program has ended, Goodbye")





