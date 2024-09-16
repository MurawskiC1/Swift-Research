import numpy as np
import scipy.stats as stats

# Given array
data = np.array([6,5,5,5])

# Mean and standard deviation of the array
mean = np.mean(data)
std_dev = np.std(data, ddof=1)
n = len(data)

# Calculating t-statistics, p-values, and confidence intervals
t_stats = (data - mean) / (std_dev / np.sqrt(n))
p_values = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=n-1)) 

conf = 1 - p_values

print(t_stats)
print(p_values)
print(conf)



