#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:23:55 2024

@author: catermurawski
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
# Read in the file
file = pd.read_csv("/Users/catermurawski/Desktop/Swift-Research/CSVExports/Pulse_Shape.csv")

def function(x):
    global standard_dev
    global simple_prop
    C = 1 / (standard_dev * np.sqrt(2 * np.pi))
    zexp = -0.5 * ((x - 0) / standard_dev)**2
    z = len(simple_prop) *C * np.exp(zexp)
    return z
    
# Make a proportions table
simple_prop = file["Too_Noisy"] / (file["Simple"] + file["Extended"] + file["Other"] + file["Too_Noisy"])

# Plot proportions frequency chart and get histogram data for scaling
counts, bins, _ = plt.hist(simple_prop, bins=20, alpha=0.5, label='Simple Proportions Frequency')
#print(counts)
# Calculate mean and standard deviation
mean = sum(simple_prop)/len(simple_prop)
standard_dev = np.sqrt(sum(simple_prop**2)/len(simple_prop))
print(standard_dev)
# Generate x values for the normal distribution (centered around the mean)
x = np.linspace(-4*standard_dev, 4*standard_dev, 1000)

# Calculate the normal distribution's y values
C = 1 / (standard_dev * np.sqrt(2 * np.pi))
exp = -0.5 * ((x - mean) / standard_dev)**2
zexp = -0.5 * ((x - 0) / standard_dev)**2
y = len(simple_prop)*C * np.exp(exp)
z = C * np.exp(zexp)*1/20*len(simple_prop)
print(len(simple_prop))
# Scale y values to match histogram
#bin_width = bins[1] - bins[0]  # Calculate bin width
#y_scaled = y * len(simple_prop) * bin_width  # Scale y to match histogram area
#z_scaled = z * len(simple_prop) * bin_width
result = integrate.quad(function,-1000,1000)
print(result)
# Plot the scaled normal distribution
#plt.plot(x, y_scaled, color='blue', label='Normal Distribution')
plt.plot(x, z, color='red', label='ND 0 Centered')

# Add vertical lines at ±1.96 standard deviations from the ND centered at 0
plt.axvline(x=1.96 * standard_dev, color='black', linestyle='--', label='+1.96 SD')
#plt.axvline(x=1.96 * standard_dev+ mean, color='black', linestyle='--', label='+1.96 SD')


# Add labels and legend
plt.xlabel("Proportion")
plt.ylabel("Frequency")
plt.title("Simple Proportions Frequency")
plt.legend()

plt.show()
