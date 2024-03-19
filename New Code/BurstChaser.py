from panoptes_client import Panoptes, Project, SubjectSet, Subject, Workflow
import numpy as np
import pandas as pd

'''https://www.zooniverse.org/projects/murawskic1/carter-project'''
#OPEN PANPOTRES AND FIND RIGHT PROJECT
Panoptes.connect(username='MurawskiC1', password='Cartbellot4ti$')
count = 0 
RETIRE = False

class BurstChaser():
    def __init__(self, Burst_Name, BurstID, workflow, Verify = None):
        self.Burst_Name = Burst_Name
        self.BurstID = BurstID
        self.workflow = workflow
        self.Verify = Verify
        self.contributers = []
        


    
    @property
    def Burst_Name(self):
        return self._Burst_Name
    
    @Burst_Name.setter
    def Burst_Name(self, i):
        self._Burst_Name = i
    
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
        
    def retire(self):
        global count, RETIRE
        if self.Verify != None:
            count += 1
            if RETIRE == True:
                print("hello")
                '''
                workflow = Workflow.find(f"{self.workflow}")
                workflow.retire_subjects(f"{self.BurstID}")
                '''
  

        
        
    def contributersAdd(self, c):
        self.contributers.append(c)
    
    def findPNG( name):
        import os
        path = "/Users/catermurawski/Desktop/Swift-Research/BurstPhotos"
        for filename in os.listdir(path):
            if name in filename:
                if os.path.isfile(os.path.join(path, filename)):  # Check if it's a file and not a directory
                    return(f"{path}/{filename}")
            
    def __lt__(self, other):
        return self.BurstID < other.BurstID
   

#This Class will start to rank all the bursts and catagorize them by their 
class PulseShape(BurstChaser):
    def __init__(self, Burst_Name, BurstID, workflow):
        super().__init__(Burst_Name, BurstID, workflow)
        self.Follow = [0,0,0,0,0,0]
        self.Shape = [0,0,0,0]
    
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
            self.Follow[2] += 1
        if 'symmetrical structure' in j:
            self.Follow[0] += 1
        if "One or more pulses with the fast-rise and slow-decay shape." in j:
            self.Follow[1] += 1
        if 'Rapid Varying pulses' in j:
            self.Follow[3] += 1
        if "I don't see any of these" in j:
            self.Follow[4] += 1
        if "too noisy" in j:
            self.Follow[5] += 1

    def ShapeCount(self, shape):
        if "extended emission" in shape:
            self.Shape[1] += 1
        elif "simple pulse" in shape:
            self.Shape[0] += 1
        elif "Other." in shape:
            self.Shape[2] +=1
        elif "too noisy" in shape:
            self.Shape[3] +=1
        #Verify iif burst has met the requirements
        self.NewVerify()

    def NewVerify(self):
        num = 10 
        total = self.Shape[0] + self.Shape[1] + self.Shape[2]+self.Shape[3]
        conf = 0.80
        max = 0
        index = 10
        if total >= num:
            for i in range(0,len(self.Shape)):
                if self.Shape[i] > max:
                    max = self.Shape[i]
                    index = i 
            for i in range(0,len(self.Shape)):
                if self.Shape[index] /(self.Shape[i]+ self.Shape[index]) <= conf and i != index:
                    index = None
                    break
        if index == 0 :
            self.Verify = "Simple"
        elif index == 1:
            self.Verify = "Extended"
        elif index == 2:
            self.Verify = "Other"
        elif index == 3:
            self.Verify = "Too Noisy"
        else:
            self.Verify = None
                

        
                


       
    def VerifyBurst(self):
        num = 10
        total = self.Shape[0] + self.Shape[1] + self.Shape[2]+self.Shape[3]
        conf = 0.80
        if self.Shape[0] > num and self.Shape[0]/total >= conf:
            self.Verify = "Simple"
        elif self.Shape[1] > num and self.Shape[1]/total >= conf:
            self.Verify = "Extended"
        elif self.Shape[2] > num and self.Shape[2]/total >= conf:
            self.Verify = "Other"
        elif self.Shape[3] > num and self.Shape[3]/total >= conf:
            self.Verify = "Too Noisy"
        else:
            self.Verify = None
            
    def export(name, pulse_list):
        pulse_list = sorted(pulse_list)
        data = {'Burst Name': [i.Burst_Name for i in pulse_list],
                'Workflow': [i.workflow for i in pulse_list],
                'BurstID': [i.BurstID for i in pulse_list],
                'Simple': [i.Shape[0] for i in pulse_list],
                'Extended': [i.Shape[1] for i in pulse_list],
                'Other': [i.Shape[2] for i in pulse_list],
                'Too Noisy': [i.Shape[3] for i in pulse_list],
                "Verify": [i.Verify for i in pulse_list],
                'Follow': [i.Follow for i in pulse_list]
                }
        df = pd.DataFrame(data)
        #creates data frame as csv file 
        df.to_csv(f'/Users/catermurawski/Desktop/Swift-Research/CSVExports/{name}.csv', index = False, header = True)
            


