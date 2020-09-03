import sklearn.cluster
from astroquery.gaia import Gaia
import numpy as np
from astropy.io import fits
from astropy.table import Table

ra = 272.96
dec = -18.53932068
angle_first = 4

job = Gaia.launch_job_async("SELECT ra, dec, parallax, pmra, pmdec, phot_g_mean_mag, bp_rp \
                             FROM gaiadr2.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),  CIRCLE('ICRS',"+str(ra) +" , "+str(dec) +" , "+ str(angle_first)+" )) \
                             and abs(parallax_over_error) > 5 and parallax > 0.1 and phot_g_mean_mag < 18")

r = job.get_results()
#print r

#for i in ra

r.write('tst.hdf', path='./tst.hdf',format='hdf5')


