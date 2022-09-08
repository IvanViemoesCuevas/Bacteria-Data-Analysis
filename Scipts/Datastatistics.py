# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:21:36 2020

@author: ivanv
"""
#Importerer numpy 
import numpy as np

#Laver en funktion der har 2 variabler, hvor den ene er en matrix og den anden er en string
def dataStatistics(data, statistic):
    
    #Udregner mean i alle søjlerne
    Mean = np.mean(data, axis = 0)
    
    #Udregner standardafvigelsen i alle søjler
    std = np.std(data, axis = 0)
    
    #Finder ud af hvor mange rækker der er i matricen
    rows = len(data)
    
    #Laver et nyt array hvor den kun gemmer de rækker hvor temperaturen er under 20
    dataCold = data[data[:,0] < 20]
    
    #Laver et nyt array hvor den kun gemmer de rækker hvor temperaturen er over 50
    dataHot = data[data[:,0] > 50]
    
    #Udregner mean der hvor temperaturen er over 50
    if len(dataHot) > 0:
        MeanHot = np.mean(dataHot, axis = 0)
    
    #Udregner mean der hvor temperaturen er under 20
    if len(dataCold) > 0:
         MeanCold = np.mean(dataCold, axis = 0)
    
    #Hvis Statistic er Mean Temperature gemmer den mean af første søjle i result
    if statistic == "Mean Temperature":
        result = Mean[0]
    
    #Hvis Statistic er Mean Growth rate gemmer den mean af anden søjle i result
    if statistic == "Mean Growth rate":
        result = Mean[1]
    
    #Hvis Statistic er Std Temperature gemmer den Std af første søjle i result
    if statistic == "Std Temperature":
        result = std[0]
    
    #Hvis Statistic er Std Growth rate gemmer den Std af anden søjle i result
    if statistic == "Std Growth rate":
        result = std[1]
    
    #Hvis Statistic er Rows gemmer sætter den variablen result lig rows
    if statistic == "Rows":
        result = rows
    
    #Hvis Statistic er Mean Hot Growth rate gemmer den meanHot af anden søjle i result
    if statistic == "Mean Hot Growth rate":
        if len(dataHot) > 0:
            result = MeanHot[1]
        else:
            print("No hot temperatures found")
            result = np.NaN
    
    #Hvis Statistic er Mean Cold Growth rate gemmer den meanCold af anden søjle i result
    if statistic == "Mean Cold Growth rate":
        if len(dataCold) > 0:
            result = MeanCold[1]
        else:
            print("No cold temperatures found")
            result = np.NaN

    
    #Returner resultatet fået fra if'erne
    return result