#class for the Pulse or noise
class PulseNoise(BurstChaser):
    def __init__(self, Burst_Name, BurstID, workflow):
        super().__init__(Burst_Name, BurstID, workflow)
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
        pulse_list = sorted(pulse_list)
        data = {'Burst Name': [i.Burst_Name for i in pulse_list],
                'Burst ID': [i.BurstID for i in pulse_list],
                'Pulse': [i.classification[0] for i in pulse_list],
                "Noise": [i.classification[1] for i in pulse_list],
                'Cant Tell': [i.classification[2] for i in pulse_list],
                'No Response': [i.classification[3] for i in pulse_list]
                }
        df = pd.DataFrame(data)
        #creates data frame as csv file 
        df.to_csv(f'/Users/catermurawski/Desktop/Swift-Research/CSVExports/{name}.csv', index = True, header = True)


class PulseLocation(BurstChaser):
    def __init__(self, Burst_Name, BurstID, workflow):
        super().__init__(Burst_Name, BurstID, workflow)
        self.locations =  []
        self.final_locations= []
        self.count = 0 

    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self ,i):
        self._count = i
    
    @property
    def locations(self):
        return self._locations

        
    @locations.setter
    def locations(self, i):
        self._locations = i
    
    @property
    def final_locations(self):
        return self._final_locations

        
    @final_locations.setter
    def final_locations(self, i):
        self._final_locations = i

    def multimode(self, x):
        n = 4
        out = []
        for i in x:
            c = x.count(i)
            if c >= n and i not in out:
                out.append(i)
        return out
            
    def finalize(self): 
        import numpy as np
        from outliers import smirnov_grubbs as grubbs
 
        x = []
        for i in self.locations:
            x.append(i.x-i.x%10)
        
        x = self.multimode(x)
        for i in x:
            seg = []
            loc = [[],[],[],[]]
            for j in range(0, len(self.locations)):
                if self.locations[j].x <= float(i+10) and self.locations[j].x >= float(i-10):
                    seg.append(self.locations[j])
            if len(seg) > 0:
                for k in seg:
                    loc[0].append(k.x)
                    loc[1].append(k.y)
                    loc[2].append(k.width)
                    loc[3].append(k.height)      
                self.final_locations.append(Location(np.mean(np.mean(grubbs.test(loc[0],0.1))),np.mean(grubbs.test(loc[1],0.1)),np.mean(grubbs.test(loc[2],0.1)),np.mean(grubbs.test(loc[3],0.1))))
                    

    def redboxes(self):
        from PIL import Image, ImageDraw
        
        loc = self.locations

        

                        
                
        def add_transparent_rectangle(input_image_path, output_image_path, rectangle_position, rectangle_size):
            # Open the image
            try:
                img = Image.open(input_image_path).convert("RGBA")
              
                #draw an image of rectangle
                draw = ImageDraw.Draw(img)
                draw.rectangle([rectangle_position[0], rectangle_position[1],rectangle_position[0] + rectangle_size[0], rectangle_position[1] + rectangle_size[1]],outline="red")
                # Save the result
                img.save(output_image_path)
            except:
                pass
            
        x = self._Burst_Name
        png = self.findPNG(x)
        # Example usage:
        input_image_path = f"/Users/catermurawski/Desktop/Swift-Research/BurstPhotos/{png}"

        output_image_path = f"/Users/catermurawski/Desktop/Swift-Research/Boxes/{self.BurstID}.png"
        for i in range(0,len(loc)):
            rectangle_position = (loc[i].x, loc[i].y)  # X and Y coordinates of the top-left corner of the rectangle
            rectangle_size = (loc[i].width,loc[i].height)# Width and height of the rectangle
    
            add_transparent_rectangle(input_image_path, output_image_path, rectangle_position, rectangle_size)
            input_image_path = f"/Users/catermurawski/Desktop/Swift-Research/Boxes/{self.BurstID}.png"


        
        
    def read(self, a):
        a = a.split(' which is automatically determined by a computer algorithm.","value":[')[1]
        self._count += 1
        if '},{' in a:
            a = a.split('},{')
        else:
            a = [a]
        for i in a:
            cata = i.split(",")
            if len(cata) >4:
                loc = Location(float(cata[0].split(":")[1]),float(cata[1].split(":")[1]), float(cata[4].split(":")[1]),float(cata[5].split(":")[1]))
                self.locations.append(loc)
 
        
    def findPNG(self, name):
        import os
        path = "/Users/catermurawski/Desktop/Swift-Research/BurstPhotos"
        for filename in os.listdir(path):
            if name in filename:
                if os.path.isfile(os.path.join(path, filename)):  # Check if it's a file and not a directory
                    return(filename)
            
            
    def findGRB(self, sid):
        file = pd.read_csv("GRB_IDS_Names.csv")
        file.set_index('Subject_ID', inplace=True)

        return file.loc[sid,'GRB_Names']
               
            
            
    def export(name, pulse_list):
        Burst_Name = []
        BurstID =[]
        l = []
        c = []
        
        for i in sorted(pulse_list):
            if len(i.locations) != 0:
                Burst_Name.append(i.Burst_Name)
                BurstID.append(i.BurstID)
                l.append(len(i.final_locations)+1)
                c.append(i.count)

        
        
        data = {'Burst Name': Burst_Name,
                'Burst ID': BurstID,
                'Boxes': l,
                'Count': c

                }
        df = pd.DataFrame(data)
        #creates data frame as csv file 
        df.to_csv(f'/Users/catermurawski/Desktop/Swift-Research/CSVExports/{name}.csv', index = True, header = True)
        

                    


        


