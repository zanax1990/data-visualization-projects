# Interactive KDE Dashboard

This notebook explores the distribution of daily COVID-19 cases. It compares kernel density estimates across bandwidths and kernels, applies a log10 transformation, compares selected countries, and builds a small Dash interface for U.S. case data.

## Input

The notebook expects `/content/Covid19-data.csv` and uses these columns:

- `location`
- `new_cases`

The dataset is not included.

## Run

```bash
jupyter notebook interactive-dash-app/interactive-dash-app.ipynb
```

To run outside Colab, change the input path in the first cell. The notebook contains executed outputs from the original run.
