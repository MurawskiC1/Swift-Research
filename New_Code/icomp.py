#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:37:01 2024

@author: catermurawski
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
beta = pd.read_csv("/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv")

# Filter the data
simple = beta['Simple']
extended = beta['Extended']


# Create a scatter plot
plt.scatter(simple, extended)
plt.xlabel('Simple')
plt.ylabel('Extended')
plt.title('Finding Clustering')
plt.show()
