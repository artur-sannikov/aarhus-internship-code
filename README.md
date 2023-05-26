# Internship scripts, Jupyter notebooks,`csv` files, and conda environments
A collection of scripts, Jupyter notebooks, and `csv` files for my internship at Aarhus University. The goal of the project was to study the microbial community and potential interaction partners of [cable bacteria](https://en.wikipedia.org/wiki/Cable_bacteria). The resulting master's  thesis "Marine sediments: interaction partners of cable bacteria revealed through metagenomics" is availabe at [this link](https://thesis.unipd.it/handle/20.500.12608/34057) or directly as a [PDF](https://thesis.unipd.it/bitstream/20.500.12608/34057/1/Sannikov_Artur.pdf).

## Scripts
1. `bin_quality_count.py` — return the number of bins above specified thresholds of completeness and contamination.
2. `extract_fasta.py` — filter sequences from a FASTA file based on a list of input contig ids and generate a filtered output file.
3. `merge_quality_taxa_tables.py` — merge datasets with taxonomic and quality information.
4. `remove_duplicate_seq.py` — remove duplicate sequences (having the same id) from a FASTA file.

## Jupyter notebooks
1. `big_quality_tables.ipynb` — combine bin ids and quality metrics of the Kalø Vig into two big tables, `kaloevig_quality_table.csv` and `loegten_quality_table.csv`.
2. `compute_abundance.ipynb` — compute abundances of genomic bins in the Kalø Vig and Løgten samples and add them to tables `kaloevig_taxa_quality_table.csv` and `loegten_taxa_quality_table.csv`.
3. `compute_electrothrix_communis_illumina_abundance.ipynb` — do the same operation as in 2 for the *Candidatus* Electrothrix communis RB sample.
4. `electrothrix_communis_illumina_taxa_quality_table.ipynb` — merge bin names, taxonomic information, completeness, and contamination values the *Candidatus* Electrothrix communis RB sample.
5. `fegenie_quality_blast.ipynb` — merge taxonomic classification, FeGenie output, quality metrics, protein hits, and bin abundance of all three samples into three sample-specific tables (`kaloevig_genes.csv`, `loegten_genes.csv`, `marine_gs_illumina_genes.csv`).
6. `fegenie_quality_table.ipynb` — merge taxonomic information FeGenie output, quality metrics of all three samples.
7. `figures.ipynb` — generate figures used in the thesis.
8. `interproscan_Dsr.ipynb` — display bin ids that contain either DsrA or DsrB protein.
9. `protein_hits.ipynb` — generate the tables with the number of protein hits of each protein in each bin of the Kalø Vig and Løgten sample.
10. `protein_hits_electrothrix_communis.ipynb` — perform the same operation as in 9 for the *Candidatus* Electrothrix communis RB sample.
11. `selecting_best_bins.ipynb` — select the best bins from either MetaDecoder or non-MetaDecoder approach.
12. `statistics.ipynb` — statistical comparison of genomic bins between the MetaDecoder and non-MetaDecoder approaches.

## `csv` files
1. `blast` directory — `csv` files containing BLAST outputs (for six extracellular electron transfer proteins) in [BLASTn output format 6](https://www.metagenomics.wiki/tools/blast/blastn-output-format-6).
2. `genes/fegenie` directory — FeGenie output tables containing "geneSummary" tables with information about found iron-related genes for all categories. For more information, refer to the [FeGenie tutorial](https://github.com/Arkadiy-Garber/FeGenie/wiki/Tutorial).
3. `genes` directory — files `kaloevig_genes.csv`, `loegten_genes.csv`, and `marine_gs_illumina_genes.csv` contain taxonomic information together with quality metrics, abundance, and numbers of protein hits.
4. `quality` directory — tables with quality information (i.e., completeness, contamination, N50, etc.) for the Kalø Vig and Løgten samples.
5. `taxonomy` directory — tables with genomic bins included in the phylogenetic tree as well as their related genomes from the [Genome Taxonomy Database](https://gtdb.ecogenomic.org/), release 07-RS207.

## Envs

Folder with environment `yml` files to generate environments used in this project. The environments are split into analysis categories:

1. Binning.
2. Genes — environments for tools related to genomic analyses.
3. Mapping.
4. QC and trimming.
5. Taxonomy.

To aid the reproducibility, virtually each tool run has its own environment (for example, CheckM runs in environment `binning/checkm.yml`).

To recreate an environment, use `conda` ([url](https://docs.conda.io/en/latest/)) or `mamba` ([url](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html)):

`conda env create --name envname --file=environment.yml`

