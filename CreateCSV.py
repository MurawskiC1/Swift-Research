#through the data, find the (shape,user,id), make a table of it all,
# 2: F
import pandas as pd
import numpy as np
fhand = open('pulse-shapes-classifications.csv')

shap = []
user = []
count = 0
definer = []
id = []
first = False

#find commas without a " in them


#ASSIGNMENT
#create empty array for the 2nd follow up question
#Create a function to find the extra answers
#append it in the for loop


#shape function that allows you to find a string in the values    
def shape(i):
    if 'A simple pulse.' in i: 
        return "Simple Pulse"
    elif i.find('A pulse followed by extended emission') != -1:
        return "Extended Emmissions"
    elif i.find("Other.") != -1:
        return "Other"
    else:
        return "Nothing found"
def follow(j):
    if 'Pulses connected with underlying emission.' in j: 
        return "Underlying emission"
    elif 'One or more pulses with symmetrical structure.' in j:
        return "Symmetrical Structure"
    elif "One or more pulses with the fast-rise and slow-decay shape." in j:
        return "Fast.R Slow.D"
    elif 'Rapidly varying pulses.' in j:
        return "Rapid Varying pulses"
    else:
        return "Nothing found"
    
#runs through all the lines in the file and splits them bu commas, adds them to different variables depending on info i want
for i in fhand:
    if first == True and shape(i) != "Nothing found":
        #here i split sting into array
        column = i.split(",")
        
        #append easy to find values
        user.append(column[1])
        id.append(column[-1].strip())
        definer.append(follow(i))
        #uses the shape find to append shape to an array
        shap.append(shape(i))
        count +=1
    #this is so it doesn't read first line    
    first = True

#format into dictionary then put in data fram
data = {'Number': np.arange(1,count+1), 'User': user, 'ID': id, 'Shape': shap, 'Definer': definer}
df = pd.DataFrame(data)

print(df)

#creates data frame as csv file 
df.to_csv(r'DataSet.csv', index = False, header = True)


