#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:44:33 2023

@author: catermurawski
"""
from panoptes_client import Panoptes, Project, SubjectSet, Subject, Workflow
Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')
import pandas as pd

GRB =Project.find("18664")

burst = SubjectSet.find("114309")
subject_ids = []
GRB_names = []
for i in burst.subjects:
    subject_ids.append(i.id)
    b = i.metadata["SIMBAD"].split("=")[1].split("&")[0]
    GRB_names.append(b)

    
data = {"Subject_ID": subject_ids, "GRB_Names": GRB_names}
frame = pd.DataFrame(data)
frame.to_csv("GRB_IDS_Names.csv", index=True, header=True)

    
    
    