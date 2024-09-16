import numpy as np

arr = np.array([8,14,3,1])

#Null hypothosis is that everything is evenly distributed at 5
#alternetice is that they are NOT evenly distributed

mean = sum(arr)/len(arr) #this is our expected

#Now we find the chi squared statistics

# X^2 = summation(observed-expected)^2/expected
chi = 0
for i in arr:
    chi += (i - mean)**2
    
chi = chi / mean

print(chi)


df = len(arr)
