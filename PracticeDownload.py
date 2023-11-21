from panoptes_client import Panoptes, Project, SubjectSet, Subject
import sys

Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')

BurstProject = Project.find("18664")

golden  = SubjectSet.find(104329)

for i in golden.subjects:
    print(i)



