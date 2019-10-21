from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras import losses, optimizers
from keras.datasets import mnist
from keras.utils import np_utils
import matplotlib.pyplot as plt
from time import gmtime, strftime
import time, os

#meilleur fichier avec la derniere metrique 
filename = 'sauvgarde/weights.10-0.99.hdf5'

model = Sequential()
model = load_model(filename)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784)
y_test = np_utils.to_categorical(y_test, 10)


score = model.evaluate(x_test, y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
