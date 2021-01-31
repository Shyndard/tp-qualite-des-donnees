#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import pandas as pd
import scipy as sp
import numpy as np
import calendar


# In[2]:


si = pd.read_excel("/home/jovyan/work/data/Savukoski kirkonkyla.xlsx", sheet_name=2)


# In[3]:


# Définition d'une fonctions permettant de récupérer la prochaine valeur existante
def getNextCorrectValue(df, rowIndex, columnIndex):
    nextValue = df.iloc[(rowIndex + 1), columnIndex]
    if np.isnan(nextValue):
        return getNextCorrectValue(df, rowIndex+2, columnIndex)
    else:
        return nextValue

# Définition d'une fonctions permettant de récupérer la précédente valeur existante
def getPreviousCorrectValue(df, rowIndex, columnIndex):
    nextValue = df.iloc[(rowIndex-1), columnIndex]
    if np.isnan(nextValue):
        return getNextCorrectValue(df, rowIndex-2, columnIndex)
    else:
        return nextValue
    
# Récupération des températures depuis l'excel
temperature=[]
indexArray=[]
month = 1
month_temperature=[]
index = 1

for row in range(0, 365):
    temperature_value_max = si.iloc[row, 6]
    temperature_value_min = si.iloc[row, 7]
    # SI la valeur max est nulle, alors on va faire la moyenne entre les valeurs max 
    # du jour précédent et suivant ayant au moins une valeur correcte
    if(np.isnan(temperature_value_max)):
        temperature_value_max = np.average([getNextCorrectValue(si, row, 6), getPreviousCorrectValue(si, row, 6)])
    # SI la valeur min est nulle, alors on va faire la moyenne entre les valeurs min 
    # du jour précédent et suivant ayant au moins une valeur correcte
    if(np.isnan(temperature_value_min)):
        temperature_value_min = np.average([getNextCorrectValue(si, row, 7), getPreviousCorrectValue(si, row, 7)])
    # On sauvegarde la moyenne entre la température max et la température min
    month_temperature.append(int(np.average([temperature_value_max, temperature_value_min])))
    currentMonth = si.iloc[row, 1]
    if currentMonth > month:
        temperature.append(month_temperature)
        month_temperature=[]
        month = currentMonth

temperature.append(month_temperature)


# In[4]:


temperature_average_per_month=[]

# Calcul de la moyenne de température par mois

for month in range(len(temperature)):
    temperature_average = np.average(temperature[month])
    temperature_average_per_month.append(temperature_average)
    print("Month {!s} average temperature {!s}".format(calendar.month_name[month + 1], temperature_average))


# In[5]:


temperature_standard_deviation_per_month=[]

# Calcul de l'écart type de température par mois

for month in range(len(temperature)):
    temperature_standard_deviation = np.std(temperature[month])
    temperature_standard_deviation_per_month.append(temperature_standard_deviation)
    print("Month {!s} standard deviation temperature {!s}".format(calendar.month_name[month + 1], temperature_standard_deviation))


# In[6]:


temperature_min_per_month=[]
temperature_max_per_month=[]

min_temp = temperature[0][0]
max_temp = temperature[0][0]

# Détermination du minimum et maximum de la température par mois et de l'année

for month in range(len(temperature)):
    temperature_min = min(temperature[month])
    temperature_max = max(temperature[month])
    temperature_min_per_month.append(temperature_min)
    temperature_max_per_month.append(temperature_max)
    if temperature_min < min_temp:
        min_temp = temperature_min
    if temperature_max > max_temp:
        max_temp = temperature_max
    print("{!s} min temp {!s} and max temp {!s}".format(calendar.month_name[month + 1], temperature_min, temperature_max))

print("Min temp {!s} and max temp {!s}".format(min_temp, max_temp))


# In[7]:


# Après analyse entre les données fournies par la station Savukoski et les données du SI-erreur qu'il n'y a pas de lien.
# En effet, on constate que 

