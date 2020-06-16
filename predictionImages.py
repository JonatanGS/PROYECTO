# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:59:17 2020

@author: JohnnyGS
"""

#Importación de las librerías necesarias.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

#Declaración de las variables.
longitud, altura = 100, 100
modelo = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'
ruta = './data/validacion/gato/hoky.jpg'
conv = load_model(modelo)
conv.load_weights(pesos)

#Carga de la imagen y tipo.
def predict(file):
    x = load_img(
        file,
        target_size = (longitud,altura)
    )
    
    x = img_to_array(x)
    
    x = np.expand_dims(
        x,
        axis = 0
    )
    
    arreglo = conv.predict(x)
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)
    
    print()
    
    if respuesta == 0:
        print(chr(27)+"[1;33m"+'Gato')
    elif respuesta == 1:
        print(chr(27)+"[1;33m"+'Perro')
    return respuesta

#Obtener resultado.
predict(ruta)
plt.imshow(mpimg.imread(ruta))