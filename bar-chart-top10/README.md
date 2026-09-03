# Top Differentially Expressed Proteins

`bar_chart.py` compares mean expression values for the ten proteins with the smallest p-values in a supplied results table.

## Expected input

Place `Significant_Proteins_p0.05.csv` in this directory. The script expects:

- `p_value`
- `mean_WT`
- `mean_JR`
- `ProteinName`

## Run

From the repository root:

```bash
python bar-chart-top10/bar_chart.py
```

The dataset is not included. The script displays the chart interactively and does not save an output file.
