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

proj = Project.find("18664")
burst = SubjectSet()
burst.links.project = proj
burst.display_name= "GOLDEN_SAMPLE"
burst.save()


run = False
file = open("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/Pulse_shape_practice_list.txt")

GRBname = []
Q1answer = []
Q1feed =[]
Q2answer = []
Q2feed =[]
helping = []


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
        Q1feed.append(seg[1])
        Q2answer.append(ans2(seg[2]))
        Q2feed.append(seg[2])
        try:
            helping.append(seg[3])
        except:
            helping.append("No Help")
    run = True
    
data = {"GRB_Name": GRBname,
        "Answer_1": Q1answer,
        "Feed_1": Q1feed,
        "Answer_2": Q2answer,
        "Feed_2": Q2feed,
        "Help": helping}
golden = pd.DataFrame(data)

subject_metadata = {}
count = 1
for i in range(0,golden.shape[0]): 
    answer1 = str(golden.Answer_1.iloc[i])
    feed1 = str(golden.Feed_1.iloc[i])
    answer2 = str(golden.Answer_2.iloc[i])
    feed2 = str(golden.Feed_2.iloc[i])
    h = str(golden.Help.iloc[i])
    
    subject_metadata[f"{bc.findPNG(golden.GRB_Name.iloc[i])}"] = {"subject_reference": count,
                                                                  'date': '2023-12-23',
                                                                  "#feedback_1_id": str(1),
                                                                  "#feedback_1_answer": answer1,
                                                                  "#feedback_1_failureMessage": f"INCORRECT. {feed1}",
                                                                  "#feedback_2_id": str(2),
                                                                  "#feedback_2_answer": answer2,
                                                                  "#feedback_2_failureMessage": f"INCORRECT. {feed2}" ,
                                                                  "Help": f"{h}"}
                                                              
    count += 1

new_subjects = []

for filename, metadata in subject_metadata.items():
    subject = Subject()

    subject.links.project = proj
    subject.add_location(filename)

    subject.metadata.update(metadata)

    subject.save()
    new_subjects.append(subject)

burst.add(new_subjects)

    
'''
  "#feedback_1_id": 1,
  "#feedback_1_answer": golden.Answer_1.iloc[i],
  "#feedback_1_successMessage": f"CORRECT! {golden.Feedback.iloc[i]}",
  "#feedback_1_failureMessage": f"INCORRECT. {golden.Feedback.iloc[i]}",
  "#feedback_2_id": 2,
  "#feedback_2_answer": golden.Answer_2.iloc[i],
  "#feedback_2_successMessage": f"CORRECT! {golden.Feedback.iloc[i]}",
  "#feedback_2_failureMessage": f"INCORRECT. {golden.Feedback.iloc[i]}"    
   }
'''
