#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:40:10 2024

@author: catermurawski
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the data
file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')


simple = file['Simple'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])
extended = file['Extended'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])
other = file['Other'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])
noisy = file['Too_Noisy'] / (file['Simple'] + file['Extended'] + file['Other'] + file['Too_Noisy'])

plt.figure()
plt.hist(noisy,bins=20)

