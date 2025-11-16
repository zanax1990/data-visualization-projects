"""Plotly Dash application for real-time ocular health exploration."""
from __future__ import annotations

import dash
from dash import Dash, Input, Output, dcc, html
import pandas as pd
import plotly.express as px

from data_utils import DISEASE_COLUMNS, correlation_columns, load_ocular_data, melt_disease_long, run_clustering


def build_figures(df: pd.DataFrame) -> tuple:
    corr = df[correlation_columns()].corr()
    corr_fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu",
        zmin=-1,
        zmax=1,
        aspect="auto",
        title="Correlation matrix",
    )

    cluster_df, _pca, _model = run_clustering(df)
    cluster_fig = px.scatter(
        cluster_df,
        x="PC1",
        y="PC2",
        color="Cluster",
        symbol="Sex",
        hover_data=["PatientID", "Age", "PrimaryDiagnosis"],
        title="Patient subgroup structure",
    )
    return corr_fig, cluster_fig, cluster_df


def build_app() -> Dash:
    df = load_ocular_data()
    long_df = melt_disease_long(df)
    corr_fig, cluster_fig, cluster_df = build_figures(df)

    app = dash.Dash(__name__)
    app.title = "Ocular Health Dashboard"

    min_age = df["Age"].min()
    max_age = df["Age"].max()

    app.layout = html.Div(
        [
            html.H1("Schwann Cell & Ocular Disease Explorer"),
            html.P(
                "Interactively explore demographics, diagnoses, and Schwann cell metrics derived from the ODIR-5K study."
            ),
            html.Div(
                [
                    html.Label("Filter patients by age"),
                    dcc.RangeSlider(
                        id="age-range",
                        min=min_age,
                        max=max_age,
                        step=1,
                        allowCross=False,
                        value=[min_age, max_age],
                        marks={int(min_age): str(int(min_age)), int(max_age): str(int(max_age))},
                    ),
                ],
                className="control-panel",
            ),
            html.Div(
                [
                    html.Label("Highlight a diagnosis"),
                    dcc.Dropdown(
                        id="disease-select",
                        options=[{"label": d, "value": d} for d in DISEASE_COLUMNS],
                        value=DISEASE_COLUMNS[0],
                        clearable=False,
                    ),
                ]
            ),
            dcc.Graph(id="correlation-heatmap", figure=corr_fig),
            html.Div(
                [
                    dcc.Graph(id="age-boxplot"),
                    dcc.Graph(id="schwann-violin"),
                ],
                className="split-row",
            ),
            dcc.Graph(id="age-regeneration-scatter"),
            dcc.Graph(id="cluster-graph", figure=cluster_fig),
        ],
        className="container",
    )

    @app.callback(
        Output("age-boxplot", "figure"),
        Output("schwann-violin", "figure"),
        Output("age-regeneration-scatter", "figure"),
        Input("age-range", "value"),
        Input("disease-select", "value"),
    )
    def update_patient_plots(age_range, disease):  # type: ignore[override]
        min_age, max_age = age_range
        age_mask = (df["Age"] >= min_age) & (df["Age"] <= max_age)
        filtered_df = df[age_mask]
        filtered_long = long_df[(long_df["Age"] >= min_age) & (long_df["Age"] <= max_age)]

        box_fig = px.box(
            filtered_long,
            x="Disease",
            y="Age",
            color="Disease",
            title="Age distribution by diagnosis",
        )

        violin_fig = px.violin(
            filtered_long[filtered_long["Disease"] == disease],
            x="Disease",
            y="SchwannCellDensity",
            box=True,
            points="all",
            title=f"Schwann cell density • {disease}",
        )

        scatter_fig = px.scatter(
            filtered_df,
            x="Age",
            y="RegenerationRate",
            color="PrimaryDiagnosis",
            symbol="Sex",
            hover_data=["PatientID", "SchwannCellDensity"],
            title="Age vs. corneal nerve regeneration",
        )
        return box_fig, violin_fig, scatter_fig

    return app


def main() -> None:
    app = build_app()
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
