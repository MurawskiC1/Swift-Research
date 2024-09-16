#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:04:29 2024

@author: catermurawski
"""

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')

# Print the DataFrame to see the data


# Normalize the data
simple = file['Simple'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])
extended = file['Extended'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])
other = file['Other'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])
noisy = file['Too_Noisy'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])

# Combine the normalized data into a DataFrame for easier handling
normalized_data = pd.DataFrame({
    'Simple': simple,
    'Extended': extended,
    'Other': other,
    'Too_Noisy': noisy,
    'GRB_Name': file['Burst_Name']
})

# Create the box plots and capture the output
plt.figure(figsize=(10, 6))
boxplot_dict = plt.boxplot([simple, extended, other, noisy], labels=['Simple', 'Extended', 'Other', 'Too_Noisy'], patch_artist=True)

# Extract and print outliers
outliers = {label: [] for label in ['Simple', 'Extended', 'Other', 'Too_Noisy']}
outlier_indices = {label: [] for label in ['Simple', 'Extended', 'Other', 'Too_Noisy']}

for i, label in enumerate(outliers.keys()):
    fliers = boxplot_dict['fliers'][i]
    outlier_values = fliers.get_ydata()
    outliers[label] = outlier_values
    
    # Find the indices of these outliers in the normalized data
    outlier_indices[label] = normalized_data[normalized_data[label].isin(outlier_values)].index

# Display outliers and corresponding GRB_Names
for label, indices in outlier_indices.items():
    print(f"Outliers in {label}:")
    for idx in indices:
        print(f"GRB_Name: {normalized_data.at[idx, 'GRB_Name']}, Value: {normalized_data.at[idx, label]}")
    print()

# Add titles and labels
plt.title('Normalized Votes for each Burst in each Classifiaction')
plt.xlabel('Classification')
plt.ylabel('Normalized Votes')
plt.grid(True)
plt.show()
