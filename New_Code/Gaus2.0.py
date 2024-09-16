#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:13:46 2024

@author: catermurawski
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')

catagories = ["Simple","Extended","Other","Too_Noisy"]
total = file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy']

# Set up the subplots: 2 rows and 2 columns for the 4 categories
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Flatten axes for easy iteration
axes = axes.flatten()

for i, cat in enumerate(catagories):
    ax = axes[i]
    f = file[cat]
    ratio = f/total
    ax.hist(ratio, bins=60, edgecolor='black',alpha=0.6, label=f"{cat} Histogram")
    ax.set_xlabel(f'{cat} Ratio')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of {cat} Ratio')
    ax.legend()
    std = np.std(ratio)
    def g(x):
        global std
        return np.exp(-(x**2)/(2*(std**2)))
    x = np.linspace(0, 1, 50)
    a = 200
    result, error = quad(g, 0, 1000)
    print(1486*result)
    y = a*np.exp(-((x)**2/(2*(std**2))))
    #for the gaussian line
    ax.plot(x,y)
   
    