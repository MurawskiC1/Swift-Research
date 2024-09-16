import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the data
file = pd.read_csv('/Users/catermurawski/desktop/Swift-Research/CSVExports/Pulse_Shape.csv')

# Define columns to process
columns_to_process = ['Simple', 'Extended', 'Other', 'Too_Noisy']

# Initialize lists for median, std, z-scores, and confidence levels
median = []
std = []
zscore = []
p_value = []
confidence_level = []

# Calculate median, std, z-scores, and confidence levels for each column
for col in columns_to_process:
    norm = file[col] / file[columns_to_process].sum(axis=1)
    
    # Calculate median and standard deviation
    med = np.median(norm)
    median.append(med)
    std_dev = norm.std()
    std.append(std_dev)
    
    # Calculate z-scores based on the median
    z = [(x - med) / std_dev for x in norm]
    zscore.append(z)
    
    # Calculate p-values for the z-scores
    p = [2 * (1 - stats.norm.cdf(abs(score))) for score in z]
    p_value.append(p)
    
    # Calculate confidence levels
    confidence = [1 - pval for pval in p]
    confidence_level.append(confidence)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Flatten axes for easy iteration
axes = axes.flatten()

# Plot histograms and overlay the standard normal PDF and CDF for each category centered around the median
for i, col in enumerate(columns_to_process):
    ax = axes[i]
    
    # Plot histogram of the z-scores
    ax.hist(zscore[i], bins=30, density=True, alpha=0.6, color='g', label='Z-Scores Histogram')
    
    # Plot the standard normal distribution curve centered around the median
    x = np.linspace(-3, 3, 100)
    p = stats.norm.pdf(x, 0, 1)  # Standard normal distribution (mean=0, std=1)
    ax.plot(x, p, 'k', linewidth=2, label='Standard Normal PDF')
    
    # Plot the standard normal CDF
    cdf = stats.norm.cdf(x, 0, 1)  # Standard normal CDF
    ax.plot(x, cdf, 'r--', linewidth=2, label='Standard Normal CDF')
    
    # Add title and labels
    ax.set_title(f'{col} Z-scores Centered on Median')
    ax.set_xlabel('Z-score')
    ax.set_ylabel('Density / Cumulative Probability')
    ax.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
