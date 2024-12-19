#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:13:06 2024

@author: catermurawski
"""

file = open('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')

out = ""

for i in file:

    
    sec = i.split(",")
    for j in sec:
        out = out + f"{j} "
        if j != sec[-1]:
            out = out + "&& "

    
print(out)