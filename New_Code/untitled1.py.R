#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:31:17 2024

@author: catermurawski
"""
import matplotlib.pyplot as plt
import pandas as pd


# Load the data
file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')

# Extract and normalize the 'Simple' column using min-max scaling
simple = file['Simple'].values.reshape(-1, 1)
scaler = MinMaxScaler()
simple_normalized = scaler.fit_transform(simple)

# Create a histogram to show the distribution of the normalized 'Simple' column
plt.hist(simple_normalized, bins=15, edgecolor='black')

# Add titles and labels
plt.title('Distribution of Simple Column (Min-Max Scaled)')
plt.xlabel('Normalized Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()

