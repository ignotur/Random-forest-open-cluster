from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
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

print (len(real_mtr))
print (len(false_mtr))

mtr = np.concatenate((real_mtr, false_mtr))
tp  = np.concatenate((type1, type2))

x_train, x_test, y_train, y_test = train_test_split(mtr, tp)


#plt.imshow(real_mtr[0].reshape((20,20)), interpolation='nearest')
#plt.show()

#plt.imshow(false_mtr[0].reshape((20,20)), interpolation='nearest')
#plt.show()

#for i in range (0, len (tp)):

#	print (tp[i])

n_smp = len(x_train)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))