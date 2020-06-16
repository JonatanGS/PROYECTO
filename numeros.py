# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:32:59 2020

@author: JohnnyGS
"""

#Importación de librerías necesarias.
import numpy as np
import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

#Creación de imágenes y etiquetas de entrenamiento y validación.
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

#Normalización de píxeles de 0 - 255 a 0 - 1.
train_images = (train_images/255)
test_images = (test_images/255)

#Flatten de 28x28 a 784.
train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))

#Creación del modelo de red neuronal.
modelo = Sequential()
modelo.add(Dense(64,activation = 'relu',input_dim=784))
modelo.add(Dense(64,activation = 'relu'))
modelo.add(Dense(10,activation = 'softmax'))

#Compilación del modelo con el optimizador y pérdida.
modelo.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

#Entrenamiento del modelo.
modelo.fit(
    train_images,
    to_categorical(train_labels),
    epochs = 5,
    batch_size = 32
)

#Imágenes a usar dentro del array de test.
prediccion = modelo.predict(test_images[40:45])

#Mostrar resultado esperado y etiquetas correspondientes a las imágenes.
print()
print(np.argmax(prediccion,axis = 1))
print(test_labels[40:45])

#Mostrar representación del número.
for i in range (40, 45):
    imagen = test_images[i]
    imagen = np.array(imagen)
    pixeles = imagen.reshape((28,28))
    plt.imshow(pixeles)
    plt.show()