import sklearn.cluster
import numpy as np
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN
import sys
import itertools
from scipy import linalg
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from astroquery.vizier import Vizier
import astropy.units as u
import astropy.coordinates as coord
from astropy.coordinates import Angle
Vizier.ROW_LIMIT = -1

table = Vizier.query_region(coord.SkyCoord(ra=272.96, dec=-18.53932068, unit=(u.deg, u.deg), frame='icrs'),catalog='J/A+A/618/A93/table1', radius=Angle(4, "deg"))
tm=table[0]

t = Table.read('tst.hdf', format='hdf5')

print (tm['RAJ2000'][0])


#print (t['ra'][0])

#sys.exit(0)

X = np.array([t['ra'], t['dec'], t['parallax'], t['pmra'], t['pmdec'] ])

Xfull = np.array([t['ra'], t['dec'], t['parallax'], t['pmra'], t['pmdec'], t['phot_g_mean_mag'], t['bp_rp'] ])

Xnew = np.transpose(X)

imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(Xnew)
Xnn = imp.transform(Xnew)

Xnew = StandardScaler().fit_transform(Xnn)

Xfull_new = np.transpose(Xfull)


print ('Number of stars: ', len(t['ra']))

clustering = DBSCAN(eps=0.0711, min_samples=17).fit(Xnew)


labels = clustering.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print ('Number of clusters: ', n_clusters_)

unique_labels = set(labels)

unique_labels.remove(-1)

known_cluster = [] ## it says if the given cluster is known as an open cluster

nonclusters = [3,6,11,13,14,15,16,19,20,21,22,23,25,26,27,28,29,30,32,38,39,40,41,43,44,45,46,47,48,51,52,53]

false_mtr = []

for k in unique_labels:

	class_member_mask = (labels == k)

	cluster_items = Xfull_new[class_member_mask]

	ra_cl  = np.array (t['ra'])
	dec_cl = np.array (t['dec']) 
	par_cl = np.array (t['parallax'])
	pmra_cl = np.array (t['pmra'])
	pmdec_cl = np.array (t['pmdec']) 
	gm_cl    = np.array (t['phot_g_mean_mag'])
	gc_cl    = np.array (t['bp_rp'])

	ra_cl   = ra_cl    [class_member_mask]
	dec_cl  = dec_cl   [class_member_mask]
	par_cl  = par_cl   [class_member_mask]
	pmra_cl = pmra_cl  [class_member_mask]
	pmdec_cl= pmdec_cl [class_member_mask]
	gm_cl   = gm_cl    [class_member_mask]
	gc_cl   = gc_cl    [class_member_mask]

	#gm_cl = gm_cl[gm_cl]
	#gc_cl = gc_cl[gc_cl]

	gm_cl1 = []
	gc_cl1 = []

	for jc in range (0, len(gm_cl)): ## filter out nan values (when Gaia could not measure the color)

		#print ('--> ', gm_cl[jc], gc_cl[jc])

		if (gc_cl[jc] != gc_cl[jc] or gm_cl[jc] != gm_cl[jc]):
			print ('Nan')	
		else:	
			gm_cl1.append (gm_cl[jc])
			gc_cl1.append (gc_cl[jc])

	#sys.exit(0)

		#if gm_cl[jc]


	ra_cl_mean    = np.mean (ra_cl)
	dec_cl_mean   = np.mean (dec_cl)
	par_cl_mean   = np.mean (par_cl)
	pmra_cl_mean  = np.mean (pmra_cl)
	pmdec_cl_mean = np.mean (pmdec_cl)

	print ('k = ', k, len(ra_cl), ra_cl_mean, dec_cl_mean, par_cl_mean, pmra_cl_mean, pmdec_cl_mean)
	

	flag_found = 0
	for j in range (0, len (tm['RAJ2000'])):

		if (abs(ra_cl_mean - tm['RAJ2000'][j]) < 0.15) and (abs(dec_cl_mean - tm['DEJ2000'][j]) < 0.15) and (abs(par_cl_mean - tm['plx'][j]) < 0.3) and (abs(pmra_cl_mean - tm['pmRA'][j]) < 0.5) and (abs(pmdec_cl_mean - tm['pmDE'][j]) < 0.5):
			flag_found = 1
			break
	known_cluster.append (flag_found)

	print ('Found? ', flag_found)

	if k in nonclusters:
		print ('k = ', k, 'we found it in the list')
		H, xedges, yedges = np.histogram2d (gc_cl1, gm_cl1, bins=20, density=True)

		H1 = H.reshape ((400))

		false_mtr.append (H1)

#	if k > 5:
#		sys.exit(0)

#	plt.scatter (ra_cl, dec_cl, s=4)

	#if flag_found == 0:

	#	plt.scatter (gc_cl, gm_cl)
	#	plt.title (str(k))
	#	plt.ylim([np.max(gm_cl), np.min(gm_cl)])	
	#	plt.show()	

	#if k > 7:
	#	sys.exit(0)

#plt.scatter (tm['RAJ2000'], tm['DEJ2000'], s=24)
#plt.show()

print ('We have managed to identify: ', np.sum(known_cluster), ' out of ', len(tm['RAJ2000']))

print ('Size of noncluster list: ', len(false_mtr))

np.save ('matrix_false_nonclusters', false_mtr)

