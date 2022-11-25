# I am extending yesterday's script in order to
# visualize the gene expression data using matplotlib.

# I am visualizing the five genes with the highest 
# average expression when infected with influenza, 
# comparing male vs. female mice.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
NUM_GENES = 5
INFECTION = "InfluenzaA"

# Read file
url = "https://github.com/Bioconductor/bioconductor-teaching/raw/master/data/GSE96870/rnaseq.csv"
genex = pd.read_csv(url, index_col='gene')

# Find five genes with the highest average expression when infected with influenza
influenza_exp = genex.loc[genex["infection"]==INFECTION]
exp_by_gene = influenza_exp.groupby("gene")["expression"]
sorted_by_mean = exp_by_gene.agg(mean="mean").sort_values("mean", ascending=False)
top_genes = sorted_by_mean[:NUM_GENES].index
top_gene_exp = genex.loc[genex.index.isin(top_genes)]

# Get male vs female expression of top genes
male_means = top_gene_exp.loc[top_gene_exp["sex"]=="Female"].groupby("gene")["expression"].mean()
female_means = top_gene_exp.loc[top_gene_exp["sex"]=="Male"].groupby("gene")["expression"].mean()

# Make a bar chart comparing the gene expression of male vs female mice
ind = np.arange(NUM_GENES)
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(ind, male_means, width, color='blue')
rects2 = ax.bar(ind + width, female_means, width, color='pink')

# add some text for labels, title and axes ticks
ax.set_ylabel('Gene counts')
ax.set_title('Most highly expressed genes in influenza-infected mice')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(top_genes)
ax.legend((rects1[0], rects2[0]), ('Male', 'Female'))

fig.savefig('genex_influenza.png')