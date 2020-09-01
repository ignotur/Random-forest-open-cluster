from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from math import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rc('font', family='serif')
mpl.rcParams.update({'font.size': 12})
mpl.rcParams.update({'legend.labelspacing':0.25, 'legend.fontsize': 12})
mpl.rcParams.update({'errorbar.capsize': 4})


real_mtr  = np.load ('matrix_real.npy')
false_mtr = np.load ('matrix_false.npy') 

type1 = np.ones (len(real_mtr))
type2 = np.zeros (len(false_mtr))

print (len(real_mtr[0: -5]))
print (len(false_mtr[0: -5]))

mtr = np.concatenate((real_mtr[0: -5], false_mtr[0: -5]))
tp  = np.concatenate((type1[0: -5], type2[0: -5]))


#plt.imshow(real_mtr[0].reshape((20,20)), interpolation='nearest')
#plt.show()

#plt.imshow(false_mtr[0].reshape((20,20)), interpolation='nearest')
#plt.show()

#for i in range (0, len (tp)):

#	print (tp[i])

n_smp = len(tp)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(mtr, tp)


#for i in range (1, 5):

print ('Real:  ', clf.predict(real_mtr[-5:-1]))
print ('False: ', clf.predict(false_mtr[-5:-1]))


