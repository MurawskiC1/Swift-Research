from panoptes_client import Panoptes, Project, SubjectSet, Subject, Workflow
import numpy as np
import pandas as pd

'''https://www.zooniverse.org/projects/murawskic1/carter-project'''
#OPEN PANPOTRES AND FIND RIGHT PROJECT
Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')

project = Project.find("22619")
