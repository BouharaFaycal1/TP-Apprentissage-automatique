

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard, ModelCheckpoint
from time import gmtime, strftime
import time

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#path = 'home/nas02a/etudiants/inf/uapv1601675/Donnees_itinerantes/sauvgarde/'+'weights.hdf5'

path = 'sauvgarde/'+ 'weights.{epoch:02d}-{val_acc:.2f}.hdf5'

tensorboard= TensorBoard(log_dir="logs/{}".format(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())),histogram_freq=0, write_graph=True, write_images=True)


#28*28 pixel 



model = Sequential()

model.add(Dense(200, input_dim=784, activation='softsign'))

model.add(Dense(200, activation='softsign'))

model.add(Dense(10, activation='softmax'))


#
model.compile(loss='binary_crossentropy',optimizer='adadelta',metrics=["accuracy"])



y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)


#affichage d'image
'''
image = x_train[0]
label = y_train[0]
plt.title('Label is {label}'.format(label=label))
plt.imshow(image, cmap='gray')
plt.show()
'''




x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

modelCheckPoint = ModelCheckpoint(path, monitor='val_acc', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)

model.fit(x_train, y_train, nb_epoch=10, verbose=1,validation_data=(x_test, y_test), callbacks=[modelCheckPoint])

#tensorboard.callbacks.ModelCheckpoint(filepath, monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=5)



score = model.evaluate(x_test, y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])



