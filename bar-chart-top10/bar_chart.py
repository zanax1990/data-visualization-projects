# --- Differential Protein Bar Chart (WT vs JR) ---
import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered dataset (only proteins with p < 0.05)
data = pd.read_csv("Significant_Proteins_p0.05.csv")

# Select top 10 most significant proteins for visualization
top_proteins = data.sort_values(by="p_value").head(10)

# Plot mean_WT vs mean_JR as side-by-side bars
plt.figure(figsize=(12, 6))
bar_width = 0.35
x = range(len(top_proteins))

plt.bar([p - bar_width/2 for p in x], top_proteins["mean_WT"],
        width=bar_width, label="WT", alpha=0.8)
plt.bar([p + bar_width/2 for p in x], top_proteins["mean_JR"],
        width=bar_width, label="JR", alpha=0.8)

# Formatting
plt.xticks(x, top_proteins["ProteinName"], rotation=60, ha='right')
plt.xlabel("Proteins")
plt.ylabel("Mean Expression Level")
plt.title("Top 10 Differentially Expressed Proteins (p < 0.05)")
plt.legend()
plt.tight_layout()
plt.show()
