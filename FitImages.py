# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:16:53 2020

@author: JohnnyGS
"""

#Importación de librerías necesarias.
import sys
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.keras import backend as K

#Limpieza de sesiones anteriores.
K.clear_session()

#Declaración de variables.
data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

epocas = 3
altura, longitud = 100, 100
batch_size = 30
pasos = 80
pasos_validacion = 200
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (3,3)
tamano_filtro2 = (2,2)
tamano_pool = (2,2)
clases = 2
lr = 0.005

#Tipo de entrenamiento a realizar.
entrenamiento_DataGen = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.3,
    zoom_range = 0.3,
    horizontal_flip = True
)

#Validación.
validacion_DataGen = ImageDataGenerator(
    rescale = 1./255    
)

#Modificación de las imágenes de entrenamiento y validación.
imagen_entrenamiento = entrenamiento_DataGen.flow_from_directory(
    data_entrenamiento,
    target_size = (altura,longitud),
    batch_size = batch_size,
    class_mode = 'categorical'
)

imagen_validacion = validacion_DataGen.flow_from_directory(
    data_validacion,
    target_size = (altura,longitud),
    batch_size = batch_size,
    class_mode = 'categorical'     
)

#Creación del modelo.
conv = Sequential()

conv.add(Convolution2D(
    filtrosConv1,
    tamano_filtro1,
    padding = 'same',
    input_shape = (altura,longitud,3),
    activation = 'relu'
))

conv.add(MaxPooling2D(
    pool_size = tamano_pool
))

conv.add(Convolution2D(
    filtrosConv2,
    tamano_filtro2,
    padding = 'same',
    activation = 'relu'
))

conv.add(MaxPooling2D(
    pool_size = tamano_pool    
))

conv.add(Flatten())

conv.add(Dense(
    256,
    activation = 'relu'    
))

conv.add(Dropout(
    0.5
))

conv.add(Dense(
    clases,
    activation = 'softmax'
))

#Compilación del modelo.
conv.compile(
    loss = 'categorical_crossentropy',
    optimizer = optimizers.Adam(learning_rate=lr),
    metrics = ['accuracy']
)

#Entrenamiento del modelo.
conv.fit(
    imagen_entrenamiento,
    steps_per_epoch = pasos,
    epochs = epocas,
    validation_data = imagen_validacion,
    validation_steps = pasos_validacion    
)

dir = './modelo'

if not os.path.exists(dir):
    os.mkdir(dir)
    
#Guardado del modelo.
conv.save('./modelo/modelo.h5')
conv.save_weights('./modelo/pesos.h5')