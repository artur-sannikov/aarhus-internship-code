# Internship scripts, Jupyter notebooks and `csv` files
A collection of scripts, Jupyter notebooks, and `csv` files for my internship at Aarhus University. The goal of the project was to study the microbial community and potential interaction partners of [cable bacteria](https://en.wikipedia.org/wiki/Cable_bacteria).

## Scripts
1. `bin_quality_count.py` — return the number of bins above specified thresholds of completeness and contamination.
2. `extract_fasta.py` — filter sequences from a fasta file based on a list of input contig ids and generate a filtered output file.
3. `merge_quality_taxa_tables.py` — merge datasets with taxonomic and quality information.
4. `remove_duplicate_seq.py` — remove duplicate sequences (having the same id) from a FASTA file.

## Jupyter notebooks
1. `big_quality_tables.ipynb` — combine bin ids and quality metrics of the Kalø Vig  into two big tables, `kaloevig_quality_table.csv` and `loegten_quality_table.csv`.
2. `compute_abundance.ipynb` — compute abundances of genomic bins in the Kalø Vig and Løgten samples and add them to tables `kaloevig_taxa_quality_table.csv` and `loegten_taxa_quality_table.csv`.
3. `compute_electrothrix_communis_illumina_abundance.ipynb` — do the same operation as in 2 for the `*Candidatus* Electrothrix communis RB` sample.
4. `electrothrix_communis_illumina_taxa_quality_table.ipynb` — merge bin names, taxonomic information, completeness, and contamination values the `*Candidatus* Electrothrix communis RB` sample.
5. `fegenie_quality_blast.ipynb` — merge taxonomic classification, FeGenie output, quality metrics, protein hits, and bin abundance of all three samples into three sample-specific tables (`kaloevig_genes.csv`, `loegten_genes.csv`, `marine_gs_illumina_genes.csv`).
6. `fegenie_quality_table.ipynb` — merge taxonomic information FeGenie output, quality metrics of all three samples.
7. `figures.ipynb` — generate figures used in the thesis.
8. `interproscan_Dsr.ipynb` — display bin ids which contain either DsrA or DsrB protein.
9. `protein_hits.ipynb` — generate the tables with the number of protein hits of each protein in each bin of the Kalø Vig and Løgten sample.
10. `protein_hits_electrothrix_communis.ipynb` — perform the same operation as in 9 for the *Candidatus* Electrothrix communis RB sample.
11. 
