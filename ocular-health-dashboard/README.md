# Ocular Health Visualization Suite

This project extends the research narrative around the **ODIR-5K** eye disease dataset and the Schwann cell regeneration studies in the cornea. It demonstrates how curated biomedical tables can be transformed into actionable visuals and interactive dashboards.

## Project structure

```
ocular-health-dashboard/
├── analysis.py              # Generates static plots (heatmaps, box/violin plots, clustering)
├── dashboard_app.py         # Plotly Dash interface for real-time exploration
├── data/
│   └── ocular_health_sample.csv  # Lightweight demo subset inspired by ODIR-5K
├── data_utils.py            # Shared helpers for loading data and clustering
├── outputs/                 # Saved figures after running analysis.py
└── requirements.txt         # Optional dependency pinning
```

## How to use the analysis workflow

1. (Optional) create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Generate the static figures discussed in the manuscript:

   ```bash
   python analysis.py
   ```

   The following plots are saved into the `outputs/` directory:

   * `correlation_heatmap.png` – correlation heatmap between demographics, Schwann metrics, and diagnoses.
   * `age_by_disease_boxplot.png` – box/strip plot of patient ages per diagnosis.
   * `schwann_density_violin.png` – violin plot of Schwann cell density vs. diagnosis.
   * `age_vs_regeneration.png` – scatter plot of age vs. corneal nerve regeneration rate.
   * `cluster_scatter.png` – PCA projection of k-means clusters for patient subgroup discovery.

## Interactive dashboard (Plotly Dash)

Launch the dashboard to explore the dataset live and reproduce the figures from the paper:

```bash
python dashboard_app.py
```

The app exposes:

* **Correlation heatmap** for demographics vs. disease burden.
* **Age filter & disease selector** to drive the age boxplot, Schwann cell violin plot, and age vs. regeneration scatter.
* **Cluster explorer** that highlights PCA components and the patient subgroups obtained from k-means.

Because the demo dataset is small, the dashboard starts instantly but the layout is ready to scale to the full ODIR-5K cohort.
