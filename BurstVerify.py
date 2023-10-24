#Creates all the classes for the bursts 


#Finds a singular burst id and see if it has been catoagorized as the same thing over and over


'''
need at least 20 people and 80% to verify

extra layer of questions

combine two codes
'''
import Burst as bst


            
               

    
file = open('DataSet.csv')

Bursts = []
Ids = []
title = False

for i in file:
    new = i.strip()
    arr = new.split(",")
    if arr[2] not in Ids and title == True:
        Bursts.append(bst.Burst(arr[2]))
        Ids.append(arr[2])
    for x in Bursts:
        if arr[2] in x.BurstID:
            #adds the burst type
            x.Definer(arr[4])
            x.Count(arr[3])
    title = True
#sh = input("What shape do you want?")

    
for i in Bursts:
    if i.Verify != None:
        print(f"\n VERIFIED    {i.BurstID} Verified: {i.Verify}")
    print(i)

    
    
        

    


    