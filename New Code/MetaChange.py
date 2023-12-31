#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:45:09 2023

@author: catermurawski
"""

from panoptes_client import Panoptes, Project, SubjectSet, Subject
from BurstChaser import BurstChaser as bc
Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')

import pandas as pd

proj = Project.find("18664")
burst = SubjectSet()
burst.links.project = proj
burst.display_name= "Golden_Sample"
burst.save()


run = False
file = open("/Users/catermurawski/Desktop/Swift-Research/Golden_Sample/Pulse_shape_practice_list.txt")

GRBname = []
Q1answer = []
Q1feed =[]
Q2answer = []
Q2answer1 = []
Q2feed =[]
Q2feed1 = []
helping = []


def ans1(shape):
    if "extended emission" in shape:
        return 1, "A pulse followed by extended emission."
    elif "A simple pulse" in shape:
        return 0 , "Only one simple pulse."
    elif "Other" in shape:
        return 2, "Other."
    elif "too noisy" in shape:
        return 3, "It is too noisy inside the blue region to see any structures."

        

def ans2(j):
    ans = []
    nums = [] 
    if 'Pulses connected with underlying emission' in j: 
        nums.append(2)
        ans.append("Pulses connected with underlying emission.")
    if 'One or more pulses with symmetrical structure' in j:
        nums.append(0)
        ans.append("One or more pulses with symmetrical structure.")
    if "One or more pulses with the fast-rise and slow-decay shape" in j:
        nums.append(1)
        ans.append("One or more pulses with the fast-rise and slow-decay.")
    if 'Rapid Varying pulses' in j:
        nums.append(3)
        ans.append("Rapidly varying pulses within a large structure.")
    if "I don't see" in j:
        nums.append(4)
        ans.append("I don't see any of these.")
    if "It is too noisy inside the blue region to see any structures." in j:
        nums.append(5)
        ans.append("It is too noisy inside the blue region to see any structures.")
        
    if len(nums) == 1:
        nums.append(-1)
        ans.append("blank")
        
    return nums[0], nums[1], ans[0] , ans[1]
    

for line in file:
    if run == True:
        if "****************************************************" in line:
            break
        seg = line.split("|")
        GRBname.append(seg[0].split(" ")[0])
        one ,two = ans1(seg[1])
        Q1answer.append(one)
        Q1feed.append(two)
        one, one1, two, two1 = ans2(seg[2])
        Q2answer.append(one)
        Q2feed.append(two)
        Q2answer1.append(one1)
        Q2feed1.append(two1)
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
        "Answer1_2": Q2answer1,
        "Feed1_2": Q2feed1,
        "Help": helping}
golden = pd.DataFrame(data)

subject_metadata = {}
count = 1
for i in range(0,golden.shape[0]): 
    answer1 = str(golden.Answer_1.iloc[i])
    feed1 = str(golden.Feed_1.iloc[i])
    answer2 = str(golden.Answer_2.iloc[i])
    feed2 = str(golden.Feed_2.iloc[i])
    answer12 = str(golden.Answer1_2.iloc[i])
    feed12 = str(golden.Feed1_2.iloc[i])
    h = str(golden.Help.iloc[i])
    if answer12 == "-1":
        pass
        
        subject_metadata[f"{bc.findPNG(golden.GRB_Name.iloc[i])}"] = {"#feedback_1_id": str(1),
                                                                      "#feedback_1_answer": answer1,
                                                                      "#feedback_1_failureMessage": feed1,
                                                                      "#feedback_2_id": str(2),
                                                                      "#feedback_2_answer": answer2,
                                                                      "#feedback_2_failureMessage": feed2,
                                                                      "#feedback_4_id": str(4),
                                                                      "#feedback_4_answer": answer2,
                                                                      "#feedback_4_failureMessage": "Look at the info button for more help",
                                                                      "#feedback_5_id": str(5),
                                                                      "#feedback_5_answer": answer1,
                                                                      "#feedback_5_failureMessage": "Look at the info button for more help",
                                                                      "Help": f"{h}"}
        
    else:
        subject_metadata[f"{bc.findPNG(golden.GRB_Name.iloc[i])}"] = {"#feedback_1_id": str(1),
                                                                      "#feedback_1_answer": answer1,
                                                                      "#feedback_1_failureMessage": feed1,
                                                                      "#feedback_2_id": str(2),
                                                                      "#feedback_2_answer": answer2,
                                                                      "#feedback_2_failureMessage": feed2,
                                                                      "#feedback_3_id": str(3),
                                                                      "#feedback_3_answer": answer12,
                                                                      "#feedback_3_failureMessage": feed12,
                                                                      "#feedback_4_id": str(4),
                                                                      "#feedback_4_answer": answer2,
                                                                      "#feedback_4_failureMessage": "Look at the info button for more help",
                                                                      "#feedback_5_id": str(5),
                                                                      "#feedback_5_answer": answer1,
                                                                      "#feedback_5_failureMessage": "Look at the info button for more help",
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
