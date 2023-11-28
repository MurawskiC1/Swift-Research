from panoptes_client import Panoptes, Project, SubjectSet, Subject, Workflow
import numpy as np
import pandas as pd

'''https://www.zooniverse.org/projects/murawskic1/carter-project'''
#OPEN PANPOTRES AND FIND RIGHT PROJECT
Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')


class BurstChaser():
    def __init__(self, BurstID, workflow, Verify = None):
        self.BurstID = BurstID
        self.workflow = workflow
        self.Verify = Verify
        self.contributers = []
    
    @property
    def BurstID(self):
        return self._BurstID
    
    @BurstID.setter
    def BurstID(self, i):
        self._BurstID = i
        
    @property
    def workflow(self):
        return self._workflow 
    
    @workflow.setter
    def workflow(self, i):
        self._workflow = i
    @property
    def contributers(self):
        return self._contributers 
    
    @contributers.setter
    def contributers(self, i):
        self._contributers = i
    @property
    def Verify(self):
        return self._Verify
    
    @Verify.setter
    def Verify(self, v):
        self._Verify = v
        
    def contributersAdd(self, c):
        self.contributers.append(c)
   

#This Class will start to rank all the bursts and catagorize them by their 
class PulseShape(BurstChaser):
    def __init__(self, BurstID, workflow):
        super().__init__(BurstID, workflow)
        self.Follow = [0,0,0,0,0]
        self.Shape = [0,0,0]

    @property
    def Shape(self):
        return self._Shape
    
    @property
    def Follow(self):
        return self._Follow
    
    @Shape.setter
    def Shape(self, i):
        self._Shape = i 
    #The japanese wife that I met online and I are hitting it off pretty well and let me tell you, i am so in love with her. Im moving next week. WOW!
    
    
        
    @Follow.setter
    def Follow(self, f):
        self._Follow = f

    def __str__(self):
        #return f"{self.BurstID}:  Simple:{self.Shape[0]}  Ext:{self.Shape[1]}  Other:{self.Shape[2]} Follow Up:{self.Follow}"
        return f"{self.BurstID}:  Shape:{self.Shape}  Follow Up:{self.Follow} Verified:{self.Verify}"
    
    
    #code to add to definer array
    def FollowCount(self, j):
        if 'Pulses connected with underlying emission.' in j: 
            self.Follow[0] += 1
        if 'One or more pulses with symmetrical structure.' in j:
            self.Follow[1] += 1
        if "One or more pulses with the fast-rise and slow-decay shape." in j:
            self.Follow[2] += 1
        if 'Rapid Varying pulses' in j:
            self.Follow[3] += 1
        if "I don't see any of these." in j:
            self.Follow[4] += 1   

    def ShapeCount(self, shape):
        if "A pulse followed by extended emission" in shape:
            self.Shape[1] += 1
        elif "A simple pulse." in shape:
            self.Shape[0] += 1
        elif "Other." in shape:
            self.Shape[2] +=1
        #Verify iif burst has met the requirements
        self.VerifyBurst()
        
    def VerifyBurst(self):
        num = 10
        total = self.Shape[0] + self.Shape[1] + self.Shape[2]
        conf = 0.50
        if self.Shape[0] > num and self.Shape[0]/total >= conf:
            self.Verify = "Simple"
        elif self.Shape[1] > num and self.Shape[1]/total >= conf:
            self.Verify = "Extended"
        elif self.Shape[2] > num and self.Shape[2]/total >= conf:
            self.Verify = "Other"
        else:
            self.Verify = None
            
    def export(name, pulse_list):
        data = {'Number': np.arange(1,len(pulse_list)+1),
                'Workflow': [i.workflow for i in pulse_list],
                'BurstID': [i.BurstID for i in pulse_list],
                'Simple': [i.Shape[0] for i in pulse_list],
                'Extended': [i.Shape[1] for i in pulse_list],
                'Other': [i.Shape[2] for i in pulse_list],
                "Verify": [i.Verify for i in pulse_list],
                'Follow': [i.Follow for i in pulse_list]
                }
        df = pd.DataFrame(data)
        #creates data frame as csv file 
        df.to_csv(f'{name}.csv', index = False, header = True)
            


#class for the Pulse or noise
class PulseNoise(BurstChaser):
    def __init__(self, BurstID, workflow):
        super().__init__(BurstID, workflow)
        self.classification = [0,0,0,0]
        
  
    @property
    def classification(self):
        return self._classification

        
    @classification.setter
    def classification(self, i):
        self._classification = i
        
    def classCount(self, a):
        if "This is a pulse." in a:
            self.classification[0] += 1
            
        elif "This is noise." in a:
            self.classification[1] += 1
        elif "It's hard to tell." in a: 
            self.classification[2] += 1
        else:
            self.classification[3] += 1
    
    def __str__(self):
        return f"{self.BurstID}: Classification: {self.classification}"
    
    def export( name, pulse_list):
        data = {'Number': np.arange(1,len(pulse_list)+1),
                'Burst ID': [i.BurstID for i in pulse_list],
                'Pulse': [i.classification[0] for i in pulse_list],
                "Noise": [i.classification[1] for i in pulse_list],
                'Cant Tell': [i.classification[2] for i in pulse_list],
                'No Response': [i.classification[3] for i in pulse_list]
                }
        df = pd.DataFrame(data)
        #creates data frame as csv file 
        df.to_csv(f'{name}.csv', index = False, header = True)



        


            
            
        
        
        
        