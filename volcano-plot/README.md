# Volcano Plot of Differential Protein Expression

`volcano_plot.py` plots log2 fold change against `-log10(p-value)` and colors points using configurable p-value and fold-change thresholds.

## Expected input

The script currently reads `Differential_results .csv` from the working directory. The table must contain:

- `p_value`
- `log2FC`

## Run

From the project directory:

```bash
cd volcano-plot
python volcano_plot.py
```

The dataset is not included. The default thresholds are `p < 0.05` and `|log2FC| > 1`.
