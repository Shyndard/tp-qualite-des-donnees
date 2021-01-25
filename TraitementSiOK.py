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


si = pd.read_excel("/home/jovyan/work/data/Climat.xlsx", sheet_name=0)


# In[3]:


temperature=[]

## Récupération des températures depuis l'excel

for column in range(3, 15):
    month_temperature=[]
    for row in range(3, 34):
        temperature_value = si.iloc[row, column]
        if(not np.isnan(temperature_value)):
            month_temperature.append(temperature_value)
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


# Affichages de la température par mois via 1 figure

get_ipython().run_line_magic('matplotlib', 'notebook')

fig, axs = plt.subplots(12)

for month in range(len(temperature)):
    axs[month].plot(temperature[month])
    plt.show()


# In[8]:


# Affichages de la température par mois via 12 figures

get_ipython().run_line_magic('matplotlib', 'notebook')

for month in range(len(temperature)):
    plot = plt.figure(month)
    plt.plot(temperature[month])
    plt.xlabel("Jour du mois")
    plt.ylabel("Température")

plt.show()


# In[9]:


get_ipython().run_line_magic('matplotlib', 'notebook')

flatten = lambda t: [item for sublist in t for item in sublist]

class SnaptoCursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([0],[0], marker="o", color="crimson", zorder=3) 
        self.x = x
        self.y = y
        self.txt = ax.text(0.7, 0.9, '')

    def mouse_move(self, event):
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        indx = np.searchsorted(self.x, [x])[0]
        x = self.x[indx]
        y = self.y[indx]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text('%1.2f°C (day %1d)' % (y, x))
        self.txt.set_position((x,y))
        self.ax.figure.canvas.draw_idle()

t = np.arange(0, 365, 1)
fig, ax = plt.subplots()

cursor = SnaptoCursor(ax, t, flatten(temperature))
cid =  plt.connect('motion_notify_event', cursor.mouse_move)

ax.plot(t, flatten(temperature),)
plt.show()


# In[10]:


t = np.arange(0, 365, 1)
fig, ax = plt.subplots()

cursor = SnaptoCursor(ax, t, flatten(temperature))
cid =  plt.connect('motion_notify_event', cursor.mouse_move)

ax.plot(t, flatten(temperature),) 
plt.show()


# In[ ]:




