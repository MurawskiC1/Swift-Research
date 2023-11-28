#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:52:54 2023

@author: catermurawski
"""

import pandas as pd
import BurstChaser as bc



beta = pd.read_csv("BurstBeta.csv")

repeatS=0
repeatP=0
#dictionairy {id: PusleShapeClass}
pulse_shapes = {}
pulse_noise = {}
#sort through all indexes
for i in range(686,beta.shape[0]):
    workflow = beta.workflow_name.iloc[i]
    wid = beta.workflow_id.iloc[i]
    id_number = beta.subject_ids.iloc[i]
    results = beta.annotations.iloc[i]
    user = beta.user_id.iloc[i]
    
    #if the index is a pulse shape
    if workflow == "Pulse shapes":
        if  id_number not in pulse_shapes:
            #create a pulse shape class
            pulse_shapes[id_number] = bc.PulseShape(id_number, wid)
        if user not in pulse_shapes[id_number].contributers:
            pulse_shapes[id_number].contributersAdd(user)
            pulse_shapes[id_number].ShapeCount(results)
            pulse_shapes[id_number].FollowCount(results)
        
        else:
            repeatS+=1
        

    #if the workflow is pulse or noise
    if workflow == "(Optional) Practice: Pulse or noise?":
        if id_number not in pulse_noise:
            pulse_noise[id_number] = bc.PulseNoise(id_number, wid)
        if user not in pulse_noise[id_number].contributers:  
            pulse_noise[id_number].contributersAdd(user)
            pulse_noise[id_number].classCount(results)
        else:
            repeatP +=1
        
print(repeatS)
print(repeatP)


###UPDATE THE CSV FILES
bc.PulseShape.export("Pulse_Shape", [pulse_shapes[i] for i in pulse_shapes])
bc.PulseNoise.export("Pulse_Noise", [pulse_noise[i] for i in pulse_noise])
                        
    

 

    

