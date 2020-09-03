from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten



real_mtr  = np.load ('matrix_real.npy')
false_mtr = np.load ('matrix_false.npy') 

type1 = np.ones (len(real_mtr))
type2 = np.zeros (len(false_mtr))

print ('Number of positives: ', len(real_mtr))
print ('Number of negatives: ', len(false_mtr))

mtr = np.concatenate((real_mtr, false_mtr))
tp  = np.concatenate((type1, type2))

x_train, x_test, y_train, y_test = train_test_split(mtr, tp)


x_train = x_train.reshape(-1,20,20,1)
x_test = x_test.reshape(-1,20,20,1)


model = Sequential()
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(20,20,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=3)

y_pred = model.predict(x_test)

y_pred = (y_pred > 0.5).astype(int)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))