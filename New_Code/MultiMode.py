import numpy as np
import scipy.stats as stats


arr = [20,18,15,2]
mean = np.mean(arr)
std = np.std(arr)
zscore = (arr - mean)/std
pvalue = stats.norm.sf(zscore)
conf = 1 - pvalue



print(f"Zscore: {zscore}")
print(f"Pvalue: {pvalue}")
print(f"Conf: {conf}")