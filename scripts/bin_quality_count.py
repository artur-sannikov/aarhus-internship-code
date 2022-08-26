"""
This script accepts a CheckM output tsv file, contamination, and completeness 
thresholds, and returns the number of bins with higher (or equal) completeness and lower contamination..
"""

import argparse
import pandas as pd

# Create parser
parser = argparse.ArgumentParser(
    description="This script accepts a CheckM output tsv file, contamination, and completeness \
        thresholds, and returns the number of bins with higher (or equal) completeness and lower contamination.\
        Default values are 50 for completeness and 10 for contamination."
)

# Add arguments
parser.add_argument("-i", "--input", required=True, help="Input CheckM output tsv file")
parser.add_argument(
    "--completeness", default=50, help="Completeness threshold, inclusive"
)
parser.add_argument(
    "--contamination", default=10, help="Contamination threshold, exclusive"
)
parser.add_argument("--output", "-o", help="If required, save bin names to a file")

# Parse arguments
args = parser.parse_args()


def filter_dataset():
    """
    Return the number of bins with >= input completeness and < input contamination, and print out their names.
    """
    # Open dataset
    input_df = pd.read_table(args.input)

    # Filter by contaminaton and completeness
    filtered_df = input_df[
        (input_df["Completeness"] >= float(args.completeness))
        & (input_df["Contamination"] < float(args.contamination))
    ]

    print(
        f"The number of bins with higher (or equal) completeness and lower contamination is {filtered_df.shape[0]} out of {input_df.shape[0]}."
    )
    print("These bins are")
    print(f"{filtered_df['Bin Id']}")

    # Save bins to a file
    filtered_df["Bin Id"].to_csv(args.output, header=None, index=None)


filter_dataset()
