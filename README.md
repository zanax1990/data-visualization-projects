# Data Visualization Projects

A small collection of Python visualization exercises covering proteomics results and COVID-19 case distributions.

| Project | Purpose | Main tools |
|---|---|---|
| `bar-chart-top10` | Compare mean expression for the ten proteins with the smallest supplied p-values | pandas, Matplotlib |
| `volcano-plot` | Plot log2 fold change against statistical significance | pandas, NumPy, Matplotlib |
| `interactive-dash-app` | Explore kernel density estimates of daily COVID-19 cases | pandas, scikit-learn, SciPy, Dash, Plotly |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\activate`.

Each project has its own usage notes. The source datasets are not included, so the expected input filename and columns must be provided before running a script or notebook.

## Repository structure

```text
.
├── bar-chart-top10/
├── interactive-dash-app/
├── volcano-plot/
└── requirements.txt
```

## Limitations

These projects are exploratory visualizations. They do not implement a complete statistical analysis pipeline, input validation, or automated tests. The notebook retains its original output cells and a Colab-specific input path.
