#The Goal of this is to use bar chart statistical methods rather than distribution because we don't have data for a distribution
#We may need distributions when using the locations
import numpy as np

#STANDARD deviation
#Has to be of a sample
#equation-> sqrt(summation(x-mean)^2/(n-1)) gotten off of khan academy


arr = np.array([10,13,12,2])

mean = sum(arr)/len(arr)
n = len(arr)

summation = 0
for i in arr:
    summation += (i - mean)**2
    
std = np.sqrt(summation/(n-1))

print(std)


#THEN WE CALCULATE STANDARD ERROR
se =  std / sqrt(n)
