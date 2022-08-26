"""This script filters sequences from a FASTA file based on a list of input contig ids."""

from Bio import SeqIO
import argparse

# Create the parser
parser = argparse.ArgumentParser(
    description="Filter sequences from a FASTA file based on a list of input contig ids."
)

# Add the arguments
parser.add_argument("--input_fasta", "-i", required=True, help="Input FASTA file.")
parser.add_argument(
    "--id_file", required=True, help="List of contig ids to extract from FASTA file."
)
parser.add_argument("--output_file", "-o", required=True, help="Output file.")

# Parse arguments
args = parser.parse_args()

input_file = args.input_fasta
id_file = args.id_file
output_file = args.output_file

with open(id_file) as id_handle:
    wanted = set(line.rstrip("\n").split(None, 1)[0] for line in id_handle)
print(f"Found {len(wanted)} unique identifiers in {id_file}.")

records = (r for r in SeqIO.parse(input_file, "fasta") if r.id in wanted)
count = SeqIO.write(records, output_file, "fasta")

print(f"Saved {count} records from {input_file} to {output_file}.")

# Count the number of the filtered ids that were not found in the input file
if count < len(wanted):
    print(f"Warning: {len(wanted) - count} IDs were not found in {input_file}.")
