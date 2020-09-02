import random
import sys
import os
import numpy as np
from astroquery.vizier import Vizier
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rc('font', family='serif')
mpl.rcParams.update({'font.size': 12})
mpl.rcParams.update({'legend.labelspacing':0.25, 'legend.fontsize': 12})
mpl.rcParams.update({'errorbar.capsize': 4})



Vizier.ROW_LIMIT = 30000

catalogs = Vizier.get_catalogs('J/A+A/618/A93/members')

print (catalogs[0]['Cluster'])

print (len(catalogs))


cluster_name = []
tr_matrix = []

#create dir for examples
if not os.path.exists('examples'):
    os.makedirs('examples')
if not os.path.exists('neg_examples'):
    os.makedirs('neg_examples')


t = 0
for i in range (0, len(catalogs[0]['Cluster'])):

	if len(cluster_name) > 0 and cluster_name[-1] == catalogs[0]['Cluster'][i]:

		#print (str(catalogs[0]['Gmag'][i]), str(catalogs[0]['BP-RP'][i]))

		if (str(catalogs[0]['Gmag'][i]).find('--') < 0) and (str(catalogs[0]['BP-RP'][i]).find('--') < 0):
			#print ('NAN')
			#sys.exit(0)

			gm.append (float(catalogs[0]['Gmag'][i]))		
			cl.append (float(catalogs[0]['BP-RP'][i]))  
		


	if len(cluster_name) > 0 and cluster_name[-1] != catalogs[0]['Cluster'][i]:

		#plt.scatter (cl, gm)
		#plt.xlabel(r'$B_p - R_p$ (mag)')
		#plt.ylabel(r'$G$ (mag)')
		#plt.ylim([18,8])
		#plt.savefig('Alessi_12.pdf')
		#plt.show()

		#gmax = np.max (gm)
		#gmin = np.min (gm)
		#cmax = np.max (cl)
		#cmin = np.min (cl)


		#print ('Values: ', gmax, gmin, cmax, cmin)

		H, xedges, yedges = np.histogram2d (cl, gm, bins=20, density=True)

		plt.imshow(H, interpolation='nearest')
		plt.savefig ('examples/'+str(cluster_name[-1])+'.jpg')
		plt.cla()
		plt.clf()
		plt.close()
		#plt.show()

		H1 = H.reshape ((400))

		for j in range (0, len(H1)):

			print ('--> ', j, H1[j])

		tr_matrix.append (H1)
	
		#break

		gm = []
		cl = []
		cluster_name.append(catalogs[0]['Cluster'][i])


	if len(cluster_name) == 0:
		gm = []
		cl = []
		cluster_name.append(catalogs[0]['Cluster'][i])


	print (i, catalogs[0]['Cluster'][i])


np.save ('matrix_real', tr_matrix)

false_mtr = []

print('Number of positive samples: ', len(tr_matrix))

for i in range (0,len(tr_matrix)):

	n = int(random.uniform (30, 500)) ## number of stars

	gm = np.random.uniform (8, 18, size = n)	
	cl = np.random.uniform (0, 5, size = n)

	H, xedges, yedges = np.histogram2d (cl, gm, bins=20, density=True)

	if i <= 10:
		plt.imshow(H, interpolation='nearest')
		plt.savefig (f'neg_examples/{i}.jpg')
		plt.cla()
		plt.clf()
		plt.close()

	H1 = H.reshape ((400))

	false_mtr.append (H1)

np.save ('matrix_false', false_mtr)

#	if i < 3:

#		plt.imshow(H, interpolation='nearest')
#		plt.show ()

	
	



