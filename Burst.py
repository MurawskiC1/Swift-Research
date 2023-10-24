#This Class will start to rank all the bursts and catagorize them by their 
class Burst():
    def __init__(self, BurstID, Verify = None):
        self.BurstID = BurstID
        self.Follow = [0,0,0,0]
        self.Shape = [0,0,0]
        self.Verify = Verify
        
    @property
    def BurstID(self):
        return self._BurstID
   
    
    @property
    def Verify(self):
        return self._Verify
    
    @property
    def Shape(self):
        return self._Shape
    
    @property
    def Follow(self):
        return self._Follow
    
    @BurstID.setter
    def BurstID(self, i):
        self._BurstID = i
        
    @Shape.setter
    def Shape(self, i):
        self._Shape = i 
    #The japanese wife that I met online and I are hitting it off pretty well and let me tell you, i am so in love with her. Im moving next week. WOW!
    
    @Verify.setter
    def Verify(self, v):
        self._Verify = v
        
    @Follow.setter
    def Follow(self, f):
        self._Follow = f

    def __str__(self):
        return f"{self.BurstID}:  Simple:{self.Shape[0]}  Ext:{self.Shape[1]}  Other:{self.Shape[2]} Follow Up:{self.Follow}"
    
    
    #code to add to definer array
    def Definer(self, j):
        if "Underlying emission" in j: 
            self.Follow[0] += 1
        elif "Symmetrical Structure" in j:
            self.Follow[1] += 1
        elif "Fast.R Slow.D" in j:
            self.Follow[2] += 1
        elif 'Rapid Varying pulses' in j:
            self.Follow[3] += 1
        else:
            return "Nothing found"
        
    def Count(self, shape):
        if "Extende" in shape:
            self.Shape[1] += 1
        elif "Simple" in shape:
            self.Shape[0] += 1
        elif "Other" in shape:
            self.Shape[2] +=1
        else:
            pass
        #Verify iif burst has met the requirements
        self.VerifyBurst()
        
    def VerifyBurst(self):
        num = 1
        total = self.Shape[0] + self.Shape[1] + self.Shape[2]
        conf = 0.50
        if self.Shape[0] > num and self.Shape[0]/total >= conf:
            self.Verify = "Simple"
        elif self.Shape[1] > num and self.Shape[1]/total >= conf:
            self.Verify = "Extended"
        elif self.Shape[2] > num and self.Shape[2]/total >= conf:
            self.Verify = "Other"

#Create user class that takes in the usernam and if the user is 
class User():
    def __init__(self, Name, Flag=True):
        self.name = Name
        self.flag = Flag
        
    @property
    def name(self):
        return self._name
    @property
    def flag(self):
        return self._flag
    
    @name.setter
    def name(self, n):
        self._name