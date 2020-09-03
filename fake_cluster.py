'''
--------------------------------------------------------------------------------
Simple script to create fake cluster from isochrones.
Run as:
>> python fake_cluster.py <n>
where 'n' is the total number of stars desired in the fake cluster.
--------------------------------------------------------------------------------
'''

import numpy as np
import pandas as pd
from numpy import random
import sys, os
import matplotlib.pyplot as plt

# add dust extinction
def add_dust_extinction():
    pass

def hess( col, mag ):
    #histogram definition
    xyrange = [[-1,2],[-5,4.0]] # data range
    bins = [20,20] # number of bins
    thresh = 3 #density threshold

    # histogram the data
    hh, locx, locy = np.histogram2d(col, mag, range=xyrange, bins=bins)
    posx = np.digitize(col, locx)
    posy = np.digitize(mag, locy)

    #select points within the histogram
    ind = (posx > 0) & (posx <= bins[0]) & (posy > 0) & (posy <= bins[1])
    hhsub = hh[posx[ind] - 1, posy[ind] - 1]
    col1, mag1 = [], []
    hh[hh < thresh] = np.nan

    return hh, xyrange

def plotHessDiagram(fake_cluster_df):
	# xlim, ylim = [-0.5, 2], [4, -5]
    g = fake_cluster_df['G']
    b_p = fake_cluster_df['Bp']
    r_p = fake_cluster_df['Rp']

    # plotting
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    hh, xyrange = hess( b_p - r_p, g )
    im = ax.imshow( np.flipud(hh.T), cmap="viridis", extent= np.array(xyrange).flatten(),
                     interpolation='nearest', origin='upper', aspect="auto")
    cb = plt.colorbar(im, ax=ax)

    ax.set_xlabel('$B_{p} - R_{p}$')
    ax.set_ylabel('G')
    ax.invert_yaxis()
    outfile = "fake_cluster.png"
    fig.savefig(outfile, dpi=300)
    plt.show()


if __name__=='__main__':
    # no. of stars that you want in your cluster
    n = int(sys.argv[1])

    # cols = ['Zini', 'MH', 'logAge', 'Mini', 'int_IMF', 'Mass', 'logL',  'logTe',\
    #         'logg', 'label', 'McoreTP', 'C_O',  'period0', 'period1', 'pmode', 'Mloss',\
    #         'tau1m',  'X', 'Y', 'Xc', 'Xn', 'Xo', 'Cexcess', 'Z', 'mbolmag',\
    #         'Gmag', 'G_BPmag', 'G_RPmag']

    isochrone = np.loadtxt("isochrone.dat", comments="#")

    temp_list = np.arange( isochrone.shape[0] )
    np.random.shuffle( temp_list )			 #shuffles the elements of temp_list randomly
    subsetIdx = temp_list[ :n ]
    subsetIdx = np.array( subsetIdx )

    fake_cluster = isochrone[subsetIdx, -3:]
    col_names = ['G', 'Bp', 'Rp']

    # save the fake cluster in pandas dataframe
    fake_cluster_df = pd.DataFrame( fake_cluster, columns=col_names )
    outfile = "fake_cluster.csv"
    fake_cluster_df.to_csv( outfile )

    plotHessDiagram(fake_cluster_df)
