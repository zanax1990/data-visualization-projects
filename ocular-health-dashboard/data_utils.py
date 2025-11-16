"""Utility functions for the ocular health analytics workflow."""
from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

DATA_PATH = Path(__file__).parent / "data" / "ocular_health_sample.csv"
DISEASE_COLUMNS = [
    "Diabetic Retinopathy",
    "Glaucoma",
    "Macular Degeneration",
    "Cataract",
]


def load_ocular_data() -> pd.DataFrame:
    """Load the ocular health dataset with helper columns."""
    df = pd.read_csv(DATA_PATH)
    df["SexBinary"] = df["Sex"].map({"F": 0, "M": 1})
    diagnosis = df[DISEASE_COLUMNS]
    has_diagnosis = diagnosis.sum(axis=1) > 0
    primary = diagnosis.idxmax(axis=1)
    df["PrimaryDiagnosis"] = primary.where(has_diagnosis, "No Finding")
    return df


def melt_disease_long(df: pd.DataFrame) -> pd.DataFrame:
    """Return a patient-level long table filtered to positive diagnoses."""
    long_df = df.melt(
        id_vars=["PatientID", "Age", "Sex", "SchwannCellDensity", "RegenerationRate"],
        value_vars=DISEASE_COLUMNS,
        var_name="Disease",
        value_name="Diagnosis",
    )
    return long_df[long_df["Diagnosis"] == 1]


def correlation_columns() -> List[str]:
    return [
        "Age",
        "SexBinary",
        "SchwannCellDensity",
        "RegenerationRate",
        *DISEASE_COLUMNS,
    ]


def run_clustering(
    df: pd.DataFrame,
    *,
    features: List[str] | None = None,
    n_clusters: int = 4,
) -> Tuple[pd.DataFrame, PCA, KMeans]:
    """Return dataframe annotated with PCA components and cluster labels."""
    if features is None:
        features = [
            "Age",
            "SexBinary",
            "SchwannCellDensity",
            "RegenerationRate",
            *DISEASE_COLUMNS,
        ]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[features])
    model = KMeans(n_clusters=n_clusters, n_init="auto", random_state=42)
    clusters = model.fit_predict(scaled)
    pca = PCA(n_components=2, random_state=42)
    pcs = pca.fit_transform(scaled)
    cluster_df = df.copy()
    cluster_df["Cluster"] = clusters
    cluster_df["PC1"] = pcs[:, 0]
    cluster_df["PC2"] = pcs[:, 1]
    return cluster_df, pca, model


__all__ = [
    "DATA_PATH",
    "DISEASE_COLUMNS",
    "load_ocular_data",
    "melt_disease_long",
    "correlation_columns",
    "run_clustering",
]
