# 🧬 Top 10 Differentially Expressed Proteins Bar Chart

This Python script generates a bar chart comparing the mean expression levels of the top 10 most significant proteins between WT and JR groups.

## 📊 What It Does
- Loads a filtered dataset with proteins where `p < 0.05`
- Sorts proteins by significance and selects the top 10
- Plots mean expression levels of WT and JR side-by-side for comparison

## 📦 Requirements
- Python 3.9+
- pandas
- matplotlib

## 🚀 Usage
```bash
python bar_chart.py
