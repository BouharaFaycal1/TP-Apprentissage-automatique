

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard, ModelCheckpoint
from time import gmtime, strftime
import time
import pandas as pnd
import numpy
from sklearn.model_selection import train_test_split
# fix random seed for reproducibility












dataset =pnd.read_csv('acoustique_voy_orales_20loc_ESTER_NCCFr_contexte_freqLex_distCentroide.csv',sep='\t', usecols=['voyelle', 'F1', 'F2', 'F3', 'F4','Z1', 'Z2', 'f0'])

y = dataset.voyelle
X = dataset.drop('voyelle', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)


dict= [0:'a', 1:'e', 2:'u',3:'o',4:'y',5:'',6:'',]

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()

model.add(Dense(200, input_dim=784, activation='softsign'))

model.add(Dense(200, activation='softsign'))

model.add(Dense(10, activation='softmax'))

model.compile(loss='binary_crossentropy',optimizer='adadelta',metrics=["accuracy"])

X_train = X_train.reshape(60000, 8)
X_test = X_test.reshape(10000, 8)


