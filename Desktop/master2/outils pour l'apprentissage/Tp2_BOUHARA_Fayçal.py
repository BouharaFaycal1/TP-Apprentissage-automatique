from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt



#nom: BOUHARA Faycal



#cahrgement des donnees
(x_train, y_train), (x_test, y_test) = mnist.load_data()




#creation de mlp avec 2 couche cache avec 2OO neurones et 10 valeur en sortie sortie
#28*28 p= 784 dimension 
	
model = Sequential()


model.add(Dense(200, input_dim=784, activation='softsign'))

model.add(Dense(200, activation='softsign'))

model.add(Dense(10, activation='softmax'))


#
model.compile(loss='binary_crossentropy',optimizer='adadelta',metrics=["accuracy"])






#affichage d'image
image = x_train[0]
label = y_train[0]
plt.title('Label is {label}'.format(label=label))
plt.imshow(image, cmap='gray')
plt.show()


#28*28 = 784 pixel
#daans notre reseau de neurones nous avons 70000 donnees dont 6000 pour l'aprentissage et 10000 pour les tests
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

#nombre de classe est de 10 car nous avons 10 valeur de sortie dans notre reseau de neurones
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)


#plus on augmante le nombre epoch plus on aura un bon resultat 
model.fit(x_train, y_train, nb_epoch=15, verbose=1,validation_data=(x_test, y_test))


#accurency= 1 veut dire il n'y a pas d'erreur 
#la loss elle permet de corriger la valeur du neurone

score = model.evaluate(x_test, y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])

#la metrique obtenu au debut  est de 0.88(activation = tanh , loss=mse et optimizer= sgd )
#apres plusieurs modification du code  j'ai obtenu 0.9949 (activation = softsign ,  loss=  binary_crossentropy et optimizer= adadelta) 
 




