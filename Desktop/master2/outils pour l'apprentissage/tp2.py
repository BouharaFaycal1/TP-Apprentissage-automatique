from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt







#cahrgement des donnees
(x_train, y_train), (x_test, y_test) = mnist.load_data()	
model = Sequential()
model.add(Dense(200, input_dim=784, activation='tanh'))

model.add(Dense(200, activation='tanh'))

model.add(Dense(10, activation='softmax'))
model.compile(loss='mse',optimizer='sgd',metrics=["accuracy"])







image = x_train[0]
label = y_train[0]
plt.title('Label is {label}'.format(label=label))
plt.imshow(image, cmap='gray')
plt.show()



x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)


y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)


model.fit(x_train, y_train, nb_epoch=15, verbose=1,validation_data=(x_test, y_test))




score = model.evaluate(x_test, y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])

#la metrique obtenu au debut  est de 0.88(activation = tanh , loss=mse et optimizer= sgd )
 




