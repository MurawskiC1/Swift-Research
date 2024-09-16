#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:54:44 2024

@author: catermurawski
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
import numpy as np

# Load the data (replace with your actual file path)
beta = pd.read_csv("/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv")

# Access the columns and normalize (assuming these columns exist in your CSV)
total = beta['Simple'] + beta['Extended'] + beta['Other'] + beta['Too_Noisy']
simple = beta['Simple'] / total
extended = beta['Extended'] / total
other = beta['Other'] / total

# Prepare the normalized data for clustering
X = pd.DataFrame({
    'Simple': simple,
    'Extended': extended,
    'Other': other
})

# Define custom initial centroids
custom_centroids = [
    [0, 0, 0],       # Example centroid 1
    [1, 0, 0],       # Example centroid 2
    [0, 1, 0],       # Example centroid 3
    [0, 0, 1],       # Example centroid 4
    [0.5, 0.5, 0],   # Example centroid 5
    [0, 0.5, 0.5],   # Example centroid 6
    [0.5, 0, 0.5],   # Example centroid 7
    [0.25, 0, 0],    # Example centroid 8
    [0, 0.25, 0],    # Example centroid 9
    [0, 0, 0.25]     # Example centroid 10
]

# Apply K-Means clustering with custom initial centroids
kmeans = KMeans(n_clusters=len(custom_centroids), init=np.array(custom_centroids), n_init=1, max_iter=100)
beta['Cluster'] = kmeans.fit_predict(X)

# Convert cluster numbers to colors
cluster_colors = {
    0: 'red',
    1: 'blue',
    2: 'green',
    3: 'orange',
    4: 'gray',
    5: 'purple',
    6: 'brown',
    7: 'pink',
    8: 'cyan',
    9: 'yellow'
}
beta['Color'] = beta['Cluster'].map(cluster_colors)

# Export the DataFrame to a CSV file (replace with your desired export path)
beta.to_csv("/Users/catermurawski/desktop/Swift-Research/CSVExports/Cluster_Classification.csv", index=False)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with clusters
sc = ax.scatter(X['Simple'], X['Extended'], X['Other'], c=beta['Color'], marker='o')

ax.set_xlabel('Simple')
ax.set_ylabel('Extended')
ax.set_zlabel('Other')

plt.show()
