#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:55:24 2024

@author: catermurawski
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import scipy.integrate as integrate

# Load the CSV file
try:
    file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')
except FileNotFoundError:
    raise SystemExit("File not found. Please check the file path.")

# Calculate the ratios for each category
categories = ['Simple', 'Extended', 'Other', 'Too_Noisy']
total = file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy']
if (total == 0).any():
    raise ValueError("The total sum of all categories is zero, which would lead to division by zero.")

ratios = {cat: file[cat] / total for cat in categories}

# Set up the subplots: 2 rows and 2 columns for the 4 categories
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Flatten axes for easy iteration
axes = axes.flatten()

# Loop over each category to create histograms and Gaussian fits
for i, cat in enumerate(categories):
    # Get the current axis
    ax = axes[i]
    
    # Calculate the ratio for this category
    pos = ratios[cat]
    
    # Skip if pos is empty or has zero variance
    if len(pos) == 0 or np.std(pos) == 0:
        ax.hist(pos, bins=30, edgecolor='black', alpha=0.6, label=f"{cat} Histogram")
        ax.set_xlabel(f'{cat} Ratio')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Distribution of {cat} Ratio')
        ax.legend()
        continue
    
    # Plot the histogram
    counts, bin_edges, _ = ax.hist(pos, bins=30, edgecolor='black', alpha=0.6, density=True, label=f"{cat} Histogram")
    
    # Calculate mean and standard deviation for Gaussian fit
    mean_pos = np.mean(pos)
    std_pos = np.std(pos)  # Use numpy std function for simplicity
    
    # Generate x values for plotting the Gaussian curve
    x = np.linspace(min(pos), max(pos), 1000)
    
    # Calculate the Gaussian fit
    gaussian_fit = x*0
    
    # Normalize the Gaussian curve to match the histogram
    gaussian_fit *= np.diff(bin_edges)[0] * len(pos)  # Scale to match histogram height
    
    # Plot the Gaussian curve
    ax.plot(x, gaussian_fit, color='red', label=f"{cat} Gaussian", linewidth=2)

    # Add labels and title
    ax.set_xlabel(f'{cat} Ratio')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of {cat} Ratio')
    ax.legend()

# Adjust layout for readability
plt.tight_layout()

# Show the plot
plt.show()
