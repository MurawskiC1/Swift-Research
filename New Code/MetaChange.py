#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:45:09 2023

@author: catermurawski
"""

from panoptes_client import Panoptes, Project, SubjectSet, Subject, Workflow
from BurstChaser import BurstChaser as bc
Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')

import pandas as pd


burst = SubjectSet.find("117825")



run = False
file = open("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/Pulse_shape_practice_list.txt")

GRBname = []
Q1answer = []
Q2answer = []
Feedback = []


def ans1(shape):
    if "extended emission" in shape:
        return 1
    elif "A simple pulse" in shape:
        return 0
    elif "Other" in shape:
        return 2
    elif "It is too noisy inside the blue region to see any structures." in shape:
        return 3

def ans2(j):
    if 'Pulses connected with underlying emission' in j: 
        return 2
    if 'One or more pulses with symmetrical structure' in j:
        return 0
    if "One or more pulses with the fast-rise and slow-decay shape" in j:
        return 1
    if 'Rapid Varying pulses' in j:
        return 3
    if "I don't see" in j:
        return 4
    if "It is too noisy inside the blue region to see any structures." in j:
        return 5
    

for line in file:
    if run == True:
        if "****************************************************" in line:
            break
        seg = line.split("|")
        GRBname.append(seg[0].split(" ")[0])
        Q1answer.append(ans1(seg[1]))
        Q2answer.append(ans2(seg[2]))
        try:
            Feedback.append(seg[3])
        except:
            Feedback.append("No Feedback")
    run = True
    
data = {"GRB_Name": GRBname,
        "Answer_1": Q1answer,
        "Answer_2": Q2answer,
        "Feedback": Feedback}
golden = pd.DataFrame(data)

subject_metadata = {}
count = 0 
for i in golden.GRB_Name:
    
    subject_metadata[bc.findPNG(i)] = {"subject_reference": count,
                                       "#feedback_1_id": 1,
                                       "#feedback_1_answer": golden[i].Answer_1,
                                       "#feedback_1_successMessage": f"CORRECT! {golden[i].Feedback}",
                                       "#feedback_1_failureMessage": f"INCORRECT. {golden[i].Feedback}",
                                       "#feedback_2_id": 2,
                                       "#feedback_2_answer": golden[i].Answer_2,
                                       "#feedback_2_successMessage": f"CORRECT! {golden[i].Feedback}",
                                       "#feedback_2_failureMessage": f"INCORRECT. {golden[i].Feedback}",
                                       
                                       }
    count += 1

new_subjects = []

for filename, metadata in subject_metadata.items():
    subject = Subject()

    subject.add_location(filename)

    subject.metadata.update(metadata)

    subject.save()
    new_subjects.append(subject)

burst.add(new_subjects)

burst.save()
    
    
    
    

