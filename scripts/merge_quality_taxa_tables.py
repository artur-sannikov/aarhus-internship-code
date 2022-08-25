"""Merge classification and quality information."""

import pandas as pd


def merge_df(ds_quality, ds_taxonomy):
    """
    Merge big quality dataset and taxonomic dataset.
    """
    # Read datasets
    df_quality = pd.read_csv(ds_quality)
    df_taxonomy = pd.read_table(ds_taxonomy)

    # Extract relevant columns from taxonomic table
    df_taxonomy = df_taxonomy[["user_genome", "classification"]]

    # Merge tables
    df_merged = df_taxonomy.merge(
        df_quality, left_on="user_genome", right_on="Bin Id"
    ).drop(columns=["user_genome"])

    # Rearrange columns for better readability (first Bin Id, second classification, and last quality metrics)
    df_merged = df_merged[
        [
            "Bin Id",
            "classification",
            "Completeness",
            "Contamination",
            "# contigs",
            "Largest contig",
            "Total length",
            "N50",
            "L50",
        ]
    ]

    return df_merged


kaloevig_merged = merge_df(
    "kaloevig_quality_table.csv", "gtdbtk.bac120.summary_kaloevig.tsv"
)
loegten_merged = merge_df(
    "loegten_quality_table.csv", "gtdbtk.bac120.summary_loegten.tsv"
)

# Save to csv files
kaloevig_merged.to_csv("kaloevig_taxa_quality_table.csv", index=False)
loegten_merged.to_csv("loegten_taxa_quality_table.csv", index=False)
