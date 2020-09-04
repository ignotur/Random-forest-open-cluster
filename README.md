# Machine learning applied to open cluster identification

[![Made at #AstroHackWeek](https://img.shields.io/badge/Made%20at-%23AstroHackWeek-8063d5.svg?style=flat)](http://astrohackweek.org/)

Code to verify if a collection of stars found in the Gaia database is an open cluster.
Clustering algorithms (e.g. DBSCAN) returns tens of cluster candidates for every few square degrees of the sky area when they are applied to the Gaia DR2 database data.
In reality some of these cluster candidates are not open clusters but rather are fluctuations of the Galactic disk stellar population.
These collections of stars are expected to have very different ages, absorptions and metallicities. 
In this repository we train random forest and convolutional neural network to distiungush between actual open cluster and general Galactic disk population. 

# Table of contents:
1. [Open clusters](#open-clusters)
2. [Gaia](#gaia)
3. [Dataset for first iteration](#dataset-used-for-first-iteration-of-this-project)
4. [Evaluation metrics](#evaluation-metrics)
5. [Next steps](#next-steps)
6. [Files description](#files-description)
7. [References](#references)
    
# Open clusters:
group of stars (up to several thousand) formed from a single molecular cloud and having approximately the same age.

<img crossorigin="anonymous" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/VISTA_Finds_Star_Clusters_Galore.jpg/800px-VISTA_Finds_Star_Clusters_Galore.jpg" class="jpg" alt="" width="289" height="251" style="">

You may have seen such open clusters in the sky in the constellation Taurus... It's M45 or the Pleiades!

<img crossorigin="anonymous" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Pleiades_large.jpg/800px-Pleiades_large.jpg" class="jpg" alt="Pleiades large.jpg" width="348" height="251" style="">

Another types of clusters which can potentially be found in the Sky are globular clusters and young stellar clusters. Globular clusters contain from hundred thousands to a few millions of stars. There are approximately 150 globular clusters in our Galaxy and all of them are known. Young stellar clusters are objects typically embedded in gas and dust and cannot be seen in the Gaia data.

## Typical features of open clusters:

### 1) Similar chemical composition 

In articles on astronomy, you can see the terms "abundance" and "metallicity". The first term is usually used to define the amount of a chemical element in relation to the amount of such an element in the Sun, but can be defined differently. The second term usually refers to the ratio of the abundance of Fe in a star (object) to the abundance of Fe in the Sun, but can be defined differently. 

Stars in the open clusters are born from the same gas cloud in a single episode of star formation, so they all are expected to have the same metallicity.

### 2) Located either in the galactic disk or near it:

The younger the open cluster the further away from the galactic center and the older ones go beyond the disk. (in spiral galaxies). 

### 3) Star formation:

After the collapse and fragmentation of a giant molecular cloud, young stars appear. The hottest stars of the spectral class O-B form H II regions around them, where new stars are formed.

### 4) Gravitationally bound group of stars:

The stars in open clusters are connected by gravity and move together in space, located about the same distance from the observer. (This means that the parallax <img src="https://latex.codecogs.com/gif.latex?\pi" title="\pi" /> and proper motion <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /> of stars within open clusters must be similar.)

If the gravitational connection is lost, but the stars still move in the same direction at similar speeds, then this group of stars is called the stellar association.
Cluster could get gravitationally unbound when the gas and dust component is lost, also massive stars explodes as supernova. The cluster could lose stars due to the tidal forces from the Galactic disk.

### Hertzsprung–Russell diagram

is a powerful diagnostical tool in the stellar astronomy. The absolute magnitude of a star (y-axis) is an indications of the star size and mass (surface gravity) while the stellar colour (x-axis) shows stellar temperature. Stars spends most of their lives at the core nuclear burning stage where exists a unique relation between stellar mass and its temperature. This relation can be seen as the nearly stright line in the Hertzsprung–Russell diagram and is called the main sequence. Stars at the top of main sequence burn the nuclear fuel much faster than stars at the bottom of the main sequence. Therefore if stellar population was born at the same time the main sequence starts to disappear from the top. The Hertzsprung–Russell diagram shows us the age of the cluster (which also indicates the type of cluster: open, globular, etc.) using the characteristic deviation from the main sequence (MS) and the initial main sequence.

<img crossorigin="anonymous" src="https://upload.wikimedia.org/wikipedia/commons/2/27/Open_cluster_HR_diagram_ages.gif" class="gif" alt="" style="">

# Gaia

Global Astrometric Interferometer for Astrophysics are made by ESA (European Space Agency)

Space telescope have worked in the optical wavelength range.
The main goal is to create a 3D map of the stars in our Milky Way Galaxy. The Gaia provides 5 element astrometry solution (parallax, proper motion and stellar coordianates) as well as the photometric measurements for stars.

<img crossorigin="anonymous" src="https://upload.wikimedia.org/wikipedia/en/f/f7/Gaia_insignia.png" class="png" alt="Gaia mission insignia">

## GAIA DATA RELEASE 2 (GAIA DR2)

[Description](https://www.cosmos.esa.int/web/gaia/dr2)

## Dataset used for first iteration of this project

(reference file: [load_data.ipynb](https://github.com/ignotur/Random-forest-open-cluster/blob/master/load_data.ipynb))

From catalog: [A+A/618/A93](https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=+J%2FA%2BA%2F618%2FA93%2Fmembers&-from=nav&-nav=cat%3AJ%2FA%2BA%2F618%2FA93%26tab%3A%7BJ%2FA%2BA%2F618%2FA93%2Fmembers%7D%26key%3Asource%3DJ%2FA%2BA%2F618%2FA93%2Fmembers%26HTTPPRM%3A%26-out.max%3D1000%26-out.form%3DHTML+Table%26-oc.form%3Dsexa%26#adapt)[1](https://arxiv.org/abs/1805.08726)

We filter stars for which Gaia didn't measure magnitude or colour

# Evaluation metrics
We use RandomForestClassifier in sklearn

1. For parameters max_depth=2, random_state=0 

Accuracy score on test set:

0.9382113821138212

Confusion matrix:
[[265  38]
 [  0 312]]
 

2. For parameters max_depth=20, random_state=0 

Accuracy score on test set:
0.9951219512195122

Confusion matrix:
[[300   3]
 [  0 312]]


# Next steps

1. Cross validation and optimisation of the hyperparameters of the random forest. 
2. Get additional evaluation metrics (accuracy score, precision, recall, F1-score, etc.) on training and test sets, and decide on the meaningful ones to optimize for.

# Files description
* data - contains: npy files with data and examples of plots either true or non clusters
* example notebooks - contains: jupyter notebooks
* methods script - contains: scripts of our method
You can start from here:
example_notebooks/pull_clusters.ipynb - requests information about cluster membership from catalogue and bin Herzprung-Russell
diagram into 400 2D bins (20 bins for color and 20 bins for G magnitude),
example_notebooks/random_forest.ipynb - reads data and trains a Random Forest
example_notebooks/cnn.ipynb - reads data and trains a Convolutional neural network



# References
[1.](https://arxiv.org/abs/1805.08726) A Gaia DR2 view of the Open Cluster population in the Milky Way
