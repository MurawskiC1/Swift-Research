#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:52:54 2023

@author: catermurawski
"""

import pandas as pd
import BurstChaser as bc



beta = pd.read_csv("BurstBeta.csv")



#dictionairy {id: PusleShapeClass}
pulse_shapes = {}
pulse_noise = {}
#sort through all indexes
for i in range(687,beta.shape[0]):
    workflow = beta.workflow_name.iloc[i]
    wid = beta.workflow_id.iloc[i]
    id_number = beta.subject_ids.iloc[i]
    results = beta.annotations.iloc[i]
    
    #if the index is a pulse shape
    if workflow == "Pulse shapes":
        if  id_number not in pulse_shapes:
            #create a pulse shape class
 
            pulse_shapes[id_number] = bc.PulseShape(id_number, wid)
            
        
        pulse_shapes[id_number].ShapeCount(results)
        pulse_shapes[id_number].FollowCount(results)

    #if the workflow is pulse or noise
    if workflow == "(Optional) Practice: Pulse or noise?":
        if id_number not in pulse_noise:
            pulse_noise[id_number] = bc.PulseNoise(id_number, wid)
        pulse_noise[id_number].classCount(results)
        
for i in pulse_shapes:
    print(pulse_shapes[i])

###UPDATE THE CSV FILES
        
bc.PulseNoise.export("Pulse_Noise", [pulse_noise[i] for i in pulse_noise])
            
bc.PulseShape.export("Pulse_Shape", [pulse_shapes[i] for i in pulse_shapes])

                        
    

 

    

