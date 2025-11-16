"""Generate exploratory plots for the ocular health project."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data_utils import (
    DISEASE_COLUMNS,
    correlation_columns,
    load_ocular_data,
    melt_disease_long,
    run_clustering,
)

OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")


def _save_current(fig: plt.Figure, filename: str) -> None:
    path = OUTPUT_DIR / filename
    fig.tight_layout()
    fig.savefig(path, dpi=300)
    plt.close(fig)
    print(f"Saved {path}")


def create_correlation_heatmap(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    corr = df[correlation_columns()].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=ax)
    ax.set_title("Demographic & Disease Correlations")
    _save_current(fig, "correlation_heatmap.png")


def create_age_boxplot(long_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(data=long_df, x="Disease", y="Age", ax=ax)
    sns.stripplot(data=long_df, x="Disease", y="Age", color="black", size=3, alpha=0.6, ax=ax)
    ax.set_title("Age distribution for each diagnosis")
    _save_current(fig, "age_by_disease_boxplot.png")


def create_schwann_violin(long_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.violinplot(
        data=long_df,
        x="Disease",
        y="SchwannCellDensity",
        ax=ax,
        inner="quartile",
        cut=0,
    )
    ax.set_ylabel("Schwann Cell Density (cells/mm)")
    ax.set_title("Schwann cell distribution by diagnosis")
    _save_current(fig, "schwann_density_violin.png")


def create_age_regeneration_scatter(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(
        data=df,
        x="Age",
        y="RegenerationRate",
        hue="PrimaryDiagnosis",
        style="Sex",
        ax=ax,
    )
    ax.set_ylabel("Corneal nerve regeneration rate")
    ax.set_title("Age vs. regeneration speed")
    _save_current(fig, "age_vs_regeneration.png")


def create_cluster_plot(cluster_df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(
        data=cluster_df,
        x="PC1",
        y="PC2",
        hue="Cluster",
        style="PrimaryDiagnosis",
        palette="Set2",
        s=80,
        ax=ax,
    )
    ax.set_title("Patient subgroups (PCA + k-means)")
    _save_current(fig, "cluster_scatter.png")


def main() -> None:
    df = load_ocular_data()
    long_df = melt_disease_long(df)
    cluster_df, _pca, _model = run_clustering(df)

    create_correlation_heatmap(df)
    create_age_boxplot(long_df)
    create_schwann_violin(long_df)
    create_age_regeneration_scatter(df)
    create_cluster_plot(cluster_df)


if __name__ == "__main__":
    main()
