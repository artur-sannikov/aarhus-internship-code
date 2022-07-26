from Bio import SeqIO
import time
import argparse

# Starting time
start = time.time()

# Create the parser
parser = argparse.ArgumentParser(
    prog="Sequence duplicates remover",
    description="Removes duplicated sequences by their ids from a FASTA file",
)

# Add parser arguments
parser.add_argument("-i", "--input_fasta", help="Input FASTA file", required=True)
parser.add_argument("-o", "--output_file", help="Output file", required=True)

# Parse the arguments
args = parser.parse_args()

seen = set()
records = []

for record in SeqIO.parse(args.input_fasta, "fasta"):
    if record.id not in seen:
        seen.add(record.id)
        records.append(record)


# Writing to a FASTA file
SeqIO.write(records, args.output_file, "fasta")

# Compute run time
end = time.time()
print(f"Run time is {(end - start)/60}")