class Location():
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @x.setter
    def x(self, i):
        self._x = i
    
    @y.setter
    def y(self, i):
        self._y = i
        
    @width.setter
    def width(self, i):
        self._width = i
    
    @height.setter
    def height(self, i):
        self._height = i

''' 
    def redbox(self):
        from scipy import stats
        
        from PIL import Image, ImageDraw
        
        def add_transparent_rectangle(input_image_path, output_image_path, rectangle_position, rectangle_size):
            # Open the image
            img = Image.open(input_image_path).convert("RGBA")
          
            #draw an image of rectangle
            draw = ImageDraw.Draw(img)
            draw.rectangle([rectangle_position[0], rectangle_position[1],rectangle_position[0] + rectangle_size[0], rectangle_position[1] + rectangle_size[1]],outline="red")
            # Save the result
            img.save(output_image_path)
            
        x = self.Burst_Name
        png = self.findPNG(x)
        # Example usage:
        input_image_path = f"/Users/catermurawski/Desktop/Swift-Research/BurstPhotos/{png}"

        output_image_path = f"/Users/catermurawski/Desktop/Swift-Research/Boxes/{self.BurstID}.png"
        rectangle_position = (stats.trim_mean(self.xloc,0.2), stats.trim_mean(self.yloc,0.2))  # X and Y coordinates of the top-left corner of the rectangle
        rectangle_size = (stats.trim_mean(self.width,0.2), stats.trim_mean(self.height,0.2))# Width and height of the rectangle

        add_transparent_rectangle(input_image_path, output_image_path, rectangle_position, rectangle_size)
    
    '''