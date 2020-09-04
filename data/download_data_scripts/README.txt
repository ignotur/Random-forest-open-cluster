# Note on downloading data

There are many ways to download/generate data. 
Besides the scripts on this folder, similar data can de generated using the notebooks to load data on `example_notebooks`.

## skr.py

This script downloads astrometric and photometric information from Gaia DR2 in a circular region RA = 272.96, DEC = -18.53932068 with radius of 4 degrees.
This information is stored in file tst.hdf
Typical number of requested stars ~600000.

### get_all_clusters.py

This scripts reads file tst.hdf and applies DBSCAN (unsupervised learning; clustering) to identify clusters candidates. The typical number of identified clusters is ~50.
After this step, the algorithms computes coordinate of found cluster candidates (as mean values for individual stellar members of the cluster) and compares them with known open clusters compiled in Cantat-Gaudin et al. (2018) article.

If a cluster is not found in this catalogue the program can either show its Hertzsprung-Russell diagram (uncomment lines 145-150) or if visual inspection was performed earlier (exist correct list nonclusters line 66), it adds nonclusters to a file which is used further in training the model.

