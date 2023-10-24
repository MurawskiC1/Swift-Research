#through the data, find the (shape,user,id), make a table of it all,
# 2: F
import pandas as pd
import numpy as np
fhand = open('burst-chaser-classifications.csv')

shap = []
user = []
singname = []
count = 0
total = 0
s = 0
e = 0
o = 0 
id = []
first = False

#find commas without a " in them


    
def shape(i):
    if 'A simple pulse.' in i: 
        return "Simple Pulse"
    elif 'A pulse followed by extended emission' in i:
        return "Extended Emmissions"
    elif "Other." in i:
        return "Other"
    else:
        return "Nothing found"
    
#runs through all the lines in the file and splits them bu commas, adds them to different variables depending on info i want
for i in fhand:
    if first == True and shape(i) != "Nothing found":
        column = i.split(",")
        user.append(column[1])
        id.append(column[-1].strip())
        shap.append(shape(i))
        total+=1
        count +=1
    #this is so it doesn't read first line    
    first = True

#format into dictionary then put in data fram
data = {'Number': np.arange(1,count+1), 'User': user, 'ID': id, 'Shape': shap}
df = pd.DataFrame(data)

print(df)

#creates data frame as csv file 
df.to_csv(r'DataSet.csv', index = False, header = True)


