import pandas as pd
import numpy as np
import scipy.stats as stats

# Load the data
file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')

# Define columns to process
columns_to_process = ['Simple', 'Extended', 'Other', 'Too_Noisy']

def classification(n):
    if n == 0:
        return 'Simple'
    if n == 1:
        return "Extended"
    if n == 2:
        return "Other"
    if n == 3:
        return "Too_Noisy"

# Initialize lists for z-scores, p-values, and confidence levels
zscore = []
p_value = []
confidence_level = []
verify = []
final_confidence = []

# Calculate z-scores, p-values, and confidence levels for each column
for col in columns_to_process:
    norm = file[col] / file[columns_to_process].sum(axis=1)
    z = [(x - norm.mean()) / norm.std() for x in norm]
    zscore.append(z)
    
    # Calculate p-values for the z-scores
    p = [2 * (1 - stats.norm.cdf(abs(score))) for score in z]
    p_value.append(p)
    
    # Calculate confidence levels
    confidence = [1 - pval for pval in p]
    confidence_level.append(confidence)

for i in range(len(file)):
    c = ""
    a = []
    fc = []
    lc = [] 
    
    for j, col in enumerate(columns_to_process):
        if zscore[j][i] > 0 and confidence_level[j][i] >= 0.60:
            a.append(j)
            fc.append(confidence_level[j][i])
        elif zscore[j][i] > 0:
            lc.append(confidence_level[j][i])
            
    if len(a) == 2:
        c = classification(a[0])+"/"+classification(a[1])
    elif len(a) == 1 and confidence_level[a[0]][i] >= 0.70:
        c = classification(a[0])
        
    if len(a) > 0:
        final_confidence.append(sum(fc) / len(fc))
    else:
        final_confidence.append(sum(lc) / len(lc))
    
    verify.append(c)

# Create a new DataFrame with BurstName and calculated statistics
results = pd.DataFrame({
    'Burst_Name': file['Burst_Name'], 
    'BurstID': file['BurstID'], 
    'Burst_PNG': file['Burst_PNG'],
    'Simple': file['Simple'], 
    'Extended': file['Extended'], 
    'Other': file['Other'], 
    'Too_Noisy': file['Too_Noisy'], 
    'Symmetrical': file['Symmetrical'],
    'FastRiseSlowDecay': file['FastRiseSlowDecay'],
    'UnderlyingEmission': file['UnderlyingEmission'],
    'RapidlyVarying': file['RapidlyVarying'],
    'Verify': verify,
    'Simple_Zscore': zscore[0], 
    'Simple_Pvalue': p_value[0], 
    'Simple_Confidence': confidence_level[0],
    'Extended_Zscore': zscore[1], 
    'Extended_Pvalue': p_value[1], 
    'Extended_Confidence': confidence_level[1],
    'Other_Zscore': zscore[2], 
    'Other_Pvalue': p_value[2], 
    'Other_Confidence': confidence_level[2],
    'Too_Noisy_Zscore': zscore[3], 
    'Too_Noisy_Pvalue': p_value[3], 
    'Too_Noisy_Confidence': confidence_level[3],
    'Final_Confidence': final_confidence
})

# Export the results to a CSV file
results.to_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape_Results.csv', index=False)

print("CSV file with results has been saved.")
