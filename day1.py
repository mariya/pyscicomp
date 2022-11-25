# My field is bioinformatics, and I will be working with gene expression data. 
# Here I am applying Day 1 Pandas basics to read a genex dataset and
# to show the min, max and mean expression values per gene.

import pandas as pd

# Read file
url = "https://github.com/Bioconductor/bioconductor-teaching/raw/master/data/GSE96870/rnaseq.csv"
genex = pd.read_csv(url, index_col='gene')

# Explore 
print("\n\nFIRST ROWS")
print(genex.head())
print("\n\nDESCRIBE DATASET")
print(genex.describe())

# Group expression by gene
exp_by_gene = genex.groupby("gene")["expression"]

# Print attributes
print("\n\nMINIMUM EXPRESSION VALUES BY GENE")
print(exp_by_gene.min())

print("\n\nMAXMIMUM EXPRESSION VALUES BY GENE")
print(exp_by_gene.max())

print("\n\nMEAN EXPRESSION VALUES BY GENE")
print(exp_by_gene.mean())