# 🌋 Volcano Plot of Differential Protein Expression

This Python script generates a volcano plot visualizing the statistical significance and fold change of protein expression between WT and JR groups.

## 📊 What It Does
- Loads the full differential expression results
- Calculates `-log10(p-value)` for visualization
- Highlights significant proteins based on `p-value` and `log2FC` thresholds
- Draws a volcano plot with color-coded points for different significance levels

## 📦 Requirements
- Python 3.9+
- pandas
- matplotlib
- numpy

## 🚀 Usage
```bash
python volcano_plot.py
