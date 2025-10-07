# --- Volcano Plot for Differentially Expressed Proteins ---
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the full differential results (not just p<0.05)
data = pd.read_csv("Differential_results .csv")

# Add -log10(p-value) for visualization
data["neg_log10_p"] = -np.log10(data["p_value"])

# Define thresholds
fc_threshold = 1        # |log2FC| > 1 = biologically meaningful
p_threshold = 0.05      # p-value < 0.05 = statistically significant

# Define color categories
colors = []
for _, row in data.iterrows():
    if row["p_value"] < p_threshold and abs(row["log2FC"]) > fc_threshold:
        colors.append("red")      # significant up/down
    elif row["p_value"] < p_threshold:
        colors.append("orange")   # p significant but small fold change
    else:
        colors.append("gray")     # not significant
data["color"] = colors

# Create volcano plot
plt.figure(figsize=(10, 6))
plt.scatter(data["log2FC"], data["neg_log10_p"], c=data["color"], alpha=0.7, edgecolors='k', s=50)

# Add threshold lines
plt.axvline(x=fc_threshold, color='blue', linestyle='--')
plt.axvline(x=-fc_threshold, color='blue', linestyle='--')
plt.axhline(y=-np.log10(p_threshold), color='green', linestyle='--')

# Labels and style
plt.xlabel("log2 Fold Change (JR vs WT)")
plt.ylabel("-log10(p-value)")
plt.title("Volcano Plot of Differential Protein Expression")
plt.tight_layout()
plt.show()
