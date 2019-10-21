from keras.models import Sequential, modal_load
from keras.layers import Dense, Activation
from keras import optimizers
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard, ModelCheckpoint
from time import gmtime, strftime
import time


model = Sequential()

(x_train, y_train), (x_test, y_test) = mnist.load_data()


x_test = x_test.reshape(10000, 784)
